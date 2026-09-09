"""Full SDK signature preview; see api_manifest.json for availability."""
from __future__ import annotations

import enum
from collections.abc import Callable, Mapping, Sequence
from typing import Any, overload

from . import Client, ClientBase

class AudioClient(Client):
    """Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

    导入：from unitree_sdk2_cpp.robot.r1 import AudioClient
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `AudioClient` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = AudioClient()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: AudioClient()
        """
        ...
    def init(self) -> None:
        """初始化当前 SDK 对象所需的底层通道或服务资源。

        可用性：AVAILABLE；分类：INITIALIZATION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            obj.init()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: Init()
        """
        ...
    def tts_maker(self, text: str, speaker_id: int) -> int:
        """对应 C++ SDK 操作 `TtsMaker(const std::string &, int32_t)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：HARDWARE_SIDE_EFFECT。

        Args:
            text: 要处理的文本内容；编码、长度和语言支持由目标服务决定。 对应 C++ 参数 `text: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。
            speaker_id: 语音合成说话人 ID。有效编号由机器人音频服务和固件决定。 对应 C++ 参数 `speaker_id: int32_t`。 取值范围为 -2147483648 到 2147483647。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.tts_maker(text=text, speaker_id=speaker_id)
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: TtsMaker(const std::string &, int32_t)
        """
        ...
    def get_volume(self) -> tuple[int, int]:
        """查询或检查 音量。

        可用性：AVAILABLE；分类：READ_ONLY。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            [0] `status` (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。
            [1] `volume` (int): 传给该接口的 音量 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `volume: uint8_t &`。 取值范围为 0 到 255。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            status, volume = obj.get_volume()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: GetVolume(uint8_t &)
        """
        ...
    def set_volume(self, volume: int) -> int:
        """设置 音量。具体副作用和安全边界见下方状态。

        可用性：AVAILABLE；分类：HARDWARE_SIDE_EFFECT。

        Args:
            volume: 传给该接口的 音量 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `volume: uint8_t`。 取值范围为 0 到 255。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.set_volume(volume=volume)
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: SetVolume(uint8_t)
        """
        ...
    def play_stream(self, app_name: str, stream_id: str, pcm_data: Sequence[int]) -> int:
        """对应 C++ SDK 操作 `PlayStream(std::string, std::string, std::vector<uint8_t>)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：HARDWARE_SIDE_EFFECT。

        Args:
            app_name: 应用名称，用于标识音频流或播放会话。允许值和命名规则以目标服务协议为准。 对应 C++ 参数 `app_name: std::string`。 底层为字符串；长度、编码和允许值由具体协议决定。
            stream_id: 音频流标识符，用于区分同一应用下的播放流。 对应 C++ 参数 `stream_id: std::string`。 底层为字符串；长度、编码和允许值由具体协议决定。
            pcm_data: 传给该接口的 `pcm` 数据 参数，Python 类型为 `Sequence[int]`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `pcm_data: std::vector<uint8_t>`。 底层是可变长度 vector；元素约束：取值范围为 0 到 255。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.play_stream(app_name=app_name, stream_id=stream_id, pcm_data=pcm_data)
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: PlayStream(std::string, std::string, std::vector<uint8_t>)
        """
        ...
    def play_stop(self, app_name: str) -> int:
        """对应 C++ SDK 操作 `PlayStop(std::string)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：HARDWARE_SIDE_EFFECT。

        Args:
            app_name: 应用名称，用于标识音频流或播放会话。允许值和命名规则以目标服务协议为准。 对应 C++ 参数 `app_name: std::string`。 底层为字符串；长度、编码和允许值由具体协议决定。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.play_stop(app_name=app_name)
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: PlayStop(std::string)
        """
        ...
    def led_control(self, r: int, g: int, b: int) -> int:
        """对应 C++ SDK 操作 `LedControl(uint8_t, uint8_t, uint8_t)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：HARDWARE_SIDE_EFFECT。

        Args:
            r: 传给该接口的 `r` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `R: uint8_t`。 取值范围为 0 到 255。
            g: 传给该接口的 `g` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `G: uint8_t`。 取值范围为 0 到 255。
            b: 传给该接口的 `b` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `B: uint8_t`。 取值范围为 0 到 255。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.led_control(r=r, g=g, b=b)
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: LedControl(uint8_t, uint8_t, uint8_t)
        """
        ...

