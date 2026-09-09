"""Full SDK signature preview; see api_manifest.json for availability."""
from __future__ import annotations

import enum
from collections.abc import Callable, Mapping, Sequence
from typing import Any, overload

class ApplyLeaseData(object):
    """SDK 数据值类型；公开字段和转换方法见下文。

    导入：from unitree_sdk2_cpp.robot import ApplyLeaseData
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `ApplyLeaseData` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = ApplyLeaseData()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: ApplyLeaseData()
        """
        ...
    id: int
    """ApplyLeaseData.id：公开字段，类型为 int。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    term: int
    """ApplyLeaseData.term：公开字段，类型为 int。
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

class ApplyLeaseParameter(object):
    """SDK 请求参数值类型；当前可能仅提供设计期签名。

    导入：from unitree_sdk2_cpp.robot import ApplyLeaseParameter
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `ApplyLeaseParameter` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = ApplyLeaseParameter()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: ApplyLeaseParameter()
        """
        ...
    name: str
    """ApplyLeaseParameter.name：公开字段，类型为 str。
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

class ChannelFactory(object):
    """SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

    导入：from unitree_sdk2_cpp.robot import ChannelFactory
    """
    def instance(self) -> ChannelFactory:
        """对应 C++ SDK 操作 `Instance()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：SIGNATURE_ONLY；分类：UNCLASSIFIED。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (ChannelFactory): 返回 `ChannelFactory`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_instance(obj: ChannelFactory) -> ChannelFactory:
                    return obj.instance()
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Instance()
        """
        ...
    @overload
    def init(self, domain_id: int, network_interface: str = ...) -> None:
        """初始化当前 SDK 对象所需的底层通道或服务资源。

        可用性：SIGNATURE_ONLY；分类：UNCLASSIFIED。

        Args:
            domain_id: DDS Domain ID。只有使用兼容 domain 的参与者才能按预期互相发现。 对应 C++ 参数 `domainId: int32_t`。 取值范围为 -2147483648 到 2147483647。
            network_interface: DDS 使用的网络接口名称，例如 Linux 上的 `eth0` 或 `enp3s0`；必须按目标机实际网卡填写。 对应 C++ 参数 `networkInterface: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_init(obj: ChannelFactory, domain_id: int, network_interface: str) -> None:
                    obj.init(domain_id=domain_id, network_interface=network_interface)
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Init(int32_t, const std::string &)
        """
        ...
    @overload
    def init(self, config_file_name: str = ...) -> None:
        """初始化当前 SDK 对象所需的底层通道或服务资源。

        可用性：SIGNATURE_ONLY；分类：UNCLASSIFIED。

        Args:
            config_file_name: 传给该接口的 配置 `file` 名称 参数，Python 类型为 `str`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `configFileName: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_init(obj: ChannelFactory, config_file_name: str) -> None:
                    obj.init(config_file_name=config_file_name)
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Init(const std::string &)
        """
        ...
    @overload
    def init(self, json_map: dict[str, Any]) -> None:
        """初始化当前 SDK 对象所需的底层通道或服务资源。

        可用性：SIGNATURE_ONLY；分类：UNCLASSIFIED。

        Args:
            json_map: 传给该接口的 `json` `map` 参数，Python 类型为 `dict[str, Any]`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `jsonMap: const common::JsonMap &`。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_init(obj: ChannelFactory, json_map: dict[str, Any]) -> None:
                    obj.init(json_map=json_map)
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Init(const common::JsonMap &)
        """
        ...
    def release(self) -> None:
        """对应 C++ SDK 操作 `Release()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：SIGNATURE_ONLY；分类：UNCLASSIFIED。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_release(obj: ChannelFactory) -> None:
                    obj.release()
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Release()
        """
        ...

class ChannelNamer(object):
    """SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

    导入：from unitree_sdk2_cpp.robot import ChannelNamer
    """
    def get_send_channel_name(self, name: str) -> str:
        """查询或检查 `send` `channel` 名称。

        可用性：SIGNATURE_ONLY；分类：UNCLASSIFIED。

        Args:
            name: SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。

        Returns:
            返回值 (str): 返回 `str`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_get_send_channel_name(obj: ChannelNamer, name: str) -> str:
                    return obj.get_send_channel_name(name=name)
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: GetSendChannelName(const std::string &)
        """
        ...
    def get_recv_channel_name(self, name: str) -> str:
        """查询或检查 `recv` `channel` 名称。

        可用性：SIGNATURE_ONLY；分类：UNCLASSIFIED。

        Args:
            name: SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。

        Returns:
            返回值 (str): 返回 `str`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_get_recv_channel_name(obj: ChannelNamer, name: str) -> str:
                    return obj.get_recv_channel_name(name=name)
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: GetRecvChannelName(const std::string &)
        """
        ...

class Client(ClientBase):
    """Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

    导入：from unitree_sdk2_cpp.robot import Client
    构造可用性：SIGNATURE_ONLY。
    """
    def __init__(self, name: str, enable_lease: bool = False) -> None:
        """初始化 `Client` 实例。是否能实际构造取决于下方可用性状态。

        可用性：SIGNATURE_ONLY；分类：CONSTRUCTION。

        Args:
            name: SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。
            enable_lease: 是否启用 SDK lease 机制；lease 的获得、续期和释放规则以服务协议为准。 对应 C++ 参数 `enableLease: bool`。 只接受布尔语义。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_construct(name: str, enable_lease: bool) -> Client:
                    return Client(name=name, enable_lease=enable_lease)
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: Client(const std::string &, bool)
        """
        ...
    def wait_lease_applied(self) -> None:
        """对应 C++ SDK 操作 `WaitLeaseApplied()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：INITIALIZATION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            obj.wait_lease_applied()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: WaitLeaseApplied()
        """
        ...
    def get_lease_id(self) -> int:
        """查询或检查 lease ID。

        可用性：SIGNATURE_ONLY；分类：READ_ONLY。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (int): 返回 `int`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_get_lease_id(obj: Client) -> int:
                    return obj.get_lease_id()
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: GetLeaseId()
        """
        ...
    def get_api_version(self) -> str:
        """查询或检查 API `version`。

        可用性：AVAILABLE；分类：READ_ONLY。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (str): 返回 `str`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.get_api_version()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: GetApiVersion() const
        """
        ...
    def get_server_api_version(self) -> str:
        """查询或检查 `server` API `version`。

        可用性：AVAILABLE；分类：READ_ONLY。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (str): 返回 `str`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.get_server_api_version()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: GetServerApiVersion()
        """
        ...

class ClientBase(object):
    """SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

    导入：from unitree_sdk2_cpp.robot import ClientBase
    构造可用性：SIGNATURE_ONLY。
    """
    def __init__(self, name: str) -> None:
        """初始化 `ClientBase` 实例。是否能实际构造取决于下方可用性状态。

        可用性：SIGNATURE_ONLY；分类：CONSTRUCTION。

        Args:
            name: SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_construct(name: str) -> ClientBase:
                    return ClientBase(name=name)
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: ClientBase(const std::string &)
        """
        ...
    def init(self) -> None:
        """初始化当前 SDK 对象所需的底层通道或服务资源。

        可用性：SIGNATURE_ONLY；分类：INITIALIZATION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_init(obj: ClientBase) -> None:
                    obj.init()
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Init()
        """
        ...
    def set_timeout_microseconds(self, microseconds: int) -> None:
        """设置客户端 RPC 超时时间，单位为微秒。

        可用性：AVAILABLE；分类：INITIALIZATION。

        Args:
            microseconds: 客户端请求超时，单位为微秒。 对应 C++ 参数 `timeout: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            client.set_timeout_microseconds(microseconds=5_000_000)
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: SetTimeout(int64_t)
        """
        ...
    def set_timeout(self, seconds: float) -> None:
        """设置客户端 RPC 超时时间，单位为秒。

        可用性：AVAILABLE；分类：INITIALIZATION。

        Args:
            seconds: 客户端请求超时，单位为秒。 对应 C++ 参数 `timeout: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            client.set_timeout(seconds=5.0)
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: SetTimeout(float)
        """
        ...

class ClientChannelNamer(ChannelNamer):
    """SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

    导入：from unitree_sdk2_cpp.robot import ClientChannelNamer
    构造可用性：SIGNATURE_ONLY。
    """
    def __init__(self) -> None:
        """初始化 `ClientChannelNamer` 实例。是否能实际构造取决于下方可用性状态。

        可用性：SIGNATURE_ONLY；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_construct() -> ClientChannelNamer:
                    return ClientChannelNamer()
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: ClientChannelNamer()
        """
        ...

class ClientStub(object):
    """SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

    导入：from unitree_sdk2_cpp.robot import ClientStub
    构造可用性：SIGNATURE_ONLY。
    """
    def __init__(self) -> None:
        """初始化 `ClientStub` 实例。是否能实际构造取决于下方可用性状态。

        可用性：SIGNATURE_ONLY；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_construct() -> ClientStub:
                    return ClientStub()
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: ClientStub()
        """
        ...
    def init(self, name: str) -> None:
        """初始化当前 SDK 对象所需的底层通道或服务资源。

        可用性：SIGNATURE_ONLY；分类：INITIALIZATION。

        Args:
            name: SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_init(obj: ClientStub, name: str) -> None:
                    obj.init(name=name)
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Init(const std::string &)
        """
        ...
    def send(self, req: Any, wait_timeout: int) -> bool:
        """对应 C++ SDK 操作 `Send(const unitree::robot::Request &, int64_t)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：SIGNATURE_ONLY；分类：HARDWARE_SIDE_EFFECT。

        Args:
            req: 传给该接口的 `req` 参数，Python 类型为 `Any`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `req: const unitree::robot::Request &`。
            wait_timeout: 请求等待超时参数；精确单位沿用对应 C++ 接口定义。 对应 C++ 参数 `waitTimeout: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。

        Returns:
            返回值 (bool): 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_send(obj: ClientStub, req: Any, wait_timeout: int) -> bool:
                    return obj.send(req=req, wait_timeout=wait_timeout)
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Send(const unitree::robot::Request &, int64_t)
        """
        ...
    def send_request(self, req: Any, wait_timeout: int) -> RequestFuture:
        """对应 C++ SDK 操作 `SendRequest(const unitree::robot::Request &, int64_t)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：SIGNATURE_ONLY；分类：HARDWARE_SIDE_EFFECT。

        Args:
            req: 传给该接口的 `req` 参数，Python 类型为 `Any`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `req: const unitree::robot::Request &`。
            wait_timeout: 请求等待超时参数；精确单位沿用对应 C++ 接口定义。 对应 C++ 参数 `waitTimeout: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。

        Returns:
            返回值 (RequestFuture): 返回 `RequestFuture`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_send_request(obj: ClientStub, req: Any, wait_timeout: int) -> RequestFuture:
                    return obj.send_request(req=req, wait_timeout=wait_timeout)
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: SendRequest(const unitree::robot::Request &, int64_t)
        """
        ...

class LeaseCache(object):
    """SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

    导入：from unitree_sdk2_cpp.robot import LeaseCache
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `LeaseCache` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = LeaseCache()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: LeaseCache()
        """
        ...
    def set(self, id: int, m_name: str, last_modified: int = 0) -> None:
        """对应 C++ SDK 操作 `Set(int64_t, const std::string &, int64_t)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：UNCLASSIFIED。

        Args:
            id: 传给该接口的 ID 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `id: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。
            m_name: 传给该接口的 `m` 名称 参数，Python 类型为 `str`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `mName: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。
            last_modified: 传给该接口的 `last` `modified` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `lastModified: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            obj.set(id=id, m_name=m_name, last_modified=last_modified)
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Set(int64_t, const std::string &, int64_t)
        """
        ...
    def renewal(self, last_modified: int = 0) -> None:
        """对应 C++ SDK 操作 `Renewal(int64_t)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：UNCLASSIFIED。

        Args:
            last_modified: 传给该接口的 `last` `modified` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `lastModified: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            obj.renewal(last_modified=last_modified)
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Renewal(int64_t)
        """
        ...
    def clear(self) -> None:
        """对应 C++ SDK 操作 `Clear()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：UNCLASSIFIED。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            obj.clear()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Clear()
        """
        ...
    def get_last_modified(self) -> int:
        """查询或检查 `last` `modified`。

        可用性：AVAILABLE；分类：UNCLASSIFIED。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (int): 返回 `int`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.get_last_modified()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: GetLastModified() const
        """
        ...
    def get_id(self) -> int:
        """查询或检查 ID。

        可用性：AVAILABLE；分类：UNCLASSIFIED。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (int): 返回 `int`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.get_id()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: GetId() const
        """
        ...
    def get_name(self) -> str:
        """查询或检查 名称。

        可用性：AVAILABLE；分类：UNCLASSIFIED。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (str): 返回 `str`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.get_name()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: GetName() const
        """
        ...

class LeaseClient(ClientBase):
    """Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

    导入：from unitree_sdk2_cpp.robot import LeaseClient
    构造可用性：AVAILABLE。
    """
    def __init__(self, name: str) -> None:
        """初始化 `LeaseClient` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            name: SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = LeaseClient(name=name)
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: LeaseClient(const std::string &)
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
    def wait_applied(self) -> None:
        """对应 C++ SDK 操作 `WaitApplied()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：INITIALIZATION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            obj.wait_applied()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: WaitApplied()
        """
        ...
    def get_id(self) -> int:
        """查询或检查 ID。

        可用性：AVAILABLE；分类：READ_ONLY。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (int): 返回 `int`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.get_id()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: GetId()
        """
        ...
    def applied(self) -> bool:
        """对应 C++ SDK 操作 `Applied()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：READ_ONLY。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (bool): 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.applied()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: Applied()
        """
        ...

