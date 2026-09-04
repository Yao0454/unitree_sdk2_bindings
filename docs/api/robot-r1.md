# Unitree SDK2 Python API 参考分卷

[返回 API 总索引](../API_REFERENCE_ZH.md) · [阅读从零开始指南](../BEGINNER_GUIDE_ZH.md)

> [!WARNING]
> 本分卷同时包含 `AVAILABLE` 和 `SIGNATURE_ONLY`。后者只是设计期类型签名。运动及硬件副作用方法即使标记为 `AVAILABLE`，也不表示当前环境可安全执行。

> [!NOTE]
> 本文件由 `generator/generate_api_docs.py` 自动生成，请勿手工维护 API 条目。

---

<a id="unitree-sdk2-cpp-robot-r1"></a>
## R1 Robot API

模块：`unitree_sdk2_cpp.robot.r1`

### 类索引

| 类 | 公开函数签名 | 属性 |
| --- | ---: | ---: |
| [`AudioClient`](#unitree-sdk2-cpp-robot-r1-audioclient) | 8 | 0 |
| [`JsonizeDataVecFloat`](#unitree-sdk2-cpp-robot-r1-jsonizedatavecfloat) | 3 | 0 |
| [`JsonizeVelocityCommand`](#unitree-sdk2-cpp-robot-r1-jsonizevelocitycommand) | 3 | 0 |
| [`LedControlParameter`](#unitree-sdk2-cpp-robot-r1-ledcontrolparameter) | 3 | 0 |
| [`LocoClient`](#unitree-sdk2-cpp-robot-r1-lococlient) | 15 | 0 |
| [`PlayStopParameter`](#unitree-sdk2-cpp-robot-r1-playstopparameter) | 3 | 0 |
| [`PlayStreamParameter`](#unitree-sdk2-cpp-robot-r1-playstreamparameter) | 3 | 0 |
| [`TtsMakerParameter`](#unitree-sdk2-cpp-robot-r1-ttsmakerparameter) | 3 | 0 |

<a id="unitree-sdk2-cpp-robot-r1-audioclient"></a>
### `unitree_sdk2_cpp.robot.r1.AudioClient`

Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

**导入**

```python
from unitree_sdk2_cpp.robot.r1 import AudioClient
```

**基类**：`Client`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-r1-audioclient-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`init`](#unitree-sdk2-cpp-robot-r1-audioclient-init-1) | `def init(self) -> None` | `AVAILABLE` | `INITIALIZATION` |
| [`tts_maker`](#unitree-sdk2-cpp-robot-r1-audioclient-tts-maker-1) | `def tts_maker(self, text: str, speaker_id: int) -> int` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |
| [`get_volume`](#unitree-sdk2-cpp-robot-r1-audioclient-get-volume-1) | `def get_volume(self) -> tuple[int, int]` | `AVAILABLE` | `READ_ONLY` |
| [`set_volume`](#unitree-sdk2-cpp-robot-r1-audioclient-set-volume-1) | `def set_volume(self, volume: int) -> int` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |
| [`play_stream`](#unitree-sdk2-cpp-robot-r1-audioclient-play-stream-1) | `def play_stream(self, app_name: str, stream_id: str, pcm_data: Sequence[int]) -> int` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |
| [`play_stop`](#unitree-sdk2-cpp-robot-r1-audioclient-play-stop-1) | `def play_stop(self, app_name: str) -> int` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |
| [`led_control`](#unitree-sdk2-cpp-robot-r1-audioclient-led-control-1) | `def led_control(self, r: int, g: int, b: int) -> int` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |

<a id="unitree-sdk2-cpp-robot-r1-audioclient-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.r1.AudioClient.__init__`

初始化 `AudioClient` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::r1::AudioClient`
- 签名：`AudioClient()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/r1/audio/audio_client.hpp:15`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = AudioClient()
```

<a id="unitree-sdk2-cpp-robot-r1-audioclient-init-1"></a>
#### `unitree_sdk2_cpp.robot.r1.AudioClient.init`

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

- 类：`unitree::robot::r1::AudioClient`
- 签名：`Init()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/r1/audio/audio_client.hpp:19`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.init()
```

<a id="unitree-sdk2-cpp-robot-r1-audioclient-tts-maker-1"></a>
#### `unitree_sdk2_cpp.robot.r1.AudioClient.tts_maker`

对应 C++ SDK 操作 `TtsMaker(const std::string &, int32_t)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def tts_maker(self, text: str, speaker_id: int) -> int
```

**可用性与安全性**

**`AVAILABLE` / `HARDWARE_SIDE_EFFECT`**：当前绑定源码已实现，调用可能修改机器人或服务状态、启动订阅或产生网络副作用。必须显式检查目标设备和返回状态。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `text` | `str` | 必填 | 要处理的文本内容；编码、长度和语言支持由目标服务决定。 对应 C++ 参数 `text: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。 |
| `speaker_id` | `int` | 必填 | 语音合成说话人 ID。有效编号由机器人音频服务和固件决定。 对应 C++ 参数 `speaker_id: int32_t`。 取值范围为 -2147483648 到 2147483647。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::r1::AudioClient`
- 签名：`TtsMaker(const std::string &, int32_t)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/r1/audio/audio_client.hpp:31`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.tts_maker(text=text, speaker_id=speaker_id)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-r1-audioclient-get-volume-1"></a>
#### `unitree_sdk2_cpp.robot.r1.AudioClient.get_volume`

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
| [1] `volume` | `int` | 传给该接口的 音量 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `volume: uint8_t &`。 取值范围为 0 到 255。 |

**对应 C++**

- 类：`unitree::robot::r1::AudioClient`
- 签名：`GetVolume(uint8_t &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/r1/audio/audio_client.hpp:43`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, volume = obj.get_volume()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-r1-audioclient-set-volume-1"></a>
#### `unitree_sdk2_cpp.robot.r1.AudioClient.set_volume`

设置 音量。具体副作用和安全边界见下方状态。

**签名**

```python
def set_volume(self, volume: int) -> int
```

**可用性与安全性**

**`AVAILABLE` / `HARDWARE_SIDE_EFFECT`**：当前绑定源码已实现，调用可能修改机器人或服务状态、启动订阅或产生网络副作用。必须显式检查目标设备和返回状态。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `volume` | `int` | 必填 | 传给该接口的 音量 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `volume: uint8_t`。 取值范围为 0 到 255。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::r1::AudioClient`
- 签名：`SetVolume(uint8_t)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/r1/audio/audio_client.hpp:57`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.set_volume(volume=volume)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-r1-audioclient-play-stream-1"></a>
#### `unitree_sdk2_cpp.robot.r1.AudioClient.play_stream`

对应 C++ SDK 操作 `PlayStream(std::string, std::string, std::vector<uint8_t>)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def play_stream(self, app_name: str, stream_id: str, pcm_data: Sequence[int]) -> int
```

**可用性与安全性**

**`AVAILABLE` / `HARDWARE_SIDE_EFFECT`**：当前绑定源码已实现，调用可能修改机器人或服务状态、启动订阅或产生网络副作用。必须显式检查目标设备和返回状态。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `app_name` | `str` | 必填 | 应用名称，用于标识音频流或播放会话。允许值和命名规则以目标服务协议为准。 对应 C++ 参数 `app_name: std::string`。 底层为字符串；长度、编码和允许值由具体协议决定。 |
| `stream_id` | `str` | 必填 | 音频流标识符，用于区分同一应用下的播放流。 对应 C++ 参数 `stream_id: std::string`。 底层为字符串；长度、编码和允许值由具体协议决定。 |
| `pcm_data` | `Sequence[int]` | 必填 | 传给该接口的 `pcm` 数据 参数，Python 类型为 `Sequence[int]`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `pcm_data: std::vector<uint8_t>`。 底层是可变长度 vector；元素约束：取值范围为 0 到 255。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::r1::AudioClient`
- 签名：`PlayStream(std::string, std::string, std::vector<uint8_t>)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/r1/audio/audio_client.hpp:68`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.play_stream(app_name=app_name, stream_id=stream_id, pcm_data=pcm_data)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-r1-audioclient-play-stop-1"></a>
#### `unitree_sdk2_cpp.robot.r1.AudioClient.play_stop`

对应 C++ SDK 操作 `PlayStop(std::string)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def play_stop(self, app_name: str) -> int
```

**可用性与安全性**

**`AVAILABLE` / `HARDWARE_SIDE_EFFECT`**：当前绑定源码已实现，调用可能修改机器人或服务状态、启动订阅或产生网络副作用。必须显式检查目标设备和返回状态。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `app_name` | `str` | 必填 | 应用名称，用于标识音频流或播放会话。允许值和命名规则以目标服务协议为准。 对应 C++ 参数 `app_name: std::string`。 底层为字符串；长度、编码和允许值由具体协议决定。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::r1::AudioClient`
- 签名：`PlayStop(std::string)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/r1/audio/audio_client.hpp:80`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.play_stop(app_name=app_name)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-r1-audioclient-led-control-1"></a>
#### `unitree_sdk2_cpp.robot.r1.AudioClient.led_control`

对应 C++ SDK 操作 `LedControl(uint8_t, uint8_t, uint8_t)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def led_control(self, r: int, g: int, b: int) -> int
```

**可用性与安全性**

**`AVAILABLE` / `HARDWARE_SIDE_EFFECT`**：当前绑定源码已实现，调用可能修改机器人或服务状态、启动订阅或产生网络副作用。必须显式检查目标设备和返回状态。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `r` | `int` | 必填 | 传给该接口的 `r` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `R: uint8_t`。 取值范围为 0 到 255。 |
| `g` | `int` | 必填 | 传给该接口的 `g` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `G: uint8_t`。 取值范围为 0 到 255。 |
| `b` | `int` | 必填 | 传给该接口的 `b` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `B: uint8_t`。 取值范围为 0 到 255。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::r1::AudioClient`
- 签名：`LedControl(uint8_t, uint8_t, uint8_t)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/r1/audio/audio_client.hpp:91`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.led_control(r=r, g=g, b=b)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-r1-jsonizedatavecfloat"></a>
### `unitree_sdk2_cpp.robot.r1.JsonizeDataVecFloat`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot.r1 import JsonizeDataVecFloat
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `data` | `list[float]` | 传给该接口的 数据 参数，Python 类型为 `list[float]`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.data` / `obj.data = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-r1-jsonizedatavecfloat-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-r1-jsonizedatavecfloat-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-r1-jsonizedatavecfloat-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-r1-jsonizedatavecfloat-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.r1.JsonizeDataVecFloat.__init__`

初始化 `JsonizeDataVecFloat` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::r1::JsonizeDataVecFloat`
- 签名：`JsonizeDataVecFloat()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/r1/loco/r1_loco_api.hpp:27`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = JsonizeDataVecFloat()
```

<a id="unitree-sdk2-cpp-robot-r1-jsonizedatavecfloat-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.r1.JsonizeDataVecFloat.from_json`

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

- 类：`unitree::robot::r1::JsonizeDataVecFloat`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/r1/loco/r1_loco_api.hpp:30`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-r1-jsonizedatavecfloat-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.r1.JsonizeDataVecFloat.to_json`

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

- 类：`unitree::robot::r1::JsonizeDataVecFloat`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/r1/loco/r1_loco_api.hpp:34`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-r1-jsonizevelocitycommand"></a>
### `unitree_sdk2_cpp.robot.r1.JsonizeVelocityCommand`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot.r1 import JsonizeVelocityCommand
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `velocity` | `list[float]` | 传给该接口的 速度 参数，Python 类型为 `list[float]`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.velocity` / `obj.velocity = value` |
| `duration` | `float` | 操作持续时间参数。精确单位、范围和默认行为以目标型号接口定义为准。 | `value = obj.duration` / `obj.duration = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-r1-jsonizevelocitycommand-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-r1-jsonizevelocitycommand-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-r1-jsonizevelocitycommand-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-r1-jsonizevelocitycommand-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.r1.JsonizeVelocityCommand.__init__`

初始化 `JsonizeVelocityCommand` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::r1::JsonizeVelocityCommand`
- 签名：`JsonizeVelocityCommand()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/r1/loco/r1_loco_api.hpp:43`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = JsonizeVelocityCommand()
```

<a id="unitree-sdk2-cpp-robot-r1-jsonizevelocitycommand-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.r1.JsonizeVelocityCommand.from_json`

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

- 类：`unitree::robot::r1::JsonizeVelocityCommand`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/r1/loco/r1_loco_api.hpp:46`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-r1-jsonizevelocitycommand-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.r1.JsonizeVelocityCommand.to_json`

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

- 类：`unitree::robot::r1::JsonizeVelocityCommand`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/r1/loco/r1_loco_api.hpp:51`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-r1-ledcontrolparameter"></a>
### `unitree_sdk2_cpp.robot.r1.LedControlParameter`

SDK 请求参数值类型；当前可能仅提供设计期签名。

**导入**

```python
from unitree_sdk2_cpp.robot.r1 import LedControlParameter
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `r` | `int` | 传给该接口的 `r` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.r` / `obj.r = value` |
| `g` | `int` | 传给该接口的 `g` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.g` / `obj.g = value` |
| `b` | `int` | 传给该接口的 `b` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.b` / `obj.b = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-r1-ledcontrolparameter-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-r1-ledcontrolparameter-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-r1-ledcontrolparameter-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-r1-ledcontrolparameter-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.r1.LedControlParameter.__init__`

初始化 `LedControlParameter` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::r1::LedControlParameter`
- 签名：`LedControlParameter()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/r1/audio/audio_api.hpp:75`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = LedControlParameter()
```

<a id="unitree-sdk2-cpp-robot-r1-ledcontrolparameter-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.r1.LedControlParameter.from_json`

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

- 类：`unitree::robot::r1::LedControlParameter`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/r1/audio/audio_api.hpp:78`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-r1-ledcontrolparameter-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.r1.LedControlParameter.to_json`

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

- 类：`unitree::robot::r1::LedControlParameter`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/r1/audio/audio_api.hpp:80`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-r1-lococlient"></a>
### `unitree_sdk2_cpp.robot.r1.LocoClient`

Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

**导入**

```python
from unitree_sdk2_cpp.robot.r1 import LocoClient
```

**基类**：`Client`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-r1-lococlient-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`init`](#unitree-sdk2-cpp-robot-r1-lococlient-init-1) | `def init(self) -> None` | `AVAILABLE` | `INITIALIZATION` |
| [`get_fsm_id`](#unitree-sdk2-cpp-robot-r1-lococlient-get-fsm-id-1) | `def get_fsm_id(self) -> tuple[int, int]` | `AVAILABLE` | `READ_ONLY` |
| [`get_fsm_mode`](#unitree-sdk2-cpp-robot-r1-lococlient-get-fsm-mode-1) | `def get_fsm_mode(self) -> tuple[int, int]` | `AVAILABLE` | `READ_ONLY` |
| [`set_fsm_id`](#unitree-sdk2-cpp-robot-r1-lococlient-set-fsm-id-1) | `def set_fsm_id(self, fsm_id: int) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`set_velocity`](#unitree-sdk2-cpp-robot-r1-lococlient-set-velocity-1) | `def set_velocity(self, vx: float, vy: float, omega: float, duration: float = 1.0) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`damp`](#unitree-sdk2-cpp-robot-r1-lococlient-damp-1) | `def damp(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`start`](#unitree-sdk2-cpp-robot-r1-lococlient-start-1) | `def start(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`stand_up`](#unitree-sdk2-cpp-robot-r1-lococlient-stand-up-1) | `def stand_up(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`zero_torque`](#unitree-sdk2-cpp-robot-r1-lococlient-zero-torque-1) | `def zero_torque(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`stop_move`](#unitree-sdk2-cpp-robot-r1-lococlient-stop-move-1) | `def stop_move(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`move（重载 1/2）`](#unitree-sdk2-cpp-robot-r1-lococlient-move-1) | `def move(self, vx: float, vy: float, vyaw: float, continous_move: bool) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`move（重载 2/2）`](#unitree-sdk2-cpp-robot-r1-lococlient-move-2) | `def move(self, vx: float, vy: float, vyaw: float) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`switch_move_mode`](#unitree-sdk2-cpp-robot-r1-lococlient-switch-move-mode-1) | `def switch_move_mode(self, flag: bool) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`set_speed_mode`](#unitree-sdk2-cpp-robot-r1-lococlient-set-speed-mode-1) | `def set_speed_mode(self, speed_mode: int) -> int` | `AVAILABLE` | `MOTION_COMMAND` |

<a id="unitree-sdk2-cpp-robot-r1-lococlient-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.r1.LocoClient.__init__`

初始化 `LocoClient` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::r1::LocoClient`
- 签名：`LocoClient()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/r1/loco/r1_loco_client.hpp:13`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = LocoClient()
```

<a id="unitree-sdk2-cpp-robot-r1-lococlient-init-1"></a>
#### `unitree_sdk2_cpp.robot.r1.LocoClient.init`

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

- 类：`unitree::robot::r1::LocoClient`
- 签名：`Init()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/r1/loco/r1_loco_client.hpp:17`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.init()
```

<a id="unitree-sdk2-cpp-robot-r1-lococlient-get-fsm-id-1"></a>
#### `unitree_sdk2_cpp.robot.r1.LocoClient.get_fsm_id`

查询或检查 FSM ID。

**签名**

```python
def get_fsm_id(self) -> tuple[int, int]
```

**可用性与安全性**

**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现只读查询。Robot Client 的服务端查询通常仍需匹配的 Linux 扩展、DDS、网络、机器人和服务；纯本地 getter 则不一定需要全部条件。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| [0] `status` | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。 |
| [1] `fsm_id` | `int` | 传给该接口的 FSM ID 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `fsm_id: int &`。 |

**对应 C++**

- 类：`unitree::robot::r1::LocoClient`
- 签名：`GetFsmId(int &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/r1/loco/r1_loco_client.hpp:28`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, fsm_id = obj.get_fsm_id()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-r1-lococlient-get-fsm-mode-1"></a>
#### `unitree_sdk2_cpp.robot.r1.LocoClient.get_fsm_mode`

查询或检查 FSM 模式。

**签名**

```python
def get_fsm_mode(self) -> tuple[int, int]
```

**可用性与安全性**

**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现只读查询。Robot Client 的服务端查询通常仍需匹配的 Linux 扩展、DDS、网络、机器人和服务；纯本地 getter 则不一定需要全部条件。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| [0] `status` | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。 |
| [1] `fsm_mode` | `int` | 传给该接口的 FSM 模式 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `fsm_mode: int &`。 |

**对应 C++**

- 类：`unitree::robot::r1::LocoClient`
- 签名：`GetFsmMode(int &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/r1/loco/r1_loco_client.hpp:43`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, fsm_mode = obj.get_fsm_mode()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-r1-lococlient-set-fsm-id-1"></a>
#### `unitree_sdk2_cpp.robot.r1.LocoClient.set_fsm_id`

设置 FSM ID。具体副作用和安全边界见下方状态。

**签名**

```python
def set_fsm_id(self, fsm_id: int) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `fsm_id` | `int` | 必填 | 传给该接口的 FSM ID 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `fsm_id: int`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::r1::LocoClient`
- 签名：`SetFsmId(int)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/r1/loco/r1_loco_client.hpp:58`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.set_fsm_id(fsm_id=fsm_id)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-r1-lococlient-set-velocity-1"></a>
#### `unitree_sdk2_cpp.robot.r1.LocoClient.set_velocity`

设置 速度。具体副作用和安全边界见下方状态。

**签名**

```python
def set_velocity(self, vx: float, vy: float, omega: float, duration: float = 1.0) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `vx` | `float` | 必填 | X 方向速度参数。坐标系、单位、符号和安全范围必须查目标型号运动协议。 对应 C++ 参数 `vx: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |
| `vy` | `float` | 必填 | Y 方向速度参数。坐标系、单位、符号和安全范围必须查目标型号运动协议。 对应 C++ 参数 `vy: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |
| `omega` | `float` | 必填 | 角速度参数。旋转轴、单位、符号和安全范围必须查目标型号运动协议。 对应 C++ 参数 `omega: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |
| `duration` | `float` | `1.0` | 操作持续时间参数。精确单位、范围和默认行为以目标型号接口定义为准。 对应 C++ 参数 `duration: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::r1::LocoClient`
- 签名：`SetVelocity(float, float, float, float)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/r1/loco/r1_loco_client.hpp:69`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.set_velocity(vx=vx, vy=vy, omega=omega, duration=duration)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-r1-lococlient-damp-1"></a>
#### `unitree_sdk2_cpp.robot.r1.LocoClient.damp`

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

- 类：`unitree::robot::r1::LocoClient`
- 签名：`Damp()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/r1/loco/r1_loco_client.hpp:82`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.damp()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-r1-lococlient-start-1"></a>
#### `unitree_sdk2_cpp.robot.r1.LocoClient.start`

启动对应 SDK 操作。具体副作用和安全边界见下方状态。

**签名**

```python
def start(self) -> int
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

- 类：`unitree::robot::r1::LocoClient`
- 签名：`Start()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/r1/loco/r1_loco_client.hpp:84`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.start()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-r1-lococlient-stand-up-1"></a>
#### `unitree_sdk2_cpp.robot.r1.LocoClient.stand_up`

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

- 类：`unitree::robot::r1::LocoClient`
- 签名：`StandUp()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/r1/loco/r1_loco_client.hpp:90`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.stand_up()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-r1-lococlient-zero-torque-1"></a>
#### `unitree_sdk2_cpp.robot.r1.LocoClient.zero_torque`

对应 C++ SDK 操作 `ZeroTorque()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def zero_torque(self) -> int
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

- 类：`unitree::robot::r1::LocoClient`
- 签名：`ZeroTorque()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/r1/loco/r1_loco_client.hpp:92`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.zero_torque()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-r1-lococlient-stop-move-1"></a>
#### `unitree_sdk2_cpp.robot.r1.LocoClient.stop_move`

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

- 类：`unitree::robot::r1::LocoClient`
- 签名：`StopMove()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/r1/loco/r1_loco_client.hpp:94`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.stop_move()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-r1-lococlient-move-1"></a>
#### `unitree_sdk2_cpp.robot.r1.LocoClient.move`（重载 1/2）

对应 C++ SDK 操作 `Move(float, float, float, bool)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
@overload
def move(self, vx: float, vy: float, vyaw: float, continous_move: bool) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `vx` | `float` | 必填 | X 方向速度参数。坐标系、单位、符号和安全范围必须查目标型号运动协议。 对应 C++ 参数 `vx: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |
| `vy` | `float` | 必填 | Y 方向速度参数。坐标系、单位、符号和安全范围必须查目标型号运动协议。 对应 C++ 参数 `vy: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |
| `vyaw` | `float` | 必填 | 偏航角速度参数。单位、符号和安全范围必须查目标型号运动协议。 对应 C++ 参数 `vyaw: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |
| `continous_move` | `bool` | 必填 | 传给该接口的 `continous` `move` 参数，Python 类型为 `bool`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `continous_move: bool`。 只接受布尔语义。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::r1::LocoClient`
- 签名：`Move(float, float, float, bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/r1/loco/r1_loco_client.hpp:96`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.move(vx=vx, vy=vy, vyaw=vyaw, continous_move=continous_move)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-r1-lococlient-move-2"></a>
#### `unitree_sdk2_cpp.robot.r1.LocoClient.move`（重载 2/2）

对应 C++ SDK 操作 `Move(float, float, float)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
@overload
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

- 类：`unitree::robot::r1::LocoClient`
- 签名：`Move(float, float, float)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/r1/loco/r1_loco_client.hpp:100`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.move(vx=vx, vy=vy, vyaw=vyaw)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-r1-lococlient-switch-move-mode-1"></a>
#### `unitree_sdk2_cpp.robot.r1.LocoClient.switch_move_mode`

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

- 类：`unitree::robot::r1::LocoClient`
- 签名：`SwitchMoveMode(bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/r1/loco/r1_loco_client.hpp:102`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.switch_move_mode(flag=flag)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-r1-lococlient-set-speed-mode-1"></a>
#### `unitree_sdk2_cpp.robot.r1.LocoClient.set_speed_mode`

设置 速度 模式。具体副作用和安全边界见下方状态。

**签名**

```python
def set_speed_mode(self, speed_mode: int) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `speed_mode` | `int` | 必填 | 传给该接口的 速度 模式 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `speed_mode: int`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::r1::LocoClient`
- 签名：`SetSpeedMode(int)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/r1/loco/r1_loco_client.hpp:107`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.set_speed_mode(speed_mode=speed_mode)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-r1-playstopparameter"></a>
### `unitree_sdk2_cpp.robot.r1.PlayStopParameter`

SDK 请求参数值类型；当前可能仅提供设计期签名。

**导入**

```python
from unitree_sdk2_cpp.robot.r1 import PlayStopParameter
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `app_name` | `str` | 应用名称，用于标识音频流或播放会话。允许值和命名规则以目标服务协议为准。 | `value = obj.app_name` / `obj.app_name = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-r1-playstopparameter-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-r1-playstopparameter-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-r1-playstopparameter-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-r1-playstopparameter-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.r1.PlayStopParameter.__init__`

初始化 `PlayStopParameter` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::r1::PlayStopParameter`
- 签名：`PlayStopParameter()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/r1/audio/audio_api.hpp:61`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = PlayStopParameter()
```

<a id="unitree-sdk2-cpp-robot-r1-playstopparameter-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.r1.PlayStopParameter.from_json`

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

- 类：`unitree::robot::r1::PlayStopParameter`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/r1/audio/audio_api.hpp:64`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-r1-playstopparameter-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.r1.PlayStopParameter.to_json`

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

- 类：`unitree::robot::r1::PlayStopParameter`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/r1/audio/audio_api.hpp:66`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-r1-playstreamparameter"></a>
### `unitree_sdk2_cpp.robot.r1.PlayStreamParameter`

SDK 请求参数值类型；当前可能仅提供设计期签名。

**导入**

```python
from unitree_sdk2_cpp.robot.r1 import PlayStreamParameter
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `app_name` | `str` | 应用名称，用于标识音频流或播放会话。允许值和命名规则以目标服务协议为准。 | `value = obj.app_name` / `obj.app_name = value` |
| `stream_id` | `str` | 音频流标识符，用于区分同一应用下的播放流。 | `value = obj.stream_id` / `obj.stream_id = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-r1-playstreamparameter-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-r1-playstreamparameter-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-r1-playstreamparameter-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-r1-playstreamparameter-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.r1.PlayStreamParameter.__init__`

初始化 `PlayStreamParameter` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::r1::PlayStreamParameter`
- 签名：`PlayStreamParameter()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/r1/audio/audio_api.hpp:45`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = PlayStreamParameter()
```

<a id="unitree-sdk2-cpp-robot-r1-playstreamparameter-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.r1.PlayStreamParameter.from_json`

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

- 类：`unitree::robot::r1::PlayStreamParameter`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/r1/audio/audio_api.hpp:48`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-r1-playstreamparameter-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.r1.PlayStreamParameter.to_json`

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

- 类：`unitree::robot::r1::PlayStreamParameter`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/r1/audio/audio_api.hpp:50`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-r1-ttsmakerparameter"></a>
### `unitree_sdk2_cpp.robot.r1.TtsMakerParameter`

SDK 请求参数值类型；当前可能仅提供设计期签名。

**导入**

```python
from unitree_sdk2_cpp.robot.r1 import TtsMakerParameter
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `index` | `int` | 传给该接口的 `index` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.index` / `obj.index = value` |
| `speaker_id` | `int` | 语音合成说话人 ID。有效编号由机器人音频服务和固件决定。 | `value = obj.speaker_id` / `obj.speaker_id = value` |
| `text` | `str` | 要处理的文本内容；编码、长度和语言支持由目标服务决定。 | `value = obj.text` / `obj.text = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-r1-ttsmakerparameter-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-r1-ttsmakerparameter-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-r1-ttsmakerparameter-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-r1-ttsmakerparameter-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.r1.TtsMakerParameter.__init__`

初始化 `TtsMakerParameter` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::r1::TtsMakerParameter`
- 签名：`TtsMakerParameter()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/r1/audio/audio_api.hpp:27`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = TtsMakerParameter()
```

<a id="unitree-sdk2-cpp-robot-r1-ttsmakerparameter-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.r1.TtsMakerParameter.from_json`

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

- 类：`unitree::robot::r1::TtsMakerParameter`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/r1/audio/audio_api.hpp:30`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-r1-ttsmakerparameter-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.r1.TtsMakerParameter.to_json`

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

- 类：`unitree::robot::r1::TtsMakerParameter`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/r1/audio/audio_api.hpp:32`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

---

[返回 API 总索引](../API_REFERENCE_ZH.md)
