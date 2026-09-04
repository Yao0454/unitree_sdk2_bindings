# Unitree SDK2 Python API 参考分卷

[返回 API 总索引](../API_REFERENCE_ZH.md) · [阅读从零开始指南](../BEGINNER_GUIDE_ZH.md)

> [!WARNING]
> 本分卷同时包含 `AVAILABLE` 和 `SIGNATURE_ONLY`。后者只是设计期类型签名。运动及硬件副作用方法即使标记为 `AVAILABLE`，也不表示当前环境可安全执行。

> [!NOTE]
> 本文件由 `generator/generate_api_docs.py` 自动生成，请勿手工维护 API 条目。

---

<a id="unitree-sdk2-cpp-channel"></a>
## Typed DDS Channel API

模块：`unitree_sdk2_cpp.channel`

### 模块函数导入

```python
from unitree_sdk2_cpp.channel import registered_message_types, initialize, initialize_from_config, release
```

下面的函数用法片段假设已经完成上述导入。

### 模块函数索引

| 函数 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`registered_message_types()`](#unitree-sdk2-cpp-channel-registered-message-types-1) | `def registered_message_types() -> list[str]` | `AVAILABLE` | `DDS_LIFECYCLE` |
| [`initialize()`](#unitree-sdk2-cpp-channel-initialize-1) | `def initialize(domain_id: int = 0, network_interface: str = '') -> None` | `AVAILABLE` | `DDS_LIFECYCLE` |
| [`initialize_from_config()`](#unitree-sdk2-cpp-channel-initialize-from-config-1) | `def initialize_from_config(config_file: str = '') -> None` | `AVAILABLE` | `DDS_LIFECYCLE` |
| [`release()`](#unitree-sdk2-cpp-channel-release-1) | `def release() -> None` | `AVAILABLE` | `DDS_LIFECYCLE` |

### 类索引

| 类 | 公开函数签名 | 属性 |
| --- | ---: | ---: |
| [`ChannelPublisher`](#unitree-sdk2-cpp-channel-channelpublisher) | 4 | 2 |
| [`ChannelSubscriber`](#unitree-sdk2-cpp-channel-channelsubscriber) | 3 | 3 |

<a id="unitree-sdk2-cpp-channel-registered-message-types-1"></a>
#### `unitree_sdk2_cpp.channel.registered_message_types`

返回当前二进制扩展已经注册的 typed DDS 消息类型名。

**签名**

```python
def registered_message_types() -> list[str]
```

**可用性与安全性**

**`AVAILABLE` / `DDS_LIFECYCLE`**：当前绑定源码已实现。该操作可能创建、使用或释放 DDS 资源。

**参数**

无参数。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `list[str]` | 当前扩展已注册的 C++ DDS 消息类型名列表。 |

**对应 C++**

- 类：`unitree_sdk2_cpp.channel`
- 签名：`registered_message_types()`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
message_type_names = registered_message_types()
```

<a id="unitree-sdk2-cpp-channel-initialize-1"></a>
#### `unitree_sdk2_cpp.channel.initialize`

使用 Domain ID 和网络接口初始化全局 DDS ChannelFactory。

**签名**

```python
def initialize(domain_id: int = 0, network_interface: str = '') -> None
```

**可用性与安全性**

**`AVAILABLE` / `DDS_LIFECYCLE`**：当前绑定源码已实现。该操作可能创建、使用或释放 DDS 资源。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `domain_id` | `int` | `0` | DDS Domain ID。只有使用兼容 domain 的参与者才能按预期互相发现。 |
| `network_interface` | `str` | `''` | DDS 使用的网络接口名称，例如 Linux 上的 `eth0` 或 `enp3s0`；必须按目标机实际网卡填写。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree_sdk2_cpp.channel`
- 签名：`ChannelFactory::Init(int32_t, const std::string &)`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
initialize(domain_id=0, network_interface="eth0")
```

<a id="unitree-sdk2-cpp-channel-initialize-from-config-1"></a>
#### `unitree_sdk2_cpp.channel.initialize_from_config`

使用 CycloneDDS 配置文件初始化全局 DDS ChannelFactory。

**签名**

```python
def initialize_from_config(config_file: str = '') -> None
```

**可用性与安全性**

**`AVAILABLE` / `DDS_LIFECYCLE`**：当前绑定源码已实现。该操作可能创建、使用或释放 DDS 资源。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `config_file` | `str` | `''` | CycloneDDS 配置文件路径；空字符串表示使用底层默认配置。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree_sdk2_cpp.channel`
- 签名：`ChannelFactory::Init(const std::string &)`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
initialize_from_config(config_file="cyclonedds.xml")
```

<a id="unitree-sdk2-cpp-channel-release-1"></a>
#### `unitree_sdk2_cpp.channel.release`

释放全局 DDS ChannelFactory 及其持有的底层资源。

**签名**

```python
def release() -> None
```

**可用性与安全性**

**`AVAILABLE` / `DDS_LIFECYCLE`**：当前绑定源码已实现。该操作可能创建、使用或释放 DDS 资源。

**参数**

无参数。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree_sdk2_cpp.channel`
- 签名：`ChannelFactory::Release()`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
release()
```

<a id="unitree-sdk2-cpp-channel-channelpublisher"></a>
### `unitree_sdk2_cpp.channel.ChannelPublisher`

typed DDS 通道包装类。必须遵守初始化、启动、关闭和全局释放顺序。

**导入**

```python
from unitree_sdk2_cpp.channel import ChannelPublisher
```

**基类**：`Generic[MessageT]`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-channel-channelpublisher-dunder-init-1) | `def __init__(self, topic: str, message_type: type[MessageT]) -> None` | `AVAILABLE` | `DDS_LIFECYCLE` |
| [`init_channel`](#unitree-sdk2-cpp-channel-channelpublisher-init-channel-1) | `def init_channel(self) -> None` | `AVAILABLE` | `DDS_LIFECYCLE` |
| [`close_channel`](#unitree-sdk2-cpp-channel-channelpublisher-close-channel-1) | `def close_channel(self) -> None` | `AVAILABLE` | `DDS_LIFECYCLE` |
| [`write`](#unitree-sdk2-cpp-channel-channelpublisher-write-1) | `def write(self, message: MessageT, wait_microsec: int = 0) -> bool` | `AVAILABLE` | `DDS_LIFECYCLE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`topic`](#unitree-sdk2-cpp-channel-channelpublisher-topic) | `str` | `只读` | `AVAILABLE` |
| [`message_type_name`](#unitree-sdk2-cpp-channel-channelpublisher-message-type-name) | `str` | `只读` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-channel-channelpublisher-dunder-init-1"></a>
#### `unitree_sdk2_cpp.channel.ChannelPublisher.__init__`

初始化 `ChannelPublisher` 实例。是否能实际构造取决于下方可用性状态。

**签名**

```python
def __init__(self, topic: str, message_type: type[MessageT]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `DDS_LIFECYCLE`**：当前绑定源码已实现。该操作可能创建、使用或释放 DDS 资源。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `topic` | `str` | 必填 | DDS topic 名称。发布端和订阅端必须同时使用兼容的 topic、消息类型和 QoS。 |
| `message_type` | `type[MessageT]` | 必填 | IDL 消息类本身，例如 `LowState`，不是 `LowState()` 实例。该类型必须存在于运行时注册表中。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。 |

**对应 C++**

- 类：`unitree_sdk2_cpp.channel.ChannelPublisher`
- 签名：`ChannelPublisher(const std::string &, type)`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = ChannelPublisher(topic=topic, message_type=message_type)
```

<a id="unitree-sdk2-cpp-channel-channelpublisher-init-channel-1"></a>
#### `unitree_sdk2_cpp.channel.ChannelPublisher.init_channel`

创建并启动 Publisher 的底层 DDS 写通道。

**签名**

```python
def init_channel(self) -> None
```

**可用性与安全性**

**`AVAILABLE` / `DDS_LIFECYCLE`**：当前绑定源码已实现。该操作可能创建、使用或释放 DDS 资源。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree_sdk2_cpp.channel.ChannelPublisher`
- 签名：`ChannelPublisher::init_channel()`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.init_channel()
```

<a id="unitree-sdk2-cpp-channel-channelpublisher-close-channel-1"></a>
#### `unitree_sdk2_cpp.channel.ChannelPublisher.close_channel`

关闭 Publisher 的底层 DDS 写通道。

**签名**

```python
def close_channel(self) -> None
```

**可用性与安全性**

**`AVAILABLE` / `DDS_LIFECYCLE`**：当前绑定源码已实现。该操作可能创建、使用或释放 DDS 资源。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree_sdk2_cpp.channel.ChannelPublisher`
- 签名：`ChannelPublisher::close_channel()`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.close_channel()
```

<a id="unitree-sdk2-cpp-channel-channelpublisher-write-1"></a>
#### `unitree_sdk2_cpp.channel.ChannelPublisher.write`

把一个类型匹配的消息样本写入 Publisher 对应的 DDS topic。

**签名**

```python
def write(self, message: MessageT, wait_microsec: int = 0) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `DDS_LIFECYCLE`**：当前绑定源码已实现。该操作可能创建、使用或释放 DDS 资源。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `message` | `MessageT` | 必填 | 要写入 DDS 的消息实例；类型必须与 Publisher 构造时声明的消息类完全一致。 |
| `wait_microsec` | `int` | `0` | 写操作允许等待的时间，单位为微秒；`0` 使用当前绑定的默认非额外等待行为。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 底层写操作是否被接受；不表示所有订阅者已处理，更不表示设备已经执行动作。 |

**对应 C++**

- 类：`unitree_sdk2_cpp.channel.ChannelPublisher`
- 签名：`ChannelPublisher::write(message, int64_t)`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.write(message=message, wait_microsec=wait_microsec)
```

<a id="unitree-sdk2-cpp-channel-channelpublisher-topic"></a>
#### `unitree_sdk2_cpp.channel.ChannelPublisher.topic`

Publisher 构造时保存的 DDS topic 名称，只读。

**签名**

```python
@property
def topic(self) -> str
```

**可用性与安全性**

**`AVAILABLE` / `DDS_LIFECYCLE`**：当前绑定源码已实现。该操作可能创建、使用或释放 DDS 资源。

**参数**

该属性只读，没有 setter 参数。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `str` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_sdk2_cpp.channel.ChannelPublisher`
- 字段类型：`ChannelPublisher::topic() const`
- 声明位置：由 pybind11 手工绑定提供；manifest 未记录独立头文件行号。

**用法**

```python
current_value = obj.topic
```

<a id="unitree-sdk2-cpp-channel-channelpublisher-message-type-name"></a>
#### `unitree_sdk2_cpp.channel.ChannelPublisher.message_type_name`

Publisher 使用的已注册 C++ 消息类型名，只读。

**签名**

```python
@property
def message_type_name(self) -> str
```

**可用性与安全性**

**`AVAILABLE` / `DDS_LIFECYCLE`**：当前绑定源码已实现。该操作可能创建、使用或释放 DDS 资源。

**参数**

该属性只读，没有 setter 参数。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `str` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_sdk2_cpp.channel.ChannelPublisher`
- 字段类型：`ChannelPublisher::message_type_name() const`
- 声明位置：由 pybind11 手工绑定提供；manifest 未记录独立头文件行号。

**用法**

```python
current_value = obj.message_type_name
```

<a id="unitree-sdk2-cpp-channel-channelsubscriber"></a>
### `unitree_sdk2_cpp.channel.ChannelSubscriber`

typed DDS 通道包装类。必须遵守初始化、启动、关闭和全局释放顺序。

**导入**

```python
from unitree_sdk2_cpp.channel import ChannelSubscriber
```

**基类**：`Generic[MessageT]`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-channel-channelsubscriber-dunder-init-1) | `def __init__(self, topic: str, message_type: type[MessageT], callback: Callable[[MessageT], None], queue_length: int = 0) -> None` | `AVAILABLE` | `DDS_LIFECYCLE` |
| [`init_channel`](#unitree-sdk2-cpp-channel-channelsubscriber-init-channel-1) | `def init_channel(self) -> None` | `AVAILABLE` | `DDS_LIFECYCLE` |
| [`close_channel`](#unitree-sdk2-cpp-channel-channelsubscriber-close-channel-1) | `def close_channel(self) -> None` | `AVAILABLE` | `DDS_LIFECYCLE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`topic`](#unitree-sdk2-cpp-channel-channelsubscriber-topic) | `str` | `只读` | `AVAILABLE` |
| [`message_type_name`](#unitree-sdk2-cpp-channel-channelsubscriber-message-type-name) | `str` | `只读` | `AVAILABLE` |
| [`last_data_available_time`](#unitree-sdk2-cpp-channel-channelsubscriber-last-data-available-time) | `int` | `只读` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-channel-channelsubscriber-dunder-init-1"></a>
#### `unitree_sdk2_cpp.channel.ChannelSubscriber.__init__`

初始化 `ChannelSubscriber` 实例。是否能实际构造取决于下方可用性状态。

**签名**

```python
def __init__(self, topic: str, message_type: type[MessageT], callback: Callable[[MessageT], None], queue_length: int = 0) -> None
```

**可用性与安全性**

**`AVAILABLE` / `DDS_LIFECYCLE`**：当前绑定源码已实现。该操作可能创建、使用或释放 DDS 资源。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `topic` | `str` | 必填 | DDS topic 名称。发布端和订阅端必须同时使用兼容的 topic、消息类型和 QoS。 |
| `message_type` | `type[MessageT]` | 必填 | IDL 消息类本身，例如 `LowState`，不是 `LowState()` 实例。该类型必须存在于运行时注册表中。 |
| `callback` | `Callable[[MessageT], None]` | 必填 | 收到数据或状态变化时调用的 Python 回调。回调签名必须与类型提示一致，并应快速返回。 |
| `queue_length` | `int` | `0` | 订阅队列长度。`0` 使用底层默认行为；更大值会允许更多积压，但也可能增加延迟和内存占用。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。 |

**对应 C++**

- 类：`unitree_sdk2_cpp.channel.ChannelSubscriber`
- 签名：`ChannelSubscriber(const std::string &, type, callback, int64_t)`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 回调可能由 SDK 工作线程触发；回调应快速返回、捕获异常，并通过线程安全队列移交耗时工作。

**用法**

```python
value = ChannelSubscriber(topic=topic, message_type=message_type, callback=callback, queue_length=queue_length)
```

<a id="unitree-sdk2-cpp-channel-channelsubscriber-init-channel-1"></a>
#### `unitree_sdk2_cpp.channel.ChannelSubscriber.init_channel`

创建并启动 Subscriber 的底层 DDS 读通道。

**签名**

```python
def init_channel(self) -> None
```

**可用性与安全性**

**`AVAILABLE` / `DDS_LIFECYCLE`**：当前绑定源码已实现。该操作可能创建、使用或释放 DDS 资源。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree_sdk2_cpp.channel.ChannelSubscriber`
- 签名：`ChannelSubscriber::init_channel()`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.init_channel()
```

<a id="unitree-sdk2-cpp-channel-channelsubscriber-close-channel-1"></a>
#### `unitree_sdk2_cpp.channel.ChannelSubscriber.close_channel`

关闭 Subscriber 的底层 DDS 读通道，并停止后续回调。

**签名**

```python
def close_channel(self) -> None
```

**可用性与安全性**

**`AVAILABLE` / `DDS_LIFECYCLE`**：当前绑定源码已实现。该操作可能创建、使用或释放 DDS 资源。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree_sdk2_cpp.channel.ChannelSubscriber`
- 签名：`ChannelSubscriber::close_channel()`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.close_channel()
```

<a id="unitree-sdk2-cpp-channel-channelsubscriber-topic"></a>
#### `unitree_sdk2_cpp.channel.ChannelSubscriber.topic`

Subscriber 构造时保存的 DDS topic 名称，只读。

**签名**

```python
@property
def topic(self) -> str
```

**可用性与安全性**

**`AVAILABLE` / `DDS_LIFECYCLE`**：当前绑定源码已实现。该操作可能创建、使用或释放 DDS 资源。

**参数**

该属性只读，没有 setter 参数。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `str` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_sdk2_cpp.channel.ChannelSubscriber`
- 字段类型：`ChannelSubscriber::topic() const`
- 声明位置：由 pybind11 手工绑定提供；manifest 未记录独立头文件行号。

**用法**

```python
current_value = obj.topic
```

<a id="unitree-sdk2-cpp-channel-channelsubscriber-message-type-name"></a>
#### `unitree_sdk2_cpp.channel.ChannelSubscriber.message_type_name`

Subscriber 使用的已注册 C++ 消息类型名，只读。

**签名**

```python
@property
def message_type_name(self) -> str
```

**可用性与安全性**

**`AVAILABLE` / `DDS_LIFECYCLE`**：当前绑定源码已实现。该操作可能创建、使用或释放 DDS 资源。

**参数**

该属性只读，没有 setter 参数。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `str` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_sdk2_cpp.channel.ChannelSubscriber`
- 字段类型：`ChannelSubscriber::message_type_name() const`
- 声明位置：由 pybind11 手工绑定提供；manifest 未记录独立头文件行号。

**用法**

```python
current_value = obj.message_type_name
```

<a id="unitree-sdk2-cpp-channel-channelsubscriber-last-data-available-time"></a>
#### `unitree_sdk2_cpp.channel.ChannelSubscriber.last_data_available_time`

底层记录的最近一次数据可用时间。其单位和时间基准以 SDK 实现为准。

**签名**

```python
@property
def last_data_available_time(self) -> int
```

**可用性与安全性**

**`AVAILABLE` / `DDS_LIFECYCLE`**：当前绑定源码已实现。该操作可能创建、使用或释放 DDS 资源。

**参数**

该属性只读，没有 setter 参数。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `int` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_sdk2_cpp.channel.ChannelSubscriber`
- 字段类型：`ChannelSubscriber::last_data_available_time() const`
- 声明位置：由 pybind11 手工绑定提供；manifest 未记录独立头文件行号。

**用法**

```python
current_value = obj.last_data_available_time
```

---

[返回 API 总索引](../API_REFERENCE_ZH.md)
