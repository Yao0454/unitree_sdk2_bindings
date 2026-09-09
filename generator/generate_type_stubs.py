"""Generate PEP 561 preview stubs and an API availability manifest."""

from __future__ import annotations

import argparse
import json
import keyword
import re
from collections import Counter, defaultdict
from pathlib import Path
try:
    from .stub_sources import generate_source_companions
    from .stub_help import enrich_stubs
except ImportError:
    from stub_sources import generate_source_companions
    from stub_help import enrich_stubs
from typing import Any


SCALAR_TYPES = {
    "bool": "bool",
    "char": "int",
    "signed char": "int",
    "unsigned char": "int",
    "int8_t": "int",
    "uint8_t": "int",
    "int16_t": "int",
    "uint16_t": "int",
    "int32_t": "int",
    "uint32_t": "int",
    "int64_t": "int",
    "uint64_t": "int",
    "short": "int",
    "unsigned short": "int",
    "int": "int",
    "unsigned int": "int",
    "long": "int",
    "unsigned long": "int",
    "long long": "int",
    "unsigned long long": "int",
    "size_t": "int",
    "float": "float",
    "double": "float",
    "void": "None",
}
CLIENT_NAMES = {"Client", "ClientBase", "ClientStub", "LeaseClient"}


def qualified_name(item: dict[str, Any]) -> str:
    namespace = item.get("namespace", "")
    return f"{namespace}::{item['name']}" if namespace else item["name"]


def method_signature(method: dict[str, Any]) -> str:
    parameters = ", ".join(item["type"] for item in method.get("parameters", []))
    suffix = " const" if method.get("is_const") else ""
    return f"{method['name']}({parameters}){suffix}"


def snake_case(name: str) -> str:
    first_pass = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", first_pass).lower()


def parameter_name(name: str, index: int) -> str:
    result = snake_case(name) if name else f"arg{index}"
    return python_identifier(result)


def python_identifier(name: str) -> str:
    return name + "_" if keyword.iskeyword(name) else name


def normalize_cpp_type(type_name: str) -> str:
    result = type_name.strip().lstrip(":")
    result = re.sub(r"\bconst\s+", "", result)
    result = re.sub(r"\s*&&?\s*$", "", result)
    result = re.sub(r"\s+", " ", result)
    result = re.sub(r"\s*<\s*", "<", result)
    result = re.sub(r"\s*>\s*", ">", result)
    result = re.sub(r"\s*,\s*", ",", result)
    return result.strip()


def split_template_arguments(arguments: str) -> list[str]:
    result: list[str] = []
    depth = 0
    start = 0
    for index, char in enumerate(arguments):
        if char == "<":
            depth += 1
        elif char == ">":
            depth -= 1
        elif char == "," and depth == 0:
            result.append(arguments[start:index].strip())
            start = index + 1
    result.append(arguments[start:].strip())
    return result


def template_parts(type_name: str) -> tuple[str, list[str]] | None:
    start = type_name.find("<")
    if start < 0 or not type_name.endswith(">"):
        return None
    return type_name[:start], split_template_arguments(type_name[start + 1 : -1])


