"""Generate the exhaustive Chinese API reference from checked-in type stubs."""

from __future__ import annotations

import argparse
import ast
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable


PACKAGE_NAME = "unitree_sdk2_cpp"
REQUIRED_PARAMETER = object()


@dataclass(frozen=True)
class Parameter:
    name: str
    annotation: str
    default: str | object = REQUIRED_PARAMETER
    kind: str = "positional_or_keyword"

    def render(self, include_default: bool = True) -> str:
        prefix = "**" if self.kind == "varkw" else "*" if self.kind == "vararg" else ""
        result = prefix + self.name
        if self.annotation:
            result += f": {self.annotation}"
        if include_default and self.default is not REQUIRED_PARAMETER:
            result += f" = {self.default}"
        return result


@dataclass
class FunctionDoc:
    module: str
    owner: str | None
    name: str
    decorators: list[str]
    parameters: list[Parameter]
    returns: str
    docstring: str
    manifest: dict[str, Any]
    source_node: ast.FunctionDef
    cpp_member: dict[str, Any] | None = None

    @property
    def python_path(self) -> str:
        prefix = f"{self.module}.{self.owner}" if self.owner else self.module
        return f"{prefix}.{self.name}"

    @property
    def is_static(self) -> bool:
        return "staticmethod" in self.decorators

    @property
    def public_parameters(self) -> list[Parameter]:
        return [item for item in self.parameters if item.name not in {"self", "cls"}]

    @property
    def signature(self) -> str:
        parameters = ", ".join(item.render() for item in self.parameters)
        return f"def {self.name}({parameters}) -> {self.returns}"


@dataclass
class PropertyDoc:
    module: str
    owner: str
    name: str
    getter: ast.FunctionDef
    setter: ast.FunctionDef | None
    manifest: dict[str, Any]

    @property
    def python_path(self) -> str:
        return f"{self.module}.{self.owner}.{self.name}"

    @property
    def read_type(self) -> str:
        return annotation(self.getter.returns)

    @property
    def write_parameter(self) -> Parameter | None:
        if self.setter is None:
            return None
        parameters = function_parameters(self.setter)
        return next((item for item in parameters if item.name != "self"), None)

    @property
    def getter_signature(self) -> str:
        return f"@property\ndef {self.name}(self) -> {self.read_type}"

    @property
    def setter_signature(self) -> str | None:
        parameter = self.write_parameter
        if parameter is None:
            return None
        return (
            f"@{self.name}.setter\n"
            f"def {self.name}(self, {parameter.render()}) -> None"
        )


@dataclass
class AttributeDoc:
    name: str
    annotation: str


@dataclass
class EnumValueDoc:
    name: str
    value: str


@dataclass
class ClassDoc:
    module: str
    name: str
    bases: list[str]
    functions: list[FunctionDoc] = field(default_factory=list)
    properties: list[PropertyDoc] = field(default_factory=list)
    attributes: list[AttributeDoc] = field(default_factory=list)
    enum_values: list[EnumValueDoc] = field(default_factory=list)

    @property
    def python_path(self) -> str:
        return f"{self.module}.{self.name}"

    @property
    def is_enum(self) -> bool:
        return any(base.endswith("IntEnum") for base in self.bases)


@dataclass
class ModuleDoc:
    name: str
    functions: list[FunctionDoc] = field(default_factory=list)
    classes: list[ClassDoc] = field(default_factory=list)


@dataclass(frozen=True)
class GenerationStats:
    modules: int
    classes: int
    functions: int
    properties: int
    attributes: int
    manifest_entries: int


PARAMETER_DESCRIPTIONS = {
    "app_name": "应用名称，用于标识音频流或播放会话。允许值和命名规则以目标服务协议为准。",
    "callback": "收到数据或状态变化时调用的 Python 回调。回调签名必须与类型提示一致，并应快速返回。",
    "config_file": "CycloneDDS 配置文件路径；空字符串表示使用底层默认配置。",
    "content": "配置、请求或序列化内容。具体格式由对应服务协议定义。",
    "domain_id": "DDS Domain ID。只有使用兼容 domain 的参与者才能按预期互相发现。",
    "duration": "操作持续时间参数。精确单位、范围和默认行为以目标型号接口定义为准。",
    "enable_lease": "是否启用 SDK lease 机制；lease 的获得、续期和释放规则以服务协议为准。",
    "enable_proi_queue": "是否启用 SDK 中名为 `proi` 的队列选项；该名称沿用上游接口，具体行为需查对应头文件。",
    "flag": "布尔开关。`True` 和 `False` 的具体业务效果由当前方法定义。",
    "json": "JSON 风格字典，键和值必须满足对应 C++ `JsonMap` 数据结构的约束。",
    "message": "要写入 DDS 的消息实例；类型必须与 Publisher 构造时声明的消息类完全一致。",
    "message_type": "IDL 消息类本身，例如 `LowState`，不是 `LowState()` 实例。该类型必须存在于运行时注册表中。",
    "microsec": "等待时间，单位为微秒。具体超时结果以 SDK 方法约定为准。",
    "microseconds": "客户端请求超时，单位为微秒。",
    "name": "SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。",
    "network_interface": "DDS 使用的网络接口名称，例如 Linux 上的 `eth0` 或 `enp3s0`；必须按目标机实际网卡填写。",
    "other": "用于比较的另一个 Python 对象。类型不兼容时比较结果通常为 `False`。",
    "queue_length": "订阅队列长度。`0` 使用底层默认行为；更大值会允许更多积压，但也可能增加延迟和内存占用。",
    "seconds": "客户端请求超时，单位为秒。",
    "speaker_id": "语音合成说话人 ID。有效编号由机器人音频服务和固件决定。",
    "stream_id": "音频流标识符，用于区分同一应用下的播放流。",
    "text": "要处理的文本内容；编码、长度和语言支持由目标服务决定。",
    "topic": "DDS topic 名称。发布端和订阅端必须同时使用兼容的 topic、消息类型和 QoS。",
    "value": "要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。",
    "wait_microsec": "写操作允许等待的时间，单位为微秒；`0` 使用当前绑定的默认非额外等待行为。",
    "wait_timeout": "请求等待超时参数；精确单位沿用对应 C++ 接口定义。",
    "vx": "X 方向速度参数。坐标系、单位、符号和安全范围必须查目标型号运动协议。",
    "vy": "Y 方向速度参数。坐标系、单位、符号和安全范围必须查目标型号运动协议。",
    "vyaw": "偏航角速度参数。单位、符号和安全范围必须查目标型号运动协议。",
    "omega": "角速度参数。旋转轴、单位、符号和安全范围必须查目标型号运动协议。",
    "yaw": "偏航角或偏航目标参数。参考系、单位和范围必须查目标型号协议。",
    "x": "X 方向位置或分量参数。参考系、单位和范围必须查当前方法及目标型号协议。",
    "y": "Y 方向位置或分量参数。参考系、单位和范围必须查当前方法及目标型号协议。",
    "z": "Z 方向位置或分量参数。参考系、单位和范围必须查当前方法及目标型号协议。",
}