class JsonizeDataVecFloat(object):
    """SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

    导入：from unitree_sdk2_cpp.robot.r1 import JsonizeDataVecFloat
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `JsonizeDataVecFloat` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = JsonizeDataVecFloat()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: JsonizeDataVecFloat()
        """
        ...
    data: list[float]
    """JsonizeDataVecFloat.data：公开字段，类型为 list[float]。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    def from_json(self, value: Mapping[str, Any]) -> None:
        """从 JSON 风格字典读取字段并更新当前 SDK 值对象。

        可用性：AVAILABLE；分类：UNCLASSIFIED。

        Args:
            value: 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 对应 C++ 参数 `json: common::JsonMap &`。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            obj.from_json(value=value)
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: fromJson(common::JsonMap &)
        """
        ...
    def to_json(self) -> dict[str, Any]:
        """把当前 SDK 值对象转换为 JSON 风格字典。

        可用性：AVAILABLE；分类：UNCLASSIFIED。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (dict[str, Any]): 返回 `dict[str, Any]`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.to_json()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: toJson(common::JsonMap &) const
        """
        ...

class JsonizeVelocityCommand(object):
    """SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

    导入：from unitree_sdk2_cpp.robot.r1 import JsonizeVelocityCommand
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `JsonizeVelocityCommand` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = JsonizeVelocityCommand()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: JsonizeVelocityCommand()
        """
        ...
    velocity: list[float]
    """JsonizeVelocityCommand.velocity：公开字段，类型为 list[float]。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    duration: float
    """JsonizeVelocityCommand.duration：公开字段，类型为 float。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    def from_json(self, value: Mapping[str, Any]) -> None:
        """从 JSON 风格字典读取字段并更新当前 SDK 值对象。

        可用性：AVAILABLE；分类：UNCLASSIFIED。

        Args:
            value: 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 对应 C++ 参数 `json: common::JsonMap &`。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            obj.from_json(value=value)
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: fromJson(common::JsonMap &)
        """
        ...
    def to_json(self) -> dict[str, Any]:
        """把当前 SDK 值对象转换为 JSON 风格字典。

        可用性：AVAILABLE；分类：UNCLASSIFIED。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (dict[str, Any]): 返回 `dict[str, Any]`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.to_json()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: toJson(common::JsonMap &) const
        """
        ...

class LedControlParameter(object):
    """SDK 请求参数值类型；当前可能仅提供设计期签名。

    导入：from unitree_sdk2_cpp.robot.r1 import LedControlParameter
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `LedControlParameter` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = LedControlParameter()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: LedControlParameter()
        """
        ...
    r: int
    """LedControlParameter.r：公开字段，类型为 int。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    g: int
    """LedControlParameter.g：公开字段，类型为 int。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    b: int
    """LedControlParameter.b：公开字段，类型为 int。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    def from_json(self, value: Mapping[str, Any]) -> None:
        """从 JSON 风格字典读取字段并更新当前 SDK 值对象。

        可用性：AVAILABLE；分类：UNCLASSIFIED。

        Args:
            value: 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 对应 C++ 参数 `json: common::JsonMap &`。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            obj.from_json(value=value)
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: fromJson(common::JsonMap &)
        """
        ...
    def to_json(self) -> dict[str, Any]:
        """把当前 SDK 值对象转换为 JSON 风格字典。

        可用性：AVAILABLE；分类：UNCLASSIFIED。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (dict[str, Any]): 返回 `dict[str, Any]`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.to_json()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: toJson(common::JsonMap &) const
        """
        ...