class TypeMapper:
    def __init__(
        self,
        classes: list[dict[str, Any]],
        python_names: dict[str, str] | None = None,
    ) -> None:
        self.classes = {qualified_name(item).lstrip(":"): item for item in classes}
        self.python_names = python_names or {}

    def annotation(
        self, type_name: str, namespace: str, position: str = "return"
    ) -> str:
        original = type_name.strip()
        normalized = normalize_cpp_type(original)
        if normalized in SCALAR_TYPES:
            return SCALAR_TYPES[normalized]
        if normalized in {"std::string", "string"}:
            return "str"
        if normalized in {"common::JsonMap", "unitree::common::JsonMap"}:
            return "dict[str, Any]"
        if "Callback" in normalized or normalized.endswith("ServerRequestHandler"):
            if "ConfigChangeStatusCallback" in normalized:
                return "Callable[[str, str], None]"
            return "Callable[..., Any]"
        if normalized.startswith("std::function<"):
            return "Callable[..., Any]"

        parts = template_parts(normalized)
        if parts:
            template, arguments = parts
            if template in {"std::vector", "std::array"} and arguments:
                value = self.annotation(arguments[0], namespace, "return")
                return f"Sequence[{value}]" if position == "input" else f"list[{value}]"
            if template in {"std::map", "std::unordered_map"} and len(arguments) == 2:
                key = self.annotation(arguments[0], namespace, "return")
                value = self.annotation(arguments[1], namespace, "return")
                mapping = f"dict[{key}, {value}]"
                return f"Mapping[{key}, {value}]" if position == "input" else mapping
            if template in {"std::shared_ptr", "std::unique_ptr"} and arguments:
                return self.annotation(arguments[0], namespace, position)
            if template in {"std::pair"} and len(arguments) == 2:
                first = self.annotation(arguments[0], namespace, "return")
                second = self.annotation(arguments[1], namespace, "return")
                return f"tuple[{first}, {second}]"
            if template in {"std::optional"} and arguments:
                return f"{self.annotation(arguments[0], namespace, position)} | None"

        if "*" in normalized:
            pointee = normalized.replace("*", "").strip()
            known = self._known_class(pointee, namespace)
            return known or "Any"
        known = self._known_class(normalized, namespace)
        if known:
            return known
        if normalized.endswith("Ptr"):
            known = self._known_class(normalized.removesuffix("Ptr"), namespace)
            return known or "Any"
        if normalized.startswith(("Eigen::", "dds::", "unitree_api::")):
            return "Any"
        return "Any"

    def _known_class(self, type_name: str, namespace: str) -> str | None:
        normalized = type_name.lstrip(":")
        candidate = self.classes.get(normalized)
        if candidate:
            if candidate["namespace"] == namespace:
                return self.python_names.get(
                    qualified_name(candidate), candidate["name"]
                )
            if candidate["namespace"] == "unitree::robot" and candidate["name"] in {
                "Client",
                "ClientBase",
            }:
                return candidate["name"]
            return None
        if normalized.endswith("::PathPoint"):
            alias = self.classes.get(
                normalized.removesuffix("PathPoint") + "stPathPoint"
            )
            if alias and alias["namespace"] == namespace:
                return "PathPoint"
        local = f"{namespace}::{normalized}" if namespace else normalized
        candidate = self.classes.get(local)
        if candidate is None and normalized == "PathPoint":
            candidate = self.classes.get(f"{namespace}::stPathPoint")
            if candidate:
                return "PathPoint"
        if not candidate:
            return None
        return self.python_names.get(qualified_name(candidate), candidate["name"])


def mutable_output(type_name: str) -> bool:
    return "&" in type_name and not type_name.lstrip().startswith("const ")


def method_status(
    cpp_class: str,
    method: dict[str, Any],
    available_methods: set[tuple[str, str]],
) -> str:
    signature = method_signature(method)
    if (cpp_class, signature) in available_methods:
        return "AVAILABLE"
    if cpp_class == "unitree::robot::ClientBase" and signature in {
        "SetTimeout(int64_t)",
        "SetTimeout(float)",
    }:
        return "AVAILABLE"
    if cpp_class == "unitree::robot::Client" and signature in {
        "WaitLeaseApplied()",
        "GetApiVersion() const",
        "GetServerApiVersion()",
    }:
        return "AVAILABLE"
    return "SIGNATURE_ONLY"


def python_default(parameter: dict[str, Any]) -> str:
    if not parameter.get("has_default"):
        return ""
    value = parameter.get("default_value")
    if value is None:
        return " = ..."
    if value == "true":
        value = "True"
    elif value == "false":
        value = "False"
    elif value == "nullptr":
        value = "None"
    return f" = {value}"


def method_annotations(
    method: dict[str, Any],
    namespace: str,
    mapper: TypeMapper,
    output_wrapper: bool,
) -> tuple[list[str], str]:
    parameters: list[str] = []
    outputs: list[str] = []
    for index, parameter in enumerate(method.get("parameters", [])):
        if output_wrapper and mutable_output(parameter["type"]):
            outputs.append(mapper.annotation(parameter["type"], namespace, "return"))
            continue
        name = parameter_name(parameter.get("name", ""), index)
        annotation = mapper.annotation(parameter["type"], namespace, "input")
        default = python_default(parameter)
        parameters.append(f"{name}: {annotation}{default}")

    result = mapper.annotation(method.get("return_type", "void"), namespace, "return")
    if outputs:
        values = ([] if result == "None" else [result]) + outputs
        result = values[0] if len(values) == 1 else f"tuple[{', '.join(values)}]"
    return parameters, result


def output_suffix(method: dict[str, Any]) -> str:
    for parameter in method.get("parameters", []):
        if not mutable_output(parameter["type"]):
            continue
        normalized = normalize_cpp_type(parameter["type"])
        parts = template_parts(normalized)
        if parts:
            template = parts[0].rsplit("::", 1)[-1]
            return snake_case(template)
        return snake_case(normalized.rsplit("::", 1)[-1].removesuffix("_"))
    return "result"