class LeaseContext(object):
    """SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

    导入：from unitree_sdk2_cpp.robot import LeaseContext
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `LeaseContext` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = LeaseContext()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: LeaseContext()
        """
        ...
    def update(self, id: int, term: int) -> None:
        """对应 C++ SDK 操作 `Update(int64_t, int64_t)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：UNCLASSIFIED。

        Args:
            id: 传给该接口的 ID 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `id: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。
            term: 传给该接口的 `term` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `term: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            obj.update(id=id, term=term)
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Update(int64_t, int64_t)
        """
        ...
    def reset(self) -> None:
        """对应 C++ SDK 操作 `Reset()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：UNCLASSIFIED。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            obj.reset()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Reset()
        """
        ...
    def valid(self) -> bool:
        """对应 C++ SDK 操作 `Valid() const`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：UNCLASSIFIED。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (bool): 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.valid()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Valid() const
        """
        ...
    def get_id(self) -> int:
        """查询或检查 ID。

        可用性：AVAILABLE；分类：UNCLASSIFIED。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (int): 返回 `int`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.get_id()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: GetId() const
        """
        ...
    def get_term(self) -> int:
        """查询或检查 `term`。

        可用性：AVAILABLE；分类：UNCLASSIFIED。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (int): 返回 `int`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.get_term()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: GetTerm() const
        """
        ...