TOKEN_LABELS = {
    "api": "API",
    "app": "应用",
    "arm": "机械臂",
    "balance": "平衡",
    "brightness": "亮度",
    "callback": "回调",
    "config": "配置",
    "data": "数据",
    "fsm": "FSM",
    "height": "高度",
    "id": "ID",
    "ids": "ID 列表",
    "image": "图像",
    "lease": "lease",
    "mode": "模式",
    "name": "名称",
    "names": "名称列表",
    "phase": "相位",
    "request": "请求",
    "response": "响应",
    "sdk": "SDK",
    "silent": "静音状态",
    "speed": "速度",
    "state": "状态",
    "status": "状态",
    "stream": "流",
    "switch": "开关",
    "task": "任务",
    "timeout": "超时",
    "velocity": "速度",
    "volume": "音量",
}

EXACT_PURPOSES = {
    "unitree_sdk2_cpp.OsHelper.instance": "返回进程内的 `OsHelper` 单例。",
    "unitree_sdk2_cpp.OsHelper.get_uid": "返回当前进程用户的 Unix UID。",
    "unitree_sdk2_cpp.OsHelper.get_gid": "返回当前进程用户的 Unix GID。",
    "unitree_sdk2_cpp.OsHelper.get_user": "返回当前进程对应的用户名。",
    "unitree_sdk2_cpp.OsHelper.get_processor_number": "返回当前主机可见的处理器数量。",
    "unitree_sdk2_cpp.OsHelper.get_page_size": "返回当前主机的操作系统内存页大小。",
    "unitree_sdk2_cpp.OsHelper.get_hostname": "返回当前主机名。",
    "unitree_sdk2_cpp.channel.registered_message_types": "返回当前二进制扩展已经注册的 typed DDS 消息类型名。",
    "unitree_sdk2_cpp.channel.initialize": "使用 Domain ID 和网络接口初始化全局 DDS ChannelFactory。",
    "unitree_sdk2_cpp.channel.initialize_from_config": "使用 CycloneDDS 配置文件初始化全局 DDS ChannelFactory。",
    "unitree_sdk2_cpp.channel.release": "释放全局 DDS ChannelFactory 及其持有的底层资源。",
    "unitree_sdk2_cpp.channel.ChannelPublisher.init_channel": "创建并启动 Publisher 的底层 DDS 写通道。",
    "unitree_sdk2_cpp.channel.ChannelPublisher.close_channel": "关闭 Publisher 的底层 DDS 写通道。",
    "unitree_sdk2_cpp.channel.ChannelPublisher.write": "把一个类型匹配的消息样本写入 Publisher 对应的 DDS topic。",
    "unitree_sdk2_cpp.channel.ChannelSubscriber.init_channel": "创建并启动 Subscriber 的底层 DDS 读通道。",
    "unitree_sdk2_cpp.channel.ChannelSubscriber.close_channel": "关闭 Subscriber 的底层 DDS 读通道，并停止后续回调。",
}

EXACT_RETURN_DESCRIPTIONS = {
    "unitree_sdk2_cpp.OsHelper.instance": "进程内的 `OsHelper` 单例。",
    "unitree_sdk2_cpp.OsHelper.get_uid": "当前进程用户的 Unix UID。",
    "unitree_sdk2_cpp.OsHelper.get_gid": "当前进程用户的 Unix GID。",
    "unitree_sdk2_cpp.OsHelper.get_user": "当前进程对应的用户名。",
    "unitree_sdk2_cpp.OsHelper.get_processor_number": "当前主机可见的处理器数量。",
    "unitree_sdk2_cpp.OsHelper.get_page_size": "操作系统内存页大小，单位为字节。",
    "unitree_sdk2_cpp.OsHelper.get_hostname": "当前主机名。",
    "unitree_sdk2_cpp.channel.registered_message_types": "当前扩展已注册的 C++ DDS 消息类型名列表。",
}

EXACT_USAGE = {
    "unitree_sdk2_cpp.OsHelper.instance": "helper = OsHelper.instance()",
    "unitree_sdk2_cpp.OsHelper.get_uid": "uid = helper.get_uid()",
    "unitree_sdk2_cpp.OsHelper.get_gid": "gid = helper.get_gid()",
    "unitree_sdk2_cpp.OsHelper.get_user": "user = helper.get_user()",
    "unitree_sdk2_cpp.OsHelper.get_processor_number": "processor_count = helper.get_processor_number()",
    "unitree_sdk2_cpp.OsHelper.get_page_size": "page_size = helper.get_page_size()",
    "unitree_sdk2_cpp.OsHelper.get_hostname": "hostname = helper.get_hostname()",
    "unitree_sdk2_cpp.channel.registered_message_types": "message_type_names = registered_message_types()",
    "unitree_sdk2_cpp.channel.initialize": 'initialize(domain_id=0, network_interface="eth0")',
    "unitree_sdk2_cpp.channel.initialize_from_config": 'initialize_from_config(config_file="cyclonedds.xml")',
    "unitree_sdk2_cpp.channel.release": "release()",
}

EXACT_PROPERTY_DESCRIPTIONS = {
    "unitree_sdk2_cpp.channel.ChannelPublisher.topic": "Publisher 构造时保存的 DDS topic 名称，只读。",
    "unitree_sdk2_cpp.channel.ChannelPublisher.message_type_name": "Publisher 使用的已注册 C++ 消息类型名，只读。",
    "unitree_sdk2_cpp.channel.ChannelSubscriber.topic": "Subscriber 构造时保存的 DDS topic 名称，只读。",
    "unitree_sdk2_cpp.channel.ChannelSubscriber.message_type_name": "Subscriber 使用的已注册 C++ 消息类型名，只读。",
    "unitree_sdk2_cpp.channel.ChannelSubscriber.last_data_available_time": "底层记录的最近一次数据可用时间。其单位和时间基准以 SDK 实现为准。",
}


def annotation(node: ast.expr | None) -> str:
    return "Any" if node is None else ast.unparse(node)


def decorator_name(node: ast.expr) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return f"{decorator_name(node.value)}.{node.attr}"
    return ast.unparse(node)