def python_method_name(cpp_class: str, method: dict[str, Any]) -> str:
    if (
        cpp_class == "unitree::robot::ClientBase"
        and method_signature(method) == "SetTimeout(int64_t)"
    ):
        return "set_timeout_microseconds"
    return python_identifier(snake_case(method["name"]))


def class_base(cpp_class: dict[str, Any], module_namespace: str) -> str:
    for base in cpp_class.get("bases", []):
        normalized = normalize_cpp_type(base["type"])
        if normalized == "unitree::robot::Client":
            return "Client"
        if normalized == "unitree::robot::ClientBase":
            return "ClientBase"
        if normalized.startswith(module_namespace + "::"):
            return normalized.rsplit("::", 1)[-1]
    return "object"


def render_robot_module(
    namespace: str,
    classes: list[dict[str, Any]],
    enums: list[dict[str, Any]],
    mapper: TypeMapper,
    classifications: dict[tuple[str, str], dict[str, str]],
    available_methods: set[tuple[str, str]],
    available_constructors: set[tuple[str, str]],
    available_classes: set[str],
    available_strategies: dict[tuple[str, str], str],
    manifest: list[dict[str, Any]],
) -> str:
    lines = [
        '"""Full SDK signature preview; see api_manifest.json for availability."""',
        "from __future__ import annotations",
        "",
        "import enum",
        "from collections.abc import Callable, Mapping, Sequence",
        "from typing import Any, overload",
    ]
    if namespace != "unitree::robot":
        lines.extend(["", "from . import Client, ClientBase"])
    lines.append("")

    for cpp_enum in sorted(enums, key=lambda item: item["name"]):
        lines.append(f"class {cpp_enum['name']}(enum.IntEnum):")
        values = cpp_enum.get("values", [])
        if values:
            lines.extend(f"    {item['name']} = ..." for item in values)
        else:
            lines.append("    ...")
        lines.append("")

    client_class_names = {
        item["name"]
        for item in classes
        if item["name"].endswith("Client") or item["name"] in CLIENT_NAMES
    }
    for cpp_class in sorted(classes, key=lambda item: item["name"]):
        cpp_name = qualified_name(cpp_class)
        base = class_base(cpp_class, namespace)
        lines.append(f"class {cpp_class['name']}({base}):")
        body: list[str] = []

        constructors = [
            item
            for item in cpp_class.get("constructors", [])
            if item.get("access") == "public"
        ]
        for index, constructor in enumerate(constructors):
            if len(constructors) > 1:
                body.append("    @overload")
            parameters, _ = method_annotations(constructor, namespace, mapper, False)
            status = (
                "AVAILABLE"
                if (
                    (cpp_name, method_signature(constructor)) in available_constructors
                    or cpp_name in available_classes
                    and not constructor.get("parameters")
                )
                else "SIGNATURE_ONLY"
            )
            body.extend(
                [
                    f"    def __init__(self{', ' if parameters else ''}{', '.join(parameters)}) -> None:",
                    f'        """{status}; C++: {cpp_name}::{method_signature(constructor)}."""',
                    "        ...",
                ]
            )
            manifest.append(
                {
                    "cpp_class": cpp_name,
                    "cpp_signature": method_signature(constructor),
                    "python_path": f"unitree_sdk2_cpp.{namespace.removeprefix('unitree::').replace('::', '.')}.{cpp_class['name']}.__init__",
                    "status": status,
                    "safety": "CONSTRUCTION",
                }
            )

        for field in cpp_class.get("fields", []):
            if field.get("access") == "public":
                body.append(
                    f"    {python_identifier(snake_case(field['name']))}: "
                    f"{mapper.annotation(field['type'], namespace, 'return')}"
                )

        if not constructors and cpp_name in available_classes and (
            cpp_class.get("kind") == "struct"
            or (cpp_name, f"{cpp_class['name']}()") in available_constructors
        ):
            body.extend(
                [
                    "    def __init__(self) -> None:",
                    f'        """AVAILABLE; C++ aggregate: {cpp_name}."""',
                    "        ...",
                ]
            )
            manifest.append(
                {
                    "cpp_class": cpp_name,
                    "cpp_signature": f"{cpp_class['name']}()",
                    "python_path": f"unitree_sdk2_cpp.{namespace.removeprefix('unitree::').replace('::', '.')}.{cpp_class['name']}.__init__",
                    "status": "AVAILABLE",
                    "safety": "CONSTRUCTION",
                }
            )

        methods = [
            item
            for item in cpp_class.get("methods", [])
            if item.get("access") == "public"
        ]
        output_wrappers = [
            cpp_class["name"] in client_class_names
            and available_strategies.get((cpp_name, method_signature(method)))
            != "MUTABLE_INPUT_COPY"
            for method in methods
        ]
        base_names = [python_method_name(cpp_name, item) for item in methods]
        input_shapes = [
            tuple(
                mapper.annotation(parameter["type"], namespace, "input")
                for parameter in method.get("parameters", [])
                if not (output_wrapper and mutable_output(parameter["type"]))
            )
            for method, output_wrapper in zip(methods, output_wrappers, strict=True)
        ]
        shape_counts = Counter(zip(base_names, input_shapes, strict=True))
        python_names = [
            (
                f"{base_name}_{output_suffix(method)}"
                if output_wrapper and shape_counts[(base_name, shape)] > 1
                else base_name
            )
            for method, base_name, shape, output_wrapper in zip(
                methods, base_names, input_shapes, output_wrappers, strict=True
            )
        ]
        grouped: Counter[str] = Counter(python_names)
        for method, python_name, output_wrapper in zip(
            methods, python_names, output_wrappers, strict=True
        ):
            if grouped[python_name] > 1:
                body.append("    @overload")
            parameters, result = method_annotations(
                method, namespace, mapper, output_wrapper
            )
            strategy = available_strategies.get(
                (cpp_name, method_signature(method))
            )
            if strategy == "JSON_DICT_INPUT":
                parameters = ["value: Mapping[str, Any]"]
                result = "None"
            elif strategy == "JSON_DICT_OUTPUT":
                parameters = []
                result = "dict[str, Any]"
            if cpp_name == "unitree::robot::ClientBase":
                if method_signature(method) == "SetTimeout(int64_t)":
                    parameters = ["microseconds: int"]
                elif method_signature(method) == "SetTimeout(float)":
                    parameters = ["seconds: float"]
            classification = classifications.get(
                (cpp_name, method_signature(method)), {}
            )
            status = method_status(cpp_name, method, available_methods)
            safety = classification.get("safety", "UNCLASSIFIED")
            strategy = available_strategies.get(
                (cpp_name, method_signature(method)),
                classification.get("binding_strategy", "SIGNATURE_PREVIEW"),
            )
            body.extend(
                [
                    f"    def {python_name}(self{', ' if parameters else ''}{', '.join(parameters)}) -> {result}:",
                    f'        """{status} | {safety} | {strategy}. C++: {method_signature(method)}."""',
                    "        ...",
                ]
            )
            manifest.append(
                {
                    "cpp_class": cpp_name,
                    "cpp_signature": method_signature(method),
                    "python_path": f"unitree_sdk2_cpp.{namespace.removeprefix('unitree::').replace('::', '.')}.{cpp_class['name']}.{python_name}",
                    "status": status,
                    "safety": safety,
                    "binding_strategy": strategy,
                    "python_return": result,
                }
            )

        lines.extend(body or ["    ..."])
        lines.append("")
        if cpp_class["name"] == "stPathPoint" and cpp_name in available_classes:
            lines.extend(["PathPoint = stPathPoint", ""])
    return "\n".join(lines)


