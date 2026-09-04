# Unitree SDK2 Python API 参考分卷

[返回 API 总索引](../API_REFERENCE_ZH.md) · [阅读从零开始指南](../BEGINNER_GUIDE_ZH.md)

> [!WARNING]
> 本分卷同时包含 `AVAILABLE` 和 `SIGNATURE_ONLY`。后者只是设计期类型签名。运动及硬件副作用方法即使标记为 `AVAILABLE`，也不表示当前环境可安全执行。

> [!NOTE]
> 本文件由 `generator/generate_api_docs.py` 自动生成，请勿手工维护 API 条目。

---

<a id="unitree-sdk2-cpp-idl-ros2"></a>
## ROS2 兼容 IDL 消息

模块：`unitree_sdk2_cpp.idl.ros2`

### 类索引

| 类 | 公开函数签名 | 属性 |
| --- | ---: | ---: |
| [`Time`](#unitree-sdk2-cpp-idl-ros2-time) | 3 | 2 |
| [`Header`](#unitree-sdk2-cpp-idl-ros2-header) | 3 | 2 |
| [`Quaternion`](#unitree-sdk2-cpp-idl-ros2-quaternion) | 3 | 4 |
| [`Vector3`](#unitree-sdk2-cpp-idl-ros2-vector3) | 3 | 3 |
| [`Imu`](#unitree-sdk2-cpp-idl-ros2-imu) | 3 | 7 |
| [`Point`](#unitree-sdk2-cpp-idl-ros2-point) | 3 | 3 |
| [`Pose`](#unitree-sdk2-cpp-idl-ros2-pose) | 3 | 2 |
| [`MapMetaData`](#unitree-sdk2-cpp-idl-ros2-mapmetadata) | 3 | 5 |
| [`OccupancyGrid`](#unitree-sdk2-cpp-idl-ros2-occupancygrid) | 3 | 3 |
| [`PoseWithCovariance`](#unitree-sdk2-cpp-idl-ros2-posewithcovariance) | 3 | 2 |
| [`Twist`](#unitree-sdk2-cpp-idl-ros2-twist) | 3 | 2 |
| [`TwistWithCovariance`](#unitree-sdk2-cpp-idl-ros2-twistwithcovariance) | 3 | 2 |
| [`Odometry`](#unitree-sdk2-cpp-idl-ros2-odometry) | 3 | 4 |
| [`Point32`](#unitree-sdk2-cpp-idl-ros2-point32) | 3 | 3 |
| [`PointField`](#unitree-sdk2-cpp-idl-ros2-pointfield) | 3 | 4 |
| [`PointCloud2`](#unitree-sdk2-cpp-idl-ros2-pointcloud2) | 3 | 9 |
| [`PointStamped`](#unitree-sdk2-cpp-idl-ros2-pointstamped) | 3 | 2 |
| [`Pose2D`](#unitree-sdk2-cpp-idl-ros2-pose2d) | 3 | 3 |
| [`PoseStamped`](#unitree-sdk2-cpp-idl-ros2-posestamped) | 3 | 2 |
| [`PoseWithCovarianceStamped`](#unitree-sdk2-cpp-idl-ros2-posewithcovariancestamped) | 3 | 2 |
| [`QuaternionStamped`](#unitree-sdk2-cpp-idl-ros2-quaternionstamped) | 3 | 2 |
| [`String`](#unitree-sdk2-cpp-idl-ros2-string) | 3 | 1 |
| [`TwistStamped`](#unitree-sdk2-cpp-idl-ros2-twiststamped) | 3 | 2 |
| [`TwistWithCovarianceStamped`](#unitree-sdk2-cpp-idl-ros2-twistwithcovariancestamped) | 3 | 2 |

<a id="unitree-sdk2-cpp-idl-ros2-time"></a>
### `unitree_sdk2_cpp.idl.ros2.Time`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.ros2 import Time
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-ros2-time-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-ros2-time-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-ros2-time-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`sec`](#unitree-sdk2-cpp-idl-ros2-time-sec) | `int` | `int` | `AVAILABLE` |
| [`nanosec`](#unitree-sdk2-cpp-idl-ros2-time-nanosec) | `int` | `int` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-ros2-time-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.Time.__init__`

初始化 `Time` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`builtin_interfaces::msg::dds_::Time_`
- 签名：`Time_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/ros2/Time_.hpp:27`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = Time()
```

<a id="unitree-sdk2-cpp-idl-ros2-time-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.Time.__eq__`

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

- 类：`builtin_interfaces::msg::dds_::Time_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-ros2-time-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.Time.__ne__`

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

- 类：`builtin_interfaces::msg::dds_::Time_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-ros2-time-sec"></a>
#### `unitree_sdk2_cpp.idl.ros2.Time.sec`

底层 `builtin_interfaces::msg::dds_::Time_` 的 `sec` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 -2147483648 到 2147483647。

**签名**

```python
@property
def sec(self) -> int

@sec.setter
def sec(self, value: int) -> None
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

- 类：`builtin_interfaces::msg::dds_::Time_`
- 字段类型：`int32_t`
- 声明位置：`include/unitree/idl/ros2/Time_.hpp:23`

**用法**

```python
current_value = obj.sec
obj.sec = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-time-nanosec"></a>
#### `unitree_sdk2_cpp.idl.ros2.Time.nanosec`

底层 `builtin_interfaces::msg::dds_::Time_` 的 `nanosec` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

**签名**

```python
@property
def nanosec(self) -> int

@nanosec.setter
def nanosec(self, value: int) -> None
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

- 类：`builtin_interfaces::msg::dds_::Time_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/ros2/Time_.hpp:24`

**用法**

```python
current_value = obj.nanosec
obj.nanosec = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-header"></a>
### `unitree_sdk2_cpp.idl.ros2.Header`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.ros2 import Header
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-ros2-header-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-ros2-header-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-ros2-header-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`stamp`](#unitree-sdk2-cpp-idl-ros2-header-stamp) | `Any` | `Any` | `AVAILABLE` |
| [`frame_id`](#unitree-sdk2-cpp-idl-ros2-header-frame-id) | `str` | `str` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-ros2-header-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.Header.__init__`

初始化 `Header` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`std_msgs::msg::dds_::Header_`
- 签名：`Header_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/ros2/Header_.hpp:29`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = Header()
```

<a id="unitree-sdk2-cpp-idl-ros2-header-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.Header.__eq__`

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

- 类：`std_msgs::msg::dds_::Header_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-ros2-header-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.Header.__ne__`

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

- 类：`std_msgs::msg::dds_::Header_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-ros2-header-stamp"></a>
#### `unitree_sdk2_cpp.idl.ros2.Header.stamp`

底层 `std_msgs::msg::dds_::Header_` 的 `stamp` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def stamp(self) -> Any

@stamp.setter
def stamp(self, value: Any) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Any` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `Any` | 返回属性当前值。 |

**对应 C++**

- 类：`std_msgs::msg::dds_::Header_`
- 字段类型：`::builtin_interfaces::msg::dds_::Time_`
- 声明位置：`include/unitree/idl/ros2/Header_.hpp:25`

**用法**

```python
current_value = obj.stamp
obj.stamp = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-header-frame-id"></a>
#### `unitree_sdk2_cpp.idl.ros2.Header.frame_id`

底层 `std_msgs::msg::dds_::Header_` 的 `frame_id` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

**签名**

```python
@property
def frame_id(self) -> str

@frame_id.setter
def frame_id(self, value: str) -> None
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

- 类：`std_msgs::msg::dds_::Header_`
- 字段类型：`std::string`
- 声明位置：`include/unitree/idl/ros2/Header_.hpp:26`

**用法**

```python
current_value = obj.frame_id
obj.frame_id = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-quaternion"></a>
### `unitree_sdk2_cpp.idl.ros2.Quaternion`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.ros2 import Quaternion
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-ros2-quaternion-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-ros2-quaternion-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-ros2-quaternion-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`x`](#unitree-sdk2-cpp-idl-ros2-quaternion-x) | `float` | `float` | `AVAILABLE` |
| [`y`](#unitree-sdk2-cpp-idl-ros2-quaternion-y) | `float` | `float` | `AVAILABLE` |
| [`z`](#unitree-sdk2-cpp-idl-ros2-quaternion-z) | `float` | `float` | `AVAILABLE` |
| [`w`](#unitree-sdk2-cpp-idl-ros2-quaternion-w) | `float` | `float` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-ros2-quaternion-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.Quaternion.__init__`

初始化 `Quaternion` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`geometry_msgs::msg::dds_::Quaternion_`
- 签名：`Quaternion_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/ros2/Quaternion_.hpp:28`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = Quaternion()
```

<a id="unitree-sdk2-cpp-idl-ros2-quaternion-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.Quaternion.__eq__`

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

- 类：`geometry_msgs::msg::dds_::Quaternion_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-ros2-quaternion-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.Quaternion.__ne__`

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

- 类：`geometry_msgs::msg::dds_::Quaternion_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-ros2-quaternion-x"></a>
#### `unitree_sdk2_cpp.idl.ros2.Quaternion.x`

底层 `geometry_msgs::msg::dds_::Quaternion_` 的 `x` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def x(self) -> float

@x.setter
def x(self, value: float) -> None
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

- 类：`geometry_msgs::msg::dds_::Quaternion_`
- 字段类型：`double`
- 声明位置：`include/unitree/idl/ros2/Quaternion_.hpp:22`

**用法**

```python
current_value = obj.x
obj.x = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-quaternion-y"></a>
#### `unitree_sdk2_cpp.idl.ros2.Quaternion.y`

底层 `geometry_msgs::msg::dds_::Quaternion_` 的 `y` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def y(self) -> float

@y.setter
def y(self, value: float) -> None
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

- 类：`geometry_msgs::msg::dds_::Quaternion_`
- 字段类型：`double`
- 声明位置：`include/unitree/idl/ros2/Quaternion_.hpp:23`

**用法**

```python
current_value = obj.y
obj.y = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-quaternion-z"></a>
#### `unitree_sdk2_cpp.idl.ros2.Quaternion.z`

底层 `geometry_msgs::msg::dds_::Quaternion_` 的 `z` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def z(self) -> float

@z.setter
def z(self, value: float) -> None
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

- 类：`geometry_msgs::msg::dds_::Quaternion_`
- 字段类型：`double`
- 声明位置：`include/unitree/idl/ros2/Quaternion_.hpp:24`

**用法**

```python
current_value = obj.z
obj.z = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-quaternion-w"></a>
#### `unitree_sdk2_cpp.idl.ros2.Quaternion.w`

底层 `geometry_msgs::msg::dds_::Quaternion_` 的 `w` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def w(self) -> float

@w.setter
def w(self, value: float) -> None
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

- 类：`geometry_msgs::msg::dds_::Quaternion_`
- 字段类型：`double`
- 声明位置：`include/unitree/idl/ros2/Quaternion_.hpp:25`

**用法**

```python
current_value = obj.w
obj.w = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-vector3"></a>
### `unitree_sdk2_cpp.idl.ros2.Vector3`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.ros2 import Vector3
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-ros2-vector3-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-ros2-vector3-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-ros2-vector3-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`x`](#unitree-sdk2-cpp-idl-ros2-vector3-x) | `float` | `float` | `AVAILABLE` |
| [`y`](#unitree-sdk2-cpp-idl-ros2-vector3-y) | `float` | `float` | `AVAILABLE` |
| [`z`](#unitree-sdk2-cpp-idl-ros2-vector3-z) | `float` | `float` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-ros2-vector3-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.Vector3.__init__`

初始化 `Vector3` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`geometry_msgs::msg::dds_::Vector3_`
- 签名：`Vector3_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/ros2/Vector3_.hpp:27`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = Vector3()
```

<a id="unitree-sdk2-cpp-idl-ros2-vector3-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.Vector3.__eq__`

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

- 类：`geometry_msgs::msg::dds_::Vector3_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-ros2-vector3-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.Vector3.__ne__`

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

- 类：`geometry_msgs::msg::dds_::Vector3_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-ros2-vector3-x"></a>
#### `unitree_sdk2_cpp.idl.ros2.Vector3.x`

底层 `geometry_msgs::msg::dds_::Vector3_` 的 `x` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def x(self) -> float

@x.setter
def x(self, value: float) -> None
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

- 类：`geometry_msgs::msg::dds_::Vector3_`
- 字段类型：`double`
- 声明位置：`include/unitree/idl/ros2/Vector3_.hpp:22`

**用法**

```python
current_value = obj.x
obj.x = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-vector3-y"></a>
#### `unitree_sdk2_cpp.idl.ros2.Vector3.y`

底层 `geometry_msgs::msg::dds_::Vector3_` 的 `y` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def y(self) -> float

@y.setter
def y(self, value: float) -> None
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

- 类：`geometry_msgs::msg::dds_::Vector3_`
- 字段类型：`double`
- 声明位置：`include/unitree/idl/ros2/Vector3_.hpp:23`

**用法**

```python
current_value = obj.y
obj.y = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-vector3-z"></a>
#### `unitree_sdk2_cpp.idl.ros2.Vector3.z`

底层 `geometry_msgs::msg::dds_::Vector3_` 的 `z` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def z(self) -> float

@z.setter
def z(self, value: float) -> None
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

- 类：`geometry_msgs::msg::dds_::Vector3_`
- 字段类型：`double`
- 声明位置：`include/unitree/idl/ros2/Vector3_.hpp:24`

**用法**

```python
current_value = obj.z
obj.z = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-imu"></a>
### `unitree_sdk2_cpp.idl.ros2.Imu`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.ros2 import Imu
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-ros2-imu-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-ros2-imu-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-ros2-imu-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`header`](#unitree-sdk2-cpp-idl-ros2-imu-header) | `Any` | `Any` | `AVAILABLE` |
| [`orientation`](#unitree-sdk2-cpp-idl-ros2-imu-orientation) | `Any` | `Any` | `AVAILABLE` |
| [`orientation_covariance`](#unitree-sdk2-cpp-idl-ros2-imu-orientation-covariance) | `list[float]` | `Sequence[float]` | `AVAILABLE` |
| [`angular_velocity`](#unitree-sdk2-cpp-idl-ros2-imu-angular-velocity) | `Any` | `Any` | `AVAILABLE` |
| [`angular_velocity_covariance`](#unitree-sdk2-cpp-idl-ros2-imu-angular-velocity-covariance) | `list[float]` | `Sequence[float]` | `AVAILABLE` |
| [`linear_acceleration`](#unitree-sdk2-cpp-idl-ros2-imu-linear-acceleration) | `Any` | `Any` | `AVAILABLE` |
| [`linear_acceleration_covariance`](#unitree-sdk2-cpp-idl-ros2-imu-linear-acceleration-covariance) | `list[float]` | `Sequence[float]` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-ros2-imu-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.Imu.__init__`

初始化 `Imu` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`sensor_msgs::msg::dds_::Imu_`
- 签名：`Imu_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/ros2/Imu_.hpp:38`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = Imu()
```

<a id="unitree-sdk2-cpp-idl-ros2-imu-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.Imu.__eq__`

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

- 类：`sensor_msgs::msg::dds_::Imu_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-ros2-imu-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.Imu.__ne__`

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

- 类：`sensor_msgs::msg::dds_::Imu_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-ros2-imu-header"></a>
#### `unitree_sdk2_cpp.idl.ros2.Imu.header`

底层 `sensor_msgs::msg::dds_::Imu_` 的 `header` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def header(self) -> Any

@header.setter
def header(self, value: Any) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Any` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `Any` | 返回属性当前值。 |

**对应 C++**

- 类：`sensor_msgs::msg::dds_::Imu_`
- 字段类型：`::std_msgs::msg::dds_::Header_`
- 声明位置：`include/unitree/idl/ros2/Imu_.hpp:29`

**用法**

```python
current_value = obj.header
obj.header = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-imu-orientation"></a>
#### `unitree_sdk2_cpp.idl.ros2.Imu.orientation`

底层 `sensor_msgs::msg::dds_::Imu_` 的 `orientation` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def orientation(self) -> Any

@orientation.setter
def orientation(self, value: Any) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Any` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `Any` | 返回属性当前值。 |

**对应 C++**

- 类：`sensor_msgs::msg::dds_::Imu_`
- 字段类型：`::geometry_msgs::msg::dds_::Quaternion_`
- 声明位置：`include/unitree/idl/ros2/Imu_.hpp:30`

**用法**

```python
current_value = obj.orientation
obj.orientation = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-imu-orientation-covariance"></a>
#### `unitree_sdk2_cpp.idl.ros2.Imu.orientation_covariance`

底层 `sensor_msgs::msg::dds_::Imu_` 的 `orientation_covariance` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 9 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def orientation_covariance(self) -> list[float]

@orientation_covariance.setter
def orientation_covariance(self, value: Sequence[float]) -> None
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

- 类：`sensor_msgs::msg::dds_::Imu_`
- 字段类型：`std::array<double, 9>`
- 声明位置：`include/unitree/idl/ros2/Imu_.hpp:31`

**用法**

```python
current_value = obj.orientation_covariance
obj.orientation_covariance = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-ros2-imu-angular-velocity"></a>
#### `unitree_sdk2_cpp.idl.ros2.Imu.angular_velocity`

底层 `sensor_msgs::msg::dds_::Imu_` 的 `angular_velocity` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def angular_velocity(self) -> Any

@angular_velocity.setter
def angular_velocity(self, value: Any) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Any` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `Any` | 返回属性当前值。 |

**对应 C++**

- 类：`sensor_msgs::msg::dds_::Imu_`
- 字段类型：`::geometry_msgs::msg::dds_::Vector3_`
- 声明位置：`include/unitree/idl/ros2/Imu_.hpp:32`

**用法**

```python
current_value = obj.angular_velocity
obj.angular_velocity = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-imu-angular-velocity-covariance"></a>
#### `unitree_sdk2_cpp.idl.ros2.Imu.angular_velocity_covariance`

底层 `sensor_msgs::msg::dds_::Imu_` 的 `angular_velocity_covariance` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 9 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def angular_velocity_covariance(self) -> list[float]

@angular_velocity_covariance.setter
def angular_velocity_covariance(self, value: Sequence[float]) -> None
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

- 类：`sensor_msgs::msg::dds_::Imu_`
- 字段类型：`std::array<double, 9>`
- 声明位置：`include/unitree/idl/ros2/Imu_.hpp:33`

**用法**

```python
current_value = obj.angular_velocity_covariance
obj.angular_velocity_covariance = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-ros2-imu-linear-acceleration"></a>
#### `unitree_sdk2_cpp.idl.ros2.Imu.linear_acceleration`

底层 `sensor_msgs::msg::dds_::Imu_` 的 `linear_acceleration` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def linear_acceleration(self) -> Any

@linear_acceleration.setter
def linear_acceleration(self, value: Any) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Any` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `Any` | 返回属性当前值。 |

**对应 C++**

- 类：`sensor_msgs::msg::dds_::Imu_`
- 字段类型：`::geometry_msgs::msg::dds_::Vector3_`
- 声明位置：`include/unitree/idl/ros2/Imu_.hpp:34`

**用法**

```python
current_value = obj.linear_acceleration
obj.linear_acceleration = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-imu-linear-acceleration-covariance"></a>
#### `unitree_sdk2_cpp.idl.ros2.Imu.linear_acceleration_covariance`

底层 `sensor_msgs::msg::dds_::Imu_` 的 `linear_acceleration_covariance` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 9 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def linear_acceleration_covariance(self) -> list[float]

@linear_acceleration_covariance.setter
def linear_acceleration_covariance(self, value: Sequence[float]) -> None
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

- 类：`sensor_msgs::msg::dds_::Imu_`
- 字段类型：`std::array<double, 9>`
- 声明位置：`include/unitree/idl/ros2/Imu_.hpp:35`

**用法**

```python
current_value = obj.linear_acceleration_covariance
obj.linear_acceleration_covariance = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-ros2-point"></a>
### `unitree_sdk2_cpp.idl.ros2.Point`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.ros2 import Point
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-ros2-point-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-ros2-point-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-ros2-point-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`x`](#unitree-sdk2-cpp-idl-ros2-point-x) | `float` | `float` | `AVAILABLE` |
| [`y`](#unitree-sdk2-cpp-idl-ros2-point-y) | `float` | `float` | `AVAILABLE` |
| [`z`](#unitree-sdk2-cpp-idl-ros2-point-z) | `float` | `float` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-ros2-point-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.Point.__init__`

初始化 `Point` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`geometry_msgs::msg::dds_::Point_`
- 签名：`Point_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/ros2/Point_.hpp:27`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = Point()
```

<a id="unitree-sdk2-cpp-idl-ros2-point-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.Point.__eq__`

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

- 类：`geometry_msgs::msg::dds_::Point_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-ros2-point-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.Point.__ne__`

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

- 类：`geometry_msgs::msg::dds_::Point_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-ros2-point-x"></a>
#### `unitree_sdk2_cpp.idl.ros2.Point.x`

底层 `geometry_msgs::msg::dds_::Point_` 的 `x` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def x(self) -> float

@x.setter
def x(self, value: float) -> None
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

- 类：`geometry_msgs::msg::dds_::Point_`
- 字段类型：`double`
- 声明位置：`include/unitree/idl/ros2/Point_.hpp:22`

**用法**

```python
current_value = obj.x
obj.x = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-point-y"></a>
#### `unitree_sdk2_cpp.idl.ros2.Point.y`

底层 `geometry_msgs::msg::dds_::Point_` 的 `y` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def y(self) -> float

@y.setter
def y(self, value: float) -> None
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

- 类：`geometry_msgs::msg::dds_::Point_`
- 字段类型：`double`
- 声明位置：`include/unitree/idl/ros2/Point_.hpp:23`

**用法**

```python
current_value = obj.y
obj.y = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-point-z"></a>
#### `unitree_sdk2_cpp.idl.ros2.Point.z`

底层 `geometry_msgs::msg::dds_::Point_` 的 `z` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def z(self) -> float

@z.setter
def z(self, value: float) -> None
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

- 类：`geometry_msgs::msg::dds_::Point_`
- 字段类型：`double`
- 声明位置：`include/unitree/idl/ros2/Point_.hpp:24`

**用法**

```python
current_value = obj.z
obj.z = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-pose"></a>
### `unitree_sdk2_cpp.idl.ros2.Pose`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.ros2 import Pose
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-ros2-pose-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-ros2-pose-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-ros2-pose-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`position`](#unitree-sdk2-cpp-idl-ros2-pose-position) | `Point` | `Point` | `AVAILABLE` |
| [`orientation`](#unitree-sdk2-cpp-idl-ros2-pose-orientation) | `Quaternion` | `Quaternion` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-ros2-pose-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.Pose.__init__`

初始化 `Pose` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`geometry_msgs::msg::dds_::Pose_`
- 签名：`Pose_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/ros2/Pose_.hpp:30`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = Pose()
```

<a id="unitree-sdk2-cpp-idl-ros2-pose-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.Pose.__eq__`

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

- 类：`geometry_msgs::msg::dds_::Pose_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-ros2-pose-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.Pose.__ne__`

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

- 类：`geometry_msgs::msg::dds_::Pose_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-ros2-pose-position"></a>
#### `unitree_sdk2_cpp.idl.ros2.Pose.position`

底层 `geometry_msgs::msg::dds_::Pose_` 的 `position` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def position(self) -> Point

@position.setter
def position(self, value: Point) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Point` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `Point` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`geometry_msgs::msg::dds_::Pose_`
- 字段类型：`::geometry_msgs::msg::dds_::Point_`
- 声明位置：`include/unitree/idl/ros2/Pose_.hpp:26`

**用法**

```python
current_value = obj.position
obj.position = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-pose-orientation"></a>
#### `unitree_sdk2_cpp.idl.ros2.Pose.orientation`

底层 `geometry_msgs::msg::dds_::Pose_` 的 `orientation` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def orientation(self) -> Quaternion

@orientation.setter
def orientation(self, value: Quaternion) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Quaternion` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `Quaternion` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`geometry_msgs::msg::dds_::Pose_`
- 字段类型：`::geometry_msgs::msg::dds_::Quaternion_`
- 声明位置：`include/unitree/idl/ros2/Pose_.hpp:27`

**用法**

```python
current_value = obj.orientation
obj.orientation = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-mapmetadata"></a>
### `unitree_sdk2_cpp.idl.ros2.MapMetaData`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.ros2 import MapMetaData
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-ros2-mapmetadata-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-ros2-mapmetadata-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-ros2-mapmetadata-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`map_load_time`](#unitree-sdk2-cpp-idl-ros2-mapmetadata-map-load-time) | `Any` | `Any` | `AVAILABLE` |
| [`resolution`](#unitree-sdk2-cpp-idl-ros2-mapmetadata-resolution) | `float` | `float` | `AVAILABLE` |
| [`width`](#unitree-sdk2-cpp-idl-ros2-mapmetadata-width) | `int` | `int` | `AVAILABLE` |
| [`height`](#unitree-sdk2-cpp-idl-ros2-mapmetadata-height) | `int` | `int` | `AVAILABLE` |
| [`origin`](#unitree-sdk2-cpp-idl-ros2-mapmetadata-origin) | `Any` | `Any` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-ros2-mapmetadata-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.MapMetaData.__init__`

初始化 `MapMetaData` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`nav_msgs::msg::dds_::MapMetaData_`
- 签名：`MapMetaData_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/ros2/MapMetaData_.hpp:34`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = MapMetaData()
```

<a id="unitree-sdk2-cpp-idl-ros2-mapmetadata-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.MapMetaData.__eq__`

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

- 类：`nav_msgs::msg::dds_::MapMetaData_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-ros2-mapmetadata-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.MapMetaData.__ne__`

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

- 类：`nav_msgs::msg::dds_::MapMetaData_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-ros2-mapmetadata-map-load-time"></a>
#### `unitree_sdk2_cpp.idl.ros2.MapMetaData.map_load_time`

底层 `nav_msgs::msg::dds_::MapMetaData_` 的 `map_load_time` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def map_load_time(self) -> Any

@map_load_time.setter
def map_load_time(self, value: Any) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Any` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `Any` | 返回属性当前值。 |

**对应 C++**

- 类：`nav_msgs::msg::dds_::MapMetaData_`
- 字段类型：`::builtin_interfaces::msg::dds_::Time_`
- 声明位置：`include/unitree/idl/ros2/MapMetaData_.hpp:27`

**用法**

```python
current_value = obj.map_load_time
obj.map_load_time = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-mapmetadata-resolution"></a>
#### `unitree_sdk2_cpp.idl.ros2.MapMetaData.resolution`

底层 `nav_msgs::msg::dds_::MapMetaData_` 的 `resolution` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def resolution(self) -> float

@resolution.setter
def resolution(self, value: float) -> None
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

- 类：`nav_msgs::msg::dds_::MapMetaData_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/ros2/MapMetaData_.hpp:28`

**用法**

```python
current_value = obj.resolution
obj.resolution = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-mapmetadata-width"></a>
#### `unitree_sdk2_cpp.idl.ros2.MapMetaData.width`

底层 `nav_msgs::msg::dds_::MapMetaData_` 的 `width` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

**签名**

```python
@property
def width(self) -> int

@width.setter
def width(self, value: int) -> None
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

- 类：`nav_msgs::msg::dds_::MapMetaData_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/ros2/MapMetaData_.hpp:29`

**用法**

```python
current_value = obj.width
obj.width = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-mapmetadata-height"></a>
#### `unitree_sdk2_cpp.idl.ros2.MapMetaData.height`

底层 `nav_msgs::msg::dds_::MapMetaData_` 的 `height` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

**签名**

```python
@property
def height(self) -> int

@height.setter
def height(self, value: int) -> None
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

- 类：`nav_msgs::msg::dds_::MapMetaData_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/ros2/MapMetaData_.hpp:30`

**用法**

```python
current_value = obj.height
obj.height = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-mapmetadata-origin"></a>
#### `unitree_sdk2_cpp.idl.ros2.MapMetaData.origin`

底层 `nav_msgs::msg::dds_::MapMetaData_` 的 `origin` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def origin(self) -> Any

@origin.setter
def origin(self, value: Any) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Any` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `Any` | 返回属性当前值。 |

**对应 C++**

- 类：`nav_msgs::msg::dds_::MapMetaData_`
- 字段类型：`::geometry_msgs::msg::dds_::Pose_`
- 声明位置：`include/unitree/idl/ros2/MapMetaData_.hpp:31`

**用法**

```python
current_value = obj.origin
obj.origin = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-occupancygrid"></a>
### `unitree_sdk2_cpp.idl.ros2.OccupancyGrid`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.ros2 import OccupancyGrid
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-ros2-occupancygrid-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-ros2-occupancygrid-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-ros2-occupancygrid-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`header`](#unitree-sdk2-cpp-idl-ros2-occupancygrid-header) | `Any` | `Any` | `AVAILABLE` |
| [`info`](#unitree-sdk2-cpp-idl-ros2-occupancygrid-info) | `MapMetaData` | `MapMetaData` | `AVAILABLE` |
| [`data`](#unitree-sdk2-cpp-idl-ros2-occupancygrid-data) | `list[int]` | `Sequence[int]` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-ros2-occupancygrid-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.OccupancyGrid.__init__`

初始化 `OccupancyGrid` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`nav_msgs::msg::dds_::OccupancyGrid_`
- 签名：`OccupancyGrid_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/ros2/OccupancyGrid_.hpp:33`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = OccupancyGrid()
```

<a id="unitree-sdk2-cpp-idl-ros2-occupancygrid-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.OccupancyGrid.__eq__`

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

- 类：`nav_msgs::msg::dds_::OccupancyGrid_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-ros2-occupancygrid-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.OccupancyGrid.__ne__`

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

- 类：`nav_msgs::msg::dds_::OccupancyGrid_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-ros2-occupancygrid-header"></a>
#### `unitree_sdk2_cpp.idl.ros2.OccupancyGrid.header`

底层 `nav_msgs::msg::dds_::OccupancyGrid_` 的 `header` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def header(self) -> Any

@header.setter
def header(self, value: Any) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Any` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `Any` | 返回属性当前值。 |

**对应 C++**

- 类：`nav_msgs::msg::dds_::OccupancyGrid_`
- 字段类型：`::std_msgs::msg::dds_::Header_`
- 声明位置：`include/unitree/idl/ros2/OccupancyGrid_.hpp:28`

**用法**

```python
current_value = obj.header
obj.header = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-occupancygrid-info"></a>
#### `unitree_sdk2_cpp.idl.ros2.OccupancyGrid.info`

底层 `nav_msgs::msg::dds_::OccupancyGrid_` 的 `info` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def info(self) -> MapMetaData

@info.setter
def info(self, value: MapMetaData) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `MapMetaData` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `MapMetaData` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`nav_msgs::msg::dds_::OccupancyGrid_`
- 字段类型：`::nav_msgs::msg::dds_::MapMetaData_`
- 声明位置：`include/unitree/idl/ros2/OccupancyGrid_.hpp:29`

**用法**

```python
current_value = obj.info
obj.info = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-occupancygrid-data"></a>
#### `unitree_sdk2_cpp.idl.ros2.OccupancyGrid.data`

底层 `nav_msgs::msg::dds_::OccupancyGrid_` 的 `data` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector；元素约束：取值范围为 0 到 255。

**签名**

```python
@property
def data(self) -> list[int]

@data.setter
def data(self, value: Sequence[int]) -> None
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

- 类：`nav_msgs::msg::dds_::OccupancyGrid_`
- 字段类型：`std::vector<uint8_t>`
- 声明位置：`include/unitree/idl/ros2/OccupancyGrid_.hpp:30`

**用法**

```python
current_value = obj.data
obj.data = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-ros2-posewithcovariance"></a>
### `unitree_sdk2_cpp.idl.ros2.PoseWithCovariance`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.ros2 import PoseWithCovariance
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-ros2-posewithcovariance-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-ros2-posewithcovariance-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-ros2-posewithcovariance-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`pose`](#unitree-sdk2-cpp-idl-ros2-posewithcovariance-pose) | `Pose` | `Pose` | `AVAILABLE` |
| [`covariance`](#unitree-sdk2-cpp-idl-ros2-posewithcovariance-covariance) | `list[float]` | `Sequence[float]` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-ros2-posewithcovariance-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.PoseWithCovariance.__init__`

初始化 `PoseWithCovariance` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`geometry_msgs::msg::dds_::PoseWithCovariance_`
- 签名：`PoseWithCovariance_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/ros2/PoseWithCovariance_.hpp:29`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = PoseWithCovariance()
```

<a id="unitree-sdk2-cpp-idl-ros2-posewithcovariance-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.PoseWithCovariance.__eq__`

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

- 类：`geometry_msgs::msg::dds_::PoseWithCovariance_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-ros2-posewithcovariance-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.PoseWithCovariance.__ne__`

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

- 类：`geometry_msgs::msg::dds_::PoseWithCovariance_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-ros2-posewithcovariance-pose"></a>
#### `unitree_sdk2_cpp.idl.ros2.PoseWithCovariance.pose`

底层 `geometry_msgs::msg::dds_::PoseWithCovariance_` 的 `pose` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def pose(self) -> Pose

@pose.setter
def pose(self, value: Pose) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Pose` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `Pose` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`geometry_msgs::msg::dds_::PoseWithCovariance_`
- 字段类型：`::geometry_msgs::msg::dds_::Pose_`
- 声明位置：`include/unitree/idl/ros2/PoseWithCovariance_.hpp:25`

**用法**

```python
current_value = obj.pose
obj.pose = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-posewithcovariance-covariance"></a>
#### `unitree_sdk2_cpp.idl.ros2.PoseWithCovariance.covariance`

底层 `geometry_msgs::msg::dds_::PoseWithCovariance_` 的 `covariance` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 36 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def covariance(self) -> list[float]

@covariance.setter
def covariance(self, value: Sequence[float]) -> None
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

- 类：`geometry_msgs::msg::dds_::PoseWithCovariance_`
- 字段类型：`std::array<double, 36>`
- 声明位置：`include/unitree/idl/ros2/PoseWithCovariance_.hpp:26`

**用法**

```python
current_value = obj.covariance
obj.covariance = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-ros2-twist"></a>
### `unitree_sdk2_cpp.idl.ros2.Twist`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.ros2 import Twist
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-ros2-twist-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-ros2-twist-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-ros2-twist-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`linear`](#unitree-sdk2-cpp-idl-ros2-twist-linear) | `Vector3` | `Vector3` | `AVAILABLE` |
| [`angular`](#unitree-sdk2-cpp-idl-ros2-twist-angular) | `Vector3` | `Vector3` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-ros2-twist-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.Twist.__init__`

初始化 `Twist` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`geometry_msgs::msg::dds_::Twist_`
- 签名：`Twist_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/ros2/Twist_.hpp:28`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = Twist()
```

<a id="unitree-sdk2-cpp-idl-ros2-twist-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.Twist.__eq__`

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

- 类：`geometry_msgs::msg::dds_::Twist_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-ros2-twist-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.Twist.__ne__`

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

- 类：`geometry_msgs::msg::dds_::Twist_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-ros2-twist-linear"></a>
#### `unitree_sdk2_cpp.idl.ros2.Twist.linear`

底层 `geometry_msgs::msg::dds_::Twist_` 的 `linear` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def linear(self) -> Vector3

@linear.setter
def linear(self, value: Vector3) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Vector3` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `Vector3` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`geometry_msgs::msg::dds_::Twist_`
- 字段类型：`::geometry_msgs::msg::dds_::Vector3_`
- 声明位置：`include/unitree/idl/ros2/Twist_.hpp:24`

**用法**

```python
current_value = obj.linear
obj.linear = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-twist-angular"></a>
#### `unitree_sdk2_cpp.idl.ros2.Twist.angular`

底层 `geometry_msgs::msg::dds_::Twist_` 的 `angular` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def angular(self) -> Vector3

@angular.setter
def angular(self, value: Vector3) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Vector3` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `Vector3` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`geometry_msgs::msg::dds_::Twist_`
- 字段类型：`::geometry_msgs::msg::dds_::Vector3_`
- 声明位置：`include/unitree/idl/ros2/Twist_.hpp:25`

**用法**

```python
current_value = obj.angular
obj.angular = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-twistwithcovariance"></a>
### `unitree_sdk2_cpp.idl.ros2.TwistWithCovariance`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.ros2 import TwistWithCovariance
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-ros2-twistwithcovariance-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-ros2-twistwithcovariance-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-ros2-twistwithcovariance-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`twist`](#unitree-sdk2-cpp-idl-ros2-twistwithcovariance-twist) | `Twist` | `Twist` | `AVAILABLE` |
| [`covariance`](#unitree-sdk2-cpp-idl-ros2-twistwithcovariance-covariance) | `list[float]` | `Sequence[float]` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-ros2-twistwithcovariance-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.TwistWithCovariance.__init__`

初始化 `TwistWithCovariance` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`geometry_msgs::msg::dds_::TwistWithCovariance_`
- 签名：`TwistWithCovariance_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/ros2/TwistWithCovariance_.hpp:29`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = TwistWithCovariance()
```

<a id="unitree-sdk2-cpp-idl-ros2-twistwithcovariance-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.TwistWithCovariance.__eq__`

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

- 类：`geometry_msgs::msg::dds_::TwistWithCovariance_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-ros2-twistwithcovariance-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.TwistWithCovariance.__ne__`

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

- 类：`geometry_msgs::msg::dds_::TwistWithCovariance_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-ros2-twistwithcovariance-twist"></a>
#### `unitree_sdk2_cpp.idl.ros2.TwistWithCovariance.twist`

底层 `geometry_msgs::msg::dds_::TwistWithCovariance_` 的 `twist` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def twist(self) -> Twist

@twist.setter
def twist(self, value: Twist) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Twist` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `Twist` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`geometry_msgs::msg::dds_::TwistWithCovariance_`
- 字段类型：`::geometry_msgs::msg::dds_::Twist_`
- 声明位置：`include/unitree/idl/ros2/TwistWithCovariance_.hpp:25`

**用法**

```python
current_value = obj.twist
obj.twist = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-twistwithcovariance-covariance"></a>
#### `unitree_sdk2_cpp.idl.ros2.TwistWithCovariance.covariance`

底层 `geometry_msgs::msg::dds_::TwistWithCovariance_` 的 `covariance` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 36 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def covariance(self) -> list[float]

@covariance.setter
def covariance(self, value: Sequence[float]) -> None
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

- 类：`geometry_msgs::msg::dds_::TwistWithCovariance_`
- 字段类型：`std::array<double, 36>`
- 声明位置：`include/unitree/idl/ros2/TwistWithCovariance_.hpp:26`

**用法**

```python
current_value = obj.covariance
obj.covariance = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-ros2-odometry"></a>
### `unitree_sdk2_cpp.idl.ros2.Odometry`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.ros2 import Odometry
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-ros2-odometry-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-ros2-odometry-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-ros2-odometry-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`header`](#unitree-sdk2-cpp-idl-ros2-odometry-header) | `Any` | `Any` | `AVAILABLE` |
| [`child_frame_id`](#unitree-sdk2-cpp-idl-ros2-odometry-child-frame-id) | `str` | `str` | `AVAILABLE` |
| [`pose`](#unitree-sdk2-cpp-idl-ros2-odometry-pose) | `Any` | `Any` | `AVAILABLE` |
| [`twist`](#unitree-sdk2-cpp-idl-ros2-odometry-twist) | `Any` | `Any` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-ros2-odometry-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.Odometry.__init__`

初始化 `Odometry` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`nav_msgs::msg::dds_::Odometry_`
- 签名：`Odometry_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/ros2/Odometry_.hpp:35`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = Odometry()
```

<a id="unitree-sdk2-cpp-idl-ros2-odometry-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.Odometry.__eq__`

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

- 类：`nav_msgs::msg::dds_::Odometry_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-ros2-odometry-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.Odometry.__ne__`

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

- 类：`nav_msgs::msg::dds_::Odometry_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-ros2-odometry-header"></a>
#### `unitree_sdk2_cpp.idl.ros2.Odometry.header`

底层 `nav_msgs::msg::dds_::Odometry_` 的 `header` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def header(self) -> Any

@header.setter
def header(self, value: Any) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Any` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `Any` | 返回属性当前值。 |

**对应 C++**

- 类：`nav_msgs::msg::dds_::Odometry_`
- 字段类型：`::std_msgs::msg::dds_::Header_`
- 声明位置：`include/unitree/idl/ros2/Odometry_.hpp:29`

**用法**

```python
current_value = obj.header
obj.header = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-odometry-child-frame-id"></a>
#### `unitree_sdk2_cpp.idl.ros2.Odometry.child_frame_id`

底层 `nav_msgs::msg::dds_::Odometry_` 的 `child_frame_id` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

**签名**

```python
@property
def child_frame_id(self) -> str

@child_frame_id.setter
def child_frame_id(self, value: str) -> None
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

- 类：`nav_msgs::msg::dds_::Odometry_`
- 字段类型：`std::string`
- 声明位置：`include/unitree/idl/ros2/Odometry_.hpp:30`

**用法**

```python
current_value = obj.child_frame_id
obj.child_frame_id = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-odometry-pose"></a>
#### `unitree_sdk2_cpp.idl.ros2.Odometry.pose`

底层 `nav_msgs::msg::dds_::Odometry_` 的 `pose` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def pose(self) -> Any

@pose.setter
def pose(self, value: Any) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Any` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `Any` | 返回属性当前值。 |

**对应 C++**

- 类：`nav_msgs::msg::dds_::Odometry_`
- 字段类型：`::geometry_msgs::msg::dds_::PoseWithCovariance_`
- 声明位置：`include/unitree/idl/ros2/Odometry_.hpp:31`

**用法**

```python
current_value = obj.pose
obj.pose = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-odometry-twist"></a>
#### `unitree_sdk2_cpp.idl.ros2.Odometry.twist`

底层 `nav_msgs::msg::dds_::Odometry_` 的 `twist` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def twist(self) -> Any

@twist.setter
def twist(self, value: Any) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Any` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `Any` | 返回属性当前值。 |

**对应 C++**

- 类：`nav_msgs::msg::dds_::Odometry_`
- 字段类型：`::geometry_msgs::msg::dds_::TwistWithCovariance_`
- 声明位置：`include/unitree/idl/ros2/Odometry_.hpp:32`

**用法**

```python
current_value = obj.twist
obj.twist = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-point32"></a>
### `unitree_sdk2_cpp.idl.ros2.Point32`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.ros2 import Point32
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-ros2-point32-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-ros2-point32-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-ros2-point32-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`x`](#unitree-sdk2-cpp-idl-ros2-point32-x) | `float` | `float` | `AVAILABLE` |
| [`y`](#unitree-sdk2-cpp-idl-ros2-point32-y) | `float` | `float` | `AVAILABLE` |
| [`z`](#unitree-sdk2-cpp-idl-ros2-point32-z) | `float` | `float` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-ros2-point32-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.Point32.__init__`

初始化 `Point32` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`geometry_msgs::msg::dds_::Point32_`
- 签名：`Point32_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/ros2/Point32_.hpp:27`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = Point32()
```

<a id="unitree-sdk2-cpp-idl-ros2-point32-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.Point32.__eq__`

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

- 类：`geometry_msgs::msg::dds_::Point32_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-ros2-point32-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.Point32.__ne__`

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

- 类：`geometry_msgs::msg::dds_::Point32_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-ros2-point32-x"></a>
#### `unitree_sdk2_cpp.idl.ros2.Point32.x`

底层 `geometry_msgs::msg::dds_::Point32_` 的 `x` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def x(self) -> float

@x.setter
def x(self, value: float) -> None
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

- 类：`geometry_msgs::msg::dds_::Point32_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/ros2/Point32_.hpp:22`

**用法**

```python
current_value = obj.x
obj.x = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-point32-y"></a>
#### `unitree_sdk2_cpp.idl.ros2.Point32.y`

底层 `geometry_msgs::msg::dds_::Point32_` 的 `y` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def y(self) -> float

@y.setter
def y(self, value: float) -> None
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

- 类：`geometry_msgs::msg::dds_::Point32_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/ros2/Point32_.hpp:23`

**用法**

```python
current_value = obj.y
obj.y = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-point32-z"></a>
#### `unitree_sdk2_cpp.idl.ros2.Point32.z`

底层 `geometry_msgs::msg::dds_::Point32_` 的 `z` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def z(self) -> float

@z.setter
def z(self, value: float) -> None
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

- 类：`geometry_msgs::msg::dds_::Point32_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/ros2/Point32_.hpp:24`

**用法**

```python
current_value = obj.z
obj.z = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-pointfield"></a>
### `unitree_sdk2_cpp.idl.ros2.PointField`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.ros2 import PointField
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-ros2-pointfield-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-ros2-pointfield-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-ros2-pointfield-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`name`](#unitree-sdk2-cpp-idl-ros2-pointfield-name) | `str` | `str` | `AVAILABLE` |
| [`offset`](#unitree-sdk2-cpp-idl-ros2-pointfield-offset) | `int` | `int` | `AVAILABLE` |
| [`datatype`](#unitree-sdk2-cpp-idl-ros2-pointfield-datatype) | `int` | `int` | `AVAILABLE` |
| [`count`](#unitree-sdk2-cpp-idl-ros2-pointfield-count) | `int` | `int` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-ros2-pointfield-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.PointField.__init__`

初始化 `PointField` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`sensor_msgs::msg::dds_::PointField_`
- 签名：`PointField_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/ros2/PointField_.hpp:50`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = PointField()
```

<a id="unitree-sdk2-cpp-idl-ros2-pointfield-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.PointField.__eq__`

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

- 类：`sensor_msgs::msg::dds_::PointField_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-ros2-pointfield-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.PointField.__ne__`

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

- 类：`sensor_msgs::msg::dds_::PointField_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-ros2-pointfield-name"></a>
#### `unitree_sdk2_cpp.idl.ros2.PointField.name`

底层 `sensor_msgs::msg::dds_::PointField_` 的 `name` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

**签名**

```python
@property
def name(self) -> str

@name.setter
def name(self, value: str) -> None
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

- 类：`sensor_msgs::msg::dds_::PointField_`
- 字段类型：`std::string`
- 声明位置：`include/unitree/idl/ros2/PointField_.hpp:44`

**用法**

```python
current_value = obj.name
obj.name = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-pointfield-offset"></a>
#### `unitree_sdk2_cpp.idl.ros2.PointField.offset`

底层 `sensor_msgs::msg::dds_::PointField_` 的 `offset` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

**签名**

```python
@property
def offset(self) -> int

@offset.setter
def offset(self, value: int) -> None
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

- 类：`sensor_msgs::msg::dds_::PointField_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/ros2/PointField_.hpp:45`

**用法**

```python
current_value = obj.offset
obj.offset = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-pointfield-datatype"></a>
#### `unitree_sdk2_cpp.idl.ros2.PointField.datatype`

底层 `sensor_msgs::msg::dds_::PointField_` 的 `datatype` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def datatype(self) -> int

@datatype.setter
def datatype(self, value: int) -> None
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

- 类：`sensor_msgs::msg::dds_::PointField_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/ros2/PointField_.hpp:46`

**用法**

```python
current_value = obj.datatype
obj.datatype = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-pointfield-count"></a>
#### `unitree_sdk2_cpp.idl.ros2.PointField.count`

底层 `sensor_msgs::msg::dds_::PointField_` 的 `count` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

**签名**

```python
@property
def count(self) -> int

@count.setter
def count(self, value: int) -> None
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

- 类：`sensor_msgs::msg::dds_::PointField_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/ros2/PointField_.hpp:47`

**用法**

```python
current_value = obj.count
obj.count = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-pointcloud2"></a>
### `unitree_sdk2_cpp.idl.ros2.PointCloud2`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.ros2 import PointCloud2
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-ros2-pointcloud2-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-ros2-pointcloud2-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-ros2-pointcloud2-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`header`](#unitree-sdk2-cpp-idl-ros2-pointcloud2-header) | `Any` | `Any` | `AVAILABLE` |
| [`height`](#unitree-sdk2-cpp-idl-ros2-pointcloud2-height) | `int` | `int` | `AVAILABLE` |
| [`width`](#unitree-sdk2-cpp-idl-ros2-pointcloud2-width) | `int` | `int` | `AVAILABLE` |
| [`fields`](#unitree-sdk2-cpp-idl-ros2-pointcloud2-fields) | `list[PointField]` | `Sequence[PointField]` | `AVAILABLE` |
| [`is_bigendian`](#unitree-sdk2-cpp-idl-ros2-pointcloud2-is-bigendian) | `bool` | `bool` | `AVAILABLE` |
| [`point_step`](#unitree-sdk2-cpp-idl-ros2-pointcloud2-point-step) | `int` | `int` | `AVAILABLE` |
| [`row_step`](#unitree-sdk2-cpp-idl-ros2-pointcloud2-row-step) | `int` | `int` | `AVAILABLE` |
| [`data`](#unitree-sdk2-cpp-idl-ros2-pointcloud2-data) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`is_dense`](#unitree-sdk2-cpp-idl-ros2-pointcloud2-is-dense) | `bool` | `bool` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-ros2-pointcloud2-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.PointCloud2.__init__`

初始化 `PointCloud2` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`sensor_msgs::msg::dds_::PointCloud2_`
- 签名：`PointCloud2_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/ros2/PointCloud2_.hpp:39`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = PointCloud2()
```

<a id="unitree-sdk2-cpp-idl-ros2-pointcloud2-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.PointCloud2.__eq__`

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

- 类：`sensor_msgs::msg::dds_::PointCloud2_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-ros2-pointcloud2-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.PointCloud2.__ne__`

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

- 类：`sensor_msgs::msg::dds_::PointCloud2_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-ros2-pointcloud2-header"></a>
#### `unitree_sdk2_cpp.idl.ros2.PointCloud2.header`

底层 `sensor_msgs::msg::dds_::PointCloud2_` 的 `header` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def header(self) -> Any

@header.setter
def header(self, value: Any) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Any` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `Any` | 返回属性当前值。 |

**对应 C++**

- 类：`sensor_msgs::msg::dds_::PointCloud2_`
- 字段类型：`::std_msgs::msg::dds_::Header_`
- 声明位置：`include/unitree/idl/ros2/PointCloud2_.hpp:28`

**用法**

```python
current_value = obj.header
obj.header = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-pointcloud2-height"></a>
#### `unitree_sdk2_cpp.idl.ros2.PointCloud2.height`

底层 `sensor_msgs::msg::dds_::PointCloud2_` 的 `height` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

**签名**

```python
@property
def height(self) -> int

@height.setter
def height(self, value: int) -> None
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

- 类：`sensor_msgs::msg::dds_::PointCloud2_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/ros2/PointCloud2_.hpp:29`

**用法**

```python
current_value = obj.height
obj.height = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-pointcloud2-width"></a>
#### `unitree_sdk2_cpp.idl.ros2.PointCloud2.width`

底层 `sensor_msgs::msg::dds_::PointCloud2_` 的 `width` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

**签名**

```python
@property
def width(self) -> int

@width.setter
def width(self, value: int) -> None
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

- 类：`sensor_msgs::msg::dds_::PointCloud2_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/ros2/PointCloud2_.hpp:30`

**用法**

```python
current_value = obj.width
obj.width = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-pointcloud2-fields"></a>
#### `unitree_sdk2_cpp.idl.ros2.PointCloud2.fields`

底层 `sensor_msgs::msg::dds_::PointCloud2_` 的 `fields` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector

**签名**

```python
@property
def fields(self) -> list[PointField]

@fields.setter
def fields(self, value: Sequence[PointField]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[PointField]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[PointField]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`sensor_msgs::msg::dds_::PointCloud2_`
- 字段类型：`std::vector< ::sensor_msgs::msg::dds_::PointField_>`
- 声明位置：`include/unitree/idl/ros2/PointCloud2_.hpp:31`

**用法**

```python
current_value = obj.fields
obj.fields = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-ros2-pointcloud2-is-bigendian"></a>
#### `unitree_sdk2_cpp.idl.ros2.PointCloud2.is_bigendian`

底层 `sensor_msgs::msg::dds_::PointCloud2_` 的 `is_bigendian` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 只接受布尔语义。

**签名**

```python
@property
def is_bigendian(self) -> bool

@is_bigendian.setter
def is_bigendian(self, value: bool) -> None
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

- 类：`sensor_msgs::msg::dds_::PointCloud2_`
- 字段类型：`bool`
- 声明位置：`include/unitree/idl/ros2/PointCloud2_.hpp:32`

**用法**

```python
current_value = obj.is_bigendian
obj.is_bigendian = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-pointcloud2-point-step"></a>
#### `unitree_sdk2_cpp.idl.ros2.PointCloud2.point_step`

底层 `sensor_msgs::msg::dds_::PointCloud2_` 的 `point_step` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

**签名**

```python
@property
def point_step(self) -> int

@point_step.setter
def point_step(self, value: int) -> None
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

- 类：`sensor_msgs::msg::dds_::PointCloud2_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/ros2/PointCloud2_.hpp:33`

**用法**

```python
current_value = obj.point_step
obj.point_step = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-pointcloud2-row-step"></a>
#### `unitree_sdk2_cpp.idl.ros2.PointCloud2.row_step`

底层 `sensor_msgs::msg::dds_::PointCloud2_` 的 `row_step` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

**签名**

```python
@property
def row_step(self) -> int

@row_step.setter
def row_step(self, value: int) -> None
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

- 类：`sensor_msgs::msg::dds_::PointCloud2_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/ros2/PointCloud2_.hpp:34`

**用法**

```python
current_value = obj.row_step
obj.row_step = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-pointcloud2-data"></a>
#### `unitree_sdk2_cpp.idl.ros2.PointCloud2.data`

底层 `sensor_msgs::msg::dds_::PointCloud2_` 的 `data` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector；元素约束：取值范围为 0 到 255。

**签名**

```python
@property
def data(self) -> list[int]

@data.setter
def data(self, value: Sequence[int]) -> None
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

- 类：`sensor_msgs::msg::dds_::PointCloud2_`
- 字段类型：`std::vector<uint8_t>`
- 声明位置：`include/unitree/idl/ros2/PointCloud2_.hpp:35`

**用法**

```python
current_value = obj.data
obj.data = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-ros2-pointcloud2-is-dense"></a>
#### `unitree_sdk2_cpp.idl.ros2.PointCloud2.is_dense`

底层 `sensor_msgs::msg::dds_::PointCloud2_` 的 `is_dense` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 只接受布尔语义。

**签名**

```python
@property
def is_dense(self) -> bool

@is_dense.setter
def is_dense(self, value: bool) -> None
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

- 类：`sensor_msgs::msg::dds_::PointCloud2_`
- 字段类型：`bool`
- 声明位置：`include/unitree/idl/ros2/PointCloud2_.hpp:36`

**用法**

```python
current_value = obj.is_dense
obj.is_dense = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-pointstamped"></a>
### `unitree_sdk2_cpp.idl.ros2.PointStamped`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.ros2 import PointStamped
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-ros2-pointstamped-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-ros2-pointstamped-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-ros2-pointstamped-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`header`](#unitree-sdk2-cpp-idl-ros2-pointstamped-header) | `Any` | `Any` | `AVAILABLE` |
| [`point`](#unitree-sdk2-cpp-idl-ros2-pointstamped-point) | `Point` | `Point` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-ros2-pointstamped-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.PointStamped.__init__`

初始化 `PointStamped` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`geometry_msgs::msg::dds_::PointStamped_`
- 签名：`PointStamped_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/ros2/PointStamped_.hpp:30`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = PointStamped()
```

<a id="unitree-sdk2-cpp-idl-ros2-pointstamped-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.PointStamped.__eq__`

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

- 类：`geometry_msgs::msg::dds_::PointStamped_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-ros2-pointstamped-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.PointStamped.__ne__`

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

- 类：`geometry_msgs::msg::dds_::PointStamped_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-ros2-pointstamped-header"></a>
#### `unitree_sdk2_cpp.idl.ros2.PointStamped.header`

底层 `geometry_msgs::msg::dds_::PointStamped_` 的 `header` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def header(self) -> Any

@header.setter
def header(self, value: Any) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Any` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `Any` | 返回属性当前值。 |

**对应 C++**

- 类：`geometry_msgs::msg::dds_::PointStamped_`
- 字段类型：`::std_msgs::msg::dds_::Header_`
- 声明位置：`include/unitree/idl/ros2/PointStamped_.hpp:26`

**用法**

```python
current_value = obj.header
obj.header = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-pointstamped-point"></a>
#### `unitree_sdk2_cpp.idl.ros2.PointStamped.point`

底层 `geometry_msgs::msg::dds_::PointStamped_` 的 `point` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def point(self) -> Point

@point.setter
def point(self, value: Point) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Point` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `Point` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`geometry_msgs::msg::dds_::PointStamped_`
- 字段类型：`::geometry_msgs::msg::dds_::Point_`
- 声明位置：`include/unitree/idl/ros2/PointStamped_.hpp:27`

**用法**

```python
current_value = obj.point
obj.point = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-pose2d"></a>
### `unitree_sdk2_cpp.idl.ros2.Pose2D`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.ros2 import Pose2D
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-ros2-pose2d-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-ros2-pose2d-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-ros2-pose2d-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`x`](#unitree-sdk2-cpp-idl-ros2-pose2d-x) | `float` | `float` | `AVAILABLE` |
| [`y`](#unitree-sdk2-cpp-idl-ros2-pose2d-y) | `float` | `float` | `AVAILABLE` |
| [`theta`](#unitree-sdk2-cpp-idl-ros2-pose2d-theta) | `float` | `float` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-ros2-pose2d-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.Pose2D.__init__`

初始化 `Pose2D` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`geometry_msgs::msg::dds_::Pose2D_`
- 签名：`Pose2D_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/ros2/Pose2D_.hpp:27`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = Pose2D()
```

<a id="unitree-sdk2-cpp-idl-ros2-pose2d-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.Pose2D.__eq__`

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

- 类：`geometry_msgs::msg::dds_::Pose2D_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-ros2-pose2d-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.Pose2D.__ne__`

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

- 类：`geometry_msgs::msg::dds_::Pose2D_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-ros2-pose2d-x"></a>
#### `unitree_sdk2_cpp.idl.ros2.Pose2D.x`

底层 `geometry_msgs::msg::dds_::Pose2D_` 的 `x` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def x(self) -> float

@x.setter
def x(self, value: float) -> None
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

- 类：`geometry_msgs::msg::dds_::Pose2D_`
- 字段类型：`double`
- 声明位置：`include/unitree/idl/ros2/Pose2D_.hpp:22`

**用法**

```python
current_value = obj.x
obj.x = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-pose2d-y"></a>
#### `unitree_sdk2_cpp.idl.ros2.Pose2D.y`

底层 `geometry_msgs::msg::dds_::Pose2D_` 的 `y` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def y(self) -> float

@y.setter
def y(self, value: float) -> None
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

- 类：`geometry_msgs::msg::dds_::Pose2D_`
- 字段类型：`double`
- 声明位置：`include/unitree/idl/ros2/Pose2D_.hpp:23`

**用法**

```python
current_value = obj.y
obj.y = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-pose2d-theta"></a>
#### `unitree_sdk2_cpp.idl.ros2.Pose2D.theta`

底层 `geometry_msgs::msg::dds_::Pose2D_` 的 `theta` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def theta(self) -> float

@theta.setter
def theta(self, value: float) -> None
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

- 类：`geometry_msgs::msg::dds_::Pose2D_`
- 字段类型：`double`
- 声明位置：`include/unitree/idl/ros2/Pose2D_.hpp:24`

**用法**

```python
current_value = obj.theta
obj.theta = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-posestamped"></a>
### `unitree_sdk2_cpp.idl.ros2.PoseStamped`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.ros2 import PoseStamped
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-ros2-posestamped-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-ros2-posestamped-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-ros2-posestamped-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`header`](#unitree-sdk2-cpp-idl-ros2-posestamped-header) | `Any` | `Any` | `AVAILABLE` |
| [`pose`](#unitree-sdk2-cpp-idl-ros2-posestamped-pose) | `Pose` | `Pose` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-ros2-posestamped-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.PoseStamped.__init__`

初始化 `PoseStamped` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`geometry_msgs::msg::dds_::PoseStamped_`
- 签名：`PoseStamped_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/ros2/PoseStamped_.hpp:30`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = PoseStamped()
```

<a id="unitree-sdk2-cpp-idl-ros2-posestamped-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.PoseStamped.__eq__`

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

- 类：`geometry_msgs::msg::dds_::PoseStamped_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-ros2-posestamped-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.PoseStamped.__ne__`

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

- 类：`geometry_msgs::msg::dds_::PoseStamped_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-ros2-posestamped-header"></a>
#### `unitree_sdk2_cpp.idl.ros2.PoseStamped.header`

底层 `geometry_msgs::msg::dds_::PoseStamped_` 的 `header` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def header(self) -> Any

@header.setter
def header(self, value: Any) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Any` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `Any` | 返回属性当前值。 |

**对应 C++**

- 类：`geometry_msgs::msg::dds_::PoseStamped_`
- 字段类型：`::std_msgs::msg::dds_::Header_`
- 声明位置：`include/unitree/idl/ros2/PoseStamped_.hpp:26`

**用法**

```python
current_value = obj.header
obj.header = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-posestamped-pose"></a>
#### `unitree_sdk2_cpp.idl.ros2.PoseStamped.pose`

底层 `geometry_msgs::msg::dds_::PoseStamped_` 的 `pose` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def pose(self) -> Pose

@pose.setter
def pose(self, value: Pose) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Pose` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `Pose` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`geometry_msgs::msg::dds_::PoseStamped_`
- 字段类型：`::geometry_msgs::msg::dds_::Pose_`
- 声明位置：`include/unitree/idl/ros2/PoseStamped_.hpp:27`

**用法**

```python
current_value = obj.pose
obj.pose = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-posewithcovariancestamped"></a>
### `unitree_sdk2_cpp.idl.ros2.PoseWithCovarianceStamped`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.ros2 import PoseWithCovarianceStamped
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-ros2-posewithcovariancestamped-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-ros2-posewithcovariancestamped-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-ros2-posewithcovariancestamped-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`header`](#unitree-sdk2-cpp-idl-ros2-posewithcovariancestamped-header) | `Any` | `Any` | `AVAILABLE` |
| [`pose`](#unitree-sdk2-cpp-idl-ros2-posewithcovariancestamped-pose) | `PoseWithCovariance` | `PoseWithCovariance` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-ros2-posewithcovariancestamped-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.PoseWithCovarianceStamped.__init__`

初始化 `PoseWithCovarianceStamped` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`geometry_msgs::msg::dds_::PoseWithCovarianceStamped_`
- 签名：`PoseWithCovarianceStamped_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/ros2/PoseWithCovarianceStamped_.hpp:30`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = PoseWithCovarianceStamped()
```

<a id="unitree-sdk2-cpp-idl-ros2-posewithcovariancestamped-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.PoseWithCovarianceStamped.__eq__`

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

- 类：`geometry_msgs::msg::dds_::PoseWithCovarianceStamped_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-ros2-posewithcovariancestamped-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.PoseWithCovarianceStamped.__ne__`

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

- 类：`geometry_msgs::msg::dds_::PoseWithCovarianceStamped_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-ros2-posewithcovariancestamped-header"></a>
#### `unitree_sdk2_cpp.idl.ros2.PoseWithCovarianceStamped.header`

底层 `geometry_msgs::msg::dds_::PoseWithCovarianceStamped_` 的 `header` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def header(self) -> Any

@header.setter
def header(self, value: Any) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Any` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `Any` | 返回属性当前值。 |

**对应 C++**

- 类：`geometry_msgs::msg::dds_::PoseWithCovarianceStamped_`
- 字段类型：`::std_msgs::msg::dds_::Header_`
- 声明位置：`include/unitree/idl/ros2/PoseWithCovarianceStamped_.hpp:26`

**用法**

```python
current_value = obj.header
obj.header = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-posewithcovariancestamped-pose"></a>
#### `unitree_sdk2_cpp.idl.ros2.PoseWithCovarianceStamped.pose`

底层 `geometry_msgs::msg::dds_::PoseWithCovarianceStamped_` 的 `pose` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def pose(self) -> PoseWithCovariance

@pose.setter
def pose(self, value: PoseWithCovariance) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `PoseWithCovariance` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `PoseWithCovariance` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`geometry_msgs::msg::dds_::PoseWithCovarianceStamped_`
- 字段类型：`::geometry_msgs::msg::dds_::PoseWithCovariance_`
- 声明位置：`include/unitree/idl/ros2/PoseWithCovarianceStamped_.hpp:27`

**用法**

```python
current_value = obj.pose
obj.pose = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-quaternionstamped"></a>
### `unitree_sdk2_cpp.idl.ros2.QuaternionStamped`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.ros2 import QuaternionStamped
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-ros2-quaternionstamped-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-ros2-quaternionstamped-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-ros2-quaternionstamped-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`header`](#unitree-sdk2-cpp-idl-ros2-quaternionstamped-header) | `Any` | `Any` | `AVAILABLE` |
| [`quaternion`](#unitree-sdk2-cpp-idl-ros2-quaternionstamped-quaternion) | `Quaternion` | `Quaternion` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-ros2-quaternionstamped-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.QuaternionStamped.__init__`

初始化 `QuaternionStamped` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`geometry_msgs::msg::dds_::QuaternionStamped_`
- 签名：`QuaternionStamped_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/ros2/QuaternionStamped_.hpp:30`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = QuaternionStamped()
```

<a id="unitree-sdk2-cpp-idl-ros2-quaternionstamped-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.QuaternionStamped.__eq__`

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

- 类：`geometry_msgs::msg::dds_::QuaternionStamped_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-ros2-quaternionstamped-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.QuaternionStamped.__ne__`

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

- 类：`geometry_msgs::msg::dds_::QuaternionStamped_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-ros2-quaternionstamped-header"></a>
#### `unitree_sdk2_cpp.idl.ros2.QuaternionStamped.header`

底层 `geometry_msgs::msg::dds_::QuaternionStamped_` 的 `header` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def header(self) -> Any

@header.setter
def header(self, value: Any) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Any` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `Any` | 返回属性当前值。 |

**对应 C++**

- 类：`geometry_msgs::msg::dds_::QuaternionStamped_`
- 字段类型：`::std_msgs::msg::dds_::Header_`
- 声明位置：`include/unitree/idl/ros2/QuaternionStamped_.hpp:26`

**用法**

```python
current_value = obj.header
obj.header = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-quaternionstamped-quaternion"></a>
#### `unitree_sdk2_cpp.idl.ros2.QuaternionStamped.quaternion`

底层 `geometry_msgs::msg::dds_::QuaternionStamped_` 的 `quaternion` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def quaternion(self) -> Quaternion

@quaternion.setter
def quaternion(self, value: Quaternion) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Quaternion` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `Quaternion` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`geometry_msgs::msg::dds_::QuaternionStamped_`
- 字段类型：`::geometry_msgs::msg::dds_::Quaternion_`
- 声明位置：`include/unitree/idl/ros2/QuaternionStamped_.hpp:27`

**用法**

```python
current_value = obj.quaternion
obj.quaternion = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-string"></a>
### `unitree_sdk2_cpp.idl.ros2.String`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.ros2 import String
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-ros2-string-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-ros2-string-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-ros2-string-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`data`](#unitree-sdk2-cpp-idl-ros2-string-data) | `str` | `str` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-ros2-string-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.String.__init__`

初始化 `String` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`std_msgs::msg::dds_::String_`
- 签名：`String_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/ros2/String_.hpp:26`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = String()
```

<a id="unitree-sdk2-cpp-idl-ros2-string-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.String.__eq__`

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

- 类：`std_msgs::msg::dds_::String_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-ros2-string-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.String.__ne__`

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

- 类：`std_msgs::msg::dds_::String_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-ros2-string-data"></a>
#### `unitree_sdk2_cpp.idl.ros2.String.data`

底层 `std_msgs::msg::dds_::String_` 的 `data` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

**签名**

```python
@property
def data(self) -> str

@data.setter
def data(self, value: str) -> None
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

- 类：`std_msgs::msg::dds_::String_`
- 字段类型：`std::string`
- 声明位置：`include/unitree/idl/ros2/String_.hpp:23`

**用法**

```python
current_value = obj.data
obj.data = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-twiststamped"></a>
### `unitree_sdk2_cpp.idl.ros2.TwistStamped`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.ros2 import TwistStamped
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-ros2-twiststamped-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-ros2-twiststamped-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-ros2-twiststamped-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`header`](#unitree-sdk2-cpp-idl-ros2-twiststamped-header) | `Any` | `Any` | `AVAILABLE` |
| [`twist`](#unitree-sdk2-cpp-idl-ros2-twiststamped-twist) | `Twist` | `Twist` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-ros2-twiststamped-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.TwistStamped.__init__`

初始化 `TwistStamped` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`geometry_msgs::msg::dds_::TwistStamped_`
- 签名：`TwistStamped_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/ros2/TwistStamped_.hpp:30`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = TwistStamped()
```

<a id="unitree-sdk2-cpp-idl-ros2-twiststamped-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.TwistStamped.__eq__`

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

- 类：`geometry_msgs::msg::dds_::TwistStamped_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-ros2-twiststamped-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.TwistStamped.__ne__`

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

- 类：`geometry_msgs::msg::dds_::TwistStamped_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-ros2-twiststamped-header"></a>
#### `unitree_sdk2_cpp.idl.ros2.TwistStamped.header`

底层 `geometry_msgs::msg::dds_::TwistStamped_` 的 `header` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def header(self) -> Any

@header.setter
def header(self, value: Any) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Any` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `Any` | 返回属性当前值。 |

**对应 C++**

- 类：`geometry_msgs::msg::dds_::TwistStamped_`
- 字段类型：`::std_msgs::msg::dds_::Header_`
- 声明位置：`include/unitree/idl/ros2/TwistStamped_.hpp:26`

**用法**

```python
current_value = obj.header
obj.header = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-twiststamped-twist"></a>
#### `unitree_sdk2_cpp.idl.ros2.TwistStamped.twist`

底层 `geometry_msgs::msg::dds_::TwistStamped_` 的 `twist` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def twist(self) -> Twist

@twist.setter
def twist(self, value: Twist) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Twist` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `Twist` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`geometry_msgs::msg::dds_::TwistStamped_`
- 字段类型：`::geometry_msgs::msg::dds_::Twist_`
- 声明位置：`include/unitree/idl/ros2/TwistStamped_.hpp:27`

**用法**

```python
current_value = obj.twist
obj.twist = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-twistwithcovariancestamped"></a>
### `unitree_sdk2_cpp.idl.ros2.TwistWithCovarianceStamped`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.ros2 import TwistWithCovarianceStamped
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-ros2-twistwithcovariancestamped-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-ros2-twistwithcovariancestamped-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-ros2-twistwithcovariancestamped-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`header`](#unitree-sdk2-cpp-idl-ros2-twistwithcovariancestamped-header) | `Any` | `Any` | `AVAILABLE` |
| [`twist`](#unitree-sdk2-cpp-idl-ros2-twistwithcovariancestamped-twist) | `TwistWithCovariance` | `TwistWithCovariance` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-ros2-twistwithcovariancestamped-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.TwistWithCovarianceStamped.__init__`

初始化 `TwistWithCovarianceStamped` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`geometry_msgs::msg::dds_::TwistWithCovarianceStamped_`
- 签名：`TwistWithCovarianceStamped_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/ros2/TwistWithCovarianceStamped_.hpp:30`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = TwistWithCovarianceStamped()
```

<a id="unitree-sdk2-cpp-idl-ros2-twistwithcovariancestamped-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.TwistWithCovarianceStamped.__eq__`

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

- 类：`geometry_msgs::msg::dds_::TwistWithCovarianceStamped_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-ros2-twistwithcovariancestamped-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.ros2.TwistWithCovarianceStamped.__ne__`

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

- 类：`geometry_msgs::msg::dds_::TwistWithCovarianceStamped_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-ros2-twistwithcovariancestamped-header"></a>
#### `unitree_sdk2_cpp.idl.ros2.TwistWithCovarianceStamped.header`

底层 `geometry_msgs::msg::dds_::TwistWithCovarianceStamped_` 的 `header` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def header(self) -> Any

@header.setter
def header(self, value: Any) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Any` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `Any` | 返回属性当前值。 |

**对应 C++**

- 类：`geometry_msgs::msg::dds_::TwistWithCovarianceStamped_`
- 字段类型：`::std_msgs::msg::dds_::Header_`
- 声明位置：`include/unitree/idl/ros2/TwistWithCovarianceStamped_.hpp:26`

**用法**

```python
current_value = obj.header
obj.header = new_value
```

<a id="unitree-sdk2-cpp-idl-ros2-twistwithcovariancestamped-twist"></a>
#### `unitree_sdk2_cpp.idl.ros2.TwistWithCovarianceStamped.twist`

底层 `geometry_msgs::msg::dds_::TwistWithCovarianceStamped_` 的 `twist` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def twist(self) -> TwistWithCovariance

@twist.setter
def twist(self, value: TwistWithCovariance) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `TwistWithCovariance` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `TwistWithCovariance` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`geometry_msgs::msg::dds_::TwistWithCovarianceStamped_`
- 字段类型：`::geometry_msgs::msg::dds_::TwistWithCovariance_`
- 声明位置：`include/unitree/idl/ros2/TwistWithCovarianceStamped_.hpp:27`

**用法**

```python
current_value = obj.twist
obj.twist = new_value
```

---

[返回 API 总索引](../API_REFERENCE_ZH.md)