class LocoClient(Client):
    """Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

    导入：from unitree_sdk2_cpp.robot.r1 import LocoClient
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `LocoClient` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = LocoClient()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: LocoClient()
        """
        ...
    def init(self) -> None:
        """初始化当前 SDK 对象所需的底层通道或服务资源。

        可用性：AVAILABLE；分类：INITIALIZATION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            obj.init()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: Init()
        """
        ...
    def get_fsm_id(self) -> tuple[int, int]:
        """查询或检查 FSM ID。

        可用性：AVAILABLE；分类：READ_ONLY。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            [0] `status` (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。
            [1] `fsm_id` (int): 传给该接口的 FSM ID 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `fsm_id: int &`。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            status, fsm_id = obj.get_fsm_id()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: GetFsmId(int &)
        """
        ...
    def get_fsm_mode(self) -> tuple[int, int]:
        """查询或检查 FSM 模式。

        可用性：AVAILABLE；分类：READ_ONLY。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            [0] `status` (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。
            [1] `fsm_mode` (int): 传给该接口的 FSM 模式 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `fsm_mode: int &`。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            status, fsm_mode = obj.get_fsm_mode()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: GetFsmMode(int &)
        """
        ...
    def set_fsm_id(self, fsm_id: int) -> int:
        """设置 FSM ID。具体副作用和安全边界见下方状态。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            fsm_id: 传给该接口的 FSM ID 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `fsm_id: int`。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.set_fsm_id(fsm_id=fsm_id)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: SetFsmId(int)
        """
        ...
    def set_velocity(self, vx: float, vy: float, omega: float, duration: float = 1.0) -> int:
        """设置 速度。具体副作用和安全边界见下方状态。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            vx: X 方向速度参数。坐标系、单位、符号和安全范围必须查目标型号运动协议。 对应 C++ 参数 `vx: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。
            vy: Y 方向速度参数。坐标系、单位、符号和安全范围必须查目标型号运动协议。 对应 C++ 参数 `vy: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。
            omega: 角速度参数。旋转轴、单位、符号和安全范围必须查目标型号运动协议。 对应 C++ 参数 `omega: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。
            duration: 操作持续时间参数。精确单位、范围和默认行为以目标型号接口定义为准。 对应 C++ 参数 `duration: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.set_velocity(vx=vx, vy=vy, omega=omega, duration=duration)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: SetVelocity(float, float, float, float)
        """
        ...
    def damp(self) -> int:
        """对应 C++ SDK 操作 `Damp()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.damp()
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: Damp()
        """
        ...
    def start(self) -> int:
        """启动对应 SDK 操作。具体副作用和安全边界见下方状态。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.start()
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: Start()
        """
        ...
    def stand_up(self) -> int:
        """对应 C++ SDK 操作 `StandUp()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.stand_up()
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: StandUp()
        """
        ...
    def zero_torque(self) -> int:
        """对应 C++ SDK 操作 `ZeroTorque()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.zero_torque()
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: ZeroTorque()
        """
        ...
    def stop_move(self) -> int:
        """请求停止对应 SDK 操作。该名称不等同于经过验证的物理急停。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.stop_move()
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: StopMove()
        """
        ...
    @overload
    def move(self, vx: float, vy: float, vyaw: float, continous_move: bool) -> int:
        """对应 C++ SDK 操作 `Move(float, float, float, bool)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            vx: X 方向速度参数。坐标系、单位、符号和安全范围必须查目标型号运动协议。 对应 C++ 参数 `vx: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。
            vy: Y 方向速度参数。坐标系、单位、符号和安全范围必须查目标型号运动协议。 对应 C++ 参数 `vy: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。
            vyaw: 偏航角速度参数。单位、符号和安全范围必须查目标型号运动协议。 对应 C++ 参数 `vyaw: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。
            continous_move: 传给该接口的 `continous` `move` 参数，Python 类型为 `bool`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `continous_move: bool`。 只接受布尔语义。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.move(vx=vx, vy=vy, vyaw=vyaw, continous_move=continous_move)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: Move(float, float, float, bool)
        """
        ...
    @overload
    def move(self, vx: float, vy: float, vyaw: float) -> int:
        """对应 C++ SDK 操作 `Move(float, float, float)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            vx: X 方向速度参数。坐标系、单位、符号和安全范围必须查目标型号运动协议。 对应 C++ 参数 `vx: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。
            vy: Y 方向速度参数。坐标系、单位、符号和安全范围必须查目标型号运动协议。 对应 C++ 参数 `vy: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。
            vyaw: 偏航角速度参数。单位、符号和安全范围必须查目标型号运动协议。 对应 C++ 参数 `vyaw: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.move(vx=vx, vy=vy, vyaw=vyaw)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: Move(float, float, float)
        """
        ...
    def switch_move_mode(self, flag: bool) -> int:
        """对应 C++ SDK 操作 `SwitchMoveMode(bool)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            flag: 布尔开关。`True` 和 `False` 的具体业务效果由当前方法定义。 对应 C++ 参数 `flag: bool`。 只接受布尔语义。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.switch_move_mode(flag=flag)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: SwitchMoveMode(bool)
        """
        ...
    def set_speed_mode(self, speed_mode: int) -> int:
        """设置 速度 模式。具体副作用和安全边界见下方状态。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            speed_mode: 传给该接口的 速度 模式 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `speed_mode: int`。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.set_speed_mode(speed_mode=speed_mode)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: SetSpeedMode(int)
        """
        ...