def function_parameters(node: ast.FunctionDef) -> list[Parameter]:
    positional = [*node.args.posonlyargs, *node.args.args]
    defaults: list[ast.expr | object] = [REQUIRED_PARAMETER] * (
        len(positional) - len(node.args.defaults)
    ) + list(node.args.defaults)
    result = [
        Parameter(
            name=item.arg,
            annotation=(
                annotation(item.annotation) if item.annotation is not None else ""
            ),
            default=(
                REQUIRED_PARAMETER
                if default is REQUIRED_PARAMETER
                else ast.unparse(default)
            ),
            kind=(
                "positional_only"
                if index < len(node.args.posonlyargs)
                else "positional_or_keyword"
            ),
        )
        for index, (item, default) in enumerate(zip(positional, defaults, strict=True))
    ]
    if node.args.vararg:
        result.append(
            Parameter(
                node.args.vararg.arg,
                (
                    annotation(node.args.vararg.annotation)
                    if node.args.vararg.annotation is not None
                    else ""
                ),
                kind="vararg",
            )
        )
    for item, default in zip(node.args.kwonlyargs, node.args.kw_defaults, strict=True):
        result.append(
            Parameter(
                item.arg,
                annotation(item.annotation) if item.annotation is not None else "",
                REQUIRED_PARAMETER if default is None else ast.unparse(default),
                "keyword_only",
            )
        )
    if node.args.kwarg:
        result.append(
            Parameter(
                node.args.kwarg.arg,
                (
                    annotation(node.args.kwarg.annotation)
                    if node.args.kwarg.annotation is not None
                    else ""
                ),
                kind="varkw",
            )
        )
    return result


def module_name(stub_root: Path, path: Path) -> str:
    relative = path.relative_to(stub_root)
    parts = list(relative.with_suffix("").parts)
    if parts[-1] == "__init__":
        parts.pop()
    return ".".join([PACKAGE_NAME, *parts]) if parts else PACKAGE_NAME


def cpp_signature(item: dict[str, Any]) -> str:
    parameters = ", ".join(
        parameter["type"] for parameter in item.get("parameters", [])
    )
    suffix = " const" if item.get("is_const") else ""
    return f"{item['name']}({parameters}){suffix}"


def load_cpp_members(
    binding_root: Path,
) -> tuple[dict[tuple[str, str], dict[str, Any]], dict[str, dict[str, Any]]]:
    member_index: dict[tuple[str, str], dict[str, Any]] = {}
    class_index: dict[str, dict[str, Any]] = {}
    for filename in ("idl_inventory.json", "robot_inventory.json"):
        payload = json.loads(
            (binding_root / "generated" / filename).read_text(encoding="utf-8")
        )
        for cpp_class in payload["classes"]:
            cpp_name = (
                f"{cpp_class['namespace']}::{cpp_class['name']}"
                if cpp_class.get("namespace")
                else cpp_class["name"]
            )
            class_index[cpp_name] = cpp_class
            for member in [
                *cpp_class.get("constructors", []),
                *cpp_class.get("methods", []),
            ]:
                member_index[(cpp_name, cpp_signature(member))] = member
    return member_index, class_index


def cpp_doc_signature(docstring: str) -> str | None:
    match = re.search(r"C\+\+: (.+?)\.?$", docstring.strip())
    return match.group(1) if match else None


def select_manifest_entry(
    path: str,
    node: ast.FunctionDef,
    manifest_by_path: dict[str, list[dict[str, Any]]],
) -> dict[str, Any]:
    candidates = manifest_by_path.get(path, [])
    if not candidates:
        raise ValueError(f"No manifest entry for {path}")
    if len(candidates) == 1:
        return candidates[0]
    documented = cpp_doc_signature(ast.get_docstring(node) or "")
    if documented:
        matches = [
            item
            for item in candidates
            if documented == item["cpp_signature"]
            or documented.endswith("::" + item["cpp_signature"])
        ]
        if len(matches) == 1:
            return matches[0]
    parameter_types = [
        item.annotation
        for item in function_parameters(node)
        if item.name not in {"self", "cls"}
    ]
    typed_matches = [
        item
        for item in candidates
        if item.get("python_parameters") == parameter_types
    ]
    if len(typed_matches) == 1:
        return typed_matches[0]
    signature = FunctionDoc(
        module="",
        owner=None,
        name=node.name,
        decorators=[],
        parameters=function_parameters(node),
        returns=annotation(node.returns),
        docstring="",
        manifest={},
        source_node=node,
    ).signature
    raise ValueError(f"Ambiguous manifest entry for {path}: {signature}")


def parse_stubs(
    binding_root: Path,
) -> tuple[list[ModuleDoc], dict[str, Any], GenerationStats]:
    stub_root = binding_root / "stubs" / "src" / "unitree_sdk2_cpp-stubs"
    manifest = json.loads((stub_root / "api_manifest.json").read_text(encoding="utf-8"))
    manifest_by_path: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entry in manifest["entries"]:
        manifest_by_path[entry["python_path"]].append(entry)
    cpp_members, _ = load_cpp_members(binding_root)

    modules: list[ModuleDoc] = []
    documented_manifest_keys: Counter[tuple[str, str]] = Counter()
    function_count = 0
    property_count = 0
    attribute_count = 0

    for path in sorted(stub_root.rglob("*.pyi")):
        module = ModuleDoc(module_name(stub_root, path))
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in tree.body:
            if isinstance(node, ast.FunctionDef):
                python_path = f"{module.name}.{node.name}"
                entry = select_manifest_entry(python_path, node, manifest_by_path)
                member = cpp_members.get((entry["cpp_class"], entry["cpp_signature"]))
                module.functions.append(
                    FunctionDoc(
                        module=module.name,
                        owner=None,
                        name=node.name,
                        decorators=[
                            decorator_name(item) for item in node.decorator_list
                        ],
                        parameters=function_parameters(node),
                        returns=annotation(node.returns),
                        docstring=ast.get_docstring(node) or "",
                        manifest=entry,
                        source_node=node,
                        cpp_member=member,
                    )
                )
                documented_manifest_keys[(python_path, entry["cpp_signature"])] += 1
                function_count += 1
                continue
            if not isinstance(node, ast.ClassDef):
                continue

            cpp_class = ClassDoc(
                module=module.name,
                name=node.name,
                bases=[ast.unparse(item) for item in node.bases],
            )
            getters: dict[str, ast.FunctionDef] = {}
            setters: dict[str, ast.FunctionDef] = {}
            for member_node in node.body:
                if isinstance(member_node, ast.FunctionDef):
                    decorators = [
                        decorator_name(item) for item in member_node.decorator_list
                    ]
                    if "property" in decorators:
                        getters[member_node.name] = member_node
                        continue
                    if any(item.endswith(".setter") for item in decorators):
                        setters[member_node.name] = member_node
                        continue
                    python_path = f"{module.name}.{node.name}.{member_node.name}"
                    entry = select_manifest_entry(
                        python_path, member_node, manifest_by_path
                    )
                    cpp_member = cpp_members.get(
                        (entry["cpp_class"], entry["cpp_signature"])
                    )
                    cpp_class.functions.append(
                        FunctionDoc(
                            module=module.name,
                            owner=node.name,
                            name=member_node.name,
                            decorators=decorators,
                            parameters=function_parameters(member_node),
                            returns=annotation(member_node.returns),
                            docstring=ast.get_docstring(member_node) or "",
                            manifest=entry,
                            source_node=member_node,
                            cpp_member=cpp_member,
                        )
                    )
                    documented_manifest_keys[(python_path, entry["cpp_signature"])] += 1
                    function_count += 1
                elif isinstance(member_node, ast.AnnAssign) and isinstance(
                    member_node.target, ast.Name
                ):
                    cpp_class.attributes.append(
                        AttributeDoc(
                            member_node.target.id,
                            annotation(member_node.annotation),
                        )
                    )
                    attribute_count += 1
                elif isinstance(member_node, ast.Assign):
                    value = ast.unparse(member_node.value)
                    for target in member_node.targets:
                        if isinstance(target, ast.Name):
                            cpp_class.enum_values.append(EnumValueDoc(target.id, value))

            for property_name in getters:
                python_path = f"{module.name}.{node.name}.{property_name}"
                candidates = manifest_by_path.get(python_path, [])
                if len(candidates) != 1:
                    raise ValueError(
                        f"Expected one manifest entry for property {python_path}, "
                        f"found {len(candidates)}"
                    )
                entry = candidates[0]
                cpp_class.properties.append(
                    PropertyDoc(
                        module.name,
                        node.name,
                        property_name,
                        getters[property_name],
                        setters.get(property_name),
                        entry,
                    )
                )
                documented_manifest_keys[(python_path, entry["cpp_signature"])] += 1
                property_count += 1
            module.classes.append(cpp_class)

        if module.functions or module.classes:
            modules.append(module)

    expected_manifest_keys = Counter(
        (entry["python_path"], entry["cpp_signature"]) for entry in manifest["entries"]
    )
    if documented_manifest_keys != expected_manifest_keys:
        missing = expected_manifest_keys - documented_manifest_keys
        extra = documented_manifest_keys - expected_manifest_keys
        raise ValueError(
            "Documentation coverage mismatch: "
            f"missing={list(missing.elements())[:5]}, "
            f"extra={list(extra.elements())[:5]}"
        )

    stats = GenerationStats(
        modules=len(modules),
        classes=sum(len(module.classes) for module in modules),
        functions=function_count,
        properties=property_count,
        attributes=attribute_count,
        manifest_entries=len(manifest["entries"]),
    )
    return modules, manifest, stats