def render_idl_module(
    module_name: str,
    report: dict[str, Any],
    inventory: dict[str, Any],
    mapper: TypeMapper,
) -> tuple[str, list[dict[str, Any]]]:
    classes_by_name = {qualified_name(item): item for item in inventory["classes"]}
    lines = [
        '"""Generated DDS message bindings."""',
        "from __future__ import annotations",
        "",
        "from collections.abc import Sequence",
        "from typing import Any",
        "",
    ]
    manifest: list[dict[str, Any]] = []
    for item in report["classes"]:
        cpp_class = classes_by_name[item["qualified_name"]]
        fields = {
            field["name"].removesuffix("_"): field for field in cpp_class["fields"]
        }
        lines.extend(
            [
                f"class {item['python_name']}:",
                "    def __init__(self) -> None: ...",
            ]
        )
        manifest.append(
            {
                "cpp_class": item["qualified_name"],
                "cpp_signature": f"{cpp_class['name']}()",
                "python_path": (
                    f"unitree_sdk2_cpp.idl.{module_name}."
                    f"{item['python_name']}.__init__"
                ),
                "status": "AVAILABLE",
                "safety": "VALUE_TYPE",
            }
        )
        for property_name in item["properties"]:
            annotation = mapper.annotation(
                fields[property_name]["type"], cpp_class["namespace"], "return"
            )
            input_annotation = mapper.annotation(
                fields[property_name]["type"], cpp_class["namespace"], "input"
            )
            lines.extend(
                [
                    "    @property",
                    f"    def {property_name}(self) -> {annotation}: ...",
                    f"    @{property_name}.setter",
                    f"    def {property_name}(self, value: {input_annotation}) -> None: ...",
                ]
            )
            manifest.append(
                {
                    "cpp_class": item["qualified_name"],
                    "cpp_signature": fields[property_name]["type"],
                    "python_path": (
                        f"unitree_sdk2_cpp.idl.{module_name}."
                        f"{item['python_name']}.{property_name}"
                    ),
                    "status": "AVAILABLE",
                    "safety": "VALUE_TYPE",
                }
            )
        if any(method["name"] == "operator==" for method in cpp_class["methods"]):
            lines.append("    def __eq__(self, other: object) -> bool: ...")
            manifest.append(
                {
                    "cpp_class": item["qualified_name"],
                    "cpp_signature": "operator==(const value &) const",
                    "python_path": (
                        f"unitree_sdk2_cpp.idl.{module_name}."
                        f"{item['python_name']}.__eq__"
                    ),
                    "status": "AVAILABLE",
                    "safety": "VALUE_TYPE",
                }
            )
        if any(method["name"] == "operator!=" for method in cpp_class["methods"]):
            lines.append("    def __ne__(self, other: object) -> bool: ...")
            manifest.append(
                {
                    "cpp_class": item["qualified_name"],
                    "cpp_signature": "operator!=(const value &) const",
                    "python_path": (
                        f"unitree_sdk2_cpp.idl.{module_name}."
                        f"{item['python_name']}.__ne__"
                    ),
                    "status": "AVAILABLE",
                    "safety": "VALUE_TYPE",
                }
            )
        lines.append("")
    return "\n".join(lines), manifest


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def generate(arguments: argparse.Namespace) -> dict[str, Any]:
    idl_inventory = json.loads(arguments.idl_inventory.read_text(encoding="utf-8"))
    robot_inventory = json.loads(arguments.robot_inventory.read_text(encoding="utf-8"))
    classification = json.loads(arguments.classification.read_text(encoding="utf-8"))
    policy = json.loads(arguments.policy.read_text(encoding="utf-8"))
    binding_report = json.loads(arguments.read_only_report.read_text(encoding="utf-8"))
    idl_reports = [
        json.loads(path.read_text(encoding="utf-8")) for path in arguments.idl_report
    ]

    output = arguments.output
    # PEP 561 declarations and discoverable source companions are separate.
    # The companion root explicitly loads the existing top-level native .so.
    package = output / "unitree_sdk2_cpp-stubs"
    idl_python_names = {
        item["qualified_name"]: item["python_name"]
        for report in idl_reports
        for item in report["classes"]
    }
    mapper = TypeMapper(
        [
            *idl_inventory["classes"],
            *robot_inventory["classes"],
            *robot_inventory["enums"],
        ],
        idl_python_names,
    )
    binding_items = [
        *binding_report["classes"],
        *binding_report.get("value_classes", []),
        *binding_report.get("utility_classes", []),
    ]
    available_classes = {item["qualified_name"] for item in binding_items}
    available_methods = {
        (item["qualified_name"], method["cpp_signature"])
        for item in binding_items
        for method in item.get("methods", [])
    }
    available_constructors = {
        (item["qualified_name"], signature)
        for item in binding_items
        for signature in item.get("constructors", [])
    }
    available_strategies = {
        (item["qualified_name"], method["cpp_signature"]): method["binding_strategy"]
        for item in binding_items
        for method in item.get("methods", [])
    }
    classifications = {
        (client["qualified_name"], method["signature"]): method
        for client in classification["clients"]
        for method in client["methods"]
    }

    write_text(
        package / "__init__.pyi",
        '''"""Unitree SDK2 extension API signature preview."""
from . import channel as channel
from . import idl as idl
from . import robot as robot

__all__ = ["channel", "idl", "robot", "OsHelper"]

class OsHelper:
    @staticmethod
    def instance() -> OsHelper: ...
    def get_uid(self) -> int: ...
    def get_gid(self) -> int: ...
    def get_user(self) -> str: ...
    def get_processor_number(self) -> int: ...
    def get_page_size(self) -> int: ...
    def get_hostname(self) -> str: ...
''',
    )
    write_text(
        package / "channel.pyi",
        '''"""Typed CycloneDDS channel API."""
from collections.abc import Callable
from typing import Any, Generic, TypeVar

MessageT = TypeVar("MessageT")

def registered_message_types() -> list[str]: ...
def initialize(domain_id: int = 0, network_interface: str = "") -> None: ...
def initialize_from_config(config_file: str = "") -> None: ...
def release() -> None: ...

class ChannelPublisher(Generic[MessageT]):
    def __init__(self, topic: str, message_type: type[MessageT]) -> None: ...
    @property
    def topic(self) -> str: ...
    @property
    def message_type_name(self) -> str: ...
    def init_channel(self) -> None: ...
    def close_channel(self) -> None: ...
    def write(self, message: MessageT, wait_microsec: int = 0) -> bool: ...

class ChannelSubscriber(Generic[MessageT]):
    def __init__(
        self,
        topic: str,
        message_type: type[MessageT],
        callback: Callable[[MessageT], None],
        queue_length: int = 0,
    ) -> None: ...
    @property
    def topic(self) -> str: ...
    @property
    def message_type_name(self) -> str: ...
    @property
    def last_data_available_time(self) -> int: ...
    def init_channel(self) -> None: ...
    def close_channel(self) -> None: ...
''',
    )

    idl_module_names = ["go2", "hg", "hg_doubleimu", "ros2"]
    write_text(
        package / "idl" / "__init__.pyi",
        '\n'.join(['"""DDS 消息类型；G1 使用 HG 消息别名。"""',
                   *(f"from . import {name} as {name}" for name in ["g1", *idl_module_names])]),
    )
    manifest_entries: list[dict[str, Any]] = []
    for name, report in zip(idl_module_names, idl_reports, strict=True):
        content, entries = render_idl_module(name, report, idl_inventory, mapper)
        write_text(package / "idl" / f"{name}.pyi", content)
        manifest_entries.extend(entries)

    hg_class_names = [item["python_name"] for item in idl_reports[1]["classes"]]
    g1_alias_lines = [
        '"""G1-friendly aliases for the unitree_hg DDS message types."""',
        "from typing import overload",
        "",
        "from .hg import (",
        *(f"    {name} as {name}," for name in hg_class_names),
        ")",
        "",
        "@overload",
        "def compute_crc(message: LowCmd) -> int: ...",
        "@overload",
        "def compute_crc(message: LowState) -> int: ...",
        "def update_crc(message: LowCmd) -> int: ...",
        "@overload",
        "def validate_crc(message: LowCmd) -> bool: ...",
        "@overload",
        "def validate_crc(message: LowState) -> bool: ...",
    ]
    write_text(package / "idl" / "g1.pyi", "\n".join(g1_alias_lines))

    manifest_entries.extend(
        [
            {
                "cpp_class": "unitree_hg::msg::dds_::LowCmd_",
                "cpp_signature": "crc32_core(LowCmd_)",
                "python_path": "unitree_sdk2_cpp.idl.g1.compute_crc",
                "status": "AVAILABLE",
                "safety": "VALUE_TYPE",
                "binding_strategy": "CRC_WRAPPER",
                "python_parameters": ["LowCmd"],
                "python_return": "int",
            },
            {
                "cpp_class": "unitree_hg::msg::dds_::LowState_",
                "cpp_signature": "crc32_core(LowState_)",
                "python_path": "unitree_sdk2_cpp.idl.g1.compute_crc",
                "status": "AVAILABLE",
                "safety": "VALUE_TYPE",
                "binding_strategy": "CRC_WRAPPER",
                "python_parameters": ["LowState"],
                "python_return": "int",
            },
            {
                "cpp_class": "unitree_hg::msg::dds_::LowCmd_",
                "cpp_signature": "crc32_core(LowCmd_); LowCmd_::crc(uint32_t)",
                "python_path": "unitree_sdk2_cpp.idl.g1.update_crc",
                "status": "AVAILABLE",
                "safety": "VALUE_TYPE",
                "binding_strategy": "CRC_WRAPPER",
                "python_parameters": ["LowCmd"],
                "python_return": "int",
            },
            {
                "cpp_class": "unitree_hg::msg::dds_::LowCmd_",
                "cpp_signature": "LowCmd_::crc() == crc32_core(LowCmd_)",
                "python_path": "unitree_sdk2_cpp.idl.g1.validate_crc",
                "status": "AVAILABLE",
                "safety": "VALUE_TYPE",
                "binding_strategy": "CRC_WRAPPER",
                "python_parameters": ["LowCmd"],
                "python_return": "bool",
            },
            {
                "cpp_class": "unitree_hg::msg::dds_::LowState_",
                "cpp_signature": "LowState_::crc() == crc32_core(LowState_)",
                "python_path": "unitree_sdk2_cpp.idl.g1.validate_crc",
                "status": "AVAILABLE",
                "safety": "VALUE_TYPE",
                "binding_strategy": "CRC_WRAPPER",
                "python_parameters": ["LowState"],
                "python_return": "bool",
            },
        ]
    )
    manifest_entries.extend(
        {
            "cpp_class": "unitree::robot::g1",
            "cpp_signature": signature,
            "python_path": f"unitree_sdk2_cpp.robot.g1.{python_name}",
            "status": "AVAILABLE",
            "safety": "SAFETY_CHECK",
            "binding_strategy": (
                "TYPE_ERASED_ADAPTER"
                if python_name == "lost_connection"
                else "DIRECT"
            ),
            "python_return": "bool",
        }
        for python_name, signature in [
            (
                "bad_orientation",
                "bad_orientation(const unitree_hg::msg::dds_::LowState_ &, float)",
            ),
            (
                "joint_vel_out_of_limit",
                "joint_vel_out_of_limit(const unitree_hg::msg::dds_::LowState_ &, float)",
            ),
            (
                "ang_vel_out_of_limit",
                "ang_vel_out_of_limit(const unitree_hg::msg::dds_::LowState_ &, float)",
            ),
            (
                "motor_winding_overheat",
                "motor_winding_overheat(const unitree_hg::msg::dds_::LowState_ &, float)",
            ),
            (
                "motor_casing_overheat",
                "motor_casing_overheat(const unitree_hg::msg::dds_::LowState_ &, float)",
            ),
            (
                "low_battery",
                "low_battery(const unitree_hg::msg::dds_::BmsState_ &, float)",
            ),
            (
                "lost_connection",
                "lost_connection(unitree::robot::ChannelSubscriberPtr<unitree_hg::msg::dds_::LowState_> &, int64_t)",
            ),
        ]
    )

    manual_paths = {
        "unitree_sdk2_cpp.OsHelper.instance": "OsHelper::Instance()",
        "unitree_sdk2_cpp.OsHelper.get_uid": "OsHelper::GetUID()",
        "unitree_sdk2_cpp.OsHelper.get_gid": "OsHelper::GetGID()",
        "unitree_sdk2_cpp.OsHelper.get_user": "OsHelper::GetUser()",
        "unitree_sdk2_cpp.OsHelper.get_processor_number": "OsHelper::GetProcessorNumber()",
        "unitree_sdk2_cpp.OsHelper.get_page_size": "OsHelper::GetPageSize()",
        "unitree_sdk2_cpp.OsHelper.get_hostname": "OsHelper::GetHostname()",
        "unitree_sdk2_cpp.channel.registered_message_types": "registered_message_types()",
        "unitree_sdk2_cpp.channel.initialize": "ChannelFactory::Init(int32_t, const std::string &)",
        "unitree_sdk2_cpp.channel.initialize_from_config": "ChannelFactory::Init(const std::string &)",
        "unitree_sdk2_cpp.channel.release": "ChannelFactory::Release()",
        "unitree_sdk2_cpp.channel.ChannelPublisher.__init__": "ChannelPublisher(const std::string &, type)",
        "unitree_sdk2_cpp.channel.ChannelPublisher.topic": "ChannelPublisher::topic() const",
        "unitree_sdk2_cpp.channel.ChannelPublisher.message_type_name": "ChannelPublisher::message_type_name() const",
        "unitree_sdk2_cpp.channel.ChannelPublisher.init_channel": "ChannelPublisher::init_channel()",
        "unitree_sdk2_cpp.channel.ChannelPublisher.close_channel": "ChannelPublisher::close_channel()",
        "unitree_sdk2_cpp.channel.ChannelPublisher.write": "ChannelPublisher::write(message, int64_t)",
        "unitree_sdk2_cpp.channel.ChannelSubscriber.__init__": "ChannelSubscriber(const std::string &, type, callback, int64_t)",
        "unitree_sdk2_cpp.channel.ChannelSubscriber.topic": "ChannelSubscriber::topic() const",
        "unitree_sdk2_cpp.channel.ChannelSubscriber.message_type_name": "ChannelSubscriber::message_type_name() const",
        "unitree_sdk2_cpp.channel.ChannelSubscriber.last_data_available_time": "ChannelSubscriber::last_data_available_time() const",
        "unitree_sdk2_cpp.channel.ChannelSubscriber.init_channel": "ChannelSubscriber::init_channel()",
        "unitree_sdk2_cpp.channel.ChannelSubscriber.close_channel": "ChannelSubscriber::close_channel()",
    }
    manifest_entries.extend(
        {
            "cpp_class": path.rsplit(".", 1)[0],
            "cpp_signature": signature,
            "python_path": path,
            "status": "AVAILABLE",
            "safety": "DDS_LIFECYCLE" if ".channel." in path else "READ_ONLY",
        }
        for path, signature in manual_paths.items()
    )

    robot_classes = [
        item
        for item in robot_inventory["classes"]
        if item["namespace"].startswith("unitree::robot")
    ]
    robot_enums = [
        item
        for item in robot_inventory["enums"]
        if item["namespace"].startswith("unitree::robot")
    ]
    by_namespace: dict[str, list[dict[str, Any]]] = defaultdict(list)
    enums_by_namespace: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in robot_classes:
        by_namespace[item["namespace"]].append(item)
    for item in robot_enums:
        enums_by_namespace[item["namespace"]].append(item)

    submodules = sorted(
        namespace.removeprefix("unitree::robot::")
        for namespace in by_namespace
        if namespace != "unitree::robot"
    )
    root_content = render_robot_module(
        "unitree::robot",
        by_namespace["unitree::robot"],
        enums_by_namespace["unitree::robot"],
        mapper,
        classifications,
        available_methods,
        available_constructors,
        available_classes,
        available_strategies,
        manifest_entries,
    )
    root_content += "\n" + "\n".join(
        f"from . import {name} as {name}" for name in submodules
    ) + "\n"
    write_text(package / "robot" / "__init__.pyi", root_content)
    for name in submodules:
        namespace = f"unitree::robot::{name}"
        content = render_robot_module(
            namespace,
            by_namespace[namespace],
            enums_by_namespace[namespace],
            mapper,
            classifications,
            available_methods,
            available_constructors,
            available_classes,
            available_strategies,
            manifest_entries,
        )
        if name == "g1":
            content += '''
from ..channel import ChannelSubscriber
from ..idl.g1 import BmsState, LowState

def bad_orientation(low_state: LowState, limit_angle: float = 1.0) -> bool: ...
def joint_vel_out_of_limit(low_state: LowState, limit_vel: float = 10.0) -> bool: ...
def ang_vel_out_of_limit(low_state: LowState, limit_vel: float = 6.0) -> bool: ...
def motor_winding_overheat(low_state: LowState, limit_temp: float = 120.0) -> bool: ...
def motor_casing_overheat(low_state: LowState, limit_temp: float = 85.0) -> bool: ...
def low_battery(bms_state: BmsState, limit_soc: float = 20.0) -> bool: ...
def lost_connection(subscriber: ChannelSubscriber[LowState], timeout_ms: int = 1000) -> bool: ...
'''
        write_text(
            package / "robot" / f"{name}.pyi",
            content,
        )

    write_text(package / "py.typed", "")
    status_counts = Counter(item["status"] for item in manifest_entries)
    manifest = {
        "schema_version": 1,
        "warning": (
            "SIGNATURE_ONLY APIs are design-time previews and are not guaranteed "
            "to exist in the current binary extension."
        ),
        "summary": {
            "idl_classes": sum(len(report["classes"]) for report in idl_reports),
            "idl_properties": sum(
                len(item["properties"])
                for report in idl_reports
                for item in report["classes"]
            ),
            "robot_classes": len(robot_classes),
            "robot_public_signatures": sum(
                len([c for c in item["constructors"] if c["access"] == "public"])
                + len([m for m in item["methods"] if m["access"] == "public"])
                for item in robot_classes
            ),
            "manifest_entries": len(manifest_entries),
            "status": dict(sorted(status_counts.items())),
        },
        "entries": sorted(
            manifest_entries,
            key=lambda item: (item["python_path"], item["cpp_signature"]),
        ),
    }
    (package / "api_manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    enrich_stubs(package, Path(__file__).resolve().parents[1])
    generate_source_companions(package)
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--idl-inventory", type=Path, required=True)
    parser.add_argument("--robot-inventory", type=Path, required=True)
    parser.add_argument("--classification", type=Path, required=True)
    parser.add_argument("--policy", type=Path, required=True)
    parser.add_argument("--read-only-report", type=Path, required=True)
    parser.add_argument("--idl-report", type=Path, action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()
    manifest = generate(arguments)
    print(json.dumps(manifest["summary"], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
