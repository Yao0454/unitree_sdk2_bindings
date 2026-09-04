# Unitree SDK2 Python API 参考分卷

[返回 API 总索引](../API_REFERENCE_ZH.md) · [阅读从零开始指南](../BEGINNER_GUIDE_ZH.md)

> [!WARNING]
> 本分卷同时包含 `AVAILABLE` 和 `SIGNATURE_ONLY`。后者只是设计期类型签名。运动及硬件副作用方法即使标记为 `AVAILABLE`，也不表示当前环境可安全执行。

> [!NOTE]
> 本文件由 `generator/generate_api_docs.py` 自动生成，请勿手工维护 API 条目。

---

<a id="unitree-sdk2-cpp-robot-a2"></a>
## A2 Robot API

模块：`unitree_sdk2_cpp.robot.a2`

### 类索引

| 类 | 公开函数签名 | 属性 |
| --- | ---: | ---: |
| [`AudioClient`](#unitree-sdk2-cpp-robot-a2-audioclient) | 8 | 0 |
| [`LedControlParameter`](#unitree-sdk2-cpp-robot-a2-ledcontrolparameter) | 3 | 0 |
| [`PathPoint`](#unitree-sdk2-cpp-robot-a2-pathpoint) | 1 | 0 |
| [`PlayStopParameter`](#unitree-sdk2-cpp-robot-a2-playstopparameter) | 3 | 0 |
| [`PlayStreamParameter`](#unitree-sdk2-cpp-robot-a2-playstreamparameter) | 3 | 0 |
| [`PoseVec4`](#unitree-sdk2-cpp-robot-a2-posevec4) | 3 | 0 |
| [`SportClient`](#unitree-sdk2-cpp-robot-a2-sportclient) | 24 | 0 |
| [`TtsMakerParameter`](#unitree-sdk2-cpp-robot-a2-ttsmakerparameter) | 3 | 0 |

<a id="unitree-sdk2-cpp-robot-a2-audioclient"></a>
### `unitree_sdk2_cpp.robot.a2.AudioClient`

Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

**导入**

```python
from unitree_sdk2_cpp.robot.a2 import AudioClient
```

**基类**：`Client`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-a2-audioclient-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`init`](#unitree-sdk2-cpp-robot-a2-audioclient-init-1) | `def init(self) -> None` | `AVAILABLE` | `INITIALIZATION` |
| [`tts_maker`](#unitree-sdk2-cpp-robot-a2-audioclient-tts-maker-1) | `def tts_maker(self, text: str, speaker_id: int) -> int` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |
| [`get_volume`](#unitree-sdk2-cpp-robot-a2-audioclient-get-volume-1) | `def get_volume(self) -> tuple[int, int]` | `AVAILABLE` | `READ_ONLY` |
| [`set_volume`](#unitree-sdk2-cpp-robot-a2-audioclient-set-volume-1) | `def set_volume(self, volume: int) -> int` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |
| [`play_stream`](#unitree-sdk2-cpp-robot-a2-audioclient-play-stream-1) | `def play_stream(self, app_name: str, stream_id: str, pcm_data: Sequence[int]) -> int` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |
| [`play_stop`](#unitree-sdk2-cpp-robot-a2-audioclient-play-stop-1) | `def play_stop(self, app_name: str) -> int` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |
| [`led_control`](#unitree-sdk2-cpp-robot-a2-audioclient-led-control-1) | `def led_control(self, r: int, g: int, b: int) -> int` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |

<a id="unitree-sdk2-cpp-robot-a2-audioclient-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.a2.AudioClient.__init__`

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

- 类：`unitree::robot::a2::AudioClient`
- 签名：`AudioClient()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/a2/audio/audio_client.hpp:15`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = AudioClient()
```

<a id="unitree-sdk2-cpp-robot-a2-audioclient-init-1"></a>
#### `unitree_sdk2_cpp.robot.a2.AudioClient.init`

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

- 类：`unitree::robot::a2::AudioClient`
- 签名：`Init()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/a2/audio/audio_client.hpp:19`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.init()
```

<a id="unitree-sdk2-cpp-robot-a2-audioclient-tts-maker-1"></a>
#### `unitree_sdk2_cpp.robot.a2.AudioClient.tts_maker`

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

- 类：`unitree::robot::a2::AudioClient`
- 签名：`TtsMaker(const std::string &, int32_t)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/a2/audio/audio_client.hpp:31`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.tts_maker(text=text, speaker_id=speaker_id)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-a2-audioclient-get-volume-1"></a>
#### `unitree_sdk2_cpp.robot.a2.AudioClient.get_volume`

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

- 类：`unitree::robot::a2::AudioClient`
- 签名：`GetVolume(uint8_t &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/a2/audio/audio_client.hpp:43`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, volume = obj.get_volume()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-a2-audioclient-set-volume-1"></a>
#### `unitree_sdk2_cpp.robot.a2.AudioClient.set_volume`

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

- 类：`unitree::robot::a2::AudioClient`
- 签名：`SetVolume(uint8_t)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/a2/audio/audio_client.hpp:57`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.set_volume(volume=volume)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-a2-audioclient-play-stream-1"></a>
#### `unitree_sdk2_cpp.robot.a2.AudioClient.play_stream`

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

- 类：`unitree::robot::a2::AudioClient`
- 签名：`PlayStream(std::string, std::string, std::vector<uint8_t>)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/a2/audio/audio_client.hpp:68`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.play_stream(app_name=app_name, stream_id=stream_id, pcm_data=pcm_data)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-a2-audioclient-play-stop-1"></a>
#### `unitree_sdk2_cpp.robot.a2.AudioClient.play_stop`

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

- 类：`unitree::robot::a2::AudioClient`
- 签名：`PlayStop(std::string)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/a2/audio/audio_client.hpp:80`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.play_stop(app_name=app_name)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-a2-audioclient-led-control-1"></a>
#### `unitree_sdk2_cpp.robot.a2.AudioClient.led_control`

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

- 类：`unitree::robot::a2::AudioClient`
- 签名：`LedControl(uint8_t, uint8_t, uint8_t)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/a2/audio/audio_client.hpp:91`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.led_control(r=r, g=g, b=b)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-a2-ledcontrolparameter"></a>
### `unitree_sdk2_cpp.robot.a2.LedControlParameter`

SDK 请求参数值类型；当前可能仅提供设计期签名。

**导入**

```python
from unitree_sdk2_cpp.robot.a2 import LedControlParameter
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
| [`__init__`](#unitree-sdk2-cpp-robot-a2-ledcontrolparameter-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-a2-ledcontrolparameter-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-a2-ledcontrolparameter-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-a2-ledcontrolparameter-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.a2.LedControlParameter.__init__`

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

- 类：`unitree::robot::a2::LedControlParameter`
- 签名：`LedControlParameter()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/a2/audio/audio_api.hpp:75`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = LedControlParameter()
```

<a id="unitree-sdk2-cpp-robot-a2-ledcontrolparameter-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.a2.LedControlParameter.from_json`

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

- 类：`unitree::robot::a2::LedControlParameter`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/a2/audio/audio_api.hpp:78`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-a2-ledcontrolparameter-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.a2.LedControlParameter.to_json`

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

- 类：`unitree::robot::a2::LedControlParameter`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/a2/audio/audio_api.hpp:80`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-a2-pathpoint"></a>
### `unitree_sdk2_cpp.robot.a2.PathPoint`

SDK 数据值类型；公开字段和转换方法见下文。

**导入**

```python
from unitree_sdk2_cpp.robot.a2 import PathPoint
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `t_from_start` | `float` | 传给该接口的 `t` `from` `start` 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.t_from_start` / `obj.t_from_start = value` |
| `x` | `float` | X 方向位置或分量参数。参考系、单位和范围必须查当前方法及目标型号协议。 | `value = obj.x` / `obj.x = value` |
| `y` | `float` | Y 方向位置或分量参数。参考系、单位和范围必须查当前方法及目标型号协议。 | `value = obj.y` / `obj.y = value` |
| `yaw` | `float` | 偏航角或偏航目标参数。参考系、单位和范围必须查目标型号协议。 | `value = obj.yaw` / `obj.yaw = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-a2-pathpoint-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |

<a id="unitree-sdk2-cpp-robot-a2-pathpoint-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.a2.PathPoint.__init__`

初始化 `PathPoint` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::a2::PathPoint`
- 签名：`PathPoint()`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = PathPoint()
```

<a id="unitree-sdk2-cpp-robot-a2-playstopparameter"></a>
### `unitree_sdk2_cpp.robot.a2.PlayStopParameter`

SDK 请求参数值类型；当前可能仅提供设计期签名。

**导入**

```python
from unitree_sdk2_cpp.robot.a2 import PlayStopParameter
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `app_name` | `str` | 应用名称，用于标识音频流或播放会话。允许值和命名规则以目标服务协议为准。 | `value = obj.app_name` / `obj.app_name = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-a2-playstopparameter-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-a2-playstopparameter-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-a2-playstopparameter-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-a2-playstopparameter-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.a2.PlayStopParameter.__init__`

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

- 类：`unitree::robot::a2::PlayStopParameter`
- 签名：`PlayStopParameter()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/a2/audio/audio_api.hpp:61`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = PlayStopParameter()
```

<a id="unitree-sdk2-cpp-robot-a2-playstopparameter-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.a2.PlayStopParameter.from_json`

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

- 类：`unitree::robot::a2::PlayStopParameter`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/a2/audio/audio_api.hpp:64`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-a2-playstopparameter-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.a2.PlayStopParameter.to_json`

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

- 类：`unitree::robot::a2::PlayStopParameter`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/a2/audio/audio_api.hpp:66`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-a2-playstreamparameter"></a>
### `unitree_sdk2_cpp.robot.a2.PlayStreamParameter`

SDK 请求参数值类型；当前可能仅提供设计期签名。

**导入**

```python
from unitree_sdk2_cpp.robot.a2 import PlayStreamParameter
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
| [`__init__`](#unitree-sdk2-cpp-robot-a2-playstreamparameter-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-a2-playstreamparameter-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-a2-playstreamparameter-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-a2-playstreamparameter-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.a2.PlayStreamParameter.__init__`

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

- 类：`unitree::robot::a2::PlayStreamParameter`
- 签名：`PlayStreamParameter()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/a2/audio/audio_api.hpp:45`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = PlayStreamParameter()
```

<a id="unitree-sdk2-cpp-robot-a2-playstreamparameter-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.a2.PlayStreamParameter.from_json`

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

- 类：`unitree::robot::a2::PlayStreamParameter`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/a2/audio/audio_api.hpp:48`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-a2-playstreamparameter-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.a2.PlayStreamParameter.to_json`

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

- 类：`unitree::robot::a2::PlayStreamParameter`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/a2/audio/audio_api.hpp:50`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-a2-posevec4"></a>
### `unitree_sdk2_cpp.robot.a2.PoseVec4`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot.a2 import PoseVec4
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `x` | `float` | X 方向位置或分量参数。参考系、单位和范围必须查当前方法及目标型号协议。 | `value = obj.x` / `obj.x = value` |
| `y` | `float` | Y 方向位置或分量参数。参考系、单位和范围必须查当前方法及目标型号协议。 | `value = obj.y` / `obj.y = value` |
| `z` | `float` | Z 方向位置或分量参数。参考系、单位和范围必须查当前方法及目标型号协议。 | `value = obj.z` / `obj.z = value` |
| `yaw` | `float` | 偏航角或偏航目标参数。参考系、单位和范围必须查目标型号协议。 | `value = obj.yaw` / `obj.yaw = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-a2-posevec4-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-a2-posevec4-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-a2-posevec4-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-a2-posevec4-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.a2.PoseVec4.__init__`

初始化 `PoseVec4` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::a2::PoseVec4`
- 签名：`PoseVec4()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/a2/sport/sport_client.hpp:35`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = PoseVec4()
```

<a id="unitree-sdk2-cpp-robot-a2-posevec4-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.a2.PoseVec4.from_json`

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

- 类：`unitree::robot::a2::PoseVec4`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/a2/sport/sport_client.hpp:43`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-a2-posevec4-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.a2.PoseVec4.to_json`

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

- 类：`unitree::robot::a2::PoseVec4`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/a2/sport/sport_client.hpp:51`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-a2-sportclient"></a>
### `unitree_sdk2_cpp.robot.a2.SportClient`

Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

**导入**

```python
from unitree_sdk2_cpp.robot.a2 import SportClient
```

**基类**：`Client`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-a2-sportclient-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`init`](#unitree-sdk2-cpp-robot-a2-sportclient-init-1) | `def init(self) -> None` | `AVAILABLE` | `INITIALIZATION` |
| [`damp`](#unitree-sdk2-cpp-robot-a2-sportclient-damp-1) | `def damp(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`balance_stand`](#unitree-sdk2-cpp-robot-a2-sportclient-balance-stand-1) | `def balance_stand(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`stop_move`](#unitree-sdk2-cpp-robot-a2-sportclient-stop-move-1) | `def stop_move(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`stand_up`](#unitree-sdk2-cpp-robot-a2-sportclient-stand-up-1) | `def stand_up(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`stand_down`](#unitree-sdk2-cpp-robot-a2-sportclient-stand-down-1) | `def stand_down(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`recovery_stand`](#unitree-sdk2-cpp-robot-a2-sportclient-recovery-stand-1) | `def recovery_stand(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`euler`](#unitree-sdk2-cpp-robot-a2-sportclient-euler-1) | `def euler(self, roll: float, pitch: float, yaw: float) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`move`](#unitree-sdk2-cpp-robot-a2-sportclient-move-1) | `def move(self, vx: float, vy: float, vyaw: float) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`switch_gait`](#unitree-sdk2-cpp-robot-a2-sportclient-switch-gait-1) | `def switch_gait(self, gait_type: int) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`body_height`](#unitree-sdk2-cpp-robot-a2-sportclient-body-height-1) | `def body_height(self, height: float) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`speed_level`](#unitree-sdk2-cpp-robot-a2-sportclient-speed-level-1) | `def speed_level(self, level: int) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`body_position`](#unitree-sdk2-cpp-robot-a2-sportclient-body-position-1) | `def body_position(self, x: float, y: float, z: float, yaw: float) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`left_side_gait`](#unitree-sdk2-cpp-robot-a2-sportclient-left-side-gait-1) | `def left_side_gait(self, enter: int) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`right_side_gait`](#unitree-sdk2-cpp-robot-a2-sportclient-right-side-gait-1) | `def right_side_gait(self, enter: int) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`hand_stand`](#unitree-sdk2-cpp-robot-a2-sportclient-hand-stand-1) | `def hand_stand(self, enter: int) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`biped_stand`](#unitree-sdk2-cpp-robot-a2-sportclient-biped-stand-1) | `def biped_stand(self, enter: int) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`front_flip`](#unitree-sdk2-cpp-robot-a2-sportclient-front-flip-1) | `def front_flip(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`back_flip`](#unitree-sdk2-cpp-robot-a2-sportclient-back-flip-1) | `def back_flip(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`reset_estimator`](#unitree-sdk2-cpp-robot-a2-sportclient-reset-estimator-1) | `def reset_estimator(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`trajectory`](#unitree-sdk2-cpp-robot-a2-sportclient-trajectory-1) | `def trajectory(self, path: Sequence[PathPoint], feedback_mode: int = 0, external_x: float = 0.0, external_y: float = 0.0, external_yaw: float = 0.0) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`set_auto_recovery`](#unitree-sdk2-cpp-robot-a2-sportclient-set-auto-recovery-1) | `def set_auto_recovery(self, switch_on: int) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`get_state`](#unitree-sdk2-cpp-robot-a2-sportclient-get-state-1) | `def get_state(self) -> tuple[int, dict[str, str]]` | `AVAILABLE` | `READ_ONLY` |

<a id="unitree-sdk2-cpp-robot-a2-sportclient-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.a2.SportClient.__init__`

初始化 `SportClient` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::a2::SportClient`
- 签名：`SportClient()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/a2/sport/sport_client.hpp:77`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = SportClient()
```

<a id="unitree-sdk2-cpp-robot-a2-sportclient-init-1"></a>
#### `unitree_sdk2_cpp.robot.a2.SportClient.init`

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

- 类：`unitree::robot::a2::SportClient`
- 签名：`Init()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/a2/sport/sport_client.hpp:81`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.init()
```

<a id="unitree-sdk2-cpp-robot-a2-sportclient-damp-1"></a>
#### `unitree_sdk2_cpp.robot.a2.SportClient.damp`

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

- 类：`unitree::robot::a2::SportClient`
- 签名：`Damp()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/a2/sport/sport_client.hpp:112`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.damp()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-a2-sportclient-balance-stand-1"></a>
#### `unitree_sdk2_cpp.robot.a2.SportClient.balance_stand`

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

- 类：`unitree::robot::a2::SportClient`
- 签名：`BalanceStand()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/a2/sport/sport_client.hpp:118`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.balance_stand()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-a2-sportclient-stop-move-1"></a>
#### `unitree_sdk2_cpp.robot.a2.SportClient.stop_move`

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

- 类：`unitree::robot::a2::SportClient`
- 签名：`StopMove()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/a2/sport/sport_client.hpp:123`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.stop_move()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-a2-sportclient-stand-up-1"></a>
#### `unitree_sdk2_cpp.robot.a2.SportClient.stand_up`

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

- 类：`unitree::robot::a2::SportClient`
- 签名：`StandUp()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/a2/sport/sport_client.hpp:129`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.stand_up()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-a2-sportclient-stand-down-1"></a>
#### `unitree_sdk2_cpp.robot.a2.SportClient.stand_down`

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

- 类：`unitree::robot::a2::SportClient`
- 签名：`StandDown()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/a2/sport/sport_client.hpp:135`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.stand_down()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-a2-sportclient-recovery-stand-1"></a>
#### `unitree_sdk2_cpp.robot.a2.SportClient.recovery_stand`

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

- 类：`unitree::robot::a2::SportClient`
- 签名：`RecoveryStand()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/a2/sport/sport_client.hpp:141`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.recovery_stand()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-a2-sportclient-euler-1"></a>
#### `unitree_sdk2_cpp.robot.a2.SportClient.euler`

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

- 类：`unitree::robot::a2::SportClient`
- 签名：`Euler(float, float, float)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/a2/sport/sport_client.hpp:147`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.euler(roll=roll, pitch=pitch, yaw=yaw)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-a2-sportclient-move-1"></a>
#### `unitree_sdk2_cpp.robot.a2.SportClient.move`

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

- 类：`unitree::robot::a2::SportClient`
- 签名：`Move(float, float, float)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/a2/sport/sport_client.hpp:158`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.move(vx=vx, vy=vy, vyaw=vyaw)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-a2-sportclient-switch-gait-1"></a>
#### `unitree_sdk2_cpp.robot.a2.SportClient.switch_gait`

对应 C++ SDK 操作 `SwitchGait(int)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def switch_gait(self, gait_type: int) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `gait_type` | `int` | 必填 | 传给该接口的 `gait` `type` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `gait_type: int`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::a2::SportClient`
- 签名：`SwitchGait(int)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/a2/sport/sport_client.hpp:169`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.switch_gait(gait_type=gait_type)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-a2-sportclient-body-height-1"></a>
#### `unitree_sdk2_cpp.robot.a2.SportClient.body_height`

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

- 类：`unitree::robot::a2::SportClient`
- 签名：`BodyHeight(float)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/a2/sport/sport_client.hpp:178`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.body_height(height=height)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-a2-sportclient-speed-level-1"></a>
#### `unitree_sdk2_cpp.robot.a2.SportClient.speed_level`

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

- 类：`unitree::robot::a2::SportClient`
- 签名：`SpeedLevel(int)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/a2/sport/sport_client.hpp:187`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.speed_level(level=level)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-a2-sportclient-body-position-1"></a>
#### `unitree_sdk2_cpp.robot.a2.SportClient.body_position`

对应 C++ SDK 操作 `BodyPosition(float, float, float, float)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def body_position(self, x: float, y: float, z: float, yaw: float) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `x` | `float` | 必填 | X 方向位置或分量参数。参考系、单位和范围必须查当前方法及目标型号协议。 对应 C++ 参数 `x: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |
| `y` | `float` | 必填 | Y 方向位置或分量参数。参考系、单位和范围必须查当前方法及目标型号协议。 对应 C++ 参数 `y: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |
| `z` | `float` | 必填 | Z 方向位置或分量参数。参考系、单位和范围必须查当前方法及目标型号协议。 对应 C++ 参数 `z: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |
| `yaw` | `float` | 必填 | 偏航角或偏航目标参数。参考系、单位和范围必须查目标型号协议。 对应 C++ 参数 `yaw: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::a2::SportClient`
- 签名：`BodyPosition(float, float, float, float)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/a2/sport/sport_client.hpp:196`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.body_position(x=x, y=y, z=z, yaw=yaw)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-a2-sportclient-left-side-gait-1"></a>
#### `unitree_sdk2_cpp.robot.a2.SportClient.left_side_gait`

对应 C++ SDK 操作 `LeftSideGait(int)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def left_side_gait(self, enter: int) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `enter` | `int` | 必填 | 传给该接口的 `enter` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `enter: int`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::a2::SportClient`
- 签名：`LeftSideGait(int)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/a2/sport/sport_client.hpp:208`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.left_side_gait(enter=enter)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-a2-sportclient-right-side-gait-1"></a>
#### `unitree_sdk2_cpp.robot.a2.SportClient.right_side_gait`

对应 C++ SDK 操作 `RightSideGait(int)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def right_side_gait(self, enter: int) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `enter` | `int` | 必填 | 传给该接口的 `enter` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `enter: int`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::a2::SportClient`
- 签名：`RightSideGait(int)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/a2/sport/sport_client.hpp:217`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.right_side_gait(enter=enter)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-a2-sportclient-hand-stand-1"></a>
#### `unitree_sdk2_cpp.robot.a2.SportClient.hand_stand`

对应 C++ SDK 操作 `HandStand(int)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def hand_stand(self, enter: int) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `enter` | `int` | 必填 | 传给该接口的 `enter` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `enter: int`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::a2::SportClient`
- 签名：`HandStand(int)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/a2/sport/sport_client.hpp:226`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.hand_stand(enter=enter)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-a2-sportclient-biped-stand-1"></a>
#### `unitree_sdk2_cpp.robot.a2.SportClient.biped_stand`

对应 C++ SDK 操作 `BipedStand(int)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def biped_stand(self, enter: int) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `enter` | `int` | 必填 | 传给该接口的 `enter` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `enter: int`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::a2::SportClient`
- 签名：`BipedStand(int)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/a2/sport/sport_client.hpp:235`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.biped_stand(enter=enter)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-a2-sportclient-front-flip-1"></a>
#### `unitree_sdk2_cpp.robot.a2.SportClient.front_flip`

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

- 类：`unitree::robot::a2::SportClient`
- 签名：`FrontFlip()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/a2/sport/sport_client.hpp:244`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.front_flip()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-a2-sportclient-back-flip-1"></a>
#### `unitree_sdk2_cpp.robot.a2.SportClient.back_flip`

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

- 类：`unitree::robot::a2::SportClient`
- 签名：`BackFlip()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/a2/sport/sport_client.hpp:250`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.back_flip()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-a2-sportclient-reset-estimator-1"></a>
#### `unitree_sdk2_cpp.robot.a2.SportClient.reset_estimator`

对应 C++ SDK 操作 `ResetEstimator()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def reset_estimator(self) -> int
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

- 类：`unitree::robot::a2::SportClient`
- 签名：`ResetEstimator()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/a2/sport/sport_client.hpp:256`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.reset_estimator()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-a2-sportclient-trajectory-1"></a>
#### `unitree_sdk2_cpp.robot.a2.SportClient.trajectory`

对应 C++ SDK 操作 `Trajectory(const std::vector<PathPoint> &, int, float, float, float)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def trajectory(self, path: Sequence[PathPoint], feedback_mode: int = 0, external_x: float = 0.0, external_y: float = 0.0, external_yaw: float = 0.0) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `path` | `Sequence[PathPoint]` | 必填 | 传给该接口的 `path` 参数，Python 类型为 `Sequence[PathPoint]`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `path: const std::vector<PathPoint> &`。 底层是可变长度 vector |
| `feedback_mode` | `int` | `0` | 传给该接口的 `feedback` 模式 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `feedback_mode: int`。 |
| `external_x` | `float` | `0.0` | 传给该接口的 `external` `x` 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `external_x: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |
| `external_y` | `float` | `0.0` | 传给该接口的 `external` `y` 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `external_y: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |
| `external_yaw` | `float` | `0.0` | 传给该接口的 `external` `yaw` 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `external_yaw: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::a2::SportClient`
- 签名：`Trajectory(const std::vector<PathPoint> &, int, float, float, float)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/a2/sport/sport_client.hpp:262`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.trajectory(path=path, feedback_mode=feedback_mode, external_x=external_x, external_y=external_y, external_yaw=external_yaw)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-a2-sportclient-set-auto-recovery-1"></a>
#### `unitree_sdk2_cpp.robot.a2.SportClient.set_auto_recovery`

设置 `auto` `recovery`。具体副作用和安全边界见下方状态。

**签名**

```python
def set_auto_recovery(self, switch_on: int) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `switch_on` | `int` | 必填 | 传给该接口的 开关 `on` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `switch_on: int`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::a2::SportClient`
- 签名：`SetAutoRecovery(int)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/a2/sport/sport_client.hpp:286`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.set_auto_recovery(switch_on=switch_on)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-a2-sportclient-get-state-1"></a>
#### `unitree_sdk2_cpp.robot.a2.SportClient.get_state`

查询或检查 状态。

**签名**

```python
def get_state(self) -> tuple[int, dict[str, str]]
```

**可用性与安全性**

**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现只读查询。Robot Client 的服务端查询通常仍需匹配的 Linux 扩展、DDS、网络、机器人和服务；纯本地 getter 则不一定需要全部条件。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| [0] `status` | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。 |
| [1] `state_map` | `dict[str, str]` | 传给该接口的 状态 `map` 参数，Python 类型为 `dict[str, str]`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `state_map: std::map<std::string, std::string> &`。 |

**对应 C++**

- 类：`unitree::robot::a2::SportClient`
- 签名：`GetState(std::map<std::string, std::string> &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/a2/sport/sport_client.hpp:295`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, state_map = obj.get_state()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-a2-ttsmakerparameter"></a>
### `unitree_sdk2_cpp.robot.a2.TtsMakerParameter`

SDK 请求参数值类型；当前可能仅提供设计期签名。

**导入**

```python
from unitree_sdk2_cpp.robot.a2 import TtsMakerParameter
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
| [`__init__`](#unitree-sdk2-cpp-robot-a2-ttsmakerparameter-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-a2-ttsmakerparameter-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-a2-ttsmakerparameter-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-a2-ttsmakerparameter-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.a2.TtsMakerParameter.__init__`

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

- 类：`unitree::robot::a2::TtsMakerParameter`
- 签名：`TtsMakerParameter()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/a2/audio/audio_api.hpp:27`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = TtsMakerParameter()
```

<a id="unitree-sdk2-cpp-robot-a2-ttsmakerparameter-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.a2.TtsMakerParameter.from_json`

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

- 类：`unitree::robot::a2::TtsMakerParameter`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/a2/audio/audio_api.hpp:30`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-a2-ttsmakerparameter-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.a2.TtsMakerParameter.to_json`

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

- 类：`unitree::robot::a2::TtsMakerParameter`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/a2/audio/audio_api.hpp:32`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

---

[返回 API 总索引](../API_REFERENCE_ZH.md)
