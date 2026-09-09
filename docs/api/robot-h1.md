# Unitree SDK2 Python API 参考分卷

[返回 API 总索引](../API_REFERENCE_ZH.md) · [阅读从零开始指南](../BEGINNER_GUIDE_ZH.md)

> [!WARNING]
> 本分卷同时包含 `AVAILABLE` 和 `SIGNATURE_ONLY`。后者只是设计期类型签名。运动及硬件副作用方法即使标记为 `AVAILABLE`，也不表示当前环境可安全执行。

> [!NOTE]
> 本文件由 `generator/generate_api_docs.py` 自动生成，请勿手工维护 API 条目。

---

<a id="unitree-sdk2-cpp-robot-h1"></a>
## H1 Robot API

模块：`unitree_sdk2_cpp.robot.h1`

### 类索引

| 类 | 公开函数签名 | 属性 |
| --- | ---: | ---: |
| [`JsonizeDataVecFloat`](#unitree-sdk2-cpp-robot-h1-jsonizedatavecfloat) | 3 | 0 |
| [`JsonizeTargetPos`](#unitree-sdk2-cpp-robot-h1-jsonizetargetpos) | 3 | 0 |
| [`JsonizeVelocityCommand`](#unitree-sdk2-cpp-robot-h1-jsonizevelocitycommand) | 3 | 0 |
| [`LocoClient`](#unitree-sdk2-cpp-robot-h1-lococlient) | 34 | 0 |

<a id="unitree-sdk2-cpp-robot-h1-jsonizedatavecfloat"></a>
### `unitree_sdk2_cpp.robot.h1.JsonizeDataVecFloat`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot.h1 import JsonizeDataVecFloat
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `data` | `list[float]` | 传给该接口的 数据 参数，Python 类型为 `list[float]`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.data` / `obj.data = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-h1-jsonizedatavecfloat-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-h1-jsonizedatavecfloat-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-h1-jsonizedatavecfloat-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-h1-jsonizedatavecfloat-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.h1.JsonizeDataVecFloat.__init__`

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

- 类：`unitree::robot::h1::JsonizeDataVecFloat`
- 签名：`JsonizeDataVecFloat()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_api.hpp:41`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = JsonizeDataVecFloat()
```

<a id="unitree-sdk2-cpp-robot-h1-jsonizedatavecfloat-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.h1.JsonizeDataVecFloat.from_json`

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

- 类：`unitree::robot::h1::JsonizeDataVecFloat`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_api.hpp:44`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-h1-jsonizedatavecfloat-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.h1.JsonizeDataVecFloat.to_json`

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

- 类：`unitree::robot::h1::JsonizeDataVecFloat`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_api.hpp:46`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-h1-jsonizetargetpos"></a>
### `unitree_sdk2_cpp.robot.h1.JsonizeTargetPos`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot.h1 import JsonizeTargetPos
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `x` | `float` | X 方向位置或分量参数。参考系、单位和范围必须查当前方法及目标型号协议。 | `value = obj.x` / `obj.x = value` |
| `y` | `float` | Y 方向位置或分量参数。参考系、单位和范围必须查当前方法及目标型号协议。 | `value = obj.y` / `obj.y = value` |
| `yaw` | `float` | 偏航角或偏航目标参数。参考系、单位和范围必须查目标型号协议。 | `value = obj.yaw` / `obj.yaw = value` |
| `relative` | `bool` | 传给该接口的 `relative` 参数，Python 类型为 `bool`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.relative` / `obj.relative = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-h1-jsonizetargetpos-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-h1-jsonizetargetpos-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-h1-jsonizetargetpos-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-h1-jsonizetargetpos-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.h1.JsonizeTargetPos.__init__`

初始化 `JsonizeTargetPos` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::h1::JsonizeTargetPos`
- 签名：`JsonizeTargetPos()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_api.hpp:72`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = JsonizeTargetPos()
```

<a id="unitree-sdk2-cpp-robot-h1-jsonizetargetpos-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.h1.JsonizeTargetPos.from_json`

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

- 类：`unitree::robot::h1::JsonizeTargetPos`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_api.hpp:75`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-h1-jsonizetargetpos-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.h1.JsonizeTargetPos.to_json`

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

- 类：`unitree::robot::h1::JsonizeTargetPos`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_api.hpp:82`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-h1-jsonizevelocitycommand"></a>
### `unitree_sdk2_cpp.robot.h1.JsonizeVelocityCommand`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot.h1 import JsonizeVelocityCommand
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
| [`__init__`](#unitree-sdk2-cpp-robot-h1-jsonizevelocitycommand-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-h1-jsonizevelocitycommand-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-h1-jsonizevelocitycommand-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-h1-jsonizevelocitycommand-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.h1.JsonizeVelocityCommand.__init__`

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

- 类：`unitree::robot::h1::JsonizeVelocityCommand`
- 签名：`JsonizeVelocityCommand()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_api.hpp:53`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = JsonizeVelocityCommand()
```

<a id="unitree-sdk2-cpp-robot-h1-jsonizevelocitycommand-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.h1.JsonizeVelocityCommand.from_json`

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

- 类：`unitree::robot::h1::JsonizeVelocityCommand`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_api.hpp:56`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-h1-jsonizevelocitycommand-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.h1.JsonizeVelocityCommand.to_json`

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

- 类：`unitree::robot::h1::JsonizeVelocityCommand`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_api.hpp:61`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-h1-lococlient"></a>
### `unitree_sdk2_cpp.robot.h1.LocoClient`

Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

**导入**

```python
from unitree_sdk2_cpp.robot.h1 import LocoClient
```

**基类**：`Client`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-h1-lococlient-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`init`](#unitree-sdk2-cpp-robot-h1-lococlient-init-1) | `def init(self) -> None` | `AVAILABLE` | `INITIALIZATION` |
| [`get_fsm_id`](#unitree-sdk2-cpp-robot-h1-lococlient-get-fsm-id-1) | `def get_fsm_id(self) -> tuple[int, int]` | `AVAILABLE` | `READ_ONLY` |
| [`get_fsm_mode`](#unitree-sdk2-cpp-robot-h1-lococlient-get-fsm-mode-1) | `def get_fsm_mode(self) -> tuple[int, int]` | `AVAILABLE` | `READ_ONLY` |
| [`get_balance_mode`](#unitree-sdk2-cpp-robot-h1-lococlient-get-balance-mode-1) | `def get_balance_mode(self) -> tuple[int, int]` | `AVAILABLE` | `READ_ONLY` |
| [`get_swing_height`](#unitree-sdk2-cpp-robot-h1-lococlient-get-swing-height-1) | `def get_swing_height(self) -> tuple[int, float]` | `AVAILABLE` | `READ_ONLY` |
| [`get_stand_height`](#unitree-sdk2-cpp-robot-h1-lococlient-get-stand-height-1) | `def get_stand_height(self) -> tuple[int, float]` | `AVAILABLE` | `READ_ONLY` |
| [`get_phase`](#unitree-sdk2-cpp-robot-h1-lococlient-get-phase-1) | `def get_phase(self) -> tuple[int, list[float]]` | `AVAILABLE` | `READ_ONLY` |
| [`enable_odom`](#unitree-sdk2-cpp-robot-h1-lococlient-enable-odom-1) | `def enable_odom(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`disable_odom`](#unitree-sdk2-cpp-robot-h1-lococlient-disable-odom-1) | `def disable_odom(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`get_odom`](#unitree-sdk2-cpp-robot-h1-lococlient-get-odom-1) | `def get_odom(self) -> tuple[int, float, float, float]` | `AVAILABLE` | `READ_ONLY` |
| [`set_fsm_id`](#unitree-sdk2-cpp-robot-h1-lococlient-set-fsm-id-1) | `def set_fsm_id(self, fsm_id: int) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`set_balance_mode`](#unitree-sdk2-cpp-robot-h1-lococlient-set-balance-mode-1) | `def set_balance_mode(self, balance_mode: int) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`set_swing_height`](#unitree-sdk2-cpp-robot-h1-lococlient-set-swing-height-1) | `def set_swing_height(self, swing_height: float) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`set_stand_height`](#unitree-sdk2-cpp-robot-h1-lococlient-set-stand-height-1) | `def set_stand_height(self, stand_height: float) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`set_velocity`](#unitree-sdk2-cpp-robot-h1-lococlient-set-velocity-1) | `def set_velocity(self, vx: float, vy: float, omega: float, duration: float = 1.0) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`set_phase`](#unitree-sdk2-cpp-robot-h1-lococlient-set-phase-1) | `def set_phase(self, phase: Sequence[float]) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`set_target_pos`](#unitree-sdk2-cpp-robot-h1-lococlient-set-target-pos-1) | `def set_target_pos(self, x: float, y: float, yaw: float, relative: bool = True) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`set_task_id`](#unitree-sdk2-cpp-robot-h1-lococlient-set-task-id-1) | `def set_task_id(self, task_id: int) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`damp`](#unitree-sdk2-cpp-robot-h1-lococlient-damp-1) | `def damp(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`start`](#unitree-sdk2-cpp-robot-h1-lococlient-start-1) | `def start(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`stand_up`](#unitree-sdk2-cpp-robot-h1-lococlient-stand-up-1) | `def stand_up(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`zero_torque`](#unitree-sdk2-cpp-robot-h1-lococlient-zero-torque-1) | `def zero_torque(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`stop_move`](#unitree-sdk2-cpp-robot-h1-lococlient-stop-move-1) | `def stop_move(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`high_stand`](#unitree-sdk2-cpp-robot-h1-lococlient-high-stand-1) | `def high_stand(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`low_stand`](#unitree-sdk2-cpp-robot-h1-lococlient-low-stand-1) | `def low_stand(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`move（重载 1/2）`](#unitree-sdk2-cpp-robot-h1-lococlient-move-1) | `def move(self, vx: float, vy: float, vyaw: float, continous_move: bool) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`move（重载 2/2）`](#unitree-sdk2-cpp-robot-h1-lococlient-move-2) | `def move(self, vx: float, vy: float, vyaw: float) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`balance_stand`](#unitree-sdk2-cpp-robot-h1-lococlient-balance-stand-1) | `def balance_stand(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`continuous_gait`](#unitree-sdk2-cpp-robot-h1-lococlient-continuous-gait-1) | `def continuous_gait(self, flag: bool) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`switch_move_mode`](#unitree-sdk2-cpp-robot-h1-lococlient-switch-move-mode-1) | `def switch_move_mode(self, flag: bool) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`set_next_foot`](#unitree-sdk2-cpp-robot-h1-lococlient-set-next-foot-1) | `def set_next_foot(self, foot: bool) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`wave_hand`](#unitree-sdk2-cpp-robot-h1-lococlient-wave-hand-1) | `def wave_hand(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`shake_hand`](#unitree-sdk2-cpp-robot-h1-lococlient-shake-hand-1) | `def shake_hand(self, stage: int = -1) -> int` | `AVAILABLE` | `MOTION_COMMAND` |

<a id="unitree-sdk2-cpp-robot-h1-lococlient-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.__init__`

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

- 类：`unitree::robot::h1::LocoClient`
- 签名：`LocoClient()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:14`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = LocoClient()
```

<a id="unitree-sdk2-cpp-robot-h1-lococlient-init-1"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.init`

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

- 类：`unitree::robot::h1::LocoClient`
- 签名：`Init()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:18`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.init()
```

<a id="unitree-sdk2-cpp-robot-h1-lococlient-get-fsm-id-1"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.get_fsm_id`

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

- 类：`unitree::robot::h1::LocoClient`
- 签名：`GetFsmId(int &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:42`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, fsm_id = obj.get_fsm_id()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-h1-lococlient-get-fsm-mode-1"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.get_fsm_mode`

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

- 类：`unitree::robot::h1::LocoClient`
- 签名：`GetFsmMode(int &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:54`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, fsm_mode = obj.get_fsm_mode()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-h1-lococlient-get-balance-mode-1"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.get_balance_mode`

查询或检查 平衡 模式。

**签名**

```python
def get_balance_mode(self) -> tuple[int, int]
```

**可用性与安全性**

**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现只读查询。Robot Client 的服务端查询通常仍需匹配的 Linux 扩展、DDS、网络、机器人和服务；纯本地 getter 则不一定需要全部条件。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| [0] `status` | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。 |
| [1] `balance_mode` | `int` | 传给该接口的 平衡 模式 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `balance_mode: int &`。 |

**对应 C++**

- 类：`unitree::robot::h1::LocoClient`
- 签名：`GetBalanceMode(int &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:66`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, balance_mode = obj.get_balance_mode()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-h1-lococlient-get-swing-height-1"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.get_swing_height`

查询或检查 `swing` 高度。

**签名**

```python
def get_swing_height(self) -> tuple[int, float]
```

**可用性与安全性**

**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现只读查询。Robot Client 的服务端查询通常仍需匹配的 Linux 扩展、DDS、网络、机器人和服务；纯本地 getter 则不一定需要全部条件。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| [0] `status` | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。 |
| [1] `swing_height` | `float` | 传给该接口的 `swing` 高度 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `swing_height: float &`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |

**对应 C++**

- 类：`unitree::robot::h1::LocoClient`
- 签名：`GetSwingHeight(float &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:78`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, swing_height = obj.get_swing_height()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-h1-lococlient-get-stand-height-1"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.get_stand_height`

查询或检查 `stand` 高度。

**签名**

```python
def get_stand_height(self) -> tuple[int, float]
```

**可用性与安全性**

**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现只读查询。Robot Client 的服务端查询通常仍需匹配的 Linux 扩展、DDS、网络、机器人和服务；纯本地 getter 则不一定需要全部条件。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| [0] `status` | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。 |
| [1] `stand_height` | `float` | 传给该接口的 `stand` 高度 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `stand_height: float &`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |

**对应 C++**

- 类：`unitree::robot::h1::LocoClient`
- 签名：`GetStandHeight(float &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:90`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, stand_height = obj.get_stand_height()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-h1-lococlient-get-phase-1"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.get_phase`

查询或检查 相位。

**签名**

```python
def get_phase(self) -> tuple[int, list[float]]
```

**可用性与安全性**

**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现只读查询。Robot Client 的服务端查询通常仍需匹配的 Linux 扩展、DDS、网络、机器人和服务；纯本地 getter 则不一定需要全部条件。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| [0] `status` | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。 |
| [1] `phase` | `list[float]` | 传给该接口的 相位 参数，Python 类型为 `list[float]`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `phase: std::vector<float> &`。 底层是可变长度 vector；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |

**对应 C++**

- 类：`unitree::robot::h1::LocoClient`
- 签名：`GetPhase(std::vector<float> &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:102`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, phase = obj.get_phase()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-h1-lococlient-enable-odom-1"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.enable_odom`

对应 C++ SDK 操作 `EnableOdom()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def enable_odom(self) -> int
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

- 类：`unitree::robot::h1::LocoClient`
- 签名：`EnableOdom()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:114`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.enable_odom()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-h1-lococlient-disable-odom-1"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.disable_odom`

对应 C++ SDK 操作 `DisableOdom()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def disable_odom(self) -> int
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

- 类：`unitree::robot::h1::LocoClient`
- 签名：`DisableOdom()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:119`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.disable_odom()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-h1-lococlient-get-odom-1"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.get_odom`

查询或检查 `odom`。

**签名**

```python
def get_odom(self) -> tuple[int, float, float, float]
```

**可用性与安全性**

**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现只读查询。Robot Client 的服务端查询通常仍需匹配的 Linux 扩展、DDS、网络、机器人和服务；纯本地 getter 则不一定需要全部条件。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| [0] `status` | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。 |
| [1] `x` | `float` | X 方向位置或分量参数。参考系、单位和范围必须查当前方法及目标型号协议。 对应 C++ 参数 `x: float &`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |
| [2] `y` | `float` | Y 方向位置或分量参数。参考系、单位和范围必须查当前方法及目标型号协议。 对应 C++ 参数 `y: float &`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |
| [3] `yaw` | `float` | 偏航角或偏航目标参数。参考系、单位和范围必须查目标型号协议。 对应 C++ 参数 `yaw: float &`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |

**对应 C++**

- 类：`unitree::robot::h1::LocoClient`
- 签名：`GetOdom(float &, float &, float &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:124`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, x, y, yaw = obj.get_odom()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-h1-lococlient-set-fsm-id-1"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.set_fsm_id`

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

- 类：`unitree::robot::h1::LocoClient`
- 签名：`SetFsmId(int)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:138`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.set_fsm_id(fsm_id=fsm_id)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-h1-lococlient-set-balance-mode-1"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.set_balance_mode`

设置 平衡 模式。具体副作用和安全边界见下方状态。

**签名**

```python
def set_balance_mode(self, balance_mode: int) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `balance_mode` | `int` | 必填 | 传给该接口的 平衡 模式 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `balance_mode: int`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::h1::LocoClient`
- 签名：`SetBalanceMode(int)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:148`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.set_balance_mode(balance_mode=balance_mode)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-h1-lococlient-set-swing-height-1"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.set_swing_height`

设置 `swing` 高度。具体副作用和安全边界见下方状态。

**签名**

```python
def set_swing_height(self, swing_height: float) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `swing_height` | `float` | 必填 | 传给该接口的 `swing` 高度 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `swing_height: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::h1::LocoClient`
- 签名：`SetSwingHeight(float)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:158`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.set_swing_height(swing_height=swing_height)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-h1-lococlient-set-stand-height-1"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.set_stand_height`

设置 `stand` 高度。具体副作用和安全边界见下方状态。

**签名**

```python
def set_stand_height(self, stand_height: float) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `stand_height` | `float` | 必填 | 传给该接口的 `stand` 高度 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `stand_height: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::h1::LocoClient`
- 签名：`SetStandHeight(float)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:168`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.set_stand_height(stand_height=stand_height)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-h1-lococlient-set-velocity-1"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.set_velocity`

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

- 类：`unitree::robot::h1::LocoClient`
- 签名：`SetVelocity(float, float, float, float)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:178`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.set_velocity(vx=vx, vy=vy, omega=omega, duration=duration)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-h1-lococlient-set-phase-1"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.set_phase`

设置 相位。具体副作用和安全边界见下方状态。

**签名**

```python
def set_phase(self, phase: Sequence[float]) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `phase` | `Sequence[float]` | 必填 | 传给该接口的 相位 参数，Python 类型为 `Sequence[float]`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `phase: std::vector<float>`。 底层是可变长度 vector；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::h1::LocoClient`
- 签名：`SetPhase(std::vector<float>)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:190`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.set_phase(phase=phase)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-h1-lococlient-set-target-pos-1"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.set_target_pos`

设置 `target` `pos`。具体副作用和安全边界见下方状态。

**签名**

```python
def set_target_pos(self, x: float, y: float, yaw: float, relative: bool = True) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `x` | `float` | 必填 | X 方向位置或分量参数。参考系、单位和范围必须查当前方法及目标型号协议。 对应 C++ 参数 `x: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |
| `y` | `float` | 必填 | Y 方向位置或分量参数。参考系、单位和范围必须查当前方法及目标型号协议。 对应 C++ 参数 `y: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |
| `yaw` | `float` | 必填 | 偏航角或偏航目标参数。参考系、单位和范围必须查目标型号协议。 对应 C++ 参数 `yaw: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |
| `relative` | `bool` | `True` | 传给该接口的 `relative` 参数，Python 类型为 `bool`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `relative: bool`。 只接受布尔语义。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::h1::LocoClient`
- 签名：`SetTargetPos(float, float, float, bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:200`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.set_target_pos(x=x, y=y, yaw=yaw, relative=relative)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-h1-lococlient-set-task-id-1"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.set_task_id`

设置 任务 ID。具体副作用和安全边界见下方状态。

**签名**

```python
def set_task_id(self, task_id: int) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `task_id` | `int` | 必填 | 传给该接口的 任务 ID 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `task_id: int`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::h1::LocoClient`
- 签名：`SetTaskId(int)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:213`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.set_task_id(task_id=task_id)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-h1-lococlient-damp-1"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.damp`

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

- 类：`unitree::robot::h1::LocoClient`
- 签名：`Damp()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:224`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.damp()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-h1-lococlient-start-1"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.start`

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

- 类：`unitree::robot::h1::LocoClient`
- 签名：`Start()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:226`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.start()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-h1-lococlient-stand-up-1"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.stand_up`

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

- 类：`unitree::robot::h1::LocoClient`
- 签名：`StandUp()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:228`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.stand_up()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-h1-lococlient-zero-torque-1"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.zero_torque`

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

- 类：`unitree::robot::h1::LocoClient`
- 签名：`ZeroTorque()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:230`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.zero_torque()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-h1-lococlient-stop-move-1"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.stop_move`

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

- 类：`unitree::robot::h1::LocoClient`
- 签名：`StopMove()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:232`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.stop_move()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-h1-lococlient-high-stand-1"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.high_stand`

对应 C++ SDK 操作 `HighStand()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def high_stand(self) -> int
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

- 类：`unitree::robot::h1::LocoClient`
- 签名：`HighStand()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:234`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.high_stand()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-h1-lococlient-low-stand-1"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.low_stand`

对应 C++ SDK 操作 `LowStand()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def low_stand(self) -> int
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

- 类：`unitree::robot::h1::LocoClient`
- 签名：`LowStand()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:236`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.low_stand()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-h1-lococlient-move-1"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.move`（重载 1/2）

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

- 类：`unitree::robot::h1::LocoClient`
- 签名：`Move(float, float, float, bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:238`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.move(vx=vx, vy=vy, vyaw=vyaw, continous_move=continous_move)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-h1-lococlient-move-2"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.move`（重载 2/2）

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

- 类：`unitree::robot::h1::LocoClient`
- 签名：`Move(float, float, float)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:242`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.move(vx=vx, vy=vy, vyaw=vyaw)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-h1-lococlient-balance-stand-1"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.balance_stand`

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

- 类：`unitree::robot::h1::LocoClient`
- 签名：`BalanceStand()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:244`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.balance_stand()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-h1-lococlient-continuous-gait-1"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.continuous_gait`

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

- 类：`unitree::robot::h1::LocoClient`
- 签名：`ContinuousGait(bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:246`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.continuous_gait(flag=flag)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-h1-lococlient-switch-move-mode-1"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.switch_move_mode`

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

- 类：`unitree::robot::h1::LocoClient`
- 签名：`SwitchMoveMode(bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:248`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.switch_move_mode(flag=flag)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-h1-lococlient-set-next-foot-1"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.set_next_foot`

设置 `next` `foot`。具体副作用和安全边界见下方状态。

**签名**

```python
def set_next_foot(self, foot: bool) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `foot` | `bool` | 必填 | 传给该接口的 `foot` 参数，Python 类型为 `bool`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `foot: bool`。 只接受布尔语义。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::h1::LocoClient`
- 签名：`SetNextFoot(bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:253`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.set_next_foot(foot=foot)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-h1-lococlient-wave-hand-1"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.wave_hand`

对应 C++ SDK 操作 `WaveHand()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def wave_hand(self) -> int
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

- 类：`unitree::robot::h1::LocoClient`
- 签名：`WaveHand()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:257`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.wave_hand()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-h1-lococlient-shake-hand-1"></a>
#### `unitree_sdk2_cpp.robot.h1.LocoClient.shake_hand`

对应 C++ SDK 操作 `ShakeHand(int)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def shake_hand(self, stage: int = -1) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `stage` | `int` | `-1` | 传给该接口的 `stage` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `stage: int`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::h1::LocoClient`
- 签名：`ShakeHand(int)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/h1/loco/h1_loco_client.hpp:259`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.shake_hand(stage=stage)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

---

[返回 API 总索引](../API_REFERENCE_ZH.md)