def anchor(value: str) -> str:
    value = re.sub(
        r"__([a-z0-9_]+?)__",
        lambda match: f"dunder-{match.group(1)}",
        value.lower(),
    )
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")


def md_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", "<br>")


def friendly_tokens(value: str) -> str:
    words = [TOKEN_LABELS.get(token, f"`{token}`") for token in value.split("_")]
    return " ".join(words)


def normalize_cpp_type(value: str) -> str:
    result = value.strip().lstrip(":")
    result = re.sub(r"\bconst\s+", "", result)
    result = re.sub(r"\s*&&?\s*$", "", result)
    return re.sub(r"\s+", " ", result).strip()


def cpp_type_constraint(value: str) -> str:
    normalized = normalize_cpp_type(value)
    integer_ranges = {
        "int8_t": "取值范围为 -128 到 127",
        "uint8_t": "取值范围为 0 到 255",
        "signed char": "通常取值范围为 -128 到 127",
        "unsigned char": "取值范围为 0 到 255",
        "int16_t": "取值范围为 -32768 到 32767",
        "uint16_t": "取值范围为 0 到 65535",
        "int32_t": "取值范围为 -2147483648 到 2147483647",
        "uint32_t": "取值范围为 0 到 4294967295",
        "int64_t": "取值范围为 -9223372036854775808 到 9223372036854775807",
        "uint64_t": "取值范围为 0 到 18446744073709551615",
        "bool": "只接受布尔语义",
    }
    if normalized in integer_ranges:
        return integer_ranges[normalized] + "。"
    array_match = re.match(r"std::array<(.+),\s*(\d+)>", normalized)
    if array_match:
        element_type, length = array_match.groups()
        element_constraint = cpp_type_constraint(element_type)
        suffix = f"；元素约束：{element_constraint}" if element_constraint else ""
        return f"底层是固定长度数组，写入序列必须正好包含 {length} 个元素{suffix}"
    vector_match = re.match(r"std::vector<(.+)>", normalized)
    if vector_match:
        element_constraint = cpp_type_constraint(vector_match.group(1))
        suffix = f"；元素约束：{element_constraint}" if element_constraint else ""
        return f"底层是可变长度 vector{suffix}"
    if normalized in {"float", "double"}:
        return "底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。"
    if normalized in {"std::string", "string"}:
        return "底层为字符串；长度、编码和允许值由具体协议决定。"
    return ""


def parameter_description(
    parameter: Parameter,
    cpp_parameter: dict[str, Any] | None,
) -> str:
    known = PARAMETER_DESCRIPTIONS.get(parameter.name)
    if known:
        result = known
    else:
        label = friendly_tokens(parameter.name)
        result = (
            f"传给该接口的 {label} 参数，Python 类型为 `{parameter.annotation}`。"
            "精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。"
        )
    if not cpp_parameter:
        return result
    cpp_name = cpp_parameter.get("name") or parameter.name
    cpp_type = cpp_parameter["type"]
    result += f" 对应 C++ 参数 `{cpp_name}: {cpp_type}`。"
    constraint = cpp_type_constraint(cpp_type)
    if constraint:
        result += " " + constraint
    return result


def function_purpose(function: FunctionDoc) -> str:
    exact = EXACT_PURPOSES.get(function.python_path)
    if exact:
        return exact
    if function.name == "__init__":
        return f"初始化 `{function.owner}` 实例。是否能实际构造取决于下方可用性状态。"
    if function.name == "__eq__":
        return "按底层 IDL 消息内容比较两个对象是否相等。"
    if function.name == "__ne__":
        return "按底层 IDL 消息内容比较两个对象是否不相等。"
    if function.name == "from_json":
        return "计划从 JSON 风格字典读取字段并更新当前 SDK 值对象。"
    if function.name == "to_json":
        return "计划把当前 SDK 值对象写入 JSON 风格字典。"
    if function.name in {"init", "initialize"}:
        return "初始化当前 SDK 对象所需的底层通道或服务资源。"
    if function.name.startswith(("get_", "check_", "is_", "has_")):
        operation = re.sub(r"^(get|check|is|has)_", "", function.name)
        return f"查询或检查 {friendly_tokens(operation)}。"
    if function.name.startswith("set_"):
        operation = function.name.removeprefix("set_")
        return f"设置 {friendly_tokens(operation)}。具体副作用和安全边界见下方状态。"
    if function.name.startswith("close"):
        return "关闭当前对象持有的底层资源。"
    if function.name.startswith("start"):
        return "启动对应 SDK 操作。具体副作用和安全边界见下方状态。"
    if function.name.startswith("stop"):
        return "请求停止对应 SDK 操作。该名称不等同于经过验证的物理急停。"
    return (
        f"对应 C++ SDK 操作 `{function.manifest['cpp_signature']}`。"
        "上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，"
        "精确语义需查目标型号协议。"
    )


