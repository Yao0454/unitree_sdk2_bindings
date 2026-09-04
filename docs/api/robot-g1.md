# Unitree SDK2 Python API 参考分卷

[返回 API 总索引](../API_REFERENCE_ZH.md) · [阅读从零开始指南](../BEGINNER_GUIDE_ZH.md)

> [!WARNING]
> 本分卷同时包含 `AVAILABLE` 和 `SIGNATURE_ONLY`。后者只是设计期类型签名。运动及硬件副作用方法即使标记为 `AVAILABLE`，也不表示当前环境可安全执行。

> [!NOTE]
> 本文件由 `generator/generate_api_docs.py` 自动生成，请勿手工维护 API 条目。

---

<a id="unitree-sdk2-cpp-robot-g1"></a>
## G1 Robot API

模块：`unitree_sdk2_cpp.robot.g1`

### 模块函数导入

```python
from unitree_sdk2_cpp.robot.g1 import bad_orientation, joint_vel_out_of_limit, ang_vel_out_of_limit, motor_winding_overheat, motor_casing_overheat, low_battery, lost_connection
```

下面的函数用法片段假设已经完成上述导入。

### 模块函数索引

| 函数 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`bad_orientation()`](#unitree-sdk2-cpp-robot-g1-bad-orientation-1) | `def bad_orientation(low_state: LowState, limit_angle: float = 1.0) -> bool` | `AVAILABLE` | `SAFETY_CHECK` |
| [`joint_vel_out_of_limit()`](#unitree-sdk2-cpp-robot-g1-joint-vel-out-of-limit-1) | `def joint_vel_out_of_limit(low_state: LowState, limit_vel: float = 10.0) -> bool` | `AVAILABLE` | `SAFETY_CHECK` |
| [`ang_vel_out_of_limit()`](#unitree-sdk2-cpp-robot-g1-ang-vel-out-of-limit-1) | `def ang_vel_out_of_limit(low_state: LowState, limit_vel: float = 6.0) -> bool` | `AVAILABLE` | `SAFETY_CHECK` |
| [`motor_winding_overheat()`](#unitree-sdk2-cpp-robot-g1-motor-winding-overheat-1) | `def motor_winding_overheat(low_state: LowState, limit_temp: float = 120.0) -> bool` | `AVAILABLE` | `SAFETY_CHECK` |
| [`motor_casing_overheat()`](#unitree-sdk2-cpp-robot-g1-motor-casing-overheat-1) | `def motor_casing_overheat(low_state: LowState, limit_temp: float = 85.0) -> bool` | `AVAILABLE` | `SAFETY_CHECK` |
| [`low_battery()`](#unitree-sdk2-cpp-robot-g1-low-battery-1) | `def low_battery(bms_state: BmsState, limit_soc: float = 20.0) -> bool` | `AVAILABLE` | `SAFETY_CHECK` |
| [`lost_connection()`](#unitree-sdk2-cpp-robot-g1-lost-connection-1) | `def lost_connection(subscriber: ChannelSubscriber[LowState], timeout_ms: int = 1000) -> bool` | `AVAILABLE` | `SAFETY_CHECK` |

### 类索引

| 类                                                                             | 公开函数签名 |  属性 |     |
| ----------------------------------------------------------------------------- | -----: | --: | --- |
| [`InternalFsmMode`](#unitree-sdk2-cpp-robot-g1-internalfsmmode)               |      0 |   0 |     |
| [`AgvClient`](#unitree-sdk2-cpp-robot-g1-agvclient)                           |      4 |   0 |     |
| [`AudioClient`](#unitree-sdk2-cpp-robot-g1-audioclient)                       |      8 |   0 |     |
| [`G1ArmActionClient`](#unitree-sdk2-cpp-robot-g1-g1armactionclient)           |     f6 |   0 |     |
| [`JsonizeDataVecFloat`](#unitree-sdk2-cpp-robot-g1-jsonizedatavecfloat)       |      3 |   0 |     |
| [`JsonizeVelocityCommand`](#unitree-sdk2-cpp-robot-g1-jsonizevelocitycommand) |      3 |   0 |     |
| [`LedControlParameter`](#unitree-sdk2-cpp-robot-g1-ledcontrolparameter)       |      3 |   0 |     |
| [`LocoClient`](#unitree-sdk2-cpp-robot-g1-lococlient)                         |     35 |   0 |     |
| [`MoveParameter`](#unitree-sdk2-cpp-robot-g1-moveparameter)                   |      3 |   0 |     |
| [`PlayStopParameter`](#unitree-sdk2-cpp-robot-g1-playstopparameter)           |      3 |   0 |     |
| [`PlayStreamParameter`](#unitree-sdk2-cpp-robot-g1-playstreamparameter)       |      3 |   0 |     |
| [`TtsMakerParameter`](#unitree-sdk2-cpp-robot-g1-ttsmakerparameter)           |      3 |   0 |     |

<a id="unitree-sdk2-cpp-robot-g1-bad-orientation-1"></a>
#### `unitree_sdk2_cpp.robot.g1.bad_orientation`

对应 C++ SDK 操作 `bad_orientation(const unitree_hg::msg::dds_::LowState_ &, float)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def bad_orientation(low_state: LowState, limit_angle: float = 1.0) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `SAFETY_CHECK`**：当前绑定源码已实现；实际执行条件仍取决于平台和对应 SDK 环境。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `low_state` | `LowState` | 必填 | 传给该接口的 `low` 状态 参数，Python 类型为 `LowState`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 |
| `limit_angle` | `float` | `1.0` | 传给该接口的 `limit` `angle` 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree::robot::g1`
- 签名：`bad_orientation(const unitree_hg::msg::dds_::LowState_ &, float)`
- 绑定策略：`DIRECT`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = bad_orientation(low_state=low_state, limit_angle=limit_angle)
```

<a id="unitree-sdk2-cpp-robot-g1-joint-vel-out-of-limit-1"></a>
#### `unitree_sdk2_cpp.robot.g1.joint_vel_out_of_limit`

对应 C++ SDK 操作 `joint_vel_out_of_limit(const unitree_hg::msg::dds_::LowState_ &, float)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def joint_vel_out_of_limit(low_state: LowState, limit_vel: float = 10.0) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `SAFETY_CHECK`**：当前绑定源码已实现；实际执行条件仍取决于平台和对应 SDK 环境。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `low_state` | `LowState` | 必填 | 传给该接口的 `low` 状态 参数，Python 类型为 `LowState`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 |
| `limit_vel` | `float` | `10.0` | 传给该接口的 `limit` `vel` 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree::robot::g1`
- 签名：`joint_vel_out_of_limit(const unitree_hg::msg::dds_::LowState_ &, float)`
- 绑定策略：`DIRECT`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = joint_vel_out_of_limit(low_state=low_state, limit_vel=limit_vel)
```

<a id="unitree-sdk2-cpp-robot-g1-ang-vel-out-of-limit-1"></a>
#### `unitree_sdk2_cpp.robot.g1.ang_vel_out_of_limit`

对应 C++ SDK 操作 `ang_vel_out_of_limit(const unitree_hg::msg::dds_::LowState_ &, float)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def ang_vel_out_of_limit(low_state: LowState, limit_vel: float = 6.0) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `SAFETY_CHECK`**：当前绑定源码已实现；实际执行条件仍取决于平台和对应 SDK 环境。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `low_state` | `LowState` | 必填 | 传给该接口的 `low` 状态 参数，Python 类型为 `LowState`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 |
| `limit_vel` | `float` | `6.0` | 传给该接口的 `limit` `vel` 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree::robot::g1`
- 签名：`ang_vel_out_of_limit(const unitree_hg::msg::dds_::LowState_ &, float)`
- 绑定策略：`DIRECT`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = ang_vel_out_of_limit(low_state=low_state, limit_vel=limit_vel)
```

<a id="unitree-sdk2-cpp-robot-g1-motor-winding-overheat-1"></a>
#### `unitree_sdk2_cpp.robot.g1.motor_winding_overheat`

对应 C++ SDK 操作 `motor_winding_overheat(const unitree_hg::msg::dds_::LowState_ &, float)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def motor_winding_overheat(low_state: LowState, limit_temp: float = 120.0) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `SAFETY_CHECK`**：当前绑定源码已实现；实际执行条件仍取决于平台和对应 SDK 环境。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `low_state` | `LowState` | 必填 | 传给该接口的 `low` 状态 参数，Python 类型为 `LowState`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 |
| `limit_temp` | `float` | `120.0` | 传给该接口的 `limit` `temp` 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree::robot::g1`
- 签名：`motor_winding_overheat(const unitree_hg::msg::dds_::LowState_ &, float)`
- 绑定策略：`DIRECT`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = motor_winding_overheat(low_state=low_state, limit_temp=limit_temp)
```

<a id="unitree-sdk2-cpp-robot-g1-motor-casing-overheat-1"></a>
#### `unitree_sdk2_cpp.robot.g1.motor_casing_overheat`

对应 C++ SDK 操作 `motor_casing_overheat(const unitree_hg::msg::dds_::LowState_ &, float)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def motor_casing_overheat(low_state: LowState, limit_temp: float = 85.0) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `SAFETY_CHECK`**：当前绑定源码已实现；实际执行条件仍取决于平台和对应 SDK 环境。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `low_state` | `LowState` | 必填 | 传给该接口的 `low` 状态 参数，Python 类型为 `LowState`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 |
| `limit_temp` | `float` | `85.0` | 传给该接口的 `limit` `temp` 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree::robot::g1`
- 签名：`motor_casing_overheat(const unitree_hg::msg::dds_::LowState_ &, float)`
- 绑定策略：`DIRECT`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = motor_casing_overheat(low_state=low_state, limit_temp=limit_temp)
```

<a id="unitree-sdk2-cpp-robot-g1-low-battery-1"></a>
#### `unitree_sdk2_cpp.robot.g1.low_battery`

对应 C++ SDK 操作 `low_battery(const unitree_hg::msg::dds_::BmsState_ &, float)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def low_battery(bms_state: BmsState, limit_soc: float = 20.0) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `SAFETY_CHECK`**：当前绑定源码已实现；实际执行条件仍取决于平台和对应 SDK 环境。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `bms_state` | `BmsState` | 必填 | 传给该接口的 `bms` 状态 参数，Python 类型为 `BmsState`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 |
| `limit_soc` | `float` | `20.0` | 传给该接口的 `limit` `soc` 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree::robot::g1`
- 签名：`low_battery(const unitree_hg::msg::dds_::BmsState_ &, float)`
- 绑定策略：`DIRECT`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = low_battery(bms_state=bms_state, limit_soc=limit_soc)
```

<a id="unitree-sdk2-cpp-robot-g1-lost-connection-1"></a>
#### `unitree_sdk2_cpp.robot.g1.lost_connection`

对应 C++ SDK 操作 `lost_connection(unitree::robot::ChannelSubscriberPtr<unitree_hg::msg::dds_::LowState_> &, int64_t)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def lost_connection(subscriber: ChannelSubscriber[LowState], timeout_ms: int = 1000) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `SAFETY_CHECK`**：当前绑定源码已实现；实际执行条件仍取决于平台和对应 SDK 环境。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `subscriber` | `ChannelSubscriber[LowState]` | 必填 | 传给该接口的 `subscriber` 参数，Python 类型为 `ChannelSubscriber[LowState]`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 |
| `timeout_ms` | `int` | `1000` | 传给该接口的 超时 `ms` 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree::robot::g1`
- 签名：`lost_connection(unitree::robot::ChannelSubscriberPtr<unitree_hg::msg::dds_::LowState_> &, int64_t)`
- 绑定策略：`TYPE_ERASED_ADAPTER`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = lost_connection(subscriber=subscriber, timeout_ms=timeout_ms)
```

<a id="unitree-sdk2-cpp-robot-g1-internalfsmmode"></a>
### `unitree_sdk2_cpp.robot.g1.InternalFsmMode`

SDK 整数枚举。枚举成员和值以目标版本头文件为准。

**导入**

```python
from unitree_sdk2_cpp.robot.g1 import InternalFsmMode
```

**基类**：`enum.IntEnum`

**枚举成员**

| 名称 | Stub 值 |
| --- | --- |
| `LAST` | `...` |
| `PASSIVE` | `...` |
| `WALKRUN` | `...` |

<a id="unitree-sdk2-cpp-robot-g1-agvclient"></a>
### `unitree_sdk2_cpp.robot.g1.AgvClient`

Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

**导入**

```python
from unitree_sdk2_cpp.robot.g1 import AgvClient
```

**基类**：`Client`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-g1-agvclient-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`init`](#unitree-sdk2-cpp-robot-g1-agvclient-init-1) | `def init(self) -> None` | `AVAILABLE` | `INITIALIZATION` |
| [`move`](#unitree-sdk2-cpp-robot-g1-agvclient-move-1) | `def move(self, vx: float, vy: float, vyaw: float) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`height_adjust`](#unitree-sdk2-cpp-robot-g1-agvclient-height-adjust-1) | `def height_adjust(self, vz: float) -> int` | `AVAILABLE` | `MOTION_COMMAND` |

<a id="unitree-sdk2-cpp-robot-g1-agvclient-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.g1.AgvClient.__init__`

初始化 `AgvClient` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::g1::AgvClient`
- 签名：`AgvClient()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/g1/agv/g1_agv_client.hpp:15`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = AgvClient()
```

<a id="unitree-sdk2-cpp-robot-g1-agvclient-init-1"></a>
#### `unitree_sdk2_cpp.robot.g1.AgvClient.init`

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

- 类：`unitree::robot::g1::AgvClient`
- 签名：`Init()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/agv/g1_agv_client.hpp:19`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.init()
```

<a id="unitree-sdk2-cpp-robot-g1-agvclient-move-1"></a>
#### `unitree_sdk2_cpp.robot.g1.AgvClient.move`

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

- 类：`unitree::robot::g1::AgvClient`
- 签名：`Move(float, float, float)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/agv/g1_agv_client.hpp:56`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.move(vx=vx, vy=vy, vyaw=vyaw)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-agvclient-height-adjust-1"></a>
#### `unitree_sdk2_cpp.robot.g1.AgvClient.height_adjust`

对应 C++ SDK 操作 `HeightAdjust(float)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def height_adjust(self, vz: float) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `vz` | `float` | 必填 | 传给该接口的 `vz` 参数，Python 类型为 `float`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `vz: float`。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::g1::AgvClient`
- 签名：`HeightAdjust(float)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/agv/g1_agv_client.hpp:93`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.height_adjust(vz=vz)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-audioclient"></a>
### `unitree_sdk2_cpp.robot.g1.AudioClient`

Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

**导入**

```python
from unitree_sdk2_cpp.robot.g1 import AudioClient
```

**基类**：`Client`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-g1-audioclient-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`init`](#unitree-sdk2-cpp-robot-g1-audioclient-init-1) | `def init(self) -> None` | `AVAILABLE` | `INITIALIZATION` |
| [`tts_maker`](#unitree-sdk2-cpp-robot-g1-audioclient-tts-maker-1) | `def tts_maker(self, text: str, speaker_id: int) -> int` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |
| [`get_volume`](#unitree-sdk2-cpp-robot-g1-audioclient-get-volume-1) | `def get_volume(self) -> tuple[int, int]` | `AVAILABLE` | `READ_ONLY` |
| [`set_volume`](#unitree-sdk2-cpp-robot-g1-audioclient-set-volume-1) | `def set_volume(self, volume: int) -> int` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |
| [`play_stream`](#unitree-sdk2-cpp-robot-g1-audioclient-play-stream-1) | `def play_stream(self, app_name: str, stream_id: str, pcm_data: Sequence[int]) -> int` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |
| [`play_stop`](#unitree-sdk2-cpp-robot-g1-audioclient-play-stop-1) | `def play_stop(self, app_name: str) -> int` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |
| [`led_control`](#unitree-sdk2-cpp-robot-g1-audioclient-led-control-1) | `def led_control(self, r: int, g: int, b: int) -> int` | `AVAILABLE` | `HARDWARE_SIDE_EFFECT` |

<a id="unitree-sdk2-cpp-robot-g1-audioclient-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.g1.AudioClient.__init__`

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

- 类：`unitree::robot::g1::AudioClient`
- 签名：`AudioClient()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/g1/audio/g1_audio_client.hpp:15`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = AudioClient()
```

<a id="unitree-sdk2-cpp-robot-g1-audioclient-init-1"></a>
#### `unitree_sdk2_cpp.robot.g1.AudioClient.init`

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

- 类：`unitree::robot::g1::AudioClient`
- 签名：`Init()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/audio/g1_audio_client.hpp:19`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.init()
```

<a id="unitree-sdk2-cpp-robot-g1-audioclient-tts-maker-1"></a>
#### `unitree_sdk2_cpp.robot.g1.AudioClient.tts_maker`

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

- 类：`unitree::robot::g1::AudioClient`
- 签名：`TtsMaker(const std::string &, int32_t)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/audio/g1_audio_client.hpp:31`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.tts_maker(text=text, speaker_id=speaker_id)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-audioclient-get-volume-1"></a>
#### `unitree_sdk2_cpp.robot.g1.AudioClient.get_volume`

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

- 类：`unitree::robot::g1::AudioClient`
- 签名：`GetVolume(uint8_t &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/g1/audio/g1_audio_client.hpp:43`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, volume = obj.get_volume()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-g1-audioclient-set-volume-1"></a>
#### `unitree_sdk2_cpp.robot.g1.AudioClient.set_volume`

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

- 类：`unitree::robot::g1::AudioClient`
- 签名：`SetVolume(uint8_t)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/audio/g1_audio_client.hpp:57`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.set_volume(volume=volume)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-audioclient-play-stream-1"></a>
#### `unitree_sdk2_cpp.robot.g1.AudioClient.play_stream`

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

- 类：`unitree::robot::g1::AudioClient`
- 签名：`PlayStream(std::string, std::string, std::vector<uint8_t>)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/audio/g1_audio_client.hpp:68`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.play_stream(app_name=app_name, stream_id=stream_id, pcm_data=pcm_data)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-audioclient-play-stop-1"></a>
#### `unitree_sdk2_cpp.robot.g1.AudioClient.play_stop`

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

- 类：`unitree::robot::g1::AudioClient`
- 签名：`PlayStop(std::string)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/audio/g1_audio_client.hpp:80`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.play_stop(app_name=app_name)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-audioclient-led-control-1"></a>
#### `unitree_sdk2_cpp.robot.g1.AudioClient.led_control`

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

- 类：`unitree::robot::g1::AudioClient`
- 签名：`LedControl(uint8_t, uint8_t, uint8_t)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/audio/g1_audio_client.hpp:91`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.led_control(r=r, g=g, b=b)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-g1armactionclient"></a>
### `unitree_sdk2_cpp.robot.g1.G1ArmActionClient`

Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

**导入**

```python
from unitree_sdk2_cpp.robot.g1 import G1ArmActionClient
```

**基类**：`Client`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `action_map` | `dict[str, int]` | 传给该接口的 `action` `map` 参数，Python 类型为 `dict[str, int]`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.action_map` / `obj.action_map = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-g1-g1armactionclient-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`init`](#unitree-sdk2-cpp-robot-g1-g1armactionclient-init-1) | `def init(self) -> None` | `AVAILABLE` | `INITIALIZATION` |
| [`execute_action（重载 1/2）`](#unitree-sdk2-cpp-robot-g1-g1armactionclient-execute-action-1) | `def execute_action(self, action_id: int) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`execute_action（重载 2/2）`](#unitree-sdk2-cpp-robot-g1-g1armactionclient-execute-action-2) | `def execute_action(self, action_name: str) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`stop_custom_action`](#unitree-sdk2-cpp-robot-g1-g1armactionclient-stop-custom-action-1) | `def stop_custom_action(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`get_action_list`](#unitree-sdk2-cpp-robot-g1-g1armactionclient-get-action-list-1) | `def get_action_list(self) -> tuple[int, str]` | `AVAILABLE` | `READ_ONLY` |

<a id="unitree-sdk2-cpp-robot-g1-g1armactionclient-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.g1.G1ArmActionClient.__init__`

初始化 `G1ArmActionClient` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::g1::G1ArmActionClient`
- 签名：`G1ArmActionClient()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/g1/arm/g1_arm_action_client.hpp:26`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = G1ArmActionClient()
```

<a id="unitree-sdk2-cpp-robot-g1-g1armactionclient-init-1"></a>
#### `unitree_sdk2_cpp.robot.g1.G1ArmActionClient.init`

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

- 类：`unitree::robot::g1::G1ArmActionClient`
- 签名：`Init()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/arm/g1_arm_action_client.hpp:30`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.init()
```

<a id="unitree-sdk2-cpp-robot-g1-g1armactionclient-execute-action-1"></a>
#### `unitree_sdk2_cpp.robot.g1.G1ArmActionClient.execute_action`（重载 1/2）

对应 C++ SDK 操作 `ExecuteAction(int32_t)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
@overload
def execute_action(self, action_id: int) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `action_id` | `int` | 必填 | 传给该接口的 `action` ID 参数，Python 类型为 `int`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `action_id: int32_t`。 取值范围为 -2147483648 到 2147483647。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::g1::G1ArmActionClient`
- 签名：`ExecuteAction(int32_t)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/arm/g1_arm_action_client.hpp:51`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.execute_action(action_id=action_id)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-g1armactionclient-execute-action-2"></a>
#### `unitree_sdk2_cpp.robot.g1.G1ArmActionClient.execute_action`（重载 2/2）

对应 C++ SDK 操作 `ExecuteAction(const std::string &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
@overload
def execute_action(self, action_name: str) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `action_name` | `str` | 必填 | 传给该接口的 `action` 名称 参数，Python 类型为 `str`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `action_name: const std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::g1::G1ArmActionClient`
- 签名：`ExecuteAction(const std::string &)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/arm/g1_arm_action_client.hpp:67`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.execute_action(action_name=action_name)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-g1armactionclient-stop-custom-action-1"></a>
#### `unitree_sdk2_cpp.robot.g1.G1ArmActionClient.stop_custom_action`

请求停止对应 SDK 操作。该名称不等同于经过验证的物理急停。

**签名**

```python
def stop_custom_action(self) -> int
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

- 类：`unitree::robot::g1::G1ArmActionClient`
- 签名：`StopCustomAction()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/arm/g1_arm_action_client.hpp:74`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.stop_custom_action()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-g1armactionclient-get-action-list-1"></a>
#### `unitree_sdk2_cpp.robot.g1.G1ArmActionClient.get_action_list`

查询或检查 `action` `list`。

**签名**

```python
def get_action_list(self) -> tuple[int, str]
```

**可用性与安全性**

**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现只读查询。Robot Client 的服务端查询通常仍需匹配的 Linux 扩展、DDS、网络、机器人和服务；纯本地 getter 则不一定需要全部条件。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| [0] `status` | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。 |
| [1] `data` | `str` | 传给该接口的 数据 参数，Python 类型为 `str`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `data: std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。 |

**对应 C++**

- 类：`unitree::robot::g1::G1ArmActionClient`
- 签名：`GetActionList(std::string &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/g1/arm/g1_arm_action_client.hpp:79`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, data = obj.get_action_list()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-g1-jsonizedatavecfloat"></a>
### `unitree_sdk2_cpp.robot.g1.JsonizeDataVecFloat`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot.g1 import JsonizeDataVecFloat
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `data` | `list[float]` | 传给该接口的 数据 参数，Python 类型为 `list[float]`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 | `value = obj.data` / `obj.data = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-g1-jsonizedatavecfloat-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-g1-jsonizedatavecfloat-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-g1-jsonizedatavecfloat-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-g1-jsonizedatavecfloat-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.g1.JsonizeDataVecFloat.__init__`

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

- 类：`unitree::robot::g1::JsonizeDataVecFloat`
- 签名：`JsonizeDataVecFloat()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_api.hpp:45`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = JsonizeDataVecFloat()
```

<a id="unitree-sdk2-cpp-robot-g1-jsonizedatavecfloat-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.g1.JsonizeDataVecFloat.from_json`

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

- 类：`unitree::robot::g1::JsonizeDataVecFloat`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_api.hpp:48`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-g1-jsonizedatavecfloat-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.g1.JsonizeDataVecFloat.to_json`

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

- 类：`unitree::robot::g1::JsonizeDataVecFloat`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_api.hpp:50`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-g1-jsonizevelocitycommand"></a>
### `unitree_sdk2_cpp.robot.g1.JsonizeVelocityCommand`

SDK 类型签名预览。请逐项查看构造函数和方法的可用性。

**导入**

```python
from unitree_sdk2_cpp.robot.g1 import JsonizeVelocityCommand
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
| [`__init__`](#unitree-sdk2-cpp-robot-g1-jsonizevelocitycommand-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-g1-jsonizevelocitycommand-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-g1-jsonizevelocitycommand-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-g1-jsonizevelocitycommand-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.g1.JsonizeVelocityCommand.__init__`

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

- 类：`unitree::robot::g1::JsonizeVelocityCommand`
- 签名：`JsonizeVelocityCommand()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_api.hpp:59`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = JsonizeVelocityCommand()
```

<a id="unitree-sdk2-cpp-robot-g1-jsonizevelocitycommand-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.g1.JsonizeVelocityCommand.from_json`

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

- 类：`unitree::robot::g1::JsonizeVelocityCommand`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_api.hpp:62`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-g1-jsonizevelocitycommand-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.g1.JsonizeVelocityCommand.to_json`

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

- 类：`unitree::robot::g1::JsonizeVelocityCommand`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_api.hpp:67`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-g1-ledcontrolparameter"></a>
### `unitree_sdk2_cpp.robot.g1.LedControlParameter`

SDK 请求参数值类型；当前可能仅提供设计期签名。

**导入**

```python
from unitree_sdk2_cpp.robot.g1 import LedControlParameter
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
| [`__init__`](#unitree-sdk2-cpp-robot-g1-ledcontrolparameter-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-g1-ledcontrolparameter-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-g1-ledcontrolparameter-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-g1-ledcontrolparameter-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LedControlParameter.__init__`

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

- 类：`unitree::robot::g1::LedControlParameter`
- 签名：`LedControlParameter()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/g1/audio/g1_audio_api.hpp:75`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = LedControlParameter()
```

<a id="unitree-sdk2-cpp-robot-g1-ledcontrolparameter-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LedControlParameter.from_json`

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

- 类：`unitree::robot::g1::LedControlParameter`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/g1/audio/g1_audio_api.hpp:78`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-g1-ledcontrolparameter-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LedControlParameter.to_json`

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

- 类：`unitree::robot::g1::LedControlParameter`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/g1/audio/g1_audio_api.hpp:80`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-g1-lococlient"></a>
### `unitree_sdk2_cpp.robot.g1.LocoClient`

Robot 服务客户端。构造、初始化和具体方法的可用性必须分别检查。

**导入**

```python
from unitree_sdk2_cpp.robot.g1 import LocoClient
```

**基类**：`Client`

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-g1-lococlient-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`init`](#unitree-sdk2-cpp-robot-g1-lococlient-init-1) | `def init(self) -> None` | `AVAILABLE` | `INITIALIZATION` |
| [`get_fsm_id`](#unitree-sdk2-cpp-robot-g1-lococlient-get-fsm-id-1) | `def get_fsm_id(self) -> tuple[int, int]` | `AVAILABLE` | `READ_ONLY` |
| [`get_fsm_mode`](#unitree-sdk2-cpp-robot-g1-lococlient-get-fsm-mode-1) | `def get_fsm_mode(self) -> tuple[int, int]` | `AVAILABLE` | `READ_ONLY` |
| [`get_balance_mode`](#unitree-sdk2-cpp-robot-g1-lococlient-get-balance-mode-1) | `def get_balance_mode(self) -> tuple[int, int]` | `AVAILABLE` | `READ_ONLY` |
| [`get_swing_height`](#unitree-sdk2-cpp-robot-g1-lococlient-get-swing-height-1) | `def get_swing_height(self) -> tuple[int, float]` | `AVAILABLE` | `READ_ONLY` |
| [`get_stand_height`](#unitree-sdk2-cpp-robot-g1-lococlient-get-stand-height-1) | `def get_stand_height(self) -> tuple[int, float]` | `AVAILABLE` | `READ_ONLY` |
| [`get_phase`](#unitree-sdk2-cpp-robot-g1-lococlient-get-phase-1) | `def get_phase(self) -> tuple[int, list[float]]` | `AVAILABLE` | `READ_ONLY` |
| [`set_fsm_id`](#unitree-sdk2-cpp-robot-g1-lococlient-set-fsm-id-1) | `def set_fsm_id(self, fsm_id: int) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`set_balance_mode`](#unitree-sdk2-cpp-robot-g1-lococlient-set-balance-mode-1) | `def set_balance_mode(self, balance_mode: int) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`set_swing_height`](#unitree-sdk2-cpp-robot-g1-lococlient-set-swing-height-1) | `def set_swing_height(self, swing_height: float) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`set_stand_height`](#unitree-sdk2-cpp-robot-g1-lococlient-set-stand-height-1) | `def set_stand_height(self, stand_height: float) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`set_velocity`](#unitree-sdk2-cpp-robot-g1-lococlient-set-velocity-1) | `def set_velocity(self, vx: float, vy: float, omega: float, duration: float = 1.0) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`set_task_id`](#unitree-sdk2-cpp-robot-g1-lococlient-set-task-id-1) | `def set_task_id(self, task_id: int) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`switch_to_user_ctrl`](#unitree-sdk2-cpp-robot-g1-lococlient-switch-to-user-ctrl-1) | `def switch_to_user_ctrl(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`switch_to_internal_ctrl`](#unitree-sdk2-cpp-robot-g1-lococlient-switch-to-internal-ctrl-1) | `def switch_to_internal_ctrl(self, mode: InternalFsmMode) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`damp`](#unitree-sdk2-cpp-robot-g1-lococlient-damp-1) | `def damp(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`start`](#unitree-sdk2-cpp-robot-g1-lococlient-start-1) | `def start(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`squat`](#unitree-sdk2-cpp-robot-g1-lococlient-squat-1) | `def squat(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`sit`](#unitree-sdk2-cpp-robot-g1-lococlient-sit-1) | `def sit(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`stand_up`](#unitree-sdk2-cpp-robot-g1-lococlient-stand-up-1) | `def stand_up(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`zero_torque`](#unitree-sdk2-cpp-robot-g1-lococlient-zero-torque-1) | `def zero_torque(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`stop_move`](#unitree-sdk2-cpp-robot-g1-lococlient-stop-move-1) | `def stop_move(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`high_stand`](#unitree-sdk2-cpp-robot-g1-lococlient-high-stand-1) | `def high_stand(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`low_stand`](#unitree-sdk2-cpp-robot-g1-lococlient-low-stand-1) | `def low_stand(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`move（重载 1/2）`](#unitree-sdk2-cpp-robot-g1-lococlient-move-1) | `def move(self, vx: float, vy: float, vyaw: float, continous_move: bool) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`move（重载 2/2）`](#unitree-sdk2-cpp-robot-g1-lococlient-move-2) | `def move(self, vx: float, vy: float, vyaw: float) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`balance_stand`](#unitree-sdk2-cpp-robot-g1-lococlient-balance-stand-1) | `def balance_stand(self) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`continuous_gait`](#unitree-sdk2-cpp-robot-g1-lococlient-continuous-gait-1) | `def continuous_gait(self, flag: bool) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`switch_move_mode`](#unitree-sdk2-cpp-robot-g1-lococlient-switch-move-mode-1) | `def switch_move_mode(self, flag: bool) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`wave_hand`](#unitree-sdk2-cpp-robot-g1-lococlient-wave-hand-1) | `def wave_hand(self, turn_flag: bool = False) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`shake_hand`](#unitree-sdk2-cpp-robot-g1-lococlient-shake-hand-1) | `def shake_hand(self, stage: int = -1) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`set_speed_mode`](#unitree-sdk2-cpp-robot-g1-lococlient-set-speed-mode-1) | `def set_speed_mode(self, speed_mode: int) -> int` | `AVAILABLE` | `MOTION_COMMAND` |
| [`get_mimic_motion`](#unitree-sdk2-cpp-robot-g1-lococlient-get-mimic-motion-1) | `def get_mimic_motion(self) -> tuple[int, str]` | `AVAILABLE` | `READ_ONLY` |
| [`_fsm_api`](#unitree-sdk2-cpp-robot-g1-lococlient-fsm-api-1) | `def _fsm_api(self, parameter: str) -> tuple[int, str]` | `AVAILABLE` | `MOTION_COMMAND` |

<a id="unitree-sdk2-cpp-robot-g1-lococlient-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.__init__`

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

- 类：`unitree::robot::g1::LocoClient`
- 签名：`LocoClient()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:14`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = LocoClient()
```

<a id="unitree-sdk2-cpp-robot-g1-lococlient-init-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.init`

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

- 类：`unitree::robot::g1::LocoClient`
- 签名：`Init()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:18`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.init()
```

<a id="unitree-sdk2-cpp-robot-g1-lococlient-get-fsm-id-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.get_fsm_id`

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

- 类：`unitree::robot::g1::LocoClient`
- 签名：`GetFsmId(int &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:40`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, fsm_id = obj.get_fsm_id()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-g1-lococlient-get-fsm-mode-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.get_fsm_mode`

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

- 类：`unitree::robot::g1::LocoClient`
- 签名：`GetFsmMode(int &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:54`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, fsm_mode = obj.get_fsm_mode()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-g1-lococlient-get-balance-mode-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.get_balance_mode`

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

- 类：`unitree::robot::g1::LocoClient`
- 签名：`GetBalanceMode(int &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:68`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, balance_mode = obj.get_balance_mode()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-g1-lococlient-get-swing-height-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.get_swing_height`

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

- 类：`unitree::robot::g1::LocoClient`
- 签名：`GetSwingHeight(float &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:82`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, swing_height = obj.get_swing_height()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-g1-lococlient-get-stand-height-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.get_stand_height`

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

- 类：`unitree::robot::g1::LocoClient`
- 签名：`GetStandHeight(float &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:96`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, stand_height = obj.get_stand_height()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-g1-lococlient-get-phase-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.get_phase`

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

- 类：`unitree::robot::g1::LocoClient`
- 签名：`GetPhase(std::vector<float> &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:110`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, phase = obj.get_phase()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-g1-lococlient-set-fsm-id-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.set_fsm_id`

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

- 类：`unitree::robot::g1::LocoClient`
- 签名：`SetFsmId(int)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:124`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.set_fsm_id(fsm_id=fsm_id)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-lococlient-set-balance-mode-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.set_balance_mode`

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

- 类：`unitree::robot::g1::LocoClient`
- 签名：`SetBalanceMode(int)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:134`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.set_balance_mode(balance_mode=balance_mode)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-lococlient-set-swing-height-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.set_swing_height`

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

- 类：`unitree::robot::g1::LocoClient`
- 签名：`SetSwingHeight(float)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:144`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.set_swing_height(swing_height=swing_height)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-lococlient-set-stand-height-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.set_stand_height`

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

- 类：`unitree::robot::g1::LocoClient`
- 签名：`SetStandHeight(float)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:154`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.set_stand_height(stand_height=stand_height)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-lococlient-set-velocity-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.set_velocity`

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

- 类：`unitree::robot::g1::LocoClient`
- 签名：`SetVelocity(float, float, float, float)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:164`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.set_velocity(vx=vx, vy=vy, omega=omega, duration=duration)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-lococlient-set-task-id-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.set_task_id`

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

- 类：`unitree::robot::g1::LocoClient`
- 签名：`SetTaskId(int)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:176`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.set_task_id(task_id=task_id)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-lococlient-switch-to-user-ctrl-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.switch_to_user_ctrl`

对应 C++ SDK 操作 `SwitchToUserCtrl()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def switch_to_user_ctrl(self) -> int
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

- 类：`unitree::robot::g1::LocoClient`
- 签名：`SwitchToUserCtrl()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:186`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.switch_to_user_ctrl()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-lococlient-switch-to-internal-ctrl-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.switch_to_internal_ctrl`

对应 C++ SDK 操作 `SwitchToInternalCtrl(unitree::robot::g1::InternalFsmMode)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def switch_to_internal_ctrl(self, mode: InternalFsmMode) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `mode` | `InternalFsmMode` | 必填 | 传给该接口的 模式 参数，Python 类型为 `InternalFsmMode`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `mode: unitree::robot::g1::InternalFsmMode`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::g1::LocoClient`
- 签名：`SwitchToInternalCtrl(unitree::robot::g1::InternalFsmMode)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:194`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.switch_to_internal_ctrl(mode=mode)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-lococlient-damp-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.damp`

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

- 类：`unitree::robot::g1::LocoClient`
- 签名：`Damp()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:214`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.damp()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-lococlient-start-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.start`

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

- 类：`unitree::robot::g1::LocoClient`
- 签名：`Start()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:216`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.start()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-lococlient-squat-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.squat`

对应 C++ SDK 操作 `Squat()`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def squat(self) -> int
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

- 类：`unitree::robot::g1::LocoClient`
- 签名：`Squat()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:218`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.squat()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-lococlient-sit-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.sit`

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

- 类：`unitree::robot::g1::LocoClient`
- 签名：`Sit()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:220`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.sit()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-lococlient-stand-up-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.stand_up`

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

- 类：`unitree::robot::g1::LocoClient`
- 签名：`StandUp()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:222`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.stand_up()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-lococlient-zero-torque-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.zero_torque`

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

- 类：`unitree::robot::g1::LocoClient`
- 签名：`ZeroTorque()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:224`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.zero_torque()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-lococlient-stop-move-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.stop_move`

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

- 类：`unitree::robot::g1::LocoClient`
- 签名：`StopMove()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:226`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.stop_move()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-lococlient-high-stand-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.high_stand`

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

- 类：`unitree::robot::g1::LocoClient`
- 签名：`HighStand()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:228`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.high_stand()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-lococlient-low-stand-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.low_stand`

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

- 类：`unitree::robot::g1::LocoClient`
- 签名：`LowStand()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:230`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.low_stand()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-lococlient-move-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.move`（重载 1/2）

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

- 类：`unitree::robot::g1::LocoClient`
- 签名：`Move(float, float, float, bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:232`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.move(vx=vx, vy=vy, vyaw=vyaw, continous_move=continous_move)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-lococlient-move-2"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.move`（重载 2/2）

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

- 类：`unitree::robot::g1::LocoClient`
- 签名：`Move(float, float, float)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:236`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.move(vx=vx, vy=vy, vyaw=vyaw)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-lococlient-balance-stand-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.balance_stand`

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

- 类：`unitree::robot::g1::LocoClient`
- 签名：`BalanceStand()`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:238`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.balance_stand()
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-lococlient-continuous-gait-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.continuous_gait`

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

- 类：`unitree::robot::g1::LocoClient`
- 签名：`ContinuousGait(bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:240`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.continuous_gait(flag=flag)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-lococlient-switch-move-mode-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.switch_move_mode`

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

- 类：`unitree::robot::g1::LocoClient`
- 签名：`SwitchMoveMode(bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:242`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.switch_move_mode(flag=flag)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-lococlient-wave-hand-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.wave_hand`

对应 C++ SDK 操作 `WaveHand(bool)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def wave_hand(self, turn_flag: bool = False) -> int
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `turn_flag` | `bool` | `False` | 传给该接口的 `turn` `flag` 参数，Python 类型为 `bool`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `turn_flag: bool`。 只接受布尔语义。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务定义解释。 |

**对应 C++**

- 类：`unitree::robot::g1::LocoClient`
- 签名：`WaveHand(bool)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:247`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.wave_hand(turn_flag=turn_flag)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-lococlient-shake-hand-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.shake_hand`

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

- 类：`unitree::robot::g1::LocoClient`
- 签名：`ShakeHand(int)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:249`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.shake_hand(stage=stage)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-lococlient-set-speed-mode-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.set_speed_mode`

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

- 类：`unitree::robot::g1::LocoClient`
- 签名：`SetSpeedMode(int)`
- 绑定策略：`DIRECT`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:265`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
result = obj.set_speed_mode(speed_mode=speed_mode)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-lococlient-get-mimic-motion-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient.get_mimic_motion`

查询或检查 `mimic` `motion`。

**签名**

```python
def get_mimic_motion(self) -> tuple[int, str]
```

**可用性与安全性**

**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现只读查询。Robot Client 的服务端查询通常仍需匹配的 Linux 扩展、DDS、网络、机器人和服务；纯本地 getter 则不一定需要全部条件。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| [0] `status` | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。 |
| [1] `data` | `str` | 传给该接口的 数据 参数，Python 类型为 `str`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `data: std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。 |

**对应 C++**

- 类：`unitree::robot::g1::LocoClient`
- 签名：`GetMimicMotion(std::string &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:298`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。

**用法**

```python
status, data = obj.get_mimic_motion()
```

> [!NOTE]
> 只读查询仍会访问 DDS/机器人服务。必须检查返回状态码，并处理超时和网络中断。

<a id="unitree-sdk2-cpp-robot-g1-lococlient-fsm-api-1"></a>
#### `unitree_sdk2_cpp.robot.g1.LocoClient._fsm_api`

对应 C++ SDK 操作 `_fsm_api(std::string, std::string &)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def _fsm_api(self, parameter: str) -> tuple[int, str]
```

**可用性与安全性**

**`AVAILABLE` / `MOTION_COMMAND`**：当前绑定源码已实现，调用会向实体机器人发送运动相关请求。只能在隔离场地、完成目标型号安全检查并准备物理急停后使用；不得从默认测试或未经确认的 Agent 流程调用。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `parameter` | `str` | 必填 | 传给该接口的 `parameter` 参数，Python 类型为 `str`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `parameter: std::string`。 底层为字符串；长度、编码和允许值由具体协议决定。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| [0] `status` | `int` | SDK 状态码；Unitree 示例通常以 `0` 表示成功，非零值需按具体服务错误码解释。 |
| [1] `data` | `str` | 传给该接口的 数据 参数，Python 类型为 `str`。精确含义、单位、范围和枚举值需查目标型号对应头文件与协议。 对应 C++ 参数 `data: std::string &`。 底层为字符串；长度、编码和允许值由具体协议决定。 |

**对应 C++**

- 类：`unitree::robot::g1::LocoClient`
- 签名：`_fsm_api(std::string, std::string &)`
- 绑定策略：`OUTPUT_WRAPPER`
- 声明位置：`include/unitree/robot/g1/loco/g1_loco_client.hpp:303`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。
- C++ 的可修改输出引用不会作为 Python 入参出现，而是按 C++ 参数顺序追加到返回元组中。
- 该方法属于运动命令。方法名包含 `stop`、`damp` 或 `zero` 也不代表它是独立物理急停。

**用法**

```python
status, data = obj._fsm_api(parameter=parameter)
```

> [!CAUTION]
> 此示例展示签名，不是可直接执行的安全脚本。调用前必须完成硬件隔离、目标机器人确认和对应型号的安全检查；运动接口还必须准备物理急停。

<a id="unitree-sdk2-cpp-robot-g1-moveparameter"></a>
### `unitree_sdk2_cpp.robot.g1.MoveParameter`

SDK 请求参数值类型；当前可能仅提供设计期签名。

**导入**

```python
from unitree_sdk2_cpp.robot.g1 import MoveParameter
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `vx` | `float` | X 方向速度参数。坐标系、单位、符号和安全范围必须查目标型号运动协议。 | `value = obj.vx` / `obj.vx = value` |
| `vy` | `float` | Y 方向速度参数。坐标系、单位、符号和安全范围必须查目标型号运动协议。 | `value = obj.vy` / `obj.vy = value` |
| `vyaw` | `float` | 偏航角速度参数。单位、符号和安全范围必须查目标型号运动协议。 | `value = obj.vyaw` / `obj.vyaw = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-g1-moveparameter-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-g1-moveparameter-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-g1-moveparameter-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-g1-moveparameter-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.g1.MoveParameter.__init__`

初始化 `MoveParameter` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree::robot::g1::MoveParameter`
- 签名：`MoveParameter()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/g1/agv/g1_agv_api.hpp:28`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = MoveParameter()
```

<a id="unitree-sdk2-cpp-robot-g1-moveparameter-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.g1.MoveParameter.from_json`

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
| `value` | `Mapping[str, Any]` | 必填 | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 对应 C++ 参数 `json: unitree::common::JsonMap &`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | 该方法不返回 Python 值；失败可能表现为异常或底层状态变化。 |

**对应 C++**

- 类：`unitree::robot::g1::MoveParameter`
- 签名：`fromJson(unitree::common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/g1/agv/g1_agv_api.hpp:36`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-g1-moveparameter-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.g1.MoveParameter.to_json`

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

- 类：`unitree::robot::g1::MoveParameter`
- 签名：`toJson(unitree::common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/g1/agv/g1_agv_api.hpp:43`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-g1-playstopparameter"></a>
### `unitree_sdk2_cpp.robot.g1.PlayStopParameter`

SDK 请求参数值类型；当前可能仅提供设计期签名。

**导入**

```python
from unitree_sdk2_cpp.robot.g1 import PlayStopParameter
```

**基类**：`object`

**公开属性**

| 名称 | Python 类型 | 含义 | 用法 |
| --- | --- | --- | --- |
| `app_name` | `str` | 应用名称，用于标识音频流或播放会话。允许值和命名规则以目标服务协议为准。 | `value = obj.app_name` / `obj.app_name = value` |

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-robot-g1-playstopparameter-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-g1-playstopparameter-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-g1-playstopparameter-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-g1-playstopparameter-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.g1.PlayStopParameter.__init__`

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

- 类：`unitree::robot::g1::PlayStopParameter`
- 签名：`PlayStopParameter()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/g1/audio/g1_audio_api.hpp:61`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = PlayStopParameter()
```

<a id="unitree-sdk2-cpp-robot-g1-playstopparameter-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.g1.PlayStopParameter.from_json`

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

- 类：`unitree::robot::g1::PlayStopParameter`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/g1/audio/g1_audio_api.hpp:64`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-g1-playstopparameter-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.g1.PlayStopParameter.to_json`

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

- 类：`unitree::robot::g1::PlayStopParameter`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/g1/audio/g1_audio_api.hpp:66`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-g1-playstreamparameter"></a>
### `unitree_sdk2_cpp.robot.g1.PlayStreamParameter`

SDK 请求参数值类型；当前可能仅提供设计期签名。

**导入**

```python
from unitree_sdk2_cpp.robot.g1 import PlayStreamParameter
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
| [`__init__`](#unitree-sdk2-cpp-robot-g1-playstreamparameter-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-g1-playstreamparameter-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-g1-playstreamparameter-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-g1-playstreamparameter-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.g1.PlayStreamParameter.__init__`

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

- 类：`unitree::robot::g1::PlayStreamParameter`
- 签名：`PlayStreamParameter()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/g1/audio/g1_audio_api.hpp:45`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = PlayStreamParameter()
```

<a id="unitree-sdk2-cpp-robot-g1-playstreamparameter-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.g1.PlayStreamParameter.from_json`

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

- 类：`unitree::robot::g1::PlayStreamParameter`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/g1/audio/g1_audio_api.hpp:48`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-g1-playstreamparameter-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.g1.PlayStreamParameter.to_json`

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

- 类：`unitree::robot::g1::PlayStreamParameter`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/g1/audio/g1_audio_api.hpp:50`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

<a id="unitree-sdk2-cpp-robot-g1-ttsmakerparameter"></a>
### `unitree_sdk2_cpp.robot.g1.TtsMakerParameter`

SDK 请求参数值类型；当前可能仅提供设计期签名。

**导入**

```python
from unitree_sdk2_cpp.robot.g1 import TtsMakerParameter
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
| [`__init__`](#unitree-sdk2-cpp-robot-g1-ttsmakerparameter-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `CONSTRUCTION` |
| [`from_json`](#unitree-sdk2-cpp-robot-g1-ttsmakerparameter-from-json-1) | `def from_json(self, value: Mapping[str, Any]) -> None` | `AVAILABLE` | `UNCLASSIFIED` |
| [`to_json`](#unitree-sdk2-cpp-robot-g1-ttsmakerparameter-to-json-1) | `def to_json(self) -> dict[str, Any]` | `AVAILABLE` | `UNCLASSIFIED` |

<a id="unitree-sdk2-cpp-robot-g1-ttsmakerparameter-dunder-init-1"></a>
#### `unitree_sdk2_cpp.robot.g1.TtsMakerParameter.__init__`

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

- 类：`unitree::robot::g1::TtsMakerParameter`
- 签名：`TtsMakerParameter()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/robot/g1/audio/g1_audio_api.hpp:27`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = TtsMakerParameter()
```

<a id="unitree-sdk2-cpp-robot-g1-ttsmakerparameter-from-json-1"></a>
#### `unitree_sdk2_cpp.robot.g1.TtsMakerParameter.from_json`

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

- 类：`unitree::robot::g1::TtsMakerParameter`
- 签名：`fromJson(common::JsonMap &)`
- 绑定策略：`JSON_DICT_INPUT`
- 声明位置：`include/unitree/robot/g1/audio/g1_audio_api.hpp:30`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
obj.from_json(value=value)
```

<a id="unitree-sdk2-cpp-robot-g1-ttsmakerparameter-to-json-1"></a>
#### `unitree_sdk2_cpp.robot.g1.TtsMakerParameter.to_json`

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

- 类：`unitree::robot::g1::TtsMakerParameter`
- 签名：`toJson(common::JsonMap &) const`
- 绑定策略：`JSON_DICT_OUTPUT`
- 声明位置：`include/unitree/robot/g1/audio/g1_audio_api.hpp:32`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = obj.to_json()
```

---

[返回 API 总索引](../API_REFERENCE_ZH.md)