class LeaseServer(ServerBase):
    """SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

    导入：from unitree_sdk2_cpp.robot import LeaseServer
    构造可用性：SIGNATURE_ONLY。
    """
    def __init__(self, name: str, term: int) -> None:
        """初始化 `LeaseServer` 实例。是否能实际构造取决于下方可用性状态。

        可用性：SIGNATURE_ONLY；分类：CONSTRUCTION。

        Args:
            name: SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。
            term: 传给该接口的 `term` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `term: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_construct(name: str, term: int) -> LeaseServer:
                    return LeaseServer(name=name, term=term)
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: LeaseServer(const std::string &, int64_t)
        """
        ...
    def init(self) -> None:
        """初始化当前 SDK 对象所需的底层通道或服务资源。

        可用性：SIGNATURE_ONLY；分类：UNCLASSIFIED。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_init(obj: LeaseServer) -> None:
                    obj.init()
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Init()
        """
        ...
    def check_request_lease_denied(self, lease_id: int) -> bool:
        """查询或检查 请求 lease `denied`。

        可用性：SIGNATURE_ONLY；分类：UNCLASSIFIED。

        Args:
            lease_id: 传给该接口的 lease ID 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `leaseId: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。

        Returns:
            返回值 (bool): 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_check_request_lease_denied(obj: LeaseServer, lease_id: int) -> bool:
                    return obj.check_request_lease_denied(lease_id=lease_id)
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: CheckRequestLeaseDenied(int64_t)
        """
        ...

