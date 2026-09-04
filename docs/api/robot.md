# Unitree SDK2 Python API 参考分卷

[返回 API 总索引](../API_REFERENCE_ZH.md) · [阅读从零开始指南](../BEGINNER_GUIDE_ZH.md)

> [!WARNING]
> 本分卷同时包含 `AVAILABLE` 和 `SIGNATURE_ONLY`。后者只是设计期类型签名。运动及硬件副作用方法即使标记为 `AVAILABLE`，也不表示当前环境可安全执行。

> [!NOTE]
> 本文件由 `generator/generate_api_docs.py` 自动生成，请勿手工维护 API 条目。

---

<a id="unitree-sdk2-cpp-robot"></a>
## Robot 公共基础 API

模块：`unitree_sdk2_cpp.robot`

### 类索引

| 类 | 公开函数签名 | 属性 |
| --- | ---: | ---: |
| [`ApplyLeaseData`](#unitree-sdk2-cpp-robot-applyleasedata) | 3 | 0 |
| [`ApplyLeaseParameter`](#unitree-sdk2-cpp-robot-applyleaseparameter) | 3 | 0 |
| [`ChannelFactory`](#unitree-sdk2-cpp-robot-channelfactory) | 5 | 0 |
| [`ChannelNamer`](#unitree-sdk2-cpp-robot-channelnamer) | 2 | 0 |
| [`Client`](#unitree-sdk2-cpp-robot-client) | 5 | 0 |
| [`ClientBase`](#unitree-sdk2-cpp-robot-clientbase) | 4 | 0 |
| [`ClientChannelNamer`](#unitree-sdk2-cpp-robot-clientchannelnamer) | 1 | 0 |
| [`ClientStub`](#unitree-sdk2-cpp-robot-clientstub) | 4 | 0 |
| [`LeaseCache`](#unitree-sdk2-cpp-robot-leasecache) | 7 | 0 |
| [`LeaseClient`](#unitree-sdk2-cpp-robot-leaseclient) | 5 | 0 |
| [`LeaseContext`](#unitree-sdk2-cpp-robot-leasecontext) | 6 | 0 |
| [`LeaseServer`](#unitree-sdk2-cpp-robot-leaseserver) | 3 | 0 |
| [`RequestFuture`](#unitree-sdk2-cpp-robot-requestfuture) | 7 | 0 |
| [`RequestFutureQueue`](#unitree-sdk2-cpp-robot-requestfuturequeue) | 5 | 0 |
| [`Server`](#unitree-sdk2-cpp-robot-server) | 7 | 0 |
| [`ServerBase`](#unitree-sdk2-cpp-robot-serverbase) | 4 | 0 |
| [`ServerChannelNamer`](#unitree-sdk2-cpp-robot-serverchannelnamer) | 1 | 0 |
| [`ServerStub`](#unitree-sdk2-cpp-robot-serverstub) | 3 | 0 |

<a id="unitree-sdk2-cpp-robot-applyleasedata"></a>
### `unitree_sdk2_cpp.robot.ApplyLeaseData`

SDK 数据值类型；公开字段和转换方法见下文。

**导入**

```python
from unitree_sdk2_cpp.robot import ApplyLeaseData
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `id` | `int` | 传给该接口的 ID 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.id` / `obj.id = value` |
| `term` | `int` | 传给该接口的 `term` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.term` / `obj.term = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-applyleasedata-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-applyleasedata-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-applyleasedata-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-applyleasedata-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.ApplyLeaseData.__init__`

初始化 `ApplyLeaseData` 实例。是否能实际构造取决于下方可用性状态。

**签名**

```python
def __init__(self) -> None
```

**可用性与安全性**

**`AVAILABLE` / `CONSTRUCTION`**：当前绑定源码已实现；实际执行条件仍取决于平台和对应 SDK 环境。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。 |

**对应 C++**

- 类：`unitree::robot::ApplyLeaseData`
- 签名：`ApplyLeaseData()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/internal/internal_api.hpp:96`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = ApplyLeaseData()
```

<a id="unitree-sdk2-cpp-robot-applyleasedata-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.ApplyLeaseData.from_json`

计划从 JSON 风格字典读取字段并更新当前 SDK 值对象。

**签名**

```python
def from_json(self, value: Mapping[str, Any]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `UNCLASSIFIED`**：当前绑定源码已实现；实际执行条件仍取决于平台和对应 SDK 环境。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `value` | `Mapping[str, Any]` | 必填 | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 对应 C++ 参数 `json: common::JsonMap &`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree::robot::ApplyLeaseData`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/internal/internal_api.hpp:102`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-applyleasedata-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.ApplyLeaseData.to_json`

计划把当前 SDK 值对象写入 JSON 风格字典。

**签名**

```python
def to_json(self) -> dict[str, Any]
```

**可用性与安全性**

**`AVAILABLE` / `UNCLASSIFIED`**：当前绑定源码已实现；实际执行条件仍取决于平台和对应 SDK 环境。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `dict[str, Any]` | 返回 `dict[str, Any]`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree::robot::ApplyLeaseData`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/internal/internal_api.hpp:108`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-applyleaseparameter"></a>
### `unitree_sdk2_cpp.robot.ApplyLeaseParameter`

SDK 请求参数值类型；当前可能仅提供设计期签名。

**导入**

```python
from unitree_sdk2_cpp.robot import ApplyLeaseParameter
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `name` | `str` | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 | `value = obj.name` / `obj.name = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-applyleaseparameter-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-applyleaseparameter-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-applyleaseparameter-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-applyleaseparameter-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.ApplyLeaseParameter.__init__`

初始化 `ApplyLeaseParameter` 实例。是否能实际构造取决于下方可用性状态。

**签名**

```python
def __init__(self) -> None
```

**可用性与安全性**

**`AVAILABLE` / `CONSTRUCTION`**：当前绑定源码已实现；实际执行条件仍取决于平台和对应 SDK 环境。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。 |

**对应 C++**

- 类：`unitree::robot::ApplyLeaseParameter`
- 签名：`ApplyLeaseParameter()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/internal/internal_api.hpp:69`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = ApplyLeaseParameter()
```

<a id="unitree-sdk2-cpp-robot-applyleaseparameter-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.ApplyLeaseParameter.from_json`

计划从 JSON 风格字典读取字段并更新当前 SDK 值对象。

**签名**

```python
def from_json(self, value: Mapping[str, Any]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `UNCLASSIFIED`**：当前绑定源码已实现；实际执行条件仍取决于平台和对应 SDK 环境。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `value` | `Mapping[str, Any]` | 必填 | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 对应 C++ 参数 `json: common::JsonMap &`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree::robot::ApplyLeaseParameter`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/internal/internal_api.hpp:75`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-applyleaseparameter-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.ApplyLeaseParameter.to_json`

计划把当前 SDK 值对象写入 JSON 风格字典。

**签名**

```python
def to_json(self) -> dict[str, Any]
```

**可用性与安全性**

**`AVAILABLE` / `UNCLASSIFIED`**：当前绑定源码已实现；实际执行条件仍取决于平台和对应 SDK 环境。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `dict[str, Any]` | 返回 `dict[str, Any]`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree::robot::ApplyLeaseParameter`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/internal/internal_api.hpp:80`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-channelfactory"></a>
### `unitree_sdk2_cpp.robot.ChannelFactory`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot import ChannelFactory
```

**基类**：`object`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`instance`](#unitree-sdk2-cpp-robot-channelfactory-instance-1) | `def instance(self) -> ChannelFactory` | `SIGNATURE_ONLY` | `UNCLASSIFIED` |
| [`init（重载 1/3）`](#unitree-sdk2-cpp-robot-channelfactory-init-1) | `def init(self, domain_id: int, network_interface: str = ...) -> None` | `SIGNATURE_ONLY` | `UNCLASSIFIED` |
| [`init（重载 2/3）`](#unitree-sdk2-cpp-robot-channelfactory-init-2) | `def init(self, config_file_name: str = ...) -> None` | `SIGNATURE_ONLY` | `UNCLASSIFIED` |
| [`init（重载 3/3）`](#unitree-sdk2-cpp-robot-channelfactory-init-3) | `def init(self, json_map: dict[str, Any]) -> None` | `SIGNATURE_ONLY` | `UNCLASSIFIED` |
| [`release`](#unitree-sdk2-cpp-robot-channelfactory-release-1) | `def release(self) -> None` | `SIGNATURE_ONLY` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-channelfactory-instance-1"></a>
#### `unitree_sdk2_cpp.robot.ChannelFactory.instance`

对应 C++ SDK 操作 `Instance()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def instance(self) -> ChannelFactory
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `UNCLASSIFIED`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `ChannelFactory` | 返回 `ChannelFactory`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree::robot::ChannelFactory`
- 签名：`Instance()`
- 绑定策略：`SIGNATURE_PREVIEW`
- 声明位置：`include/unitree/robot/channel/channel_factory.hpp:19`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_instance(obj: ChannelFactory) -> ChannelFactory:
        return obj.instance()
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-channelfactory-init-1"></a>
#### `unitree_sdk2_cpp.robot.ChannelFactory.init`（重载 1/3）

初始化当前 SDK 对象所需的底层通道或服务资源。

**签名**

```python
@overload
def init(self, domain_id: int, network_interface: str = ...) -> None
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `UNCLASSIFIED`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `domain_id` | `int` | 必填 | DDS Domain ID。只有使用兼容 domain 的参与者才能按预期互相发现。 对应 C++ 参数 `domainId: int32_t`。 取值范围为 -2147483648 到 2147483647。 |
| `network_interface` | `str` | `...` | DDS 使用的网络接口名称，例如 Linux 上的 `eth0` 或 `enp3s0`；必须按目标机实际网卡填写。 对应 C++ 参数 `networkInterface: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree::robot::ChannelFactory`
- 签名：`Init(int32_t, const std::string &)`
- 绑定策略：`SIGNATURE_PREVIEW`
- 声明位置：`include/unitree/robot/channel/channel_factory.hpp:25`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 默认值显示为 `...`，表示 C++ 声明存在默认参数，但当前 AST 清单没有保存其字面量；省略参数可使用上游默认行为。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_init(obj: ChannelFactory, domain_id: int, network_interface: str) -> None:
        obj.init(domain_id=domain_id, network_interface=network_interface)
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-channelfactory-init-2"></a>
#### `unitree_sdk2_cpp.robot.ChannelFactory.init`（重载 2/3）

初始化当前 SDK 对象所需的底层通道或服务资源。

**签名**

```python
@overload
def init(self, config_file_name: str = ...) -> None
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `UNCLASSIFIED`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `config_file_name` | `str` | `...` | 传给该接口的 配置 `file` 名称 参数，Python 类型为 `str`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `configFileName: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree::robot::ChannelFactory`
- 签名：`Init(const std::string &)`
- 绑定策略：`SIGNATURE_PREVIEW`
- 声明位置：`include/unitree/robot/channel/channel_factory.hpp:26`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 默认值显示为 `...`，表示 C++ 声明存在默认参数，但当前 AST 清单没有保存其字面量；省略参数可使用上游默认行为。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_init(obj: ChannelFactory, config_file_name: str) -> None:
        obj.init(config_file_name=config_file_name)
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-channelfactory-init-3"></a>
#### `unitree_sdk2_cpp.robot.ChannelFactory.init`（重载 3/3）

初始化当前 SDK 对象所需的底层通道或服务资源。

**签名**

```python
@overload
def init(self, json_map: dict[str, Any]) -> None
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `UNCLASSIFIED`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `json_map` | `dict[str, Any]` | 必填 | 传给该接口的 `json` `map` 参数，Python 类型为 `dict[str, Any]`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `jsonMap: const common::JsonMap &`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree::robot::ChannelFactory`
- 签名：`Init(const common::JsonMap &)`
- 绑定策略：`SIGNATURE_PREVIEW`
- 声明位置：`include/unitree/robot/channel/channel_factory.hpp:27`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_init(obj: ChannelFactory, json_map: dict[str, Any]) -> None:
        obj.init(json_map=json_map)
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-channelfactory-release-1"></a>
#### `unitree_sdk2_cpp.robot.ChannelFactory.release`

对应 C++ SDK 操作 `Release()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def release(self) -> None
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `UNCLASSIFIED`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree::robot::ChannelFactory`
- 签名：`Release()`
- 绑定策略：`SIGNATURE_PREVIEW`
- 声明位置：`include/unitree/robot/channel/channel_factory.hpp:29`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_release(obj: ChannelFactory) -> None:
        obj.release()
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-channelnamer"></a>
### `unitree_sdk2_cpp.robot.ChannelNamer`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot import ChannelNamer
```

**基类**：`object`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`get_send_channel_name`](#unitree-sdk2-cpp-robot-channelnamer-get-send-channel-name-1) | `def get_send_channel_name(self, name: str) -> str` | `SIGNATURE_ONLY` | `UNCLASSIFIED` |
| [`get_recv_channel_name`](#unitree-sdk2-cpp-robot-channelnamer-get-recv-channel-name-1) | `def get_recv_channel_name(self, name: str) -> str` | `SIGNATURE_ONLY` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-channelnamer-get-send-channel-name-1"></a>
#### `unitree_sdk2_cpp.robot.ChannelNamer.get_send_channel_name`

查询或检查 `send` `channel` 名称。

**签名**

```python
def get_send_channel_name(self, name: str) -> str
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `UNCLASSIFIED`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `name` | `str` | 必填 | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `str` | 返回 `str`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree::robot::ChannelNamer`
- 签名：`GetSendChannelName(const std::string &)`
- 绑定策略：`SIGNATURE_PREVIEW`
- 声明位置：`include/unitree/robot/channel/channel_namer.hpp:21`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_get_send_channel_name(obj: ChannelNamer, name: str) -> str:
        return obj.get_send_channel_name(name=name)
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-channelnamer-get-recv-channel-name-1"></a>
#### `unitree_sdk2_cpp.robot.ChannelNamer.get_recv_channel_name`

查询或检查 `recv` `channel` 名称。

**签名**

```python
def get_recv_channel_name(self, name: str) -> str
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `UNCLASSIFIED`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `name` | `str` | 必填 | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `str` | 返回 `str`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree::robot::ChannelNamer`
- 签名：`GetRecvChannelName(const std::string &)`
- 绑定策略：`SIGNATURE_PREVIEW`
- 声明位置：`include/unitree/robot/channel/channel_namer.hpp:22`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_get_recv_channel_name(obj: ChannelNamer, name: str) -> str:
        return obj.get_recv_channel_name(name=name)
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-client"></a>
### `unitree_sdk2_cpp.robot.Client`

Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

**导入**

```python
from unitree_sdk2_cpp.robot import Client
```

**基类**：`ClientBase`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-client-dunder-init-1) | `def __init__(self, name: str, enable_lease: bool = False) -> None` | `SIGNATURE_ONLY` | `CONSTRUCTION` |
| [`wait_lease_applied`](#unitree-sdk2-cpp-robot-client-wait-lease-applied-1) | `def wait_lease_applied(self) -> None` | `AVAILABLE` | `INITIALIZATION` |
| [`get_lease_id`](#unitree-sdk2-cpp-robot-client-get-lease-id-1) | `def get_lease_id(self) -> int` | `SIGNATURE_ONLY` | `READ_ONLY` |
| [`get_api_version`](#unitree-sdk2-cpp-robot-client-get-api-version-1) | `def get_api_version(self) -> str` | `AVAILABLE` | `READ_ONLY` |
| [`get_server_api_version`](#unitree-sdk2-cpp-robot-client-get-server-api-version-1) | `def get_server_api_version(self) -> str` | `AVAILABLE` | `READ_ONLY` |

<a id="unitree-sdk2-cpp-robot-client-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.Client.__init__`

初始化 `Client` 实例。是否能实际构造取决于下方可用性状态。

**签名**

```python
def __init__(self, name: str, enable_lease: bool = False) -> None
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `CONSTRUCTION`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `name` | `str` | 必填 | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。 |
| `enable_lease` | `bool` | `False` | 是否启用 SDK lease 机制；lease 的获得、续期和释放规则以服务协议为准。 对应 C++ 参数 `enableLease: bool`。 只接受布尔语义。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。 |

**对应 C++**

- 类：`unitree::robot::Client`
- 签名：`Client(const std::string &, bool)`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/client/client.hpp:24`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_construct(name: str, enable_lease: bool) -> Client:
        return Client(name=name, enable_lease=enable_lease)
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-client-wait-lease-applied-1"></a>
#### `unitree_sdk2_cpp.robot.Client.wait_lease_applied`

对应 C++ SDK 操作 `WaitLeaseApplied()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def wait_lease_applied(self) -> None
```

**可用性与安全性**

**`AVAILABLE` / `INITIALIZATION`**：当前绑定源码已实现；实际执行条件仍取决于平台和对应 SDK 环境。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree::robot::Client`
- 签名：`WaitLeaseApplied()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/client/client.hpp:27`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.wait_lease_applied()
```

<a id="unitree-sdk2-cpp-robot-client-get-lease-id-1"></a>
#### `unitree_sdk2_cpp.robot.Client.get_lease_id`

查询或检查 lease ID。

**签名**

```python
def get_lease_id(self) -> int
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `READ_ONLY`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | 返回 `int`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree::robot::Client`
- 签名：`GetLeaseId()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/client/client.hpp:28`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_get_lease_id(obj: Client) -> int:
        return obj.get_lease_id()
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-client-get-api-version-1"></a>
#### `unitree_sdk2_cpp.robot.Client.get_api_version`

查询或检查 API `version`。

**签名**

```python
def get_api_version(self) -> str
```

**可用性与安全性**

**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现只读查询。Robot Client 的服务端查询通常仍需匹配的 Linux 扩展、DDS、网络、机器人和服务；纯本地 getter 则不一定需要全部条件。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `str` | 返回 `str`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree::robot::Client`
- 签名：`GetApiVersion() const`
- 绑定策略：`REFERENCE_POLICY`
- 声明位置：`include/unitree/robot/client/client.hpp:30`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.get_api_version()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-client-get-server-api-version-1"></a>
#### `unitree_sdk2_cpp.robot.Client.get_server_api_version`

查询或检查 `server` API `version`。

**签名**

```python
def get_server_api_version(self) -> str
```

**可用性与安全性**

**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现只读查询。Robot Client 的服务端查询通常仍需匹配的 Linux 扩展、DDS、网络、机器人和服务；纯本地 getter 则不一定需要全部条件。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `str` | 返回 `str`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree::robot::Client`
- 签名：`GetServerApiVersion()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/client/client.hpp:31`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.get_server_api_version()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-clientbase"></a>
### `unitree_sdk2_cpp.robot.ClientBase`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot import ClientBase
```

**基类**：`object`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-clientbase-dunder-init-1) | `def __init__(self, name: str) -> None` | `SIGNATURE_ONLY` | `CONSTRUCTION` |
| [`init`](#unitree-sdk2-cpp-robot-clientbase-init-1) | `def init(self) -> None` | `SIGNATURE_ONLY` | `INITIALIZATION` |
| [`set_timeout_microseconds`](#unitree-sdk2-cpp-robot-clientbase-set-timeout-microseconds-1) | `def set_timeout_microseconds(self, microseconds: int) -> None` | `AVAILABLE` | `INITIALIZATION` |
| [`set_timeout`](#unitree-sdk2-cpp-robot-clientbase-set-timeout-1) | `def set_timeout(self, seconds: float) -> None` | `AVAILABLE` | `INITIALIZATION` |

<a id="unitree-sdk2-cpp-robot-clientbase-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.ClientBase.__init__`

初始化 `ClientBase` 实例。是否能实际构造取决于下方可用性状态。

**签名**

```python
def __init__(self, name: str) -> None
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `CONSTRUCTION`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `name` | `str` | 必填 | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。 |

**对应 C++**

- 类：`unitree::robot::ClientBase`
- 签名：`ClientBase(const std::string &)`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/client/client_base.hpp:23`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_construct(name: str) -> ClientBase:
        return ClientBase(name=name)
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-clientbase-init-1"></a>
#### `unitree_sdk2_cpp.robot.ClientBase.init`

初始化当前 SDK 对象所需的底层通道或服务资源。

**签名**

```python
def init(self) -> None
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `INITIALIZATION`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree::robot::ClientBase`
- 签名：`Init()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/client/client_base.hpp:26`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_init(obj: ClientBase) -> None:
        obj.init()
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-clientbase-set-timeout-microseconds-1"></a>
#### `unitree_sdk2_cpp.robot.ClientBase.set_timeout_microseconds`

设置 超时 `microseconds`。具体副作用和安全边界见下方状态。

**签名**

```python
def set_timeout_microseconds(self, microseconds: int) -> None
```

**可用性与安全性**

**`AVAILABLE` / `INITIALIZATION`**：当前绑定源码已实现；实际执行条件仍取决于平台和对应 SDK 环境。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `microseconds` | `int` | 必填 | 客户端请求超时，单位为微秒。 对应 C++ 参数 `timeout: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree::robot::ClientBase`
- 签名：`SetTimeout(int64_t)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/client/client_base.hpp:28`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.set_timeout_microseconds(microseconds=microseconds)
```

<a id="unitree-sdk2-cpp-robot-clientbase-set-timeout-1"></a>
#### `unitree_sdk2_cpp.robot.ClientBase.set_timeout`

设置 超时。具体副作用和安全边界见下方状态。

**签名**

```python
def set_timeout(self, seconds: float) -> None
```

**可用性与安全性**

**`AVAILABLE` / `INITIALIZATION`**：当前绑定源码已实现；实际执行条件仍取决于平台和对应 SDK 环境。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `seconds` | `float` | 必填 | 客户端请求超时，单位为秒。 对应 C++ 参数 `timeout: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree::robot::ClientBase`
- 签名：`SetTimeout(float)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/client/client_base.hpp:29`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.set_timeout(seconds=seconds)
```

<a id="unitree-sdk2-cpp-robot-clientchannelnamer"></a>
### `unitree_sdk2_cpp.robot.ClientChannelNamer`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot import ClientChannelNamer
```

**基类**：`ChannelNamer`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-clientchannelnamer-dunder-init-1) | `def __init__(self) -> None` | `SIGNATURE_ONLY` | `CONSTRUCTION` |

<a id="unitree-sdk2-cpp-robot-clientchannelnamer-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.ClientChannelNamer.__init__`

初始化 `ClientChannelNamer` 实例。是否能实际构造取决于下方可用性状态。

**签名**

```python
def __init__(self) -> None
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `CONSTRUCTION`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。 |

**对应 C++**

- 类：`unitree::robot::ClientChannelNamer`
- 签名：`ClientChannelNamer()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/channel/channel_namer.hpp:34`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_construct() -> ClientChannelNamer:
        return ClientChannelNamer()
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-clientstub"></a>
### `unitree_sdk2_cpp.robot.ClientStub`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot import ClientStub
```

**基类**：`object`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-clientstub-dunder-init-1) | `def __init__(self) -> None` | `SIGNATURE_ONLY` | `CONSTRUCTION` |
| [`init`](#unitree-sdk2-cpp-robot-clientstub-init-1) | `def init(self, name: str) -> None` | `SIGNATURE_ONLY` | `INITIALIZATION` |
| [`send`](#unitree-sdk2-cpp-robot-clientstub-send-1) | `def send(self, req: Any, wait_timeout: int) -> bool` | `SIGNATURE_ONLY` | `HARDWARE_SIDE_EFFECT` |
| [`send_request`](#unitree-sdk2-cpp-robot-clientstub-send-request-1) | `def send_request(self, req: Any, wait_timeout: int) -> RequestFuture` | `SIGNATURE_ONLY` | `HARDWARE_SIDE_EFFECT` |

<a id="unitree-sdk2-cpp-robot-clientstub-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.ClientStub.__init__`

初始化 `ClientStub` 实例。是否能实际构造取决于下方可用性状态。

**签名**

```python
def __init__(self) -> None
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `CONSTRUCTION`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。 |

**对应 C++**

- 类：`unitree::robot::ClientStub`
- 签名：`ClientStub()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/client/client_stub.hpp:15`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_construct() -> ClientStub:
        return ClientStub()
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-clientstub-init-1"></a>
#### `unitree_sdk2_cpp.robot.ClientStub.init`

初始化当前 SDK 对象所需的底层通道或服务资源。

**签名**

```python
def init(self, name: str) -> None
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `INITIALIZATION`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `name` | `str` | 必填 | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree::robot::ClientStub`
- 签名：`Init(const std::string &)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/client/client_stub.hpp:18`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_init(obj: ClientStub, name: str) -> None:
        obj.init(name=name)
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-clientstub-send-1"></a>
#### `unitree_sdk2_cpp.robot.ClientStub.send`

对应 C++ SDK 操作 `Send(const unitree::robot::Request &, int64_t)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def send(self, req: Any, wait_timeout: int) -> bool
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `HARDWARE_SIDE_EFFECT`**：仅用于补全和静态检查。当前二进制没有该 Python 方法，未来实现还需单独评审硬件副作用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `req` | `Any` | 必填 | 传给该接口的 `req` 参数，Python 类型为 `Any`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `req: const unitree::robot::Request &`。 |
| `wait_timeout` | `int` | 必填 | 请求等待超时参数；精确单位沿用对应 C++ 接口定义。 对应 C++ 参数 `waitTimeout: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree::robot::ClientStub`
- 签名：`Send(const unitree::robot::Request &, int64_t)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/client/client_stub.hpp:20`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_send(obj: ClientStub, req: Any, wait_timeout: int) -> bool:
        return obj.send(req=req, wait_timeout=wait_timeout)
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-clientstub-send-request-1"></a>
#### `unitree_sdk2_cpp.robot.ClientStub.send_request`

对应 C++ SDK 操作 `SendRequest(const unitree::robot::Request &, int64_t)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def send_request(self, req: Any, wait_timeout: int) -> RequestFuture
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `HARDWARE_SIDE_EFFECT`**：仅用于补全和静态检查。当前二进制没有该 Python 方法，未来实现还需单独评审硬件副作用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `req` | `Any` | 必填 | 传给该接口的 `req` 参数，Python 类型为 `Any`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `req: const unitree::robot::Request &`。 |
| `wait_timeout` | `int` | 必填 | 请求等待超时参数；精确单位沿用对应 C++ 接口定义。 对应 C++ 参数 `waitTimeout: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `RequestFuture` | 返回 `RequestFuture`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree::robot::ClientStub`
- 签名：`SendRequest(const unitree::robot::Request &, int64_t)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/client/client_stub.hpp:21`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_send_request(obj: ClientStub, req: Any, wait_timeout: int) -> RequestFuture:
        return obj.send_request(req=req, wait_timeout=wait_timeout)
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-leasecache"></a>
### `unitree_sdk2_cpp.robot.LeaseCache`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot import LeaseCache
```

**基类**：`object`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-leasecache-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`set`](#unitree-sdk2-cpp-robot-leasecache-set-1) | `def set(self, id: int, m_name: str, last_modified: int = 0) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`renewal`](#unitree-sdk2-cpp-robot-leasecache-renewal-1) | `def renewal(self, last_modified: int = 0) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`clear`](#unitree-sdk2-cpp-robot-leasecache-clear-1) | `def clear(self) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`get_last_modified`](#unitree-sdk2-cpp-robot-leasecache-get-last-modified-1) | `def get_last_modified(self) -> int` | `AVAILABLE` | `UNCLASSIFIED` |
| [`get_id`](#unitree-sdk2-cpp-robot-leasecache-get-id-1) | `def get_id(self) -> int` | `AVAILABLE` | `UNCLASSIFIED` |
| [`get_name`](#unitree-sdk2-cpp-robot-leasecache-get-name-1) | `def get_name(self) -> str` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-leasecache-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.LeaseCache.__init__`

初始化 `LeaseCache` 实例。是否能实际构造取决于下方可用性状态。

**签名**

```python
def __init__(self) -> None
```

**可用性与安全性**

**`AVAILABLE` / `CONSTRUCTION`**：当前绑定源码已实现；实际执行条件仍取决于平台和对应 SDK 环境。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。 |

**对应 C++**

- 类：`unitree::robot::LeaseCache`
- 签名：`LeaseCache()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/server/lease_server.hpp:13`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = LeaseCache()
```

<a id="unitree-sdk2-cpp-robot-leasecache-set-1"></a>
#### `unitree_sdk2_cpp.robot.LeaseCache.set`

对应 C++ SDK 操作 `Set(int64_t, const std::string &, int64_t)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def set(self, id: int, m_name: str, last_modified: int = 0) -> None
```

**可用性与安全性**

**`AVAILABLE` / `UNCLASSIFIED`**：当前绑定源码已实现；实际执行条件仍取决于平台和对应 SDK 环境。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `id` | `int` | 必填 | 传给该接口的 ID 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `id: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。 |
| `m_name` | `str` | 必填 | 传给该接口的 `m` 名称 参数，Python 类型为 `str`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `mName: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。 |
| `last_modified` | `int` | `0` | 传给该接口的 `last` `modified` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `lastModified: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree::robot::LeaseCache`
- 签名：`Set(int64_t, const std::string &, int64_t)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/server/lease_server.hpp:16`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.set(id=id, m_name=m_name, last_modified=last_modified)
```

<a id="unitree-sdk2-cpp-robot-leasecache-renewal-1"></a>
#### `unitree_sdk2_cpp.robot.LeaseCache.renewal`

对应 C++ SDK 操作 `Renewal(int64_t)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def renewal(self, last_modified: int = 0) -> None
```

**可用性与安全性**

**`AVAILABLE` / `UNCLASSIFIED`**：当前绑定源码已实现；实际执行条件仍取决于平台和对应 SDK 环境。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `last_modified` | `int` | `0` | 传给该接口的 `last` `modified` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `lastModified: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree::robot::LeaseCache`
- 签名：`Renewal(int64_t)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/server/lease_server.hpp:17`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.renewal(last_modified=last_modified)
```

<a id="unitree-sdk2-cpp-robot-leasecache-clear-1"></a>
#### `unitree_sdk2_cpp.robot.LeaseCache.clear`

对应 C++ SDK 操作 `Clear()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def clear(self) -> None
```

**可用性与安全性**

**`AVAILABLE` / `UNCLASSIFIED`**：当前绑定源码已实现；实际执行条件仍取决于平台和对应 SDK 环境。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree::robot::LeaseCache`
- 签名：`Clear()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/server/lease_server.hpp:18`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.clear()
```

<a id="unitree-sdk2-cpp-robot-leasecache-get-last-modified-1"></a>
#### `unitree_sdk2_cpp.robot.LeaseCache.get_last_modified`

查询或检查 `last` `modified`。

**签名**

```python
def get_last_modified(self) -> int
```

**可用性与安全性**

**`AVAILABLE` / `UNCLASSIFIED`**：当前绑定源码已实现；实际执行条件仍取决于平台和对应 SDK 环境。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::LeaseCache`
- 签名：`GetLastModified() const`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/server/lease_server.hpp:20`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.get_last_modified()
```

<a id="unitree-sdk2-cpp-robot-leasecache-get-id-1"></a>
#### `unitree_sdk2_cpp.robot.LeaseCache.get_id`

查询或检查 ID。

**签名**

```python
def get_id(self) -> int
```

**可用性与安全性**

**`AVAILABLE` / `UNCLASSIFIED`**：当前绑定源码已实现；实际执行条件仍取决于平台和对应 SDK 环境。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::LeaseCache`
- 签名：`GetId() const`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/server/lease_server.hpp:21`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.get_id()
```

<a id="unitree-sdk2-cpp-robot-leasecache-get-name-1"></a>
#### `unitree_sdk2_cpp.robot.LeaseCache.get_name`

查询或检查 名称。

**签名**

```python
def get_name(self) -> str
```

**可用性与安全性**

**`AVAILABLE` / `UNCLASSIFIED`**：当前绑定源码已实现；实际执行条件仍取决于平台和对应 SDK 环境。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `str` | 返回 `str`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree::robot::LeaseCache`
- 签名：`GetName() const`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/server/lease_server.hpp:22`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.get_name()
```

<a id="unitree-sdk2-cpp-robot-leaseclient"></a>
### `unitree_sdk2_cpp.robot.LeaseClient`

Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

**导入**

```python
from unitree_sdk2_cpp.robot import LeaseClient
```

**基类**：`ClientBase`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-leaseclient-dunder-init-1) | `def __init__(self, name: str) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`init`](#unitree-sdk2-cpp-robot-leaseclient-init-1) | `def init(self) -> None` | `AVAILABLE` | `INITIALIZATION` |
| [`wait_applied`](#unitree-sdk2-cpp-robot-leaseclient-wait-applied-1) | `def wait_applied(self) -> None` | `AVAILABLE` | `INITIALIZATION` |
| [`get_id`](#unitree-sdk2-cpp-robot-leaseclient-get-id-1) | `def get_id(self) -> int` | `AVAILABLE` | `READ_ONLY` |
| [`applied`](#unitree-sdk2-cpp-robot-leaseclient-applied-1) | `def applied(self) -> bool` | `AVAILABLE` | `READ_ONLY` |

<a id="unitree-sdk2-cpp-robot-leaseclient-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.LeaseClient.__init__`

初始化 `LeaseClient` 实例。是否能实际构造取决于下方可用性状态。

**签名**

```python
def __init__(self, name: str) -> None
```

**可用性与安全性**

**`AVAILABLE` / `CONSTRUCTION`**：当前绑定源码已实现；实际执行条件仍取决于平台和对应 SDK 环境。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `name` | `str` | 必填 | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。 |

**对应 C++**

- 类：`unitree::robot::LeaseClient`
- 签名：`LeaseClient(const std::string &)`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/client/lease_client.hpp:35`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = LeaseClient(name=name)
```

<a id="unitree-sdk2-cpp-robot-leaseclient-init-1"></a>
#### `unitree_sdk2_cpp.robot.LeaseClient.init`

初始化当前 SDK 对象所需的底层通道或服务资源。

**签名**

```python
def init(self) -> None
```

**可用性与安全性**

**`AVAILABLE` / `INITIALIZATION`**：当前绑定源码已实现；实际执行条件仍取决于平台和对应 SDK 环境。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree::robot::LeaseClient`
- 签名：`Init()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/client/lease_client.hpp:38`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.init()
```

<a id="unitree-sdk2-cpp-robot-leaseclient-wait-applied-1"></a>
#### `unitree_sdk2_cpp.robot.LeaseClient.wait_applied`

对应 C++ SDK 操作 `WaitApplied()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def wait_applied(self) -> None
```

**可用性与安全性**

**`AVAILABLE` / `INITIALIZATION`**：当前绑定源码已实现；实际执行条件仍取决于平台和对应 SDK 环境。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree::robot::LeaseClient`
- 签名：`WaitApplied()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/client/lease_client.hpp:40`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.wait_applied()
```

<a id="unitree-sdk2-cpp-robot-leaseclient-get-id-1"></a>
#### `unitree_sdk2_cpp.robot.LeaseClient.get_id`

查询或检查 ID。

**签名**

```python
def get_id(self) -> int
```

**可用性与安全性**

**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现只读查询。Robot Client 的服务端查询通常仍需匹配的 Linux 扩展、DDS、网络、机器人和服务；纯本地 getter 则不一定需要全部条件。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::LeaseClient`
- 签名：`GetId()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/client/lease_client.hpp:41`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.get_id()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-leaseclient-applied-1"></a>
#### `unitree_sdk2_cpp.robot.LeaseClient.applied`

对应 C++ SDK 操作 `Applied()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def applied(self) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现只读查询。Robot Client 的服务端查询通常仍需匹配的 Linux 扩展、DDS、网络、机器人和服务；纯本地 getter 则不一定需要全部条件。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree::robot::LeaseClient`
- 签名：`Applied()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/client/lease_client.hpp:42`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.applied()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-leasecontext"></a>
### `unitree_sdk2_cpp.robot.LeaseContext`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot import LeaseContext
```

**基类**：`object`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-leasecontext-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`update`](#unitree-sdk2-cpp-robot-leasecontext-update-1) | `def update(self, id: int, term: int) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`reset`](#unitree-sdk2-cpp-robot-leasecontext-reset-1) | `def reset(self) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`valid`](#unitree-sdk2-cpp-robot-leasecontext-valid-1) | `def valid(self) -> bool` | `AVAILABLE` | `UNCLASSIFIED` |
| [`get_id`](#unitree-sdk2-cpp-robot-leasecontext-get-id-1) | `def get_id(self) -> int` | `AVAILABLE` | `UNCLASSIFIED` |
| [`get_term`](#unitree-sdk2-cpp-robot-leasecontext-get-term-1) | `def get_term(self) -> int` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-leasecontext-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.LeaseContext.__init__`

初始化 `LeaseContext` 实例。是否能实际构造取决于下方可用性状态。

**签名**

```python
def __init__(self) -> None
```

**可用性与安全性**

**`AVAILABLE` / `CONSTRUCTION`**：当前绑定源码已实现；实际执行条件仍取决于平台和对应 SDK 环境。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。 |

**对应 C++**

- 类：`unitree::robot::LeaseContext`
- 签名：`LeaseContext()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/client/lease_client.hpp:14`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = LeaseContext()
```

<a id="unitree-sdk2-cpp-robot-leasecontext-update-1"></a>
#### `unitree_sdk2_cpp.robot.LeaseContext.update`

对应 C++ SDK 操作 `Update(int64_t, int64_t)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def update(self, id: int, term: int) -> None
```

**可用性与安全性**

**`AVAILABLE` / `UNCLASSIFIED`**：当前绑定源码已实现；实际执行条件仍取决于平台和对应 SDK 环境。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `id` | `int` | 必填 | 传给该接口的 ID 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `id: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。 |
| `term` | `int` | 必填 | 传给该接口的 `term` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `term: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree::robot::LeaseContext`
- 签名：`Update(int64_t, int64_t)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/client/lease_client.hpp:17`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.update(id=id, term=term)
```

<a id="unitree-sdk2-cpp-robot-leasecontext-reset-1"></a>
#### `unitree_sdk2_cpp.robot.LeaseContext.reset`

对应 C++ SDK 操作 `Reset()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def reset(self) -> None
```

**可用性与安全性**

**`AVAILABLE` / `UNCLASSIFIED`**：当前绑定源码已实现；实际执行条件仍取决于平台和对应 SDK 环境。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree::robot::LeaseContext`
- 签名：`Reset()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/client/lease_client.hpp:18`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.reset()
```

<a id="unitree-sdk2-cpp-robot-leasecontext-valid-1"></a>
#### `unitree_sdk2_cpp.robot.LeaseContext.valid`

对应 C++ SDK 操作 `Valid() const`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def valid(self) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `UNCLASSIFIED`**：当前绑定源码已实现；实际执行条件仍取决于平台和对应 SDK 环境。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree::robot::LeaseContext`
- 签名：`Valid() const`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/client/lease_client.hpp:20`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.valid()
```

<a id="unitree-sdk2-cpp-robot-leasecontext-get-id-1"></a>
#### `unitree_sdk2_cpp.robot.LeaseContext.get_id`

查询或检查 ID。

**签名**

```python
def get_id(self) -> int
```

**可用性与安全性**

**`AVAILABLE` / `UNCLASSIFIED`**：当前绑定源码已实现；实际执行条件仍取决于平台和对应 SDK 环境。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::LeaseContext`
- 签名：`GetId() const`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/client/lease_client.hpp:22`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.get_id()
```

<a id="unitree-sdk2-cpp-robot-leasecontext-get-term-1"></a>
#### `unitree_sdk2_cpp.robot.LeaseContext.get_term`

查询或检查 `term`。

**签名**

```python
def get_term(self) -> int
```

**可用性与安全性**

**`AVAILABLE` / `UNCLASSIFIED`**：当前绑定源码已实现；实际执行条件仍取决于平台和对应 SDK 环境。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::LeaseContext`
- 签名：`GetTerm() const`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/client/lease_client.hpp:23`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.get_term()
```

<a id="unitree-sdk2-cpp-robot-leaseserver"></a>
### `unitree_sdk2_cpp.robot.LeaseServer`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot import LeaseServer
```

**基类**：`ServerBase`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-leaseserver-dunder-init-1) | `def __init__(self, name: str, term: int) -> None` | `SIGNATURE_ONLY` | `CONSTRUCTION` |
| [`init`](#unitree-sdk2-cpp-robot-leaseserver-init-1) | `def init(self) -> None` | `SIGNATURE_ONLY` | `UNCLASSIFIED` |
| [`check_request_lease_denied`](#unitree-sdk2-cpp-robot-leaseserver-check-request-lease-denied-1) | `def check_request_lease_denied(self, lease_id: int) -> bool` | `SIGNATURE_ONLY` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-leaseserver-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.LeaseServer.__init__`

初始化 `LeaseServer` 实例。是否能实际构造取决于下方可用性状态。

**签名**

```python
def __init__(self, name: str, term: int) -> None
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `CONSTRUCTION`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `name` | `str` | 必填 | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。 |
| `term` | `int` | 必填 | 传给该接口的 `term` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `term: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。 |

**对应 C++**

- 类：`unitree::robot::LeaseServer`
- 签名：`LeaseServer(const std::string &, int64_t)`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/server/lease_server.hpp:33`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_construct(name: str, term: int) -> LeaseServer:
        return LeaseServer(name=name, term=term)
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-leaseserver-init-1"></a>
#### `unitree_sdk2_cpp.robot.LeaseServer.init`

初始化当前 SDK 对象所需的底层通道或服务资源。

**签名**

```python
def init(self) -> None
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `UNCLASSIFIED`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree::robot::LeaseServer`
- 签名：`Init()`
- 绑定策略：`SIGNATURE_PREVIEW`
- 声明位置：`include/unitree/robot/server/lease_server.hpp:36`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_init(obj: LeaseServer) -> None:
        obj.init()
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-leaseserver-check-request-lease-denied-1"></a>
#### `unitree_sdk2_cpp.robot.LeaseServer.check_request_lease_denied`

查询或检查 请求 lease `denied`。

**签名**

```python
def check_request_lease_denied(self, lease_id: int) -> bool
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `UNCLASSIFIED`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `lease_id` | `int` | 必填 | 传给该接口的 lease ID 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `leaseId: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree::robot::LeaseServer`
- 签名：`CheckRequestLeaseDenied(int64_t)`
- 绑定策略：`SIGNATURE_PREVIEW`
- 声明位置：`include/unitree/robot/server/lease_server.hpp:38`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_check_request_lease_denied(obj: LeaseServer, lease_id: int) -> bool:
        return obj.check_request_lease_denied(lease_id=lease_id)
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-requestfuture"></a>
### `unitree_sdk2_cpp.robot.RequestFuture`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot import RequestFuture
```

**基类**：`object`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__（重载 1/2）`](#unitree-sdk2-cpp-robot-requestfuture-dunder-init-1) | `def __init__(self) -> None` | `SIGNATURE_ONLY` | `CONSTRUCTION` |
| [`__init__（重载 2/2）`](#unitree-sdk2-cpp-robot-requestfuture-dunder-init-2) | `def __init__(self, request_id: int) -> None` | `SIGNATURE_ONLY` | `CONSTRUCTION` |
| [`set_request_id`](#unitree-sdk2-cpp-robot-requestfuture-set-request-id-1) | `def set_request_id(self, request_id: int) -> None` | `SIGNATURE_ONLY` | `UNCLASSIFIED` |
| [`get_request_id`](#unitree-sdk2-cpp-robot-requestfuture-get-request-id-1) | `def get_request_id(self) -> int` | `SIGNATURE_ONLY` | `UNCLASSIFIED` |
| [`set_queue`](#unitree-sdk2-cpp-robot-requestfuture-set-queue-1) | `def set_queue(self, future_queue_ptr: RequestFutureQueue) -> bool` | `SIGNATURE_ONLY` | `UNCLASSIFIED` |
| [`get_response`](#unitree-sdk2-cpp-robot-requestfuture-get-response-1) | `def get_response(self, microsec: int) -> Any` | `SIGNATURE_ONLY` | `UNCLASSIFIED` |
| [`ready`](#unitree-sdk2-cpp-robot-requestfuture-ready-1) | `def ready(self, request_ptr: Any) -> None` | `SIGNATURE_ONLY` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-requestfuture-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.RequestFuture.__init__`（重载 1/2）

初始化 `RequestFuture` 实例。是否能实际构造取决于下方可用性状态。

**签名**

```python
@overload
def __init__(self) -> None
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `CONSTRUCTION`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。 |

**对应 C++**

- 类：`unitree::robot::RequestFuture`
- 签名：`RequestFuture()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/future/request_future.hpp:27`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_construct() -> RequestFuture:
        return RequestFuture()
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-requestfuture-dunder-init-2"></a>
#### `unitree_sdk2_cpp.robot.RequestFuture.__init__`（重载 2/2）

初始化 `RequestFuture` 实例。是否能实际构造取决于下方可用性状态。

**签名**

```python
@overload
def __init__(self, request_id: int) -> None
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `CONSTRUCTION`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `request_id` | `int` | 必填 | 传给该接口的 请求 ID 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `requestId: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。 |

**对应 C++**

- 类：`unitree::robot::RequestFuture`
- 签名：`RequestFuture(int64_t)`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/future/request_future.hpp:28`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_construct(request_id: int) -> RequestFuture:
        return RequestFuture(request_id=request_id)
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-requestfuture-set-request-id-1"></a>
#### `unitree_sdk2_cpp.robot.RequestFuture.set_request_id`

设置 请求 ID。具体副作用和安全边界见下方状态。

**签名**

```python
def set_request_id(self, request_id: int) -> None
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `UNCLASSIFIED`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `request_id` | `int` | 必填 | 传给该接口的 请求 ID 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `requestId: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree::robot::RequestFuture`
- 签名：`SetRequestId(int64_t)`
- 绑定策略：`SIGNATURE_PREVIEW`
- 声明位置：`include/unitree/robot/future/request_future.hpp:31`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_set_request_id(obj: RequestFuture, request_id: int) -> None:
        obj.set_request_id(request_id=request_id)
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-requestfuture-get-request-id-1"></a>
#### `unitree_sdk2_cpp.robot.RequestFuture.get_request_id`

查询或检查 请求 ID。

**签名**

```python
def get_request_id(self) -> int
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `UNCLASSIFIED`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::RequestFuture`
- 签名：`GetRequestId() const`
- 绑定策略：`SIGNATURE_PREVIEW`
- 声明位置：`include/unitree/robot/future/request_future.hpp:32`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_get_request_id(obj: RequestFuture) -> int:
        return obj.get_request_id()
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-requestfuture-set-queue-1"></a>
#### `unitree_sdk2_cpp.robot.RequestFuture.set_queue`

设置 `queue`。具体副作用和安全边界见下方状态。

**签名**

```python
def set_queue(self, future_queue_ptr: RequestFutureQueue) -> bool
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `UNCLASSIFIED`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `future_queue_ptr` | `RequestFutureQueue` | 必填 | 传给该接口的 `future` `queue` `ptr` 参数，Python 类型为 `RequestFutureQueue`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `futureQueuePtr: const std::shared_ptr<RequestFutureQueue> &`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree::robot::RequestFuture`
- 签名：`SetQueue(const std::shared_ptr<RequestFutureQueue> &)`
- 绑定策略：`SIGNATURE_PREVIEW`
- 声明位置：`include/unitree/robot/future/request_future.hpp:34`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_set_queue(obj: RequestFuture, future_queue_ptr: RequestFutureQueue) -> bool:
        return obj.set_queue(future_queue_ptr=future_queue_ptr)
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-requestfuture-get-response-1"></a>
#### `unitree_sdk2_cpp.robot.RequestFuture.get_response`

查询或检查 响应。

**签名**

```python
def get_response(self, microsec: int) -> Any
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `UNCLASSIFIED`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `microsec` | `int` | 必填 | 等待时间，单位为微秒。具体超时结果以 SDK 方法约定为准。 对应 C++ 参数 `microsec: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `Any` | 返回 `Any`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree::robot::RequestFuture`
- 签名：`GetResponse(int64_t)`
- 绑定策略：`SIGNATURE_PREVIEW`
- 声明位置：`include/unitree/robot/future/request_future.hpp:36`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_get_response(obj: RequestFuture, microsec: int) -> Any:
        return obj.get_response(microsec=microsec)
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-requestfuture-ready-1"></a>
#### `unitree_sdk2_cpp.robot.RequestFuture.ready`

对应 C++ SDK 操作 `Ready(const unitree::robot::ResponsePtr &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def ready(self, request_ptr: Any) -> None
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `UNCLASSIFIED`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `request_ptr` | `Any` | 必填 | 传给该接口的 请求 `ptr` 参数，Python 类型为 `Any`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `requestPtr: const unitree::robot::ResponsePtr &`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree::robot::RequestFuture`
- 签名：`Ready(const unitree::robot::ResponsePtr &)`
- 绑定策略：`SIGNATURE_PREVIEW`
- 声明位置：`include/unitree/robot/future/request_future.hpp:39`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_ready(obj: RequestFuture, request_ptr: Any) -> None:
        obj.ready(request_ptr=request_ptr)
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-requestfuturequeue"></a>
### `unitree_sdk2_cpp.robot.RequestFutureQueue`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot import RequestFutureQueue
```

**基类**：`object`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-requestfuturequeue-dunder-init-1) | `def __init__(self) -> None` | `SIGNATURE_ONLY` | `CONSTRUCTION` |
| [`get`](#unitree-sdk2-cpp-robot-requestfuturequeue-get-1) | `def get(self, request_id: int) -> RequestFuture` | `SIGNATURE_ONLY` | `UNCLASSIFIED` |
| [`put`](#unitree-sdk2-cpp-robot-requestfuturequeue-put-1) | `def put(self, request_id: int, future_ptr: RequestFuture) -> bool` | `SIGNATURE_ONLY` | `UNCLASSIFIED` |
| [`remove`](#unitree-sdk2-cpp-robot-requestfuturequeue-remove-1) | `def remove(self, request_id: int) -> None` | `SIGNATURE_ONLY` | `UNCLASSIFIED` |
| [`size`](#unitree-sdk2-cpp-robot-requestfuturequeue-size-1) | `def size(self) -> int` | `SIGNATURE_ONLY` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-requestfuturequeue-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.RequestFutureQueue.__init__`

初始化 `RequestFutureQueue` 实例。是否能实际构造取决于下方可用性状态。

**签名**

```python
def __init__(self) -> None
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `CONSTRUCTION`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。 |

**对应 C++**

- 类：`unitree::robot::RequestFutureQueue`
- 签名：`RequestFutureQueue()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/future/request_future.hpp:65`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_construct() -> RequestFutureQueue:
        return RequestFutureQueue()
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-requestfuturequeue-get-1"></a>
#### `unitree_sdk2_cpp.robot.RequestFutureQueue.get`

对应 C++ SDK 操作 `Get(int64_t)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def get(self, request_id: int) -> RequestFuture
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `UNCLASSIFIED`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `request_id` | `int` | 必填 | 传给该接口的 请求 ID 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `requestId: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `RequestFuture` | 返回 `RequestFuture`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree::robot::RequestFutureQueue`
- 签名：`Get(int64_t)`
- 绑定策略：`SIGNATURE_PREVIEW`
- 声明位置：`include/unitree/robot/future/request_future.hpp:68`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_get(obj: RequestFutureQueue, request_id: int) -> RequestFuture:
        return obj.get(request_id=request_id)
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-requestfuturequeue-put-1"></a>
#### `unitree_sdk2_cpp.robot.RequestFutureQueue.put`

对应 C++ SDK 操作 `Put(int64_t, const unitree::robot::RequestFuturePtr &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def put(self, request_id: int, future_ptr: RequestFuture) -> bool
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `UNCLASSIFIED`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `request_id` | `int` | 必填 | 传给该接口的 请求 ID 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `requestId: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。 |
| `future_ptr` | `RequestFuture` | 必填 | 传给该接口的 `future` `ptr` 参数，Python 类型为 `RequestFuture`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `futurePtr: const unitree::robot::RequestFuturePtr &`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree::robot::RequestFutureQueue`
- 签名：`Put(int64_t, const unitree::robot::RequestFuturePtr &)`
- 绑定策略：`SIGNATURE_PREVIEW`
- 声明位置：`include/unitree/robot/future/request_future.hpp:69`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_put(obj: RequestFutureQueue, request_id: int, future_ptr: RequestFuture) -> bool:
        return obj.put(request_id=request_id, future_ptr=future_ptr)
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-requestfuturequeue-remove-1"></a>
#### `unitree_sdk2_cpp.robot.RequestFutureQueue.remove`

对应 C++ SDK 操作 `Remove(int64_t)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def remove(self, request_id: int) -> None
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `UNCLASSIFIED`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `request_id` | `int` | 必填 | 传给该接口的 请求 ID 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `requestId: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree::robot::RequestFutureQueue`
- 签名：`Remove(int64_t)`
- 绑定策略：`SIGNATURE_PREVIEW`
- 声明位置：`include/unitree/robot/future/request_future.hpp:70`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_remove(obj: RequestFutureQueue, request_id: int) -> None:
        obj.remove(request_id=request_id)
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-requestfuturequeue-size-1"></a>
#### `unitree_sdk2_cpp.robot.RequestFutureQueue.size`

对应 C++ SDK 操作 `Size()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def size(self) -> int
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `UNCLASSIFIED`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::RequestFutureQueue`
- 签名：`Size()`
- 绑定策略：`SIGNATURE_PREVIEW`
- 声明位置：`include/unitree/robot/future/request_future.hpp:72`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_size(obj: RequestFutureQueue) -> int:
        return obj.size()
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-server"></a>
### `unitree_sdk2_cpp.robot.Server`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot import Server
```

**基类**：`ServerBase`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-server-dunder-init-1) | `def __init__(self, name: str) -> None` | `SIGNATURE_ONLY` | `CONSTRUCTION` |
| [`init`](#unitree-sdk2-cpp-robot-server-init-1) | `def init(self) -> None` | `SIGNATURE_ONLY` | `UNCLASSIFIED` |
| [`start_lease（重载 1/2）`](#unitree-sdk2-cpp-robot-server-start-lease-1) | `def start_lease(self, lease_term: int) -> None` | `SIGNATURE_ONLY` | `UNCLASSIFIED` |
| [`start_lease（重载 2/2）`](#unitree-sdk2-cpp-robot-server-start-lease-2) | `def start_lease(self, lease_term: float) -> None` | `SIGNATURE_ONLY` | `UNCLASSIFIED` |
| [`get_name`](#unitree-sdk2-cpp-robot-server-get-name-1) | `def get_name(self) -> str` | `SIGNATURE_ONLY` | `UNCLASSIFIED` |
| [`get_api_version`](#unitree-sdk2-cpp-robot-server-get-api-version-1) | `def get_api_version(self) -> str` | `SIGNATURE_ONLY` | `UNCLASSIFIED` |
| [`get_current_api_id`](#unitree-sdk2-cpp-robot-server-get-current-api-id-1) | `def get_current_api_id(self) -> int` | `SIGNATURE_ONLY` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-server-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.Server.__init__`

初始化 `Server` 实例。是否能实际构造取决于下方可用性状态。

**签名**

```python
def __init__(self, name: str) -> None
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `CONSTRUCTION`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `name` | `str` | 必填 | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。 |

**对应 C++**

- 类：`unitree::robot::Server`
- 签名：`Server(const std::string &)`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/server/server.hpp:29`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_construct(name: str) -> Server:
        return Server(name=name)
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-server-init-1"></a>
#### `unitree_sdk2_cpp.robot.Server.init`

初始化当前 SDK 对象所需的底层通道或服务资源。

**签名**

```python
def init(self) -> None
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `UNCLASSIFIED`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree::robot::Server`
- 签名：`Init()`
- 绑定策略：`SIGNATURE_PREVIEW`
- 声明位置：`include/unitree/robot/server/server.hpp:32`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_init(obj: Server) -> None:
        obj.init()
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-server-start-lease-1"></a>
#### `unitree_sdk2_cpp.robot.Server.start_lease`（重载 1/2）

启动对应 SDK 操作。具体副作用和安全边界见下方状态。

**签名**

```python
@overload
def start_lease(self, lease_term: int) -> None
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `UNCLASSIFIED`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `lease_term` | `int` | 必填 | 传给该接口的 lease `term` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `leaseTerm: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree::robot::Server`
- 签名：`StartLease(int64_t)`
- 绑定策略：`SIGNATURE_PREVIEW`
- 声明位置：`include/unitree/robot/server/server.hpp:34`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_start_lease(obj: Server, lease_term: int) -> None:
        obj.start_lease(lease_term=lease_term)
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-server-start-lease-2"></a>
#### `unitree_sdk2_cpp.robot.Server.start_lease`（重载 2/2）

启动对应 SDK 操作。具体副作用和安全边界见下方状态。

**签名**

```python
@overload
def start_lease(self, lease_term: float) -> None
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `UNCLASSIFIED`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `lease_term` | `float` | 必填 | 传给该接口的 lease `term` 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `leaseTerm: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree::robot::Server`
- 签名：`StartLease(float)`
- 绑定策略：`SIGNATURE_PREVIEW`
- 声明位置：`include/unitree/robot/server/server.hpp:35`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_start_lease(obj: Server, lease_term: float) -> None:
        obj.start_lease(lease_term=lease_term)
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-server-get-name-1"></a>
#### `unitree_sdk2_cpp.robot.Server.get_name`

查询或检查 名称。

**签名**

```python
def get_name(self) -> str
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `UNCLASSIFIED`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `str` | 返回 `str`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree::robot::Server`
- 签名：`GetName()`
- 绑定策略：`SIGNATURE_PREVIEW`
- 声明位置：`include/unitree/robot/server/server.hpp:37`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_get_name(obj: Server) -> str:
        return obj.get_name()
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-server-get-api-version-1"></a>
#### `unitree_sdk2_cpp.robot.Server.get_api_version`

查询或检查 API `version`。

**签名**

```python
def get_api_version(self) -> str
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `UNCLASSIFIED`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `str` | 返回 `str`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree::robot::Server`
- 签名：`GetApiVersion() const`
- 绑定策略：`SIGNATURE_PREVIEW`
- 声明位置：`include/unitree/robot/server/server.hpp:38`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_get_api_version(obj: Server) -> str:
        return obj.get_api_version()
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-server-get-current-api-id-1"></a>
#### `unitree_sdk2_cpp.robot.Server.get_current_api_id`

查询或检查 `current` API ID。

**签名**

```python
def get_current_api_id(self) -> int
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `UNCLASSIFIED`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::Server`
- 签名：`GetCurrentApiId() const`
- 绑定策略：`SIGNATURE_PREVIEW`
- 声明位置：`include/unitree/robot/server/server.hpp:40`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_get_current_api_id(obj: Server) -> int:
        return obj.get_current_api_id()
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-serverbase"></a>
### `unitree_sdk2_cpp.robot.ServerBase`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot import ServerBase
```

**基类**：`object`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-serverbase-dunder-init-1) | `def __init__(self, name: str) -> None` | `SIGNATURE_ONLY` | `CONSTRUCTION` |
| [`init`](#unitree-sdk2-cpp-robot-serverbase-init-1) | `def init(self) -> None` | `SIGNATURE_ONLY` | `UNCLASSIFIED` |
| [`start`](#unitree-sdk2-cpp-robot-serverbase-start-1) | `def start(self, enable_proi_queue: bool = ...) -> None` | `SIGNATURE_ONLY` | `UNCLASSIFIED` |
| [`get_name`](#unitree-sdk2-cpp-robot-serverbase-get-name-1) | `def get_name(self) -> str` | `SIGNATURE_ONLY` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-serverbase-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.ServerBase.__init__`

初始化 `ServerBase` 实例。是否能实际构造取决于下方可用性状态。

**签名**

```python
def __init__(self, name: str) -> None
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `CONSTRUCTION`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `name` | `str` | 必填 | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。 |

**对应 C++**

- 类：`unitree::robot::ServerBase`
- 签名：`ServerBase(const std::string &)`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/server/server_base.hpp:13`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_construct(name: str) -> ServerBase:
        return ServerBase(name=name)
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-serverbase-init-1"></a>
#### `unitree_sdk2_cpp.robot.ServerBase.init`

初始化当前 SDK 对象所需的底层通道或服务资源。

**签名**

```python
def init(self) -> None
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `UNCLASSIFIED`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree::robot::ServerBase`
- 签名：`Init()`
- 绑定策略：`SIGNATURE_PREVIEW`
- 声明位置：`include/unitree/robot/server/server_base.hpp:16`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_init(obj: ServerBase) -> None:
        obj.init()
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-serverbase-start-1"></a>
#### `unitree_sdk2_cpp.robot.ServerBase.start`

启动对应 SDK 操作。具体副作用和安全边界见下方状态。

**签名**

```python
def start(self, enable_proi_queue: bool = ...) -> None
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `UNCLASSIFIED`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `enable_proi_queue` | `bool` | `...` | 是否启用 SDK 中名为 `proi` 的队列选项；该名称沿用上游接口，具体行为需查对应头文件。 对应 C++ 参数 `enableProiQueue: bool`。 只接受布尔语义。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree::robot::ServerBase`
- 签名：`Start(bool)`
- 绑定策略：`SIGNATURE_PREVIEW`
- 声明位置：`include/unitree/robot/server/server_base.hpp:17`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 默认值显示为 `...`，表示 C++ 声明存在默认参数，但当前 AST 清单没有保存其字面量；省略参数可使用上游默认行为。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_start(obj: ServerBase, enable_proi_queue: bool) -> None:
        obj.start(enable_proi_queue=enable_proi_queue)
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-serverbase-get-name-1"></a>
#### `unitree_sdk2_cpp.robot.ServerBase.get_name`

查询或检查 名称。

**签名**

```python
def get_name(self) -> str
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `UNCLASSIFIED`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `str` | 返回 `str`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree::robot::ServerBase`
- 签名：`GetName() const`
- 绑定策略：`SIGNATURE_PREVIEW`
- 声明位置：`include/unitree/robot/server/server_base.hpp:19`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_get_name(obj: ServerBase) -> str:
        return obj.get_name()
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-serverchannelnamer"></a>
### `unitree_sdk2_cpp.robot.ServerChannelNamer`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot import ServerChannelNamer
```

**基类**：`ChannelNamer`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-serverchannelnamer-dunder-init-1) | `def __init__(self) -> None` | `SIGNATURE_ONLY` | `CONSTRUCTION` |

<a id="unitree-sdk2-cpp-robot-serverchannelnamer-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.ServerChannelNamer.__init__`

初始化 `ServerChannelNamer` 实例。是否能实际构造取决于下方可用性状态。

**签名**

```python
def __init__(self) -> None
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `CONSTRUCTION`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。 |

**对应 C++**

- 类：`unitree::robot::ServerChannelNamer`
- 签名：`ServerChannelNamer()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/channel/channel_namer.hpp:51`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_construct() -> ServerChannelNamer:
        return ServerChannelNamer()
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-serverstub"></a>
### `unitree_sdk2_cpp.robot.ServerStub`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot import ServerStub
```

**基类**：`object`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-serverstub-dunder-init-1) | `def __init__(self) -> None` | `SIGNATURE_ONLY` | `CONSTRUCTION` |
| [`init`](#unitree-sdk2-cpp-robot-serverstub-init-1) | `def init(self, name: str, handler: Callable[..., Any], enable_proi_queue: bool) -> None` | `SIGNATURE_ONLY` | `UNCLASSIFIED` |
| [`send`](#unitree-sdk2-cpp-robot-serverstub-send-1) | `def send(self, response: Any, timeout: int = ...) -> bool` | `SIGNATURE_ONLY` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-serverstub-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.ServerStub.__init__`

初始化 `ServerStub` 实例。是否能实际构造取决于下方可用性状态。

**签名**

```python
def __init__(self) -> None
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `CONSTRUCTION`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。 |

**对应 C++**

- 类：`unitree::robot::ServerStub`
- 签名：`ServerStub()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/server/server_stub.hpp:18`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_construct() -> ServerStub:
        return ServerStub()
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-serverstub-init-1"></a>
#### `unitree_sdk2_cpp.robot.ServerStub.init`

初始化当前 SDK 对象所需的底层通道或服务资源。

**签名**

```python
def init(self, name: str, handler: Callable[..., Any], enable_proi_queue: bool) -> None
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `UNCLASSIFIED`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `name` | `str` | 必填 | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。 |
| `handler` | `Callable[..., Any]` | 必填 | 传给该接口的 `handler` 参数，Python 类型为 `Callable[..., Any]`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `handler: const unitree::robot::ServerRequestHandler &`。 |
| `enable_proi_queue` | `bool` | 必填 | 是否启用 SDK 中名为 `proi` 的队列选项；该名称沿用上游接口，具体行为需查对应头文件。 对应 C++ 参数 `enableProiQueue: bool`。 只接受布尔语义。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree::robot::ServerStub`
- 签名：`Init(const std::string &, const unitree::robot::ServerRequestHandler &, bool)`
- 绑定策略：`SIGNATURE_PREVIEW`
- 声明位置：`include/unitree/robot/server/server_stub.hpp:21`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。
- 回调可能由 SDK 工作线程触发；回调应快速返回、捕获异常，并通过线程安全队列移交耗时工作。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_init(obj: ServerStub, name: str, handler: Callable[..., Any], enable_proi_queue: bool) -> None:
        obj.init(name=name, handler=handler, enable_proi_queue=enable_proi_queue)
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

<a id="unitree-sdk2-cpp-robot-serverstub-send-1"></a>
#### `unitree_sdk2_cpp.robot.ServerStub.send`

对应 C++ SDK 操作 `Send(const unitree::robot::Response &, int64_t)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def send(self, response: Any, timeout: int = ...) -> bool
```

**可用性与安全性**

**`SIGNATURE_ONLY` / `UNCLASSIFIED`**：当前只有设计期签名，不能假设已存在于运行时扩展。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `response` | `Any` | 必填 | 传给该接口的 响应 参数，Python 类型为 `Any`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `response: const unitree::robot::Response &`。 |
| `timeout` | `int` | `...` | 传给该接口的 超时 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `timeout: int64_t`。 取值范围为 -9223372036854775808 到 9223372036854775807。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree::robot::ServerStub`
- 签名：`Send(const unitree::robot::Response &, int64_t)`
- 绑定策略：`SIGNATURE_PREVIEW`
- 声明位置：`include/unitree/robot/server/server_stub.hpp:22`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 默认值显示为 `...`，表示 C++ 声明存在默认参数，但当前 AST 清单没有保存其字面量；省略参数可使用上游默认行为。
- 该条目可以被编辑器和类型检查器识别，但当前运行时可能在属性查找阶段直接失败。

**用法**

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def planned_send(obj: ServerStub, response: Any, timeout: int) -> bool:
        return obj.send(response=response, timeout=timeout)
```

> [!CAUTION]
> 上面的 `TYPE_CHECKING` 示例只表达计划调用形态。该分支在普通 Python 运行时为假，不代表当前扩展能执行此接口。

---

[返回 API 总索引](../API_REFERENCE_ZH.md)
