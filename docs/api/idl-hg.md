# Unitree SDK2 Python API 参考分卷

[返回 API 总索引](../API_REFERENCE_ZH.md) · [阅读从零开始指南](../BEGINNER_GUIDE_ZH.md)

> [!WARNING]
> 本分卷同时包含 `AVAILABLE` 和 `SIGNATURE_ONLY`。后者只是设计期类型签名。运动及硬件副作用方法即使标记为 `AVAILABLE`，也不表示当前环境可安全执行。

> [!NOTE]
> 本文件由 `generator/generate_api_docs.py` 自动生成，请勿手工维护 API 条目。

---

<a id="unitree-sdk2-cpp-idl-hg"></a>
## HG IDL 消息

模块：`unitree_sdk2_cpp.idl.hg`

### 类索引

| 类 | 公开函数签名 | 属性 |
| --- | ---: | ---: |
| [`AgvBmsState`](#unitree-sdk2-cpp-idl-hg-agvbmsstate) | 3 | 7 |
| [`BmsCmd`](#unitree-sdk2-cpp-idl-hg-bmscmd) | 3 | 2 |
| [`BmsState`](#unitree-sdk2-cpp-idl-hg-bmsstate) | 3 | 13 |
| [`MotorCmd`](#unitree-sdk2-cpp-idl-hg-motorcmd) | 3 | 7 |
| [`HandCmd`](#unitree-sdk2-cpp-idl-hg-handcmd) | 3 | 2 |
| [`IMUState`](#unitree-sdk2-cpp-idl-hg-imustate) | 3 | 5 |
| [`MotorState`](#unitree-sdk2-cpp-idl-hg-motorstate) | 3 | 10 |
| [`PressSensorState`](#unitree-sdk2-cpp-idl-hg-presssensorstate) | 3 | 4 |
| [`HandState`](#unitree-sdk2-cpp-idl-hg-handstate) | 3 | 9 |
| [`LowCmd`](#unitree-sdk2-cpp-idl-hg-lowcmd) | 3 | 5 |
| [`LowState`](#unitree-sdk2-cpp-idl-hg-lowstate) | 3 | 9 |
| [`MainBoardState`](#unitree-sdk2-cpp-idl-hg-mainboardstate) | 3 | 4 |
| [`SportModeState`](#unitree-sdk2-cpp-idl-hg-sportmodestate) | 3 | 4 |

<a id="unitree-sdk2-cpp-idl-hg-agvbmsstate"></a>
### `unitree_sdk2_cpp.idl.hg.AgvBmsState`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.hg import AgvBmsState
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-hg-agvbmsstate-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-hg-agvbmsstate-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-hg-agvbmsstate-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`software_version`](#unitree-sdk2-cpp-idl-hg-agvbmsstate-software-version) | `str` | `str` | `AVAILABLE` |
| [`battery_percentage`](#unitree-sdk2-cpp-idl-hg-agvbmsstate-battery-percentage) | `int` | `int` | `AVAILABLE` |
| [`current`](#unitree-sdk2-cpp-idl-hg-agvbmsstate-current) | `int` | `int` | `AVAILABLE` |
| [`temperature`](#unitree-sdk2-cpp-idl-hg-agvbmsstate-temperature) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`docking_status`](#unitree-sdk2-cpp-idl-hg-agvbmsstate-docking-status) | `str` | `str` | `AVAILABLE` |
| [`is_charging`](#unitree-sdk2-cpp-idl-hg-agvbmsstate-is-charging) | `bool` | `bool` | `AVAILABLE` |
| [`is_dc_connected`](#unitree-sdk2-cpp-idl-hg-agvbmsstate-is-dc-connected) | `bool` | `bool` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-hg-agvbmsstate-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.hg.AgvBmsState.__init__`

初始化 `AgvBmsState` 实例。是否能实际构造取决于下方可用性状态。

**签名**

```python
def __init__(self) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::AgvBmsState_`
- 签名：`AgvBmsState_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/hg/AgvBmsState_.hpp:34`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = AgvBmsState()
```

<a id="unitree-sdk2-cpp-idl-hg-agvbmsstate-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.hg.AgvBmsState.__eq__`

按底层 IDL 消息内容比较两个对象是否相等。

**签名**

```python
def __eq__(self, other: object) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `other` | `object` | 必填 | 用于比较的另一个 Python 对象。类型不兼容时比较结果通常为 `False`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::AgvBmsState_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-hg-agvbmsstate-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.hg.AgvBmsState.__ne__`

按底层 IDL 消息内容比较两个对象是否不相等。

**签名**

```python
def __ne__(self, other: object) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `other` | `object` | 必填 | 用于比较的另一个 Python 对象。类型不兼容时比较结果通常为 `False`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::AgvBmsState_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-hg-agvbmsstate-software-version"></a>
#### `unitree_sdk2_cpp.idl.hg.AgvBmsState.software_version`

底层 `unitree_hg::msg::dds_::AgvBmsState_` 的 `software_version` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

**签名**

```python
@property
def software_version(self) -> str

@software_version.setter
def software_version(self, value: str) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `str` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `str` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::AgvBmsState_`
- 字段类型：`std::string`
- 声明位置：`include/unitree/idl/hg/AgvBmsState_.hpp:25`

**用法**

```python
current_value = obj.software_version
obj.software_version = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-agvbmsstate-battery-percentage"></a>
#### `unitree_sdk2_cpp.idl.hg.AgvBmsState.battery_percentage`

底层 `unitree_hg::msg::dds_::AgvBmsState_` 的 `battery_percentage` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def battery_percentage(self) -> int

@battery_percentage.setter
def battery_percentage(self, value: int) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `int` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `int` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::AgvBmsState_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/hg/AgvBmsState_.hpp:26`

**用法**

```python
current_value = obj.battery_percentage
obj.battery_percentage = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-agvbmsstate-current"></a>
#### `unitree_sdk2_cpp.idl.hg.AgvBmsState.current`

底层 `unitree_hg::msg::dds_::AgvBmsState_` 的 `current` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 -2147483648 到 2147483647。

**签名**

```python
@property
def current(self) -> int

@current.setter
def current(self, value: int) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `int` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `int` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::AgvBmsState_`
- 字段类型：`int32_t`
- 声明位置：`include/unitree/idl/hg/AgvBmsState_.hpp:27`

**用法**

```python
current_value = obj.current
obj.current = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-agvbmsstate-temperature"></a>
#### `unitree_sdk2_cpp.idl.hg.AgvBmsState.temperature`

底层 `unitree_hg::msg::dds_::AgvBmsState_` 的 `temperature` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：取值范围为 -32768 到 32767。

**签名**

```python
@property
def temperature(self) -> list[int]

@temperature.setter
def temperature(self, value: Sequence[int]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[int]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[int]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::AgvBmsState_`
- 字段类型：`std::array<int16_t, 3>`
- 声明位置：`include/unitree/idl/hg/AgvBmsState_.hpp:28`

**用法**

```python
current_value = obj.temperature
obj.temperature = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-agvbmsstate-docking-status"></a>
#### `unitree_sdk2_cpp.idl.hg.AgvBmsState.docking_status`

底层 `unitree_hg::msg::dds_::AgvBmsState_` 的 `docking_status` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

**签名**

```python
@property
def docking_status(self) -> str

@docking_status.setter
def docking_status(self, value: str) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `str` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `str` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::AgvBmsState_`
- 字段类型：`std::string`
- 声明位置：`include/unitree/idl/hg/AgvBmsState_.hpp:29`

**用法**

```python
current_value = obj.docking_status
obj.docking_status = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-agvbmsstate-is-charging"></a>
#### `unitree_sdk2_cpp.idl.hg.AgvBmsState.is_charging`

底层 `unitree_hg::msg::dds_::AgvBmsState_` 的 `is_charging` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 只接受布尔语义。

**签名**

```python
@property
def is_charging(self) -> bool

@is_charging.setter
def is_charging(self, value: bool) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `bool` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `bool` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::AgvBmsState_`
- 字段类型：`bool`
- 声明位置：`include/unitree/idl/hg/AgvBmsState_.hpp:30`

**用法**

```python
current_value = obj.is_charging
obj.is_charging = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-agvbmsstate-is-dc-connected"></a>
#### `unitree_sdk2_cpp.idl.hg.AgvBmsState.is_dc_connected`

底层 `unitree_hg::msg::dds_::AgvBmsState_` 的 `is_dc_connected` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 只接受布尔语义。

**签名**

```python
@property
def is_dc_connected(self) -> bool

@is_dc_connected.setter
def is_dc_connected(self, value: bool) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `bool` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `bool` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::AgvBmsState_`
- 字段类型：`bool`
- 声明位置：`include/unitree/idl/hg/AgvBmsState_.hpp:31`

**用法**

```python
current_value = obj.is_dc_connected
obj.is_dc_connected = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-bmscmd"></a>
### `unitree_sdk2_cpp.idl.hg.BmsCmd`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.hg import BmsCmd
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-hg-bmscmd-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-hg-bmscmd-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-hg-bmscmd-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`cmd`](#unitree-sdk2-cpp-idl-hg-bmscmd-cmd) | `int` | `int` | `AVAILABLE` |
| [`reserve`](#unitree-sdk2-cpp-idl-hg-bmscmd-reserve) | `list[int]` | `Sequence[int]` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-hg-bmscmd-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.hg.BmsCmd.__init__`

初始化 `BmsCmd` 实例。是否能实际构造取决于下方可用性状态。

**签名**

```python
def __init__(self) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::BmsCmd_`
- 签名：`BmsCmd_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/hg/BmsCmd_.hpp:28`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = BmsCmd()
```

<a id="unitree-sdk2-cpp-idl-hg-bmscmd-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.hg.BmsCmd.__eq__`

按底层 IDL 消息内容比较两个对象是否相等。

**签名**

```python
def __eq__(self, other: object) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `other` | `object` | 必填 | 用于比较的另一个 Python 对象。类型不兼容时比较结果通常为 `False`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::BmsCmd_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-hg-bmscmd-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.hg.BmsCmd.__ne__`

按底层 IDL 消息内容比较两个对象是否不相等。

**签名**

```python
def __ne__(self, other: object) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `other` | `object` | 必填 | 用于比较的另一个 Python 对象。类型不兼容时比较结果通常为 `False`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::BmsCmd_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-hg-bmscmd-cmd"></a>
#### `unitree_sdk2_cpp.idl.hg.BmsCmd.cmd`

底层 `unitree_hg::msg::dds_::BmsCmd_` 的 `cmd` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def cmd(self) -> int

@cmd.setter
def cmd(self, value: int) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `int` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `int` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::BmsCmd_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/hg/BmsCmd_.hpp:24`

**用法**

```python
current_value = obj.cmd
obj.cmd = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-bmscmd-reserve"></a>
#### `unitree_sdk2_cpp.idl.hg.BmsCmd.reserve`

底层 `unitree_hg::msg::dds_::BmsCmd_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 40 个元素；元素约束：取值范围为 0 到 255。

**签名**

```python
@property
def reserve(self) -> list[int]

@reserve.setter
def reserve(self, value: Sequence[int]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[int]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[int]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::BmsCmd_`
- 字段类型：`std::array<uint8_t, 40>`
- 声明位置：`include/unitree/idl/hg/BmsCmd_.hpp:25`

**用法**

```python
current_value = obj.reserve
obj.reserve = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-bmsstate"></a>
### `unitree_sdk2_cpp.idl.hg.BmsState`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.hg import BmsState
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-hg-bmsstate-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-hg-bmsstate-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-hg-bmsstate-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`version_high`](#unitree-sdk2-cpp-idl-hg-bmsstate-version-high) | `int` | `int` | `AVAILABLE` |
| [`version_low`](#unitree-sdk2-cpp-idl-hg-bmsstate-version-low) | `int` | `int` | `AVAILABLE` |
| [`fn`](#unitree-sdk2-cpp-idl-hg-bmsstate-fn) | `int` | `int` | `AVAILABLE` |
| [`cell_vol`](#unitree-sdk2-cpp-idl-hg-bmsstate-cell-vol) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`bmsvoltage`](#unitree-sdk2-cpp-idl-hg-bmsstate-bmsvoltage) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`current`](#unitree-sdk2-cpp-idl-hg-bmsstate-current) | `int` | `int` | `AVAILABLE` |
| [`soc`](#unitree-sdk2-cpp-idl-hg-bmsstate-soc) | `int` | `int` | `AVAILABLE` |
| [`soh`](#unitree-sdk2-cpp-idl-hg-bmsstate-soh) | `int` | `int` | `AVAILABLE` |
| [`temperature`](#unitree-sdk2-cpp-idl-hg-bmsstate-temperature) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`cycle`](#unitree-sdk2-cpp-idl-hg-bmsstate-cycle) | `int` | `int` | `AVAILABLE` |
| [`manufacturer_date`](#unitree-sdk2-cpp-idl-hg-bmsstate-manufacturer-date) | `int` | `int` | `AVAILABLE` |
| [`bmsstate`](#unitree-sdk2-cpp-idl-hg-bmsstate-bmsstate) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`reserve`](#unitree-sdk2-cpp-idl-hg-bmsstate-reserve) | `list[int]` | `Sequence[int]` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-hg-bmsstate-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.hg.BmsState.__init__`

初始化 `BmsState` 实例。是否能实际构造取决于下方可用性状态。

**签名**

```python
def __init__(self) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::BmsState_`
- 签名：`BmsState_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/hg/BmsState_.hpp:39`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = BmsState()
```

<a id="unitree-sdk2-cpp-idl-hg-bmsstate-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.hg.BmsState.__eq__`

按底层 IDL 消息内容比较两个对象是否相等。

**签名**

```python
def __eq__(self, other: object) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `other` | `object` | 必填 | 用于比较的另一个 Python 对象。类型不兼容时比较结果通常为 `False`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::BmsState_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-hg-bmsstate-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.hg.BmsState.__ne__`

按底层 IDL 消息内容比较两个对象是否不相等。

**签名**

```python
def __ne__(self, other: object) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `other` | `object` | 必填 | 用于比较的另一个 Python 对象。类型不兼容时比较结果通常为 `False`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::BmsState_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-hg-bmsstate-version-high"></a>
#### `unitree_sdk2_cpp.idl.hg.BmsState.version_high`

底层 `unitree_hg::msg::dds_::BmsState_` 的 `version_high` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def version_high(self) -> int

@version_high.setter
def version_high(self, value: int) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `int` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `int` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::BmsState_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/hg/BmsState_.hpp:24`

**用法**

```python
current_value = obj.version_high
obj.version_high = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-bmsstate-version-low"></a>
#### `unitree_sdk2_cpp.idl.hg.BmsState.version_low`

底层 `unitree_hg::msg::dds_::BmsState_` 的 `version_low` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def version_low(self) -> int

@version_low.setter
def version_low(self, value: int) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `int` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `int` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::BmsState_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/hg/BmsState_.hpp:25`

**用法**

```python
current_value = obj.version_low
obj.version_low = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-bmsstate-fn"></a>
#### `unitree_sdk2_cpp.idl.hg.BmsState.fn`

底层 `unitree_hg::msg::dds_::BmsState_` 的 `fn` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def fn(self) -> int

@fn.setter
def fn(self, value: int) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `int` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `int` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::BmsState_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/hg/BmsState_.hpp:26`

**用法**

```python
current_value = obj.fn
obj.fn = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-bmsstate-cell-vol"></a>
#### `unitree_sdk2_cpp.idl.hg.BmsState.cell_vol`

底层 `unitree_hg::msg::dds_::BmsState_` 的 `cell_vol` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 40 个元素；元素约束：取值范围为 0 到 65535。

**签名**

```python
@property
def cell_vol(self) -> list[int]

@cell_vol.setter
def cell_vol(self, value: Sequence[int]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[int]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[int]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::BmsState_`
- 字段类型：`std::array<uint16_t, 40>`
- 声明位置：`include/unitree/idl/hg/BmsState_.hpp:27`

**用法**

```python
current_value = obj.cell_vol
obj.cell_vol = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-bmsstate-bmsvoltage"></a>
#### `unitree_sdk2_cpp.idl.hg.BmsState.bmsvoltage`

底层 `unitree_hg::msg::dds_::BmsState_` 的 `bmsvoltage` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：取值范围为 0 到 4294967295。

**签名**

```python
@property
def bmsvoltage(self) -> list[int]

@bmsvoltage.setter
def bmsvoltage(self, value: Sequence[int]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[int]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[int]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::BmsState_`
- 字段类型：`std::array<uint32_t, 3>`
- 声明位置：`include/unitree/idl/hg/BmsState_.hpp:28`

**用法**

```python
current_value = obj.bmsvoltage
obj.bmsvoltage = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-bmsstate-current"></a>
#### `unitree_sdk2_cpp.idl.hg.BmsState.current`

底层 `unitree_hg::msg::dds_::BmsState_` 的 `current` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 -2147483648 到 2147483647。

**签名**

```python
@property
def current(self) -> int

@current.setter
def current(self, value: int) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `int` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `int` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::BmsState_`
- 字段类型：`int32_t`
- 声明位置：`include/unitree/idl/hg/BmsState_.hpp:29`

**用法**

```python
current_value = obj.current
obj.current = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-bmsstate-soc"></a>
#### `unitree_sdk2_cpp.idl.hg.BmsState.soc`

底层 `unitree_hg::msg::dds_::BmsState_` 的 `soc` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def soc(self) -> int

@soc.setter
def soc(self, value: int) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `int` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `int` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::BmsState_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/hg/BmsState_.hpp:30`

**用法**

```python
current_value = obj.soc
obj.soc = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-bmsstate-soh"></a>
#### `unitree_sdk2_cpp.idl.hg.BmsState.soh`

底层 `unitree_hg::msg::dds_::BmsState_` 的 `soh` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def soh(self) -> int

@soh.setter
def soh(self, value: int) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `int` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `int` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::BmsState_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/hg/BmsState_.hpp:31`

**用法**

```python
current_value = obj.soh
obj.soh = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-bmsstate-temperature"></a>
#### `unitree_sdk2_cpp.idl.hg.BmsState.temperature`

底层 `unitree_hg::msg::dds_::BmsState_` 的 `temperature` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 12 个元素；元素约束：取值范围为 -32768 到 32767。

**签名**

```python
@property
def temperature(self) -> list[int]

@temperature.setter
def temperature(self, value: Sequence[int]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[int]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[int]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::BmsState_`
- 字段类型：`std::array<int16_t, 12>`
- 声明位置：`include/unitree/idl/hg/BmsState_.hpp:32`

**用法**

```python
current_value = obj.temperature
obj.temperature = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-bmsstate-cycle"></a>
#### `unitree_sdk2_cpp.idl.hg.BmsState.cycle`

底层 `unitree_hg::msg::dds_::BmsState_` 的 `cycle` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 65535。

**签名**

```python
@property
def cycle(self) -> int

@cycle.setter
def cycle(self, value: int) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `int` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `int` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::BmsState_`
- 字段类型：`uint16_t`
- 声明位置：`include/unitree/idl/hg/BmsState_.hpp:33`

**用法**

```python
current_value = obj.cycle
obj.cycle = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-bmsstate-manufacturer-date"></a>
#### `unitree_sdk2_cpp.idl.hg.BmsState.manufacturer_date`

底层 `unitree_hg::msg::dds_::BmsState_` 的 `manufacturer_date` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 65535。

**签名**

```python
@property
def manufacturer_date(self) -> int

@manufacturer_date.setter
def manufacturer_date(self, value: int) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `int` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `int` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::BmsState_`
- 字段类型：`uint16_t`
- 声明位置：`include/unitree/idl/hg/BmsState_.hpp:34`

**用法**

```python
current_value = obj.manufacturer_date
obj.manufacturer_date = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-bmsstate-bmsstate"></a>
#### `unitree_sdk2_cpp.idl.hg.BmsState.bmsstate`

底层 `unitree_hg::msg::dds_::BmsState_` 的 `bmsstate` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 5 个元素；元素约束：取值范围为 0 到 4294967295。

**签名**

```python
@property
def bmsstate(self) -> list[int]

@bmsstate.setter
def bmsstate(self, value: Sequence[int]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[int]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[int]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::BmsState_`
- 字段类型：`std::array<uint32_t, 5>`
- 声明位置：`include/unitree/idl/hg/BmsState_.hpp:35`

**用法**

```python
current_value = obj.bmsstate
obj.bmsstate = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-bmsstate-reserve"></a>
#### `unitree_sdk2_cpp.idl.hg.BmsState.reserve`

底层 `unitree_hg::msg::dds_::BmsState_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：取值范围为 0 到 4294967295。

**签名**

```python
@property
def reserve(self) -> list[int]

@reserve.setter
def reserve(self, value: Sequence[int]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[int]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[int]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::BmsState_`
- 字段类型：`std::array<uint32_t, 3>`
- 声明位置：`include/unitree/idl/hg/BmsState_.hpp:36`

**用法**

```python
current_value = obj.reserve
obj.reserve = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-motorcmd"></a>
### `unitree_sdk2_cpp.idl.hg.MotorCmd`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.hg import MotorCmd
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-hg-motorcmd-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-hg-motorcmd-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-hg-motorcmd-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`mode`](#unitree-sdk2-cpp-idl-hg-motorcmd-mode) | `int` | `int` | `AVAILABLE` |
| [`q`](#unitree-sdk2-cpp-idl-hg-motorcmd-q) | `float` | `float` | `AVAILABLE` |
| [`dq`](#unitree-sdk2-cpp-idl-hg-motorcmd-dq) | `float` | `float` | `AVAILABLE` |
| [`tau`](#unitree-sdk2-cpp-idl-hg-motorcmd-tau) | `float` | `float` | `AVAILABLE` |
| [`kp`](#unitree-sdk2-cpp-idl-hg-motorcmd-kp) | `float` | `float` | `AVAILABLE` |
| [`kd`](#unitree-sdk2-cpp-idl-hg-motorcmd-kd) | `float` | `float` | `AVAILABLE` |
| [`reserve`](#unitree-sdk2-cpp-idl-hg-motorcmd-reserve) | `int` | `int` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-hg-motorcmd-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.hg.MotorCmd.__init__`

初始化 `MotorCmd` 实例。是否能实际构造取决于下方可用性状态。

**签名**

```python
def __init__(self) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::MotorCmd_`
- 签名：`MotorCmd_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/hg/MotorCmd_.hpp:32`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = MotorCmd()
```

<a id="unitree-sdk2-cpp-idl-hg-motorcmd-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.hg.MotorCmd.__eq__`

按底层 IDL 消息内容比较两个对象是否相等。

**签名**

```python
def __eq__(self, other: object) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `other` | `object` | 必填 | 用于比较的另一个 Python 对象。类型不兼容时比较结果通常为 `False`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::MotorCmd_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-hg-motorcmd-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.hg.MotorCmd.__ne__`

按底层 IDL 消息内容比较两个对象是否不相等。

**签名**

```python
def __ne__(self, other: object) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `other` | `object` | 必填 | 用于比较的另一个 Python 对象。类型不兼容时比较结果通常为 `False`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::MotorCmd_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-hg-motorcmd-mode"></a>
#### `unitree_sdk2_cpp.idl.hg.MotorCmd.mode`

底层 `unitree_hg::msg::dds_::MotorCmd_` 的 `mode` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def mode(self) -> int

@mode.setter
def mode(self, value: int) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `int` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `int` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::MotorCmd_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/hg/MotorCmd_.hpp:23`

**用法**

```python
current_value = obj.mode
obj.mode = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-motorcmd-q"></a>
#### `unitree_sdk2_cpp.idl.hg.MotorCmd.q`

底层 `unitree_hg::msg::dds_::MotorCmd_` 的 `q` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def q(self) -> float

@q.setter
def q(self, value: float) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `float` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `float` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::MotorCmd_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/hg/MotorCmd_.hpp:24`

**用法**

```python
current_value = obj.q
obj.q = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-motorcmd-dq"></a>
#### `unitree_sdk2_cpp.idl.hg.MotorCmd.dq`

底层 `unitree_hg::msg::dds_::MotorCmd_` 的 `dq` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def dq(self) -> float

@dq.setter
def dq(self, value: float) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `float` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `float` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::MotorCmd_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/hg/MotorCmd_.hpp:25`

**用法**

```python
current_value = obj.dq
obj.dq = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-motorcmd-tau"></a>
#### `unitree_sdk2_cpp.idl.hg.MotorCmd.tau`

底层 `unitree_hg::msg::dds_::MotorCmd_` 的 `tau` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def tau(self) -> float

@tau.setter
def tau(self, value: float) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `float` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `float` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::MotorCmd_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/hg/MotorCmd_.hpp:26`

**用法**

```python
current_value = obj.tau
obj.tau = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-motorcmd-kp"></a>
#### `unitree_sdk2_cpp.idl.hg.MotorCmd.kp`

底层 `unitree_hg::msg::dds_::MotorCmd_` 的 `kp` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def kp(self) -> float

@kp.setter
def kp(self, value: float) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `float` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `float` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::MotorCmd_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/hg/MotorCmd_.hpp:27`

**用法**

```python
current_value = obj.kp
obj.kp = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-motorcmd-kd"></a>
#### `unitree_sdk2_cpp.idl.hg.MotorCmd.kd`

底层 `unitree_hg::msg::dds_::MotorCmd_` 的 `kd` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def kd(self) -> float

@kd.setter
def kd(self, value: float) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `float` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `float` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::MotorCmd_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/hg/MotorCmd_.hpp:28`

**用法**

```python
current_value = obj.kd
obj.kd = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-motorcmd-reserve"></a>
#### `unitree_sdk2_cpp.idl.hg.MotorCmd.reserve`

底层 `unitree_hg::msg::dds_::MotorCmd_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

**签名**

```python
@property
def reserve(self) -> int

@reserve.setter
def reserve(self, value: int) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `int` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `int` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::MotorCmd_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/hg/MotorCmd_.hpp:29`

**用法**

```python
current_value = obj.reserve
obj.reserve = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-handcmd"></a>
### `unitree_sdk2_cpp.idl.hg.HandCmd`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.hg import HandCmd
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-hg-handcmd-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-hg-handcmd-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-hg-handcmd-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`motor_cmd`](#unitree-sdk2-cpp-idl-hg-handcmd-motor-cmd) | `list[MotorCmd]` | `Sequence[MotorCmd]` | `AVAILABLE` |
| [`reserve`](#unitree-sdk2-cpp-idl-hg-handcmd-reserve) | `list[int]` | `Sequence[int]` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-hg-handcmd-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.hg.HandCmd.__init__`

初始化 `HandCmd` 实例。是否能实际构造取决于下方可用性状态。

**签名**

```python
def __init__(self) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::HandCmd_`
- 签名：`HandCmd_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/hg/HandCmd_.hpp:31`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = HandCmd()
```

<a id="unitree-sdk2-cpp-idl-hg-handcmd-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.hg.HandCmd.__eq__`

按底层 IDL 消息内容比较两个对象是否相等。

**签名**

```python
def __eq__(self, other: object) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `other` | `object` | 必填 | 用于比较的另一个 Python 对象。类型不兼容时比较结果通常为 `False`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::HandCmd_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-hg-handcmd-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.hg.HandCmd.__ne__`

按底层 IDL 消息内容比较两个对象是否不相等。

**签名**

```python
def __ne__(self, other: object) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `other` | `object` | 必填 | 用于比较的另一个 Python 对象。类型不兼容时比较结果通常为 `False`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::HandCmd_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-hg-handcmd-motor-cmd"></a>
#### `unitree_sdk2_cpp.idl.hg.HandCmd.motor_cmd`

底层 `unitree_hg::msg::dds_::HandCmd_` 的 `motor_cmd` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector

**签名**

```python
@property
def motor_cmd(self) -> list[MotorCmd]

@motor_cmd.setter
def motor_cmd(self, value: Sequence[MotorCmd]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[MotorCmd]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[MotorCmd]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::HandCmd_`
- 字段类型：`std::vector< ::unitree_hg::msg::dds_::MotorCmd_>`
- 声明位置：`include/unitree/idl/hg/HandCmd_.hpp:27`

**用法**

```python
current_value = obj.motor_cmd
obj.motor_cmd = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-handcmd-reserve"></a>
#### `unitree_sdk2_cpp.idl.hg.HandCmd.reserve`

底层 `unitree_hg::msg::dds_::HandCmd_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：取值范围为 0 到 4294967295。

**签名**

```python
@property
def reserve(self) -> list[int]

@reserve.setter
def reserve(self, value: Sequence[int]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[int]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[int]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::HandCmd_`
- 字段类型：`std::array<uint32_t, 4>`
- 声明位置：`include/unitree/idl/hg/HandCmd_.hpp:28`

**用法**

```python
current_value = obj.reserve
obj.reserve = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-imustate"></a>
### `unitree_sdk2_cpp.idl.hg.IMUState`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.hg import IMUState
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-hg-imustate-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-hg-imustate-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-hg-imustate-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`quaternion`](#unitree-sdk2-cpp-idl-hg-imustate-quaternion) | `list[float]` | `Sequence[float]` | `AVAILABLE` |
| [`gyroscope`](#unitree-sdk2-cpp-idl-hg-imustate-gyroscope) | `list[float]` | `Sequence[float]` | `AVAILABLE` |
| [`accelerometer`](#unitree-sdk2-cpp-idl-hg-imustate-accelerometer) | `list[float]` | `Sequence[float]` | `AVAILABLE` |
| [`rpy`](#unitree-sdk2-cpp-idl-hg-imustate-rpy) | `list[float]` | `Sequence[float]` | `AVAILABLE` |
| [`temperature`](#unitree-sdk2-cpp-idl-hg-imustate-temperature) | `int` | `int` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-hg-imustate-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.hg.IMUState.__init__`

初始化 `IMUState` 实例。是否能实际构造取决于下方可用性状态。

**签名**

```python
def __init__(self) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::IMUState_`
- 签名：`IMUState_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/hg/IMUState_.hpp:31`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = IMUState()
```

<a id="unitree-sdk2-cpp-idl-hg-imustate-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.hg.IMUState.__eq__`

按底层 IDL 消息内容比较两个对象是否相等。

**签名**

```python
def __eq__(self, other: object) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `other` | `object` | 必填 | 用于比较的另一个 Python 对象。类型不兼容时比较结果通常为 `False`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::IMUState_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-hg-imustate-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.hg.IMUState.__ne__`

按底层 IDL 消息内容比较两个对象是否不相等。

**签名**

```python
def __ne__(self, other: object) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `other` | `object` | 必填 | 用于比较的另一个 Python 对象。类型不兼容时比较结果通常为 `False`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::IMUState_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-hg-imustate-quaternion"></a>
#### `unitree_sdk2_cpp.idl.hg.IMUState.quaternion`

底层 `unitree_hg::msg::dds_::IMUState_` 的 `quaternion` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def quaternion(self) -> list[float]

@quaternion.setter
def quaternion(self, value: Sequence[float]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[float]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[float]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::IMUState_`
- 字段类型：`std::array<float, 4>`
- 声明位置：`include/unitree/idl/hg/IMUState_.hpp:24`

**用法**

```python
current_value = obj.quaternion
obj.quaternion = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-imustate-gyroscope"></a>
#### `unitree_sdk2_cpp.idl.hg.IMUState.gyroscope`

底层 `unitree_hg::msg::dds_::IMUState_` 的 `gyroscope` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def gyroscope(self) -> list[float]

@gyroscope.setter
def gyroscope(self, value: Sequence[float]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[float]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[float]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::IMUState_`
- 字段类型：`std::array<float, 3>`
- 声明位置：`include/unitree/idl/hg/IMUState_.hpp:25`

**用法**

```python
current_value = obj.gyroscope
obj.gyroscope = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-imustate-accelerometer"></a>
#### `unitree_sdk2_cpp.idl.hg.IMUState.accelerometer`

底层 `unitree_hg::msg::dds_::IMUState_` 的 `accelerometer` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def accelerometer(self) -> list[float]

@accelerometer.setter
def accelerometer(self, value: Sequence[float]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[float]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[float]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::IMUState_`
- 字段类型：`std::array<float, 3>`
- 声明位置：`include/unitree/idl/hg/IMUState_.hpp:26`

**用法**

```python
current_value = obj.accelerometer
obj.accelerometer = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-imustate-rpy"></a>
#### `unitree_sdk2_cpp.idl.hg.IMUState.rpy`

底层 `unitree_hg::msg::dds_::IMUState_` 的 `rpy` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def rpy(self) -> list[float]

@rpy.setter
def rpy(self, value: Sequence[float]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[float]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[float]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::IMUState_`
- 字段类型：`std::array<float, 3>`
- 声明位置：`include/unitree/idl/hg/IMUState_.hpp:27`

**用法**

```python
current_value = obj.rpy
obj.rpy = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-imustate-temperature"></a>
#### `unitree_sdk2_cpp.idl.hg.IMUState.temperature`

底层 `unitree_hg::msg::dds_::IMUState_` 的 `temperature` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 -32768 到 32767。

**签名**

```python
@property
def temperature(self) -> int

@temperature.setter
def temperature(self, value: int) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `int` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `int` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::IMUState_`
- 字段类型：`int16_t`
- 声明位置：`include/unitree/idl/hg/IMUState_.hpp:28`

**用法**

```python
current_value = obj.temperature
obj.temperature = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-motorstate"></a>
### `unitree_sdk2_cpp.idl.hg.MotorState`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.hg import MotorState
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-hg-motorstate-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-hg-motorstate-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-hg-motorstate-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`mode`](#unitree-sdk2-cpp-idl-hg-motorstate-mode) | `int` | `int` | `AVAILABLE` |
| [`q`](#unitree-sdk2-cpp-idl-hg-motorstate-q) | `float` | `float` | `AVAILABLE` |
| [`dq`](#unitree-sdk2-cpp-idl-hg-motorstate-dq) | `float` | `float` | `AVAILABLE` |
| [`ddq`](#unitree-sdk2-cpp-idl-hg-motorstate-ddq) | `float` | `float` | `AVAILABLE` |
| [`tau_est`](#unitree-sdk2-cpp-idl-hg-motorstate-tau-est) | `float` | `float` | `AVAILABLE` |
| [`temperature`](#unitree-sdk2-cpp-idl-hg-motorstate-temperature) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`vol`](#unitree-sdk2-cpp-idl-hg-motorstate-vol) | `float` | `float` | `AVAILABLE` |
| [`sensor`](#unitree-sdk2-cpp-idl-hg-motorstate-sensor) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`motorstate`](#unitree-sdk2-cpp-idl-hg-motorstate-motorstate) | `int` | `int` | `AVAILABLE` |
| [`reserve`](#unitree-sdk2-cpp-idl-hg-motorstate-reserve) | `list[int]` | `Sequence[int]` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-hg-motorstate-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.hg.MotorState.__init__`

初始化 `MotorState` 实例。是否能实际构造取决于下方可用性状态。

**签名**

```python
def __init__(self) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::MotorState_`
- 签名：`MotorState_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/hg/MotorState_.hpp:36`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = MotorState()
```

<a id="unitree-sdk2-cpp-idl-hg-motorstate-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.hg.MotorState.__eq__`

按底层 IDL 消息内容比较两个对象是否相等。

**签名**

```python
def __eq__(self, other: object) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `other` | `object` | 必填 | 用于比较的另一个 Python 对象。类型不兼容时比较结果通常为 `False`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::MotorState_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-hg-motorstate-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.hg.MotorState.__ne__`

按底层 IDL 消息内容比较两个对象是否不相等。

**签名**

```python
def __ne__(self, other: object) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `other` | `object` | 必填 | 用于比较的另一个 Python 对象。类型不兼容时比较结果通常为 `False`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::MotorState_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-hg-motorstate-mode"></a>
#### `unitree_sdk2_cpp.idl.hg.MotorState.mode`

底层 `unitree_hg::msg::dds_::MotorState_` 的 `mode` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def mode(self) -> int

@mode.setter
def mode(self, value: int) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `int` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `int` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::MotorState_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/hg/MotorState_.hpp:24`

**用法**

```python
current_value = obj.mode
obj.mode = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-motorstate-q"></a>
#### `unitree_sdk2_cpp.idl.hg.MotorState.q`

底层 `unitree_hg::msg::dds_::MotorState_` 的 `q` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def q(self) -> float

@q.setter
def q(self, value: float) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `float` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `float` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::MotorState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/hg/MotorState_.hpp:25`

**用法**

```python
current_value = obj.q
obj.q = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-motorstate-dq"></a>
#### `unitree_sdk2_cpp.idl.hg.MotorState.dq`

底层 `unitree_hg::msg::dds_::MotorState_` 的 `dq` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def dq(self) -> float

@dq.setter
def dq(self, value: float) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `float` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `float` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::MotorState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/hg/MotorState_.hpp:26`

**用法**

```python
current_value = obj.dq
obj.dq = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-motorstate-ddq"></a>
#### `unitree_sdk2_cpp.idl.hg.MotorState.ddq`

底层 `unitree_hg::msg::dds_::MotorState_` 的 `ddq` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def ddq(self) -> float

@ddq.setter
def ddq(self, value: float) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `float` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `float` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::MotorState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/hg/MotorState_.hpp:27`

**用法**

```python
current_value = obj.ddq
obj.ddq = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-motorstate-tau-est"></a>
#### `unitree_sdk2_cpp.idl.hg.MotorState.tau_est`

底层 `unitree_hg::msg::dds_::MotorState_` 的 `tau_est` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def tau_est(self) -> float

@tau_est.setter
def tau_est(self, value: float) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `float` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `float` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::MotorState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/hg/MotorState_.hpp:28`

**用法**

```python
current_value = obj.tau_est
obj.tau_est = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-motorstate-temperature"></a>
#### `unitree_sdk2_cpp.idl.hg.MotorState.temperature`

底层 `unitree_hg::msg::dds_::MotorState_` 的 `temperature` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 -32768 到 32767。

**签名**

```python
@property
def temperature(self) -> list[int]

@temperature.setter
def temperature(self, value: Sequence[int]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[int]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[int]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::MotorState_`
- 字段类型：`std::array<int16_t, 2>`
- 声明位置：`include/unitree/idl/hg/MotorState_.hpp:29`

**用法**

```python
current_value = obj.temperature
obj.temperature = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-motorstate-vol"></a>
#### `unitree_sdk2_cpp.idl.hg.MotorState.vol`

底层 `unitree_hg::msg::dds_::MotorState_` 的 `vol` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def vol(self) -> float

@vol.setter
def vol(self, value: float) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `float` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `float` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::MotorState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/hg/MotorState_.hpp:30`

**用法**

```python
current_value = obj.vol
obj.vol = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-motorstate-sensor"></a>
#### `unitree_sdk2_cpp.idl.hg.MotorState.sensor`

底层 `unitree_hg::msg::dds_::MotorState_` 的 `sensor` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 4294967295。

**签名**

```python
@property
def sensor(self) -> list[int]

@sensor.setter
def sensor(self, value: Sequence[int]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[int]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[int]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::MotorState_`
- 字段类型：`std::array<uint32_t, 2>`
- 声明位置：`include/unitree/idl/hg/MotorState_.hpp:31`

**用法**

```python
current_value = obj.sensor
obj.sensor = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-motorstate-motorstate"></a>
#### `unitree_sdk2_cpp.idl.hg.MotorState.motorstate`

底层 `unitree_hg::msg::dds_::MotorState_` 的 `motorstate` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

**签名**

```python
@property
def motorstate(self) -> int

@motorstate.setter
def motorstate(self, value: int) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `int` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `int` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::MotorState_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/hg/MotorState_.hpp:32`

**用法**

```python
current_value = obj.motorstate
obj.motorstate = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-motorstate-reserve"></a>
#### `unitree_sdk2_cpp.idl.hg.MotorState.reserve`

底层 `unitree_hg::msg::dds_::MotorState_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：取值范围为 0 到 4294967295。

**签名**

```python
@property
def reserve(self) -> list[int]

@reserve.setter
def reserve(self, value: Sequence[int]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[int]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[int]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::MotorState_`
- 字段类型：`std::array<uint32_t, 4>`
- 声明位置：`include/unitree/idl/hg/MotorState_.hpp:33`

**用法**

```python
current_value = obj.reserve
obj.reserve = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-presssensorstate"></a>
### `unitree_sdk2_cpp.idl.hg.PressSensorState`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.hg import PressSensorState
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-hg-presssensorstate-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-hg-presssensorstate-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-hg-presssensorstate-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`pressure`](#unitree-sdk2-cpp-idl-hg-presssensorstate-pressure) | `list[float]` | `Sequence[float]` | `AVAILABLE` |
| [`temperature`](#unitree-sdk2-cpp-idl-hg-presssensorstate-temperature) | `list[float]` | `Sequence[float]` | `AVAILABLE` |
| [`lost`](#unitree-sdk2-cpp-idl-hg-presssensorstate-lost) | `int` | `int` | `AVAILABLE` |
| [`reserve`](#unitree-sdk2-cpp-idl-hg-presssensorstate-reserve) | `int` | `int` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-hg-presssensorstate-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.hg.PressSensorState.__init__`

初始化 `PressSensorState` 实例。是否能实际构造取决于下方可用性状态。

**签名**

```python
def __init__(self) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::PressSensorState_`
- 签名：`PressSensorState_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/hg/PressSensorState_.hpp:30`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = PressSensorState()
```

<a id="unitree-sdk2-cpp-idl-hg-presssensorstate-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.hg.PressSensorState.__eq__`

按底层 IDL 消息内容比较两个对象是否相等。

**签名**

```python
def __eq__(self, other: object) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `other` | `object` | 必填 | 用于比较的另一个 Python 对象。类型不兼容时比较结果通常为 `False`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::PressSensorState_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-hg-presssensorstate-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.hg.PressSensorState.__ne__`

按底层 IDL 消息内容比较两个对象是否不相等。

**签名**

```python
def __ne__(self, other: object) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `other` | `object` | 必填 | 用于比较的另一个 Python 对象。类型不兼容时比较结果通常为 `False`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::PressSensorState_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-hg-presssensorstate-pressure"></a>
#### `unitree_sdk2_cpp.idl.hg.PressSensorState.pressure`

底层 `unitree_hg::msg::dds_::PressSensorState_` 的 `pressure` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 12 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def pressure(self) -> list[float]

@pressure.setter
def pressure(self, value: Sequence[float]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[float]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[float]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::PressSensorState_`
- 字段类型：`std::array<float, 12>`
- 声明位置：`include/unitree/idl/hg/PressSensorState_.hpp:24`

**用法**

```python
current_value = obj.pressure
obj.pressure = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-presssensorstate-temperature"></a>
#### `unitree_sdk2_cpp.idl.hg.PressSensorState.temperature`

底层 `unitree_hg::msg::dds_::PressSensorState_` 的 `temperature` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 12 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def temperature(self) -> list[float]

@temperature.setter
def temperature(self, value: Sequence[float]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[float]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[float]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::PressSensorState_`
- 字段类型：`std::array<float, 12>`
- 声明位置：`include/unitree/idl/hg/PressSensorState_.hpp:25`

**用法**

```python
current_value = obj.temperature
obj.temperature = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-presssensorstate-lost"></a>
#### `unitree_sdk2_cpp.idl.hg.PressSensorState.lost`

底层 `unitree_hg::msg::dds_::PressSensorState_` 的 `lost` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

**签名**

```python
@property
def lost(self) -> int

@lost.setter
def lost(self, value: int) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `int` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `int` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::PressSensorState_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/hg/PressSensorState_.hpp:26`

**用法**

```python
current_value = obj.lost
obj.lost = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-presssensorstate-reserve"></a>
#### `unitree_sdk2_cpp.idl.hg.PressSensorState.reserve`

底层 `unitree_hg::msg::dds_::PressSensorState_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

**签名**

```python
@property
def reserve(self) -> int

@reserve.setter
def reserve(self, value: int) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `int` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `int` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::PressSensorState_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/hg/PressSensorState_.hpp:27`

**用法**

```python
current_value = obj.reserve
obj.reserve = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-handstate"></a>
### `unitree_sdk2_cpp.idl.hg.HandState`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.hg import HandState
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-hg-handstate-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-hg-handstate-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-hg-handstate-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`motor_state`](#unitree-sdk2-cpp-idl-hg-handstate-motor-state) | `list[MotorState]` | `Sequence[MotorState]` | `AVAILABLE` |
| [`press_sensor_state`](#unitree-sdk2-cpp-idl-hg-handstate-press-sensor-state) | `list[PressSensorState]` | `Sequence[PressSensorState]` | `AVAILABLE` |
| [`imu_state`](#unitree-sdk2-cpp-idl-hg-handstate-imu-state) | `IMUState` | `IMUState` | `AVAILABLE` |
| [`power_v`](#unitree-sdk2-cpp-idl-hg-handstate-power-v) | `float` | `float` | `AVAILABLE` |
| [`power_a`](#unitree-sdk2-cpp-idl-hg-handstate-power-a) | `float` | `float` | `AVAILABLE` |
| [`system_v`](#unitree-sdk2-cpp-idl-hg-handstate-system-v) | `float` | `float` | `AVAILABLE` |
| [`device_v`](#unitree-sdk2-cpp-idl-hg-handstate-device-v) | `float` | `float` | `AVAILABLE` |
| [`error`](#unitree-sdk2-cpp-idl-hg-handstate-error) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`reserve`](#unitree-sdk2-cpp-idl-hg-handstate-reserve) | `list[int]` | `Sequence[int]` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-hg-handstate-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.hg.HandState.__init__`

初始化 `HandState` 实例。是否能实际构造取决于下方可用性状态。

**签名**

```python
def __init__(self) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::HandState_`
- 签名：`HandState_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/hg/HandState_.hpp:42`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = HandState()
```

<a id="unitree-sdk2-cpp-idl-hg-handstate-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.hg.HandState.__eq__`

按底层 IDL 消息内容比较两个对象是否相等。

**签名**

```python
def __eq__(self, other: object) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `other` | `object` | 必填 | 用于比较的另一个 Python 对象。类型不兼容时比较结果通常为 `False`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::HandState_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-hg-handstate-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.hg.HandState.__ne__`

按底层 IDL 消息内容比较两个对象是否不相等。

**签名**

```python
def __ne__(self, other: object) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `other` | `object` | 必填 | 用于比较的另一个 Python 对象。类型不兼容时比较结果通常为 `False`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::HandState_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-hg-handstate-motor-state"></a>
#### `unitree_sdk2_cpp.idl.hg.HandState.motor_state`

底层 `unitree_hg::msg::dds_::HandState_` 的 `motor_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector

**签名**

```python
@property
def motor_state(self) -> list[MotorState]

@motor_state.setter
def motor_state(self, value: Sequence[MotorState]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[MotorState]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[MotorState]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::HandState_`
- 字段类型：`std::vector< ::unitree_hg::msg::dds_::MotorState_>`
- 声明位置：`include/unitree/idl/hg/HandState_.hpp:31`

**用法**

```python
current_value = obj.motor_state
obj.motor_state = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-handstate-press-sensor-state"></a>
#### `unitree_sdk2_cpp.idl.hg.HandState.press_sensor_state`

底层 `unitree_hg::msg::dds_::HandState_` 的 `press_sensor_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector

**签名**

```python
@property
def press_sensor_state(self) -> list[PressSensorState]

@press_sensor_state.setter
def press_sensor_state(self, value: Sequence[PressSensorState]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[PressSensorState]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[PressSensorState]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::HandState_`
- 字段类型：`std::vector< ::unitree_hg::msg::dds_::PressSensorState_>`
- 声明位置：`include/unitree/idl/hg/HandState_.hpp:32`

**用法**

```python
current_value = obj.press_sensor_state
obj.press_sensor_state = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-handstate-imu-state"></a>
#### `unitree_sdk2_cpp.idl.hg.HandState.imu_state`

底层 `unitree_hg::msg::dds_::HandState_` 的 `imu_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def imu_state(self) -> IMUState

@imu_state.setter
def imu_state(self, value: IMUState) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `IMUState` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `IMUState` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::HandState_`
- 字段类型：`::unitree_hg::msg::dds_::IMUState_`
- 声明位置：`include/unitree/idl/hg/HandState_.hpp:33`

**用法**

```python
current_value = obj.imu_state
obj.imu_state = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-handstate-power-v"></a>
#### `unitree_sdk2_cpp.idl.hg.HandState.power_v`

底层 `unitree_hg::msg::dds_::HandState_` 的 `power_v` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def power_v(self) -> float

@power_v.setter
def power_v(self, value: float) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `float` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `float` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::HandState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/hg/HandState_.hpp:34`

**用法**

```python
current_value = obj.power_v
obj.power_v = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-handstate-power-a"></a>
#### `unitree_sdk2_cpp.idl.hg.HandState.power_a`

底层 `unitree_hg::msg::dds_::HandState_` 的 `power_a` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def power_a(self) -> float

@power_a.setter
def power_a(self, value: float) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `float` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `float` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::HandState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/hg/HandState_.hpp:35`

**用法**

```python
current_value = obj.power_a
obj.power_a = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-handstate-system-v"></a>
#### `unitree_sdk2_cpp.idl.hg.HandState.system_v`

底层 `unitree_hg::msg::dds_::HandState_` 的 `system_v` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def system_v(self) -> float

@system_v.setter
def system_v(self, value: float) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `float` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `float` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::HandState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/hg/HandState_.hpp:36`

**用法**

```python
current_value = obj.system_v
obj.system_v = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-handstate-device-v"></a>
#### `unitree_sdk2_cpp.idl.hg.HandState.device_v`

底层 `unitree_hg::msg::dds_::HandState_` 的 `device_v` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def device_v(self) -> float

@device_v.setter
def device_v(self, value: float) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `float` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `float` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::HandState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/hg/HandState_.hpp:37`

**用法**

```python
current_value = obj.device_v
obj.device_v = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-handstate-error"></a>
#### `unitree_sdk2_cpp.idl.hg.HandState.error`

底层 `unitree_hg::msg::dds_::HandState_` 的 `error` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 4294967295。

**签名**

```python
@property
def error(self) -> list[int]

@error.setter
def error(self, value: Sequence[int]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[int]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[int]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::HandState_`
- 字段类型：`std::array<uint32_t, 2>`
- 声明位置：`include/unitree/idl/hg/HandState_.hpp:38`

**用法**

```python
current_value = obj.error
obj.error = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-handstate-reserve"></a>
#### `unitree_sdk2_cpp.idl.hg.HandState.reserve`

底层 `unitree_hg::msg::dds_::HandState_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 4294967295。

**签名**

```python
@property
def reserve(self) -> list[int]

@reserve.setter
def reserve(self, value: Sequence[int]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[int]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[int]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::HandState_`
- 字段类型：`std::array<uint32_t, 2>`
- 声明位置：`include/unitree/idl/hg/HandState_.hpp:39`

**用法**

```python
current_value = obj.reserve
obj.reserve = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-lowcmd"></a>
### `unitree_sdk2_cpp.idl.hg.LowCmd`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.hg import LowCmd
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-hg-lowcmd-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-hg-lowcmd-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-hg-lowcmd-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`mode_pr`](#unitree-sdk2-cpp-idl-hg-lowcmd-mode-pr) | `int` | `int` | `AVAILABLE` |
| [`mode_machine`](#unitree-sdk2-cpp-idl-hg-lowcmd-mode-machine) | `int` | `int` | `AVAILABLE` |
| [`motor_cmd`](#unitree-sdk2-cpp-idl-hg-lowcmd-motor-cmd) | `list[MotorCmd]` | `Sequence[MotorCmd]` | `AVAILABLE` |
| [`reserve`](#unitree-sdk2-cpp-idl-hg-lowcmd-reserve) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`crc`](#unitree-sdk2-cpp-idl-hg-lowcmd-crc) | `int` | `int` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-hg-lowcmd-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.hg.LowCmd.__init__`

初始化 `LowCmd` 实例。是否能实际构造取决于下方可用性状态。

**签名**

```python
def __init__(self) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::LowCmd_`
- 签名：`LowCmd_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/hg/LowCmd_.hpp:33`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = LowCmd()
```

<a id="unitree-sdk2-cpp-idl-hg-lowcmd-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.hg.LowCmd.__eq__`

按底层 IDL 消息内容比较两个对象是否相等。

**签名**

```python
def __eq__(self, other: object) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `other` | `object` | 必填 | 用于比较的另一个 Python 对象。类型不兼容时比较结果通常为 `False`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::LowCmd_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-hg-lowcmd-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.hg.LowCmd.__ne__`

按底层 IDL 消息内容比较两个对象是否不相等。

**签名**

```python
def __ne__(self, other: object) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `other` | `object` | 必填 | 用于比较的另一个 Python 对象。类型不兼容时比较结果通常为 `False`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::LowCmd_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-hg-lowcmd-mode-pr"></a>
#### `unitree_sdk2_cpp.idl.hg.LowCmd.mode_pr`

底层 `unitree_hg::msg::dds_::LowCmd_` 的 `mode_pr` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def mode_pr(self) -> int

@mode_pr.setter
def mode_pr(self, value: int) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `int` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `int` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::LowCmd_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/hg/LowCmd_.hpp:26`

**用法**

```python
current_value = obj.mode_pr
obj.mode_pr = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-lowcmd-mode-machine"></a>
#### `unitree_sdk2_cpp.idl.hg.LowCmd.mode_machine`

底层 `unitree_hg::msg::dds_::LowCmd_` 的 `mode_machine` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def mode_machine(self) -> int

@mode_machine.setter
def mode_machine(self, value: int) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `int` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `int` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::LowCmd_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/hg/LowCmd_.hpp:27`

**用法**

```python
current_value = obj.mode_machine
obj.mode_machine = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-lowcmd-motor-cmd"></a>
#### `unitree_sdk2_cpp.idl.hg.LowCmd.motor_cmd`

底层 `unitree_hg::msg::dds_::LowCmd_` 的 `motor_cmd` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 35 个元素

**签名**

```python
@property
def motor_cmd(self) -> list[MotorCmd]

@motor_cmd.setter
def motor_cmd(self, value: Sequence[MotorCmd]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[MotorCmd]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[MotorCmd]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::LowCmd_`
- 字段类型：`std::array< ::unitree_hg::msg::dds_::MotorCmd_, 35>`
- 声明位置：`include/unitree/idl/hg/LowCmd_.hpp:28`

**用法**

```python
current_value = obj.motor_cmd
obj.motor_cmd = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-lowcmd-reserve"></a>
#### `unitree_sdk2_cpp.idl.hg.LowCmd.reserve`

底层 `unitree_hg::msg::dds_::LowCmd_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：取值范围为 0 到 4294967295。

**签名**

```python
@property
def reserve(self) -> list[int]

@reserve.setter
def reserve(self, value: Sequence[int]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[int]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[int]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::LowCmd_`
- 字段类型：`std::array<uint32_t, 4>`
- 声明位置：`include/unitree/idl/hg/LowCmd_.hpp:29`

**用法**

```python
current_value = obj.reserve
obj.reserve = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-lowcmd-crc"></a>
#### `unitree_sdk2_cpp.idl.hg.LowCmd.crc`

底层 `unitree_hg::msg::dds_::LowCmd_` 的 `crc` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

**签名**

```python
@property
def crc(self) -> int

@crc.setter
def crc(self, value: int) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `int` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `int` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::LowCmd_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/hg/LowCmd_.hpp:30`

**用法**

```python
current_value = obj.crc
obj.crc = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-lowstate"></a>
### `unitree_sdk2_cpp.idl.hg.LowState`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.hg import LowState
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-hg-lowstate-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-hg-lowstate-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-hg-lowstate-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`version`](#unitree-sdk2-cpp-idl-hg-lowstate-version) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`mode_pr`](#unitree-sdk2-cpp-idl-hg-lowstate-mode-pr) | `int` | `int` | `AVAILABLE` |
| [`mode_machine`](#unitree-sdk2-cpp-idl-hg-lowstate-mode-machine) | `int` | `int` | `AVAILABLE` |
| [`tick`](#unitree-sdk2-cpp-idl-hg-lowstate-tick) | `int` | `int` | `AVAILABLE` |
| [`imu_state`](#unitree-sdk2-cpp-idl-hg-lowstate-imu-state) | `IMUState` | `IMUState` | `AVAILABLE` |
| [`motor_state`](#unitree-sdk2-cpp-idl-hg-lowstate-motor-state) | `list[MotorState]` | `Sequence[MotorState]` | `AVAILABLE` |
| [`wireless_remote`](#unitree-sdk2-cpp-idl-hg-lowstate-wireless-remote) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`reserve`](#unitree-sdk2-cpp-idl-hg-lowstate-reserve) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`crc`](#unitree-sdk2-cpp-idl-hg-lowstate-crc) | `int` | `int` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-hg-lowstate-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.hg.LowState.__init__`

初始化 `LowState` 实例。是否能实际构造取决于下方可用性状态。

**签名**

```python
def __init__(self) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::LowState_`
- 签名：`LowState_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/hg/LowState_.hpp:39`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = LowState()
```

<a id="unitree-sdk2-cpp-idl-hg-lowstate-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.hg.LowState.__eq__`

按底层 IDL 消息内容比较两个对象是否相等。

**签名**

```python
def __eq__(self, other: object) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `other` | `object` | 必填 | 用于比较的另一个 Python 对象。类型不兼容时比较结果通常为 `False`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::LowState_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-hg-lowstate-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.hg.LowState.__ne__`

按底层 IDL 消息内容比较两个对象是否不相等。

**签名**

```python
def __ne__(self, other: object) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `other` | `object` | 必填 | 用于比较的另一个 Python 对象。类型不兼容时比较结果通常为 `False`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::LowState_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-hg-lowstate-version"></a>
#### `unitree_sdk2_cpp.idl.hg.LowState.version`

底层 `unitree_hg::msg::dds_::LowState_` 的 `version` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 4294967295。

**签名**

```python
@property
def version(self) -> list[int]

@version.setter
def version(self, value: Sequence[int]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[int]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[int]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::LowState_`
- 字段类型：`std::array<uint32_t, 2>`
- 声明位置：`include/unitree/idl/hg/LowState_.hpp:28`

**用法**

```python
current_value = obj.version
obj.version = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-lowstate-mode-pr"></a>
#### `unitree_sdk2_cpp.idl.hg.LowState.mode_pr`

底层 `unitree_hg::msg::dds_::LowState_` 的 `mode_pr` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def mode_pr(self) -> int

@mode_pr.setter
def mode_pr(self, value: int) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `int` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `int` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::LowState_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/hg/LowState_.hpp:29`

**用法**

```python
current_value = obj.mode_pr
obj.mode_pr = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-lowstate-mode-machine"></a>
#### `unitree_sdk2_cpp.idl.hg.LowState.mode_machine`

底层 `unitree_hg::msg::dds_::LowState_` 的 `mode_machine` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def mode_machine(self) -> int

@mode_machine.setter
def mode_machine(self, value: int) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `int` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `int` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::LowState_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/hg/LowState_.hpp:30`

**用法**

```python
current_value = obj.mode_machine
obj.mode_machine = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-lowstate-tick"></a>
#### `unitree_sdk2_cpp.idl.hg.LowState.tick`

底层 `unitree_hg::msg::dds_::LowState_` 的 `tick` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

**签名**

```python
@property
def tick(self) -> int

@tick.setter
def tick(self, value: int) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `int` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `int` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::LowState_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/hg/LowState_.hpp:31`

**用法**

```python
current_value = obj.tick
obj.tick = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-lowstate-imu-state"></a>
#### `unitree_sdk2_cpp.idl.hg.LowState.imu_state`

底层 `unitree_hg::msg::dds_::LowState_` 的 `imu_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def imu_state(self) -> IMUState

@imu_state.setter
def imu_state(self, value: IMUState) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `IMUState` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `IMUState` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::LowState_`
- 字段类型：`::unitree_hg::msg::dds_::IMUState_`
- 声明位置：`include/unitree/idl/hg/LowState_.hpp:32`

**用法**

```python
current_value = obj.imu_state
obj.imu_state = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-lowstate-motor-state"></a>
#### `unitree_sdk2_cpp.idl.hg.LowState.motor_state`

底层 `unitree_hg::msg::dds_::LowState_` 的 `motor_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 35 个元素

**签名**

```python
@property
def motor_state(self) -> list[MotorState]

@motor_state.setter
def motor_state(self, value: Sequence[MotorState]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[MotorState]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[MotorState]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::LowState_`
- 字段类型：`std::array< ::unitree_hg::msg::dds_::MotorState_, 35>`
- 声明位置：`include/unitree/idl/hg/LowState_.hpp:33`

**用法**

```python
current_value = obj.motor_state
obj.motor_state = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-lowstate-wireless-remote"></a>
#### `unitree_sdk2_cpp.idl.hg.LowState.wireless_remote`

底层 `unitree_hg::msg::dds_::LowState_` 的 `wireless_remote` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 40 个元素；元素约束：取值范围为 0 到 255。

**签名**

```python
@property
def wireless_remote(self) -> list[int]

@wireless_remote.setter
def wireless_remote(self, value: Sequence[int]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[int]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[int]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::LowState_`
- 字段类型：`std::array<uint8_t, 40>`
- 声明位置：`include/unitree/idl/hg/LowState_.hpp:34`

**用法**

```python
current_value = obj.wireless_remote
obj.wireless_remote = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-lowstate-reserve"></a>
#### `unitree_sdk2_cpp.idl.hg.LowState.reserve`

底层 `unitree_hg::msg::dds_::LowState_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：取值范围为 0 到 4294967295。

**签名**

```python
@property
def reserve(self) -> list[int]

@reserve.setter
def reserve(self, value: Sequence[int]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[int]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[int]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::LowState_`
- 字段类型：`std::array<uint32_t, 4>`
- 声明位置：`include/unitree/idl/hg/LowState_.hpp:35`

**用法**

```python
current_value = obj.reserve
obj.reserve = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-lowstate-crc"></a>
#### `unitree_sdk2_cpp.idl.hg.LowState.crc`

底层 `unitree_hg::msg::dds_::LowState_` 的 `crc` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

**签名**

```python
@property
def crc(self) -> int

@crc.setter
def crc(self, value: int) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `int` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `int` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::LowState_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/hg/LowState_.hpp:36`

**用法**

```python
current_value = obj.crc
obj.crc = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-mainboardstate"></a>
### `unitree_sdk2_cpp.idl.hg.MainBoardState`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.hg import MainBoardState
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-hg-mainboardstate-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-hg-mainboardstate-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-hg-mainboardstate-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`fan_state`](#unitree-sdk2-cpp-idl-hg-mainboardstate-fan-state) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`temperature`](#unitree-sdk2-cpp-idl-hg-mainboardstate-temperature) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`value`](#unitree-sdk2-cpp-idl-hg-mainboardstate-value) | `list[float]` | `Sequence[float]` | `AVAILABLE` |
| [`state`](#unitree-sdk2-cpp-idl-hg-mainboardstate-state) | `list[int]` | `Sequence[int]` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-hg-mainboardstate-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.hg.MainBoardState.__init__`

初始化 `MainBoardState` 实例。是否能实际构造取决于下方可用性状态。

**签名**

```python
def __init__(self) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::MainBoardState_`
- 签名：`MainBoardState_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/hg/MainBoardState_.hpp:30`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = MainBoardState()
```

<a id="unitree-sdk2-cpp-idl-hg-mainboardstate-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.hg.MainBoardState.__eq__`

按底层 IDL 消息内容比较两个对象是否相等。

**签名**

```python
def __eq__(self, other: object) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `other` | `object` | 必填 | 用于比较的另一个 Python 对象。类型不兼容时比较结果通常为 `False`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::MainBoardState_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-hg-mainboardstate-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.hg.MainBoardState.__ne__`

按底层 IDL 消息内容比较两个对象是否不相等。

**签名**

```python
def __ne__(self, other: object) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `other` | `object` | 必填 | 用于比较的另一个 Python 对象。类型不兼容时比较结果通常为 `False`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::MainBoardState_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-hg-mainboardstate-fan-state"></a>
#### `unitree_sdk2_cpp.idl.hg.MainBoardState.fan_state`

底层 `unitree_hg::msg::dds_::MainBoardState_` 的 `fan_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 6 个元素；元素约束：取值范围为 0 到 65535。

**签名**

```python
@property
def fan_state(self) -> list[int]

@fan_state.setter
def fan_state(self, value: Sequence[int]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[int]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[int]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::MainBoardState_`
- 字段类型：`std::array<uint16_t, 6>`
- 声明位置：`include/unitree/idl/hg/MainBoardState_.hpp:24`

**用法**

```python
current_value = obj.fan_state
obj.fan_state = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-mainboardstate-temperature"></a>
#### `unitree_sdk2_cpp.idl.hg.MainBoardState.temperature`

底层 `unitree_hg::msg::dds_::MainBoardState_` 的 `temperature` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 6 个元素；元素约束：取值范围为 -32768 到 32767。

**签名**

```python
@property
def temperature(self) -> list[int]

@temperature.setter
def temperature(self, value: Sequence[int]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[int]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[int]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::MainBoardState_`
- 字段类型：`std::array<int16_t, 6>`
- 声明位置：`include/unitree/idl/hg/MainBoardState_.hpp:25`

**用法**

```python
current_value = obj.temperature
obj.temperature = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-mainboardstate-value"></a>
#### `unitree_sdk2_cpp.idl.hg.MainBoardState.value`

底层 `unitree_hg::msg::dds_::MainBoardState_` 的 `value` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 6 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def value(self) -> list[float]

@value.setter
def value(self, value: Sequence[float]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[float]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[float]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::MainBoardState_`
- 字段类型：`std::array<float, 6>`
- 声明位置：`include/unitree/idl/hg/MainBoardState_.hpp:26`

**用法**

```python
current_value = obj.value
obj.value = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-mainboardstate-state"></a>
#### `unitree_sdk2_cpp.idl.hg.MainBoardState.state`

底层 `unitree_hg::msg::dds_::MainBoardState_` 的 `state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 6 个元素；元素约束：取值范围为 0 到 4294967295。

**签名**

```python
@property
def state(self) -> list[int]

@state.setter
def state(self, value: Sequence[int]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[int]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[int]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::MainBoardState_`
- 字段类型：`std::array<uint32_t, 6>`
- 声明位置：`include/unitree/idl/hg/MainBoardState_.hpp:27`

**用法**

```python
current_value = obj.state
obj.state = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-sportmodestate"></a>
### `unitree_sdk2_cpp.idl.hg.SportModeState`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.hg import SportModeState
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-hg-sportmodestate-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-hg-sportmodestate-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-hg-sportmodestate-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`fsm_id`](#unitree-sdk2-cpp-idl-hg-sportmodestate-fsm-id) | `int` | `int` | `AVAILABLE` |
| [`fsm_mode`](#unitree-sdk2-cpp-idl-hg-sportmodestate-fsm-mode) | `int` | `int` | `AVAILABLE` |
| [`task_id`](#unitree-sdk2-cpp-idl-hg-sportmodestate-task-id) | `int` | `int` | `AVAILABLE` |
| [`task_time`](#unitree-sdk2-cpp-idl-hg-sportmodestate-task-time) | `float` | `float` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-hg-sportmodestate-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.hg.SportModeState.__init__`

初始化 `SportModeState` 实例。是否能实际构造取决于下方可用性状态。

**签名**

```python
def __init__(self) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 无 | `None` | `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::SportModeState_`
- 签名：`SportModeState_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/hg/SportModeState_.hpp:29`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = SportModeState()
```

<a id="unitree-sdk2-cpp-idl-hg-sportmodestate-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.hg.SportModeState.__eq__`

按底层 IDL 消息内容比较两个对象是否相等。

**签名**

```python
def __eq__(self, other: object) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `other` | `object` | 必填 | 用于比较的另一个 Python 对象。类型不兼容时比较结果通常为 `False`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::SportModeState_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-hg-sportmodestate-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.hg.SportModeState.__ne__`

按底层 IDL 消息内容比较两个对象是否不相等。

**签名**

```python
def __ne__(self, other: object) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `other` | `object` | 必填 | 用于比较的另一个 Python 对象。类型不兼容时比较结果通常为 `False`。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::SportModeState_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-hg-sportmodestate-fsm-id"></a>
#### `unitree_sdk2_cpp.idl.hg.SportModeState.fsm_id`

底层 `unitree_hg::msg::dds_::SportModeState_` 的 `fsm_id` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

**签名**

```python
@property
def fsm_id(self) -> int

@fsm_id.setter
def fsm_id(self, value: int) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `int` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `int` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::SportModeState_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/hg/SportModeState_.hpp:23`

**用法**

```python
current_value = obj.fsm_id
obj.fsm_id = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-sportmodestate-fsm-mode"></a>
#### `unitree_sdk2_cpp.idl.hg.SportModeState.fsm_mode`

底层 `unitree_hg::msg::dds_::SportModeState_` 的 `fsm_mode` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

**签名**

```python
@property
def fsm_mode(self) -> int

@fsm_mode.setter
def fsm_mode(self, value: int) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `int` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `int` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::SportModeState_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/hg/SportModeState_.hpp:24`

**用法**

```python
current_value = obj.fsm_mode
obj.fsm_mode = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-sportmodestate-task-id"></a>
#### `unitree_sdk2_cpp.idl.hg.SportModeState.task_id`

底层 `unitree_hg::msg::dds_::SportModeState_` 的 `task_id` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

**签名**

```python
@property
def task_id(self) -> int

@task_id.setter
def task_id(self, value: int) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `int` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `int` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::SportModeState_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/hg/SportModeState_.hpp:25`

**用法**

```python
current_value = obj.task_id
obj.task_id = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-sportmodestate-task-time"></a>
#### `unitree_sdk2_cpp.idl.hg.SportModeState.task_time`

底层 `unitree_hg::msg::dds_::SportModeState_` 的 `task_time` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def task_time(self) -> float

@task_time.setter
def task_time(self, value: float) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `float` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `float` | 返回属性当前值。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::SportModeState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/hg/SportModeState_.hpp:26`

**用法**

```python
current_value = obj.task_time
obj.task_time = new_value
```

---

[返回 API 总索引](../API_REFERENCE_ZH.md)