class RequestFuture(object):
    """SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

    导入：from unitree_sdk2_cpp.robot import RequestFuture
    构造可用性：SIGNATURE_ONLY。
    """
    @overload
    def __init__(self) -> None:
        """初始化 `RequestFuture` 实例。是否能实际构造取决于下方可用性状态。

        可用性：SIGNATURE_ONLY；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_construct() -> RequestFuture:
                    return RequestFuture()
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: RequestFuture()
        """
        ...
    @overload
    def __init__(self, request_id: int) -> None:
        """初始化 `RequestFuture` 实例。是否能实际构造取决于下方可用性状态。

        可用性：SIGNATURE_ONLY；分类：CONSTRUCTION。

        Args:
            request_id: 传给该接口的 请求 ID 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `requestId: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_construct(request_id: int) -> RequestFuture:
                    return RequestFuture(request_id=request_id)
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: RequestFuture(int64_t)
        """
        ...
    def set_request_id(self, request_id: int) -> None:
        """设置 请求 ID。具体副作用和安全边界见下方状态。

        可用性：SIGNATURE_ONLY；分类：UNCLASSIFIED。

        Args:
            request_id: 传给该接口的 请求 ID 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `requestId: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_set_request_id(obj: RequestFuture, request_id: int) -> None:
                    obj.set_request_id(request_id=request_id)
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: SetRequestId(int64_t)
        """
        ...
    def get_request_id(self) -> int:
        """查询或检查 请求 ID。

        可用性：SIGNATURE_ONLY；分类：UNCLASSIFIED。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_get_request_id(obj: RequestFuture) -> int:
                    return obj.get_request_id()
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: GetRequestId() const
        """
        ...
    def set_queue(self, future_queue_ptr: RequestFutureQueue) -> bool:
        """设置 `queue`。具体副作用和安全边界见下方状态。

        可用性：SIGNATURE_ONLY；分类：UNCLASSIFIED。

        Args:
            future_queue_ptr: 传给该接口的 `future` `queue` `ptr` 参数，Python 类型为 `RequestFutureQueue`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `futureQueuePtr: const std::shared_ptr<RequestFutureQueue> &`。

        Returns:
            返回值 (bool): 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_set_queue(obj: RequestFuture, future_queue_ptr: RequestFutureQueue) -> bool:
                    return obj.set_queue(future_queue_ptr=future_queue_ptr)
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: SetQueue(const std::shared_ptr<RequestFutureQueue> &)
        """
        ...
    def get_response(self, microsec: int) -> Any:
        """查询或检查 响应。

        可用性：SIGNATURE_ONLY；分类：UNCLASSIFIED。

        Args:
            microsec: 等待时间，单位为微秒。具体超时结果以 SDK 方法约定为准。 对应 C++ 参数 `microsec: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。

        Returns:
            返回值 (Any): 返回 `Any`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_get_response(obj: RequestFuture, microsec: int) -> Any:
                    return obj.get_response(microsec=microsec)
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: GetResponse(int64_t)
        """
        ...
    def ready(self, request_ptr: Any) -> None:
        """对应 C++ SDK 操作 `Ready(const unitree::robot::ResponsePtr &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：SIGNATURE_ONLY；分类：UNCLASSIFIED。

        Args:
            request_ptr: 传给该接口的 请求 `ptr` 参数，Python 类型为 `Any`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `requestPtr: const unitree::robot::ResponsePtr &`。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_ready(obj: RequestFuture, request_ptr: Any) -> None:
                    obj.ready(request_ptr=request_ptr)
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Ready(const unitree::robot::ResponsePtr &)
        """
        ...

