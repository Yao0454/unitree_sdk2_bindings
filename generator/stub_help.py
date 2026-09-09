"""Build IDE hover documentation from the same typed model as the API manual."""

from __future__ import annotations

import ast
from pathlib import Path

try:
    from . import generate_api_docs as docs
except ImportError:
    import generate_api_docs as docs


PURPOSES = {
    "robot.go2.SportClient.move": "发送 Go2 高层速度指令：前后、左右平移和偏航旋转。",
    "robot.go2.SportClient.stop_move": "请求 Go2 停止高层移动；不是独立硬件急停。",
    "robot.go2.SportClient.stand_up": "请求 Go2 起立。返回成功表示请求被接受，不代表已经完成起立。",
    "robot.go2.SportClient.stand_down": "请求 Go2 趴下；执行前需确认周围空间。",
    "robot.go2.RobotStateClient.service_list": "查询 Go2 服务列表，返回状态码和 ServiceState 对象列表。",
    "robot.go2.RobotStateClient.service_switch": "启用或停用指定 Go2 服务，会改变机器人服务状态。",
    "robot.go2.VideoClient.get_image_sample": "获取相机编码后的图片字节，不是 RGB 像素矩阵。",
    "robot.go2.VuiClient.get_volume": "查询 Go2 音量等级。",
    "robot.go2.VuiClient.set_volume": "设置 Go2 音量等级；有效范围以设备固件为准。",
    "robot.go2.VuiClient.get_brightness": "查询 Go2 灯光亮度等级。",
    "robot.go2.VuiClient.set_brightness": "设置 Go2 灯光亮度等级；有效范围以设备固件为准。",
    "robot.g1.G1ArmActionClient.get_action_list": "查询 G1 当前支持的机械臂动作，返回服务提供的原始字符串。",
    "robot.g1.G1ArmActionClient.execute_action": "按动作 ID 或自定义名称执行 G1 机械臂动作。先查询动作列表确认目标。",
    "robot.g1.G1ArmActionClient.stop_custom_action": "请求停止当前自定义机械臂动作；不保证停止所有内置动作。",
    "robot.g1.LocoClient.get_fsm_id": "查询 G1 当前 FSM 状态编号。",
    "robot.g1.LocoClient.get_fsm_mode": "查询 G1 当前 FSM 模式。",
    "robot.g1.LocoClient.set_fsm_id": "请求切换 G1 FSM 状态。目标编号含义取决于固件，切换可能引发运动。",
    "robot.g1.AudioClient.tts_maker": "请求 G1 把指定文字转换为语音并播放。",
    "robot.ClientBase.set_timeout": "设置客户端 RPC 超时时间，单位为秒。",
    "robot.ClientBase.set_timeout_microseconds": "设置客户端 RPC 超时时间，单位为微秒。",
    "idl.g1.compute_crc": "计算 G1 消息的 CRC，不修改消息。",
    "idl.g1.update_crc": "计算并回写 G1 LowCmd.crc，返回新的 CRC。修改字段后应重新计算。",
    "idl.g1.validate_crc": "比较 G1 消息内容与 crc 字段是否匹配；不等价于运动安全检查。",
}

EXAMPLES = {
    "robot.go2.SportClient.move": "# client 已初始化，机器人处于可行走状态\ntry:\n    code = client.move(vx=0.1, vy=0.0, vyaw=0.0)\n    if code != 0:\n        raise RuntimeError(f'move 失败: {code}')\nfinally:\n    stop_code = client.stop_move()\n    if stop_code != 0:\n        raise RuntimeError(f'停止失败: {stop_code}')",
    "robot.go2.RobotStateClient.service_list": "code, services = client.service_list()\nif code != 0:\n    raise RuntimeError(f'查询失败: {code}')\nfor service in services:\n    print(service.name, service.status)",
    "robot.go2.VideoClient.get_image_sample": "code, data = client.get_image_sample()\nif code != 0:\n    raise RuntimeError(f'获取图片失败: {code}')\nimage_bytes = bytes(data)",
    "robot.g1.G1ArmActionClient.get_action_list": "code, actions = client.get_action_list()\nif code != 0:\n    raise RuntimeError(f'查询失败: {code}')\nprint(actions)",
    "robot.g1.LocoClient.get_fsm_id": "code, fsm_id = client.get_fsm_id()\nif code != 0:\n    raise RuntimeError(f'查询失败: {code}')\nprint(fsm_id)",
    "robot.ClientBase.set_timeout": "client.set_timeout(seconds=5.0)",
    "robot.ClientBase.set_timeout_microseconds": "client.set_timeout_microseconds(microseconds=5_000_000)",
    "idl.g1.compute_crc": "checksum = compute_crc(message)",
    "idl.g1.update_crc": "checksum = update_crc(command)\nassert command.crc == checksum",
    "idl.g1.validate_crc": "valid = validate_crc(message)",
}


