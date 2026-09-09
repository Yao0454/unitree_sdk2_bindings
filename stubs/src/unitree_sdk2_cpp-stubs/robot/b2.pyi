"""Full SDK signature preview; see api_manifest.json for availability."""
from __future__ import annotations

import enum
from collections.abc import Callable, Mapping, Sequence
from typing import Any, overload

from . import Client, ClientBase

class BackVideoClient(Client):
    """Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

    导入：from unitree_sdk2_cpp.robot.b2 import BackVideoClient
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `BackVideoClient` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = BackVideoClient()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: BackVideoClient()
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
    def get_image_sample(self) -> tuple[int, list[int]]:
        """查询或检查 图像 `sample`。

        可用性：AVAILABLE；分类：READ_ONLY。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            [0] `status` (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。
            [1] `output_1` (list[int]): 传给该接口的 `output` `1` 参数，Python 类型为 `list[int]`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `output_1: std::vector<uint8_t> &`。 底层是可变长度 vector；元素约束：取值范围为 0 到 255。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            status, output_1 = obj.get_image_sample()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: GetImageSample(std::vector<uint8_t> &)
        """
        ...

class ConfigClient(Client):
    """Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

    导入：from unitree_sdk2_cpp.robot.b2 import ConfigClient
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `ConfigClient` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = ConfigClient()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: ConfigClient()
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
    def set(self, name: str, content: str) -> int:
        """对应 C++ SDK 操作 `Set(const std::string &, const std::string &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：HARDWARE_SIDE_EFFECT。

        Args:
            name: SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。
            content: 配置、请求或序列化内容。具体格式由对应服务协议定义。 对应 C++ 参数 `content: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.set(name=name, content=content)
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: Set(const std::string &, const std::string &)
        """
        ...
    def get(self, name: str) -> tuple[int, str]:
        """对应 C++ SDK 操作 `Get(const std::string &, std::string &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：READ_ONLY。

        Args:
            name: SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。

        Returns:
            [0] `status` (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。
            [1] `content` (str): 配置、请求或序列化内容。具体格式由对应服务协议定义。 对应 C++ 参数 `content: std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            status, content = obj.get(name=name)
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: Get(const std::string &, std::string &)
        """
        ...
    def del_(self, name: str) -> int:
        """对应 C++ SDK 操作 `Del(const std::string &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：HARDWARE_SIDE_EFFECT。

        Args:
            name: SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.del_(name=name)
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: Del(const std::string &)
        """
        ...
    def meta_config_meta(self, name: str) -> tuple[int, ConfigMeta]:
        """对应 C++ SDK 操作 `Meta(const std::string &, unitree::robot::b2::ConfigMeta &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：HARDWARE_SIDE_EFFECT。

        Args:
            name: SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。

        Returns:
            [0] `status` (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。
            [1] `meta` (ConfigMeta): 传给该接口的 `meta` 参数，Python 类型为 `ConfigMeta`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `meta: unitree::robot::b2::ConfigMeta &`。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            status, meta = obj.meta_config_meta(name=name)
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: Meta(const std::string &, unitree::robot::b2::ConfigMeta &)
        """
        ...
    def meta_string(self, name: str) -> tuple[int, str]:
        """对应 C++ SDK 操作 `Meta(const std::string &, std::string &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：HARDWARE_SIDE_EFFECT。

        Args:
            name: SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。

        Returns:
            [0] `status` (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。
            [1] `meta` (str): 传给该接口的 `meta` 参数，Python 类型为 `str`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `meta: std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            status, meta = obj.meta_string(name=name)
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: Meta(const std::string &, std::string &)
        """
        ...
    def subscribe_change_status(self, name: str, callback: Callable[[str, str], None]) -> None:
        """对应 C++ SDK 操作 `SubscribeChangeStatus(const std::string &, const unitree::robot::b2::ConfigChangeStatusCallback &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：HARDWARE_SIDE_EFFECT。

        Args:
            name: SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。
            callback: 收到数据或状态变化时调用的 Python 回调。回调签名必须与类型提示一致，并应快速返回。 对应 C++ 参数 `callback: const unitree::robot::b2::ConfigChangeStatusCallback &`。

        Returns:
            无 (None): 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            obj.subscribe_change_status(name=name, callback=callback)
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: SubscribeChangeStatus(const std::string &, const unitree::robot::b2::ConfigChangeStatusCallback &)
        """
        ...

class ConfigDelParameter(object):
    """SDK 请求参数值类型；当前可能仅提供设计期签名。

    导入：from unitree_sdk2_cpp.robot.b2 import ConfigDelParameter
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `ConfigDelParameter` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = ConfigDelParameter()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: ConfigDelParameter()
        """
        ...
    name: str
    """ConfigDelParameter.name：公开字段，类型为 str。
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

class ConfigGetData(object):
    """SDK 数据值类型；公开字段和转换方法见下文。

    导入：from unitree_sdk2_cpp.robot.b2 import ConfigGetData
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `ConfigGetData` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = ConfigGetData()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: ConfigGetData()
        """
        ...
    content: str
    """ConfigGetData.content：公开字段，类型为 str。
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

class ConfigGetParameter(object):
    """SDK 请求参数值类型；当前可能仅提供设计期签名。

    导入：from unitree_sdk2_cpp.robot.b2 import ConfigGetParameter
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `ConfigGetParameter` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = ConfigGetParameter()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: ConfigGetParameter()
        """
        ...
    name: str
    """ConfigGetParameter.name：公开字段，类型为 str。
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

class ConfigMeta(object):
    """SDK 数据值类型；公开字段和转换方法见下文。

    导入：from unitree_sdk2_cpp.robot.b2 import ConfigMeta
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `ConfigMeta` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = ConfigMeta()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: ConfigMeta()
        """
        ...
    name: str
    """ConfigMeta.name：公开字段，类型为 str。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    last_modified: str
    """ConfigMeta.last_modified：公开字段，类型为 str。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    size: int
    """ConfigMeta.size：公开字段，类型为 int。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    epoch: int
    """ConfigMeta.epoch：公开字段，类型为 int。
    具体单位及允许值以对应 SDK 数据结构为准。
    """

class ConfigMetaData(object):
    """SDK 数据值类型；公开字段和转换方法见下文。

    导入：from unitree_sdk2_cpp.robot.b2 import ConfigMetaData
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `ConfigMetaData` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = ConfigMetaData()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: ConfigMetaData()
        """
        ...
    meta: JsonizeConfigMeta
    """ConfigMetaData.meta：公开字段，类型为 JsonizeConfigMeta。
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

class ConfigMetaParameter(object):
    """SDK 请求参数值类型；当前可能仅提供设计期签名。

    导入：from unitree_sdk2_cpp.robot.b2 import ConfigMetaParameter
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `ConfigMetaParameter` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = ConfigMetaParameter()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: ConfigMetaParameter()
        """
        ...
    name: str
    """ConfigMetaParameter.name：公开字段，类型为 str。
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

class ConfigSetParameter(object):
    """SDK 请求参数值类型；当前可能仅提供设计期签名。

    导入：from unitree_sdk2_cpp.robot.b2 import ConfigSetParameter
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `ConfigSetParameter` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = ConfigSetParameter()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: ConfigSetParameter()
        """
        ...
    name: str
    """ConfigSetParameter.name：公开字段，类型为 str。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    content: str
    """ConfigSetParameter.content：公开字段，类型为 str。
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

class FrontVideoClient(Client):
    """Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

    导入：from unitree_sdk2_cpp.robot.b2 import FrontVideoClient
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `FrontVideoClient` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = FrontVideoClient()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: FrontVideoClient()
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
    def get_image_sample(self) -> tuple[int, list[int]]:
        """查询或检查 图像 `sample`。

        可用性：AVAILABLE；分类：READ_ONLY。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            [0] `status` (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。
            [1] `output_1` (list[int]): 传给该接口的 `output` `1` 参数，Python 类型为 `list[int]`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `output_1: std::vector<uint8_t> &`。 底层是可变长度 vector；元素约束：取值范围为 0 到 255。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            status, output_1 = obj.get_image_sample()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: GetImageSample(std::vector<uint8_t> &)
        """
        ...

class JsonizeConfigMeta(object):
    """SDK 数据值类型；公开字段和转换方法见下文。

    导入：from unitree_sdk2_cpp.robot.b2 import JsonizeConfigMeta
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `JsonizeConfigMeta` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = JsonizeConfigMeta()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: JsonizeConfigMeta()
        """
        ...
    name: str
    """JsonizeConfigMeta.name：公开字段，类型为 str。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    last_modified: str
    """JsonizeConfigMeta.last_modified：公开字段，类型为 str。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    size: int
    """JsonizeConfigMeta.size：公开字段，类型为 int。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    epoch: int
    """JsonizeConfigMeta.epoch：公开字段，类型为 int。
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

class JsonizeModeName(object):
    """SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

    导入：from unitree_sdk2_cpp.robot.b2 import JsonizeModeName
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `JsonizeModeName` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = JsonizeModeName()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: JsonizeModeName()
        """
        ...
    name: str
    """JsonizeModeName.name：公开字段，类型为 str。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    form: str
    """JsonizeModeName.form：公开字段，类型为 str。
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

class JsonizeSilent(object):
    """SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

    导入：from unitree_sdk2_cpp.robot.b2 import JsonizeSilent
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `JsonizeSilent` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = JsonizeSilent()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: JsonizeSilent()
        """
        ...
    silent: bool
    """JsonizeSilent.silent：公开字段，类型为 bool。
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

class LowPowerStatusData(object):
    """SDK 数据值类型；公开字段和转换方法见下文。

    导入：from unitree_sdk2_cpp.robot.b2 import LowPowerStatusData
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `LowPowerStatusData` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = LowPowerStatusData()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: LowPowerStatusData()
        """
        ...
    status: int
    """LowPowerStatusData.status：公开字段，类型为 int。
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

class LowPowerSwitchParameter(object):
    """SDK 请求参数值类型；当前可能仅提供设计期签名。

    导入：from unitree_sdk2_cpp.robot.b2 import LowPowerSwitchParameter
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `LowPowerSwitchParameter` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = LowPowerSwitchParameter()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: LowPowerSwitchParameter()
        """
        ...
    swit: int
    """LowPowerSwitchParameter.swit：公开字段，类型为 int。
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

class MotionSwitcherClient(Client):
    """Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

    导入：from unitree_sdk2_cpp.robot.b2 import MotionSwitcherClient
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `MotionSwitcherClient` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = MotionSwitcherClient()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: MotionSwitcherClient()
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
    def check_mode(self) -> tuple[int, str, str]:
        """查询或检查 模式。

        可用性：AVAILABLE；分类：READ_ONLY。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            [0] `status` (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。
            [1] `form` (str): 传给该接口的 `form` 参数，Python 类型为 `str`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `form: std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。
            [2] `name` (str): SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            status, form, name = obj.check_mode()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: CheckMode(std::string &, std::string &)
        """
        ...
    def select_mode(self, name_or_alias: str) -> int:
        """对应 C++ SDK 操作 `SelectMode(const std::string &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            name_or_alias: 传给该接口的 名称 `or` `alias` 参数，Python 类型为 `str`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `nameOrAlias: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.select_mode(name_or_alias=name_or_alias)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: SelectMode(const std::string &)
        """
        ...
    def release_mode(self) -> int:
        """对应 C++ SDK 操作 `ReleaseMode()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.release_mode()
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: ReleaseMode()
        """
        ...
    def set_silent(self, silent: bool) -> int:
        """设置 静音状态。具体副作用和安全边界见下方状态。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            silent: 传给该接口的 静音状态 参数，Python 类型为 `bool`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `silent: bool`。 只接受布尔语义。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.set_silent(silent=silent)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: SetSilent(bool)
        """
        ...
    def get_silent(self) -> tuple[int, bool]:
        """查询或检查 静音状态。

        可用性：AVAILABLE；分类：READ_ONLY。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            [0] `status` (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。
            [1] `silent` (bool): 传给该接口的 静音状态 参数，Python 类型为 `bool`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `silent: bool &`。 只接受布尔语义。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            status, silent = obj.get_silent()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: GetSilent(bool &)
        """
        ...

class PkgVersionData(object):
    """SDK 数据值类型；公开字段和转换方法见下文。

    导入：from unitree_sdk2_cpp.robot.b2 import PkgVersionData
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `PkgVersionData` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = PkgVersionData()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: PkgVersionData()
        """
        ...
    package_version: str
    """PkgVersionData.package_version：公开字段，类型为 str。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    module_version_map: dict[str, str]
    """PkgVersionData.module_version_map：公开字段，类型为 dict[str, str]。
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

class RobotStateClient(Client):
    """Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

    导入：from unitree_sdk2_cpp.robot.b2 import RobotStateClient
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `RobotStateClient` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = RobotStateClient()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: RobotStateClient()
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
    def service_list(self) -> tuple[int, list[ServiceState]]:
        """对应 C++ SDK 操作 `ServiceList(std::vector<ServiceState> &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：READ_ONLY。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            [0] `status` (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。
            [1] `serviceStateList` (list[ServiceState]): 传给该接口的 `serviceStateList` 参数，Python 类型为 `list[ServiceState]`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `serviceStateList: std::vector<ServiceState> &`。 底层是可变长度 vector

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            status, serviceStateList = obj.service_list()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: ServiceList(std::vector<ServiceState> &)
        """
        ...
    def service_switch(self, name: str, swit: int) -> tuple[int, int]:
        """对应 C++ SDK 操作 `ServiceSwitch(const std::string &, int32_t, int32_t &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：HARDWARE_SIDE_EFFECT。

        Args:
            name: SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。
            swit: 传给该接口的 `swit` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `swit: int32_t`。 取值范围为 -2147483648 到 2147483647。

        Returns:
            [0] `status` (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。
            [1] `status` (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            status, status = obj.service_switch(name=name, swit=swit)
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: ServiceSwitch(const std::string &, int32_t, int32_t &)
        """
        ...
    def set_report_freq(self, interval: int, duration: int) -> int:
        """设置 `report` `freq`。具体副作用和安全边界见下方状态。

        可用性：AVAILABLE；分类：HARDWARE_SIDE_EFFECT。

        Args:
            interval: 传给该接口的 `interval` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `interval: int32_t`。 取值范围为 -2147483648 到 2147483647。
            duration: 操作持续时间参数。精确单位、范围和默认行为以目标型号接口定义为准。 对应 C++ 参数 `duration: int32_t`。 取值范围为 -2147483648 到 2147483647。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.set_report_freq(interval=interval, duration=duration)
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: SetReportFreq(int32_t, int32_t)
        """
        ...
    def low_power_switch(self, swit: int) -> int:
        """对应 C++ SDK 操作 `LowPowerSwitch(int32_t)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：HARDWARE_SIDE_EFFECT。

        Args:
            swit: 传给该接口的 `swit` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `swit: int32_t`。 取值范围为 -2147483648 到 2147483647。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.low_power_switch(swit=swit)
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: LowPowerSwitch(int32_t)
        """
        ...
    def low_power_status(self) -> tuple[int, int]:
        """对应 C++ SDK 操作 `LowPowerStatus(int32_t &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：HARDWARE_SIDE_EFFECT。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            [0] `status` (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。
            [1] `status` (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            status, status = obj.low_power_status()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: LowPowerStatus(int32_t &)
        """
        ...
    def get_pkg_version(self) -> tuple[int, str, dict[str, str]]:
        """查询或检查 `pkg` `version`。

        可用性：AVAILABLE；分类：READ_ONLY。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            [0] `status` (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。
            [1] `packageVersion` (str): 传给该接口的 `packageVersion` 参数，Python 类型为 `str`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `packageVersion: std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。
            [2] `moduleVersionMap` (dict[str, str]): 传给该接口的 `moduleVersionMap` 参数，Python 类型为 `dict[str, str]`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `moduleVersionMap: std::map<std::string, std::string> &`。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            status, packageVersion, moduleVersionMap = obj.get_pkg_version()
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: GetPkgVersion(std::string &, std::map<std::string, std::string> &)
        """
        ...

class ServiceState(object):
    """SDK 数据值类型；公开字段和转换方法见下文。

    导入：from unitree_sdk2_cpp.robot.b2 import ServiceState
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `ServiceState` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = ServiceState()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: ServiceState()
        """
        ...
    name: str
    """ServiceState.name：公开字段，类型为 str。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    status: int
    """ServiceState.status：公开字段，类型为 int。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    protect: int
    """ServiceState.protect：公开字段，类型为 int。
    具体单位及允许值以对应 SDK 数据结构为准。
    """

class ServiceStateData(object):
    """SDK 数据值类型；公开字段和转换方法见下文。

    导入：from unitree_sdk2_cpp.robot.b2 import ServiceStateData
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `ServiceStateData` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = ServiceStateData()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: ServiceStateData()
        """
        ...
    name: str
    """ServiceStateData.name：公开字段，类型为 str。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    status: int
    """ServiceStateData.status：公开字段，类型为 int。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    protect: int
    """ServiceStateData.protect：公开字段，类型为 int。
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

class ServiceSwitchData(object):
    """SDK 数据值类型；公开字段和转换方法见下文。

    导入：from unitree_sdk2_cpp.robot.b2 import ServiceSwitchData
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `ServiceSwitchData` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = ServiceSwitchData()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: ServiceSwitchData()
        """
        ...
    name: str
    """ServiceSwitchData.name：公开字段，类型为 str。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    status: int
    """ServiceSwitchData.status：公开字段，类型为 int。
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

class ServiceSwitchParameter(object):
    """SDK 请求参数值类型；当前可能仅提供设计期签名。

    导入：from unitree_sdk2_cpp.robot.b2 import ServiceSwitchParameter
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `ServiceSwitchParameter` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = ServiceSwitchParameter()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: ServiceSwitchParameter()
        """
        ...
    name: str
    """ServiceSwitchParameter.name：公开字段，类型为 str。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    swit: int
    """ServiceSwitchParameter.swit：公开字段，类型为 int。
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

class SetReportFreqParameter(object):
    """SDK 请求参数值类型；当前可能仅提供设计期签名。

    导入：from unitree_sdk2_cpp.robot.b2 import SetReportFreqParameter
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `SetReportFreqParameter` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = SetReportFreqParameter()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: SetReportFreqParameter()
        """
        ...
    interval: int
    """SetReportFreqParameter.interval：公开字段，类型为 int。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    duration: int
    """SetReportFreqParameter.duration：公开字段，类型为 int。
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

    导入：from unitree_sdk2_cpp.robot.b2 import SportClient
    构造可用性：AVAILABLE。
    """
    def __init__(self, enable_lease: bool = False) -> None:
        """初始化 `SportClient` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            enable_lease: 是否启用 SDK lease 机制；lease 的获得、续期和释放规则以服务协议为准。 对应 C++ 参数 `enableLease: bool`。 只接受布尔语义。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = SportClient(enable_lease=enable_lease)
            ```

        Notes:
            服务调用前须初始化 DDS、构造客户端、设置超时并调用 init()。
            C++: SportClient(bool)
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
    def switch_gait(self, d: int) -> int:
        """对应 C++ SDK 操作 `SwitchGait(int)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            d: 传给该接口的 `d` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `d: int`。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.switch_gait(d=d)
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
    def trajectory_follow(self, path: Sequence[PathPoint]) -> int:
        """对应 C++ SDK 操作 `TrajectoryFollow(std::vector<unitree::robot::b2::PathPoint> &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            path: 传给该接口的 `path` 参数，Python 类型为 `Sequence[PathPoint]`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `path: std::vector<unitree::robot::b2::PathPoint> &`。 底层是可变长度 vector

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.trajectory_follow(path=path)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: TrajectoryFollow(std::vector<unitree::robot::b2::PathPoint> &)
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
    def move_to_pos(self, x: float, y: float, yaw: float) -> int:
        """对应 C++ SDK 操作 `MoveToPos(float, float, float)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            x: X 方向位置或分量参数。参考系、单位和范围必须查当前方法及目标型号协议。 对应 C++ 参数 `x: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。
            y: Y 方向位置或分量参数。参考系、单位和范围必须查当前方法及目标型号协议。 对应 C++ 参数 `y: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。
            yaw: 偏航角或偏航目标参数。参考系、单位和范围必须查目标型号协议。 对应 C++ 参数 `yaw: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.move_to_pos(x=x, y=y, yaw=yaw)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: MoveToPos(float, float, float)
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
    def vision_walk(self, flag: bool) -> int:
        """对应 C++ SDK 操作 `VisionWalk(bool)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            flag: 布尔开关。`True` 和 `False` 的具体业务效果由当前方法定义。 对应 C++ 参数 `flag: bool`。 只接受布尔语义。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.vision_walk(flag=flag)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: VisionWalk(bool)
        """
        ...
    def hand_stand(self, flag: bool) -> int:
        """对应 C++ SDK 操作 `HandStand(bool)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            flag: 布尔开关。`True` 和 `False` 的具体业务效果由当前方法定义。 对应 C++ 参数 `flag: bool`。 只接受布尔语义。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.hand_stand(flag=flag)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: HandStand(bool)
        """
        ...
    def auto_recovery_set(self, flag: bool) -> int:
        """对应 C++ SDK 操作 `AutoRecoverySet(bool)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            flag: 布尔开关。`True` 和 `False` 的具体业务效果由当前方法定义。 对应 C++ 参数 `flag: bool`。 只接受布尔语义。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.auto_recovery_set(flag=flag)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: AutoRecoverySet(bool)
        """
        ...
    def free_walk(self) -> int:
        """对应 C++ SDK 操作 `FreeWalk()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.free_walk()
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: FreeWalk()
        """
        ...
    def classic_walk(self, flag: bool) -> int:
        """对应 C++ SDK 操作 `ClassicWalk(bool)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            flag: 布尔开关。`True` 和 `False` 的具体业务效果由当前方法定义。 对应 C++ 参数 `flag: bool`。 只接受布尔语义。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.classic_walk(flag=flag)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: ClassicWalk(bool)
        """
        ...
    def fast_walk(self, flag: bool) -> int:
        """对应 C++ SDK 操作 `FastWalk(bool)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            flag: 布尔开关。`True` 和 `False` 的具体业务效果由当前方法定义。 对应 C++ 参数 `flag: bool`。 只接受布尔语义。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.fast_walk(flag=flag)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: FastWalk(bool)
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
    def free_height(self, flag: bool) -> int:
        """对应 C++ SDK 操作 `FreeHeight(bool)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            flag: 布尔开关。`True` 和 `False` 的具体业务效果由当前方法定义。 对应 C++ 参数 `flag: bool`。 只接受布尔语义。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.free_height(flag=flag)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: FreeHeight(bool)
        """
        ...
    def gait_height(self, flag: bool) -> int:
        """对应 C++ SDK 操作 `GaitHeight(bool)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

        可用性：AVAILABLE；分类：MOTION_COMMAND。

        Args:
            flag: 布尔开关。`True` 和 `False` 的具体业务效果由当前方法定义。 对应 C++ 参数 `flag: bool`。 只接受布尔语义。

        Returns:
            返回值 (int): SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            result = obj.gait_height(flag=flag)
            ```

        Notes:
            会向实体机器人发送运动请求；仅在确认目标状态并准备停止手段后调用。
            C++: GaitHeight(bool)
        """
        ...

class stPathPoint(object):
    """SDK 数据值类型；公开字段和转换方法见下文。

    导入：from unitree_sdk2_cpp.robot.b2 import stPathPoint
    构造可用性：AVAILABLE。
    """
    time_from_start: float
    """stPathPoint.time_from_start：公开字段，类型为 float。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    x: float
    """stPathPoint.x：公开字段，类型为 float。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    y: float
    """stPathPoint.y：公开字段，类型为 float。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    yaw: float
    """stPathPoint.yaw：公开字段，类型为 float。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    vx: float
    """stPathPoint.vx：公开字段，类型为 float。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    vy: float
    """stPathPoint.vy：公开字段，类型为 float。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    vyaw: float
    """stPathPoint.vyaw：公开字段，类型为 float。
    具体单位及允许值以对应 SDK 数据结构为准。
    """
    def __init__(self) -> None:
        """初始化 `stPathPoint` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：CONSTRUCTION。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = stPathPoint()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: stPathPoint()
        """
        ...

PathPoint = stPathPoint
