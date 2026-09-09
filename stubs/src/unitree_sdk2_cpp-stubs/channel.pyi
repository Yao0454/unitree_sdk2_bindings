"""Typed CycloneDDS channel API."""
from collections.abc import Callable
from typing import Any, Generic, TypeVar

MessageT = TypeVar("MessageT")

def registered_message_types() -> list[str]:
    """返回当前二进制扩展已经注册的 typed DDS 消息类型名。

    可用性：AVAILABLE；分类：DDS_LIFECYCLE。

    Args:
        无显式参数；实例方法的 self 由 Python 自动传入。

    Returns:
        返回值 (list[str]): 当前扩展已注册的 C++ DDS 消息类型名列表。

    Examples:
        用法片段；obj/client 和参数变量需先按业务准备。

        ```python
        message_type_names = registered_message_types()
        ```

    Notes:
        stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
        C++: registered_message_types()
    """
    ...
def initialize(domain_id: int = 0, network_interface: str = "") -> None:
    """使用 Domain ID 和网络接口初始化全局 DDS ChannelFactory。

    可用性：AVAILABLE；分类：DDS_LIFECYCLE。

    Args:
        domain_id: DDS Domain ID。只有使用兼容 domain 的参与者才能按预期互相发现。
        network_interface: DDS 使用的网络接口名称，例如 Linux 上的 `eth0` 或 `enp3s0`；必须按目标机实际网卡填写。

    Returns:
        无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

    Examples:
        用法片段；obj/client 和参数变量需先按业务准备。

        ```python
        initialize(domain_id=0, network_interface="eth0")
        ```

    Notes:
        stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
        C++: ChannelFactory::Init(int32_t, const std::string &)
    """
    ...
def initialize_from_config(config_file: str = "") -> None:
    """使用 CycloneDDS 配置文件初始化全局 DDS ChannelFactory。

    可用性：AVAILABLE；分类：DDS_LIFECYCLE。

    Args:
        config_file: CycloneDDS 配置文件路径；空字符串表示使用底层默认配置。

    Returns:
        无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

    Examples:
        用法片段；obj/client 和参数变量需先按业务准备。

        ```python
        initialize_from_config(config_file="cyclonedds.xml")
        ```

    Notes:
        stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
        C++: ChannelFactory::Init(const std::string &)
    """
    ...
def release() -> None:
    """释放全局 DDS ChannelFactory 及其持有的底层资源。

    可用性：AVAILABLE；分类：DDS_LIFECYCLE。

    Args:
        无显式参数；实例方法的 self 由 Python 自动传入。

    Returns:
        无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

    Examples:
        用法片段；obj/client 和参数变量需先按业务准备。

        ```python
        release()
        ```

    Notes:
        stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
        C++: ChannelFactory::Release()
    """
    ...

class ChannelPublisher(Generic[MessageT]):
    """typed DDS 通道包装类。必须遵守初始化、启动、关闭和全局释放顺序。

    导入：from unitree_sdk2_cpp.channel import ChannelPublisher
    构造可用性：AVAILABLE。
    """
    def __init__(self, topic: str, message_type: type[MessageT]) -> None:
        """初始化 `ChannelPublisher` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：DDS_LIFECYCLE。

        Args:
            topic: DDS topic 名称。发布端和订阅端必须同时使用兼容的 topic、消息类型和 QoS。
            message_type: IDL 消息类本身，例如 `LowState`，不是 `LowState()` 实例。该类型必须存在于运行时注册表中。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = ChannelPublisher(topic=topic, message_type=message_type)
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: ChannelPublisher(const std::string &, type)
        """
        ...
    @property
    def topic(self) -> str:
        """Publisher 构造时保存的 DDS topic 名称，只读。

        Returns:
            str：字段当前值。

        Examples:
            value = obj.topic
        """
        ...
    @property
    def message_type_name(self) -> str:
        """Publisher 使用的已注册 C++ 消息类型名，只读。

        Returns:
            str：字段当前值。

        Examples:
            value = obj.message_type_name
        """
        ...
    def init_channel(self) -> None:
        """创建并启动 Publisher 的底层 DDS 写通道。

        可用性：AVAILABLE；分类：DDS_LIFECYCLE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            obj.init_channel()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: ChannelPublisher::init_channel()
        """
        ...
    def close_channel(self) -> None:
        """关闭 Publisher 的底层 DDS 写通道。

        可用性：AVAILABLE；分类：DDS_LIFECYCLE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            obj.close_channel()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: ChannelPublisher::close_channel()
        """
        ...
    def write(self, message: MessageT, wait_microsec: int = 0) -> bool:
        """把一个类型匹配的消息样本写入 Publisher 对应的 DDS topic。

        可用性：AVAILABLE；分类：DDS_LIFECYCLE。

        Args:
            message: 要写入 DDS 的消息实例；类型必须与 Publisher 构造时声明的消息类完全一致。
            wait_microsec: 写操作允许等待的时间，单位为微秒；`0` 使用当前绑定的默认非额外等待行为。

        Returns:
            返回值 (bool): 底层写操作是否被接受；不表示所有订阅者已处理，更不表示设备已经执行动作。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.write(message=message, wait_microsec=wait_microsec)
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: ChannelPublisher::write(message, int64_t)
        """
        ...

class ChannelSubscriber(Generic[MessageT]):
    """typed DDS 通道包装类。必须遵守初始化、启动、关闭和全局释放顺序。

    导入：from unitree_sdk2_cpp.channel import ChannelSubscriber
    构造可用性：AVAILABLE。
    """
    def __init__(
        self,
        topic: str,
        message_type: type[MessageT],
        callback: Callable[[MessageT], None],
        queue_length: int = 0,
    ) -> None:
        """初始化 `ChannelSubscriber` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：DDS_LIFECYCLE。

        Args:
            topic: DDS topic 名称。发布端和订阅端必须同时使用兼容的 topic、消息类型和 QoS。
            message_type: IDL 消息类本身，例如 `LowState`，不是 `LowState()` 实例。该类型必须存在于运行时注册表中。
            callback: 收到数据或状态变化时调用的 Python 回调。回调签名必须与类型提示一致，并应快速返回。
            queue_length: 订阅队列长度。`0` 使用底层默认行为；更大值会允许更多积压，但也可能增加延迟和内存占用。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = ChannelSubscriber(topic=topic, message_type=message_type, callback=callback, queue_length=queue_length)
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: ChannelSubscriber(const std::string &, type, callback, int64_t)
        """
        ...
    @property
    def topic(self) -> str:
        """Subscriber 构造时保存的 DDS topic 名称，只读。

        Returns:
            str：字段当前值。

        Examples:
            value = obj.topic
        """
        ...
    @property
    def message_type_name(self) -> str:
        """Subscriber 使用的已注册 C++ 消息类型名，只读。

        Returns:
            str：字段当前值。

        Examples:
            value = obj.message_type_name
        """
        ...
    @property
    def last_data_available_time(self) -> int:
        """底层记录的最近一次数据可用时间。其单位和时间基准以 SDK 实现为准。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.last_data_available_time
        """
        ...
    def init_channel(self) -> None:
        """创建并启动 Subscriber 的底层 DDS 读通道。

        可用性：AVAILABLE；分类：DDS_LIFECYCLE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            obj.init_channel()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: ChannelSubscriber::init_channel()
        """
        ...
    def close_channel(self) -> None:
        """关闭 Subscriber 的底层 DDS 读通道，并停止后续回调。

        可用性：AVAILABLE；分类：DDS_LIFECYCLE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            obj.close_channel()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: ChannelSubscriber::close_channel()
        """
        ...