def class_purpose(item: ClassDoc) -> str:
    if item.is_enum:
        return "SDK 整数枚举。枚举成员和值以目标版本头文件为准。"
    if item.module.startswith(f"{PACKAGE_NAME}.idl."):
        return "可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。"
    if item.name.endswith("Client"):
        return "Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。"
    if item.name.endswith("Parameter"):
        return "SDK 请求参数值类型；当前可能仅提供设计期签名。"
    if item.name.endswith(("Data", "State", "Status", "Meta", "Point")):
        return "SDK 数据值类型；公开字段和转换方法见下文。"
    if item.python_path == "unitree_sdk2_cpp.OsHelper":
        return "读取当前主机操作系统信息的单例辅助类。"
    if item.module == f"{PACKAGE_NAME}.channel":
        return "typed DDS 通道包装类。必须遵守初始化、启动、关闭和全局释放顺序。"
    return "SDK 类型签名预览。请逐项查看构造函数和方法的可用性。"


def status_note(entry: dict[str, Any]) -> str:
    status = entry["status"]
    safety = entry.get("safety", "UNCLASSIFIED")
    if status == "SIGNATURE_ONLY" and safety == "MOTION_COMMAND":
        return (
            "**`SIGNATURE_ONLY` / `MOTION_COMMAND`**：仅用于补全和静态检查。"
            "当前二进制没有该 Python 方法；不得按可执行运动接口使用。"
        )
    if status == "SIGNATURE_ONLY" and safety == "HARDWARE_SIDE_EFFECT":
        return (
            "**`SIGNATURE_ONLY` / `HARDWARE_SIDE_EFFECT`**：仅用于补全和静态检查。"
            "当前二进制没有该 Python 方法，未来实现还需单独评审硬件副作用。"
        )
    if status == "SIGNATURE_ONLY":
        return (
            f"**`SIGNATURE_ONLY` / `{safety}`**：当前只有设计期签名，"
            "不能假设已存在于运行时扩展。"
        )
    if safety == "READ_ONLY":
        if entry["python_path"].startswith("unitree_sdk2_cpp.OsHelper."):
            return (
                "**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现本机信息读取。"
                "该方法不初始化 DDS，也不访问机器人。"
            )
        return (
            "**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现只读查询。"
            "Robot Client 的服务端查询通常仍需匹配的 Linux 扩展、DDS、网络、"
            "机器人和服务；纯本地 getter 则不一定需要全部条件。"
        )
    if safety == "VALUE_TYPE":
        return "**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。"
    if safety == "DDS_LIFECYCLE":
        return (
            "**`AVAILABLE` / `DDS_LIFECYCLE`**：当前绑定源码已实现。"
            "该操作可能创建、使用或释放 DDS 资源。"
        )
    if safety == "MOTION_COMMAND":
        return (
            "**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人"
            "发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；"
            "不得从默认测试或未经确认的 Agent 流程调用。"
        )
    if safety == "HARDWARE_SIDE_EFFECT":
        return (
            "**`AVAILABLE` / `HARDWARE_SIDE_EFFECT`**：当前绑定源码已实现，调用可能修改"
            "机器人或服务状态、启动订阅或产生网络副作用。必须显式检查目标设备和返回状态。"
        )
    return (
        f"**`AVAILABLE` / `{safety}`**：当前绑定源码已实现；"
        "实际执行条件仍取决于平台和对应 SDK 环境。"
    )


def cpp_input_parameters(function: FunctionDoc) -> list[dict[str, Any]]:
    if not function.cpp_member:
        return []
    parameters = function.cpp_member.get("parameters", [])
    if function.manifest.get("binding_strategy") == "OUTPUT_WRAPPER":
        parameters = [
            item
            for item in parameters
            if not (
                "&" in item["type"] and not item["type"].lstrip().startswith("const ")
            )
        ]
    return parameters


def output_parameter_names(function: FunctionDoc) -> list[str]:
    if not function.cpp_member:
        return []
    if function.manifest.get("binding_strategy") != "OUTPUT_WRAPPER":
        return []
    return [
        item.get("name") or f"output_{index}"
        for index, item in enumerate(function.cpp_member.get("parameters", []), 1)
        if "&" in item["type"] and not item["type"].lstrip().startswith("const ")
    ]


def output_parameters(function: FunctionDoc) -> list[dict[str, Any]]:
    if not function.cpp_member:
        return []
    if function.manifest.get("binding_strategy") != "OUTPUT_WRAPPER":
        return []
    return [
        item
        for item in function.cpp_member.get("parameters", [])
        if "&" in item["type"] and not item["type"].lstrip().startswith("const ")
    ]


def split_tuple_annotation(value: str) -> list[str] | None:
    try:
        node = ast.parse(value, mode="eval").body
    except SyntaxError:
        return None
    if not isinstance(node, ast.Subscript):
        return None
    if not isinstance(node.value, ast.Name) or node.value.id != "tuple":
        return None
    if isinstance(node.slice, ast.Tuple):
        return [ast.unparse(item) for item in node.slice.elts]
    return [ast.unparse(node.slice)]


def return_rows(function: FunctionDoc) -> list[tuple[str, str, str]]:
    if function.name == "__init__":
        return [
            (
                "无",
                "None",
                "`__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。",
            )
        ]
    if function.returns == "None":
        return [
            ("无", "None", "该方法不返回 Python 值；失败可能表现为异常或底层状态变化。")
        ]
    output_names = output_parameter_names(function)
    output_items = output_parameters(function)
    tuple_parts = split_tuple_annotation(function.returns)
    if output_names and tuple_parts:
        names = ["status", *output_names]
        rows: list[tuple[str, str, str]] = []
        for index, type_name in enumerate(tuple_parts):
            name = names[index] if index < len(names) else f"value_{index}"
            description = (
                "SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。"
                if name == "status"
                else parameter_description(
                    Parameter(name, type_name),
                    output_items[index - 1] if index - 1 < len(output_items) else None,
                )
            )
            rows.append((f"[{index}] `{name}`", type_name, description))
        return rows
    if function.python_path.endswith(".write") and function.returns == "bool":
        return [
            (
                "返回值",
                "bool",
                "底层写操作是否被接受；不表示所有订阅者已处理，更不表示设备已经执行动作。",
            )
        ]
    if (
        function.returns == "int"
        and function.module.startswith(f"{PACKAGE_NAME}.robot")
        and function.name not in {"get_lease_id"}
    ):
        return [
            (
                "返回值",
                "int",
                "SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。",
            )
        ]
    exact = EXACT_RETURN_DESCRIPTIONS.get(function.python_path)
    if exact:
        return [("返回值", function.returns, exact)]
    return [
        (
            "返回值",
            function.returns,
            f"返回 `{function.returns}`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。",
        )
    ]


def source_location(function: FunctionDoc, binding_root: Path) -> str:
    if not function.cpp_member:
        return "由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。"
    location = function.cpp_member.get("location", {})
    filename = location.get("file")
    if not filename:
        return "上游 AST 清单未记录源文件位置。"
    path = Path(filename)
    try:
        display = path.relative_to(binding_root.parent)
    except ValueError:
        display = path
    line = location.get("line")
    return f"`{display}{f':{line}' if line else ''}`"


