"""Full SDK signature preview; see api_manifest.json for availability."""
from __future__ import annotations

import enum
from collections.abc import Callable, Mapping, Sequence
from typing import Any, overload

from . import Client, ClientBase

class AudioClient(Client):
    """Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

    导入：from unitree_sdk2_cpp.robot.a2 import AudioClient
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

class LedControlParameter(object):
    """SDK 请求参数值类型；当前可能仅提供设计期签名。

    导入：from unitree_sdk2_cpp.robot.a2 import LedControlParameter
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

class PathPoint(object):
    """SDK 数据值类型；公开字段和转换方法见下文。

    导入：from unitree_sdk2_cpp.robot.a2 import PathPoint
    构造可用性：AVAILABLE。
    """
    t_from_start: float
    """PathPoint.t_from_start：公开字段，类型为 float。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    x: float
    """PathPoint.x：公开字段，类型为 float。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    y: float
    """PathPoint.y：公开字段，类型为 float。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    yaw: float
    """PathPoint.yaw：公开字段，类型为 float。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    def __init__(self) -> None:
        """初始化 `PathPoint` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = PathPoint()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: PathPoint()
        """
        ...

class PlayStopParameter(object):
    """SDK 请求参数值类型；当前可能仅提供设计期签名。

    导入：from unitree_sdk2_cpp.robot.a2 import PlayStopParameter
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

    导入：from unitree_sdk2_cpp.robot.a2 import PlayStreamParameter
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

class PoseVec4(object):
    """SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

    导入：from unitree_sdk2_cpp.robot.a2 import PoseVec4
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `PoseVec4` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = PoseVec4()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: PoseVec4()
        """
        ...
    x: float
    """PoseVec4.x：公开字段，类型为 float。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    y: float
    """PoseVec4.y：公开字段，类型为 float。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    z: float
    """PoseVec4.z：公开字段，类型为 float。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    yaw: float
    """PoseVec4.yaw：公开字段，类型为 float。
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

class SportClient(Client):
    """Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

    导入：from unitree_sdk2_cpp.robot.a2 import SportClient
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `SportClient` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = SportClient()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: SportClient()
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
    def balance_stand(self) -> int:
        """对应 C++ SDK 操作 `BalanceStand()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.balance_stand()
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: BalanceStand()
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
    def stand_down(self) -> int:
        """对应 C++ SDK 操作 `StandDown()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.stand_down()
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: StandDown()
        """
        ...
    def recovery_stand(self) -> int:
        """对应 C++ SDK 操作 `RecoveryStand()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.recovery_stand()
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: RecoveryStand()
        """
        ...
    def euler(self, roll: float, pitch: float, yaw: float) -> int:
        """对应 C++ SDK 操作 `Euler(float, float, float)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            roll: 传给该接口的 `roll` 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `roll: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。
            pitch: 传给该接口的 `pitch` 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `pitch: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。
            yaw: 偏航角或偏航目标参数。参考系、单位和范围必须查目标型号协议。 对应 C++ 参数 `yaw: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.euler(roll=roll, pitch=pitch, yaw=yaw)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: Euler(float, float, float)
        """
        ...
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
    def switch_gait(self, gait_type: int) -> int:
        """对应 C++ SDK 操作 `SwitchGait(int)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            gait_type: 传给该接口的 `gait` `type` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `gait_type: int`。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.switch_gait(gait_type=gait_type)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: SwitchGait(int)
        """
        ...
    def body_height(self, height: float) -> int:
        """对应 C++ SDK 操作 `BodyHeight(float)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            height: 传给该接口的 高度 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `height: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.body_height(height=height)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: BodyHeight(float)
        """
        ...
    def speed_level(self, level: int) -> int:
        """对应 C++ SDK 操作 `SpeedLevel(int)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            level: 传给该接口的 `level` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `level: int`。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.speed_level(level=level)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: SpeedLevel(int)
        """
        ...
    def body_position(self, x: float, y: float, z: float, yaw: float) -> int:
        """对应 C++ SDK 操作 `BodyPosition(float, float, float, float)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            x: X 方向位置或分量参数。参考系、单位和范围必须查当前方法及目标型号协议。 对应 C++ 参数 `x: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。
            y: Y 方向位置或分量参数。参考系、单位和范围必须查当前方法及目标型号协议。 对应 C++ 参数 `y: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。
            z: Z 方向位置或分量参数。参考系、单位和范围必须查当前方法及目标型号协议。 对应 C++ 参数 `z: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。
            yaw: 偏航角或偏航目标参数。参考系、单位和范围必须查目标型号协议。 对应 C++ 参数 `yaw: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.body_position(x=x, y=y, z=z, yaw=yaw)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: BodyPosition(float, float, float, float)
        """
        ...
    def left_side_gait(self, enter: int) -> int:
        """对应 C++ SDK 操作 `LeftSideGait(int)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            enter: 传给该接口的 `enter` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `enter: int`。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.left_side_gait(enter=enter)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: LeftSideGait(int)
        """
        ...
    def right_side_gait(self, enter: int) -> int:
        """对应 C++ SDK 操作 `RightSideGait(int)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            enter: 传给该接口的 `enter` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `enter: int`。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.right_side_gait(enter=enter)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: RightSideGait(int)
        """
        ...
    def hand_stand(self, enter: int) -> int:
        """对应 C++ SDK 操作 `HandStand(int)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            enter: 传给该接口的 `enter` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `enter: int`。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.hand_stand(enter=enter)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: HandStand(int)
        """
        ...
    def biped_stand(self, enter: int) -> int:
        """对应 C++ SDK 操作 `BipedStand(int)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            enter: 传给该接口的 `enter` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `enter: int`。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.biped_stand(enter=enter)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: BipedStand(int)
        """
        ...
    def front_flip(self) -> int:
        """对应 C++ SDK 操作 `FrontFlip()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.front_flip()
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: FrontFlip()
        """
        ...
    def back_flip(self) -> int:
        """对应 C++ SDK 操作 `BackFlip()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.back_flip()
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: BackFlip()
        """
        ...
    def reset_estimator(self) -> int:
        """对应 C++ SDK 操作 `ResetEstimator()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.reset_estimator()
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: ResetEstimator()
        """
        ...
    def trajectory(self, path: Sequence[PathPoint], feedback_mode: int = 0, external_x: float = 0.0, external_y: float = 0.0, external_yaw: float = 0.0) -> int:
        """对应 C++ SDK 操作 `Trajectory(const std::vector<PathPoint> &, int, float, float, float)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            path: 传给该接口的 `path` 参数，Python 类型为 `Sequence[PathPoint]`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `path: const std::vector<PathPoint> &`。 底层是可变长度 vector
            feedback_mode: 传给该接口的 `feedback` 模式 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `feedback_mode: int`。
            external_x: 传给该接口的 `external` `x` 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `external_x: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。
            external_y: 传给该接口的 `external` `y` 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `external_y: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。
            external_yaw: 传给该接口的 `external` `yaw` 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `external_yaw: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.trajectory(path=path, feedback_mode=feedback_mode, external_x=external_x, external_y=external_y, external_yaw=external_yaw)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: Trajectory(const std::vector<PathPoint> &, int, float, float, float)
        """
        ...
    def set_auto_recovery(self, switch_on: int) -> int:
        """设置 `auto` `recovery`。具体副作用和安全边界见下方状态。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            switch_on: 传给该接口的 开关 `on` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `switch_on: int`。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.set_auto_recovery(switch_on=switch_on)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: SetAutoRecovery(int)
        """
        ...
    def get_state(self) -> tuple[int, dict[str, str]]:
        """查询或检查 状态。

        可用性：AVAILABLE；分类：READ_ONLY。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            [0] `status` (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。
            [1] `state_map` (dict[str, str]): 传给该接口的 状态 `map` 参数，Python 类型为 `dict[str, str]`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `state_map: std::map<std::string, std::string> &`。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            status, state_map = obj.get_state()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: GetState(std::map<std::string, std::string> &)
        """
        ...

class TtsMakerParameter(object):
    """SDK 请求参数值类型；当前可能仅提供设计期签名。

    导入：from unitree_sdk2_cpp.robot.a2 import TtsMakerParameter
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