class RequestFutureQueue(object):
    """SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

    导入：from unitree_sdk2_cpp.robot import RequestFutureQueue
    构造可用性：SIGNATURE_ONLY。
    """
    def __init__(self) -> None:
        """初始化 `RequestFutureQueue` 实例。是否能实际构造取决于下方可用性状态。

        可用性：SIGNATURE_ONLY；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_construct() -> RequestFutureQueue:
                    return RequestFutureQueue()
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: RequestFutureQueue()
        """
        ...
    def get(self, request_id: int) -> RequestFuture:
        """对应 C++ SDK 操作 `Get(int64_t)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：SIGNATURE_ONLY；分类：UNCLASSIFIED。

        Args:
            request_id: 传给该接口的 请求 ID 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `requestId: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。

        Returns:
            返回值 (RequestFuture): 返回 `RequestFuture`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_get(obj: RequestFutureQueue, request_id: int) -> RequestFuture:
                    return obj.get(request_id=request_id)
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Get(int64_t)
        """
        ...
    def put(self, request_id: int, future_ptr: RequestFuture) -> bool:
        """对应 C++ SDK 操作 `Put(int64_t, const unitree::robot::RequestFuturePtr &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：SIGNATURE_ONLY；分类：UNCLASSIFIED。

        Args:
            request_id: 传给该接口的 请求 ID 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `requestId: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。
            future_ptr: 传给该接口的 `future` `ptr` 参数，Python 类型为 `RequestFuture`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `futurePtr: const unitree::robot::RequestFuturePtr &`。

        Returns:
            返回值 (bool): 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_put(obj: RequestFutureQueue, request_id: int, future_ptr: RequestFuture) -> bool:
                    return obj.put(request_id=request_id, future_ptr=future_ptr)
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Put(int64_t, const unitree::robot::RequestFuturePtr &)
        """
        ...
    def remove(self, request_id: int) -> None:
        """对应 C++ SDK 操作 `Remove(int64_t)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：SIGNATURE_ONLY；分类：UNCLASSIFIED。

        Args:
            request_id: 传给该接口的 请求 ID 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `requestId: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_remove(obj: RequestFutureQueue, request_id: int) -> None:
                    obj.remove(request_id=request_id)
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Remove(int64_t)
        """
        ...
    def size(self) -> int:
        """对应 C++ SDK 操作 `Size()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：SIGNATURE_ONLY；分类：UNCLASSIFIED。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (int): 返回 `int`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_size(obj: RequestFutureQueue) -> int:
                    return obj.size()
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Size()
        """
        ...