def usage_lhs(function: FunctionDoc) -> str:
    rows = return_rows(function)
    if function.returns == "None" or function.name == "__init__":
        return ""
    if len(rows) > 1:
        return ", ".join(row[0].split("`")[1] for row in rows) + " = "
    return "result = "


def call_arguments(parameters: Iterable[Parameter]) -> str:
    return ", ".join(
        (
            f"*{item.name}"
            if item.kind == "vararg"
            else (
                f"**{item.name}" if item.kind == "varkw" else f"{item.name}={item.name}"
            )
        )
        for item in parameters
    )


def usage_example(function: FunctionDoc) -> str:
    exact = EXACT_USAGE.get(function.python_path)
    if exact:
        return exact
    parameters = function.public_parameters
    arguments = call_arguments(parameters)
    status = function.manifest["status"]
    owner = function.owner
    if function.name == "__eq__":
        return "same = left == right"
    if function.name == "__ne__":
        return "different = left != right"
    if function.name == "__init__":
        normal = f"value = {owner}({arguments})"
        if status == "AVAILABLE":
            return normal
        declarations = ", ".join(
            item.render(include_default=False) for item in parameters
        )
        return (
            "from typing import TYPE_CHECKING\n\n"
            "if TYPE_CHECKING:\n"
            f"    def planned_construct({declarations}) -> {owner}:\n"
            f"        return {owner}({arguments})"
        )
    if owner is None:
        call = f"{function.name}({arguments})"
    else:
        target = owner if function.is_static else "obj"
        call = f"{target}.{function.name}({arguments})"
    statement = f"{usage_lhs(function)}{call}"
    if status == "AVAILABLE":
        return statement
    declarations = [f"obj: {owner}"] if owner and not function.is_static else []
    declarations.extend(item.render(include_default=False) for item in parameters)
    definition_parameters = ", ".join(declarations)
    body = statement
    if function.returns != "None":
        body = "return " + call
    return (
        "from typing import TYPE_CHECKING\n\n"
        "if TYPE_CHECKING:\n"
        f"    def planned_{function.name}({definition_parameters}) -> {function.returns}:\n"
        f"        {body}"
    )


def property_description(item: PropertyDoc) -> str:
    exact = EXACT_PROPERTY_DESCRIPTIONS.get(item.python_path)
    if exact:
        return exact
    result = (
        f"底层 `{item.manifest['cpp_class']}` 的 `{item.name}` 字段。"
        "类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。"
    )
    constraint = cpp_type_constraint(item.manifest["cpp_signature"])
    if constraint:
        result += " " + constraint
    return result


def function_notes(function: FunctionDoc) -> list[str]:
    notes = [
        "示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。"
    ]
    if any(item.default == "..." for item in function.public_parameters):
        notes.append(
            "默认值显示为 `...`，表示 C++ 声明存在默认参数，但当前 AST 清单没有保存其字面量；"
            "省略参数可使用上游默认行为。"
        )
    if function.manifest.get("binding_strategy") == "OUTPUT_WRAPPER":
        notes.append(
            "C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。"
        )
    if function.manifest["status"] == "SIGNATURE_ONLY":
        notes.append(
            "该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。"
        )
    if function.manifest.get("safety") == "MOTION_COMMAND":
        notes.append(
            "该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。"
        )
    if any("Callable" in item.annotation for item in function.public_parameters):
        notes.append(
            "回调可能由 SDK 工作线程触发；回调应快速返回、捕获异常，并通过线程安全队列移交耗时工作。"
        )
    return notes


def property_source(
    item: PropertyDoc, class_index: dict[str, dict[str, Any]], binding_root: Path
) -> str:
    cpp_class = class_index.get(item.manifest["cpp_class"])
    if not cpp_class:
        return "由 pybind11 手工绑定提供；manifest 未记录独立头文件行号。"
    property_name = item.name
    field_item = next(
        (
            field
            for field in cpp_class.get("fields", [])
            if field["name"].removesuffix("_") == property_name
        ),
        None,
    )
    if not field_item:
        return "上游 AST 清单未记录对应字段位置。"
    location = field_item.get("location", {})
    filename = location.get("file")
    if not filename:
        return "上游 AST 清单未记录对应字段位置。"
    path = Path(filename)
    try:
        display = path.relative_to(binding_root.parent)
    except ValueError:
        display = path
    line = location.get("line")
    return f"`{display}{f':{line}' if line else ''}`"


def module_title(name: str) -> str:
    titles = {
        PACKAGE_NAME: "系统辅助 API",
        f"{PACKAGE_NAME}.channel": "Typed DDS Channel API",
        f"{PACKAGE_NAME}.idl.go2": "Go2 IDL 消息",
        f"{PACKAGE_NAME}.idl.hg": "HG IDL 消息",
        f"{PACKAGE_NAME}.idl.hg_doubleimu": "HG Double-IMU IDL 消息",
        f"{PACKAGE_NAME}.idl.ros2": "ROS2 兼容 IDL 消息",
        f"{PACKAGE_NAME}.robot": "Robot 公共基础 API",
        f"{PACKAGE_NAME}.robot.a2": "A2 Robot API",
        f"{PACKAGE_NAME}.robot.as2": "AS2 Robot API",
        f"{PACKAGE_NAME}.robot.b2": "B2 Robot API",
        f"{PACKAGE_NAME}.robot.g1": "G1 Robot API",
        f"{PACKAGE_NAME}.robot.go2": "Go2 Robot API",
        f"{PACKAGE_NAME}.robot.h1": "H1 Robot API",
        f"{PACKAGE_NAME}.robot.h2": "H2 Robot API",
        f"{PACKAGE_NAME}.robot.r1": "R1 Robot API",
    }
    return titles.get(name, name)