class PlayStopParameter(object):
    """SDK 请求参数值类型；当前可能仅提供设计期签名。

    导入：from unitree_sdk2_cpp.robot.r1 import PlayStopParameter
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `PlayStopParameter` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = PlayStopParameter()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: PlayStopParameter()
        """
        ...
    app_name: str
    """PlayStopParameter.app_name：公开字段，类型为 str。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    def from_json(self, value: Mapping[str, Any]) -> None:
        """从 JSON 风格字典读取字段并更新当前 SDK 值对象。

        可用性：AVAILABLE；分类：UNCLASSIFIED。

        Args:
            value: 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 对应 C++ 参数 `json: common::JsonMap &`。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            obj.from_json(value=value)
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: fromJson(common::JsonMap &)
        """
        ...
    def to_json(self) -> dict[str, Any]:
        """把当前 SDK 值对象转换为 JSON 风格字典。

        可用性：AVAILABLE；分类：UNCLASSIFIED。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (dict[str, Any]): 返回 `dict[str, Any]`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.to_json()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: toJson(common::JsonMap &) const
        """
        ...

class PlayStreamParameter(object):
    """SDK 请求参数值类型；当前可能仅提供设计期签名。

    导入：from unitree_sdk2_cpp.robot.r1 import PlayStreamParameter
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `PlayStreamParameter` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = PlayStreamParameter()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: PlayStreamParameter()
        """
        ...
    app_name: str
    """PlayStreamParameter.app_name：公开字段，类型为 str。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    stream_id: str
    """PlayStreamParameter.stream_id：公开字段，类型为 str。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    def from_json(self, value: Mapping[str, Any]) -> None:
        """从 JSON 风格字典读取字段并更新当前 SDK 值对象。

        可用性：AVAILABLE；分类：UNCLASSIFIED。

        Args:
            value: 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 对应 C++ 参数 `json: common::JsonMap &`。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            obj.from_json(value=value)
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: fromJson(common::JsonMap &)
        """
        ...
    def to_json(self) -> dict[str, Any]:
        """把当前 SDK 值对象转换为 JSON 风格字典。

        可用性：AVAILABLE；分类：UNCLASSIFIED。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (dict[str, Any]): 返回 `dict[str, Any]`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.to_json()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: toJson(common::JsonMap &) const
        """
        ...

class TtsMakerParameter(object):
    """SDK 请求参数值类型；当前可能仅提供设计期签名。

    导入：from unitree_sdk2_cpp.robot.r1 import TtsMakerParameter
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `TtsMakerParameter` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = TtsMakerParameter()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: TtsMakerParameter()
        """
        ...
    index: int
    """TtsMakerParameter.index：公开字段，类型为 int。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    speaker_id: int
    """TtsMakerParameter.speaker_id：公开字段，类型为 int。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    text: str
    """TtsMakerParameter.text：公开字段，类型为 str。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    def from_json(self, value: Mapping[str, Any]) -> None:
        """从 JSON 风格字典读取字段并更新当前 SDK 值对象。

        可用性：AVAILABLE；分类：UNCLASSIFIED。

        Args:
            value: 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 对应 C++ 参数 `json: common::JsonMap &`。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            obj.from_json(value=value)
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: fromJson(common::JsonMap &)
        """
        ...
    def to_json(self) -> dict[str, Any]:
        """把当前 SDK 值对象转换为 JSON 风格字典。

        可用性：AVAILABLE；分类：UNCLASSIFIED。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (dict[str, Any]): 返回 `dict[str, Any]`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.to_json()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: toJson(common::JsonMap &) const
        """
        ...
