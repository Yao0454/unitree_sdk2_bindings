# Unitree SDK2 Python API 参考分卷

[返回 API 总索引](../API_REFERENCE_ZH.md) · [阅读从零开始指南](../BEGINNER_GUIDE_ZH.md)

> [!WARNING]
> 本分卷同时包含 `AVAILABLE` 和 `SIGNATURE_ONLY`。后者只是设计期类型签名。运动及硬件副作用方法即使标记为 `AVAILABLE`，也不表示当前环境可安全执行。

> [!NOTE]
> 本文件由 `generator/generate_api_docs.py` 自动生成，请勿手工维护 API 条目。

---

<a id="unitree-sdk2-cpp-robot-go2"></a>
## Go2 Robot API

模块：`unitree_sdk2_cpp.robot.go2`

### 类索引

| 类 | 公开函数签名 | 属性 |
| --- | ---: | ---: |
| [`ConfigClient`](#unitree-sdk2-cpp-robot-go2-configclient) | 8 | 0 |
| [`ConfigDelParameter`](#unitree-sdk2-cpp-robot-go2-configdelparameter) | 3 | 0 |
| [`ConfigGetData`](#unitree-sdk2-cpp-robot-go2-configgetdata) | 3 | 0 |
| [`ConfigGetParameter`](#unitree-sdk2-cpp-robot-go2-configgetparameter) | 3 | 0 |
| [`ConfigMeta`](#unitree-sdk2-cpp-robot-go2-configmeta) | 1 | 0 |
| [`ConfigMetaData`](#unitree-sdk2-cpp-robot-go2-configmetadata) | 3 | 0 |
| [`ConfigMetaParameter`](#unitree-sdk2-cpp-robot-go2-configmetaparameter) | 3 | 0 |
| [`ConfigSetParameter`](#unitree-sdk2-cpp-robot-go2-configsetparameter) | 3 | 0 |
| [`JsonizeCommObjInt`](#unitree-sdk2-cpp-robot-go2-jsonizecommobjint) | 3 | 0 |
| [`JsonizeConfigMeta`](#unitree-sdk2-cpp-robot-go2-jsonizeconfigmeta) | 3 | 0 |
| [`JsonizeDataBool`](#unitree-sdk2-cpp-robot-go2-jsonizedatabool) | 3 | 0 |
| [`JsonizeDataDouble`](#unitree-sdk2-cpp-robot-go2-jsonizedatadouble) | 3 | 0 |
| [`JsonizeDataFloat`](#unitree-sdk2-cpp-robot-go2-jsonizedatafloat) | 3 | 0 |
| [`JsonizeDataInt`](#unitree-sdk2-cpp-robot-go2-jsonizedataint) | 3 | 0 |
| [`JsonizeDataString`](#unitree-sdk2-cpp-robot-go2-jsonizedatastring) | 3 | 0 |
| [`JsonizeFlagBool`](#unitree-sdk2-cpp-robot-go2-jsonizeflagbool) | 3 | 0 |
| [`JsonizePathPoint`](#unitree-sdk2-cpp-robot-go2-jsonizepathpoint) | 3 | 0 |
| [`JsonizeQuat`](#unitree-sdk2-cpp-robot-go2-jsonizequat) | 3 | 0 |
| [`JsonizeVec3`](#unitree-sdk2-cpp-robot-go2-jsonizevec3) | 3 | 0 |
| [`ObstaclesAvoidClient`](#unitree-sdk2-cpp-robot-go2-obstaclesavoidclient) | 8 | 0 |
| [`ObstaclesAvoidMoveParameter`](#unitree-sdk2-cpp-robot-go2-obstaclesavoidmoveparameter) | 3 | 0 |
| [`ObstaclesAvoidRemoteCommandSource`](#unitree-sdk2-cpp-robot-go2-obstaclesavoidremotecommandsource) | 3 | 0 |
| [`ObstaclesAvoidSwitchGetData`](#unitree-sdk2-cpp-robot-go2-obstaclesavoidswitchgetdata) | 3 | 0 |
| [`ObstaclesAvoidSwitchSetParameter`](#unitree-sdk2-cpp-robot-go2-obstaclesavoidswitchsetparameter) | 3 | 0 |
| [`RobotStateClient`](#unitree-sdk2-cpp-robot-go2-robotstateclient) | 5 | 0 |
| [`ServiceState`](#unitree-sdk2-cpp-robot-go2-servicestate) | 1 | 0 |
| [`ServiceStateData`](#unitree-sdk2-cpp-robot-go2-servicestatedata) | 3 | 0 |
| [`ServiceSwitchData`](#unitree-sdk2-cpp-robot-go2-serviceswitchdata) | 3 | 0 |
| [`ServiceSwitchParameter`](#unitree-sdk2-cpp-robot-go2-serviceswitchparameter) | 3 | 0 |
| [`SetReportFreqParameter`](#unitree-sdk2-cpp-robot-go2-setreportfreqparameter) | 3 | 0 |
| [`SportClient`](#unitree-sdk2-cpp-robot-go2-sportclient) | 41 | 0 |
| [`UtrackClient`](#unitree-sdk2-cpp-robot-go2-utrackclient) | 5 | 0 |
| [`UtrackSwitchGetData`](#unitree-sdk2-cpp-robot-go2-utrackswitchgetdata) | 3 | 0 |
| [`UtrackSwitchSetParameter`](#unitree-sdk2-cpp-robot-go2-utrackswitchsetparameter) | 3 | 0 |
| [`VideoClient`](#unitree-sdk2-cpp-robot-go2-videoclient) | 3 | 0 |
| [`VuiClient`](#unitree-sdk2-cpp-robot-go2-vuiclient) | 8 | 0 |
| [`stPathPoint`](#unitree-sdk2-cpp-robot-go2-stpathpoint) | 1 | 0 |

<a id="unitree-sdk2-cpp-robot-go2-configclient"></a>
### `unitree_sdk2_cpp.robot.go2.ConfigClient`

Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import ConfigClient
```

**基类**：`Client`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-go2-configclient-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`init`](#unitree-sdk2-cpp-robot-go2-configclient-init-1) | `def init(self) -> None` | `AVAILABLE` | `INITIALIZATION` |
| [`set`](#unitree-sdk2-cpp-robot-go2-configclient-set-1) | `def set(self, name: str, content: str) -> int` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |
| [`get`](#unitree-sdk2-cpp-robot-go2-configclient-get-1) | `def get(self, name: str) -> tuple[int, str]` | `AVAILABLE` | `READ_ONLY` |
| [`del_`](#unitree-sdk2-cpp-robot-go2-configclient-del-1) | `def del_(self, name: str) -> int` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |
| [`meta_config_meta`](#unitree-sdk2-cpp-robot-go2-configclient-meta-config-meta-1) | `def meta_config_meta(self, name: str) -> tuple[int, ConfigMeta]` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |
| [`meta_string`](#unitree-sdk2-cpp-robot-go2-configclient-meta-string-1) | `def meta_string(self, name: str) -> tuple[int, str]` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |
| [`subscribe_change_status`](#unitree-sdk2-cpp-robot-go2-configclient-subscribe-change-status-1) | `def subscribe_change_status(self, name: str, callback: Callable[[str, str], None]) -> None` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |

<a id="unitree-sdk2-cpp-robot-go2-configclient-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ConfigClient.__init__`

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

- 类：`unitree::robot::go2::ConfigClient`
- 签名：`ConfigClient()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/go2/config/config_client.hpp:41`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = ConfigClient()
```

<a id="unitree-sdk2-cpp-robot-go2-configclient-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ConfigClient.init`

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

- 类：`unitree::robot::go2::ConfigClient`
- 签名：`Init()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/config/config_client.hpp:44`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.init()
```

<a id="unitree-sdk2-cpp-robot-go2-configclient-set-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ConfigClient.set`

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

- 类：`unitree::robot::go2::ConfigClient`
- 签名：`Set(const std::string &, const std::string &)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/config/config_client.hpp:46`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.set(name=name, content=content)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-configclient-get-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ConfigClient.get`

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

- 类：`unitree::robot::go2::ConfigClient`
- 签名：`Get(const std::string &, std::string &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/go2/config/config_client.hpp:47`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, content = obj.get(name=name)
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-go2-configclient-del-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ConfigClient.del_`

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

- 类：`unitree::robot::go2::ConfigClient`
- 签名：`Del(const std::string &)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/config/config_client.hpp:48`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.del_(name=name)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-configclient-meta-config-meta-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ConfigClient.meta_config_meta`

对应 C++ SDK 操作 `Meta(const std::string &, unitree::robot::go2::ConfigMeta &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

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
| [1] `meta` | `ConfigMeta` | 传给该接口的 `meta` 参数，Python 类型为 `ConfigMeta`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `meta: unitree::robot::go2::ConfigMeta &`。 |

**对应 C++**

- 类：`unitree::robot::go2::ConfigClient`
- 签名：`Meta(const std::string &, unitree::robot::go2::ConfigMeta &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/go2/config/config_client.hpp:49`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, meta = obj.meta_config_meta(name=name)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-configclient-meta-string-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ConfigClient.meta_string`

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

- 类：`unitree::robot::go2::ConfigClient`
- 签名：`Meta(const std::string &, std::string &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/go2/config/config_client.hpp:50`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, meta = obj.meta_string(name=name)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-configclient-subscribe-change-status-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ConfigClient.subscribe_change_status`

对应 C++ SDK 操作 `SubscribeChangeStatus(const std::string &, const unitree::robot::go2::ConfigChangeStatusCallback &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

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
| `callback` | `Callable[[str, str], None]` | 必填 | 收到数据或状态变化时调用的 Python 回调。回调签名必须与类型提示一致，并应快速返回。 对应 C++ 参数 `callback: const unitree::robot::go2::ConfigChangeStatusCallback &`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree::robot::go2::ConfigClient`
- 签名：`SubscribeChangeStatus(const std::string &, const unitree::robot::go2::ConfigChangeStatusCallback &)`
- 绑定策略：`CALLBACK_MANUAL`
- 声明位置：`include/unitree/robot/go2/config/config_client.hpp:52`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 回调可能由 SDK 工作线程触发；回调应快速返回、捕获异常，并通过线程安全队列移交耗时工作。

**用法**

```python
obj.subscribe_change_status(name=name, callback=callback)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-configdelparameter"></a>
### `unitree_sdk2_cpp.robot.go2.ConfigDelParameter`

SDK 请求参数值类型；当前可能仅提供设计期签名。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import ConfigDelParameter
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `name` | `str` | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 | `value = obj.name` / `obj.name = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-go2-configdelparameter-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-go2-configdelparameter-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-go2-configdelparameter-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-go2-configdelparameter-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ConfigDelParameter.__init__`

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

- 类：`unitree::robot::go2::ConfigDelParameter`
- 签名：`ConfigDelParameter()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/go2/config/config_api.hpp:140`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = ConfigDelParameter()
```

<a id="unitree-sdk2-cpp-robot-go2-configdelparameter-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ConfigDelParameter.from_json`

从 JSON 风格字典读取字段并更新当前 SDK 值对象。

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

- 类：`unitree::robot::go2::ConfigDelParameter`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/go2/config/config_api.hpp:146`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-go2-configdelparameter-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ConfigDelParameter.to_json`

把当前 SDK 值对象转换为 JSON 风格字典。

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

- 类：`unitree::robot::go2::ConfigDelParameter`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/go2/config/config_api.hpp:151`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-go2-configgetdata"></a>
### `unitree_sdk2_cpp.robot.go2.ConfigGetData`

SDK 数据值类型；公开字段和转换方法见下文。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import ConfigGetData
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `content` | `str` | 配置、请求或序列化内容。具体格式由对应服务协议定义。 | `value = obj.content` / `obj.content = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-go2-configgetdata-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-go2-configgetdata-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-go2-configgetdata-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-go2-configgetdata-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ConfigGetData.__init__`

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

- 类：`unitree::robot::go2::ConfigGetData`
- 签名：`ConfigGetData()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/go2/config/config_api.hpp:117`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = ConfigGetData()
```

<a id="unitree-sdk2-cpp-robot-go2-configgetdata-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ConfigGetData.from_json`

从 JSON 风格字典读取字段并更新当前 SDK 值对象。

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

- 类：`unitree::robot::go2::ConfigGetData`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/go2/config/config_api.hpp:123`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-go2-configgetdata-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ConfigGetData.to_json`

把当前 SDK 值对象转换为 JSON 风格字典。

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

- 类：`unitree::robot::go2::ConfigGetData`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/go2/config/config_api.hpp:128`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-go2-configgetparameter"></a>
### `unitree_sdk2_cpp.robot.go2.ConfigGetParameter`

SDK 请求参数值类型；当前可能仅提供设计期签名。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import ConfigGetParameter
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `name` | `str` | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 | `value = obj.name` / `obj.name = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-go2-configgetparameter-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-go2-configgetparameter-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-go2-configgetparameter-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-go2-configgetparameter-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ConfigGetParameter.__init__`

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

- 类：`unitree::robot::go2::ConfigGetParameter`
- 签名：`ConfigGetParameter()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/go2/config/config_api.hpp:94`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = ConfigGetParameter()
```

<a id="unitree-sdk2-cpp-robot-go2-configgetparameter-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ConfigGetParameter.from_json`

从 JSON 风格字典读取字段并更新当前 SDK 值对象。

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

- 类：`unitree::robot::go2::ConfigGetParameter`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/go2/config/config_api.hpp:100`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-go2-configgetparameter-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ConfigGetParameter.to_json`

把当前 SDK 值对象转换为 JSON 风格字典。

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

- 类：`unitree::robot::go2::ConfigGetParameter`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/go2/config/config_api.hpp:105`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-go2-configmeta"></a>
### `unitree_sdk2_cpp.robot.go2.ConfigMeta`

SDK 数据值类型；公开字段和转换方法见下文。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import ConfigMeta
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
| [`__init__`](#unitree-sdk2-cpp-robot-go2-configmeta-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |

<a id="unitree-sdk2-cpp-robot-go2-configmeta-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ConfigMeta.__init__`

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

- 类：`unitree::robot::go2::ConfigMeta`
- 签名：`ConfigMeta()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/go2/config/config_client.hpp:20`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = ConfigMeta()
```

<a id="unitree-sdk2-cpp-robot-go2-configmetadata"></a>
### `unitree_sdk2_cpp.robot.go2.ConfigMetaData`

SDK 数据值类型；公开字段和转换方法见下文。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import ConfigMetaData
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `meta` | `JsonizeConfigMeta` | 传给该接口的 `meta` 参数，Python 类型为 `JsonizeConfigMeta`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.meta` / `obj.meta = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-go2-configmetadata-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-go2-configmetadata-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-go2-configmetadata-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-go2-configmetadata-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ConfigMetaData.__init__`

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

- 类：`unitree::robot::go2::ConfigMetaData`
- 签名：`ConfigMetaData()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/go2/config/config_api.hpp:186`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = ConfigMetaData()
```

<a id="unitree-sdk2-cpp-robot-go2-configmetadata-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ConfigMetaData.from_json`

从 JSON 风格字典读取字段并更新当前 SDK 值对象。

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

- 类：`unitree::robot::go2::ConfigMetaData`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/go2/config/config_api.hpp:192`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-go2-configmetadata-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ConfigMetaData.to_json`

把当前 SDK 值对象转换为 JSON 风格字典。

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

- 类：`unitree::robot::go2::ConfigMetaData`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/go2/config/config_api.hpp:197`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-go2-configmetaparameter"></a>
### `unitree_sdk2_cpp.robot.go2.ConfigMetaParameter`

SDK 请求参数值类型；当前可能仅提供设计期签名。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import ConfigMetaParameter
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `name` | `str` | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 | `value = obj.name` / `obj.name = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-go2-configmetaparameter-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-go2-configmetaparameter-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-go2-configmetaparameter-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-go2-configmetaparameter-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ConfigMetaParameter.__init__`

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

- 类：`unitree::robot::go2::ConfigMetaParameter`
- 签名：`ConfigMetaParameter()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/go2/config/config_api.hpp:163`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = ConfigMetaParameter()
```

<a id="unitree-sdk2-cpp-robot-go2-configmetaparameter-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ConfigMetaParameter.from_json`

从 JSON 风格字典读取字段并更新当前 SDK 值对象。

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

- 类：`unitree::robot::go2::ConfigMetaParameter`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/go2/config/config_api.hpp:169`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-go2-configmetaparameter-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ConfigMetaParameter.to_json`

把当前 SDK 值对象转换为 JSON 风格字典。

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

- 类：`unitree::robot::go2::ConfigMetaParameter`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/go2/config/config_api.hpp:174`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-go2-configsetparameter"></a>
### `unitree_sdk2_cpp.robot.go2.ConfigSetParameter`

SDK 请求参数值类型；当前可能仅提供设计期签名。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import ConfigSetParameter
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
| [`__init__`](#unitree-sdk2-cpp-robot-go2-configsetparameter-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-go2-configsetparameter-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-go2-configsetparameter-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-go2-configsetparameter-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ConfigSetParameter.__init__`

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

- 类：`unitree::robot::go2::ConfigSetParameter`
- 签名：`ConfigSetParameter()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/go2/config/config_api.hpp:68`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = ConfigSetParameter()
```

<a id="unitree-sdk2-cpp-robot-go2-configsetparameter-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ConfigSetParameter.from_json`

从 JSON 风格字典读取字段并更新当前 SDK 值对象。

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

- 类：`unitree::robot::go2::ConfigSetParameter`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/go2/config/config_api.hpp:74`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-go2-configsetparameter-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ConfigSetParameter.to_json`

把当前 SDK 值对象转换为 JSON 风格字典。

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

- 类：`unitree::robot::go2::ConfigSetParameter`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/go2/config/config_api.hpp:80`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-go2-jsonizecommobjint"></a>
### `unitree_sdk2_cpp.robot.go2.JsonizeCommObjInt`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import JsonizeCommObjInt
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `value` | `int` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 | `value = obj.value` / `obj.value = value` |
| `name` | `str` | SDK 对象、配置项、服务或动作的名称。允许值由调用它的具体接口定义。 | `value = obj.name` / `obj.name = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-go2-jsonizecommobjint-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-go2-jsonizecommobjint-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-go2-jsonizecommobjint-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-go2-jsonizecommobjint-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.JsonizeCommObjInt.__init__`

初始化 `JsonizeCommObjInt` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::go2::JsonizeCommObjInt`
- 签名：`JsonizeCommObjInt()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/go2/public/jsonize_type.hpp:287`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = JsonizeCommObjInt()
```

<a id="unitree-sdk2-cpp-robot-go2-jsonizecommobjint-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.JsonizeCommObjInt.from_json`

从 JSON 风格字典读取字段并更新当前 SDK 值对象。

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

- 类：`unitree::robot::go2::JsonizeCommObjInt`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/go2/public/jsonize_type.hpp:293`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-go2-jsonizecommobjint-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.JsonizeCommObjInt.to_json`

把当前 SDK 值对象转换为 JSON 风格字典。

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

- 类：`unitree::robot::go2::JsonizeCommObjInt`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/go2/public/jsonize_type.hpp:298`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-go2-jsonizeconfigmeta"></a>
### `unitree_sdk2_cpp.robot.go2.JsonizeConfigMeta`

SDK 数据值类型；公开字段和转换方法见下文。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import JsonizeConfigMeta
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
| [`__init__`](#unitree-sdk2-cpp-robot-go2-jsonizeconfigmeta-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-go2-jsonizeconfigmeta-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-go2-jsonizeconfigmeta-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-go2-jsonizeconfigmeta-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.JsonizeConfigMeta.__init__`

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

- 类：`unitree::robot::go2::JsonizeConfigMeta`
- 签名：`JsonizeConfigMeta()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/go2/config/config_api.hpp:36`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = JsonizeConfigMeta()
```

<a id="unitree-sdk2-cpp-robot-go2-jsonizeconfigmeta-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.JsonizeConfigMeta.from_json`

从 JSON 风格字典读取字段并更新当前 SDK 值对象。

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

- 类：`unitree::robot::go2::JsonizeConfigMeta`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/go2/config/config_api.hpp:42`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-go2-jsonizeconfigmeta-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.JsonizeConfigMeta.to_json`

把当前 SDK 值对象转换为 JSON 风格字典。

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

- 类：`unitree::robot::go2::JsonizeConfigMeta`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/go2/config/config_api.hpp:50`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-go2-jsonizedatabool"></a>
### `unitree_sdk2_cpp.robot.go2.JsonizeDataBool`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import JsonizeDataBool
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `data` | `bool` | 传给该接口的 数据 参数，Python 类型为 `bool`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.data` / `obj.data = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-go2-jsonizedatabool-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-go2-jsonizedatabool-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-go2-jsonizedatabool-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-go2-jsonizedatabool-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.JsonizeDataBool.__init__`

初始化 `JsonizeDataBool` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::go2::JsonizeDataBool`
- 签名：`JsonizeDataBool()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/go2/public/jsonize_type.hpp:44`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = JsonizeDataBool()
```

<a id="unitree-sdk2-cpp-robot-go2-jsonizedatabool-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.JsonizeDataBool.from_json`

从 JSON 风格字典读取字段并更新当前 SDK 值对象。

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

- 类：`unitree::robot::go2::JsonizeDataBool`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/go2/public/jsonize_type.hpp:50`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-go2-jsonizedatabool-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.JsonizeDataBool.to_json`

把当前 SDK 值对象转换为 JSON 风格字典。

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

- 类：`unitree::robot::go2::JsonizeDataBool`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/go2/public/jsonize_type.hpp:55`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-go2-jsonizedatadouble"></a>
### `unitree_sdk2_cpp.robot.go2.JsonizeDataDouble`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import JsonizeDataDouble
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `data` | `float` | 传给该接口的 数据 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.data` / `obj.data = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-go2-jsonizedatadouble-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-go2-jsonizedatadouble-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-go2-jsonizedatadouble-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-go2-jsonizedatadouble-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.JsonizeDataDouble.__init__`

初始化 `JsonizeDataDouble` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::go2::JsonizeDataDouble`
- 签名：`JsonizeDataDouble()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/go2/public/jsonize_type.hpp:122`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = JsonizeDataDouble()
```

<a id="unitree-sdk2-cpp-robot-go2-jsonizedatadouble-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.JsonizeDataDouble.from_json`

从 JSON 风格字典读取字段并更新当前 SDK 值对象。

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

- 类：`unitree::robot::go2::JsonizeDataDouble`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/go2/public/jsonize_type.hpp:128`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-go2-jsonizedatadouble-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.JsonizeDataDouble.to_json`

把当前 SDK 值对象转换为 JSON 风格字典。

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

- 类：`unitree::robot::go2::JsonizeDataDouble`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/go2/public/jsonize_type.hpp:133`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-go2-jsonizedatafloat"></a>
### `unitree_sdk2_cpp.robot.go2.JsonizeDataFloat`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import JsonizeDataFloat
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `data` | `float` | 传给该接口的 数据 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.data` / `obj.data = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-go2-jsonizedatafloat-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-go2-jsonizedatafloat-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-go2-jsonizedatafloat-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-go2-jsonizedatafloat-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.JsonizeDataFloat.__init__`

初始化 `JsonizeDataFloat` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::go2::JsonizeDataFloat`
- 签名：`JsonizeDataFloat()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/go2/public/jsonize_type.hpp:96`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = JsonizeDataFloat()
```

<a id="unitree-sdk2-cpp-robot-go2-jsonizedatafloat-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.JsonizeDataFloat.from_json`

从 JSON 风格字典读取字段并更新当前 SDK 值对象。

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

- 类：`unitree::robot::go2::JsonizeDataFloat`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/go2/public/jsonize_type.hpp:102`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-go2-jsonizedatafloat-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.JsonizeDataFloat.to_json`

把当前 SDK 值对象转换为 JSON 风格字典。

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

- 类：`unitree::robot::go2::JsonizeDataFloat`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/go2/public/jsonize_type.hpp:107`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-go2-jsonizedataint"></a>
### `unitree_sdk2_cpp.robot.go2.JsonizeDataInt`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import JsonizeDataInt
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `data` | `int` | 传给该接口的 数据 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.data` / `obj.data = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-go2-jsonizedataint-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-go2-jsonizedataint-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-go2-jsonizedataint-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-go2-jsonizedataint-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.JsonizeDataInt.__init__`

初始化 `JsonizeDataInt` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::go2::JsonizeDataInt`
- 签名：`JsonizeDataInt()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/go2/public/jsonize_type.hpp:70`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = JsonizeDataInt()
```

<a id="unitree-sdk2-cpp-robot-go2-jsonizedataint-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.JsonizeDataInt.from_json`

从 JSON 风格字典读取字段并更新当前 SDK 值对象。

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

- 类：`unitree::robot::go2::JsonizeDataInt`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/go2/public/jsonize_type.hpp:76`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-go2-jsonizedataint-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.JsonizeDataInt.to_json`

把当前 SDK 值对象转换为 JSON 风格字典。

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

- 类：`unitree::robot::go2::JsonizeDataInt`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/go2/public/jsonize_type.hpp:81`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-go2-jsonizedatastring"></a>
### `unitree_sdk2_cpp.robot.go2.JsonizeDataString`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import JsonizeDataString
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `data` | `str` | 传给该接口的 数据 参数，Python 类型为 `str`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.data` / `obj.data = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-go2-jsonizedatastring-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-go2-jsonizedatastring-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-go2-jsonizedatastring-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-go2-jsonizedatastring-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.JsonizeDataString.__init__`

初始化 `JsonizeDataString` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::go2::JsonizeDataString`
- 签名：`JsonizeDataString()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/go2/public/jsonize_type.hpp:148`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = JsonizeDataString()
```

<a id="unitree-sdk2-cpp-robot-go2-jsonizedatastring-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.JsonizeDataString.from_json`

从 JSON 风格字典读取字段并更新当前 SDK 值对象。

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

- 类：`unitree::robot::go2::JsonizeDataString`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/go2/public/jsonize_type.hpp:154`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-go2-jsonizedatastring-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.JsonizeDataString.to_json`

把当前 SDK 值对象转换为 JSON 风格字典。

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

- 类：`unitree::robot::go2::JsonizeDataString`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/go2/public/jsonize_type.hpp:159`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-go2-jsonizeflagbool"></a>
### `unitree_sdk2_cpp.robot.go2.JsonizeFlagBool`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import JsonizeFlagBool
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `flag` | `bool` | 布尔开关。`True` 和 `False` 的具体业务效果由当前方法定义。 | `value = obj.flag` / `obj.flag = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-go2-jsonizeflagbool-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-go2-jsonizeflagbool-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-go2-jsonizeflagbool-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-go2-jsonizeflagbool-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.JsonizeFlagBool.__init__`

初始化 `JsonizeFlagBool` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::go2::JsonizeFlagBool`
- 签名：`JsonizeFlagBool()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/go2/public/jsonize_type.hpp:18`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = JsonizeFlagBool()
```

<a id="unitree-sdk2-cpp-robot-go2-jsonizeflagbool-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.JsonizeFlagBool.from_json`

从 JSON 风格字典读取字段并更新当前 SDK 值对象。

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

- 类：`unitree::robot::go2::JsonizeFlagBool`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/go2/public/jsonize_type.hpp:24`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-go2-jsonizeflagbool-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.JsonizeFlagBool.to_json`

把当前 SDK 值对象转换为 JSON 风格字典。

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

- 类：`unitree::robot::go2::JsonizeFlagBool`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/go2/public/jsonize_type.hpp:29`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-go2-jsonizepathpoint"></a>
### `unitree_sdk2_cpp.robot.go2.JsonizePathPoint`

SDK 数据值类型；公开字段和转换方法见下文。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import JsonizePathPoint
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
| [`__init__`](#unitree-sdk2-cpp-robot-go2-jsonizepathpoint-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-go2-jsonizepathpoint-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-go2-jsonizepathpoint-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-go2-jsonizepathpoint-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.JsonizePathPoint.__init__`

初始化 `JsonizePathPoint` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::go2::JsonizePathPoint`
- 签名：`JsonizePathPoint()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/go2/public/jsonize_type.hpp:241`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = JsonizePathPoint()
```

<a id="unitree-sdk2-cpp-robot-go2-jsonizepathpoint-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.JsonizePathPoint.from_json`

从 JSON 风格字典读取字段并更新当前 SDK 值对象。

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

- 类：`unitree::robot::go2::JsonizePathPoint`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/go2/public/jsonize_type.hpp:249`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-go2-jsonizepathpoint-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.JsonizePathPoint.to_json`

把当前 SDK 值对象转换为 JSON 风格字典。

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

- 类：`unitree::robot::go2::JsonizePathPoint`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/go2/public/jsonize_type.hpp:260`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-go2-jsonizequat"></a>
### `unitree_sdk2_cpp.robot.go2.JsonizeQuat`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import JsonizeQuat
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `x` | `float` | X 方向位置或分量参数。参考系、单位和范围必须查当前方法及目标型号协议。 | `value = obj.x` / `obj.x = value` |
| `y` | `float` | Y 方向位置或分量参数。参考系、单位和范围必须查当前方法及目标型号协议。 | `value = obj.y` / `obj.y = value` |
| `z` | `float` | Z 方向位置或分量参数。参考系、单位和范围必须查当前方法及目标型号协议。 | `value = obj.z` / `obj.z = value` |
| `w` | `float` | 传给该接口的 `w` 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.w` / `obj.w = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-go2-jsonizequat-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-go2-jsonizequat-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-go2-jsonizequat-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-go2-jsonizequat-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.JsonizeQuat.__init__`

初始化 `JsonizeQuat` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::go2::JsonizeQuat`
- 签名：`JsonizeQuat()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/go2/public/jsonize_type.hpp:206`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = JsonizeQuat()
```

<a id="unitree-sdk2-cpp-robot-go2-jsonizequat-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.JsonizeQuat.from_json`

从 JSON 风格字典读取字段并更新当前 SDK 值对象。

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

- 类：`unitree::robot::go2::JsonizeQuat`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/go2/public/jsonize_type.hpp:212`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-go2-jsonizequat-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.JsonizeQuat.to_json`

把当前 SDK 值对象转换为 JSON 风格字典。

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

- 类：`unitree::robot::go2::JsonizeQuat`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/go2/public/jsonize_type.hpp:220`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-go2-jsonizevec3"></a>
### `unitree_sdk2_cpp.robot.go2.JsonizeVec3`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import JsonizeVec3
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `x` | `float` | X 方向位置或分量参数。参考系、单位和范围必须查当前方法及目标型号协议。 | `value = obj.x` / `obj.x = value` |
| `y` | `float` | Y 方向位置或分量参数。参考系、单位和范围必须查当前方法及目标型号协议。 | `value = obj.y` / `obj.y = value` |
| `z` | `float` | Z 方向位置或分量参数。参考系、单位和范围必须查当前方法及目标型号协议。 | `value = obj.z` / `obj.z = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-go2-jsonizevec3-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-go2-jsonizevec3-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-go2-jsonizevec3-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-go2-jsonizevec3-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.JsonizeVec3.__init__`

初始化 `JsonizeVec3` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::go2::JsonizeVec3`
- 签名：`JsonizeVec3()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/go2/public/jsonize_type.hpp:174`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = JsonizeVec3()
```

<a id="unitree-sdk2-cpp-robot-go2-jsonizevec3-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.JsonizeVec3.from_json`

从 JSON 风格字典读取字段并更新当前 SDK 值对象。

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

- 类：`unitree::robot::go2::JsonizeVec3`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/go2/public/jsonize_type.hpp:180`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-go2-jsonizevec3-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.JsonizeVec3.to_json`

把当前 SDK 值对象转换为 JSON 风格字典。

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

- 类：`unitree::robot::go2::JsonizeVec3`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/go2/public/jsonize_type.hpp:187`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-go2-obstaclesavoidclient"></a>
### `unitree_sdk2_cpp.robot.go2.ObstaclesAvoidClient`

Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import ObstaclesAvoidClient
```

**基类**：`Client`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-go2-obstaclesavoidclient-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`init`](#unitree-sdk2-cpp-robot-go2-obstaclesavoidclient-init-1) | `def init(self) -> None` | `AVAILABLE` | `INITIALIZATION` |
| [`switch_set`](#unitree-sdk2-cpp-robot-go2-obstaclesavoidclient-switch-set-1) | `def switch_set(self, enable: bool) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`switch_get`](#unitree-sdk2-cpp-robot-go2-obstaclesavoidclient-switch-get-1) | `def switch_get(self) -> tuple[int, bool]` | `AVAILABLE` | `MOTION_COMMAND` |
| [`move`](#unitree-sdk2-cpp-robot-go2-obstaclesavoidclient-move-1) | `def move(self, x: float, y: float, yaw: float) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`use_remote_command_from_api`](#unitree-sdk2-cpp-robot-go2-obstaclesavoidclient-use-remote-command-from-api-1) | `def use_remote_command_from_api(self, is_remote_commands_from_api: bool) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`move_to_absolute_position`](#unitree-sdk2-cpp-robot-go2-obstaclesavoidclient-move-to-absolute-position-1) | `def move_to_absolute_position(self, x: float, y: float, yaw: float) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`move_to_increment_position`](#unitree-sdk2-cpp-robot-go2-obstaclesavoidclient-move-to-increment-position-1) | `def move_to_increment_position(self, x: float, y: float, yaw: float) -> int` | `AVAILABLE` | `MOTION_COMMAND` |

<a id="unitree-sdk2-cpp-robot-go2-obstaclesavoidclient-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ObstaclesAvoidClient.__init__`

初始化 `ObstaclesAvoidClient` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::go2::ObstaclesAvoidClient`
- 签名：`ObstaclesAvoidClient()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/go2/obstacles_avoid/obstacles_avoid_client.hpp:15`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = ObstaclesAvoidClient()
```

<a id="unitree-sdk2-cpp-robot-go2-obstaclesavoidclient-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ObstaclesAvoidClient.init`

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

- 类：`unitree::robot::go2::ObstaclesAvoidClient`
- 签名：`Init()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/obstacles_avoid/obstacles_avoid_client.hpp:18`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.init()
```

<a id="unitree-sdk2-cpp-robot-go2-obstaclesavoidclient-switch-set-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ObstaclesAvoidClient.switch_set`

对应 C++ SDK 操作 `SwitchSet(bool)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def switch_set(self, enable: bool) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `enable` | `bool` | 必填 | 传给该接口的 `enable` 参数，Python 类型为 `bool`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `enable: bool`。 只接受布尔语义。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::go2::ObstaclesAvoidClient`
- 签名：`SwitchSet(bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/obstacles_avoid/obstacles_avoid_client.hpp:20`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.switch_set(enable=enable)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-obstaclesavoidclient-switch-get-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ObstaclesAvoidClient.switch_get`

对应 C++ SDK 操作 `SwitchGet(bool &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def switch_get(self) -> tuple[int, bool]
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| [0] `status` | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。 |
| [1] `enable` | `bool` | 传给该接口的 `enable` 参数，Python 类型为 `bool`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `enable: bool &`。 只接受布尔语义。 |

**对应 C++**

- 类：`unitree::robot::go2::ObstaclesAvoidClient`
- 签名：`SwitchGet(bool &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/go2/obstacles_avoid/obstacles_avoid_client.hpp:21`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
status, enable = obj.switch_get()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-obstaclesavoidclient-move-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ObstaclesAvoidClient.move`

对应 C++ SDK 操作 `Move(float, float, float)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def move(self, x: float, y: float, yaw: float) -> int
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

- 类：`unitree::robot::go2::ObstaclesAvoidClient`
- 签名：`Move(float, float, float)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/obstacles_avoid/obstacles_avoid_client.hpp:23`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.move(x=x, y=y, yaw=yaw)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-obstaclesavoidclient-use-remote-command-from-api-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ObstaclesAvoidClient.use_remote_command_from_api`

对应 C++ SDK 操作 `UseRemoteCommandFromApi(bool)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def use_remote_command_from_api(self, is_remote_commands_from_api: bool) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `is_remote_commands_from_api` | `bool` | 必填 | 传给该接口的 `is` `remote` `commands` `from` API 参数，Python 类型为 `bool`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `isRemoteCommandsFromApi: bool`。 只接受布尔语义。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::go2::ObstaclesAvoidClient`
- 签名：`UseRemoteCommandFromApi(bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/obstacles_avoid/obstacles_avoid_client.hpp:24`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.use_remote_command_from_api(is_remote_commands_from_api=is_remote_commands_from_api)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-obstaclesavoidclient-move-to-absolute-position-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ObstaclesAvoidClient.move_to_absolute_position`

对应 C++ SDK 操作 `MoveToAbsolutePosition(float, float, float)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def move_to_absolute_position(self, x: float, y: float, yaw: float) -> int
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

- 类：`unitree::robot::go2::ObstaclesAvoidClient`
- 签名：`MoveToAbsolutePosition(float, float, float)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/obstacles_avoid/obstacles_avoid_client.hpp:26`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.move_to_absolute_position(x=x, y=y, yaw=yaw)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-obstaclesavoidclient-move-to-increment-position-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ObstaclesAvoidClient.move_to_increment_position`

对应 C++ SDK 操作 `MoveToIncrementPosition(float, float, float)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def move_to_increment_position(self, x: float, y: float, yaw: float) -> int
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

- 类：`unitree::robot::go2::ObstaclesAvoidClient`
- 签名：`MoveToIncrementPosition(float, float, float)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/obstacles_avoid/obstacles_avoid_client.hpp:27`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.move_to_increment_position(x=x, y=y, yaw=yaw)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-obstaclesavoidmoveparameter"></a>
### `unitree_sdk2_cpp.robot.go2.ObstaclesAvoidMoveParameter`

SDK 请求参数值类型；当前可能仅提供设计期签名。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import ObstaclesAvoidMoveParameter
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `m_x` | `float` | 传给该接口的 `m` `x` 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.m_x` / `obj.m_x = value` |
| `m_y` | `float` | 传给该接口的 `m` `y` 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.m_y` / `obj.m_y = value` |
| `m_yaw` | `float` | 传给该接口的 `m` `yaw` 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.m_yaw` / `obj.m_yaw = value` |
| `m_mode` | `int` | 传给该接口的 `m` 模式 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.m_mode` / `obj.m_mode = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-go2-obstaclesavoidmoveparameter-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-go2-obstaclesavoidmoveparameter-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-go2-obstaclesavoidmoveparameter-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-go2-obstaclesavoidmoveparameter-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ObstaclesAvoidMoveParameter.__init__`

初始化 `ObstaclesAvoidMoveParameter` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::go2::ObstaclesAvoidMoveParameter`
- 签名：`ObstaclesAvoidMoveParameter()`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = ObstaclesAvoidMoveParameter()
```

<a id="unitree-sdk2-cpp-robot-go2-obstaclesavoidmoveparameter-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ObstaclesAvoidMoveParameter.from_json`

从 JSON 风格字典读取字段并更新当前 SDK 值对象。

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

- 类：`unitree::robot::go2::ObstaclesAvoidMoveParameter`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/go2/obstacles_avoid/obstacles_avoid_api.hpp:55`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-go2-obstaclesavoidmoveparameter-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ObstaclesAvoidMoveParameter.to_json`

把当前 SDK 值对象转换为 JSON 风格字典。

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

- 类：`unitree::robot::go2::ObstaclesAvoidMoveParameter`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/go2/obstacles_avoid/obstacles_avoid_api.hpp:63`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-go2-obstaclesavoidremotecommandsource"></a>
### `unitree_sdk2_cpp.robot.go2.ObstaclesAvoidRemoteCommandSource`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import ObstaclesAvoidRemoteCommandSource
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `m_is_remote_commands_from_api` | `bool` | 传给该接口的 `m` `is` `remote` `commands` `from` API 参数，Python 类型为 `bool`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.m_is_remote_commands_from_api` / `obj.m_is_remote_commands_from_api = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-go2-obstaclesavoidremotecommandsource-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-go2-obstaclesavoidremotecommandsource-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-go2-obstaclesavoidremotecommandsource-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-go2-obstaclesavoidremotecommandsource-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ObstaclesAvoidRemoteCommandSource.__init__`

初始化 `ObstaclesAvoidRemoteCommandSource` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::go2::ObstaclesAvoidRemoteCommandSource`
- 签名：`ObstaclesAvoidRemoteCommandSource()`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = ObstaclesAvoidRemoteCommandSource()
```

<a id="unitree-sdk2-cpp-robot-go2-obstaclesavoidremotecommandsource-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ObstaclesAvoidRemoteCommandSource.from_json`

从 JSON 风格字典读取字段并更新当前 SDK 值对象。

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

- 类：`unitree::robot::go2::ObstaclesAvoidRemoteCommandSource`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/go2/obstacles_avoid/obstacles_avoid_api.hpp:87`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-go2-obstaclesavoidremotecommandsource-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ObstaclesAvoidRemoteCommandSource.to_json`

把当前 SDK 值对象转换为 JSON 风格字典。

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

- 类：`unitree::robot::go2::ObstaclesAvoidRemoteCommandSource`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/go2/obstacles_avoid/obstacles_avoid_api.hpp:92`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-go2-obstaclesavoidswitchgetdata"></a>
### `unitree_sdk2_cpp.robot.go2.ObstaclesAvoidSwitchGetData`

SDK 数据值类型；公开字段和转换方法见下文。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import ObstaclesAvoidSwitchGetData
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `m_enable` | `bool` | 传给该接口的 `m` `enable` 参数，Python 类型为 `bool`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.m_enable` / `obj.m_enable = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-go2-obstaclesavoidswitchgetdata-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-go2-obstaclesavoidswitchgetdata-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-go2-obstaclesavoidswitchgetdata-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-go2-obstaclesavoidswitchgetdata-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ObstaclesAvoidSwitchGetData.__init__`

初始化 `ObstaclesAvoidSwitchGetData` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::go2::ObstaclesAvoidSwitchGetData`
- 签名：`ObstaclesAvoidSwitchGetData()`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = ObstaclesAvoidSwitchGetData()
```

<a id="unitree-sdk2-cpp-robot-go2-obstaclesavoidswitchgetdata-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ObstaclesAvoidSwitchGetData.from_json`

从 JSON 风格字典读取字段并更新当前 SDK 值对象。

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

- 类：`unitree::robot::go2::ObstaclesAvoidSwitchGetData`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/go2/obstacles_avoid/obstacles_avoid_api.hpp:39`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-go2-obstaclesavoidswitchgetdata-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ObstaclesAvoidSwitchGetData.to_json`

把当前 SDK 值对象转换为 JSON 风格字典。

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

- 类：`unitree::robot::go2::ObstaclesAvoidSwitchGetData`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/go2/obstacles_avoid/obstacles_avoid_api.hpp:44`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-go2-obstaclesavoidswitchsetparameter"></a>
### `unitree_sdk2_cpp.robot.go2.ObstaclesAvoidSwitchSetParameter`

SDK 请求参数值类型；当前可能仅提供设计期签名。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import ObstaclesAvoidSwitchSetParameter
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `m_enable` | `bool` | 传给该接口的 `m` `enable` 参数，Python 类型为 `bool`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.m_enable` / `obj.m_enable = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-go2-obstaclesavoidswitchsetparameter-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-go2-obstaclesavoidswitchsetparameter-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-go2-obstaclesavoidswitchsetparameter-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-go2-obstaclesavoidswitchsetparameter-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ObstaclesAvoidSwitchSetParameter.__init__`

初始化 `ObstaclesAvoidSwitchSetParameter` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::go2::ObstaclesAvoidSwitchSetParameter`
- 签名：`ObstaclesAvoidSwitchSetParameter()`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = ObstaclesAvoidSwitchSetParameter()
```

<a id="unitree-sdk2-cpp-robot-go2-obstaclesavoidswitchsetparameter-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ObstaclesAvoidSwitchSetParameter.from_json`

从 JSON 风格字典读取字段并更新当前 SDK 值对象。

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

- 类：`unitree::robot::go2::ObstaclesAvoidSwitchSetParameter`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/go2/obstacles_avoid/obstacles_avoid_api.hpp:23`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-go2-obstaclesavoidswitchsetparameter-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ObstaclesAvoidSwitchSetParameter.to_json`

把当前 SDK 值对象转换为 JSON 风格字典。

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

- 类：`unitree::robot::go2::ObstaclesAvoidSwitchSetParameter`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/go2/obstacles_avoid/obstacles_avoid_api.hpp:28`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-go2-robotstateclient"></a>
### `unitree_sdk2_cpp.robot.go2.RobotStateClient`

Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import RobotStateClient
```

**基类**：`Client`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-go2-robotstateclient-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`init`](#unitree-sdk2-cpp-robot-go2-robotstateclient-init-1) | `def init(self) -> None` | `AVAILABLE` | `INITIALIZATION` |
| [`service_list`](#unitree-sdk2-cpp-robot-go2-robotstateclient-service-list-1) | `def service_list(self) -> tuple[int, list[ServiceState]]` | `AVAILABLE` | `READ_ONLY` |
| [`service_switch`](#unitree-sdk2-cpp-robot-go2-robotstateclient-service-switch-1) | `def service_switch(self, name: str, swit: int) -> tuple[int, int]` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |
| [`set_report_freq`](#unitree-sdk2-cpp-robot-go2-robotstateclient-set-report-freq-1) | `def set_report_freq(self, interval: int, duration: int) -> int` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |

<a id="unitree-sdk2-cpp-robot-go2-robotstateclient-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.RobotStateClient.__init__`

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

- 类：`unitree::robot::go2::RobotStateClient`
- 签名：`RobotStateClient()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/go2/robot_state/robot_state_client.hpp:32`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = RobotStateClient()
```

<a id="unitree-sdk2-cpp-robot-go2-robotstateclient-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.RobotStateClient.init`

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

- 类：`unitree::robot::go2::RobotStateClient`
- 签名：`Init()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/robot_state/robot_state_client.hpp:35`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.init()
```

<a id="unitree-sdk2-cpp-robot-go2-robotstateclient-service-list-1"></a>
#### `unitree_sdk2_cpp.robot.go2.RobotStateClient.service_list`

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

- 类：`unitree::robot::go2::RobotStateClient`
- 签名：`ServiceList(std::vector<ServiceState> &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/go2/robot_state/robot_state_client.hpp:37`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, serviceStateList = obj.service_list()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-go2-robotstateclient-service-switch-1"></a>
#### `unitree_sdk2_cpp.robot.go2.RobotStateClient.service_switch`

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

- 类：`unitree::robot::go2::RobotStateClient`
- 签名：`ServiceSwitch(const std::string &, int32_t, int32_t &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/go2/robot_state/robot_state_client.hpp:38`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, status = obj.service_switch(name=name, swit=swit)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-robotstateclient-set-report-freq-1"></a>
#### `unitree_sdk2_cpp.robot.go2.RobotStateClient.set_report_freq`

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

- 类：`unitree::robot::go2::RobotStateClient`
- 签名：`SetReportFreq(int32_t, int32_t)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/robot_state/robot_state_client.hpp:39`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.set_report_freq(interval=interval, duration=duration)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-servicestate"></a>
### `unitree_sdk2_cpp.robot.go2.ServiceState`

SDK 数据值类型；公开字段和转换方法见下文。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import ServiceState
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
| [`__init__`](#unitree-sdk2-cpp-robot-go2-servicestate-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |

<a id="unitree-sdk2-cpp-robot-go2-servicestate-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ServiceState.__init__`

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

- 类：`unitree::robot::go2::ServiceState`
- 签名：`ServiceState()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/go2/robot_state/robot_state_client.hpp:18`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = ServiceState()
```

<a id="unitree-sdk2-cpp-robot-go2-servicestatedata"></a>
### `unitree_sdk2_cpp.robot.go2.ServiceStateData`

SDK 数据值类型；公开字段和转换方法见下文。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import ServiceStateData
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
| [`__init__`](#unitree-sdk2-cpp-robot-go2-servicestatedata-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-go2-servicestatedata-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-go2-servicestatedata-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-go2-servicestatedata-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ServiceStateData.__init__`

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

- 类：`unitree::robot::go2::ServiceStateData`
- 签名：`ServiceStateData()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/go2/robot_state/robot_state_api.hpp:122`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = ServiceStateData()
```

<a id="unitree-sdk2-cpp-robot-go2-servicestatedata-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ServiceStateData.from_json`

从 JSON 风格字典读取字段并更新当前 SDK 值对象。

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

- 类：`unitree::robot::go2::ServiceStateData`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/go2/robot_state/robot_state_api.hpp:128`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-go2-servicestatedata-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ServiceStateData.to_json`

把当前 SDK 值对象转换为 JSON 风格字典。

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

- 类：`unitree::robot::go2::ServiceStateData`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/go2/robot_state/robot_state_api.hpp:135`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-go2-serviceswitchdata"></a>
### `unitree_sdk2_cpp.robot.go2.ServiceSwitchData`

SDK 数据值类型；公开字段和转换方法见下文。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import ServiceSwitchData
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
| [`__init__`](#unitree-sdk2-cpp-robot-go2-serviceswitchdata-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-go2-serviceswitchdata-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-go2-serviceswitchdata-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-go2-serviceswitchdata-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ServiceSwitchData.__init__`

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

- 类：`unitree::robot::go2::ServiceSwitchData`
- 签名：`ServiceSwitchData()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/go2/robot_state/robot_state_api.hpp:64`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = ServiceSwitchData()
```

<a id="unitree-sdk2-cpp-robot-go2-serviceswitchdata-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ServiceSwitchData.from_json`

从 JSON 风格字典读取字段并更新当前 SDK 值对象。

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

- 类：`unitree::robot::go2::ServiceSwitchData`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/go2/robot_state/robot_state_api.hpp:70`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-go2-serviceswitchdata-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ServiceSwitchData.to_json`

把当前 SDK 值对象转换为 JSON 风格字典。

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

- 类：`unitree::robot::go2::ServiceSwitchData`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/go2/robot_state/robot_state_api.hpp:76`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-go2-serviceswitchparameter"></a>
### `unitree_sdk2_cpp.robot.go2.ServiceSwitchParameter`

SDK 请求参数值类型；当前可能仅提供设计期签名。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import ServiceSwitchParameter
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
| [`__init__`](#unitree-sdk2-cpp-robot-go2-serviceswitchparameter-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-go2-serviceswitchparameter-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-go2-serviceswitchparameter-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-go2-serviceswitchparameter-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ServiceSwitchParameter.__init__`

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

- 类：`unitree::robot::go2::ServiceSwitchParameter`
- 签名：`ServiceSwitchParameter()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/go2/robot_state/robot_state_api.hpp:35`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = ServiceSwitchParameter()
```

<a id="unitree-sdk2-cpp-robot-go2-serviceswitchparameter-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ServiceSwitchParameter.from_json`

从 JSON 风格字典读取字段并更新当前 SDK 值对象。

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

- 类：`unitree::robot::go2::ServiceSwitchParameter`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/go2/robot_state/robot_state_api.hpp:41`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-go2-serviceswitchparameter-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.ServiceSwitchParameter.to_json`

把当前 SDK 值对象转换为 JSON 风格字典。

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

- 类：`unitree::robot::go2::ServiceSwitchParameter`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/go2/robot_state/robot_state_api.hpp:47`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-go2-setreportfreqparameter"></a>
### `unitree_sdk2_cpp.robot.go2.SetReportFreqParameter`

SDK 请求参数值类型；当前可能仅提供设计期签名。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import SetReportFreqParameter
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
| [`__init__`](#unitree-sdk2-cpp-robot-go2-setreportfreqparameter-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-go2-setreportfreqparameter-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-go2-setreportfreqparameter-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-go2-setreportfreqparameter-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SetReportFreqParameter.__init__`

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

- 类：`unitree::robot::go2::SetReportFreqParameter`
- 签名：`SetReportFreqParameter()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/go2/robot_state/robot_state_api.hpp:93`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = SetReportFreqParameter()
```

<a id="unitree-sdk2-cpp-robot-go2-setreportfreqparameter-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SetReportFreqParameter.from_json`

从 JSON 风格字典读取字段并更新当前 SDK 值对象。

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

- 类：`unitree::robot::go2::SetReportFreqParameter`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/go2/robot_state/robot_state_api.hpp:99`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-go2-setreportfreqparameter-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SetReportFreqParameter.to_json`

把当前 SDK 值对象转换为 JSON 风格字典。

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

- 类：`unitree::robot::go2::SetReportFreqParameter`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/go2/robot_state/robot_state_api.hpp:105`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-go2-sportclient"></a>
### `unitree_sdk2_cpp.robot.go2.SportClient`

Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import SportClient
```

**基类**：`Client`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-go2-sportclient-dunder-init-1) | `def __init__(self, enable_lease: bool = False) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`init`](#unitree-sdk2-cpp-robot-go2-sportclient-init-1) | `def init(self) -> None` | `AVAILABLE` | `INITIALIZATION` |
| [`damp`](#unitree-sdk2-cpp-robot-go2-sportclient-damp-1) | `def damp(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`balance_stand`](#unitree-sdk2-cpp-robot-go2-sportclient-balance-stand-1) | `def balance_stand(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`stop_move`](#unitree-sdk2-cpp-robot-go2-sportclient-stop-move-1) | `def stop_move(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`stand_up`](#unitree-sdk2-cpp-robot-go2-sportclient-stand-up-1) | `def stand_up(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`stand_down`](#unitree-sdk2-cpp-robot-go2-sportclient-stand-down-1) | `def stand_down(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`recovery_stand`](#unitree-sdk2-cpp-robot-go2-sportclient-recovery-stand-1) | `def recovery_stand(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`euler`](#unitree-sdk2-cpp-robot-go2-sportclient-euler-1) | `def euler(self, roll: float, pitch: float, yaw: float) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`move`](#unitree-sdk2-cpp-robot-go2-sportclient-move-1) | `def move(self, vx: float, vy: float, vyaw: float) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`sit`](#unitree-sdk2-cpp-robot-go2-sportclient-sit-1) | `def sit(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`rise_sit`](#unitree-sdk2-cpp-robot-go2-sportclient-rise-sit-1) | `def rise_sit(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`speed_level`](#unitree-sdk2-cpp-robot-go2-sportclient-speed-level-1) | `def speed_level(self, level: int) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`hello`](#unitree-sdk2-cpp-robot-go2-sportclient-hello-1) | `def hello(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`stretch`](#unitree-sdk2-cpp-robot-go2-sportclient-stretch-1) | `def stretch(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`switch_joystick`](#unitree-sdk2-cpp-robot-go2-sportclient-switch-joystick-1) | `def switch_joystick(self, flag: bool) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`content`](#unitree-sdk2-cpp-robot-go2-sportclient-content-1) | `def content(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`heart`](#unitree-sdk2-cpp-robot-go2-sportclient-heart-1) | `def heart(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`pose`](#unitree-sdk2-cpp-robot-go2-sportclient-pose-1) | `def pose(self, flag: bool) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`scrape`](#unitree-sdk2-cpp-robot-go2-sportclient-scrape-1) | `def scrape(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`front_flip`](#unitree-sdk2-cpp-robot-go2-sportclient-front-flip-1) | `def front_flip(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`front_jump`](#unitree-sdk2-cpp-robot-go2-sportclient-front-jump-1) | `def front_jump(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`front_pounce`](#unitree-sdk2-cpp-robot-go2-sportclient-front-pounce-1) | `def front_pounce(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`dance1`](#unitree-sdk2-cpp-robot-go2-sportclient-dance1-1) | `def dance1(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`dance2`](#unitree-sdk2-cpp-robot-go2-sportclient-dance2-1) | `def dance2(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`left_flip`](#unitree-sdk2-cpp-robot-go2-sportclient-left-flip-1) | `def left_flip(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`back_flip`](#unitree-sdk2-cpp-robot-go2-sportclient-back-flip-1) | `def back_flip(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`hand_stand`](#unitree-sdk2-cpp-robot-go2-sportclient-hand-stand-1) | `def hand_stand(self, flag: bool) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`free_walk`](#unitree-sdk2-cpp-robot-go2-sportclient-free-walk-1) | `def free_walk(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`free_bound`](#unitree-sdk2-cpp-robot-go2-sportclient-free-bound-1) | `def free_bound(self, flag: bool) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`free_jump`](#unitree-sdk2-cpp-robot-go2-sportclient-free-jump-1) | `def free_jump(self, flag: bool) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`free_avoid`](#unitree-sdk2-cpp-robot-go2-sportclient-free-avoid-1) | `def free_avoid(self, flag: bool) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`classic_walk`](#unitree-sdk2-cpp-robot-go2-sportclient-classic-walk-1) | `def classic_walk(self, flag: bool) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`walk_upright`](#unitree-sdk2-cpp-robot-go2-sportclient-walk-upright-1) | `def walk_upright(self, flag: bool) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`cross_step`](#unitree-sdk2-cpp-robot-go2-sportclient-cross-step-1) | `def cross_step(self, flag: bool) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`auto_recover_set`](#unitree-sdk2-cpp-robot-go2-sportclient-auto-recover-set-1) | `def auto_recover_set(self, flag: bool) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`auto_recover_get`](#unitree-sdk2-cpp-robot-go2-sportclient-auto-recover-get-1) | `def auto_recover_get(self) -> tuple[int, bool]` | `AVAILABLE` | `MOTION_COMMAND` |
| [`static_walk`](#unitree-sdk2-cpp-robot-go2-sportclient-static-walk-1) | `def static_walk(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`trot_run`](#unitree-sdk2-cpp-robot-go2-sportclient-trot-run-1) | `def trot_run(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`economic_gait`](#unitree-sdk2-cpp-robot-go2-sportclient-economic-gait-1) | `def economic_gait(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`switch_avoid_mode`](#unitree-sdk2-cpp-robot-go2-sportclient-switch-avoid-mode-1) | `def switch_avoid_mode(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |

<a id="unitree-sdk2-cpp-robot-go2-sportclient-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.__init__`

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

- 类：`unitree::robot::go2::SportClient`
- 签名：`SportClient(bool)`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:34`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = SportClient(enable_lease=enable_lease)
```

<a id="unitree-sdk2-cpp-robot-go2-sportclient-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.init`

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

- 类：`unitree::robot::go2::SportClient`
- 签名：`Init()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:37`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.init()
```

<a id="unitree-sdk2-cpp-robot-go2-sportclient-damp-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.damp`

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

- 类：`unitree::robot::go2::SportClient`
- 签名：`Damp()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:39`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.damp()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-balance-stand-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.balance_stand`

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

- 类：`unitree::robot::go2::SportClient`
- 签名：`BalanceStand()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:40`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.balance_stand()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-stop-move-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.stop_move`

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

- 类：`unitree::robot::go2::SportClient`
- 签名：`StopMove()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:41`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.stop_move()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-stand-up-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.stand_up`

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

- 类：`unitree::robot::go2::SportClient`
- 签名：`StandUp()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:42`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.stand_up()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-stand-down-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.stand_down`

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

- 类：`unitree::robot::go2::SportClient`
- 签名：`StandDown()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:43`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.stand_down()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-recovery-stand-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.recovery_stand`

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

- 类：`unitree::robot::go2::SportClient`
- 签名：`RecoveryStand()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:44`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.recovery_stand()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-euler-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.euler`

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

- 类：`unitree::robot::go2::SportClient`
- 签名：`Euler(float, float, float)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:45`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.euler(roll=roll, pitch=pitch, yaw=yaw)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-move-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.move`

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

- 类：`unitree::robot::go2::SportClient`
- 签名：`Move(float, float, float)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:46`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.move(vx=vx, vy=vy, vyaw=vyaw)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-sit-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.sit`

对应 C++ SDK 操作 `Sit()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def sit(self) -> int
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

- 类：`unitree::robot::go2::SportClient`
- 签名：`Sit()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:47`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.sit()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-rise-sit-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.rise_sit`

对应 C++ SDK 操作 `RiseSit()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def rise_sit(self) -> int
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

- 类：`unitree::robot::go2::SportClient`
- 签名：`RiseSit()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:48`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.rise_sit()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-speed-level-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.speed_level`

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

- 类：`unitree::robot::go2::SportClient`
- 签名：`SpeedLevel(int)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:49`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.speed_level(level=level)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-hello-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.hello`

对应 C++ SDK 操作 `Hello()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def hello(self) -> int
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

- 类：`unitree::robot::go2::SportClient`
- 签名：`Hello()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:50`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.hello()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-stretch-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.stretch`

对应 C++ SDK 操作 `Stretch()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def stretch(self) -> int
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

- 类：`unitree::robot::go2::SportClient`
- 签名：`Stretch()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:51`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.stretch()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-switch-joystick-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.switch_joystick`

对应 C++ SDK 操作 `SwitchJoystick(bool)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def switch_joystick(self, flag: bool) -> int
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

- 类：`unitree::robot::go2::SportClient`
- 签名：`SwitchJoystick(bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:52`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.switch_joystick(flag=flag)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-content-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.content`

对应 C++ SDK 操作 `Content()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def content(self) -> int
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

- 类：`unitree::robot::go2::SportClient`
- 签名：`Content()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:53`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.content()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-heart-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.heart`

对应 C++ SDK 操作 `Heart()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def heart(self) -> int
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

- 类：`unitree::robot::go2::SportClient`
- 签名：`Heart()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:54`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.heart()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-pose-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.pose`

对应 C++ SDK 操作 `Pose(bool)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def pose(self, flag: bool) -> int
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

- 类：`unitree::robot::go2::SportClient`
- 签名：`Pose(bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:55`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.pose(flag=flag)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-scrape-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.scrape`

对应 C++ SDK 操作 `Scrape()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def scrape(self) -> int
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

- 类：`unitree::robot::go2::SportClient`
- 签名：`Scrape()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:56`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.scrape()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-front-flip-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.front_flip`

对应 C++ SDK 操作 `FrontFlip()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def front_flip(self) -> int
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

- 类：`unitree::robot::go2::SportClient`
- 签名：`FrontFlip()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:57`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.front_flip()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-front-jump-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.front_jump`

对应 C++ SDK 操作 `FrontJump()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def front_jump(self) -> int
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

- 类：`unitree::robot::go2::SportClient`
- 签名：`FrontJump()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:58`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.front_jump()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-front-pounce-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.front_pounce`

对应 C++ SDK 操作 `FrontPounce()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def front_pounce(self) -> int
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

- 类：`unitree::robot::go2::SportClient`
- 签名：`FrontPounce()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:59`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.front_pounce()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-dance1-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.dance1`

对应 C++ SDK 操作 `Dance1()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def dance1(self) -> int
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

- 类：`unitree::robot::go2::SportClient`
- 签名：`Dance1()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:60`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.dance1()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-dance2-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.dance2`

对应 C++ SDK 操作 `Dance2()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def dance2(self) -> int
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

- 类：`unitree::robot::go2::SportClient`
- 签名：`Dance2()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:61`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.dance2()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-left-flip-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.left_flip`

对应 C++ SDK 操作 `LeftFlip()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def left_flip(self) -> int
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

- 类：`unitree::robot::go2::SportClient`
- 签名：`LeftFlip()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:62`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.left_flip()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-back-flip-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.back_flip`

对应 C++ SDK 操作 `BackFlip()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def back_flip(self) -> int
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

- 类：`unitree::robot::go2::SportClient`
- 签名：`BackFlip()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:63`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.back_flip()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-hand-stand-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.hand_stand`

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

- 类：`unitree::robot::go2::SportClient`
- 签名：`HandStand(bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:64`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.hand_stand(flag=flag)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-free-walk-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.free_walk`

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

- 类：`unitree::robot::go2::SportClient`
- 签名：`FreeWalk()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:65`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.free_walk()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-free-bound-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.free_bound`

对应 C++ SDK 操作 `FreeBound(bool)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def free_bound(self, flag: bool) -> int
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

- 类：`unitree::robot::go2::SportClient`
- 签名：`FreeBound(bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:66`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.free_bound(flag=flag)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-free-jump-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.free_jump`

对应 C++ SDK 操作 `FreeJump(bool)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def free_jump(self, flag: bool) -> int
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

- 类：`unitree::robot::go2::SportClient`
- 签名：`FreeJump(bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:67`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.free_jump(flag=flag)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-free-avoid-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.free_avoid`

对应 C++ SDK 操作 `FreeAvoid(bool)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def free_avoid(self, flag: bool) -> int
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

- 类：`unitree::robot::go2::SportClient`
- 签名：`FreeAvoid(bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:68`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.free_avoid(flag=flag)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-classic-walk-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.classic_walk`

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

- 类：`unitree::robot::go2::SportClient`
- 签名：`ClassicWalk(bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:69`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.classic_walk(flag=flag)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-walk-upright-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.walk_upright`

对应 C++ SDK 操作 `WalkUpright(bool)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def walk_upright(self, flag: bool) -> int
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

- 类：`unitree::robot::go2::SportClient`
- 签名：`WalkUpright(bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:70`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.walk_upright(flag=flag)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-cross-step-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.cross_step`

对应 C++ SDK 操作 `CrossStep(bool)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def cross_step(self, flag: bool) -> int
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

- 类：`unitree::robot::go2::SportClient`
- 签名：`CrossStep(bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:71`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.cross_step(flag=flag)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-auto-recover-set-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.auto_recover_set`

对应 C++ SDK 操作 `AutoRecoverSet(bool)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def auto_recover_set(self, flag: bool) -> int
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

- 类：`unitree::robot::go2::SportClient`
- 签名：`AutoRecoverSet(bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:72`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.auto_recover_set(flag=flag)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-auto-recover-get-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.auto_recover_get`

对应 C++ SDK 操作 `AutoRecoverGet(bool &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def auto_recover_get(self) -> tuple[int, bool]
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| [0] `status` | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。 |
| [1] `flag` | `bool` | 布尔开关。`True` 和 `False` 的具体业务效果由当前方法定义。 对应 C++ 参数 `flag: bool &`。 只接受布尔语义。 |

**对应 C++**

- 类：`unitree::robot::go2::SportClient`
- 签名：`AutoRecoverGet(bool &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:73`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
status, flag = obj.auto_recover_get()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-static-walk-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.static_walk`

对应 C++ SDK 操作 `StaticWalk()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def static_walk(self) -> int
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

- 类：`unitree::robot::go2::SportClient`
- 签名：`StaticWalk()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:74`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.static_walk()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-trot-run-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.trot_run`

对应 C++ SDK 操作 `TrotRun()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def trot_run(self) -> int
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

- 类：`unitree::robot::go2::SportClient`
- 签名：`TrotRun()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:75`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.trot_run()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-economic-gait-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.economic_gait`

对应 C++ SDK 操作 `EconomicGait()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def economic_gait(self) -> int
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

- 类：`unitree::robot::go2::SportClient`
- 签名：`EconomicGait()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:76`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.economic_gait()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-sportclient-switch-avoid-mode-1"></a>
#### `unitree_sdk2_cpp.robot.go2.SportClient.switch_avoid_mode`

对应 C++ SDK 操作 `SwitchAvoidMode()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def switch_avoid_mode(self) -> int
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

- 类：`unitree::robot::go2::SportClient`
- 签名：`SwitchAvoidMode()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/sport/sport_client.hpp:77`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.switch_avoid_mode()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-utrackclient"></a>
### `unitree_sdk2_cpp.robot.go2.UtrackClient`

Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import UtrackClient
```

**基类**：`Client`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-go2-utrackclient-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`init`](#unitree-sdk2-cpp-robot-go2-utrackclient-init-1) | `def init(self) -> None` | `AVAILABLE` | `INITIALIZATION` |
| [`switch_set`](#unitree-sdk2-cpp-robot-go2-utrackclient-switch-set-1) | `def switch_set(self, enable: bool) -> int` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |
| [`switch_get`](#unitree-sdk2-cpp-robot-go2-utrackclient-switch-get-1) | `def switch_get(self) -> tuple[int, bool]` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |
| [`is_tracking`](#unitree-sdk2-cpp-robot-go2-utrackclient-is-tracking-1) | `def is_tracking(self) -> tuple[int, bool]` | `AVAILABLE` | `READ_ONLY` |

<a id="unitree-sdk2-cpp-robot-go2-utrackclient-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.UtrackClient.__init__`

初始化 `UtrackClient` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::go2::UtrackClient`
- 签名：`UtrackClient()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/go2/utrack/utrack_client.hpp:15`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = UtrackClient()
```

<a id="unitree-sdk2-cpp-robot-go2-utrackclient-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.UtrackClient.init`

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

- 类：`unitree::robot::go2::UtrackClient`
- 签名：`Init()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/utrack/utrack_client.hpp:18`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.init()
```

<a id="unitree-sdk2-cpp-robot-go2-utrackclient-switch-set-1"></a>
#### `unitree_sdk2_cpp.robot.go2.UtrackClient.switch_set`

对应 C++ SDK 操作 `SwitchSet(bool)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def switch_set(self, enable: bool) -> int
```

**可用性与安全性**

**`AVAILABLE` / `HARDWARE_SIDE_EFFECT`**：当前绑定源码已实现，调用可能修改机器人或服务状态、启动订阅或产生网络副作用。必须显式检查目标设备和返回状态。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `enable` | `bool` | 必填 | 传给该接口的 `enable` 参数，Python 类型为 `bool`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `enable: bool`。 只接受布尔语义。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::go2::UtrackClient`
- 签名：`SwitchSet(bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/utrack/utrack_client.hpp:20`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.switch_set(enable=enable)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-utrackclient-switch-get-1"></a>
#### `unitree_sdk2_cpp.robot.go2.UtrackClient.switch_get`

对应 C++ SDK 操作 `SwitchGet(bool &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def switch_get(self) -> tuple[int, bool]
```

**可用性与安全性**

**`AVAILABLE` / `HARDWARE_SIDE_EFFECT`**：当前绑定源码已实现，调用可能修改机器人或服务状态、启动订阅或产生网络副作用。必须显式检查目标设备和返回状态。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| [0] `status` | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。 |
| [1] `enable` | `bool` | 传给该接口的 `enable` 参数，Python 类型为 `bool`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `enable: bool &`。 只接受布尔语义。 |

**对应 C++**

- 类：`unitree::robot::go2::UtrackClient`
- 签名：`SwitchGet(bool &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/go2/utrack/utrack_client.hpp:21`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, enable = obj.switch_get()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-utrackclient-is-tracking-1"></a>
#### `unitree_sdk2_cpp.robot.go2.UtrackClient.is_tracking`

查询或检查 `tracking`。

**签名**

```python
def is_tracking(self) -> tuple[int, bool]
```

**可用性与安全性**

**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现只读查询。Robot Client 的服务端查询通常仍需匹配的 Linux 扩展、DDS、网络、机器人和服务；纯本地 getter 则不一定需要全部条件。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| [0] `status` | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。 |
| [1] `enable` | `bool` | 传给该接口的 `enable` 参数，Python 类型为 `bool`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `enable: bool &`。 只接受布尔语义。 |

**对应 C++**

- 类：`unitree::robot::go2::UtrackClient`
- 签名：`IsTracking(bool &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/go2/utrack/utrack_client.hpp:22`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, enable = obj.is_tracking()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-go2-utrackswitchgetdata"></a>
### `unitree_sdk2_cpp.robot.go2.UtrackSwitchGetData`

SDK 数据值类型；公开字段和转换方法见下文。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import UtrackSwitchGetData
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `m_enable` | `int` | 传给该接口的 `m` `enable` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.m_enable` / `obj.m_enable = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-go2-utrackswitchgetdata-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-go2-utrackswitchgetdata-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-go2-utrackswitchgetdata-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-go2-utrackswitchgetdata-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.UtrackSwitchGetData.__init__`

初始化 `UtrackSwitchGetData` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::go2::UtrackSwitchGetData`
- 签名：`UtrackSwitchGetData()`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = UtrackSwitchGetData()
```

<a id="unitree-sdk2-cpp-robot-go2-utrackswitchgetdata-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.UtrackSwitchGetData.from_json`

从 JSON 风格字典读取字段并更新当前 SDK 值对象。

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

- 类：`unitree::robot::go2::UtrackSwitchGetData`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/go2/utrack/utrack_api.hpp:38`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-go2-utrackswitchgetdata-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.UtrackSwitchGetData.to_json`

把当前 SDK 值对象转换为 JSON 风格字典。

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

- 类：`unitree::robot::go2::UtrackSwitchGetData`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/go2/utrack/utrack_api.hpp:43`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-go2-utrackswitchsetparameter"></a>
### `unitree_sdk2_cpp.robot.go2.UtrackSwitchSetParameter`

SDK 请求参数值类型；当前可能仅提供设计期签名。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import UtrackSwitchSetParameter
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `m_enable` | `int` | 传给该接口的 `m` `enable` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.m_enable` / `obj.m_enable = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-go2-utrackswitchsetparameter-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-go2-utrackswitchsetparameter-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-go2-utrackswitchsetparameter-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-go2-utrackswitchsetparameter-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.UtrackSwitchSetParameter.__init__`

初始化 `UtrackSwitchSetParameter` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::go2::UtrackSwitchSetParameter`
- 签名：`UtrackSwitchSetParameter()`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = UtrackSwitchSetParameter()
```

<a id="unitree-sdk2-cpp-robot-go2-utrackswitchsetparameter-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.UtrackSwitchSetParameter.from_json`

从 JSON 风格字典读取字段并更新当前 SDK 值对象。

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

- 类：`unitree::robot::go2::UtrackSwitchSetParameter`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/go2/utrack/utrack_api.hpp:22`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-go2-utrackswitchsetparameter-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.go2.UtrackSwitchSetParameter.to_json`

把当前 SDK 值对象转换为 JSON 风格字典。

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

- 类：`unitree::robot::go2::UtrackSwitchSetParameter`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/go2/utrack/utrack_api.hpp:27`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-go2-videoclient"></a>
### `unitree_sdk2_cpp.robot.go2.VideoClient`

Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import VideoClient
```

**基类**：`Client`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-go2-videoclient-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`init`](#unitree-sdk2-cpp-robot-go2-videoclient-init-1) | `def init(self) -> None` | `AVAILABLE` | `INITIALIZATION` |
| [`get_image_sample`](#unitree-sdk2-cpp-robot-go2-videoclient-get-image-sample-1) | `def get_image_sample(self) -> tuple[int, list[int]]` | `AVAILABLE` | `READ_ONLY` |

<a id="unitree-sdk2-cpp-robot-go2-videoclient-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.VideoClient.__init__`

初始化 `VideoClient` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::go2::VideoClient`
- 签名：`VideoClient()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/go2/video/video_client.hpp:18`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = VideoClient()
```

<a id="unitree-sdk2-cpp-robot-go2-videoclient-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.VideoClient.init`

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

- 类：`unitree::robot::go2::VideoClient`
- 签名：`Init()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/video/video_client.hpp:21`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.init()
```

<a id="unitree-sdk2-cpp-robot-go2-videoclient-get-image-sample-1"></a>
#### `unitree_sdk2_cpp.robot.go2.VideoClient.get_image_sample`

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

- 类：`unitree::robot::go2::VideoClient`
- 签名：`GetImageSample(std::vector<uint8_t> &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/go2/video/video_client.hpp:27`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, output_1 = obj.get_image_sample()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-go2-vuiclient"></a>
### `unitree_sdk2_cpp.robot.go2.VuiClient`

Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import VuiClient
```

**基类**：`Client`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-go2-vuiclient-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`init`](#unitree-sdk2-cpp-robot-go2-vuiclient-init-1) | `def init(self) -> None` | `AVAILABLE` | `INITIALIZATION` |
| [`set_switch`](#unitree-sdk2-cpp-robot-go2-vuiclient-set-switch-1) | `def set_switch(self, enable: int) -> int` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |
| [`get_switch`](#unitree-sdk2-cpp-robot-go2-vuiclient-get-switch-1) | `def get_switch(self) -> tuple[int, int]` | `AVAILABLE` | `READ_ONLY` |
| [`set_volume`](#unitree-sdk2-cpp-robot-go2-vuiclient-set-volume-1) | `def set_volume(self, level: int) -> int` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |
| [`get_volume`](#unitree-sdk2-cpp-robot-go2-vuiclient-get-volume-1) | `def get_volume(self) -> tuple[int, int]` | `AVAILABLE` | `READ_ONLY` |
| [`set_brightness`](#unitree-sdk2-cpp-robot-go2-vuiclient-set-brightness-1) | `def set_brightness(self, level: int) -> int` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |
| [`get_brightness`](#unitree-sdk2-cpp-robot-go2-vuiclient-get-brightness-1) | `def get_brightness(self) -> tuple[int, int]` | `AVAILABLE` | `READ_ONLY` |

<a id="unitree-sdk2-cpp-robot-go2-vuiclient-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.VuiClient.__init__`

初始化 `VuiClient` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::go2::VuiClient`
- 签名：`VuiClient()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/go2/vui/vui_client.hpp:18`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = VuiClient()
```

<a id="unitree-sdk2-cpp-robot-go2-vuiclient-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.VuiClient.init`

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

- 类：`unitree::robot::go2::VuiClient`
- 签名：`Init()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/vui/vui_client.hpp:21`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.init()
```

<a id="unitree-sdk2-cpp-robot-go2-vuiclient-set-switch-1"></a>
#### `unitree_sdk2_cpp.robot.go2.VuiClient.set_switch`

设置 开关。具体副作用和安全边界见下方状态。

**签名**

```python
def set_switch(self, enable: int) -> int
```

**可用性与安全性**

**`AVAILABLE` / `HARDWARE_SIDE_EFFECT`**：当前绑定源码已实现，调用可能修改机器人或服务状态、启动订阅或产生网络副作用。必须显式检查目标设备和返回状态。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `enable` | `int` | 必填 | 传给该接口的 `enable` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `enable: int`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::go2::VuiClient`
- 签名：`SetSwitch(int)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/vui/vui_client.hpp:27`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.set_switch(enable=enable)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-vuiclient-get-switch-1"></a>
#### `unitree_sdk2_cpp.robot.go2.VuiClient.get_switch`

查询或检查 开关。

**签名**

```python
def get_switch(self) -> tuple[int, int]
```

**可用性与安全性**

**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现只读查询。Robot Client 的服务端查询通常仍需匹配的 Linux 扩展、DDS、网络、机器人和服务；纯本地 getter 则不一定需要全部条件。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| [0] `status` | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。 |
| [1] `output_1` | `int` | 传给该接口的 `output` `1` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `output_1: int &`。 |

**对应 C++**

- 类：`unitree::robot::go2::VuiClient`
- 签名：`GetSwitch(int &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/go2/vui/vui_client.hpp:33`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, output_1 = obj.get_switch()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-go2-vuiclient-set-volume-1"></a>
#### `unitree_sdk2_cpp.robot.go2.VuiClient.set_volume`

设置 音量。具体副作用和安全边界见下方状态。

**签名**

```python
def set_volume(self, level: int) -> int
```

**可用性与安全性**

**`AVAILABLE` / `HARDWARE_SIDE_EFFECT`**：当前绑定源码已实现，调用可能修改机器人或服务状态、启动订阅或产生网络副作用。必须显式检查目标设备和返回状态。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `level` | `int` | 必填 | 传给该接口的 `level` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `level: int`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::go2::VuiClient`
- 签名：`SetVolume(int)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/vui/vui_client.hpp:39`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.set_volume(level=level)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-vuiclient-get-volume-1"></a>
#### `unitree_sdk2_cpp.robot.go2.VuiClient.get_volume`

查询或检查 音量。

**签名**

```python
def get_volume(self) -> tuple[int, int]
```

**可用性与安全性**

**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现只读查询。Robot Client 的服务端查询通常仍需匹配的 Linux 扩展、DDS、网络、机器人和服务；纯本地 getter 则不一定需要全部条件。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| [0] `status` | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。 |
| [1] `output_1` | `int` | 传给该接口的 `output` `1` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `output_1: int &`。 |

**对应 C++**

- 类：`unitree::robot::go2::VuiClient`
- 签名：`GetVolume(int &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/go2/vui/vui_client.hpp:45`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, output_1 = obj.get_volume()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-go2-vuiclient-set-brightness-1"></a>
#### `unitree_sdk2_cpp.robot.go2.VuiClient.set_brightness`

设置 亮度。具体副作用和安全边界见下方状态。

**签名**

```python
def set_brightness(self, level: int) -> int
```

**可用性与安全性**

**`AVAILABLE` / `HARDWARE_SIDE_EFFECT`**：当前绑定源码已实现，调用可能修改机器人或服务状态、启动订阅或产生网络副作用。必须显式检查目标设备和返回状态。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `level` | `int` | 必填 | 传给该接口的 `level` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `level: int`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::go2::VuiClient`
- 签名：`SetBrightness(int)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/go2/vui/vui_client.hpp:51`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.set_brightness(level=level)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-go2-vuiclient-get-brightness-1"></a>
#### `unitree_sdk2_cpp.robot.go2.VuiClient.get_brightness`

查询或检查 亮度。

**签名**

```python
def get_brightness(self) -> tuple[int, int]
```

**可用性与安全性**

**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现只读查询。Robot Client 的服务端查询通常仍需匹配的 Linux 扩展、DDS、网络、机器人和服务；纯本地 getter 则不一定需要全部条件。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| [0] `status` | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。 |
| [1] `output_1` | `int` | 传给该接口的 `output` `1` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `output_1: int &`。 |

**对应 C++**

- 类：`unitree::robot::go2::VuiClient`
- 签名：`GetBrightness(int &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/go2/vui/vui_client.hpp:57`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, output_1 = obj.get_brightness()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-go2-stpathpoint"></a>
### `unitree_sdk2_cpp.robot.go2.stPathPoint`

SDK 数据值类型；公开字段和转换方法见下文。

**导入**

```python
from unitree_sdk2_cpp.robot.go2 import stPathPoint
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
| [`__init__`](#unitree-sdk2-cpp-robot-go2-stpathpoint-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |

<a id="unitree-sdk2-cpp-robot-go2-stpathpoint-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.go2.stPathPoint.__init__`

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

- 类：`unitree::robot::go2::stPathPoint`
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
