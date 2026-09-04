# Unitree SDK2 Python API 参考分卷

[返回 API 总索引](../API_REFERENCE_ZH.md) · [阅读从零开始指南](../BEGINNER_GUIDE_ZH.md)

> [!WARNING]
> 本分卷同时包含 `AVAILABLE` 和 `SIGNATURE_ONLY`。后者只是设计期类型签名。运动及硬件副作用方法即使标记为 `AVAILABLE`，也不表示当前环境可安全执行。

> [!NOTE]
> 本文件由 `generator/generate_api_docs.py` 自动生成，请勿手工维护 API 条目。

---

<a id="unitree-sdk2-cpp-robot-b2"></a>
## B2 Robot API

模块：`unitree_sdk2_cpp.robot.b2`

### 类索引

| 类 | 公开函数签名 | 属性 |
| --- | ---: | ---: |
| [`BackVideoClient`](#unitree-sdk2-cpp-robot-b2-backvideoclient) | 3 | 0 |
| [`ConfigClient`](#unitree-sdk2-cpp-robot-b2-configclient) | 8 | 0 |
| [`ConfigDelParameter`](#unitree-sdk2-cpp-robot-b2-configdelparameter) | 3 | 0 |
| [`ConfigGetData`](#unitree-sdk2-cpp-robot-b2-configgetdata) | 3 | 0 |
| [`ConfigGetParameter`](#unitree-sdk2-cpp-robot-b2-configgetparameter) | 3 | 0 |
| [`ConfigMeta`](#unitree-sdk2-cpp-robot-b2-configmeta) | 1 | 0 |
| [`ConfigMetaData`](#unitree-sdk2-cpp-robot-b2-configmetadata) | 3 | 0 |
| [`ConfigMetaParameter`](#unitree-sdk2-cpp-robot-b2-configmetaparameter) | 3 | 0 |
| [`ConfigSetParameter`](#unitree-sdk2-cpp-robot-b2-configsetparameter) | 3 | 0 |
| [`FrontVideoClient`](#unitree-sdk2-cpp-robot-b2-frontvideoclient) | 3 | 0 |
| [`JsonizeConfigMeta`](#unitree-sdk2-cpp-robot-b2-jsonizeconfigmeta) | 3 | 0 |
| [`JsonizeModeName`](#unitree-sdk2-cpp-robot-b2-jsonizemodename) | 3 | 0 |
| [`JsonizeSilent`](#unitree-sdk2-cpp-robot-b2-jsonizesilent) | 3 | 0 |
| [`LowPowerStatusData`](#unitree-sdk2-cpp-robot-b2-lowpowerstatusdata) | 3 | 0 |
| [`LowPowerSwitchParameter`](#unitree-sdk2-cpp-robot-b2-lowpowerswitchparameter) | 3 | 0 |
| [`MotionSwitcherClient`](#unitree-sdk2-cpp-robot-b2-motionswitcherclient) | 7 | 0 |
| [`PkgVersionData`](#unitree-sdk2-cpp-robot-b2-pkgversiondata) | 3 | 0 |
| [`RobotStateClient`](#unitree-sdk2-cpp-robot-b2-robotstateclient) | 8 | 0 |
| [`ServiceState`](#unitree-sdk2-cpp-robot-b2-servicestate) | 1 | 0 |
| [`ServiceStateData`](#unitree-sdk2-cpp-robot-b2-servicestatedata) | 3 | 0 |
| [`ServiceSwitchData`](#unitree-sdk2-cpp-robot-b2-serviceswitchdata) | 3 | 0 |
| [`ServiceSwitchParameter`](#unitree-sdk2-cpp-robot-b2-serviceswitchparameter) | 3 | 0 |
| [`SetReportFreqParameter`](#unitree-sdk2-cpp-robot-b2-setreportfreqparameter) | 3 | 0 |
| [`SportClient`](#unitree-sdk2-cpp-robot-b2-sportclient) | 25 | 0 |
| [`stPathPoint`](#unitree-sdk2-cpp-robot-b2-stpathpoint) | 1 | 0 |

<a id="unitree-sdk2-cpp-robot-b2-backvideoclient"></a>
### `unitree_sdk2_cpp.robot.b2.BackVideoClient`

Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

**导入**

```python
from unitree_sdk2_cpp.robot.b2 import BackVideoClient
```

**基类**：`Client`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-b2-backvideoclient-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`init`](#unitree-sdk2-cpp-robot-b2-backvideoclient-init-1) | `def init(self) -> None` | `AVAILABLE` | `INITIALIZATION` |
| [`get_image_sample`](#unitree-sdk2-cpp-robot-b2-backvideoclient-get-image-sample-1) | `def get_image_sample(self) -> tuple[int, list[int]]` | `AVAILABLE` | `READ_ONLY` |

<a id="unitree-sdk2-cpp-robot-b2-backvideoclient-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.b2.BackVideoClient.__init__`

初始化 `BackVideoClient` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::b2::BackVideoClient`
- 签名：`BackVideoClient()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/b2/back_video/back_video_client.hpp:18`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = BackVideoClient()
```

<a id="unitree-sdk2-cpp-robot-b2-backvideoclient-init-1"></a>
#### `unitree_sdk2_cpp.robot.b2.BackVideoClient.init`

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

- 类：`unitree::robot::b2::BackVideoClient`
- 签名：`Init()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/back_video/back_video_client.hpp:21`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.init()
```

<a id="unitree-sdk2-cpp-robot-b2-backvideoclient-get-image-sample-1"></a>
#### `unitree_sdk2_cpp.robot.b2.BackVideoClient.get_image_sample`

查询或检查 图像 `sample`。

**签名**

```python
def get_image_sample(self) -> tuple[int, list[int]]
```

**可用性与安全性**

**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现只读查询。Robot Client 的服务端查询通常仍需匹配的 Linux 扩展、DDS、网络、机器人和服务；纯本地 getter 则不一定需要全部条件。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| [0] `status` | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。 |
| [1] `output_1` | `list[int]` | 传给该接口的 `output` `1` 参数，Python 类型为 `list[int]`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `output_1: std::vector<uint8_t> &`。 底层是可变长度 vector；元素约束：取值范围为 0 到 255。 |

**对应 C++**

- 类：`unitree::robot::b2::BackVideoClient`
- 签名：`GetImageSample(std::vector<uint8_t> &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/b2/back_video/back_video_client.hpp:27`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, output_1 = obj.get_image_sample()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-b2-configclient"></a>
### `unitree_sdk2_cpp.robot.b2.ConfigClient`

Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

**导入**

```python
from unitree_sdk2_cpp.robot.b2 import ConfigClient
```

**基类**：`Client`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-b2-configclient-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`init`](#unitree-sdk2-cpp-robot-b2-configclient-init-1) | `def init(self) -> None` | `AVAILABLE` | `INITIALIZATION` |
| [`set`](#unitree-sdk2-cpp-robot-b2-configclient-set-1) | `def set(self, name: str, content: str) -> int` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |
| [`get`](#unitree-sdk2-cpp-robot-b2-configclient-get-1) | `def get(self, name: str) -> tuple[int, str]` | `AVAILABLE` | `READ_ONLY` |
| [`del_`](#unitree-sdk2-cpp-robot-b2-configclient-del-1) | `def del_(self, name: str) -> int` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |
| [`meta_config_meta`](#unitree-sdk2-cpp-robot-b2-configclient-meta-config-meta-1) | `def meta_config_meta(self, name: str) -> tuple[int, ConfigMeta]` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |
| [`meta_string`](#unitree-sdk2-cpp-robot-b2-configclient-meta-string-1) | `def meta_string(self, name: str) -> tuple[int, str]` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |
| [`subscribe_change_status`](#unitree-sdk2-cpp-robot-b2-configclient-subscribe-change-status-1) | `def subscribe_change_status(self, name: str, callback: Callable[[str, str], None]) -> None` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |

<a id="unitree-sdk2-cpp-robot-b2-configclient-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ConfigClient.__init__`

初始化 `ConfigClient` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::b2::ConfigClient`
- 签名：`ConfigClient()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/b2/config/config_client.hpp:41`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = ConfigClient()
```

<a id="unitree-sdk2-cpp-robot-b2-configclient-init-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ConfigClient.init`

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

- 类：`unitree::robot::b2::ConfigClient`
- 签名：`Init()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/config/config_client.hpp:44`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.init()
```

<a id="unitree-sdk2-cpp-robot-b2-configclient-set-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ConfigClient.set`

对应 C++ SDK 操作 `Set(const std::string &, const std::string &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def set(self, name: str, content: str) -> int
```

**可用性与安全性**

**`AVAILABLE` / `HARDWARE_SIDE_EFFECT`**：当前绑定源码已实现，调用可能修改机器人或服务状态、启动订阅或产生网络副作用。必须显式检查目标设备和返回状态。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `name` | `str` | 必填 | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。 |
| `content` | `str` | 必填 | 配置、请求或序列化内容。具体格式由对应服务协议定义。 对应 C++ 参数 `content: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::b2::ConfigClient`
- 签名：`Set(const std::string &, const std::string &)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/config/config_client.hpp:46`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.set(name=name, content=content)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-configclient-get-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ConfigClient.get`

对应 C++ SDK 操作 `Get(const std::string &, std::string &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def get(self, name: str) -> tuple[int, str]
```

**可用性与安全性**

**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现只读查询。Robot Client 的服务端查询通常仍需匹配的 Linux 扩展、DDS、网络、机器人和服务；纯本地 getter 则不一定需要全部条件。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `name` | `str` | 必填 | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| [0] `status` | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。 |
| [1] `content` | `str` | 配置、请求或序列化内容。具体格式由对应服务协议定义。 对应 C++ 参数 `content: std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。 |

**对应 C++**

- 类：`unitree::robot::b2::ConfigClient`
- 签名：`Get(const std::string &, std::string &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/b2/config/config_client.hpp:47`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, content = obj.get(name=name)
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-b2-configclient-del-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ConfigClient.del_`

对应 C++ SDK 操作 `Del(const std::string &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def del_(self, name: str) -> int
```

**可用性与安全性**

**`AVAILABLE` / `HARDWARE_SIDE_EFFECT`**：当前绑定源码已实现，调用可能修改机器人或服务状态、启动订阅或产生网络副作用。必须显式检查目标设备和返回状态。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `name` | `str` | 必填 | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::b2::ConfigClient`
- 签名：`Del(const std::string &)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/config/config_client.hpp:48`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.del_(name=name)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-configclient-meta-config-meta-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ConfigClient.meta_config_meta`

对应 C++ SDK 操作 `Meta(const std::string &, unitree::robot::b2::ConfigMeta &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def meta_config_meta(self, name: str) -> tuple[int, ConfigMeta]
```

**可用性与安全性**

**`AVAILABLE` / `HARDWARE_SIDE_EFFECT`**：当前绑定源码已实现，调用可能修改机器人或服务状态、启动订阅或产生网络副作用。必须显式检查目标设备和返回状态。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `name` | `str` | 必填 | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| [0] `status` | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。 |
| [1] `meta` | `ConfigMeta` | 传给该接口的 `meta` 参数，Python 类型为 `ConfigMeta`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `meta: unitree::robot::b2::ConfigMeta &`。 |

**对应 C++**

- 类：`unitree::robot::b2::ConfigClient`
- 签名：`Meta(const std::string &, unitree::robot::b2::ConfigMeta &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/b2/config/config_client.hpp:49`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, meta = obj.meta_config_meta(name=name)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-configclient-meta-string-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ConfigClient.meta_string`

对应 C++ SDK 操作 `Meta(const std::string &, std::string &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def meta_string(self, name: str) -> tuple[int, str]
```

**可用性与安全性**

**`AVAILABLE` / `HARDWARE_SIDE_EFFECT`**：当前绑定源码已实现，调用可能修改机器人或服务状态、启动订阅或产生网络副作用。必须显式检查目标设备和返回状态。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `name` | `str` | 必填 | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| [0] `status` | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。 |
| [1] `meta` | `str` | 传给该接口的 `meta` 参数，Python 类型为 `str`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `meta: std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。 |

**对应 C++**

- 类：`unitree::robot::b2::ConfigClient`
- 签名：`Meta(const std::string &, std::string &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/b2/config/config_client.hpp:50`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, meta = obj.meta_string(name=name)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-configclient-subscribe-change-status-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ConfigClient.subscribe_change_status`

对应 C++ SDK 操作 `SubscribeChangeStatus(const std::string &, const unitree::robot::b2::ConfigChangeStatusCallback &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def subscribe_change_status(self, name: str, callback: Callable[[str, str], None]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `HARDWARE_SIDE_EFFECT`**：当前绑定源码已实现，调用可能修改机器人或服务状态、启动订阅或产生网络副作用。必须显式检查目标设备和返回状态。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `name` | `str` | 必填 | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。 |
| `callback` | `Callable[[str, str], None]` | 必填 | 收到数据或状态变化时调用的 Python 回调。回调签名必须与类型提示一致，并应快速返回。 对应 C++ 参数 `callback: const unitree::robot::b2::ConfigChangeStatusCallback &`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree::robot::b2::ConfigClient`
- 签名：`SubscribeChangeStatus(const std::string &, const unitree::robot::b2::ConfigChangeStatusCallback &)`
- 绑定策略：`CALLBACK_MANUAL`
- 声明位置：`include/unitree/robot/b2/config/config_client.hpp:52`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 回调可能由 SDK 工作线程触发；回调应快速返回、捕获异常，并通过线程安全队列移交耗时工作。

**用法**

```python
obj.subscribe_change_status(name=name, callback=callback)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-configdelparameter"></a>
### `unitree_sdk2_cpp.robot.b2.ConfigDelParameter`

SDK 请求参数值类型；当前可能仅提供设计期签名。

**导入**

```python
from unitree_sdk2_cpp.robot.b2 import ConfigDelParameter
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `name` | `str` | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 | `value = obj.name` / `obj.name = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-b2-configdelparameter-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-b2-configdelparameter-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-b2-configdelparameter-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-b2-configdelparameter-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ConfigDelParameter.__init__`

初始化 `ConfigDelParameter` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::b2::ConfigDelParameter`
- 签名：`ConfigDelParameter()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/b2/config/config_api.hpp:140`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = ConfigDelParameter()
```

<a id="unitree-sdk2-cpp-robot-b2-configdelparameter-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ConfigDelParameter.from_json`

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

- 类：`unitree::robot::b2::ConfigDelParameter`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/b2/config/config_api.hpp:146`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-b2-configdelparameter-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ConfigDelParameter.to_json`

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

- 类：`unitree::robot::b2::ConfigDelParameter`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/b2/config/config_api.hpp:151`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-b2-configgetdata"></a>
### `unitree_sdk2_cpp.robot.b2.ConfigGetData`

SDK 数据值类型；公开字段和转换方法见下文。

**导入**

```python
from unitree_sdk2_cpp.robot.b2 import ConfigGetData
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `content` | `str` | 配置、请求或序列化内容。具体格式由对应服务协议定义。 | `value = obj.content` / `obj.content = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-b2-configgetdata-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-b2-configgetdata-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-b2-configgetdata-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-b2-configgetdata-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ConfigGetData.__init__`

初始化 `ConfigGetData` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::b2::ConfigGetData`
- 签名：`ConfigGetData()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/b2/config/config_api.hpp:117`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = ConfigGetData()
```

<a id="unitree-sdk2-cpp-robot-b2-configgetdata-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ConfigGetData.from_json`

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

- 类：`unitree::robot::b2::ConfigGetData`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/b2/config/config_api.hpp:123`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-b2-configgetdata-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ConfigGetData.to_json`

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

- 类：`unitree::robot::b2::ConfigGetData`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/b2/config/config_api.hpp:128`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-b2-configgetparameter"></a>
### `unitree_sdk2_cpp.robot.b2.ConfigGetParameter`

SDK 请求参数值类型；当前可能仅提供设计期签名。

**导入**

```python
from unitree_sdk2_cpp.robot.b2 import ConfigGetParameter
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `name` | `str` | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 | `value = obj.name` / `obj.name = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-b2-configgetparameter-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-b2-configgetparameter-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-b2-configgetparameter-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-b2-configgetparameter-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ConfigGetParameter.__init__`

初始化 `ConfigGetParameter` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::b2::ConfigGetParameter`
- 签名：`ConfigGetParameter()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/b2/config/config_api.hpp:94`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = ConfigGetParameter()
```

<a id="unitree-sdk2-cpp-robot-b2-configgetparameter-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ConfigGetParameter.from_json`

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

- 类：`unitree::robot::b2::ConfigGetParameter`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/b2/config/config_api.hpp:100`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-b2-configgetparameter-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ConfigGetParameter.to_json`

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

- 类：`unitree::robot::b2::ConfigGetParameter`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/b2/config/config_api.hpp:105`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-b2-configmeta"></a>
### `unitree_sdk2_cpp.robot.b2.ConfigMeta`

SDK 数据值类型；公开字段和转换方法见下文。

**导入**

```python
from unitree_sdk2_cpp.robot.b2 import ConfigMeta
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `name` | `str` | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 | `value = obj.name` / `obj.name = value` |
| `last_modified` | `str` | 传给该接口的 `last` `modified` 参数，Python 类型为 `str`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.last_modified` / `obj.last_modified = value` |
| `size` | `int` | 传给该接口的 `size` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.size` / `obj.size = value` |
| `epoch` | `int` | 传给该接口的 `epoch` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.epoch` / `obj.epoch = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-b2-configmeta-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |

<a id="unitree-sdk2-cpp-robot-b2-configmeta-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ConfigMeta.__init__`

初始化 `ConfigMeta` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::b2::ConfigMeta`
- 签名：`ConfigMeta()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/b2/config/config_client.hpp:20`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = ConfigMeta()
```

<a id="unitree-sdk2-cpp-robot-b2-configmetadata"></a>
### `unitree_sdk2_cpp.robot.b2.ConfigMetaData`

SDK 数据值类型；公开字段和转换方法见下文。

**导入**

```python
from unitree_sdk2_cpp.robot.b2 import ConfigMetaData
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `meta` | `JsonizeConfigMeta` | 传给该接口的 `meta` 参数，Python 类型为 `JsonizeConfigMeta`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.meta` / `obj.meta = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-b2-configmetadata-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-b2-configmetadata-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-b2-configmetadata-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-b2-configmetadata-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ConfigMetaData.__init__`

初始化 `ConfigMetaData` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::b2::ConfigMetaData`
- 签名：`ConfigMetaData()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/b2/config/config_api.hpp:186`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = ConfigMetaData()
```

<a id="unitree-sdk2-cpp-robot-b2-configmetadata-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ConfigMetaData.from_json`

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

- 类：`unitree::robot::b2::ConfigMetaData`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/b2/config/config_api.hpp:192`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-b2-configmetadata-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ConfigMetaData.to_json`

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

- 类：`unitree::robot::b2::ConfigMetaData`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/b2/config/config_api.hpp:197`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-b2-configmetaparameter"></a>
### `unitree_sdk2_cpp.robot.b2.ConfigMetaParameter`

SDK 请求参数值类型；当前可能仅提供设计期签名。

**导入**

```python
from unitree_sdk2_cpp.robot.b2 import ConfigMetaParameter
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `name` | `str` | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 | `value = obj.name` / `obj.name = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-b2-configmetaparameter-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-b2-configmetaparameter-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-b2-configmetaparameter-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-b2-configmetaparameter-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ConfigMetaParameter.__init__`

初始化 `ConfigMetaParameter` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::b2::ConfigMetaParameter`
- 签名：`ConfigMetaParameter()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/b2/config/config_api.hpp:163`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = ConfigMetaParameter()
```

<a id="unitree-sdk2-cpp-robot-b2-configmetaparameter-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ConfigMetaParameter.from_json`

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

- 类：`unitree::robot::b2::ConfigMetaParameter`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/b2/config/config_api.hpp:169`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-b2-configmetaparameter-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ConfigMetaParameter.to_json`

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

- 类：`unitree::robot::b2::ConfigMetaParameter`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/b2/config/config_api.hpp:174`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-b2-configsetparameter"></a>
### `unitree_sdk2_cpp.robot.b2.ConfigSetParameter`

SDK 请求参数值类型；当前可能仅提供设计期签名。

**导入**

```python
from unitree_sdk2_cpp.robot.b2 import ConfigSetParameter
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `name` | `str` | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 | `value = obj.name` / `obj.name = value` |
| `content` | `str` | 配置、请求或序列化内容。具体格式由对应服务协议定义。 | `value = obj.content` / `obj.content = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-b2-configsetparameter-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-b2-configsetparameter-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-b2-configsetparameter-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-b2-configsetparameter-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ConfigSetParameter.__init__`

初始化 `ConfigSetParameter` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::b2::ConfigSetParameter`
- 签名：`ConfigSetParameter()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/b2/config/config_api.hpp:68`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = ConfigSetParameter()
```

<a id="unitree-sdk2-cpp-robot-b2-configsetparameter-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ConfigSetParameter.from_json`

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

- 类：`unitree::robot::b2::ConfigSetParameter`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/b2/config/config_api.hpp:74`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-b2-configsetparameter-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ConfigSetParameter.to_json`

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

- 类：`unitree::robot::b2::ConfigSetParameter`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/b2/config/config_api.hpp:80`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-b2-frontvideoclient"></a>
### `unitree_sdk2_cpp.robot.b2.FrontVideoClient`

Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

**导入**

```python
from unitree_sdk2_cpp.robot.b2 import FrontVideoClient
```

**基类**：`Client`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-b2-frontvideoclient-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`init`](#unitree-sdk2-cpp-robot-b2-frontvideoclient-init-1) | `def init(self) -> None` | `AVAILABLE` | `INITIALIZATION` |
| [`get_image_sample`](#unitree-sdk2-cpp-robot-b2-frontvideoclient-get-image-sample-1) | `def get_image_sample(self) -> tuple[int, list[int]]` | `AVAILABLE` | `READ_ONLY` |

<a id="unitree-sdk2-cpp-robot-b2-frontvideoclient-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.b2.FrontVideoClient.__init__`

初始化 `FrontVideoClient` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::b2::FrontVideoClient`
- 签名：`FrontVideoClient()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/b2/front_video/front_video_client.hpp:18`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = FrontVideoClient()
```

<a id="unitree-sdk2-cpp-robot-b2-frontvideoclient-init-1"></a>
#### `unitree_sdk2_cpp.robot.b2.FrontVideoClient.init`

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

- 类：`unitree::robot::b2::FrontVideoClient`
- 签名：`Init()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/front_video/front_video_client.hpp:21`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.init()
```

<a id="unitree-sdk2-cpp-robot-b2-frontvideoclient-get-image-sample-1"></a>
#### `unitree_sdk2_cpp.robot.b2.FrontVideoClient.get_image_sample`

查询或检查 图像 `sample`。

**签名**

```python
def get_image_sample(self) -> tuple[int, list[int]]
```

**可用性与安全性**

**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现只读查询。Robot Client 的服务端查询通常仍需匹配的 Linux 扩展、DDS、网络、机器人和服务；纯本地 getter 则不一定需要全部条件。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| [0] `status` | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。 |
| [1] `output_1` | `list[int]` | 传给该接口的 `output` `1` 参数，Python 类型为 `list[int]`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `output_1: std::vector<uint8_t> &`。 底层是可变长度 vector；元素约束：取值范围为 0 到 255。 |

**对应 C++**

- 类：`unitree::robot::b2::FrontVideoClient`
- 签名：`GetImageSample(std::vector<uint8_t> &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/b2/front_video/front_video_client.hpp:27`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, output_1 = obj.get_image_sample()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-b2-jsonizeconfigmeta"></a>
### `unitree_sdk2_cpp.robot.b2.JsonizeConfigMeta`

SDK 数据值类型；公开字段和转换方法见下文。

**导入**

```python
from unitree_sdk2_cpp.robot.b2 import JsonizeConfigMeta
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `name` | `str` | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 | `value = obj.name` / `obj.name = value` |
| `last_modified` | `str` | 传给该接口的 `last` `modified` 参数，Python 类型为 `str`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.last_modified` / `obj.last_modified = value` |
| `size` | `int` | 传给该接口的 `size` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.size` / `obj.size = value` |
| `epoch` | `int` | 传给该接口的 `epoch` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.epoch` / `obj.epoch = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-b2-jsonizeconfigmeta-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-b2-jsonizeconfigmeta-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-b2-jsonizeconfigmeta-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-b2-jsonizeconfigmeta-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.b2.JsonizeConfigMeta.__init__`

初始化 `JsonizeConfigMeta` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::b2::JsonizeConfigMeta`
- 签名：`JsonizeConfigMeta()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/b2/config/config_api.hpp:36`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = JsonizeConfigMeta()
```

<a id="unitree-sdk2-cpp-robot-b2-jsonizeconfigmeta-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.b2.JsonizeConfigMeta.from_json`

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

- 类：`unitree::robot::b2::JsonizeConfigMeta`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/b2/config/config_api.hpp:42`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-b2-jsonizeconfigmeta-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.b2.JsonizeConfigMeta.to_json`

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

- 类：`unitree::robot::b2::JsonizeConfigMeta`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/b2/config/config_api.hpp:50`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-b2-jsonizemodename"></a>
### `unitree_sdk2_cpp.robot.b2.JsonizeModeName`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot.b2 import JsonizeModeName
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `name` | `str` | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 | `value = obj.name` / `obj.name = value` |
| `form` | `str` | 传给该接口的 `form` 参数，Python 类型为 `str`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.form` / `obj.form = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-b2-jsonizemodename-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-b2-jsonizemodename-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-b2-jsonizemodename-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-b2-jsonizemodename-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.b2.JsonizeModeName.__init__`

初始化 `JsonizeModeName` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::b2::JsonizeModeName`
- 签名：`JsonizeModeName()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/b2/motion_switcher/motion_switcher_api.hpp:37`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = JsonizeModeName()
```

<a id="unitree-sdk2-cpp-robot-b2-jsonizemodename-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.b2.JsonizeModeName.from_json`

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

- 类：`unitree::robot::b2::JsonizeModeName`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/b2/motion_switcher/motion_switcher_api.hpp:44`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-b2-jsonizemodename-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.b2.JsonizeModeName.to_json`

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

- 类：`unitree::robot::b2::JsonizeModeName`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/b2/motion_switcher/motion_switcher_api.hpp:55`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-b2-jsonizesilent"></a>
### `unitree_sdk2_cpp.robot.b2.JsonizeSilent`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot.b2 import JsonizeSilent
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `silent` | `bool` | 传给该接口的 静音状态 参数，Python 类型为 `bool`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.silent` / `obj.silent = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-b2-jsonizesilent-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-b2-jsonizesilent-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-b2-jsonizesilent-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-b2-jsonizesilent-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.b2.JsonizeSilent.__init__`

初始化 `JsonizeSilent` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::b2::JsonizeSilent`
- 签名：`JsonizeSilent()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/b2/motion_switcher/motion_switcher_api.hpp:73`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = JsonizeSilent()
```

<a id="unitree-sdk2-cpp-robot-b2-jsonizesilent-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.b2.JsonizeSilent.from_json`

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

- 类：`unitree::robot::b2::JsonizeSilent`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/b2/motion_switcher/motion_switcher_api.hpp:80`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-b2-jsonizesilent-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.b2.JsonizeSilent.to_json`

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

- 类：`unitree::robot::b2::JsonizeSilent`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/b2/motion_switcher/motion_switcher_api.hpp:86`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-b2-lowpowerstatusdata"></a>
### `unitree_sdk2_cpp.robot.b2.LowPowerStatusData`

SDK 数据值类型；公开字段和转换方法见下文。

**导入**

```python
from unitree_sdk2_cpp.robot.b2 import LowPowerStatusData
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `status` | `int` | 传给该接口的 状态 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.status` / `obj.status = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-b2-lowpowerstatusdata-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-b2-lowpowerstatusdata-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-b2-lowpowerstatusdata-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-b2-lowpowerstatusdata-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.b2.LowPowerStatusData.__init__`

初始化 `LowPowerStatusData` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::b2::LowPowerStatusData`
- 签名：`LowPowerStatusData()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/b2/robot_state/robot_state_api.hpp:183`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = LowPowerStatusData()
```

<a id="unitree-sdk2-cpp-robot-b2-lowpowerstatusdata-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.b2.LowPowerStatusData.from_json`

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

- 类：`unitree::robot::b2::LowPowerStatusData`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/b2/robot_state/robot_state_api.hpp:189`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-b2-lowpowerstatusdata-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.b2.LowPowerStatusData.to_json`

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

- 类：`unitree::robot::b2::LowPowerStatusData`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/b2/robot_state/robot_state_api.hpp:194`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-b2-lowpowerswitchparameter"></a>
### `unitree_sdk2_cpp.robot.b2.LowPowerSwitchParameter`

SDK 请求参数值类型；当前可能仅提供设计期签名。

**导入**

```python
from unitree_sdk2_cpp.robot.b2 import LowPowerSwitchParameter
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `swit` | `int` | 传给该接口的 `swit` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.swit` / `obj.swit = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-b2-lowpowerswitchparameter-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-b2-lowpowerswitchparameter-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-b2-lowpowerswitchparameter-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-b2-lowpowerswitchparameter-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.b2.LowPowerSwitchParameter.__init__`

初始化 `LowPowerSwitchParameter` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::b2::LowPowerSwitchParameter`
- 签名：`LowPowerSwitchParameter()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/b2/robot_state/robot_state_api.hpp:157`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = LowPowerSwitchParameter()
```

<a id="unitree-sdk2-cpp-robot-b2-lowpowerswitchparameter-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.b2.LowPowerSwitchParameter.from_json`

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

- 类：`unitree::robot::b2::LowPowerSwitchParameter`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/b2/robot_state/robot_state_api.hpp:163`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-b2-lowpowerswitchparameter-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.b2.LowPowerSwitchParameter.to_json`

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

- 类：`unitree::robot::b2::LowPowerSwitchParameter`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/b2/robot_state/robot_state_api.hpp:168`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-b2-motionswitcherclient"></a>
### `unitree_sdk2_cpp.robot.b2.MotionSwitcherClient`

Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

**导入**

```python
from unitree_sdk2_cpp.robot.b2 import MotionSwitcherClient
```

**基类**：`Client`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-b2-motionswitcherclient-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`init`](#unitree-sdk2-cpp-robot-b2-motionswitcherclient-init-1) | `def init(self) -> None` | `AVAILABLE` | `INITIALIZATION` |
| [`check_mode`](#unitree-sdk2-cpp-robot-b2-motionswitcherclient-check-mode-1) | `def check_mode(self) -> tuple[int, str, str]` | `AVAILABLE` | `READ_ONLY` |
| [`select_mode`](#unitree-sdk2-cpp-robot-b2-motionswitcherclient-select-mode-1) | `def select_mode(self, name_or_alias: str) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`release_mode`](#unitree-sdk2-cpp-robot-b2-motionswitcherclient-release-mode-1) | `def release_mode(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`set_silent`](#unitree-sdk2-cpp-robot-b2-motionswitcherclient-set-silent-1) | `def set_silent(self, silent: bool) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`get_silent`](#unitree-sdk2-cpp-robot-b2-motionswitcherclient-get-silent-1) | `def get_silent(self) -> tuple[int, bool]` | `AVAILABLE` | `READ_ONLY` |

<a id="unitree-sdk2-cpp-robot-b2-motionswitcherclient-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.b2.MotionSwitcherClient.__init__`

初始化 `MotionSwitcherClient` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::b2::MotionSwitcherClient`
- 签名：`MotionSwitcherClient()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/b2/motion_switcher/motion_switcher_client.hpp:18`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = MotionSwitcherClient()
```

<a id="unitree-sdk2-cpp-robot-b2-motionswitcherclient-init-1"></a>
#### `unitree_sdk2_cpp.robot.b2.MotionSwitcherClient.init`

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

- 类：`unitree::robot::b2::MotionSwitcherClient`
- 签名：`Init()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/motion_switcher/motion_switcher_client.hpp:21`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.init()
```

<a id="unitree-sdk2-cpp-robot-b2-motionswitcherclient-check-mode-1"></a>
#### `unitree_sdk2_cpp.robot.b2.MotionSwitcherClient.check_mode`

查询或检查 模式。

**签名**

```python
def check_mode(self) -> tuple[int, str, str]
```

**可用性与安全性**

**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现只读查询。Robot Client 的服务端查询通常仍需匹配的 Linux 扩展、DDS、网络、机器人和服务；纯本地 getter 则不一定需要全部条件。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| [0] `status` | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。 |
| [1] `form` | `str` | 传给该接口的 `form` 参数，Python 类型为 `str`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `form: std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。 |
| [2] `name` | `str` | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。 |

**对应 C++**

- 类：`unitree::robot::b2::MotionSwitcherClient`
- 签名：`CheckMode(std::string &, std::string &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/b2/motion_switcher/motion_switcher_client.hpp:23`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, form, name = obj.check_mode()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-b2-motionswitcherclient-select-mode-1"></a>
#### `unitree_sdk2_cpp.robot.b2.MotionSwitcherClient.select_mode`

对应 C++ SDK 操作 `SelectMode(const std::string &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def select_mode(self, name_or_alias: str) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `name_or_alias` | `str` | 必填 | 传给该接口的 名称 `or` `alias` 参数，Python 类型为 `str`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `nameOrAlias: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::b2::MotionSwitcherClient`
- 签名：`SelectMode(const std::string &)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/motion_switcher/motion_switcher_client.hpp:24`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.select_mode(name_or_alias=name_or_alias)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-motionswitcherclient-release-mode-1"></a>
#### `unitree_sdk2_cpp.robot.b2.MotionSwitcherClient.release_mode`

对应 C++ SDK 操作 `ReleaseMode()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def release_mode(self) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::b2::MotionSwitcherClient`
- 签名：`ReleaseMode()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/motion_switcher/motion_switcher_client.hpp:25`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.release_mode()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-motionswitcherclient-set-silent-1"></a>
#### `unitree_sdk2_cpp.robot.b2.MotionSwitcherClient.set_silent`

设置 静音状态。具体副作用和安全边界见下方状态。

**签名**

```python
def set_silent(self, silent: bool) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `silent` | `bool` | 必填 | 传给该接口的 静音状态 参数，Python 类型为 `bool`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `silent: bool`。 只接受布尔语义。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::b2::MotionSwitcherClient`
- 签名：`SetSilent(bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/motion_switcher/motion_switcher_client.hpp:26`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.set_silent(silent=silent)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-motionswitcherclient-get-silent-1"></a>
#### `unitree_sdk2_cpp.robot.b2.MotionSwitcherClient.get_silent`

查询或检查 静音状态。

**签名**

```python
def get_silent(self) -> tuple[int, bool]
```

**可用性与安全性**

**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现只读查询。Robot Client 的服务端查询通常仍需匹配的 Linux 扩展、DDS、网络、机器人和服务；纯本地 getter 则不一定需要全部条件。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| [0] `status` | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。 |
| [1] `silent` | `bool` | 传给该接口的 静音状态 参数，Python 类型为 `bool`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `silent: bool &`。 只接受布尔语义。 |

**对应 C++**

- 类：`unitree::robot::b2::MotionSwitcherClient`
- 签名：`GetSilent(bool &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/b2/motion_switcher/motion_switcher_client.hpp:27`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, silent = obj.get_silent()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-b2-pkgversiondata"></a>
### `unitree_sdk2_cpp.robot.b2.PkgVersionData`

SDK 数据值类型；公开字段和转换方法见下文。

**导入**

```python
from unitree_sdk2_cpp.robot.b2 import PkgVersionData
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `package_version` | `str` | 传给该接口的 `package` `version` 参数，Python 类型为 `str`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.package_version` / `obj.package_version = value` |
| `module_version_map` | `dict[str, str]` | 传给该接口的 `module` `version` `map` 参数，Python 类型为 `dict[str, str]`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.module_version_map` / `obj.module_version_map = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-b2-pkgversiondata-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-b2-pkgversiondata-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-b2-pkgversiondata-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-b2-pkgversiondata-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.b2.PkgVersionData.__init__`

初始化 `PkgVersionData` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::b2::PkgVersionData`
- 签名：`PkgVersionData()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/b2/robot_state/robot_state_api.hpp:209`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = PkgVersionData()
```

<a id="unitree-sdk2-cpp-robot-b2-pkgversiondata-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.b2.PkgVersionData.from_json`

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

- 类：`unitree::robot::b2::PkgVersionData`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/b2/robot_state/robot_state_api.hpp:215`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-b2-pkgversiondata-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.b2.PkgVersionData.to_json`

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

- 类：`unitree::robot::b2::PkgVersionData`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/b2/robot_state/robot_state_api.hpp:221`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-b2-robotstateclient"></a>
### `unitree_sdk2_cpp.robot.b2.RobotStateClient`

Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

**导入**

```python
from unitree_sdk2_cpp.robot.b2 import RobotStateClient
```

**基类**：`Client`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-b2-robotstateclient-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`init`](#unitree-sdk2-cpp-robot-b2-robotstateclient-init-1) | `def init(self) -> None` | `AVAILABLE` | `INITIALIZATION` |
| [`service_list`](#unitree-sdk2-cpp-robot-b2-robotstateclient-service-list-1) | `def service_list(self) -> tuple[int, list[ServiceState]]` | `AVAILABLE` | `READ_ONLY` |
| [`service_switch`](#unitree-sdk2-cpp-robot-b2-robotstateclient-service-switch-1) | `def service_switch(self, name: str, swit: int) -> tuple[int, int]` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |
| [`set_report_freq`](#unitree-sdk2-cpp-robot-b2-robotstateclient-set-report-freq-1) | `def set_report_freq(self, interval: int, duration: int) -> int` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |
| [`low_power_switch`](#unitree-sdk2-cpp-robot-b2-robotstateclient-low-power-switch-1) | `def low_power_switch(self, swit: int) -> int` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |
| [`low_power_status`](#unitree-sdk2-cpp-robot-b2-robotstateclient-low-power-status-1) | `def low_power_status(self) -> tuple[int, int]` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |
| [`get_pkg_version`](#unitree-sdk2-cpp-robot-b2-robotstateclient-get-pkg-version-1) | `def get_pkg_version(self) -> tuple[int, str, dict[str, str]]` | `AVAILABLE` | `READ_ONLY` |

<a id="unitree-sdk2-cpp-robot-b2-robotstateclient-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.b2.RobotStateClient.__init__`

初始化 `RobotStateClient` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::b2::RobotStateClient`
- 签名：`RobotStateClient()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/b2/robot_state/robot_state_client.hpp:32`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = RobotStateClient()
```

<a id="unitree-sdk2-cpp-robot-b2-robotstateclient-init-1"></a>
#### `unitree_sdk2_cpp.robot.b2.RobotStateClient.init`

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

- 类：`unitree::robot::b2::RobotStateClient`
- 签名：`Init()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/robot_state/robot_state_client.hpp:35`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.init()
```

<a id="unitree-sdk2-cpp-robot-b2-robotstateclient-service-list-1"></a>
#### `unitree_sdk2_cpp.robot.b2.RobotStateClient.service_list`

对应 C++ SDK 操作 `ServiceList(std::vector<ServiceState> &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def service_list(self) -> tuple[int, list[ServiceState]]
```

**可用性与安全性**

**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现只读查询。Robot Client 的服务端查询通常仍需匹配的 Linux 扩展、DDS、网络、机器人和服务；纯本地 getter 则不一定需要全部条件。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| [0] `status` | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。 |
| [1] `serviceStateList` | `list[ServiceState]` | 传给该接口的 `serviceStateList` 参数，Python 类型为 `list[ServiceState]`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `serviceStateList: std::vector<ServiceState> &`。 底层是可变长度 vector |

**对应 C++**

- 类：`unitree::robot::b2::RobotStateClient`
- 签名：`ServiceList(std::vector<ServiceState> &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/b2/robot_state/robot_state_client.hpp:37`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, serviceStateList = obj.service_list()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-b2-robotstateclient-service-switch-1"></a>
#### `unitree_sdk2_cpp.robot.b2.RobotStateClient.service_switch`

对应 C++ SDK 操作 `ServiceSwitch(const std::string &, int32_t, int32_t &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def service_switch(self, name: str, swit: int) -> tuple[int, int]
```

**可用性与安全性**

**`AVAILABLE` / `HARDWARE_SIDE_EFFECT`**：当前绑定源码已实现，调用可能修改机器人或服务状态、启动订阅或产生网络副作用。必须显式检查目标设备和返回状态。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `name` | `str` | 必填 | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 对应 C++ 参数 `name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。 |
| `swit` | `int` | 必填 | 传给该接口的 `swit` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `swit: int32_t`。 取值范围为 -2147483648 到 2147483647。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| [0] `status` | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。 |
| [1] `status` | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。 |

**对应 C++**

- 类：`unitree::robot::b2::RobotStateClient`
- 签名：`ServiceSwitch(const std::string &, int32_t, int32_t &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/b2/robot_state/robot_state_client.hpp:38`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, status = obj.service_switch(name=name, swit=swit)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-robotstateclient-set-report-freq-1"></a>
#### `unitree_sdk2_cpp.robot.b2.RobotStateClient.set_report_freq`

设置 `report` `freq`。具体副作用和安全边界见下方状态。

**签名**

```python
def set_report_freq(self, interval: int, duration: int) -> int
```

**可用性与安全性**

**`AVAILABLE` / `HARDWARE_SIDE_EFFECT`**：当前绑定源码已实现，调用可能修改机器人或服务状态、启动订阅或产生网络副作用。必须显式检查目标设备和返回状态。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `interval` | `int` | 必填 | 传给该接口的 `interval` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `interval: int32_t`。 取值范围为 -2147483648 到 2147483647。 |
| `duration` | `int` | 必填 | 操作持续时间参数。精确单位、范围和默认行为以目标型号接口定义为准。 对应 C++ 参数 `duration: int32_t`。 取值范围为 -2147483648 到 2147483647。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::b2::RobotStateClient`
- 签名：`SetReportFreq(int32_t, int32_t)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/robot_state/robot_state_client.hpp:39`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.set_report_freq(interval=interval, duration=duration)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-robotstateclient-low-power-switch-1"></a>
#### `unitree_sdk2_cpp.robot.b2.RobotStateClient.low_power_switch`

对应 C++ SDK 操作 `LowPowerSwitch(int32_t)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def low_power_switch(self, swit: int) -> int
```

**可用性与安全性**

**`AVAILABLE` / `HARDWARE_SIDE_EFFECT`**：当前绑定源码已实现，调用可能修改机器人或服务状态、启动订阅或产生网络副作用。必须显式检查目标设备和返回状态。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `swit` | `int` | 必填 | 传给该接口的 `swit` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `swit: int32_t`。 取值范围为 -2147483648 到 2147483647。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::b2::RobotStateClient`
- 签名：`LowPowerSwitch(int32_t)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/robot_state/robot_state_client.hpp:40`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.low_power_switch(swit=swit)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-robotstateclient-low-power-status-1"></a>
#### `unitree_sdk2_cpp.robot.b2.RobotStateClient.low_power_status`

对应 C++ SDK 操作 `LowPowerStatus(int32_t &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def low_power_status(self) -> tuple[int, int]
```

**可用性与安全性**

**`AVAILABLE` / `HARDWARE_SIDE_EFFECT`**：当前绑定源码已实现，调用可能修改机器人或服务状态、启动订阅或产生网络副作用。必须显式检查目标设备和返回状态。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| [0] `status` | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。 |
| [1] `status` | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。 |

**对应 C++**

- 类：`unitree::robot::b2::RobotStateClient`
- 签名：`LowPowerStatus(int32_t &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/b2/robot_state/robot_state_client.hpp:41`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, status = obj.low_power_status()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-robotstateclient-get-pkg-version-1"></a>
#### `unitree_sdk2_cpp.robot.b2.RobotStateClient.get_pkg_version`

查询或检查 `pkg` `version`。

**签名**

```python
def get_pkg_version(self) -> tuple[int, str, dict[str, str]]
```

**可用性与安全性**

**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现只读查询。Robot Client 的服务端查询通常仍需匹配的 Linux 扩展、DDS、网络、机器人和服务；纯本地 getter 则不一定需要全部条件。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| [0] `status` | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。 |
| [1] `packageVersion` | `str` | 传给该接口的 `packageVersion` 参数，Python 类型为 `str`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `packageVersion: std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。 |
| [2] `moduleVersionMap` | `dict[str, str]` | 传给该接口的 `moduleVersionMap` 参数，Python 类型为 `dict[str, str]`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `moduleVersionMap: std::map<std::string, std::string> &`。 |

**对应 C++**

- 类：`unitree::robot::b2::RobotStateClient`
- 签名：`GetPkgVersion(std::string &, std::map<std::string, std::string> &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/b2/robot_state/robot_state_client.hpp:42`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, packageVersion, moduleVersionMap = obj.get_pkg_version()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-b2-servicestate"></a>
### `unitree_sdk2_cpp.robot.b2.ServiceState`

SDK 数据值类型；公开字段和转换方法见下文。

**导入**

```python
from unitree_sdk2_cpp.robot.b2 import ServiceState
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `name` | `str` | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 | `value = obj.name` / `obj.name = value` |
| `status` | `int` | 传给该接口的 状态 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.status` / `obj.status = value` |
| `protect` | `int` | 传给该接口的 `protect` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.protect` / `obj.protect = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-b2-servicestate-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |

<a id="unitree-sdk2-cpp-robot-b2-servicestate-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ServiceState.__init__`

初始化 `ServiceState` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::b2::ServiceState`
- 签名：`ServiceState()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/b2/robot_state/robot_state_client.hpp:18`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = ServiceState()
```

<a id="unitree-sdk2-cpp-robot-b2-servicestatedata"></a>
### `unitree_sdk2_cpp.robot.b2.ServiceStateData`

SDK 数据值类型；公开字段和转换方法见下文。

**导入**

```python
from unitree_sdk2_cpp.robot.b2 import ServiceStateData
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `name` | `str` | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 | `value = obj.name` / `obj.name = value` |
| `status` | `int` | 传给该接口的 状态 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.status` / `obj.status = value` |
| `protect` | `int` | 传给该接口的 `protect` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.protect` / `obj.protect = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-b2-servicestatedata-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-b2-servicestatedata-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-b2-servicestatedata-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-b2-servicestatedata-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ServiceStateData.__init__`

初始化 `ServiceStateData` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::b2::ServiceStateData`
- 签名：`ServiceStateData()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/b2/robot_state/robot_state_api.hpp:125`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = ServiceStateData()
```

<a id="unitree-sdk2-cpp-robot-b2-servicestatedata-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ServiceStateData.from_json`

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

- 类：`unitree::robot::b2::ServiceStateData`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/b2/robot_state/robot_state_api.hpp:131`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-b2-servicestatedata-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ServiceStateData.to_json`

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

- 类：`unitree::robot::b2::ServiceStateData`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/b2/robot_state/robot_state_api.hpp:138`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-b2-serviceswitchdata"></a>
### `unitree_sdk2_cpp.robot.b2.ServiceSwitchData`

SDK 数据值类型；公开字段和转换方法见下文。

**导入**

```python
from unitree_sdk2_cpp.robot.b2 import ServiceSwitchData
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `name` | `str` | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 | `value = obj.name` / `obj.name = value` |
| `status` | `int` | 传给该接口的 状态 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.status` / `obj.status = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-b2-serviceswitchdata-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-b2-serviceswitchdata-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-b2-serviceswitchdata-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-b2-serviceswitchdata-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ServiceSwitchData.__init__`

初始化 `ServiceSwitchData` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::b2::ServiceSwitchData`
- 签名：`ServiceSwitchData()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/b2/robot_state/robot_state_api.hpp:67`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = ServiceSwitchData()
```

<a id="unitree-sdk2-cpp-robot-b2-serviceswitchdata-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ServiceSwitchData.from_json`

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

- 类：`unitree::robot::b2::ServiceSwitchData`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/b2/robot_state/robot_state_api.hpp:73`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-b2-serviceswitchdata-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ServiceSwitchData.to_json`

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

- 类：`unitree::robot::b2::ServiceSwitchData`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/b2/robot_state/robot_state_api.hpp:79`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-b2-serviceswitchparameter"></a>
### `unitree_sdk2_cpp.robot.b2.ServiceSwitchParameter`

SDK 请求参数值类型；当前可能仅提供设计期签名。

**导入**

```python
from unitree_sdk2_cpp.robot.b2 import ServiceSwitchParameter
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `name` | `str` | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 | `value = obj.name` / `obj.name = value` |
| `swit` | `int` | 传给该接口的 `swit` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.swit` / `obj.swit = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-b2-serviceswitchparameter-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-b2-serviceswitchparameter-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-b2-serviceswitchparameter-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-b2-serviceswitchparameter-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ServiceSwitchParameter.__init__`

初始化 `ServiceSwitchParameter` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::b2::ServiceSwitchParameter`
- 签名：`ServiceSwitchParameter()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/b2/robot_state/robot_state_api.hpp:38`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = ServiceSwitchParameter()
```

<a id="unitree-sdk2-cpp-robot-b2-serviceswitchparameter-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ServiceSwitchParameter.from_json`

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

- 类：`unitree::robot::b2::ServiceSwitchParameter`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/b2/robot_state/robot_state_api.hpp:44`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-b2-serviceswitchparameter-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.b2.ServiceSwitchParameter.to_json`

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

- 类：`unitree::robot::b2::ServiceSwitchParameter`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/b2/robot_state/robot_state_api.hpp:50`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-b2-setreportfreqparameter"></a>
### `unitree_sdk2_cpp.robot.b2.SetReportFreqParameter`

SDK 请求参数值类型；当前可能仅提供设计期签名。

**导入**

```python
from unitree_sdk2_cpp.robot.b2 import SetReportFreqParameter
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `interval` | `int` | 传给该接口的 `interval` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.interval` / `obj.interval = value` |
| `duration` | `int` | 操作持续时间参数。精确单位、范围和默认行为以目标型号接口定义为准。 | `value = obj.duration` / `obj.duration = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-b2-setreportfreqparameter-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-b2-setreportfreqparameter-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-b2-setreportfreqparameter-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-b2-setreportfreqparameter-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.b2.SetReportFreqParameter.__init__`

初始化 `SetReportFreqParameter` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::b2::SetReportFreqParameter`
- 签名：`SetReportFreqParameter()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/b2/robot_state/robot_state_api.hpp:96`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = SetReportFreqParameter()
```

<a id="unitree-sdk2-cpp-robot-b2-setreportfreqparameter-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.b2.SetReportFreqParameter.from_json`

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

- 类：`unitree::robot::b2::SetReportFreqParameter`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/b2/robot_state/robot_state_api.hpp:102`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-b2-setreportfreqparameter-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.b2.SetReportFreqParameter.to_json`

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

- 类：`unitree::robot::b2::SetReportFreqParameter`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/b2/robot_state/robot_state_api.hpp:108`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-b2-sportclient"></a>
### `unitree_sdk2_cpp.robot.b2.SportClient`

Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

**导入**

```python
from unitree_sdk2_cpp.robot.b2 import SportClient
```

**基类**：`Client`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-b2-sportclient-dunder-init-1) | `def __init__(self, enable_lease: bool = False) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`init`](#unitree-sdk2-cpp-robot-b2-sportclient-init-1) | `def init(self) -> None` | `AVAILABLE` | `INITIALIZATION` |
| [`damp`](#unitree-sdk2-cpp-robot-b2-sportclient-damp-1) | `def damp(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`balance_stand`](#unitree-sdk2-cpp-robot-b2-sportclient-balance-stand-1) | `def balance_stand(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`stop_move`](#unitree-sdk2-cpp-robot-b2-sportclient-stop-move-1) | `def stop_move(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`stand_up`](#unitree-sdk2-cpp-robot-b2-sportclient-stand-up-1) | `def stand_up(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`stand_down`](#unitree-sdk2-cpp-robot-b2-sportclient-stand-down-1) | `def stand_down(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`recovery_stand`](#unitree-sdk2-cpp-robot-b2-sportclient-recovery-stand-1) | `def recovery_stand(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`move`](#unitree-sdk2-cpp-robot-b2-sportclient-move-1) | `def move(self, vx: float, vy: float, vyaw: float) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`switch_gait`](#unitree-sdk2-cpp-robot-b2-sportclient-switch-gait-1) | `def switch_gait(self, d: int) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`body_height`](#unitree-sdk2-cpp-robot-b2-sportclient-body-height-1) | `def body_height(self, height: float) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`speed_level`](#unitree-sdk2-cpp-robot-b2-sportclient-speed-level-1) | `def speed_level(self, level: int) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`trajectory_follow`](#unitree-sdk2-cpp-robot-b2-sportclient-trajectory-follow-1) | `def trajectory_follow(self, path: Sequence[PathPoint]) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`continuous_gait`](#unitree-sdk2-cpp-robot-b2-sportclient-continuous-gait-1) | `def continuous_gait(self, flag: bool) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`move_to_pos`](#unitree-sdk2-cpp-robot-b2-sportclient-move-to-pos-1) | `def move_to_pos(self, x: float, y: float, yaw: float) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`switch_move_mode`](#unitree-sdk2-cpp-robot-b2-sportclient-switch-move-mode-1) | `def switch_move_mode(self, flag: bool) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`vision_walk`](#unitree-sdk2-cpp-robot-b2-sportclient-vision-walk-1) | `def vision_walk(self, flag: bool) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`hand_stand`](#unitree-sdk2-cpp-robot-b2-sportclient-hand-stand-1) | `def hand_stand(self, flag: bool) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`auto_recovery_set`](#unitree-sdk2-cpp-robot-b2-sportclient-auto-recovery-set-1) | `def auto_recovery_set(self, flag: bool) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`free_walk`](#unitree-sdk2-cpp-robot-b2-sportclient-free-walk-1) | `def free_walk(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`classic_walk`](#unitree-sdk2-cpp-robot-b2-sportclient-classic-walk-1) | `def classic_walk(self, flag: bool) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`fast_walk`](#unitree-sdk2-cpp-robot-b2-sportclient-fast-walk-1) | `def fast_walk(self, flag: bool) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`euler`](#unitree-sdk2-cpp-robot-b2-sportclient-euler-1) | `def euler(self, roll: float, pitch: float, yaw: float) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`free_height`](#unitree-sdk2-cpp-robot-b2-sportclient-free-height-1) | `def free_height(self, flag: bool) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`gait_height`](#unitree-sdk2-cpp-robot-b2-sportclient-gait-height-1) | `def gait_height(self, flag: bool) -> int` | `AVAILABLE` | `MOTION_COMMAND` |

<a id="unitree-sdk2-cpp-robot-b2-sportclient-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.b2.SportClient.__init__`

初始化 `SportClient` 实例。是否能实际构造取决于下方可用性状态。

**签名**

```python
def __init__(self, enable_lease: bool = False) -> None
```

**可用性与安全性**

**`AVAILABLE` / `CONSTRUCTION`**：当前绑定源码已实现；实际执行条件仍取决于平台和对应 SDK 环境。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `enable_lease` | `bool` | `False` | 是否启用 SDK lease 机制；lease 的获得、续期和释放规则以服务协议为准。 对应 C++ 参数 `enableLease: bool`。 只接受布尔语义。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。 |

**对应 C++**

- 类：`unitree::robot::b2::SportClient`
- 签名：`SportClient(bool)`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/b2/sport/sport_client.hpp:34`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = SportClient(enable_lease=enable_lease)
```

<a id="unitree-sdk2-cpp-robot-b2-sportclient-init-1"></a>
#### `unitree_sdk2_cpp.robot.b2.SportClient.init`

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

- 类：`unitree::robot::b2::SportClient`
- 签名：`Init()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/sport/sport_client.hpp:37`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.init()
```

<a id="unitree-sdk2-cpp-robot-b2-sportclient-damp-1"></a>
#### `unitree_sdk2_cpp.robot.b2.SportClient.damp`

对应 C++ SDK 操作 `Damp()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def damp(self) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::b2::SportClient`
- 签名：`Damp()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/sport/sport_client.hpp:39`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.damp()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-sportclient-balance-stand-1"></a>
#### `unitree_sdk2_cpp.robot.b2.SportClient.balance_stand`

对应 C++ SDK 操作 `BalanceStand()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def balance_stand(self) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::b2::SportClient`
- 签名：`BalanceStand()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/sport/sport_client.hpp:41`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.balance_stand()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-sportclient-stop-move-1"></a>
#### `unitree_sdk2_cpp.robot.b2.SportClient.stop_move`

请求停止对应 SDK 操作。该名称不等同于经过验证的物理急停。

**签名**

```python
def stop_move(self) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::b2::SportClient`
- 签名：`StopMove()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/sport/sport_client.hpp:43`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.stop_move()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-sportclient-stand-up-1"></a>
#### `unitree_sdk2_cpp.robot.b2.SportClient.stand_up`

对应 C++ SDK 操作 `StandUp()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def stand_up(self) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::b2::SportClient`
- 签名：`StandUp()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/sport/sport_client.hpp:45`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.stand_up()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-sportclient-stand-down-1"></a>
#### `unitree_sdk2_cpp.robot.b2.SportClient.stand_down`

对应 C++ SDK 操作 `StandDown()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def stand_down(self) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::b2::SportClient`
- 签名：`StandDown()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/sport/sport_client.hpp:47`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.stand_down()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-sportclient-recovery-stand-1"></a>
#### `unitree_sdk2_cpp.robot.b2.SportClient.recovery_stand`

对应 C++ SDK 操作 `RecoveryStand()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def recovery_stand(self) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::b2::SportClient`
- 签名：`RecoveryStand()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/sport/sport_client.hpp:49`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.recovery_stand()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-sportclient-move-1"></a>
#### `unitree_sdk2_cpp.robot.b2.SportClient.move`

对应 C++ SDK 操作 `Move(float, float, float)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def move(self, vx: float, vy: float, vyaw: float) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `vx` | `float` | 必填 | X 方向速度参数。坐标系、单位、符号和安全范围必须查目标型号运动协议。 对应 C++ 参数 `vx: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |
| `vy` | `float` | 必填 | Y 方向速度参数。坐标系、单位、符号和安全范围必须查目标型号运动协议。 对应 C++ 参数 `vy: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |
| `vyaw` | `float` | 必填 | 偏航角速度参数。单位、符号和安全范围必须查目标型号运动协议。 对应 C++ 参数 `vyaw: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::b2::SportClient`
- 签名：`Move(float, float, float)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/sport/sport_client.hpp:51`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.move(vx=vx, vy=vy, vyaw=vyaw)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-sportclient-switch-gait-1"></a>
#### `unitree_sdk2_cpp.robot.b2.SportClient.switch_gait`

对应 C++ SDK 操作 `SwitchGait(int)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def switch_gait(self, d: int) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `d` | `int` | 必填 | 传给该接口的 `d` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `d: int`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::b2::SportClient`
- 签名：`SwitchGait(int)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/sport/sport_client.hpp:53`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.switch_gait(d=d)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-sportclient-body-height-1"></a>
#### `unitree_sdk2_cpp.robot.b2.SportClient.body_height`

对应 C++ SDK 操作 `BodyHeight(float)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def body_height(self, height: float) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `height` | `float` | 必填 | 传给该接口的 高度 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `height: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::b2::SportClient`
- 签名：`BodyHeight(float)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/sport/sport_client.hpp:55`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.body_height(height=height)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-sportclient-speed-level-1"></a>
#### `unitree_sdk2_cpp.robot.b2.SportClient.speed_level`

对应 C++ SDK 操作 `SpeedLevel(int)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def speed_level(self, level: int) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `level` | `int` | 必填 | 传给该接口的 `level` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `level: int`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::b2::SportClient`
- 签名：`SpeedLevel(int)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/sport/sport_client.hpp:57`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.speed_level(level=level)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-sportclient-trajectory-follow-1"></a>
#### `unitree_sdk2_cpp.robot.b2.SportClient.trajectory_follow`

对应 C++ SDK 操作 `TrajectoryFollow(std::vector<unitree::robot::b2::PathPoint> &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def trajectory_follow(self, path: Sequence[PathPoint]) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `path` | `Sequence[PathPoint]` | 必填 | 传给该接口的 `path` 参数，Python 类型为 `Sequence[PathPoint]`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `path: std::vector<unitree::robot::b2::PathPoint> &`。 底层是可变长度 vector |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::b2::SportClient`
- 签名：`TrajectoryFollow(std::vector<unitree::robot::b2::PathPoint> &)`
- 绑定策略：`MUTABLE_INPUT_COPY`
- 声明位置：`include/unitree/robot/b2/sport/sport_client.hpp:59`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.trajectory_follow(path=path)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-sportclient-continuous-gait-1"></a>
#### `unitree_sdk2_cpp.robot.b2.SportClient.continuous_gait`

对应 C++ SDK 操作 `ContinuousGait(bool)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def continuous_gait(self, flag: bool) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `flag` | `bool` | 必填 | 布尔开关。`True` 和 `False` 的具体业务效果由当前方法定义。 对应 C++ 参数 `flag: bool`。 只接受布尔语义。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::b2::SportClient`
- 签名：`ContinuousGait(bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/sport/sport_client.hpp:61`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.continuous_gait(flag=flag)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-sportclient-move-to-pos-1"></a>
#### `unitree_sdk2_cpp.robot.b2.SportClient.move_to_pos`

对应 C++ SDK 操作 `MoveToPos(float, float, float)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def move_to_pos(self, x: float, y: float, yaw: float) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `x` | `float` | 必填 | X 方向位置或分量参数。参考系、单位和范围必须查当前方法及目标型号协议。 对应 C++ 参数 `x: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |
| `y` | `float` | 必填 | Y 方向位置或分量参数。参考系、单位和范围必须查当前方法及目标型号协议。 对应 C++ 参数 `y: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |
| `yaw` | `float` | 必填 | 偏航角或偏航目标参数。参考系、单位和范围必须查目标型号协议。 对应 C++ 参数 `yaw: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::b2::SportClient`
- 签名：`MoveToPos(float, float, float)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/sport/sport_client.hpp:63`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.move_to_pos(x=x, y=y, yaw=yaw)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-sportclient-switch-move-mode-1"></a>
#### `unitree_sdk2_cpp.robot.b2.SportClient.switch_move_mode`

对应 C++ SDK 操作 `SwitchMoveMode(bool)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def switch_move_mode(self, flag: bool) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `flag` | `bool` | 必填 | 布尔开关。`True` 和 `False` 的具体业务效果由当前方法定义。 对应 C++ 参数 `flag: bool`。 只接受布尔语义。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::b2::SportClient`
- 签名：`SwitchMoveMode(bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/sport/sport_client.hpp:65`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.switch_move_mode(flag=flag)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-sportclient-vision-walk-1"></a>
#### `unitree_sdk2_cpp.robot.b2.SportClient.vision_walk`

对应 C++ SDK 操作 `VisionWalk(bool)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def vision_walk(self, flag: bool) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `flag` | `bool` | 必填 | 布尔开关。`True` 和 `False` 的具体业务效果由当前方法定义。 对应 C++ 参数 `flag: bool`。 只接受布尔语义。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::b2::SportClient`
- 签名：`VisionWalk(bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/sport/sport_client.hpp:67`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.vision_walk(flag=flag)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-sportclient-hand-stand-1"></a>
#### `unitree_sdk2_cpp.robot.b2.SportClient.hand_stand`

对应 C++ SDK 操作 `HandStand(bool)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def hand_stand(self, flag: bool) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `flag` | `bool` | 必填 | 布尔开关。`True` 和 `False` 的具体业务效果由当前方法定义。 对应 C++ 参数 `flag: bool`。 只接受布尔语义。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::b2::SportClient`
- 签名：`HandStand(bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/sport/sport_client.hpp:69`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.hand_stand(flag=flag)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-sportclient-auto-recovery-set-1"></a>
#### `unitree_sdk2_cpp.robot.b2.SportClient.auto_recovery_set`

对应 C++ SDK 操作 `AutoRecoverySet(bool)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def auto_recovery_set(self, flag: bool) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `flag` | `bool` | 必填 | 布尔开关。`True` 和 `False` 的具体业务效果由当前方法定义。 对应 C++ 参数 `flag: bool`。 只接受布尔语义。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::b2::SportClient`
- 签名：`AutoRecoverySet(bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/sport/sport_client.hpp:71`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.auto_recovery_set(flag=flag)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-sportclient-free-walk-1"></a>
#### `unitree_sdk2_cpp.robot.b2.SportClient.free_walk`

对应 C++ SDK 操作 `FreeWalk()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def free_walk(self) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::b2::SportClient`
- 签名：`FreeWalk()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/sport/sport_client.hpp:73`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.free_walk()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-sportclient-classic-walk-1"></a>
#### `unitree_sdk2_cpp.robot.b2.SportClient.classic_walk`

对应 C++ SDK 操作 `ClassicWalk(bool)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def classic_walk(self, flag: bool) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `flag` | `bool` | 必填 | 布尔开关。`True` 和 `False` 的具体业务效果由当前方法定义。 对应 C++ 参数 `flag: bool`。 只接受布尔语义。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::b2::SportClient`
- 签名：`ClassicWalk(bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/sport/sport_client.hpp:75`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.classic_walk(flag=flag)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-sportclient-fast-walk-1"></a>
#### `unitree_sdk2_cpp.robot.b2.SportClient.fast_walk`

对应 C++ SDK 操作 `FastWalk(bool)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def fast_walk(self, flag: bool) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `flag` | `bool` | 必填 | 布尔开关。`True` 和 `False` 的具体业务效果由当前方法定义。 对应 C++ 参数 `flag: bool`。 只接受布尔语义。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::b2::SportClient`
- 签名：`FastWalk(bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/sport/sport_client.hpp:77`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.fast_walk(flag=flag)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-sportclient-euler-1"></a>
#### `unitree_sdk2_cpp.robot.b2.SportClient.euler`

对应 C++ SDK 操作 `Euler(float, float, float)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def euler(self, roll: float, pitch: float, yaw: float) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `roll` | `float` | 必填 | 传给该接口的 `roll` 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `roll: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |
| `pitch` | `float` | 必填 | 传给该接口的 `pitch` 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `pitch: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |
| `yaw` | `float` | 必填 | 偏航角或偏航目标参数。参考系、单位和范围必须查目标型号协议。 对应 C++ 参数 `yaw: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::b2::SportClient`
- 签名：`Euler(float, float, float)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/sport/sport_client.hpp:79`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.euler(roll=roll, pitch=pitch, yaw=yaw)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-sportclient-free-height-1"></a>
#### `unitree_sdk2_cpp.robot.b2.SportClient.free_height`

对应 C++ SDK 操作 `FreeHeight(bool)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def free_height(self, flag: bool) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `flag` | `bool` | 必填 | 布尔开关。`True` 和 `False` 的具体业务效果由当前方法定义。 对应 C++ 参数 `flag: bool`。 只接受布尔语义。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::b2::SportClient`
- 签名：`FreeHeight(bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/sport/sport_client.hpp:81`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.free_height(flag=flag)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-sportclient-gait-height-1"></a>
#### `unitree_sdk2_cpp.robot.b2.SportClient.gait_height`

对应 C++ SDK 操作 `GaitHeight(bool)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def gait_height(self, flag: bool) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `flag` | `bool` | 必填 | 布尔开关。`True` 和 `False` 的具体业务效果由当前方法定义。 对应 C++ 参数 `flag: bool`。 只接受布尔语义。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::b2::SportClient`
- 签名：`GaitHeight(bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/b2/sport/sport_client.hpp:83`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.gait_height(flag=flag)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-b2-stpathpoint"></a>
### `unitree_sdk2_cpp.robot.b2.stPathPoint`

SDK 数据值类型；公开字段和转换方法见下文。

**导入**

```python
from unitree_sdk2_cpp.robot.b2 import stPathPoint
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `time_from_start` | `float` | 传给该接口的 `time` `from` `start` 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.time_from_start` / `obj.time_from_start = value` |
| `x` | `float` | X 方向位置或分量参数。参考系、单位和范围必须查当前方法及目标型号协议。 | `value = obj.x` / `obj.x = value` |
| `y` | `float` | Y 方向位置或分量参数。参考系、单位和范围必须查当前方法及目标型号协议。 | `value = obj.y` / `obj.y = value` |
| `yaw` | `float` | 偏航角或偏航目标参数。参考系、单位和范围必须查目标型号协议。 | `value = obj.yaw` / `obj.yaw = value` |
| `vx` | `float` | X 方向速度参数。坐标系、单位、符号和安全范围必须查目标型号运动协议。 | `value = obj.vx` / `obj.vx = value` |
| `vy` | `float` | Y 方向速度参数。坐标系、单位、符号和安全范围必须查目标型号运动协议。 | `value = obj.vy` / `obj.vy = value` |
| `vyaw` | `float` | 偏航角速度参数。单位、符号和安全范围必须查目标型号运动协议。 | `value = obj.vyaw` / `obj.vyaw = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-b2-stpathpoint-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |

<a id="unitree-sdk2-cpp-robot-b2-stpathpoint-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.b2.stPathPoint.__init__`

初始化 `stPathPoint` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::b2::stPathPoint`
- 签名：`stPathPoint()`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = stPathPoint()
```

---

[返回 API 总索引](../API_REFERENCE_ZH.md)