class Server(ServerBase):
    """SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

    导入：from unitree_sdk2_cpp.robot import Server
    构造可用性：SIGNATURE_ONLY。
    """
    def __init__(self, name: str) -> None:
        """初始化 `Server` 实例。是否能实际构造取决于下方可用性状态。

        可用性：SIGNATURE_ONLY；分类：CONSTRUCTION。

        Args:
            name: SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_construct(name: str) -> Server:
                    return Server(name=name)
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Server(const std::string &)
        """
        ...
    def init(self) -> None:
        """初始化当前 SDK 对象所需的底层通道或服务资源。

        可用性：SIGNATURE_ONLY；分类：UNCLASSIFIED。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_init(obj: Server) -> None:
                    obj.init()
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Init()
        """
        ...
    @overload
    def start_lease(self, lease_term: int) -> None:
        """启动对应 SDK 操作。具体副作用和安全边界见下方状态。

        可用性：SIGNATURE_ONLY；分类：UNCLASSIFIED。

        Args:
            lease_term: 传给该接口的 lease `term` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `leaseTerm: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_start_lease(obj: Server, lease_term: int) -> None:
                    obj.start_lease(lease_term=lease_term)
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: StartLease(int64_t)
        """
        ...
    @overload
    def start_lease(self, lease_term: float) -> None:
        """启动对应 SDK 操作。具体副作用和安全边界见下方状态。

        可用性：SIGNATURE_ONLY；分类：UNCLASSIFIED。

        Args:
            lease_term: 传给该接口的 lease `term` 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `leaseTerm: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_start_lease(obj: Server, lease_term: float) -> None:
                    obj.start_lease(lease_term=lease_term)
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: StartLease(float)
        """
        ...
    def get_name(self) -> str:
        """查询或检查 名称。

        可用性：SIGNATURE_ONLY；分类：UNCLASSIFIED。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (str): 返回 `str`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_get_name(obj: Server) -> str:
                    return obj.get_name()
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: GetName()
        """
        ...
    def get_api_version(self) -> str:
        """查询或检查 API `version`。

        可用性：SIGNATURE_ONLY；分类：UNCLASSIFIED。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (str): 返回 `str`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_get_api_version(obj: Server) -> str:
                    return obj.get_api_version()
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: GetApiVersion() const
        """
        ...
    def get_current_api_id(self) -> int:
        """查询或检查 `current` API ID。

        可用性：SIGNATURE_ONLY；分类：UNCLASSIFIED。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_get_current_api_id(obj: Server) -> int:
                    return obj.get_current_api_id()
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: GetCurrentApiId() const
        """
        ...