def function_help(function: docs.FunctionDoc) -> str:
    key = function.python_path.removeprefix("unitree_sdk2_cpp.")
    lines = [PURPOSES.get(key, docs.function_purpose(function)), "",
             f"可用性：{function.manifest['status']}；分类：{function.manifest.get('safety', 'UNCLASSIFIED')}。",
             "", "Args:"]
    cpp_params = docs.cpp_input_parameters(function)
    for index, param in enumerate(function.public_parameters):
        cpp_param = cpp_params[index] if index < len(cpp_params) else None
        description = docs.parameter_description(param, cpp_param)
        if key == "robot.go2.SportClient.move":
            description = {"vx": "前向速度，单位 m/s；负值为向后。", "vy": "左向速度，单位 m/s；负值为向右。", "vyaw": "偏航角速度，单位 rad/s；正值为左转。"}[param.name]
        elif key.endswith("execute_action"):
            description = {"action_id": "从 get_action_list() 查询并确认的动作 ID。", "action_name": "已在机器人端配置的自定义动作名称。"}.get(param.name, description)
        lines.append(f"    {param.name}: {description}")
    if not function.public_parameters:
        lines.append("    无显式参数；实例方法的 self 由 Python 自动传入。")
    lines.extend(["", "Returns:"])
    for label, type_name, description in docs.return_rows(function):
        lines.append(f"    {label} ({type_name}): {description}")
    example = EXAMPLES.get(key, docs.usage_example(function))
    if key.endswith("G1ArmActionClient.execute_action"):
        param = function.public_parameters[0].name
        example = f"# {param} 已从设备动作列表或自定义配置中确认\ncode = client.execute_action({param})\nif code != 0:\n    raise RuntimeError(f'执行失败: {{code}}')"
    lines.extend(["", "Examples:", "    用法片段；obj/client 和参数变量需先按业务准备。", "", "    ```python"])
    lines.extend("    " + line for line in example.splitlines())
    lines.extend(["    ```", "", "Notes:"])
    if function.manifest["status"] == "SIGNATURE_ONLY":
        lines.append("    仅供设计时预览，不能假设该成员存在于原生扩展。")
    if function.manifest.get("safety") == "MOTION_COMMAND":
        lines.append("    会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。")
    elif function.module.startswith("unitree_sdk2_cpp.robot") and function.owner and function.owner.endswith("Client"):
        lines.append("    服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。")
    else:
        lines.append("    stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。")
    lines.append(f"    C++: {function.manifest['cpp_signature']}")
    return "\n".join(lines)


def enrich_stubs(package: Path, binding_root: Path) -> None:
    modules, _, _ = docs.parse_stubs(binding_root, stub_root=package)
    by_module = {module.name: module for module in modules}
    for path in sorted(package.rglob("*.pyi")):
        module = by_module.get(docs.module_name(package, path))
        if module is None:
            continue
        source = path.read_text(encoding="utf-8")
        tree = ast.parse(source)
        lines = source.splitlines(keepends=True)
        offsets = [0]
        for line in lines:
            offsets.append(offsets[-1] + len(line))
        edits: list[tuple[int, int, str]] = []

        def literal(text: str, indent: int) -> str:
            safe = text.replace('"""', '\\"\\"\\"')
            return '"""' + safe.replace("\n", "\n" + " " * indent) + '\n' + ' ' * indent + '"""'

        def document_function(node: ast.FunctionDef, text: str) -> None:
            start = offsets[node.body[0].lineno - 1] + node.body[0].col_offset
            end = offsets[node.end_lineno - 1] + node.end_col_offset
            indent = node.col_offset + 4
            # A multiline signature can still end with an inline ': ...'.
            inline = bool(lines[node.body[0].lineno - 1][:node.body[0].col_offset].strip())
            if inline:
                start = offsets[node.body[0].lineno - 1] + len(lines[node.body[0].lineno - 1][:node.body[0].col_offset].rstrip())
            prefix = "\n" + " " * indent if inline else ""
            replacement = prefix + literal(text, indent) + "\n" + " " * indent + "..."
            edits.append((start, end, replacement))

        for function in module.functions:
            document_function(function.source_node, function_help(function))
        for cls in module.classes:
            class_node = next(node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == cls.name)
            insert = offsets[class_node.lineno]
            indent = class_node.col_offset + 4
            class_text = docs.class_purpose(cls) + f"\n\n导入：from {module.name} import {cls.name}"
            if cls.functions:
                constructor = next((f for f in cls.functions if f.name == '__init__'), None)
                if constructor:
                    class_text += f"\n构造可用性：{constructor.manifest['status']}。"
            edits.append((insert, insert, " " * indent + literal(class_text, indent) + "\n"))
            for function in cls.functions:
                document_function(function.source_node, function_help(function))
            for prop in cls.properties:
                text = (docs.property_description(prop) + f"\n\nReturns:\n    {prop.read_type}：字段当前值。\n\nExamples:\n    value = obj.{prop.name}")
                if prop.setter:
                    text += f"\n    # 修改副本后必须回写\n    obj.{prop.name} = value"
                document_function(prop.getter, text)
                if prop.setter:
                    document_function(prop.setter, docs.property_description(prop) + f"\n\nArgs:\n    value: 写入的新值；固定数组长度必须与 SDK 一致。\n\nReturns:\n    None\n\nExamples:\n    obj.{prop.name} = value")
            for node in class_node.body:
                if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
                    at = offsets[node.end_lineno]
                    text = f"{cls.name}.{node.target.id}：公开字段，类型为 {ast.unparse(node.annotation)}。\n具体单位及允许值以对应 SDK 数据结构为准。"
                    edits.append((at, at, " " * indent + literal(text, indent) + "\n"))
        for start, end, replacement in sorted(edits, key=lambda edit: (edit[0], edit[1]), reverse=True):
            source = source[:start] + replacement + source[end:]
        try:
            ast.parse(source)
        except SyntaxError as error:
            nearby = source.splitlines()[max(0, (error.lineno or 1) - 4):(error.lineno or 1) + 3]
            raise ValueError(f"Invalid generated help in {path}: {error}\n" + "\n".join(nearby)) from error
        path.write_text("\n".join(line.rstrip() for line in source.splitlines()) + "\n", encoding="utf-8")
