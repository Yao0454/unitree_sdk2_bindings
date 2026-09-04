# Unitree SDK2 Python API 参考分卷

[返回 API 总索引](../API_REFERENCE_ZH.md) · [阅读从零开始指南](../BEGINNER_GUIDE_ZH.md)

> [!WARNING]
> 本分卷同时包含 `AVAILABLE` 和 `SIGNATURE_ONLY`。后者只是设计期类型签名。运动及硬件副作用方法即使标记为 `AVAILABLE`，也不表示当前环境可安全执行。

> [!NOTE]
> 本文件由 `generator/generate_api_docs.py` 自动生成，请勿手工维护 API 条目。

---

<a id="unitree-sdk2-cpp-idl-hg-doubleimu"></a>
## HG Double-IMU IDL 消息

模块：`unitree_sdk2_cpp.idl.hg_doubleimu`

### 类索引

| 类 | 公开函数签名 | 属性 |
| --- | ---: | ---: |
| [`doubleIMUState`](#unitree-sdk2-cpp-idl-hg-doubleimu-doubleimustate) | 3 | 6 |

<a id="unitree-sdk2-cpp-idl-hg-doubleimu-doubleimustate"></a>
### `unitree_sdk2_cpp.idl.hg_doubleimu.doubleIMUState`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.hg_doubleimu import doubleIMUState
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-hg-doubleimu-doubleimustate-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-hg-doubleimu-doubleimustate-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-hg-doubleimu-doubleimustate-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`quaternion`](#unitree-sdk2-cpp-idl-hg-doubleimu-doubleimustate-quaternion) | `list[float]` | `Sequence[float]` | `AVAILABLE` |
| [`gyroscope`](#unitree-sdk2-cpp-idl-hg-doubleimu-doubleimustate-gyroscope) | `list[float]` | `Sequence[float]` | `AVAILABLE` |
| [`accelerometer`](#unitree-sdk2-cpp-idl-hg-doubleimu-doubleimustate-accelerometer) | `list[float]` | `Sequence[float]` | `AVAILABLE` |
| [`rpy`](#unitree-sdk2-cpp-idl-hg-doubleimu-doubleimustate-rpy) | `list[float]` | `Sequence[float]` | `AVAILABLE` |
| [`temperature`](#unitree-sdk2-cpp-idl-hg-doubleimu-doubleimustate-temperature) | `int` | `int` | `AVAILABLE` |
| [`tick`](#unitree-sdk2-cpp-idl-hg-doubleimu-doubleimustate-tick) | `int` | `int` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-hg-doubleimu-doubleimustate-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.hg_doubleimu.doubleIMUState.__init__`

初始化 `doubleIMUState` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree_hg_doubleimu::msg::dds_::doubleIMUState_`
- 签名：`doubleIMUState_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/hg_doubleimu/doubleIMUState_.hpp:32`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = doubleIMUState()
```

<a id="unitree-sdk2-cpp-idl-hg-doubleimu-doubleimustate-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.hg_doubleimu.doubleIMUState.__eq__`

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

- 类：`unitree_hg_doubleimu::msg::dds_::doubleIMUState_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-hg-doubleimu-doubleimustate-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.hg_doubleimu.doubleIMUState.__ne__`

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

- 类：`unitree_hg_doubleimu::msg::dds_::doubleIMUState_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-hg-doubleimu-doubleimustate-quaternion"></a>
#### `unitree_sdk2_cpp.idl.hg_doubleimu.doubleIMUState.quaternion`

底层 `unitree_hg_doubleimu::msg::dds_::doubleIMUState_` 的 `quaternion` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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

- 类：`unitree_hg_doubleimu::msg::dds_::doubleIMUState_`
- 字段类型：`std::array<float, 4>`
- 声明位置：`include/unitree/idl/hg_doubleimu/doubleIMUState_.hpp:24`

**用法**

```python
current_value = obj.quaternion
obj.quaternion = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-doubleimu-doubleimustate-gyroscope"></a>
#### `unitree_sdk2_cpp.idl.hg_doubleimu.doubleIMUState.gyroscope`

底层 `unitree_hg_doubleimu::msg::dds_::doubleIMUState_` 的 `gyroscope` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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

- 类：`unitree_hg_doubleimu::msg::dds_::doubleIMUState_`
- 字段类型：`std::array<float, 3>`
- 声明位置：`include/unitree/idl/hg_doubleimu/doubleIMUState_.hpp:25`

**用法**

```python
current_value = obj.gyroscope
obj.gyroscope = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-doubleimu-doubleimustate-accelerometer"></a>
#### `unitree_sdk2_cpp.idl.hg_doubleimu.doubleIMUState.accelerometer`

底层 `unitree_hg_doubleimu::msg::dds_::doubleIMUState_` 的 `accelerometer` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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

- 类：`unitree_hg_doubleimu::msg::dds_::doubleIMUState_`
- 字段类型：`std::array<float, 3>`
- 声明位置：`include/unitree/idl/hg_doubleimu/doubleIMUState_.hpp:26`

**用法**

```python
current_value = obj.accelerometer
obj.accelerometer = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-doubleimu-doubleimustate-rpy"></a>
#### `unitree_sdk2_cpp.idl.hg_doubleimu.doubleIMUState.rpy`

底层 `unitree_hg_doubleimu::msg::dds_::doubleIMUState_` 的 `rpy` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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

- 类：`unitree_hg_doubleimu::msg::dds_::doubleIMUState_`
- 字段类型：`std::array<float, 3>`
- 声明位置：`include/unitree/idl/hg_doubleimu/doubleIMUState_.hpp:27`

**用法**

```python
current_value = obj.rpy
obj.rpy = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-hg-doubleimu-doubleimustate-temperature"></a>
#### `unitree_sdk2_cpp.idl.hg_doubleimu.doubleIMUState.temperature`

底层 `unitree_hg_doubleimu::msg::dds_::doubleIMUState_` 的 `temperature` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 -32768 到 32767。

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

- 类：`unitree_hg_doubleimu::msg::dds_::doubleIMUState_`
- 字段类型：`int16_t`
- 声明位置：`include/unitree/idl/hg_doubleimu/doubleIMUState_.hpp:28`

**用法**

```python
current_value = obj.temperature
obj.temperature = new_value
```

<a id="unitree-sdk2-cpp-idl-hg-doubleimu-doubleimustate-tick"></a>
#### `unitree_sdk2_cpp.idl.hg_doubleimu.doubleIMUState.tick`

底层 `unitree_hg_doubleimu::msg::dds_::doubleIMUState_` 的 `tick` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

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

- 类：`unitree_hg_doubleimu::msg::dds_::doubleIMUState_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/hg_doubleimu/doubleIMUState_.hpp:29`

**用法**

```python
current_value = obj.tick
obj.tick = new_value
```

---

[返回 API 总索引](../API_REFERENCE_ZH.md)