class ServerBase(object):
    """SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

    导入：from unitree_sdk2_cpp.robot import ServerBase
    构造可用性：SIGNATURE_ONLY。
    """
    def __init__(self, name: str) -> None:
        """初始化 `ServerBase` 实例。是否能实际构造取决于下方可用性状态。

        可用性：SIGNATURE_ONLY；分类：CONSTRUCTION。

        Args:
            name: SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_construct(name: str) -> ServerBase:
                    return ServerBase(name=name)
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: ServerBase(const std::string &)
        """
        ...
    def init(self) -> None:
        """初始化当前 SDK 对象所需的底层通道或服务资源。

        可用性：SIGNATURE_ONLY；分类：UNCLASSIFIED。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_init(obj: ServerBase) -> None:
                    obj.init()
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Init()
        """
        ...
    def start(self, enable_proi_queue: bool = ...) -> None:
        """启动对应 SDK 操作。具体副作用和安全边界见下方状态。

        可用性：SIGNATURE_ONLY；分类：UNCLASSIFIED。

        Args:
            enable_proi_queue: 是否启用 SDK 中名为 `proi` 的队列选项；该名称沿用上游接口，具体行为需查对应头文件。 对应 C++ 参数 `enableProiQueue: bool`。 只接受布尔语义。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_start(obj: ServerBase, enable_proi_queue: bool) -> None:
                    obj.start(enable_proi_queue=enable_proi_queue)
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Start(bool)
        """
        ...
    def get_name(self) -> str:
        """查询或检查 名称。

        可用性：SIGNATURE_ONLY；分类：UNCLASSIFIED。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (str): 返回 `str`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_get_name(obj: ServerBase) -> str:
                    return obj.get_name()
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: GetName() const
        """
        ...

class ServerChannelNamer(ChannelNamer):
    """SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

    导入：from unitree_sdk2_cpp.robot import ServerChannelNamer
    构造可用性：SIGNATURE_ONLY。
    """
    def __init__(self) -> None:
        """初始化 `ServerChannelNamer` 实例。是否能实际构造取决于下方可用性状态。

        可用性：SIGNATURE_ONLY；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_construct() -> ServerChannelNamer:
                    return ServerChannelNamer()
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: ServerChannelNamer()
        """
        ...

class ServerStub(object):
    """SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

    导入：from unitree_sdk2_cpp.robot import ServerStub
    构造可用性：SIGNATURE_ONLY。
    """
    def __init__(self) -> None:
        """初始化 `ServerStub` 实例。是否能实际构造取决于下方可用性状态。

        可用性：SIGNATURE_ONLY；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_construct() -> ServerStub:
                    return ServerStub()
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: ServerStub()
        """
        ...
    def init(self, name: str, handler: Callable[..., Any], enable_proi_queue: bool) -> None:
        """初始化当前 SDK 对象所需的底层通道或服务资源。

        可用性：SIGNATURE_ONLY；分类：UNCLASSIFIED。

        Args:
            name: SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。
            handler: 传给该接口的 `handler` 参数，Python 类型为 `Callable[..., Any]`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `handler: const unitree::robot::ServerRequestHandler &`。
            enable_proi_queue: 是否启用 SDK 中名为 `proi` 的队列选项；该名称沿用上游接口，具体行为需查对应头文件。 对应 C++ 参数 `enableProiQueue: bool`。 只接受布尔语义。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_init(obj: ServerStub, name: str, handler: Callable[..., Any], enable_proi_queue: bool) -> None:
                    obj.init(name=name, handler=handler, enable_proi_queue=enable_proi_queue)
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Init(const std::string &, const unitree::robot::ServerRequestHandler &, bool)
        """
        ...
    def send(self, response: Any, timeout: int = ...) -> bool:
        """对应 C++ SDK 操作 `Send(const unitree::robot::Response &, int64_t)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：SIGNATURE_ONLY；分类：UNCLASSIFIED。

        Args:
            response: 传给该接口的 响应 参数，Python 类型为 `Any`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `response: const unitree::robot::Response &`。
            timeout: 传给该接口的 超时 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `timeout: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。

        Returns:
            返回值 (bool): 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            from typing import TYPE_CHECKING

            if TYPE_CHECKING:
                def planned_send(obj: ServerStub, response: Any, timeout: int) -> bool:
                    return obj.send(response=response, timeout=timeout)
            ```

        Notes:
            仅供设计时预览，不能假设该成员存在于原生扩展。
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Send(const unitree::robot::Response &, int64_t)
        """
        ...

from . import a2 as a2
from . import as2 as as2
from . import b2 as b2
from . import g1 as g1
from . import go2 as go2
from . import h1 as h1
from . import h2 as h2
from . import r1 as r1