def render_function(
    function: FunctionDoc,
    binding_root: Path,
    overload_index: int,
    overload_total: int,
) -> list[str]:
    suffix = f"（重载 {overload_index}/{overload_total}）" if overload_total > 1 else ""
    entry = function.manifest
    lines = [
        f'<a id="{anchor(function.python_path)}-{overload_index}"></a>',
        f"#### `{function.python_path}`{suffix}",
        "",
        function_purpose(function),
        "",
        "**签名**",
        "",
        "```python",
    ]
    if "overload" in function.decorators:
        lines.append("@overload")
    if function.is_static:
        lines.append("@staticmethod")
    lines.extend(
        [
            function.signature,
            "```",
            "",
            "**可用性与安全性**",
            "",
            status_note(entry),
            "",
        ]
    )
    cpp_inputs = cpp_input_parameters(function)
    lines.extend(["**参数**", ""])
    parameters = function.public_parameters
    if parameters:
        lines.extend(
            [
                "| 名称 | Python 类型 | 默认值 | 含义 |",
                "| --- | --- | --- | --- |",
            ]
        )
        for index, parameter in enumerate(parameters):
            cpp_parameter = cpp_inputs[index] if index < len(cpp_inputs) else None
            default = (
                "必填"
                if parameter.default is REQUIRED_PARAMETER
                else f"`{parameter.default}`"
            )
            lines.append(
                f"| `{parameter.name}` | `{md_escape(parameter.annotation)}` | {default} | "
                f"{md_escape(parameter_description(parameter, cpp_parameter))} |"
            )
    else:
        lines.append(
            "无参数。"
            if function.owner is None
            else "无显式参数。实例方法中的 `self` 由 Python 自动传入。"
        )
    lines.extend(
        ["", "**返回值**", "", "| 位置 | 类型 | 含义 |", "| --- | --- | --- |"]
    )
    for name, type_name, description in return_rows(function):
        lines.append(
            f"| {name} | `{md_escape(type_name)}` | {md_escape(description)} |"
        )
    lines.extend(
        [
            "",
            "**对应 C++**",
            "",
            f"- 类：`{entry['cpp_class']}`",
            f"- 签名：`{entry['cpp_signature']}`",
            f"- 绑定策略：`{entry.get('binding_strategy', '未单独标注')}`",
            f"- 声明位置：{source_location(function, binding_root)}",
            "",
            "**说明**",
            "",
        ]
    )
    lines.extend(f"- {note}" for note in function_notes(function))
    lines.extend(
        [
            "",
            "**用法**",
            "",
            "```python",
            usage_example(function),
            "```",
            "",
        ]
    )
    if entry["status"] == "SIGNATURE_ONLY":
        lines.extend(
            [
                "> [!CAUTION]",
                "> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。"
                "该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。",
                "",
            ]
        )
    elif entry.get("safety") == "READ_ONLY" and function.module.startswith(
        f"{PACKAGE_NAME}.robot"
    ):
        lines.extend(
            [
                "> [!NOTE]",
                "> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。",
                "",
            ]
        )
    elif entry.get("safety") in {"MOTION_COMMAND", "HARDWARE_SIDE_EFFECT"}:
        lines.extend(
            [
                "> [!CAUTION]",
                "> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、"
                "目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。",
                "",
            ]
        )
    return lines


def render_property(
    item: PropertyDoc,
    class_index: dict[str, dict[str, Any]],
    binding_root: Path,
) -> list[str]:
    lines = [
        f'<a id="{anchor(item.python_path)}"></a>',
        f"#### `{item.python_path}`",
        "",
        property_description(item),
        "",
        "**签名**",
        "",
        "```python",
        item.getter_signature,
    ]
    setter = item.setter_signature
    if setter:
        lines.extend(["", setter])
    lines.extend(["```", "", "**可用性与安全性**", "", status_note(item.manifest), ""])
    parameter = item.write_parameter
    lines.extend(["**参数**", ""])
    if parameter:
        lines.extend(
            [
                "| 名称 | Python 类型 | 含义 |",
                "| --- | --- | --- |",
                f"| `{parameter.name}` | `{md_escape(parameter.annotation)}` | "
                f"{md_escape(parameter_description(parameter, None))} |",
            ]
        )
    else:
        lines.append("该属性只读，没有 setter 参数。")
    lines.extend(
        [
            "",
            "**返回值**",
            "",
            "| 位置 | 类型 | 含义 |",
            "| --- | --- | --- |",
            f"| getter 返回值 | `{md_escape(item.read_type)}` | 返回属性当前值。"
            + (
                "数组、vector 和嵌套消息采用复制语义。 |"
                if item.read_type.startswith("list[")
                or (
                    item.module.startswith(f"{PACKAGE_NAME}.idl.")
                    and item.read_type not in {"bool", "int", "float", "str", "Any"}
                )
                else " |"
            ),
            "",
            "**对应 C++**",
            "",
            f"- 类：`{item.manifest['cpp_class']}`",
            f"- 字段类型：`{item.manifest['cpp_signature']}`",
            f"- 声明位置：{property_source(item, class_index, binding_root)}",
            "",
            "**用法**",
            "",
            "```python",
            f"current_value = obj.{item.name}",
        ]
    )
    if parameter:
        lines.append(f"obj.{item.name} = new_value")
    lines.extend(["```", ""])
    if parameter and (
        item.read_type.startswith("list[")
        or item.read_type not in {parameter.annotation}
    ):
        lines.extend(
            [
                "> [!TIP]",
                "> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。"
                "只修改 getter 返回的副本不会可靠地更新原 C++ 消息。",
                "",
            ]
        )
    return lines


def render_class(
    item: ClassDoc,
    binding_root: Path,
    class_index: dict[str, dict[str, Any]],
) -> list[str]:
    lines = [
        f'<a id="{anchor(item.python_path)}"></a>',
        f"### `{item.python_path}`",
        "",
        class_purpose(item),
        "",
        "**导入**",
        "",
        "```python",
        f"from {item.module} import {item.name}",
        "```",
        "",
    ]
    if item.bases:
        lines.extend([f"**基类**：{', '.join(f'`{base}`' for base in item.bases)}", ""])
    if item.enum_values:
        lines.extend(["**枚举成员**", "", "| 名称 | Stub 值 |", "| --- | --- |"])
        lines.extend(
            f"| `{value.name}` | `{value.value}` |" for value in item.enum_values
        )
        lines.append("")
    if item.attributes:
        lines.extend(
            [
                "**公开属性**",
                "",
                "| 名称 | Python 类型 | 含义 | 用法 |",
                "| --- | --- | --- | --- |",
            ]
        )
        for attribute in item.attributes:
            meaning = parameter_description(
                Parameter(attribute.name, attribute.annotation), None
            )
            lines.append(
                f"| `{attribute.name}` | `{md_escape(attribute.annotation)}` | "
                f"{md_escape(meaning)} | `value = obj.{attribute.name}` / "
                f"`obj.{attribute.name} = value` |"
            )
        lines.append("")
    if item.functions:
        lines.extend(
            [
                "**方法索引**",
                "",
                "| 方法 | Python 签名 | 状态 | 安全分类 |",
                "| --- | --- | --- | --- |",
            ]
        )
        totals = Counter(function.name for function in item.functions)
        positions: Counter[str] = Counter()
        for function in item.functions:
            positions[function.name] += 1
            display_name = function.name
            if totals[function.name] > 1:
                display_name += (
                    f"（重载 {positions[function.name]}/{totals[function.name]}）"
                )
            lines.append(
                f"| [`{display_name}`](#{anchor(function.python_path)}-{positions[function.name]}) | "
                f"`{md_escape(function.signature)}` | "
                f"`{function.manifest['status']}` | "
                f"`{function.manifest.get('safety', 'UNCLASSIFIED')}` |"
            )
        lines.append("")
    if item.properties:
        lines.extend(
            [
                "**属性索引**",
                "",
                "| 属性 | 读取类型 | 写入类型 | 状态 |",
                "| --- | --- | --- | --- |",
            ]
        )
        for property_item in item.properties:
            write_parameter = property_item.write_parameter
            write_type = write_parameter.annotation if write_parameter else "只读"
            lines.append(
                f"| [`{property_item.name}`](#{anchor(property_item.python_path)}) | "
                f"`{md_escape(property_item.read_type)}` | `{md_escape(write_type)}` | "
                f"`{property_item.manifest['status']}` |"
            )
        lines.append("")
    overloads = Counter(function.name for function in item.functions)
    positions: Counter[str] = Counter()
    for function in item.functions:
        positions[function.name] += 1
        lines.extend(
            render_function(
                function,
                binding_root,
                positions[function.name],
                overloads[function.name],
            )
        )
    for property_item in item.properties:
        lines.extend(render_property(property_item, class_index, binding_root))
    if (
        not item.functions
        and not item.properties
        and not item.attributes
        and not item.enum_values
    ):
        lines.extend(["该类型当前没有公开成员签名。", ""])
    return lines


