# Unitree SDK2 Python API 参考分卷

[返回 API 总索引](../API_REFERENCE_ZH.md) · [阅读从零开始指南](../BEGINNER_GUIDE_ZH.md)

> [!WARNING]
> 本分卷同时包含 `AVAILABLE` 和 `SIGNATURE_ONLY`。后者只是设计期类型签名。运动及硬件副作用方法即使标记为 `AVAILABLE`，也不表示当前环境可安全执行。

> [!NOTE]
> 本文件由 `generator/generate_api_docs.py` 自动生成，请勿手工维护 API 条目。

---

<a id="unitree-sdk2-cpp-robot-as2"></a>
## AS2 Robot API

模块：`unitree_sdk2_cpp.robot.as2`

### 类索引

| 类 | 公开函数签名 | 属性 |
| --- | ---: | ---: |
| [`PoseVec4`](#unitree-sdk2-cpp-robot-as2-posevec4) | 3 | 0 |
| [`SportClient`](#unitree-sdk2-cpp-robot-as2-sportclient) | 34 | 0 |

<a id="unitree-sdk2-cpp-robot-as2-posevec4"></a>
### `unitree_sdk2_cpp.robot.as2.PoseVec4`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot.as2 import PoseVec4
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
| [`__init__`](#unitree-sdk2-cpp-robot-as2-posevec4-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-as2-posevec4-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-as2-posevec4-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-as2-posevec4-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.as2.PoseVec4.__init__`

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

- 类：`unitree::robot::as2::PoseVec4`
- 签名：`PoseVec4()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:18`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = PoseVec4()
```

<a id="unitree-sdk2-cpp-robot-as2-posevec4-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.as2.PoseVec4.from_json`

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

- 类：`unitree::robot::as2::PoseVec4`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:26`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-as2-posevec4-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.as2.PoseVec4.to_json`

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

- 类：`unitree::robot::as2::PoseVec4`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:34`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-as2-sportclient"></a>
### `unitree_sdk2_cpp.robot.as2.SportClient`

Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

**导入**

```python
from unitree_sdk2_cpp.robot.as2 import SportClient
```

**基类**：`Client`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-as2-sportclient-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`init`](#unitree-sdk2-cpp-robot-as2-sportclient-init-1) | `def init(self) -> None` | `AVAILABLE` | `INITIALIZATION` |
| [`damp`](#unitree-sdk2-cpp-robot-as2-sportclient-damp-1) | `def damp(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`balance_stand`](#unitree-sdk2-cpp-robot-as2-sportclient-balance-stand-1) | `def balance_stand(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`stop_move`](#unitree-sdk2-cpp-robot-as2-sportclient-stop-move-1) | `def stop_move(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`stand_up`](#unitree-sdk2-cpp-robot-as2-sportclient-stand-up-1) | `def stand_up(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`stand_down`](#unitree-sdk2-cpp-robot-as2-sportclient-stand-down-1) | `def stand_down(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`recovery_stand`](#unitree-sdk2-cpp-robot-as2-sportclient-recovery-stand-1) | `def recovery_stand(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`euler`](#unitree-sdk2-cpp-robot-as2-sportclient-euler-1) | `def euler(self, roll: float, pitch: float, yaw: float) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`move`](#unitree-sdk2-cpp-robot-as2-sportclient-move-1) | `def move(self, vx: float, vy: float, vyaw: float) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`switch_gait`](#unitree-sdk2-cpp-robot-as2-sportclient-switch-gait-1) | `def switch_gait(self, gait_type: int) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`body_height`](#unitree-sdk2-cpp-robot-as2-sportclient-body-height-1) | `def body_height(self, height: float) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`speed_level`](#unitree-sdk2-cpp-robot-as2-sportclient-speed-level-1) | `def speed_level(self, level: int) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`body_position`](#unitree-sdk2-cpp-robot-as2-sportclient-body-position-1) | `def body_position(self, x: float, y: float, z: float, yaw: float) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`left_side_gait`](#unitree-sdk2-cpp-robot-as2-sportclient-left-side-gait-1) | `def left_side_gait(self, enter: int) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`right_side_gait`](#unitree-sdk2-cpp-robot-as2-sportclient-right-side-gait-1) | `def right_side_gait(self, enter: int) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`hand_stand`](#unitree-sdk2-cpp-robot-as2-sportclient-hand-stand-1) | `def hand_stand(self, enter: int) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`biped_stand`](#unitree-sdk2-cpp-robot-as2-sportclient-biped-stand-1) | `def biped_stand(self, enter: int) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`front_flip`](#unitree-sdk2-cpp-robot-as2-sportclient-front-flip-1) | `def front_flip(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`back_flip`](#unitree-sdk2-cpp-robot-as2-sportclient-back-flip-1) | `def back_flip(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`greeting`](#unitree-sdk2-cpp-robot-as2-sportclient-greeting-1) | `def greeting(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`heart`](#unitree-sdk2-cpp-robot-as2-sportclient-heart-1) | `def heart(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`content`](#unitree-sdk2-cpp-robot-as2-sportclient-content-1) | `def content(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`dance1`](#unitree-sdk2-cpp-robot-as2-sportclient-dance1-1) | `def dance1(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`dance2`](#unitree-sdk2-cpp-robot-as2-sportclient-dance2-1) | `def dance2(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`handshake`](#unitree-sdk2-cpp-robot-as2-sportclient-handshake-1) | `def handshake(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`stretch`](#unitree-sdk2-cpp-robot-as2-sportclient-stretch-1) | `def stretch(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`sit`](#unitree-sdk2-cpp-robot-as2-sportclient-sit-1) | `def sit(self, enter: int) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`front_jump`](#unitree-sdk2-cpp-robot-as2-sportclient-front-jump-1) | `def front_jump(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`push_up`](#unitree-sdk2-cpp-robot-as2-sportclient-push-up-1) | `def push_up(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`up_jump`](#unitree-sdk2-cpp-robot-as2-sportclient-up-jump-1) | `def up_jump(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`set_auto_recovery`](#unitree-sdk2-cpp-robot-as2-sportclient-set-auto-recovery-1) | `def set_auto_recovery(self, switch_on: int) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`switch_joystick`](#unitree-sdk2-cpp-robot-as2-sportclient-switch-joystick-1) | `def switch_joystick(self, switch_on: int) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`get_state`](#unitree-sdk2-cpp-robot-as2-sportclient-get-state-1) | `def get_state(self) -> tuple[int, dict[str, str]]` | `AVAILABLE` | `READ_ONLY` |

<a id="unitree-sdk2-cpp-robot-as2-sportclient-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.__init__`

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

- 类：`unitree::robot::as2::SportClient`
- 签名：`SportClient()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:52`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = SportClient()
```

<a id="unitree-sdk2-cpp-robot-as2-sportclient-init-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.init`

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

- 类：`unitree::robot::as2::SportClient`
- 签名：`Init()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:56`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.init()
```

<a id="unitree-sdk2-cpp-robot-as2-sportclient-damp-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.damp`

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

- 类：`unitree::robot::as2::SportClient`
- 签名：`Damp()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:97`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.damp()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-as2-sportclient-balance-stand-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.balance_stand`

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

- 类：`unitree::robot::as2::SportClient`
- 签名：`BalanceStand()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:103`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.balance_stand()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-as2-sportclient-stop-move-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.stop_move`

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

- 类：`unitree::robot::as2::SportClient`
- 签名：`StopMove()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:108`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.stop_move()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-as2-sportclient-stand-up-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.stand_up`

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

- 类：`unitree::robot::as2::SportClient`
- 签名：`StandUp()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:114`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.stand_up()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-as2-sportclient-stand-down-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.stand_down`

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

- 类：`unitree::robot::as2::SportClient`
- 签名：`StandDown()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:120`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.stand_down()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-as2-sportclient-recovery-stand-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.recovery_stand`

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

- 类：`unitree::robot::as2::SportClient`
- 签名：`RecoveryStand()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:126`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.recovery_stand()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-as2-sportclient-euler-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.euler`

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

- 类：`unitree::robot::as2::SportClient`
- 签名：`Euler(float, float, float)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:132`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.euler(roll=roll, pitch=pitch, yaw=yaw)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-as2-sportclient-move-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.move`

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

- 类：`unitree::robot::as2::SportClient`
- 签名：`Move(float, float, float)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:143`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.move(vx=vx, vy=vy, vyaw=vyaw)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-as2-sportclient-switch-gait-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.switch_gait`

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

- 类：`unitree::robot::as2::SportClient`
- 签名：`SwitchGait(int)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:154`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.switch_gait(gait_type=gait_type)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-as2-sportclient-body-height-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.body_height`

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

- 类：`unitree::robot::as2::SportClient`
- 签名：`BodyHeight(float)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:163`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.body_height(height=height)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-as2-sportclient-speed-level-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.speed_level`

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

- 类：`unitree::robot::as2::SportClient`
- 签名：`SpeedLevel(int)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:172`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.speed_level(level=level)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-as2-sportclient-body-position-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.body_position`

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

- 类：`unitree::robot::as2::SportClient`
- 签名：`BodyPosition(float, float, float, float)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:181`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.body_position(x=x, y=y, z=z, yaw=yaw)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-as2-sportclient-left-side-gait-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.left_side_gait`

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

- 类：`unitree::robot::as2::SportClient`
- 签名：`LeftSideGait(int)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:193`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.left_side_gait(enter=enter)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-as2-sportclient-right-side-gait-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.right_side_gait`

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

- 类：`unitree::robot::as2::SportClient`
- 签名：`RightSideGait(int)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:202`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.right_side_gait(enter=enter)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-as2-sportclient-hand-stand-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.hand_stand`

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

- 类：`unitree::robot::as2::SportClient`
- 签名：`HandStand(int)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:211`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.hand_stand(enter=enter)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-as2-sportclient-biped-stand-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.biped_stand`

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

- 类：`unitree::robot::as2::SportClient`
- 签名：`BipedStand(int)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:220`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.biped_stand(enter=enter)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-as2-sportclient-front-flip-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.front_flip`

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

- 类：`unitree::robot::as2::SportClient`
- 签名：`FrontFlip()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:229`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.front_flip()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-as2-sportclient-back-flip-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.back_flip`

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

- 类：`unitree::robot::as2::SportClient`
- 签名：`BackFlip()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:235`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.back_flip()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-as2-sportclient-greeting-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.greeting`

对应 C++ SDK 操作 `Greeting()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def greeting(self) -> int
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

- 类：`unitree::robot::as2::SportClient`
- 签名：`Greeting()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:241`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.greeting()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-as2-sportclient-heart-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.heart`

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

- 类：`unitree::robot::as2::SportClient`
- 签名：`Heart()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:247`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.heart()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-as2-sportclient-content-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.content`

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

- 类：`unitree::robot::as2::SportClient`
- 签名：`Content()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:253`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.content()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-as2-sportclient-dance1-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.dance1`

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

- 类：`unitree::robot::as2::SportClient`
- 签名：`Dance1()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:259`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.dance1()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-as2-sportclient-dance2-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.dance2`

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

- 类：`unitree::robot::as2::SportClient`
- 签名：`Dance2()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:265`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.dance2()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-as2-sportclient-handshake-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.handshake`

对应 C++ SDK 操作 `Handshake()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def handshake(self) -> int
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

- 类：`unitree::robot::as2::SportClient`
- 签名：`Handshake()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:271`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.handshake()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-as2-sportclient-stretch-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.stretch`

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

- 类：`unitree::robot::as2::SportClient`
- 签名：`Stretch()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:277`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.stretch()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-as2-sportclient-sit-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.sit`

对应 C++ SDK 操作 `Sit(int)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def sit(self, enter: int) -> int
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

- 类：`unitree::robot::as2::SportClient`
- 签名：`Sit(int)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:283`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.sit(enter=enter)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-as2-sportclient-front-jump-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.front_jump`

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

- 类：`unitree::robot::as2::SportClient`
- 签名：`FrontJump()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:292`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.front_jump()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-as2-sportclient-push-up-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.push_up`

对应 C++ SDK 操作 `PushUp()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def push_up(self) -> int
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

- 类：`unitree::robot::as2::SportClient`
- 签名：`PushUp()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:298`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.push_up()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-as2-sportclient-up-jump-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.up_jump`

对应 C++ SDK 操作 `UpJump()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def up_jump(self) -> int
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

- 类：`unitree::robot::as2::SportClient`
- 签名：`UpJump()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:304`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.up_jump()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-as2-sportclient-set-auto-recovery-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.set_auto_recovery`

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

- 类：`unitree::robot::as2::SportClient`
- 签名：`SetAutoRecovery(int)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:310`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.set_auto_recovery(switch_on=switch_on)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-as2-sportclient-switch-joystick-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.switch_joystick`

对应 C++ SDK 操作 `SwitchJoystick(int)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def switch_joystick(self, switch_on: int) -> int
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

- 类：`unitree::robot::as2::SportClient`
- 签名：`SwitchJoystick(int)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:319`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.switch_joystick(switch_on=switch_on)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-as2-sportclient-get-state-1"></a>
#### `unitree_sdk2_cpp.robot.as2.SportClient.get_state`

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

- 类：`unitree::robot::as2::SportClient`
- 签名：`GetState(std::map<std::string, std::string> &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/as2/sport/sport_client.hpp:328`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, state_map = obj.get_state()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

---

[返回 API 总索引](../API_REFERENCE_ZH.md)
