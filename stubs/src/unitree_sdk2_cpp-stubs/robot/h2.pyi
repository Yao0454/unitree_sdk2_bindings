"""Full SDK signature preview; see api_manifest.json for availability."""
from __future__ import annotations

import enum
from collections.abc import Callable, Mapping, Sequence
from typing import Any, overload

from . import Client, ClientBase

class FsmIdInfo(object):
    """SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

    导入：from unitree_sdk2_cpp.robot.h2 import FsmIdInfo
    构造可用性：AVAILABLE。
    """
    @overload
    def __init__(self) -> None:
        """初始化 `FsmIdInfo` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = FsmIdInfo()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: FsmIdInfo()
        """
        ...
    @overload
    def __init__(self, i: int, n: str) -> None:
        """初始化 `FsmIdInfo` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            i: 传给该接口的 `i` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `i: int`。
            n: 传给该接口的 `n` 参数，Python 类型为 `str`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `n: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = FsmIdInfo(i=i, n=n)
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: FsmIdInfo(int, const std::string &)
        """
        ...
    id: int
    """FsmIdInfo.id：公开字段，类型为 int。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    name: str
    """FsmIdInfo.name：公开字段，类型为 str。
    具体单位及允许值以对应 SDK 数据结构为准。
    """

class H2ArmActionClient(Client):
    """Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

    导入：from unitree_sdk2_cpp.robot.h2 import H2ArmActionClient
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `H2ArmActionClient` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = H2ArmActionClient()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: H2ArmActionClient()
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
    @overload
    def execute_action(self, action_id: int) -> int:
        """对应 C++ SDK 操作 `ExecuteAction(int32_t)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            action_id: 从 get_action_list() 查询并确认的动作 ID。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.execute_action(action_id=action_id)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: ExecuteAction(int32_t)
        """
        ...
    @overload
    def execute_action(self, action_name: str) -> int:
        """对应 C++ SDK 操作 `ExecuteAction(const std::string &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            action_name: 已在机器人端配置的自定义动作名称。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.execute_action(action_name=action_name)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: ExecuteAction(const std::string &)
        """
        ...
    def stop_custom_action(self) -> int:
        """请求停止对应 SDK 操作。该名称不等同于经过验证的物理急停。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.stop_custom_action()
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: StopCustomAction()
        """
        ...
    def get_action_list(self) -> tuple[int, str]:
        """查询或检查 `action` `list`。

        可用性：AVAILABLE；分类：READ_ONLY。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            [0] `status` (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。
            [1] `data` (str): 传给该接口的 数据 参数，Python 类型为 `str`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `data: std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            status, data = obj.get_action_list()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: GetActionList(std::string &)
        """
        ...

class JsonizeArmActionCommand(object):
    """SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

    导入：from unitree_sdk2_cpp.robot.h2 import JsonizeArmActionCommand
    构造可用性：AVAILABLE。
    """
    action_id: int
    """JsonizeArmActionCommand.action_id：公开字段，类型为 int。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    def __init__(self) -> None:
        """初始化 `JsonizeArmActionCommand` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = JsonizeArmActionCommand()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: JsonizeArmActionCommand()
        """
        ...
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

class JsonizeArmActionName(object):
    """SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

    导入：from unitree_sdk2_cpp.robot.h2 import JsonizeArmActionName
    构造可用性：AVAILABLE。
    """
    action_name: str
    """JsonizeArmActionName.action_name：公开字段，类型为 str。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    def __init__(self) -> None:
        """初始化 `JsonizeArmActionName` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = JsonizeArmActionName()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: JsonizeArmActionName()
        """
        ...
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

class JsonizeDataVecFloat(object):
    """SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

    导入：from unitree_sdk2_cpp.robot.h2 import JsonizeDataVecFloat
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

class JsonizeFsmIdList(object):
    """SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

    导入：from unitree_sdk2_cpp.robot.h2 import JsonizeFsmIdList
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `JsonizeFsmIdList` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = JsonizeFsmIdList()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: JsonizeFsmIdList()
        """
        ...
    fsm_ids: list[FsmIdInfo]
    """JsonizeFsmIdList.fsm_ids：公开字段，类型为 list[FsmIdInfo]。
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

    导入：from unitree_sdk2_cpp.robot.h2 import JsonizeVelocityCommand
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