def render_module(
    module: ModuleDoc,
    binding_root: Path,
    class_index: dict[str, dict[str, Any]],
) -> list[str]:
    lines = [
        f'<a id="{anchor(module.name)}"></a>',
        f"## {module_title(module.name)}",
        "",
        f"模块：`{module.name}`",
        "",
    ]
    if module.functions:
        imported_names = ", ".join(function.name for function in module.functions)
        lines.extend(
            [
                "### 模块函数导入",
                "",
                "```python",
                f"from {module.name} import {imported_names}",
                "```",
                "",
                "下面的函数用法片段假设已经完成上述导入。",
                "",
                "### 模块函数索引",
                "",
                "| 函数 | Python 签名 | 状态 | 安全分类 |",
                "| --- | --- | --- | --- |",
            ]
        )
        for function in module.functions:
            entry = function.manifest
            lines.append(
                f"| [`{function.name}()`](#{anchor(function.python_path)}-1) | "
                f"`{md_escape(function.signature)}` | `{entry['status']}` | "
                f"`{entry.get('safety', 'UNCLASSIFIED')}` |"
            )
        lines.append("")
    if module.classes:
        lines.extend(
            ["### 类索引", "", "| 类 | 公开函数签名 | 属性 |", "| --- | ---: | ---: |"]
        )
        for class_item in module.classes:
            lines.append(
                f"| [`{class_item.name}`](#{anchor(class_item.python_path)}) | "
                f"{len(class_item.functions)} | {len(class_item.properties)} |"
            )
        lines.append("")
    overloads = Counter(function.name for function in module.functions)
    positions: Counter[str] = Counter()
    for function in module.functions:
        positions[function.name] += 1
        lines.extend(
            render_function(
                function,
                binding_root,
                positions[function.name],
                overloads[function.name],
            )
        )
    for class_item in module.classes:
        lines.extend(render_class(class_item, binding_root, class_index))
    return lines


def render_document(
    modules: list[ModuleDoc],
    manifest: dict[str, Any],
    stats: GenerationStats,
    binding_root: Path,
) -> str:
    _, class_index = load_cpp_members(binding_root)
    lines = [
        "# Unitree SDK2 Python 完整 API 参考",
        "",
        "本参考采用常见科学计算库的 API Reference 组织方式：先按模块分类索引，"
        "再为每个类、函数和属性提供签名、参数、返回值、可用性、C++ 对应项和用法。"
        "学习路径和完整教程请先阅读 [从零开始指南](BEGINNER_GUIDE_ZH.md)。",
        "",
        "> [!WARNING]",
        "> 本文同时包含 `AVAILABLE` 和 `SIGNATURE_ONLY`。后者只是设计期类型签名。"
        "运动及硬件副作用方法已进入运行时绑定，但只表示接口可调用，不表示当前环境可安全执行；"
        "默认测试绝不会构造客户端、初始化 DDS 或发送机器人指令。",
        "",
        "> [!NOTE]",
        "> 本文件由 `generator/generate_api_docs.py` 从 `.pyi`、`api_manifest.json` "
        "和 Clang AST 清单生成。不要手工维护 API 条目；修改签名后应重新生成并运行测试。",
        "",
        "## 如何阅读本参考",
        "",
        "每个 API 条目包含以下部分：",
        "",
        "- **签名**：Python 类型检查器看到的准确调用形态；",
        "- **可用性与安全性**：区分当前实现和仅签名预览；",
        "- **参数**：Python 类型、默认值和能够从 SDK 定义可靠确认的含义；",
        "- **返回值**：包括 C++ 输出引用转换后的 Python 元组顺序；",
        "- **对应 C++**：原类、原签名、绑定策略和头文件位置；",
        "- **用法**：`AVAILABLE` 给出调用形态，`SIGNATURE_ONLY` 只给出 `TYPE_CHECKING` 计划代码。",
        "",
        "各条目中的代码是局部调用片段，不是完整脚本。类章节会先给出导入语句；"
        "`obj`、`helper`、`client`、`publisher`、`subscriber` 和参数变量表示调用者已经"
        "按业务规则创建、初始化并校验好的对象。",
        "",
        "参数名称无法表达单位、坐标系、范围或枚举值时，本文会明确要求查目标型号协议。"
        "这比根据名字猜测更可靠。",
        "",
        "## 覆盖统计",
        "",
        "| 项目 | 数量 |",
        "| --- | ---: |",
        f"| 有内容的 Python 模块 | {stats.modules} |",
        f"| 类和枚举 | {stats.classes} |",
        f"| 普通/重载函数签名 | {stats.functions} |",
        f"| Python 属性 | {stats.properties} |",
        f"| 公开数据属性 | {stats.attributes} |",
        f"| Manifest 条目 | {stats.manifest_entries} |",
        f"| `AVAILABLE` | {manifest['summary']['status']['AVAILABLE']} |",
        f"| `SIGNATURE_ONLY` | {manifest['summary']['status']['SIGNATURE_ONLY']} |",
        "",
        "一个 Python 属性在 manifest 中占一个条目，但下文会同时写出 getter 和 setter 签名。"
        "重载方法按不同 C++ 签名分别展开。",
        "",
        "## 分类索引",
        "",
        "| 分类 | Python 模块 | 函数 | 类 |",
        "| --- | --- | ---: | ---: |",
    ]
    for module in modules:
        lines.append(
            f"| {module_title(module.name)} | "
            f"[`{module.name}`](#{anchor(module.name)}) | "
            f"{len(module.functions)} | {len(module.classes)} |"
        )
    lines.extend(["", "---", ""])
    for index, module in enumerate(modules):
        lines.extend(render_module(module, binding_root, class_index))
        if index != len(modules) - 1:
            lines.extend(["---", ""])
    return "\n".join(lines).rstrip() + "\n"


def generate(binding_root: Path, output: Path) -> GenerationStats:
    modules, manifest, stats = parse_stubs(binding_root)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        render_document(modules, manifest, stats, binding_root),
        encoding="utf-8",
    )
    return stats


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--binding-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "docs" / "API_REFERENCE_ZH.md",
    )
    arguments = parser.parse_args()
    stats = generate(arguments.binding_root.resolve(), arguments.output.resolve())
    print(json.dumps(stats.__dict__, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