class LocoClient(Client):
    """Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

    导入：from unitree_sdk2_cpp.robot.h2 import LocoClient
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
    def get_balance_mode(self) -> tuple[int, int]:
        """查询或检查 平衡 模式。

        可用性：AVAILABLE；分类：READ_ONLY。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            [0] `status` (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。
            [1] `balance_mode` (int): 传给该接口的 平衡 模式 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `balance_mode: int &`。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            status, balance_mode = obj.get_balance_mode()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: GetBalanceMode(int &)
        """
        ...
    def get_swing_height(self) -> tuple[int, float]:
        """查询或检查 `swing` 高度。

        可用性：AVAILABLE；分类：READ_ONLY。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            [0] `status` (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。
            [1] `swing_height` (float): 传给该接口的 `swing` 高度 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `swing_height: float &`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            status, swing_height = obj.get_swing_height()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: GetSwingHeight(float &)
        """
        ...
    def get_stand_height(self) -> tuple[int, float]:
        """查询或检查 `stand` 高度。

        可用性：AVAILABLE；分类：READ_ONLY。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            [0] `status` (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。
            [1] `stand_height` (float): 传给该接口的 `stand` 高度 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `stand_height: float &`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            status, stand_height = obj.get_stand_height()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: GetStandHeight(float &)
        """
        ...
    def get_phase(self) -> tuple[int, list[float]]:
        """查询或检查 相位。

        可用性：AVAILABLE；分类：READ_ONLY。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            [0] `status` (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。
            [1] `phase` (list[float]): 传给该接口的 相位 参数，Python 类型为 `list[float]`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `phase: std::vector<float> &`。 底层是可变长度 vector；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            status, phase = obj.get_phase()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: GetPhase(std::vector<float> &)
        """
        ...
    def get_arm_sdk_status(self) -> tuple[int, bool]:
        """查询或检查 机械臂 SDK 状态。

        可用性：AVAILABLE；分类：READ_ONLY。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            [0] `status` (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。
            [1] `arm_sdk_status` (bool): 传给该接口的 机械臂 SDK 状态 参数，Python 类型为 `bool`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `arm_sdk_status: bool &`。 只接受布尔语义。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            status, arm_sdk_status = obj.get_arm_sdk_status()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: GetArmSdkStatus(bool &)
        """
        ...
    def get_available_fsm_ids(self) -> tuple[int, list[int], list[str]]:
        """查询或检查 `available` FSM ID 列表。

        可用性：AVAILABLE；分类：READ_ONLY。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            [0] `status` (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。
            [1] `ids` (list[int]): 传给该接口的 ID 列表 参数，Python 类型为 `list[int]`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `ids: std::vector<int> &`。 底层是可变长度 vector
            [2] `names` (list[str]): 传给该接口的 名称列表 参数，Python 类型为 `list[str]`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `names: std::vector<std::string> &`。 底层是可变长度 vector；元素约束：底层为字符串；长度、编码和允许值由具体协议决定。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            status, ids, names = obj.get_available_fsm_ids()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: GetAvailableFsmIds(std::vector<int> &, std::vector<std::string> &)
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
    def set_balance_mode(self, balance_mode: int) -> int:
        """设置 平衡 模式。具体副作用和安全边界见下方状态。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            balance_mode: 传给该接口的 平衡 模式 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `balance_mode: int`。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.set_balance_mode(balance_mode=balance_mode)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: SetBalanceMode(int)
        """
        ...
    def set_punch_api(self, punch_api: Sequence[float]) -> int:
        """设置 `punch` API。具体副作用和安全边界见下方状态。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            punch_api: 传给该接口的 `punch` API 参数，Python 类型为 `Sequence[float]`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `punch_api: std::vector<float> &`。 底层是可变长度 vector；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.set_punch_api(punch_api=punch_api)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: SetPunchApi(std::vector<float> &)
        """
        ...
    def set_swing_height(self, swing_height: float) -> int:
        """设置 `swing` 高度。具体副作用和安全边界见下方状态。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            swing_height: 传给该接口的 `swing` 高度 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `swing_height: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.set_swing_height(swing_height=swing_height)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: SetSwingHeight(float)
        """
        ...
    def set_stand_height(self, stand_height: float) -> int:
        """设置 `stand` 高度。具体副作用和安全边界见下方状态。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            stand_height: 传给该接口的 `stand` 高度 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `stand_height: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.set_stand_height(stand_height=stand_height)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: SetStandHeight(float)
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
    def set_task_id(self, task_id: int) -> int:
        """设置 任务 ID。具体副作用和安全边界见下方状态。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            task_id: 传给该接口的 任务 ID 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `task_id: int`。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.set_task_id(task_id=task_id)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: SetTaskId(int)
        """
        ...
    def set_arm_sdk_status(self, arm_sdk_status: bool) -> int:
        """设置 机械臂 SDK 状态。具体副作用和安全边界见下方状态。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            arm_sdk_status: 传给该接口的 机械臂 SDK 状态 参数，Python 类型为 `bool`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `arm_sdk_status: bool`。 只接受布尔语义。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.set_arm_sdk_status(arm_sdk_status=arm_sdk_status)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: SetArmSdkStatus(bool)
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
    def squat(self) -> int:
        """对应 C++ SDK 操作 `Squat()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.squat()
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: Squat()
        """
        ...
    def sit(self) -> int:
        """对应 C++ SDK 操作 `Sit()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.sit()
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: Sit()
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
    def high_stand(self) -> int:
        """对应 C++ SDK 操作 `HighStand()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.high_stand()
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: HighStand()
        """
        ...
    def low_stand(self) -> int:
        """对应 C++ SDK 操作 `LowStand()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.low_stand()
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: LowStand()
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
    def continuous_gait(self, flag: bool) -> int:
        """对应 C++ SDK 操作 `ContinuousGait(bool)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            flag: 布尔开关。`True` 和 `False` 的具体业务效果由当前方法定义。 对应 C++ 参数 `flag: bool`。 只接受布尔语义。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.continuous_gait(flag=flag)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: ContinuousGait(bool)
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
    def wave_hand(self, turn_flag: bool = False) -> int:
        """对应 C++ SDK 操作 `WaveHand(bool)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            turn_flag: 传给该接口的 `turn` `flag` 参数，Python 类型为 `bool`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `turn_flag: bool`。 只接受布尔语义。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.wave_hand(turn_flag=turn_flag)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: WaveHand(bool)
        """
        ...
    def shake_hand(self, stage: int = -1) -> int:
        """对应 C++ SDK 操作 `ShakeHand(int)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            stage: 传给该接口的 `stage` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `stage: int`。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.shake_hand(stage=stage)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: ShakeHand(int)
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
    def enable_arm_sdk(self) -> int:
        """对应 C++ SDK 操作 `EnableArmSDK()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.enable_arm_sdk()
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: EnableArmSDK()
        """
        ...
    def disable_arm_sdk(self) -> int:
        """对应 C++ SDK 操作 `DisableArmSDK()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.disable_arm_sdk()
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: DisableArmSDK()
        """
        ...
