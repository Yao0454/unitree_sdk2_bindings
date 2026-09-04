# Unitree SDK2 Python API 参考分卷

[返回 API 总索引](../API_REFERENCE_ZH.md) · [阅读从零开始指南](../BEGINNER_GUIDE_ZH.md)

> [!WARNING]
> 本分卷同时包含 `AVAILABLE` 和 `SIGNATURE_ONLY`。后者只是设计期类型签名。运动及硬件副作用方法即使标记为 `AVAILABLE`，也不表示当前环境可安全执行。

> [!NOTE]
> 本文件由 `generator/generate_api_docs.py` 自动生成，请勿手工维护 API 条目。

---

<a id="unitree-sdk2-cpp-idl-go2"></a>
## Go2 IDL 消息

模块：`unitree_sdk2_cpp.idl.go2`

### 类索引

| 类 | 公开函数签名 | 属性 |
| --- | ---: | ---: |
| [`AudioData`](#unitree-sdk2-cpp-idl-go2-audiodata) | 3 | 2 |
| [`BmsCmd`](#unitree-sdk2-cpp-idl-go2-bmscmd) | 3 | 2 |
| [`BmsState`](#unitree-sdk2-cpp-idl-go2-bmsstate) | 3 | 9 |
| [`ConfigChangeStatus`](#unitree-sdk2-cpp-idl-go2-configchangestatus) | 3 | 2 |
| [`Error`](#unitree-sdk2-cpp-idl-go2-error) | 3 | 2 |
| [`Go2FrontVideoData`](#unitree-sdk2-cpp-idl-go2-go2frontvideodata) | 3 | 4 |
| [`HeightMap`](#unitree-sdk2-cpp-idl-go2-heightmap) | 3 | 7 |
| [`IMUState`](#unitree-sdk2-cpp-idl-go2-imustate) | 3 | 5 |
| [`InterfaceConfig`](#unitree-sdk2-cpp-idl-go2-interfaceconfig) | 3 | 3 |
| [`LidarState`](#unitree-sdk2-cpp-idl-go2-lidarstate) | 3 | 18 |
| [`MotorCmd`](#unitree-sdk2-cpp-idl-go2-motorcmd) | 3 | 7 |
| [`LowCmd`](#unitree-sdk2-cpp-idl-go2-lowcmd) | 3 | 14 |
| [`MotorState`](#unitree-sdk2-cpp-idl-go2-motorstate) | 3 | 11 |
| [`LowState`](#unitree-sdk2-cpp-idl-go2-lowstate) | 3 | 22 |
| [`MotorCmds`](#unitree-sdk2-cpp-idl-go2-motorcmds) | 3 | 1 |
| [`MotorStates`](#unitree-sdk2-cpp-idl-go2-motorstates) | 3 | 1 |
| [`PathPoint`](#unitree-sdk2-cpp-idl-go2-pathpoint) | 3 | 7 |
| [`Req`](#unitree-sdk2-cpp-idl-go2-req) | 3 | 2 |
| [`Res`](#unitree-sdk2-cpp-idl-go2-res) | 3 | 3 |
| [`SportModeCmd`](#unitree-sdk2-cpp-idl-go2-sportmodecmd) | 3 | 11 |
| [`TimeSpec`](#unitree-sdk2-cpp-idl-go2-timespec) | 3 | 2 |
| [`SportModeState`](#unitree-sdk2-cpp-idl-go2-sportmodestate) | 3 | 16 |
| [`UwbState`](#unitree-sdk2-cpp-idl-go2-uwbstate) | 3 | 17 |
| [`UwbSwitch`](#unitree-sdk2-cpp-idl-go2-uwbswitch) | 3 | 1 |
| [`VoxelMapCompressed`](#unitree-sdk2-cpp-idl-go2-voxelmapcompressed) | 3 | 7 |
| [`WirelessController`](#unitree-sdk2-cpp-idl-go2-wirelesscontroller) | 3 | 5 |

<a id="unitree-sdk2-cpp-idl-go2-audiodata"></a>
### `unitree_sdk2_cpp.idl.go2.AudioData`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.go2 import AudioData
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-go2-audiodata-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-go2-audiodata-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-go2-audiodata-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`time_frame`](#unitree-sdk2-cpp-idl-go2-audiodata-time-frame) | `int` | `int` | `AVAILABLE` |
| [`data`](#unitree-sdk2-cpp-idl-go2-audiodata-data) | `list[int]` | `Sequence[int]` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-go2-audiodata-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.go2.AudioData.__init__`

初始化 `AudioData` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree_go::msg::dds_::AudioData_`
- 签名：`AudioData_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/go2/AudioData_.hpp:28`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = AudioData()
```

<a id="unitree-sdk2-cpp-idl-go2-audiodata-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.go2.AudioData.__eq__`

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

- 类：`unitree_go::msg::dds_::AudioData_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-go2-audiodata-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.go2.AudioData.__ne__`

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

- 类：`unitree_go::msg::dds_::AudioData_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-go2-audiodata-time-frame"></a>
#### `unitree_sdk2_cpp.idl.go2.AudioData.time_frame`

底层 `unitree_go::msg::dds_::AudioData_` 的 `time_frame` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 18446744073709551615。

**签名**

```python
@property
def time_frame(self) -> int

@time_frame.setter
def time_frame(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::AudioData_`
- 字段类型：`uint64_t`
- 声明位置：`include/unitree/idl/go2/AudioData_.hpp:24`

**用法**

```python
current_value = obj.time_frame
obj.time_frame = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-audiodata-data"></a>
#### `unitree_sdk2_cpp.idl.go2.AudioData.data`

底层 `unitree_go::msg::dds_::AudioData_` 的 `data` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector；元素约束：取值范围为 0 到 255。

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

- 类：`unitree_go::msg::dds_::AudioData_`
- 字段类型：`std::vector<uint8_t>`
- 声明位置：`include/unitree/idl/go2/AudioData_.hpp:25`

**用法**

```python
current_value = obj.data
obj.data = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-bmscmd"></a>
### `unitree_sdk2_cpp.idl.go2.BmsCmd`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.go2 import BmsCmd
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-go2-bmscmd-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-go2-bmscmd-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-go2-bmscmd-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`off`](#unitree-sdk2-cpp-idl-go2-bmscmd-off) | `int` | `int` | `AVAILABLE` |
| [`reserve`](#unitree-sdk2-cpp-idl-go2-bmscmd-reserve) | `list[int]` | `Sequence[int]` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-go2-bmscmd-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.go2.BmsCmd.__init__`

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

- 类：`unitree_go::msg::dds_::BmsCmd_`
- 签名：`BmsCmd_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/go2/BmsCmd_.hpp:28`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = BmsCmd()
```

<a id="unitree-sdk2-cpp-idl-go2-bmscmd-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.go2.BmsCmd.__eq__`

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

- 类：`unitree_go::msg::dds_::BmsCmd_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-go2-bmscmd-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.go2.BmsCmd.__ne__`

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

- 类：`unitree_go::msg::dds_::BmsCmd_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-go2-bmscmd-off"></a>
#### `unitree_sdk2_cpp.idl.go2.BmsCmd.off`

底层 `unitree_go::msg::dds_::BmsCmd_` 的 `off` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def off(self) -> int

@off.setter
def off(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::BmsCmd_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/go2/BmsCmd_.hpp:24`

**用法**

```python
current_value = obj.off
obj.off = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-bmscmd-reserve"></a>
#### `unitree_sdk2_cpp.idl.go2.BmsCmd.reserve`

底层 `unitree_go::msg::dds_::BmsCmd_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：取值范围为 0 到 255。

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

- 类：`unitree_go::msg::dds_::BmsCmd_`
- 字段类型：`std::array<uint8_t, 3>`
- 声明位置：`include/unitree/idl/go2/BmsCmd_.hpp:25`

**用法**

```python
current_value = obj.reserve
obj.reserve = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-bmsstate"></a>
### `unitree_sdk2_cpp.idl.go2.BmsState`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.go2 import BmsState
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-go2-bmsstate-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-go2-bmsstate-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-go2-bmsstate-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`version_high`](#unitree-sdk2-cpp-idl-go2-bmsstate-version-high) | `int` | `int` | `AVAILABLE` |
| [`version_low`](#unitree-sdk2-cpp-idl-go2-bmsstate-version-low) | `int` | `int` | `AVAILABLE` |
| [`status`](#unitree-sdk2-cpp-idl-go2-bmsstate-status) | `int` | `int` | `AVAILABLE` |
| [`soc`](#unitree-sdk2-cpp-idl-go2-bmsstate-soc) | `int` | `int` | `AVAILABLE` |
| [`current`](#unitree-sdk2-cpp-idl-go2-bmsstate-current) | `int` | `int` | `AVAILABLE` |
| [`cycle`](#unitree-sdk2-cpp-idl-go2-bmsstate-cycle) | `int` | `int` | `AVAILABLE` |
| [`bq_ntc`](#unitree-sdk2-cpp-idl-go2-bmsstate-bq-ntc) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`mcu_ntc`](#unitree-sdk2-cpp-idl-go2-bmsstate-mcu-ntc) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`cell_vol`](#unitree-sdk2-cpp-idl-go2-bmsstate-cell-vol) | `list[int]` | `Sequence[int]` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-go2-bmsstate-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.go2.BmsState.__init__`

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

- 类：`unitree_go::msg::dds_::BmsState_`
- 签名：`BmsState_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/go2/BmsState_.hpp:35`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = BmsState()
```

<a id="unitree-sdk2-cpp-idl-go2-bmsstate-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.go2.BmsState.__eq__`

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

- 类：`unitree_go::msg::dds_::BmsState_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-go2-bmsstate-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.go2.BmsState.__ne__`

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

- 类：`unitree_go::msg::dds_::BmsState_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-go2-bmsstate-version-high"></a>
#### `unitree_sdk2_cpp.idl.go2.BmsState.version_high`

底层 `unitree_go::msg::dds_::BmsState_` 的 `version_high` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

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

- 类：`unitree_go::msg::dds_::BmsState_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/go2/BmsState_.hpp:24`

**用法**

```python
current_value = obj.version_high
obj.version_high = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-bmsstate-version-low"></a>
#### `unitree_sdk2_cpp.idl.go2.BmsState.version_low`

底层 `unitree_go::msg::dds_::BmsState_` 的 `version_low` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

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

- 类：`unitree_go::msg::dds_::BmsState_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/go2/BmsState_.hpp:25`

**用法**

```python
current_value = obj.version_low
obj.version_low = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-bmsstate-status"></a>
#### `unitree_sdk2_cpp.idl.go2.BmsState.status`

底层 `unitree_go::msg::dds_::BmsState_` 的 `status` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def status(self) -> int

@status.setter
def status(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::BmsState_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/go2/BmsState_.hpp:26`

**用法**

```python
current_value = obj.status
obj.status = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-bmsstate-soc"></a>
#### `unitree_sdk2_cpp.idl.go2.BmsState.soc`

底层 `unitree_go::msg::dds_::BmsState_` 的 `soc` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

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

- 类：`unitree_go::msg::dds_::BmsState_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/go2/BmsState_.hpp:27`

**用法**

```python
current_value = obj.soc
obj.soc = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-bmsstate-current"></a>
#### `unitree_sdk2_cpp.idl.go2.BmsState.current`

底层 `unitree_go::msg::dds_::BmsState_` 的 `current` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 -2147483648 到 2147483647。

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

- 类：`unitree_go::msg::dds_::BmsState_`
- 字段类型：`int32_t`
- 声明位置：`include/unitree/idl/go2/BmsState_.hpp:28`

**用法**

```python
current_value = obj.current
obj.current = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-bmsstate-cycle"></a>
#### `unitree_sdk2_cpp.idl.go2.BmsState.cycle`

底层 `unitree_go::msg::dds_::BmsState_` 的 `cycle` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 65535。

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

- 类：`unitree_go::msg::dds_::BmsState_`
- 字段类型：`uint16_t`
- 声明位置：`include/unitree/idl/go2/BmsState_.hpp:29`

**用法**

```python
current_value = obj.cycle
obj.cycle = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-bmsstate-bq-ntc"></a>
#### `unitree_sdk2_cpp.idl.go2.BmsState.bq_ntc`

底层 `unitree_go::msg::dds_::BmsState_` 的 `bq_ntc` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 255。

**签名**

```python
@property
def bq_ntc(self) -> list[int]

@bq_ntc.setter
def bq_ntc(self, value: Sequence[int]) -> None
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

- 类：`unitree_go::msg::dds_::BmsState_`
- 字段类型：`std::array<uint8_t, 2>`
- 声明位置：`include/unitree/idl/go2/BmsState_.hpp:30`

**用法**

```python
current_value = obj.bq_ntc
obj.bq_ntc = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-bmsstate-mcu-ntc"></a>
#### `unitree_sdk2_cpp.idl.go2.BmsState.mcu_ntc`

底层 `unitree_go::msg::dds_::BmsState_` 的 `mcu_ntc` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 255。

**签名**

```python
@property
def mcu_ntc(self) -> list[int]

@mcu_ntc.setter
def mcu_ntc(self, value: Sequence[int]) -> None
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

- 类：`unitree_go::msg::dds_::BmsState_`
- 字段类型：`std::array<uint8_t, 2>`
- 声明位置：`include/unitree/idl/go2/BmsState_.hpp:31`

**用法**

```python
current_value = obj.mcu_ntc
obj.mcu_ntc = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-bmsstate-cell-vol"></a>
#### `unitree_sdk2_cpp.idl.go2.BmsState.cell_vol`

底层 `unitree_go::msg::dds_::BmsState_` 的 `cell_vol` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 15 个元素；元素约束：取值范围为 0 到 65535。

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

- 类：`unitree_go::msg::dds_::BmsState_`
- 字段类型：`std::array<uint16_t, 15>`
- 声明位置：`include/unitree/idl/go2/BmsState_.hpp:32`

**用法**

```python
current_value = obj.cell_vol
obj.cell_vol = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-configchangestatus"></a>
### `unitree_sdk2_cpp.idl.go2.ConfigChangeStatus`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.go2 import ConfigChangeStatus
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-go2-configchangestatus-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-go2-configchangestatus-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-go2-configchangestatus-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`name`](#unitree-sdk2-cpp-idl-go2-configchangestatus-name) | `str` | `str` | `AVAILABLE` |
| [`content`](#unitree-sdk2-cpp-idl-go2-configchangestatus-content) | `str` | `str` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-go2-configchangestatus-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.go2.ConfigChangeStatus.__init__`

初始化 `ConfigChangeStatus` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree_go::msg::dds_::ConfigChangeStatus_`
- 签名：`ConfigChangeStatus_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/go2/ConfigChangeStatus_.hpp:27`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = ConfigChangeStatus()
```

<a id="unitree-sdk2-cpp-idl-go2-configchangestatus-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.go2.ConfigChangeStatus.__eq__`

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

- 类：`unitree_go::msg::dds_::ConfigChangeStatus_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-go2-configchangestatus-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.go2.ConfigChangeStatus.__ne__`

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

- 类：`unitree_go::msg::dds_::ConfigChangeStatus_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-go2-configchangestatus-name"></a>
#### `unitree_sdk2_cpp.idl.go2.ConfigChangeStatus.name`

底层 `unitree_go::msg::dds_::ConfigChangeStatus_` 的 `name` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

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

- 类：`unitree_go::msg::dds_::ConfigChangeStatus_`
- 字段类型：`std::string`
- 声明位置：`include/unitree/idl/go2/ConfigChangeStatus_.hpp:23`

**用法**

```python
current_value = obj.name
obj.name = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-configchangestatus-content"></a>
#### `unitree_sdk2_cpp.idl.go2.ConfigChangeStatus.content`

底层 `unitree_go::msg::dds_::ConfigChangeStatus_` 的 `content` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

**签名**

```python
@property
def content(self) -> str

@content.setter
def content(self, value: str) -> None
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

- 类：`unitree_go::msg::dds_::ConfigChangeStatus_`
- 字段类型：`std::string`
- 声明位置：`include/unitree/idl/go2/ConfigChangeStatus_.hpp:24`

**用法**

```python
current_value = obj.content
obj.content = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-error"></a>
### `unitree_sdk2_cpp.idl.go2.Error`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.go2 import Error
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-go2-error-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-go2-error-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-go2-error-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`source`](#unitree-sdk2-cpp-idl-go2-error-source) | `int` | `int` | `AVAILABLE` |
| [`state`](#unitree-sdk2-cpp-idl-go2-error-state) | `int` | `int` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-go2-error-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.go2.Error.__init__`

初始化 `Error` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree_go::msg::dds_::Error_`
- 签名：`Error_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/go2/Error_.hpp:27`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = Error()
```

<a id="unitree-sdk2-cpp-idl-go2-error-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.go2.Error.__eq__`

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

- 类：`unitree_go::msg::dds_::Error_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-go2-error-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.go2.Error.__ne__`

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

- 类：`unitree_go::msg::dds_::Error_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-go2-error-source"></a>
#### `unitree_sdk2_cpp.idl.go2.Error.source`

底层 `unitree_go::msg::dds_::Error_` 的 `source` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

**签名**

```python
@property
def source(self) -> int

@source.setter
def source(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::Error_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/go2/Error_.hpp:23`

**用法**

```python
current_value = obj.source
obj.source = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-error-state"></a>
#### `unitree_sdk2_cpp.idl.go2.Error.state`

底层 `unitree_go::msg::dds_::Error_` 的 `state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

**签名**

```python
@property
def state(self) -> int

@state.setter
def state(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::Error_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/go2/Error_.hpp:24`

**用法**

```python
current_value = obj.state
obj.state = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-go2frontvideodata"></a>
### `unitree_sdk2_cpp.idl.go2.Go2FrontVideoData`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.go2 import Go2FrontVideoData
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-go2-go2frontvideodata-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-go2-go2frontvideodata-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-go2-go2frontvideodata-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`time_frame`](#unitree-sdk2-cpp-idl-go2-go2frontvideodata-time-frame) | `int` | `int` | `AVAILABLE` |
| [`video720p`](#unitree-sdk2-cpp-idl-go2-go2frontvideodata-video720p) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`video360p`](#unitree-sdk2-cpp-idl-go2-go2frontvideodata-video360p) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`video180p`](#unitree-sdk2-cpp-idl-go2-go2frontvideodata-video180p) | `list[int]` | `Sequence[int]` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-go2-go2frontvideodata-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.go2.Go2FrontVideoData.__init__`

初始化 `Go2FrontVideoData` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree_go::msg::dds_::Go2FrontVideoData_`
- 签名：`Go2FrontVideoData_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/go2/Go2FrontVideoData_.hpp:30`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = Go2FrontVideoData()
```

<a id="unitree-sdk2-cpp-idl-go2-go2frontvideodata-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.go2.Go2FrontVideoData.__eq__`

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

- 类：`unitree_go::msg::dds_::Go2FrontVideoData_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-go2-go2frontvideodata-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.go2.Go2FrontVideoData.__ne__`

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

- 类：`unitree_go::msg::dds_::Go2FrontVideoData_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-go2-go2frontvideodata-time-frame"></a>
#### `unitree_sdk2_cpp.idl.go2.Go2FrontVideoData.time_frame`

底层 `unitree_go::msg::dds_::Go2FrontVideoData_` 的 `time_frame` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 18446744073709551615。

**签名**

```python
@property
def time_frame(self) -> int

@time_frame.setter
def time_frame(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::Go2FrontVideoData_`
- 字段类型：`uint64_t`
- 声明位置：`include/unitree/idl/go2/Go2FrontVideoData_.hpp:24`

**用法**

```python
current_value = obj.time_frame
obj.time_frame = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-go2frontvideodata-video720p"></a>
#### `unitree_sdk2_cpp.idl.go2.Go2FrontVideoData.video720p`

底层 `unitree_go::msg::dds_::Go2FrontVideoData_` 的 `video720p` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector；元素约束：取值范围为 0 到 255。

**签名**

```python
@property
def video720p(self) -> list[int]

@video720p.setter
def video720p(self, value: Sequence[int]) -> None
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

- 类：`unitree_go::msg::dds_::Go2FrontVideoData_`
- 字段类型：`std::vector<uint8_t>`
- 声明位置：`include/unitree/idl/go2/Go2FrontVideoData_.hpp:25`

**用法**

```python
current_value = obj.video720p
obj.video720p = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-go2frontvideodata-video360p"></a>
#### `unitree_sdk2_cpp.idl.go2.Go2FrontVideoData.video360p`

底层 `unitree_go::msg::dds_::Go2FrontVideoData_` 的 `video360p` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector；元素约束：取值范围为 0 到 255。

**签名**

```python
@property
def video360p(self) -> list[int]

@video360p.setter
def video360p(self, value: Sequence[int]) -> None
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

- 类：`unitree_go::msg::dds_::Go2FrontVideoData_`
- 字段类型：`std::vector<uint8_t>`
- 声明位置：`include/unitree/idl/go2/Go2FrontVideoData_.hpp:26`

**用法**

```python
current_value = obj.video360p
obj.video360p = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-go2frontvideodata-video180p"></a>
#### `unitree_sdk2_cpp.idl.go2.Go2FrontVideoData.video180p`

底层 `unitree_go::msg::dds_::Go2FrontVideoData_` 的 `video180p` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector；元素约束：取值范围为 0 到 255。

**签名**

```python
@property
def video180p(self) -> list[int]

@video180p.setter
def video180p(self, value: Sequence[int]) -> None
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

- 类：`unitree_go::msg::dds_::Go2FrontVideoData_`
- 字段类型：`std::vector<uint8_t>`
- 声明位置：`include/unitree/idl/go2/Go2FrontVideoData_.hpp:27`

**用法**

```python
current_value = obj.video180p
obj.video180p = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-heightmap"></a>
### `unitree_sdk2_cpp.idl.go2.HeightMap`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.go2 import HeightMap
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-go2-heightmap-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-go2-heightmap-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-go2-heightmap-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`stamp`](#unitree-sdk2-cpp-idl-go2-heightmap-stamp) | `float` | `float` | `AVAILABLE` |
| [`frame_id`](#unitree-sdk2-cpp-idl-go2-heightmap-frame-id) | `str` | `str` | `AVAILABLE` |
| [`resolution`](#unitree-sdk2-cpp-idl-go2-heightmap-resolution) | `float` | `float` | `AVAILABLE` |
| [`width`](#unitree-sdk2-cpp-idl-go2-heightmap-width) | `int` | `int` | `AVAILABLE` |
| [`height`](#unitree-sdk2-cpp-idl-go2-heightmap-height) | `int` | `int` | `AVAILABLE` |
| [`origin`](#unitree-sdk2-cpp-idl-go2-heightmap-origin) | `list[float]` | `Sequence[float]` | `AVAILABLE` |
| [`data`](#unitree-sdk2-cpp-idl-go2-heightmap-data) | `list[float]` | `Sequence[float]` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-go2-heightmap-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.go2.HeightMap.__init__`

初始化 `HeightMap` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree_go::msg::dds_::HeightMap_`
- 签名：`HeightMap_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/go2/HeightMap_.hpp:35`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = HeightMap()
```

<a id="unitree-sdk2-cpp-idl-go2-heightmap-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.go2.HeightMap.__eq__`

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

- 类：`unitree_go::msg::dds_::HeightMap_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-go2-heightmap-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.go2.HeightMap.__ne__`

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

- 类：`unitree_go::msg::dds_::HeightMap_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-go2-heightmap-stamp"></a>
#### `unitree_sdk2_cpp.idl.go2.HeightMap.stamp`

底层 `unitree_go::msg::dds_::HeightMap_` 的 `stamp` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def stamp(self) -> float

@stamp.setter
def stamp(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::HeightMap_`
- 字段类型：`double`
- 声明位置：`include/unitree/idl/go2/HeightMap_.hpp:26`

**用法**

```python
current_value = obj.stamp
obj.stamp = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-heightmap-frame-id"></a>
#### `unitree_sdk2_cpp.idl.go2.HeightMap.frame_id`

底层 `unitree_go::msg::dds_::HeightMap_` 的 `frame_id` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

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

- 类：`unitree_go::msg::dds_::HeightMap_`
- 字段类型：`std::string`
- 声明位置：`include/unitree/idl/go2/HeightMap_.hpp:27`

**用法**

```python
current_value = obj.frame_id
obj.frame_id = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-heightmap-resolution"></a>
#### `unitree_sdk2_cpp.idl.go2.HeightMap.resolution`

底层 `unitree_go::msg::dds_::HeightMap_` 的 `resolution` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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

- 类：`unitree_go::msg::dds_::HeightMap_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/HeightMap_.hpp:28`

**用法**

```python
current_value = obj.resolution
obj.resolution = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-heightmap-width"></a>
#### `unitree_sdk2_cpp.idl.go2.HeightMap.width`

底层 `unitree_go::msg::dds_::HeightMap_` 的 `width` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

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

- 类：`unitree_go::msg::dds_::HeightMap_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/go2/HeightMap_.hpp:29`

**用法**

```python
current_value = obj.width
obj.width = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-heightmap-height"></a>
#### `unitree_sdk2_cpp.idl.go2.HeightMap.height`

底层 `unitree_go::msg::dds_::HeightMap_` 的 `height` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

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

- 类：`unitree_go::msg::dds_::HeightMap_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/go2/HeightMap_.hpp:30`

**用法**

```python
current_value = obj.height
obj.height = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-heightmap-origin"></a>
#### `unitree_sdk2_cpp.idl.go2.HeightMap.origin`

底层 `unitree_go::msg::dds_::HeightMap_` 的 `origin` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def origin(self) -> list[float]

@origin.setter
def origin(self, value: Sequence[float]) -> None
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

- 类：`unitree_go::msg::dds_::HeightMap_`
- 字段类型：`std::array<float, 2>`
- 声明位置：`include/unitree/idl/go2/HeightMap_.hpp:31`

**用法**

```python
current_value = obj.origin
obj.origin = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-heightmap-data"></a>
#### `unitree_sdk2_cpp.idl.go2.HeightMap.data`

底层 `unitree_go::msg::dds_::HeightMap_` 的 `data` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def data(self) -> list[float]

@data.setter
def data(self, value: Sequence[float]) -> None
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

- 类：`unitree_go::msg::dds_::HeightMap_`
- 字段类型：`std::vector<float>`
- 声明位置：`include/unitree/idl/go2/HeightMap_.hpp:32`

**用法**

```python
current_value = obj.data
obj.data = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-imustate"></a>
### `unitree_sdk2_cpp.idl.go2.IMUState`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.go2 import IMUState
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-go2-imustate-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-go2-imustate-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-go2-imustate-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`quaternion`](#unitree-sdk2-cpp-idl-go2-imustate-quaternion) | `list[float]` | `Sequence[float]` | `AVAILABLE` |
| [`gyroscope`](#unitree-sdk2-cpp-idl-go2-imustate-gyroscope) | `list[float]` | `Sequence[float]` | `AVAILABLE` |
| [`accelerometer`](#unitree-sdk2-cpp-idl-go2-imustate-accelerometer) | `list[float]` | `Sequence[float]` | `AVAILABLE` |
| [`rpy`](#unitree-sdk2-cpp-idl-go2-imustate-rpy) | `list[float]` | `Sequence[float]` | `AVAILABLE` |
| [`temperature`](#unitree-sdk2-cpp-idl-go2-imustate-temperature) | `int` | `int` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-go2-imustate-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.go2.IMUState.__init__`

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

- 类：`unitree_go::msg::dds_::IMUState_`
- 签名：`IMUState_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/go2/IMUState_.hpp:31`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = IMUState()
```

<a id="unitree-sdk2-cpp-idl-go2-imustate-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.go2.IMUState.__eq__`

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

- 类：`unitree_go::msg::dds_::IMUState_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-go2-imustate-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.go2.IMUState.__ne__`

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

- 类：`unitree_go::msg::dds_::IMUState_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-go2-imustate-quaternion"></a>
#### `unitree_sdk2_cpp.idl.go2.IMUState.quaternion`

底层 `unitree_go::msg::dds_::IMUState_` 的 `quaternion` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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

- 类：`unitree_go::msg::dds_::IMUState_`
- 字段类型：`std::array<float, 4>`
- 声明位置：`include/unitree/idl/go2/IMUState_.hpp:24`

**用法**

```python
current_value = obj.quaternion
obj.quaternion = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-imustate-gyroscope"></a>
#### `unitree_sdk2_cpp.idl.go2.IMUState.gyroscope`

底层 `unitree_go::msg::dds_::IMUState_` 的 `gyroscope` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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

- 类：`unitree_go::msg::dds_::IMUState_`
- 字段类型：`std::array<float, 3>`
- 声明位置：`include/unitree/idl/go2/IMUState_.hpp:25`

**用法**

```python
current_value = obj.gyroscope
obj.gyroscope = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-imustate-accelerometer"></a>
#### `unitree_sdk2_cpp.idl.go2.IMUState.accelerometer`

底层 `unitree_go::msg::dds_::IMUState_` 的 `accelerometer` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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

- 类：`unitree_go::msg::dds_::IMUState_`
- 字段类型：`std::array<float, 3>`
- 声明位置：`include/unitree/idl/go2/IMUState_.hpp:26`

**用法**

```python
current_value = obj.accelerometer
obj.accelerometer = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-imustate-rpy"></a>
#### `unitree_sdk2_cpp.idl.go2.IMUState.rpy`

底层 `unitree_go::msg::dds_::IMUState_` 的 `rpy` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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

- 类：`unitree_go::msg::dds_::IMUState_`
- 字段类型：`std::array<float, 3>`
- 声明位置：`include/unitree/idl/go2/IMUState_.hpp:27`

**用法**

```python
current_value = obj.rpy
obj.rpy = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-imustate-temperature"></a>
#### `unitree_sdk2_cpp.idl.go2.IMUState.temperature`

底层 `unitree_go::msg::dds_::IMUState_` 的 `temperature` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

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

- 类：`unitree_go::msg::dds_::IMUState_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/go2/IMUState_.hpp:28`

**用法**

```python
current_value = obj.temperature
obj.temperature = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-interfaceconfig"></a>
### `unitree_sdk2_cpp.idl.go2.InterfaceConfig`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.go2 import InterfaceConfig
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-go2-interfaceconfig-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-go2-interfaceconfig-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-go2-interfaceconfig-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`mode`](#unitree-sdk2-cpp-idl-go2-interfaceconfig-mode) | `int` | `int` | `AVAILABLE` |
| [`value`](#unitree-sdk2-cpp-idl-go2-interfaceconfig-value) | `int` | `int` | `AVAILABLE` |
| [`reserve`](#unitree-sdk2-cpp-idl-go2-interfaceconfig-reserve) | `list[int]` | `Sequence[int]` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-go2-interfaceconfig-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.go2.InterfaceConfig.__init__`

初始化 `InterfaceConfig` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree_go::msg::dds_::InterfaceConfig_`
- 签名：`InterfaceConfig_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/go2/InterfaceConfig_.hpp:29`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = InterfaceConfig()
```

<a id="unitree-sdk2-cpp-idl-go2-interfaceconfig-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.go2.InterfaceConfig.__eq__`

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

- 类：`unitree_go::msg::dds_::InterfaceConfig_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-go2-interfaceconfig-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.go2.InterfaceConfig.__ne__`

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

- 类：`unitree_go::msg::dds_::InterfaceConfig_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-go2-interfaceconfig-mode"></a>
#### `unitree_sdk2_cpp.idl.go2.InterfaceConfig.mode`

底层 `unitree_go::msg::dds_::InterfaceConfig_` 的 `mode` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

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

- 类：`unitree_go::msg::dds_::InterfaceConfig_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/go2/InterfaceConfig_.hpp:24`

**用法**

```python
current_value = obj.mode
obj.mode = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-interfaceconfig-value"></a>
#### `unitree_sdk2_cpp.idl.go2.InterfaceConfig.value`

底层 `unitree_go::msg::dds_::InterfaceConfig_` 的 `value` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def value(self) -> int

@value.setter
def value(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::InterfaceConfig_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/go2/InterfaceConfig_.hpp:25`

**用法**

```python
current_value = obj.value
obj.value = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-interfaceconfig-reserve"></a>
#### `unitree_sdk2_cpp.idl.go2.InterfaceConfig.reserve`

底层 `unitree_go::msg::dds_::InterfaceConfig_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 255。

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

- 类：`unitree_go::msg::dds_::InterfaceConfig_`
- 字段类型：`std::array<uint8_t, 2>`
- 声明位置：`include/unitree/idl/go2/InterfaceConfig_.hpp:26`

**用法**

```python
current_value = obj.reserve
obj.reserve = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-lidarstate"></a>
### `unitree_sdk2_cpp.idl.go2.LidarState`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.go2 import LidarState
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-go2-lidarstate-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-go2-lidarstate-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-go2-lidarstate-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`stamp`](#unitree-sdk2-cpp-idl-go2-lidarstate-stamp) | `float` | `float` | `AVAILABLE` |
| [`firmware_version`](#unitree-sdk2-cpp-idl-go2-lidarstate-firmware-version) | `str` | `str` | `AVAILABLE` |
| [`software_version`](#unitree-sdk2-cpp-idl-go2-lidarstate-software-version) | `str` | `str` | `AVAILABLE` |
| [`sdk_version`](#unitree-sdk2-cpp-idl-go2-lidarstate-sdk-version) | `str` | `str` | `AVAILABLE` |
| [`sys_rotation_speed`](#unitree-sdk2-cpp-idl-go2-lidarstate-sys-rotation-speed) | `float` | `float` | `AVAILABLE` |
| [`com_rotation_speed`](#unitree-sdk2-cpp-idl-go2-lidarstate-com-rotation-speed) | `float` | `float` | `AVAILABLE` |
| [`error_state`](#unitree-sdk2-cpp-idl-go2-lidarstate-error-state) | `int` | `int` | `AVAILABLE` |
| [`dirty_percentage`](#unitree-sdk2-cpp-idl-go2-lidarstate-dirty-percentage) | `int` | `int` | `AVAILABLE` |
| [`cloud_frequency`](#unitree-sdk2-cpp-idl-go2-lidarstate-cloud-frequency) | `float` | `float` | `AVAILABLE` |
| [`cloud_packet_loss_rate`](#unitree-sdk2-cpp-idl-go2-lidarstate-cloud-packet-loss-rate) | `float` | `float` | `AVAILABLE` |
| [`cloud_size`](#unitree-sdk2-cpp-idl-go2-lidarstate-cloud-size) | `int` | `int` | `AVAILABLE` |
| [`cloud_scan_num`](#unitree-sdk2-cpp-idl-go2-lidarstate-cloud-scan-num) | `int` | `int` | `AVAILABLE` |
| [`imu_frequency`](#unitree-sdk2-cpp-idl-go2-lidarstate-imu-frequency) | `float` | `float` | `AVAILABLE` |
| [`imu_packet_loss_rate`](#unitree-sdk2-cpp-idl-go2-lidarstate-imu-packet-loss-rate) | `float` | `float` | `AVAILABLE` |
| [`imu_rpy`](#unitree-sdk2-cpp-idl-go2-lidarstate-imu-rpy) | `list[float]` | `Sequence[float]` | `AVAILABLE` |
| [`serial_recv_stamp`](#unitree-sdk2-cpp-idl-go2-lidarstate-serial-recv-stamp) | `float` | `float` | `AVAILABLE` |
| [`serial_buffer_size`](#unitree-sdk2-cpp-idl-go2-lidarstate-serial-buffer-size) | `int` | `int` | `AVAILABLE` |
| [`serial_buffer_read`](#unitree-sdk2-cpp-idl-go2-lidarstate-serial-buffer-read) | `int` | `int` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-go2-lidarstate-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.go2.LidarState.__init__`

初始化 `LidarState` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree_go::msg::dds_::LidarState_`
- 签名：`LidarState_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/go2/LidarState_.hpp:45`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = LidarState()
```

<a id="unitree-sdk2-cpp-idl-go2-lidarstate-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.go2.LidarState.__eq__`

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

- 类：`unitree_go::msg::dds_::LidarState_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-go2-lidarstate-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.go2.LidarState.__ne__`

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

- 类：`unitree_go::msg::dds_::LidarState_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-go2-lidarstate-stamp"></a>
#### `unitree_sdk2_cpp.idl.go2.LidarState.stamp`

底层 `unitree_go::msg::dds_::LidarState_` 的 `stamp` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def stamp(self) -> float

@stamp.setter
def stamp(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::LidarState_`
- 字段类型：`double`
- 声明位置：`include/unitree/idl/go2/LidarState_.hpp:25`

**用法**

```python
current_value = obj.stamp
obj.stamp = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lidarstate-firmware-version"></a>
#### `unitree_sdk2_cpp.idl.go2.LidarState.firmware_version`

底层 `unitree_go::msg::dds_::LidarState_` 的 `firmware_version` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

**签名**

```python
@property
def firmware_version(self) -> str

@firmware_version.setter
def firmware_version(self, value: str) -> None
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

- 类：`unitree_go::msg::dds_::LidarState_`
- 字段类型：`std::string`
- 声明位置：`include/unitree/idl/go2/LidarState_.hpp:26`

**用法**

```python
current_value = obj.firmware_version
obj.firmware_version = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lidarstate-software-version"></a>
#### `unitree_sdk2_cpp.idl.go2.LidarState.software_version`

底层 `unitree_go::msg::dds_::LidarState_` 的 `software_version` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

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

- 类：`unitree_go::msg::dds_::LidarState_`
- 字段类型：`std::string`
- 声明位置：`include/unitree/idl/go2/LidarState_.hpp:27`

**用法**

```python
current_value = obj.software_version
obj.software_version = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lidarstate-sdk-version"></a>
#### `unitree_sdk2_cpp.idl.go2.LidarState.sdk_version`

底层 `unitree_go::msg::dds_::LidarState_` 的 `sdk_version` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

**签名**

```python
@property
def sdk_version(self) -> str

@sdk_version.setter
def sdk_version(self, value: str) -> None
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

- 类：`unitree_go::msg::dds_::LidarState_`
- 字段类型：`std::string`
- 声明位置：`include/unitree/idl/go2/LidarState_.hpp:28`

**用法**

```python
current_value = obj.sdk_version
obj.sdk_version = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lidarstate-sys-rotation-speed"></a>
#### `unitree_sdk2_cpp.idl.go2.LidarState.sys_rotation_speed`

底层 `unitree_go::msg::dds_::LidarState_` 的 `sys_rotation_speed` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def sys_rotation_speed(self) -> float

@sys_rotation_speed.setter
def sys_rotation_speed(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::LidarState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/LidarState_.hpp:29`

**用法**

```python
current_value = obj.sys_rotation_speed
obj.sys_rotation_speed = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lidarstate-com-rotation-speed"></a>
#### `unitree_sdk2_cpp.idl.go2.LidarState.com_rotation_speed`

底层 `unitree_go::msg::dds_::LidarState_` 的 `com_rotation_speed` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def com_rotation_speed(self) -> float

@com_rotation_speed.setter
def com_rotation_speed(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::LidarState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/LidarState_.hpp:30`

**用法**

```python
current_value = obj.com_rotation_speed
obj.com_rotation_speed = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lidarstate-error-state"></a>
#### `unitree_sdk2_cpp.idl.go2.LidarState.error_state`

底层 `unitree_go::msg::dds_::LidarState_` 的 `error_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def error_state(self) -> int

@error_state.setter
def error_state(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::LidarState_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/go2/LidarState_.hpp:31`

**用法**

```python
current_value = obj.error_state
obj.error_state = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lidarstate-dirty-percentage"></a>
#### `unitree_sdk2_cpp.idl.go2.LidarState.dirty_percentage`

底层 `unitree_go::msg::dds_::LidarState_` 的 `dirty_percentage` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def dirty_percentage(self) -> int

@dirty_percentage.setter
def dirty_percentage(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::LidarState_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/go2/LidarState_.hpp:32`

**用法**

```python
current_value = obj.dirty_percentage
obj.dirty_percentage = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lidarstate-cloud-frequency"></a>
#### `unitree_sdk2_cpp.idl.go2.LidarState.cloud_frequency`

底层 `unitree_go::msg::dds_::LidarState_` 的 `cloud_frequency` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def cloud_frequency(self) -> float

@cloud_frequency.setter
def cloud_frequency(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::LidarState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/LidarState_.hpp:33`

**用法**

```python
current_value = obj.cloud_frequency
obj.cloud_frequency = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lidarstate-cloud-packet-loss-rate"></a>
#### `unitree_sdk2_cpp.idl.go2.LidarState.cloud_packet_loss_rate`

底层 `unitree_go::msg::dds_::LidarState_` 的 `cloud_packet_loss_rate` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def cloud_packet_loss_rate(self) -> float

@cloud_packet_loss_rate.setter
def cloud_packet_loss_rate(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::LidarState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/LidarState_.hpp:34`

**用法**

```python
current_value = obj.cloud_packet_loss_rate
obj.cloud_packet_loss_rate = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lidarstate-cloud-size"></a>
#### `unitree_sdk2_cpp.idl.go2.LidarState.cloud_size`

底层 `unitree_go::msg::dds_::LidarState_` 的 `cloud_size` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

**签名**

```python
@property
def cloud_size(self) -> int

@cloud_size.setter
def cloud_size(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::LidarState_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/go2/LidarState_.hpp:35`

**用法**

```python
current_value = obj.cloud_size
obj.cloud_size = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lidarstate-cloud-scan-num"></a>
#### `unitree_sdk2_cpp.idl.go2.LidarState.cloud_scan_num`

底层 `unitree_go::msg::dds_::LidarState_` 的 `cloud_scan_num` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

**签名**

```python
@property
def cloud_scan_num(self) -> int

@cloud_scan_num.setter
def cloud_scan_num(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::LidarState_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/go2/LidarState_.hpp:36`

**用法**

```python
current_value = obj.cloud_scan_num
obj.cloud_scan_num = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lidarstate-imu-frequency"></a>
#### `unitree_sdk2_cpp.idl.go2.LidarState.imu_frequency`

底层 `unitree_go::msg::dds_::LidarState_` 的 `imu_frequency` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def imu_frequency(self) -> float

@imu_frequency.setter
def imu_frequency(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::LidarState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/LidarState_.hpp:37`

**用法**

```python
current_value = obj.imu_frequency
obj.imu_frequency = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lidarstate-imu-packet-loss-rate"></a>
#### `unitree_sdk2_cpp.idl.go2.LidarState.imu_packet_loss_rate`

底层 `unitree_go::msg::dds_::LidarState_` 的 `imu_packet_loss_rate` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def imu_packet_loss_rate(self) -> float

@imu_packet_loss_rate.setter
def imu_packet_loss_rate(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::LidarState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/LidarState_.hpp:38`

**用法**

```python
current_value = obj.imu_packet_loss_rate
obj.imu_packet_loss_rate = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lidarstate-imu-rpy"></a>
#### `unitree_sdk2_cpp.idl.go2.LidarState.imu_rpy`

底层 `unitree_go::msg::dds_::LidarState_` 的 `imu_rpy` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def imu_rpy(self) -> list[float]

@imu_rpy.setter
def imu_rpy(self, value: Sequence[float]) -> None
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

- 类：`unitree_go::msg::dds_::LidarState_`
- 字段类型：`std::array<float, 3>`
- 声明位置：`include/unitree/idl/go2/LidarState_.hpp:39`

**用法**

```python
current_value = obj.imu_rpy
obj.imu_rpy = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-lidarstate-serial-recv-stamp"></a>
#### `unitree_sdk2_cpp.idl.go2.LidarState.serial_recv_stamp`

底层 `unitree_go::msg::dds_::LidarState_` 的 `serial_recv_stamp` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def serial_recv_stamp(self) -> float

@serial_recv_stamp.setter
def serial_recv_stamp(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::LidarState_`
- 字段类型：`double`
- 声明位置：`include/unitree/idl/go2/LidarState_.hpp:40`

**用法**

```python
current_value = obj.serial_recv_stamp
obj.serial_recv_stamp = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lidarstate-serial-buffer-size"></a>
#### `unitree_sdk2_cpp.idl.go2.LidarState.serial_buffer_size`

底层 `unitree_go::msg::dds_::LidarState_` 的 `serial_buffer_size` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

**签名**

```python
@property
def serial_buffer_size(self) -> int

@serial_buffer_size.setter
def serial_buffer_size(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::LidarState_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/go2/LidarState_.hpp:41`

**用法**

```python
current_value = obj.serial_buffer_size
obj.serial_buffer_size = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lidarstate-serial-buffer-read"></a>
#### `unitree_sdk2_cpp.idl.go2.LidarState.serial_buffer_read`

底层 `unitree_go::msg::dds_::LidarState_` 的 `serial_buffer_read` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

**签名**

```python
@property
def serial_buffer_read(self) -> int

@serial_buffer_read.setter
def serial_buffer_read(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::LidarState_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/go2/LidarState_.hpp:42`

**用法**

```python
current_value = obj.serial_buffer_read
obj.serial_buffer_read = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-motorcmd"></a>
### `unitree_sdk2_cpp.idl.go2.MotorCmd`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.go2 import MotorCmd
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-go2-motorcmd-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-go2-motorcmd-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-go2-motorcmd-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`mode`](#unitree-sdk2-cpp-idl-go2-motorcmd-mode) | `int` | `int` | `AVAILABLE` |
| [`q`](#unitree-sdk2-cpp-idl-go2-motorcmd-q) | `float` | `float` | `AVAILABLE` |
| [`dq`](#unitree-sdk2-cpp-idl-go2-motorcmd-dq) | `float` | `float` | `AVAILABLE` |
| [`tau`](#unitree-sdk2-cpp-idl-go2-motorcmd-tau) | `float` | `float` | `AVAILABLE` |
| [`kp`](#unitree-sdk2-cpp-idl-go2-motorcmd-kp) | `float` | `float` | `AVAILABLE` |
| [`kd`](#unitree-sdk2-cpp-idl-go2-motorcmd-kd) | `float` | `float` | `AVAILABLE` |
| [`reserve`](#unitree-sdk2-cpp-idl-go2-motorcmd-reserve) | `list[int]` | `Sequence[int]` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-go2-motorcmd-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.go2.MotorCmd.__init__`

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

- 类：`unitree_go::msg::dds_::MotorCmd_`
- 签名：`MotorCmd_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/go2/MotorCmd_.hpp:33`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = MotorCmd()
```

<a id="unitree-sdk2-cpp-idl-go2-motorcmd-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.go2.MotorCmd.__eq__`

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

- 类：`unitree_go::msg::dds_::MotorCmd_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-go2-motorcmd-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.go2.MotorCmd.__ne__`

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

- 类：`unitree_go::msg::dds_::MotorCmd_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-go2-motorcmd-mode"></a>
#### `unitree_sdk2_cpp.idl.go2.MotorCmd.mode`

底层 `unitree_go::msg::dds_::MotorCmd_` 的 `mode` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

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

- 类：`unitree_go::msg::dds_::MotorCmd_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/go2/MotorCmd_.hpp:24`

**用法**

```python
current_value = obj.mode
obj.mode = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-motorcmd-q"></a>
#### `unitree_sdk2_cpp.idl.go2.MotorCmd.q`

底层 `unitree_go::msg::dds_::MotorCmd_` 的 `q` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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

- 类：`unitree_go::msg::dds_::MotorCmd_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/MotorCmd_.hpp:25`

**用法**

```python
current_value = obj.q
obj.q = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-motorcmd-dq"></a>
#### `unitree_sdk2_cpp.idl.go2.MotorCmd.dq`

底层 `unitree_go::msg::dds_::MotorCmd_` 的 `dq` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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

- 类：`unitree_go::msg::dds_::MotorCmd_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/MotorCmd_.hpp:26`

**用法**

```python
current_value = obj.dq
obj.dq = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-motorcmd-tau"></a>
#### `unitree_sdk2_cpp.idl.go2.MotorCmd.tau`

底层 `unitree_go::msg::dds_::MotorCmd_` 的 `tau` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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

- 类：`unitree_go::msg::dds_::MotorCmd_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/MotorCmd_.hpp:27`

**用法**

```python
current_value = obj.tau
obj.tau = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-motorcmd-kp"></a>
#### `unitree_sdk2_cpp.idl.go2.MotorCmd.kp`

底层 `unitree_go::msg::dds_::MotorCmd_` 的 `kp` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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

- 类：`unitree_go::msg::dds_::MotorCmd_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/MotorCmd_.hpp:28`

**用法**

```python
current_value = obj.kp
obj.kp = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-motorcmd-kd"></a>
#### `unitree_sdk2_cpp.idl.go2.MotorCmd.kd`

底层 `unitree_go::msg::dds_::MotorCmd_` 的 `kd` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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

- 类：`unitree_go::msg::dds_::MotorCmd_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/MotorCmd_.hpp:29`

**用法**

```python
current_value = obj.kd
obj.kd = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-motorcmd-reserve"></a>
#### `unitree_sdk2_cpp.idl.go2.MotorCmd.reserve`

底层 `unitree_go::msg::dds_::MotorCmd_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：取值范围为 0 到 4294967295。

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

- 类：`unitree_go::msg::dds_::MotorCmd_`
- 字段类型：`std::array<uint32_t, 3>`
- 声明位置：`include/unitree/idl/go2/MotorCmd_.hpp:30`

**用法**

```python
current_value = obj.reserve
obj.reserve = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-lowcmd"></a>
### `unitree_sdk2_cpp.idl.go2.LowCmd`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.go2 import LowCmd
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-go2-lowcmd-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-go2-lowcmd-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-go2-lowcmd-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`head`](#unitree-sdk2-cpp-idl-go2-lowcmd-head) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`level_flag`](#unitree-sdk2-cpp-idl-go2-lowcmd-level-flag) | `int` | `int` | `AVAILABLE` |
| [`frame_reserve`](#unitree-sdk2-cpp-idl-go2-lowcmd-frame-reserve) | `int` | `int` | `AVAILABLE` |
| [`sn`](#unitree-sdk2-cpp-idl-go2-lowcmd-sn) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`version`](#unitree-sdk2-cpp-idl-go2-lowcmd-version) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`bandwidth`](#unitree-sdk2-cpp-idl-go2-lowcmd-bandwidth) | `int` | `int` | `AVAILABLE` |
| [`motor_cmd`](#unitree-sdk2-cpp-idl-go2-lowcmd-motor-cmd) | `list[MotorCmd]` | `Sequence[MotorCmd]` | `AVAILABLE` |
| [`bms_cmd`](#unitree-sdk2-cpp-idl-go2-lowcmd-bms-cmd) | `BmsCmd` | `BmsCmd` | `AVAILABLE` |
| [`wireless_remote`](#unitree-sdk2-cpp-idl-go2-lowcmd-wireless-remote) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`led`](#unitree-sdk2-cpp-idl-go2-lowcmd-led) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`fan`](#unitree-sdk2-cpp-idl-go2-lowcmd-fan) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`gpio`](#unitree-sdk2-cpp-idl-go2-lowcmd-gpio) | `int` | `int` | `AVAILABLE` |
| [`reserve`](#unitree-sdk2-cpp-idl-go2-lowcmd-reserve) | `int` | `int` | `AVAILABLE` |
| [`crc`](#unitree-sdk2-cpp-idl-go2-lowcmd-crc) | `int` | `int` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-go2-lowcmd-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.go2.LowCmd.__init__`

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

- 类：`unitree_go::msg::dds_::LowCmd_`
- 签名：`LowCmd_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/go2/LowCmd_.hpp:44`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = LowCmd()
```

<a id="unitree-sdk2-cpp-idl-go2-lowcmd-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.go2.LowCmd.__eq__`

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

- 类：`unitree_go::msg::dds_::LowCmd_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-go2-lowcmd-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.go2.LowCmd.__ne__`

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

- 类：`unitree_go::msg::dds_::LowCmd_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-go2-lowcmd-head"></a>
#### `unitree_sdk2_cpp.idl.go2.LowCmd.head`

底层 `unitree_go::msg::dds_::LowCmd_` 的 `head` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 255。

**签名**

```python
@property
def head(self) -> list[int]

@head.setter
def head(self, value: Sequence[int]) -> None
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

- 类：`unitree_go::msg::dds_::LowCmd_`
- 字段类型：`std::array<uint8_t, 2>`
- 声明位置：`include/unitree/idl/go2/LowCmd_.hpp:28`

**用法**

```python
current_value = obj.head
obj.head = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-lowcmd-level-flag"></a>
#### `unitree_sdk2_cpp.idl.go2.LowCmd.level_flag`

底层 `unitree_go::msg::dds_::LowCmd_` 的 `level_flag` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def level_flag(self) -> int

@level_flag.setter
def level_flag(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::LowCmd_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/go2/LowCmd_.hpp:29`

**用法**

```python
current_value = obj.level_flag
obj.level_flag = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lowcmd-frame-reserve"></a>
#### `unitree_sdk2_cpp.idl.go2.LowCmd.frame_reserve`

底层 `unitree_go::msg::dds_::LowCmd_` 的 `frame_reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def frame_reserve(self) -> int

@frame_reserve.setter
def frame_reserve(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::LowCmd_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/go2/LowCmd_.hpp:30`

**用法**

```python
current_value = obj.frame_reserve
obj.frame_reserve = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lowcmd-sn"></a>
#### `unitree_sdk2_cpp.idl.go2.LowCmd.sn`

底层 `unitree_go::msg::dds_::LowCmd_` 的 `sn` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 4294967295。

**签名**

```python
@property
def sn(self) -> list[int]

@sn.setter
def sn(self, value: Sequence[int]) -> None
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

- 类：`unitree_go::msg::dds_::LowCmd_`
- 字段类型：`std::array<uint32_t, 2>`
- 声明位置：`include/unitree/idl/go2/LowCmd_.hpp:31`

**用法**

```python
current_value = obj.sn
obj.sn = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-lowcmd-version"></a>
#### `unitree_sdk2_cpp.idl.go2.LowCmd.version`

底层 `unitree_go::msg::dds_::LowCmd_` 的 `version` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 4294967295。

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

- 类：`unitree_go::msg::dds_::LowCmd_`
- 字段类型：`std::array<uint32_t, 2>`
- 声明位置：`include/unitree/idl/go2/LowCmd_.hpp:32`

**用法**

```python
current_value = obj.version
obj.version = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-lowcmd-bandwidth"></a>
#### `unitree_sdk2_cpp.idl.go2.LowCmd.bandwidth`

底层 `unitree_go::msg::dds_::LowCmd_` 的 `bandwidth` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 65535。

**签名**

```python
@property
def bandwidth(self) -> int

@bandwidth.setter
def bandwidth(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::LowCmd_`
- 字段类型：`uint16_t`
- 声明位置：`include/unitree/idl/go2/LowCmd_.hpp:33`

**用法**

```python
current_value = obj.bandwidth
obj.bandwidth = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lowcmd-motor-cmd"></a>
#### `unitree_sdk2_cpp.idl.go2.LowCmd.motor_cmd`

底层 `unitree_go::msg::dds_::LowCmd_` 的 `motor_cmd` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 20 个元素

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

- 类：`unitree_go::msg::dds_::LowCmd_`
- 字段类型：`std::array< ::unitree_go::msg::dds_::MotorCmd_, 20>`
- 声明位置：`include/unitree/idl/go2/LowCmd_.hpp:34`

**用法**

```python
current_value = obj.motor_cmd
obj.motor_cmd = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-lowcmd-bms-cmd"></a>
#### `unitree_sdk2_cpp.idl.go2.LowCmd.bms_cmd`

底层 `unitree_go::msg::dds_::LowCmd_` 的 `bms_cmd` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def bms_cmd(self) -> BmsCmd

@bms_cmd.setter
def bms_cmd(self, value: BmsCmd) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `BmsCmd` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `BmsCmd` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_go::msg::dds_::LowCmd_`
- 字段类型：`::unitree_go::msg::dds_::BmsCmd_`
- 声明位置：`include/unitree/idl/go2/LowCmd_.hpp:35`

**用法**

```python
current_value = obj.bms_cmd
obj.bms_cmd = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lowcmd-wireless-remote"></a>
#### `unitree_sdk2_cpp.idl.go2.LowCmd.wireless_remote`

底层 `unitree_go::msg::dds_::LowCmd_` 的 `wireless_remote` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 40 个元素；元素约束：取值范围为 0 到 255。

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

- 类：`unitree_go::msg::dds_::LowCmd_`
- 字段类型：`std::array<uint8_t, 40>`
- 声明位置：`include/unitree/idl/go2/LowCmd_.hpp:36`

**用法**

```python
current_value = obj.wireless_remote
obj.wireless_remote = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-lowcmd-led"></a>
#### `unitree_sdk2_cpp.idl.go2.LowCmd.led`

底层 `unitree_go::msg::dds_::LowCmd_` 的 `led` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 12 个元素；元素约束：取值范围为 0 到 255。

**签名**

```python
@property
def led(self) -> list[int]

@led.setter
def led(self, value: Sequence[int]) -> None
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

- 类：`unitree_go::msg::dds_::LowCmd_`
- 字段类型：`std::array<uint8_t, 12>`
- 声明位置：`include/unitree/idl/go2/LowCmd_.hpp:37`

**用法**

```python
current_value = obj.led
obj.led = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-lowcmd-fan"></a>
#### `unitree_sdk2_cpp.idl.go2.LowCmd.fan`

底层 `unitree_go::msg::dds_::LowCmd_` 的 `fan` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 255。

**签名**

```python
@property
def fan(self) -> list[int]

@fan.setter
def fan(self, value: Sequence[int]) -> None
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

- 类：`unitree_go::msg::dds_::LowCmd_`
- 字段类型：`std::array<uint8_t, 2>`
- 声明位置：`include/unitree/idl/go2/LowCmd_.hpp:38`

**用法**

```python
current_value = obj.fan
obj.fan = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-lowcmd-gpio"></a>
#### `unitree_sdk2_cpp.idl.go2.LowCmd.gpio`

底层 `unitree_go::msg::dds_::LowCmd_` 的 `gpio` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def gpio(self) -> int

@gpio.setter
def gpio(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::LowCmd_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/go2/LowCmd_.hpp:39`

**用法**

```python
current_value = obj.gpio
obj.gpio = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lowcmd-reserve"></a>
#### `unitree_sdk2_cpp.idl.go2.LowCmd.reserve`

底层 `unitree_go::msg::dds_::LowCmd_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

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

- 类：`unitree_go::msg::dds_::LowCmd_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/go2/LowCmd_.hpp:40`

**用法**

```python
current_value = obj.reserve
obj.reserve = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lowcmd-crc"></a>
#### `unitree_sdk2_cpp.idl.go2.LowCmd.crc`

底层 `unitree_go::msg::dds_::LowCmd_` 的 `crc` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

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

- 类：`unitree_go::msg::dds_::LowCmd_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/go2/LowCmd_.hpp:41`

**用法**

```python
current_value = obj.crc
obj.crc = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-motorstate"></a>
### `unitree_sdk2_cpp.idl.go2.MotorState`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.go2 import MotorState
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-go2-motorstate-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-go2-motorstate-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-go2-motorstate-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`mode`](#unitree-sdk2-cpp-idl-go2-motorstate-mode) | `int` | `int` | `AVAILABLE` |
| [`q`](#unitree-sdk2-cpp-idl-go2-motorstate-q) | `float` | `float` | `AVAILABLE` |
| [`dq`](#unitree-sdk2-cpp-idl-go2-motorstate-dq) | `float` | `float` | `AVAILABLE` |
| [`ddq`](#unitree-sdk2-cpp-idl-go2-motorstate-ddq) | `float` | `float` | `AVAILABLE` |
| [`tau_est`](#unitree-sdk2-cpp-idl-go2-motorstate-tau-est) | `float` | `float` | `AVAILABLE` |
| [`q_raw`](#unitree-sdk2-cpp-idl-go2-motorstate-q-raw) | `float` | `float` | `AVAILABLE` |
| [`dq_raw`](#unitree-sdk2-cpp-idl-go2-motorstate-dq-raw) | `float` | `float` | `AVAILABLE` |
| [`ddq_raw`](#unitree-sdk2-cpp-idl-go2-motorstate-ddq-raw) | `float` | `float` | `AVAILABLE` |
| [`temperature`](#unitree-sdk2-cpp-idl-go2-motorstate-temperature) | `int` | `int` | `AVAILABLE` |
| [`lost`](#unitree-sdk2-cpp-idl-go2-motorstate-lost) | `int` | `int` | `AVAILABLE` |
| [`reserve`](#unitree-sdk2-cpp-idl-go2-motorstate-reserve) | `list[int]` | `Sequence[int]` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-go2-motorstate-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.go2.MotorState.__init__`

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

- 类：`unitree_go::msg::dds_::MotorState_`
- 签名：`MotorState_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/go2/MotorState_.hpp:37`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = MotorState()
```

<a id="unitree-sdk2-cpp-idl-go2-motorstate-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.go2.MotorState.__eq__`

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

- 类：`unitree_go::msg::dds_::MotorState_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-go2-motorstate-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.go2.MotorState.__ne__`

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

- 类：`unitree_go::msg::dds_::MotorState_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-go2-motorstate-mode"></a>
#### `unitree_sdk2_cpp.idl.go2.MotorState.mode`

底层 `unitree_go::msg::dds_::MotorState_` 的 `mode` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

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

- 类：`unitree_go::msg::dds_::MotorState_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/go2/MotorState_.hpp:24`

**用法**

```python
current_value = obj.mode
obj.mode = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-motorstate-q"></a>
#### `unitree_sdk2_cpp.idl.go2.MotorState.q`

底层 `unitree_go::msg::dds_::MotorState_` 的 `q` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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

- 类：`unitree_go::msg::dds_::MotorState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/MotorState_.hpp:25`

**用法**

```python
current_value = obj.q
obj.q = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-motorstate-dq"></a>
#### `unitree_sdk2_cpp.idl.go2.MotorState.dq`

底层 `unitree_go::msg::dds_::MotorState_` 的 `dq` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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

- 类：`unitree_go::msg::dds_::MotorState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/MotorState_.hpp:26`

**用法**

```python
current_value = obj.dq
obj.dq = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-motorstate-ddq"></a>
#### `unitree_sdk2_cpp.idl.go2.MotorState.ddq`

底层 `unitree_go::msg::dds_::MotorState_` 的 `ddq` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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

- 类：`unitree_go::msg::dds_::MotorState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/MotorState_.hpp:27`

**用法**

```python
current_value = obj.ddq
obj.ddq = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-motorstate-tau-est"></a>
#### `unitree_sdk2_cpp.idl.go2.MotorState.tau_est`

底层 `unitree_go::msg::dds_::MotorState_` 的 `tau_est` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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

- 类：`unitree_go::msg::dds_::MotorState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/MotorState_.hpp:28`

**用法**

```python
current_value = obj.tau_est
obj.tau_est = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-motorstate-q-raw"></a>
#### `unitree_sdk2_cpp.idl.go2.MotorState.q_raw`

底层 `unitree_go::msg::dds_::MotorState_` 的 `q_raw` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def q_raw(self) -> float

@q_raw.setter
def q_raw(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::MotorState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/MotorState_.hpp:29`

**用法**

```python
current_value = obj.q_raw
obj.q_raw = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-motorstate-dq-raw"></a>
#### `unitree_sdk2_cpp.idl.go2.MotorState.dq_raw`

底层 `unitree_go::msg::dds_::MotorState_` 的 `dq_raw` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def dq_raw(self) -> float

@dq_raw.setter
def dq_raw(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::MotorState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/MotorState_.hpp:30`

**用法**

```python
current_value = obj.dq_raw
obj.dq_raw = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-motorstate-ddq-raw"></a>
#### `unitree_sdk2_cpp.idl.go2.MotorState.ddq_raw`

底层 `unitree_go::msg::dds_::MotorState_` 的 `ddq_raw` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def ddq_raw(self) -> float

@ddq_raw.setter
def ddq_raw(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::MotorState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/MotorState_.hpp:31`

**用法**

```python
current_value = obj.ddq_raw
obj.ddq_raw = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-motorstate-temperature"></a>
#### `unitree_sdk2_cpp.idl.go2.MotorState.temperature`

底层 `unitree_go::msg::dds_::MotorState_` 的 `temperature` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

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

- 类：`unitree_go::msg::dds_::MotorState_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/go2/MotorState_.hpp:32`

**用法**

```python
current_value = obj.temperature
obj.temperature = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-motorstate-lost"></a>
#### `unitree_sdk2_cpp.idl.go2.MotorState.lost`

底层 `unitree_go::msg::dds_::MotorState_` 的 `lost` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

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

- 类：`unitree_go::msg::dds_::MotorState_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/go2/MotorState_.hpp:33`

**用法**

```python
current_value = obj.lost
obj.lost = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-motorstate-reserve"></a>
#### `unitree_sdk2_cpp.idl.go2.MotorState.reserve`

底层 `unitree_go::msg::dds_::MotorState_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 4294967295。

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

- 类：`unitree_go::msg::dds_::MotorState_`
- 字段类型：`std::array<uint32_t, 2>`
- 声明位置：`include/unitree/idl/go2/MotorState_.hpp:34`

**用法**

```python
current_value = obj.reserve
obj.reserve = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-lowstate"></a>
### `unitree_sdk2_cpp.idl.go2.LowState`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.go2 import LowState
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-go2-lowstate-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-go2-lowstate-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-go2-lowstate-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`head`](#unitree-sdk2-cpp-idl-go2-lowstate-head) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`level_flag`](#unitree-sdk2-cpp-idl-go2-lowstate-level-flag) | `int` | `int` | `AVAILABLE` |
| [`frame_reserve`](#unitree-sdk2-cpp-idl-go2-lowstate-frame-reserve) | `int` | `int` | `AVAILABLE` |
| [`sn`](#unitree-sdk2-cpp-idl-go2-lowstate-sn) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`version`](#unitree-sdk2-cpp-idl-go2-lowstate-version) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`bandwidth`](#unitree-sdk2-cpp-idl-go2-lowstate-bandwidth) | `int` | `int` | `AVAILABLE` |
| [`imu_state`](#unitree-sdk2-cpp-idl-go2-lowstate-imu-state) | `IMUState` | `IMUState` | `AVAILABLE` |
| [`motor_state`](#unitree-sdk2-cpp-idl-go2-lowstate-motor-state) | `list[MotorState]` | `Sequence[MotorState]` | `AVAILABLE` |
| [`bms_state`](#unitree-sdk2-cpp-idl-go2-lowstate-bms-state) | `BmsState` | `BmsState` | `AVAILABLE` |
| [`foot_force`](#unitree-sdk2-cpp-idl-go2-lowstate-foot-force) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`foot_force_est`](#unitree-sdk2-cpp-idl-go2-lowstate-foot-force-est) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`tick`](#unitree-sdk2-cpp-idl-go2-lowstate-tick) | `int` | `int` | `AVAILABLE` |
| [`wireless_remote`](#unitree-sdk2-cpp-idl-go2-lowstate-wireless-remote) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`bit_flag`](#unitree-sdk2-cpp-idl-go2-lowstate-bit-flag) | `int` | `int` | `AVAILABLE` |
| [`adc_reel`](#unitree-sdk2-cpp-idl-go2-lowstate-adc-reel) | `float` | `float` | `AVAILABLE` |
| [`temperature_ntc1`](#unitree-sdk2-cpp-idl-go2-lowstate-temperature-ntc1) | `int` | `int` | `AVAILABLE` |
| [`temperature_ntc2`](#unitree-sdk2-cpp-idl-go2-lowstate-temperature-ntc2) | `int` | `int` | `AVAILABLE` |
| [`power_v`](#unitree-sdk2-cpp-idl-go2-lowstate-power-v) | `float` | `float` | `AVAILABLE` |
| [`power_a`](#unitree-sdk2-cpp-idl-go2-lowstate-power-a) | `float` | `float` | `AVAILABLE` |
| [`fan_frequency`](#unitree-sdk2-cpp-idl-go2-lowstate-fan-frequency) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`reserve`](#unitree-sdk2-cpp-idl-go2-lowstate-reserve) | `int` | `int` | `AVAILABLE` |
| [`crc`](#unitree-sdk2-cpp-idl-go2-lowstate-crc) | `int` | `int` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-go2-lowstate-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.go2.LowState.__init__`

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

- 类：`unitree_go::msg::dds_::LowState_`
- 签名：`LowState_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/go2/LowState_.hpp:54`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = LowState()
```

<a id="unitree-sdk2-cpp-idl-go2-lowstate-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.go2.LowState.__eq__`

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

- 类：`unitree_go::msg::dds_::LowState_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-go2-lowstate-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.go2.LowState.__ne__`

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

- 类：`unitree_go::msg::dds_::LowState_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-go2-lowstate-head"></a>
#### `unitree_sdk2_cpp.idl.go2.LowState.head`

底层 `unitree_go::msg::dds_::LowState_` 的 `head` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 255。

**签名**

```python
@property
def head(self) -> list[int]

@head.setter
def head(self, value: Sequence[int]) -> None
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

- 类：`unitree_go::msg::dds_::LowState_`
- 字段类型：`std::array<uint8_t, 2>`
- 声明位置：`include/unitree/idl/go2/LowState_.hpp:30`

**用法**

```python
current_value = obj.head
obj.head = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-lowstate-level-flag"></a>
#### `unitree_sdk2_cpp.idl.go2.LowState.level_flag`

底层 `unitree_go::msg::dds_::LowState_` 的 `level_flag` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def level_flag(self) -> int

@level_flag.setter
def level_flag(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::LowState_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/go2/LowState_.hpp:31`

**用法**

```python
current_value = obj.level_flag
obj.level_flag = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lowstate-frame-reserve"></a>
#### `unitree_sdk2_cpp.idl.go2.LowState.frame_reserve`

底层 `unitree_go::msg::dds_::LowState_` 的 `frame_reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def frame_reserve(self) -> int

@frame_reserve.setter
def frame_reserve(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::LowState_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/go2/LowState_.hpp:32`

**用法**

```python
current_value = obj.frame_reserve
obj.frame_reserve = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lowstate-sn"></a>
#### `unitree_sdk2_cpp.idl.go2.LowState.sn`

底层 `unitree_go::msg::dds_::LowState_` 的 `sn` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 4294967295。

**签名**

```python
@property
def sn(self) -> list[int]

@sn.setter
def sn(self, value: Sequence[int]) -> None
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

- 类：`unitree_go::msg::dds_::LowState_`
- 字段类型：`std::array<uint32_t, 2>`
- 声明位置：`include/unitree/idl/go2/LowState_.hpp:33`

**用法**

```python
current_value = obj.sn
obj.sn = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-lowstate-version"></a>
#### `unitree_sdk2_cpp.idl.go2.LowState.version`

底层 `unitree_go::msg::dds_::LowState_` 的 `version` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 4294967295。

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

- 类：`unitree_go::msg::dds_::LowState_`
- 字段类型：`std::array<uint32_t, 2>`
- 声明位置：`include/unitree/idl/go2/LowState_.hpp:34`

**用法**

```python
current_value = obj.version
obj.version = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-lowstate-bandwidth"></a>
#### `unitree_sdk2_cpp.idl.go2.LowState.bandwidth`

底层 `unitree_go::msg::dds_::LowState_` 的 `bandwidth` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 65535。

**签名**

```python
@property
def bandwidth(self) -> int

@bandwidth.setter
def bandwidth(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::LowState_`
- 字段类型：`uint16_t`
- 声明位置：`include/unitree/idl/go2/LowState_.hpp:35`

**用法**

```python
current_value = obj.bandwidth
obj.bandwidth = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lowstate-imu-state"></a>
#### `unitree_sdk2_cpp.idl.go2.LowState.imu_state`

底层 `unitree_go::msg::dds_::LowState_` 的 `imu_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

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

- 类：`unitree_go::msg::dds_::LowState_`
- 字段类型：`::unitree_go::msg::dds_::IMUState_`
- 声明位置：`include/unitree/idl/go2/LowState_.hpp:36`

**用法**

```python
current_value = obj.imu_state
obj.imu_state = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lowstate-motor-state"></a>
#### `unitree_sdk2_cpp.idl.go2.LowState.motor_state`

底层 `unitree_go::msg::dds_::LowState_` 的 `motor_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 20 个元素

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

- 类：`unitree_go::msg::dds_::LowState_`
- 字段类型：`std::array< ::unitree_go::msg::dds_::MotorState_, 20>`
- 声明位置：`include/unitree/idl/go2/LowState_.hpp:37`

**用法**

```python
current_value = obj.motor_state
obj.motor_state = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-lowstate-bms-state"></a>
#### `unitree_sdk2_cpp.idl.go2.LowState.bms_state`

底层 `unitree_go::msg::dds_::LowState_` 的 `bms_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def bms_state(self) -> BmsState

@bms_state.setter
def bms_state(self, value: BmsState) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `BmsState` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `BmsState` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_go::msg::dds_::LowState_`
- 字段类型：`::unitree_go::msg::dds_::BmsState_`
- 声明位置：`include/unitree/idl/go2/LowState_.hpp:38`

**用法**

```python
current_value = obj.bms_state
obj.bms_state = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lowstate-foot-force"></a>
#### `unitree_sdk2_cpp.idl.go2.LowState.foot_force`

底层 `unitree_go::msg::dds_::LowState_` 的 `foot_force` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：取值范围为 -32768 到 32767。

**签名**

```python
@property
def foot_force(self) -> list[int]

@foot_force.setter
def foot_force(self, value: Sequence[int]) -> None
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

- 类：`unitree_go::msg::dds_::LowState_`
- 字段类型：`std::array<int16_t, 4>`
- 声明位置：`include/unitree/idl/go2/LowState_.hpp:39`

**用法**

```python
current_value = obj.foot_force
obj.foot_force = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-lowstate-foot-force-est"></a>
#### `unitree_sdk2_cpp.idl.go2.LowState.foot_force_est`

底层 `unitree_go::msg::dds_::LowState_` 的 `foot_force_est` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：取值范围为 -32768 到 32767。

**签名**

```python
@property
def foot_force_est(self) -> list[int]

@foot_force_est.setter
def foot_force_est(self, value: Sequence[int]) -> None
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

- 类：`unitree_go::msg::dds_::LowState_`
- 字段类型：`std::array<int16_t, 4>`
- 声明位置：`include/unitree/idl/go2/LowState_.hpp:40`

**用法**

```python
current_value = obj.foot_force_est
obj.foot_force_est = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-lowstate-tick"></a>
#### `unitree_sdk2_cpp.idl.go2.LowState.tick`

底层 `unitree_go::msg::dds_::LowState_` 的 `tick` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

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

- 类：`unitree_go::msg::dds_::LowState_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/go2/LowState_.hpp:41`

**用法**

```python
current_value = obj.tick
obj.tick = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lowstate-wireless-remote"></a>
#### `unitree_sdk2_cpp.idl.go2.LowState.wireless_remote`

底层 `unitree_go::msg::dds_::LowState_` 的 `wireless_remote` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 40 个元素；元素约束：取值范围为 0 到 255。

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

- 类：`unitree_go::msg::dds_::LowState_`
- 字段类型：`std::array<uint8_t, 40>`
- 声明位置：`include/unitree/idl/go2/LowState_.hpp:42`

**用法**

```python
current_value = obj.wireless_remote
obj.wireless_remote = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-lowstate-bit-flag"></a>
#### `unitree_sdk2_cpp.idl.go2.LowState.bit_flag`

底层 `unitree_go::msg::dds_::LowState_` 的 `bit_flag` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def bit_flag(self) -> int

@bit_flag.setter
def bit_flag(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::LowState_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/go2/LowState_.hpp:43`

**用法**

```python
current_value = obj.bit_flag
obj.bit_flag = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lowstate-adc-reel"></a>
#### `unitree_sdk2_cpp.idl.go2.LowState.adc_reel`

底层 `unitree_go::msg::dds_::LowState_` 的 `adc_reel` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def adc_reel(self) -> float

@adc_reel.setter
def adc_reel(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::LowState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/LowState_.hpp:44`

**用法**

```python
current_value = obj.adc_reel
obj.adc_reel = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lowstate-temperature-ntc1"></a>
#### `unitree_sdk2_cpp.idl.go2.LowState.temperature_ntc1`

底层 `unitree_go::msg::dds_::LowState_` 的 `temperature_ntc1` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def temperature_ntc1(self) -> int

@temperature_ntc1.setter
def temperature_ntc1(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::LowState_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/go2/LowState_.hpp:45`

**用法**

```python
current_value = obj.temperature_ntc1
obj.temperature_ntc1 = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lowstate-temperature-ntc2"></a>
#### `unitree_sdk2_cpp.idl.go2.LowState.temperature_ntc2`

底层 `unitree_go::msg::dds_::LowState_` 的 `temperature_ntc2` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def temperature_ntc2(self) -> int

@temperature_ntc2.setter
def temperature_ntc2(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::LowState_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/go2/LowState_.hpp:46`

**用法**

```python
current_value = obj.temperature_ntc2
obj.temperature_ntc2 = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lowstate-power-v"></a>
#### `unitree_sdk2_cpp.idl.go2.LowState.power_v`

底层 `unitree_go::msg::dds_::LowState_` 的 `power_v` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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

- 类：`unitree_go::msg::dds_::LowState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/LowState_.hpp:47`

**用法**

```python
current_value = obj.power_v
obj.power_v = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lowstate-power-a"></a>
#### `unitree_sdk2_cpp.idl.go2.LowState.power_a`

底层 `unitree_go::msg::dds_::LowState_` 的 `power_a` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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

- 类：`unitree_go::msg::dds_::LowState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/LowState_.hpp:48`

**用法**

```python
current_value = obj.power_a
obj.power_a = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lowstate-fan-frequency"></a>
#### `unitree_sdk2_cpp.idl.go2.LowState.fan_frequency`

底层 `unitree_go::msg::dds_::LowState_` 的 `fan_frequency` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：取值范围为 0 到 65535。

**签名**

```python
@property
def fan_frequency(self) -> list[int]

@fan_frequency.setter
def fan_frequency(self, value: Sequence[int]) -> None
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

- 类：`unitree_go::msg::dds_::LowState_`
- 字段类型：`std::array<uint16_t, 4>`
- 声明位置：`include/unitree/idl/go2/LowState_.hpp:49`

**用法**

```python
current_value = obj.fan_frequency
obj.fan_frequency = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-lowstate-reserve"></a>
#### `unitree_sdk2_cpp.idl.go2.LowState.reserve`

底层 `unitree_go::msg::dds_::LowState_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

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

- 类：`unitree_go::msg::dds_::LowState_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/go2/LowState_.hpp:50`

**用法**

```python
current_value = obj.reserve
obj.reserve = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-lowstate-crc"></a>
#### `unitree_sdk2_cpp.idl.go2.LowState.crc`

底层 `unitree_go::msg::dds_::LowState_` 的 `crc` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

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

- 类：`unitree_go::msg::dds_::LowState_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/go2/LowState_.hpp:51`

**用法**

```python
current_value = obj.crc
obj.crc = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-motorcmds"></a>
### `unitree_sdk2_cpp.idl.go2.MotorCmds`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.go2 import MotorCmds
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-go2-motorcmds-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-go2-motorcmds-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-go2-motorcmds-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`cmds`](#unitree-sdk2-cpp-idl-go2-motorcmds-cmds) | `list[MotorCmd]` | `Sequence[MotorCmd]` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-go2-motorcmds-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.go2.MotorCmds.__init__`

初始化 `MotorCmds` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree_go::msg::dds_::MotorCmds_`
- 签名：`MotorCmds_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/go2/MotorCmds_.hpp:28`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = MotorCmds()
```

<a id="unitree-sdk2-cpp-idl-go2-motorcmds-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.go2.MotorCmds.__eq__`

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

- 类：`unitree_go::msg::dds_::MotorCmds_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-go2-motorcmds-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.go2.MotorCmds.__ne__`

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

- 类：`unitree_go::msg::dds_::MotorCmds_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-go2-motorcmds-cmds"></a>
#### `unitree_sdk2_cpp.idl.go2.MotorCmds.cmds`

底层 `unitree_go::msg::dds_::MotorCmds_` 的 `cmds` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector

**签名**

```python
@property
def cmds(self) -> list[MotorCmd]

@cmds.setter
def cmds(self, value: Sequence[MotorCmd]) -> None
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

- 类：`unitree_go::msg::dds_::MotorCmds_`
- 字段类型：`std::vector< ::unitree_go::msg::dds_::MotorCmd_>`
- 声明位置：`include/unitree/idl/go2/MotorCmds_.hpp:25`

**用法**

```python
current_value = obj.cmds
obj.cmds = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-motorstates"></a>
### `unitree_sdk2_cpp.idl.go2.MotorStates`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.go2 import MotorStates
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-go2-motorstates-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-go2-motorstates-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-go2-motorstates-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`states`](#unitree-sdk2-cpp-idl-go2-motorstates-states) | `list[MotorState]` | `Sequence[MotorState]` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-go2-motorstates-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.go2.MotorStates.__init__`

初始化 `MotorStates` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree_go::msg::dds_::MotorStates_`
- 签名：`MotorStates_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/go2/MotorStates_.hpp:28`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = MotorStates()
```

<a id="unitree-sdk2-cpp-idl-go2-motorstates-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.go2.MotorStates.__eq__`

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

- 类：`unitree_go::msg::dds_::MotorStates_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-go2-motorstates-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.go2.MotorStates.__ne__`

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

- 类：`unitree_go::msg::dds_::MotorStates_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-go2-motorstates-states"></a>
#### `unitree_sdk2_cpp.idl.go2.MotorStates.states`

底层 `unitree_go::msg::dds_::MotorStates_` 的 `states` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector

**签名**

```python
@property
def states(self) -> list[MotorState]

@states.setter
def states(self, value: Sequence[MotorState]) -> None
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

- 类：`unitree_go::msg::dds_::MotorStates_`
- 字段类型：`std::vector< ::unitree_go::msg::dds_::MotorState_>`
- 声明位置：`include/unitree/idl/go2/MotorStates_.hpp:25`

**用法**

```python
current_value = obj.states
obj.states = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-pathpoint"></a>
### `unitree_sdk2_cpp.idl.go2.PathPoint`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.go2 import PathPoint
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-go2-pathpoint-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-go2-pathpoint-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-go2-pathpoint-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`t_from_start`](#unitree-sdk2-cpp-idl-go2-pathpoint-t-from-start) | `float` | `float` | `AVAILABLE` |
| [`x`](#unitree-sdk2-cpp-idl-go2-pathpoint-x) | `float` | `float` | `AVAILABLE` |
| [`y`](#unitree-sdk2-cpp-idl-go2-pathpoint-y) | `float` | `float` | `AVAILABLE` |
| [`yaw`](#unitree-sdk2-cpp-idl-go2-pathpoint-yaw) | `float` | `float` | `AVAILABLE` |
| [`vx`](#unitree-sdk2-cpp-idl-go2-pathpoint-vx) | `float` | `float` | `AVAILABLE` |
| [`vy`](#unitree-sdk2-cpp-idl-go2-pathpoint-vy) | `float` | `float` | `AVAILABLE` |
| [`vyaw`](#unitree-sdk2-cpp-idl-go2-pathpoint-vyaw) | `float` | `float` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-go2-pathpoint-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.go2.PathPoint.__init__`

初始化 `PathPoint` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree_go::msg::dds_::PathPoint_`
- 签名：`PathPoint_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/go2/PathPoint_.hpp:31`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = PathPoint()
```

<a id="unitree-sdk2-cpp-idl-go2-pathpoint-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.go2.PathPoint.__eq__`

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

- 类：`unitree_go::msg::dds_::PathPoint_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-go2-pathpoint-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.go2.PathPoint.__ne__`

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

- 类：`unitree_go::msg::dds_::PathPoint_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-go2-pathpoint-t-from-start"></a>
#### `unitree_sdk2_cpp.idl.go2.PathPoint.t_from_start`

底层 `unitree_go::msg::dds_::PathPoint_` 的 `t_from_start` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def t_from_start(self) -> float

@t_from_start.setter
def t_from_start(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::PathPoint_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/PathPoint_.hpp:22`

**用法**

```python
current_value = obj.t_from_start
obj.t_from_start = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-pathpoint-x"></a>
#### `unitree_sdk2_cpp.idl.go2.PathPoint.x`

底层 `unitree_go::msg::dds_::PathPoint_` 的 `x` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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

- 类：`unitree_go::msg::dds_::PathPoint_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/PathPoint_.hpp:23`

**用法**

```python
current_value = obj.x
obj.x = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-pathpoint-y"></a>
#### `unitree_sdk2_cpp.idl.go2.PathPoint.y`

底层 `unitree_go::msg::dds_::PathPoint_` 的 `y` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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

- 类：`unitree_go::msg::dds_::PathPoint_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/PathPoint_.hpp:24`

**用法**

```python
current_value = obj.y
obj.y = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-pathpoint-yaw"></a>
#### `unitree_sdk2_cpp.idl.go2.PathPoint.yaw`

底层 `unitree_go::msg::dds_::PathPoint_` 的 `yaw` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def yaw(self) -> float

@yaw.setter
def yaw(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::PathPoint_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/PathPoint_.hpp:25`

**用法**

```python
current_value = obj.yaw
obj.yaw = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-pathpoint-vx"></a>
#### `unitree_sdk2_cpp.idl.go2.PathPoint.vx`

底层 `unitree_go::msg::dds_::PathPoint_` 的 `vx` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def vx(self) -> float

@vx.setter
def vx(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::PathPoint_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/PathPoint_.hpp:26`

**用法**

```python
current_value = obj.vx
obj.vx = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-pathpoint-vy"></a>
#### `unitree_sdk2_cpp.idl.go2.PathPoint.vy`

底层 `unitree_go::msg::dds_::PathPoint_` 的 `vy` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def vy(self) -> float

@vy.setter
def vy(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::PathPoint_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/PathPoint_.hpp:27`

**用法**

```python
current_value = obj.vy
obj.vy = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-pathpoint-vyaw"></a>
#### `unitree_sdk2_cpp.idl.go2.PathPoint.vyaw`

底层 `unitree_go::msg::dds_::PathPoint_` 的 `vyaw` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def vyaw(self) -> float

@vyaw.setter
def vyaw(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::PathPoint_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/PathPoint_.hpp:28`

**用法**

```python
current_value = obj.vyaw
obj.vyaw = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-req"></a>
### `unitree_sdk2_cpp.idl.go2.Req`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.go2 import Req
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-go2-req-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-go2-req-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-go2-req-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`uuid`](#unitree-sdk2-cpp-idl-go2-req-uuid) | `str` | `str` | `AVAILABLE` |
| [`body`](#unitree-sdk2-cpp-idl-go2-req-body) | `str` | `str` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-go2-req-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.go2.Req.__init__`

初始化 `Req` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree_go::msg::dds_::Req_`
- 签名：`Req_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/go2/Req_.hpp:27`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = Req()
```

<a id="unitree-sdk2-cpp-idl-go2-req-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.go2.Req.__eq__`

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

- 类：`unitree_go::msg::dds_::Req_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-go2-req-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.go2.Req.__ne__`

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

- 类：`unitree_go::msg::dds_::Req_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-go2-req-uuid"></a>
#### `unitree_sdk2_cpp.idl.go2.Req.uuid`

底层 `unitree_go::msg::dds_::Req_` 的 `uuid` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

**签名**

```python
@property
def uuid(self) -> str

@uuid.setter
def uuid(self, value: str) -> None
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

- 类：`unitree_go::msg::dds_::Req_`
- 字段类型：`std::string`
- 声明位置：`include/unitree/idl/go2/Req_.hpp:23`

**用法**

```python
current_value = obj.uuid
obj.uuid = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-req-body"></a>
#### `unitree_sdk2_cpp.idl.go2.Req.body`

底层 `unitree_go::msg::dds_::Req_` 的 `body` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

**签名**

```python
@property
def body(self) -> str

@body.setter
def body(self, value: str) -> None
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

- 类：`unitree_go::msg::dds_::Req_`
- 字段类型：`std::string`
- 声明位置：`include/unitree/idl/go2/Req_.hpp:24`

**用法**

```python
current_value = obj.body
obj.body = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-res"></a>
### `unitree_sdk2_cpp.idl.go2.Res`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.go2 import Res
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-go2-res-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-go2-res-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-go2-res-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`uuid`](#unitree-sdk2-cpp-idl-go2-res-uuid) | `str` | `str` | `AVAILABLE` |
| [`data`](#unitree-sdk2-cpp-idl-go2-res-data) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`body`](#unitree-sdk2-cpp-idl-go2-res-body) | `str` | `str` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-go2-res-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.go2.Res.__init__`

初始化 `Res` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree_go::msg::dds_::Res_`
- 签名：`Res_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/go2/Res_.hpp:30`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = Res()
```

<a id="unitree-sdk2-cpp-idl-go2-res-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.go2.Res.__eq__`

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

- 类：`unitree_go::msg::dds_::Res_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-go2-res-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.go2.Res.__ne__`

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

- 类：`unitree_go::msg::dds_::Res_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-go2-res-uuid"></a>
#### `unitree_sdk2_cpp.idl.go2.Res.uuid`

底层 `unitree_go::msg::dds_::Res_` 的 `uuid` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

**签名**

```python
@property
def uuid(self) -> str

@uuid.setter
def uuid(self, value: str) -> None
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

- 类：`unitree_go::msg::dds_::Res_`
- 字段类型：`std::string`
- 声明位置：`include/unitree/idl/go2/Res_.hpp:25`

**用法**

```python
current_value = obj.uuid
obj.uuid = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-res-data"></a>
#### `unitree_sdk2_cpp.idl.go2.Res.data`

底层 `unitree_go::msg::dds_::Res_` 的 `data` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector；元素约束：取值范围为 0 到 255。

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

- 类：`unitree_go::msg::dds_::Res_`
- 字段类型：`std::vector<uint8_t>`
- 声明位置：`include/unitree/idl/go2/Res_.hpp:26`

**用法**

```python
current_value = obj.data
obj.data = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-res-body"></a>
#### `unitree_sdk2_cpp.idl.go2.Res.body`

底层 `unitree_go::msg::dds_::Res_` 的 `body` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

**签名**

```python
@property
def body(self) -> str

@body.setter
def body(self, value: str) -> None
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

- 类：`unitree_go::msg::dds_::Res_`
- 字段类型：`std::string`
- 声明位置：`include/unitree/idl/go2/Res_.hpp:27`

**用法**

```python
current_value = obj.body
obj.body = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-sportmodecmd"></a>
### `unitree_sdk2_cpp.idl.go2.SportModeCmd`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.go2 import SportModeCmd
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-go2-sportmodecmd-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-go2-sportmodecmd-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-go2-sportmodecmd-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`mode`](#unitree-sdk2-cpp-idl-go2-sportmodecmd-mode) | `int` | `int` | `AVAILABLE` |
| [`gait_type`](#unitree-sdk2-cpp-idl-go2-sportmodecmd-gait-type) | `int` | `int` | `AVAILABLE` |
| [`speed_level`](#unitree-sdk2-cpp-idl-go2-sportmodecmd-speed-level) | `int` | `int` | `AVAILABLE` |
| [`foot_raise_height`](#unitree-sdk2-cpp-idl-go2-sportmodecmd-foot-raise-height) | `float` | `float` | `AVAILABLE` |
| [`body_height`](#unitree-sdk2-cpp-idl-go2-sportmodecmd-body-height) | `float` | `float` | `AVAILABLE` |
| [`position`](#unitree-sdk2-cpp-idl-go2-sportmodecmd-position) | `list[float]` | `Sequence[float]` | `AVAILABLE` |
| [`euler`](#unitree-sdk2-cpp-idl-go2-sportmodecmd-euler) | `list[float]` | `Sequence[float]` | `AVAILABLE` |
| [`velocity`](#unitree-sdk2-cpp-idl-go2-sportmodecmd-velocity) | `list[float]` | `Sequence[float]` | `AVAILABLE` |
| [`yaw_speed`](#unitree-sdk2-cpp-idl-go2-sportmodecmd-yaw-speed) | `float` | `float` | `AVAILABLE` |
| [`bms_cmd`](#unitree-sdk2-cpp-idl-go2-sportmodecmd-bms-cmd) | `BmsCmd` | `BmsCmd` | `AVAILABLE` |
| [`path_point`](#unitree-sdk2-cpp-idl-go2-sportmodecmd-path-point) | `list[PathPoint]` | `Sequence[PathPoint]` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-go2-sportmodecmd-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.go2.SportModeCmd.__init__`

初始化 `SportModeCmd` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree_go::msg::dds_::SportModeCmd_`
- 签名：`SportModeCmd_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/go2/SportModeCmd_.hpp:41`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = SportModeCmd()
```

<a id="unitree-sdk2-cpp-idl-go2-sportmodecmd-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.go2.SportModeCmd.__eq__`

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

- 类：`unitree_go::msg::dds_::SportModeCmd_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-go2-sportmodecmd-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.go2.SportModeCmd.__ne__`

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

- 类：`unitree_go::msg::dds_::SportModeCmd_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-go2-sportmodecmd-mode"></a>
#### `unitree_sdk2_cpp.idl.go2.SportModeCmd.mode`

底层 `unitree_go::msg::dds_::SportModeCmd_` 的 `mode` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

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

- 类：`unitree_go::msg::dds_::SportModeCmd_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/go2/SportModeCmd_.hpp:28`

**用法**

```python
current_value = obj.mode
obj.mode = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-sportmodecmd-gait-type"></a>
#### `unitree_sdk2_cpp.idl.go2.SportModeCmd.gait_type`

底层 `unitree_go::msg::dds_::SportModeCmd_` 的 `gait_type` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def gait_type(self) -> int

@gait_type.setter
def gait_type(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::SportModeCmd_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/go2/SportModeCmd_.hpp:29`

**用法**

```python
current_value = obj.gait_type
obj.gait_type = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-sportmodecmd-speed-level"></a>
#### `unitree_sdk2_cpp.idl.go2.SportModeCmd.speed_level`

底层 `unitree_go::msg::dds_::SportModeCmd_` 的 `speed_level` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def speed_level(self) -> int

@speed_level.setter
def speed_level(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::SportModeCmd_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/go2/SportModeCmd_.hpp:30`

**用法**

```python
current_value = obj.speed_level
obj.speed_level = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-sportmodecmd-foot-raise-height"></a>
#### `unitree_sdk2_cpp.idl.go2.SportModeCmd.foot_raise_height`

底层 `unitree_go::msg::dds_::SportModeCmd_` 的 `foot_raise_height` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def foot_raise_height(self) -> float

@foot_raise_height.setter
def foot_raise_height(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::SportModeCmd_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/SportModeCmd_.hpp:31`

**用法**

```python
current_value = obj.foot_raise_height
obj.foot_raise_height = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-sportmodecmd-body-height"></a>
#### `unitree_sdk2_cpp.idl.go2.SportModeCmd.body_height`

底层 `unitree_go::msg::dds_::SportModeCmd_` 的 `body_height` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def body_height(self) -> float

@body_height.setter
def body_height(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::SportModeCmd_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/SportModeCmd_.hpp:32`

**用法**

```python
current_value = obj.body_height
obj.body_height = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-sportmodecmd-position"></a>
#### `unitree_sdk2_cpp.idl.go2.SportModeCmd.position`

底层 `unitree_go::msg::dds_::SportModeCmd_` 的 `position` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def position(self) -> list[float]

@position.setter
def position(self, value: Sequence[float]) -> None
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

- 类：`unitree_go::msg::dds_::SportModeCmd_`
- 字段类型：`std::array<float, 2>`
- 声明位置：`include/unitree/idl/go2/SportModeCmd_.hpp:33`

**用法**

```python
current_value = obj.position
obj.position = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-sportmodecmd-euler"></a>
#### `unitree_sdk2_cpp.idl.go2.SportModeCmd.euler`

底层 `unitree_go::msg::dds_::SportModeCmd_` 的 `euler` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def euler(self) -> list[float]

@euler.setter
def euler(self, value: Sequence[float]) -> None
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

- 类：`unitree_go::msg::dds_::SportModeCmd_`
- 字段类型：`std::array<float, 3>`
- 声明位置：`include/unitree/idl/go2/SportModeCmd_.hpp:34`

**用法**

```python
current_value = obj.euler
obj.euler = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-sportmodecmd-velocity"></a>
#### `unitree_sdk2_cpp.idl.go2.SportModeCmd.velocity`

底层 `unitree_go::msg::dds_::SportModeCmd_` 的 `velocity` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def velocity(self) -> list[float]

@velocity.setter
def velocity(self, value: Sequence[float]) -> None
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

- 类：`unitree_go::msg::dds_::SportModeCmd_`
- 字段类型：`std::array<float, 2>`
- 声明位置：`include/unitree/idl/go2/SportModeCmd_.hpp:35`

**用法**

```python
current_value = obj.velocity
obj.velocity = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-sportmodecmd-yaw-speed"></a>
#### `unitree_sdk2_cpp.idl.go2.SportModeCmd.yaw_speed`

底层 `unitree_go::msg::dds_::SportModeCmd_` 的 `yaw_speed` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def yaw_speed(self) -> float

@yaw_speed.setter
def yaw_speed(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::SportModeCmd_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/SportModeCmd_.hpp:36`

**用法**

```python
current_value = obj.yaw_speed
obj.yaw_speed = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-sportmodecmd-bms-cmd"></a>
#### `unitree_sdk2_cpp.idl.go2.SportModeCmd.bms_cmd`

底层 `unitree_go::msg::dds_::SportModeCmd_` 的 `bms_cmd` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def bms_cmd(self) -> BmsCmd

@bms_cmd.setter
def bms_cmd(self, value: BmsCmd) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `BmsCmd` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `BmsCmd` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_go::msg::dds_::SportModeCmd_`
- 字段类型：`::unitree_go::msg::dds_::BmsCmd_`
- 声明位置：`include/unitree/idl/go2/SportModeCmd_.hpp:37`

**用法**

```python
current_value = obj.bms_cmd
obj.bms_cmd = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-sportmodecmd-path-point"></a>
#### `unitree_sdk2_cpp.idl.go2.SportModeCmd.path_point`

底层 `unitree_go::msg::dds_::SportModeCmd_` 的 `path_point` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 30 个元素

**签名**

```python
@property
def path_point(self) -> list[PathPoint]

@path_point.setter
def path_point(self, value: Sequence[PathPoint]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[PathPoint]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[PathPoint]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_go::msg::dds_::SportModeCmd_`
- 字段类型：`std::array< ::unitree_go::msg::dds_::PathPoint_, 30>`
- 声明位置：`include/unitree/idl/go2/SportModeCmd_.hpp:38`

**用法**

```python
current_value = obj.path_point
obj.path_point = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-timespec"></a>
### `unitree_sdk2_cpp.idl.go2.TimeSpec`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.go2 import TimeSpec
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-go2-timespec-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-go2-timespec-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-go2-timespec-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`sec`](#unitree-sdk2-cpp-idl-go2-timespec-sec) | `int` | `int` | `AVAILABLE` |
| [`nanosec`](#unitree-sdk2-cpp-idl-go2-timespec-nanosec) | `int` | `int` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-go2-timespec-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.go2.TimeSpec.__init__`

初始化 `TimeSpec` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree_go::msg::dds_::TimeSpec_`
- 签名：`TimeSpec_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/go2/TimeSpec_.hpp:27`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = TimeSpec()
```

<a id="unitree-sdk2-cpp-idl-go2-timespec-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.go2.TimeSpec.__eq__`

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

- 类：`unitree_go::msg::dds_::TimeSpec_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-go2-timespec-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.go2.TimeSpec.__ne__`

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

- 类：`unitree_go::msg::dds_::TimeSpec_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-go2-timespec-sec"></a>
#### `unitree_sdk2_cpp.idl.go2.TimeSpec.sec`

底层 `unitree_go::msg::dds_::TimeSpec_` 的 `sec` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 -2147483648 到 2147483647。

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

- 类：`unitree_go::msg::dds_::TimeSpec_`
- 字段类型：`int32_t`
- 声明位置：`include/unitree/idl/go2/TimeSpec_.hpp:23`

**用法**

```python
current_value = obj.sec
obj.sec = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-timespec-nanosec"></a>
#### `unitree_sdk2_cpp.idl.go2.TimeSpec.nanosec`

底层 `unitree_go::msg::dds_::TimeSpec_` 的 `nanosec` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

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

- 类：`unitree_go::msg::dds_::TimeSpec_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/go2/TimeSpec_.hpp:24`

**用法**

```python
current_value = obj.nanosec
obj.nanosec = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-sportmodestate"></a>
### `unitree_sdk2_cpp.idl.go2.SportModeState`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.go2 import SportModeState
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-go2-sportmodestate-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-go2-sportmodestate-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-go2-sportmodestate-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`stamp`](#unitree-sdk2-cpp-idl-go2-sportmodestate-stamp) | `TimeSpec` | `TimeSpec` | `AVAILABLE` |
| [`error_code`](#unitree-sdk2-cpp-idl-go2-sportmodestate-error-code) | `int` | `int` | `AVAILABLE` |
| [`imu_state`](#unitree-sdk2-cpp-idl-go2-sportmodestate-imu-state) | `IMUState` | `IMUState` | `AVAILABLE` |
| [`mode`](#unitree-sdk2-cpp-idl-go2-sportmodestate-mode) | `int` | `int` | `AVAILABLE` |
| [`progress`](#unitree-sdk2-cpp-idl-go2-sportmodestate-progress) | `float` | `float` | `AVAILABLE` |
| [`gait_type`](#unitree-sdk2-cpp-idl-go2-sportmodestate-gait-type) | `int` | `int` | `AVAILABLE` |
| [`foot_raise_height`](#unitree-sdk2-cpp-idl-go2-sportmodestate-foot-raise-height) | `float` | `float` | `AVAILABLE` |
| [`position`](#unitree-sdk2-cpp-idl-go2-sportmodestate-position) | `list[float]` | `Sequence[float]` | `AVAILABLE` |
| [`body_height`](#unitree-sdk2-cpp-idl-go2-sportmodestate-body-height) | `float` | `float` | `AVAILABLE` |
| [`velocity`](#unitree-sdk2-cpp-idl-go2-sportmodestate-velocity) | `list[float]` | `Sequence[float]` | `AVAILABLE` |
| [`yaw_speed`](#unitree-sdk2-cpp-idl-go2-sportmodestate-yaw-speed) | `float` | `float` | `AVAILABLE` |
| [`range_obstacle`](#unitree-sdk2-cpp-idl-go2-sportmodestate-range-obstacle) | `list[float]` | `Sequence[float]` | `AVAILABLE` |
| [`foot_force`](#unitree-sdk2-cpp-idl-go2-sportmodestate-foot-force) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`foot_position_body`](#unitree-sdk2-cpp-idl-go2-sportmodestate-foot-position-body) | `list[float]` | `Sequence[float]` | `AVAILABLE` |
| [`foot_speed_body`](#unitree-sdk2-cpp-idl-go2-sportmodestate-foot-speed-body) | `list[float]` | `Sequence[float]` | `AVAILABLE` |
| [`path_point`](#unitree-sdk2-cpp-idl-go2-sportmodestate-path-point) | `list[PathPoint]` | `Sequence[PathPoint]` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-go2-sportmodestate-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.go2.SportModeState.__init__`

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

- 类：`unitree_go::msg::dds_::SportModeState_`
- 签名：`SportModeState_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/go2/SportModeState_.hpp:48`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = SportModeState()
```

<a id="unitree-sdk2-cpp-idl-go2-sportmodestate-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.go2.SportModeState.__eq__`

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

- 类：`unitree_go::msg::dds_::SportModeState_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-go2-sportmodestate-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.go2.SportModeState.__ne__`

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

- 类：`unitree_go::msg::dds_::SportModeState_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-go2-sportmodestate-stamp"></a>
#### `unitree_sdk2_cpp.idl.go2.SportModeState.stamp`

底层 `unitree_go::msg::dds_::SportModeState_` 的 `stamp` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

**签名**

```python
@property
def stamp(self) -> TimeSpec

@stamp.setter
def stamp(self, value: TimeSpec) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `TimeSpec` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `TimeSpec` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_go::msg::dds_::SportModeState_`
- 字段类型：`::unitree_go::msg::dds_::TimeSpec_`
- 声明位置：`include/unitree/idl/go2/SportModeState_.hpp:30`

**用法**

```python
current_value = obj.stamp
obj.stamp = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-sportmodestate-error-code"></a>
#### `unitree_sdk2_cpp.idl.go2.SportModeState.error_code`

底层 `unitree_go::msg::dds_::SportModeState_` 的 `error_code` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

**签名**

```python
@property
def error_code(self) -> int

@error_code.setter
def error_code(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::SportModeState_`
- 字段类型：`uint32_t`
- 声明位置：`include/unitree/idl/go2/SportModeState_.hpp:31`

**用法**

```python
current_value = obj.error_code
obj.error_code = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-sportmodestate-imu-state"></a>
#### `unitree_sdk2_cpp.idl.go2.SportModeState.imu_state`

底层 `unitree_go::msg::dds_::SportModeState_` 的 `imu_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

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

- 类：`unitree_go::msg::dds_::SportModeState_`
- 字段类型：`::unitree_go::msg::dds_::IMUState_`
- 声明位置：`include/unitree/idl/go2/SportModeState_.hpp:32`

**用法**

```python
current_value = obj.imu_state
obj.imu_state = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-sportmodestate-mode"></a>
#### `unitree_sdk2_cpp.idl.go2.SportModeState.mode`

底层 `unitree_go::msg::dds_::SportModeState_` 的 `mode` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

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

- 类：`unitree_go::msg::dds_::SportModeState_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/go2/SportModeState_.hpp:33`

**用法**

```python
current_value = obj.mode
obj.mode = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-sportmodestate-progress"></a>
#### `unitree_sdk2_cpp.idl.go2.SportModeState.progress`

底层 `unitree_go::msg::dds_::SportModeState_` 的 `progress` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def progress(self) -> float

@progress.setter
def progress(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::SportModeState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/SportModeState_.hpp:34`

**用法**

```python
current_value = obj.progress
obj.progress = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-sportmodestate-gait-type"></a>
#### `unitree_sdk2_cpp.idl.go2.SportModeState.gait_type`

底层 `unitree_go::msg::dds_::SportModeState_` 的 `gait_type` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def gait_type(self) -> int

@gait_type.setter
def gait_type(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::SportModeState_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/go2/SportModeState_.hpp:35`

**用法**

```python
current_value = obj.gait_type
obj.gait_type = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-sportmodestate-foot-raise-height"></a>
#### `unitree_sdk2_cpp.idl.go2.SportModeState.foot_raise_height`

底层 `unitree_go::msg::dds_::SportModeState_` 的 `foot_raise_height` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def foot_raise_height(self) -> float

@foot_raise_height.setter
def foot_raise_height(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::SportModeState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/SportModeState_.hpp:36`

**用法**

```python
current_value = obj.foot_raise_height
obj.foot_raise_height = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-sportmodestate-position"></a>
#### `unitree_sdk2_cpp.idl.go2.SportModeState.position`

底层 `unitree_go::msg::dds_::SportModeState_` 的 `position` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def position(self) -> list[float]

@position.setter
def position(self, value: Sequence[float]) -> None
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

- 类：`unitree_go::msg::dds_::SportModeState_`
- 字段类型：`std::array<float, 3>`
- 声明位置：`include/unitree/idl/go2/SportModeState_.hpp:37`

**用法**

```python
current_value = obj.position
obj.position = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-sportmodestate-body-height"></a>
#### `unitree_sdk2_cpp.idl.go2.SportModeState.body_height`

底层 `unitree_go::msg::dds_::SportModeState_` 的 `body_height` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def body_height(self) -> float

@body_height.setter
def body_height(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::SportModeState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/SportModeState_.hpp:38`

**用法**

```python
current_value = obj.body_height
obj.body_height = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-sportmodestate-velocity"></a>
#### `unitree_sdk2_cpp.idl.go2.SportModeState.velocity`

底层 `unitree_go::msg::dds_::SportModeState_` 的 `velocity` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def velocity(self) -> list[float]

@velocity.setter
def velocity(self, value: Sequence[float]) -> None
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

- 类：`unitree_go::msg::dds_::SportModeState_`
- 字段类型：`std::array<float, 3>`
- 声明位置：`include/unitree/idl/go2/SportModeState_.hpp:39`

**用法**

```python
current_value = obj.velocity
obj.velocity = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-sportmodestate-yaw-speed"></a>
#### `unitree_sdk2_cpp.idl.go2.SportModeState.yaw_speed`

底层 `unitree_go::msg::dds_::SportModeState_` 的 `yaw_speed` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def yaw_speed(self) -> float

@yaw_speed.setter
def yaw_speed(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::SportModeState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/SportModeState_.hpp:40`

**用法**

```python
current_value = obj.yaw_speed
obj.yaw_speed = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-sportmodestate-range-obstacle"></a>
#### `unitree_sdk2_cpp.idl.go2.SportModeState.range_obstacle`

底层 `unitree_go::msg::dds_::SportModeState_` 的 `range_obstacle` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def range_obstacle(self) -> list[float]

@range_obstacle.setter
def range_obstacle(self, value: Sequence[float]) -> None
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

- 类：`unitree_go::msg::dds_::SportModeState_`
- 字段类型：`std::array<float, 4>`
- 声明位置：`include/unitree/idl/go2/SportModeState_.hpp:41`

**用法**

```python
current_value = obj.range_obstacle
obj.range_obstacle = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-sportmodestate-foot-force"></a>
#### `unitree_sdk2_cpp.idl.go2.SportModeState.foot_force`

底层 `unitree_go::msg::dds_::SportModeState_` 的 `foot_force` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：取值范围为 -32768 到 32767。

**签名**

```python
@property
def foot_force(self) -> list[int]

@foot_force.setter
def foot_force(self, value: Sequence[int]) -> None
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

- 类：`unitree_go::msg::dds_::SportModeState_`
- 字段类型：`std::array<int16_t, 4>`
- 声明位置：`include/unitree/idl/go2/SportModeState_.hpp:42`

**用法**

```python
current_value = obj.foot_force
obj.foot_force = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-sportmodestate-foot-position-body"></a>
#### `unitree_sdk2_cpp.idl.go2.SportModeState.foot_position_body`

底层 `unitree_go::msg::dds_::SportModeState_` 的 `foot_position_body` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 12 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def foot_position_body(self) -> list[float]

@foot_position_body.setter
def foot_position_body(self, value: Sequence[float]) -> None
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

- 类：`unitree_go::msg::dds_::SportModeState_`
- 字段类型：`std::array<float, 12>`
- 声明位置：`include/unitree/idl/go2/SportModeState_.hpp:43`

**用法**

```python
current_value = obj.foot_position_body
obj.foot_position_body = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-sportmodestate-foot-speed-body"></a>
#### `unitree_sdk2_cpp.idl.go2.SportModeState.foot_speed_body`

底层 `unitree_go::msg::dds_::SportModeState_` 的 `foot_speed_body` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 12 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def foot_speed_body(self) -> list[float]

@foot_speed_body.setter
def foot_speed_body(self, value: Sequence[float]) -> None
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

- 类：`unitree_go::msg::dds_::SportModeState_`
- 字段类型：`std::array<float, 12>`
- 声明位置：`include/unitree/idl/go2/SportModeState_.hpp:44`

**用法**

```python
current_value = obj.foot_speed_body
obj.foot_speed_body = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-sportmodestate-path-point"></a>
#### `unitree_sdk2_cpp.idl.go2.SportModeState.path_point`

底层 `unitree_go::msg::dds_::SportModeState_` 的 `path_point` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 10 个元素

**签名**

```python
@property
def path_point(self) -> list[PathPoint]

@path_point.setter
def path_point(self, value: Sequence[PathPoint]) -> None
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 含义 |
| --- | --- | --- |
| `value` | `Sequence[PathPoint]` | 要写入或传递的新值，必须符合该参数的 Python 类型以及底层 C++ 范围约束。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| getter 返回值 | `list[PathPoint]` | 返回属性当前值。数组、vector 和嵌套消息采用复制语义。 |

**对应 C++**

- 类：`unitree_go::msg::dds_::SportModeState_`
- 字段类型：`std::array< ::unitree_go::msg::dds_::PathPoint_, 10>`
- 声明位置：`include/unitree/idl/go2/SportModeState_.hpp:45`

**用法**

```python
current_value = obj.path_point
obj.path_point = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-uwbstate"></a>
### `unitree_sdk2_cpp.idl.go2.UwbState`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.go2 import UwbState
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-go2-uwbstate-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-go2-uwbstate-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-go2-uwbstate-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`version`](#unitree-sdk2-cpp-idl-go2-uwbstate-version) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`channel`](#unitree-sdk2-cpp-idl-go2-uwbstate-channel) | `int` | `int` | `AVAILABLE` |
| [`joy_mode`](#unitree-sdk2-cpp-idl-go2-uwbstate-joy-mode) | `int` | `int` | `AVAILABLE` |
| [`orientation_est`](#unitree-sdk2-cpp-idl-go2-uwbstate-orientation-est) | `float` | `float` | `AVAILABLE` |
| [`pitch_est`](#unitree-sdk2-cpp-idl-go2-uwbstate-pitch-est) | `float` | `float` | `AVAILABLE` |
| [`distance_est`](#unitree-sdk2-cpp-idl-go2-uwbstate-distance-est) | `float` | `float` | `AVAILABLE` |
| [`yaw_est`](#unitree-sdk2-cpp-idl-go2-uwbstate-yaw-est) | `float` | `float` | `AVAILABLE` |
| [`tag_roll`](#unitree-sdk2-cpp-idl-go2-uwbstate-tag-roll) | `float` | `float` | `AVAILABLE` |
| [`tag_pitch`](#unitree-sdk2-cpp-idl-go2-uwbstate-tag-pitch) | `float` | `float` | `AVAILABLE` |
| [`tag_yaw`](#unitree-sdk2-cpp-idl-go2-uwbstate-tag-yaw) | `float` | `float` | `AVAILABLE` |
| [`base_roll`](#unitree-sdk2-cpp-idl-go2-uwbstate-base-roll) | `float` | `float` | `AVAILABLE` |
| [`base_pitch`](#unitree-sdk2-cpp-idl-go2-uwbstate-base-pitch) | `float` | `float` | `AVAILABLE` |
| [`base_yaw`](#unitree-sdk2-cpp-idl-go2-uwbstate-base-yaw) | `float` | `float` | `AVAILABLE` |
| [`joystick`](#unitree-sdk2-cpp-idl-go2-uwbstate-joystick) | `list[float]` | `Sequence[float]` | `AVAILABLE` |
| [`error_state`](#unitree-sdk2-cpp-idl-go2-uwbstate-error-state) | `int` | `int` | `AVAILABLE` |
| [`buttons`](#unitree-sdk2-cpp-idl-go2-uwbstate-buttons) | `int` | `int` | `AVAILABLE` |
| [`enabled_from_app`](#unitree-sdk2-cpp-idl-go2-uwbstate-enabled-from-app) | `int` | `int` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-go2-uwbstate-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.go2.UwbState.__init__`

初始化 `UwbState` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree_go::msg::dds_::UwbState_`
- 签名：`UwbState_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/go2/UwbState_.hpp:43`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = UwbState()
```

<a id="unitree-sdk2-cpp-idl-go2-uwbstate-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.go2.UwbState.__eq__`

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

- 类：`unitree_go::msg::dds_::UwbState_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-go2-uwbstate-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.go2.UwbState.__ne__`

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

- 类：`unitree_go::msg::dds_::UwbState_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-go2-uwbstate-version"></a>
#### `unitree_sdk2_cpp.idl.go2.UwbState.version`

底层 `unitree_go::msg::dds_::UwbState_` 的 `version` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 255。

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

- 类：`unitree_go::msg::dds_::UwbState_`
- 字段类型：`std::array<uint8_t, 2>`
- 声明位置：`include/unitree/idl/go2/UwbState_.hpp:24`

**用法**

```python
current_value = obj.version
obj.version = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-uwbstate-channel"></a>
#### `unitree_sdk2_cpp.idl.go2.UwbState.channel`

底层 `unitree_go::msg::dds_::UwbState_` 的 `channel` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def channel(self) -> int

@channel.setter
def channel(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::UwbState_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/go2/UwbState_.hpp:25`

**用法**

```python
current_value = obj.channel
obj.channel = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-uwbstate-joy-mode"></a>
#### `unitree_sdk2_cpp.idl.go2.UwbState.joy_mode`

底层 `unitree_go::msg::dds_::UwbState_` 的 `joy_mode` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def joy_mode(self) -> int

@joy_mode.setter
def joy_mode(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::UwbState_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/go2/UwbState_.hpp:26`

**用法**

```python
current_value = obj.joy_mode
obj.joy_mode = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-uwbstate-orientation-est"></a>
#### `unitree_sdk2_cpp.idl.go2.UwbState.orientation_est`

底层 `unitree_go::msg::dds_::UwbState_` 的 `orientation_est` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def orientation_est(self) -> float

@orientation_est.setter
def orientation_est(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::UwbState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/UwbState_.hpp:27`

**用法**

```python
current_value = obj.orientation_est
obj.orientation_est = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-uwbstate-pitch-est"></a>
#### `unitree_sdk2_cpp.idl.go2.UwbState.pitch_est`

底层 `unitree_go::msg::dds_::UwbState_` 的 `pitch_est` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def pitch_est(self) -> float

@pitch_est.setter
def pitch_est(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::UwbState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/UwbState_.hpp:28`

**用法**

```python
current_value = obj.pitch_est
obj.pitch_est = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-uwbstate-distance-est"></a>
#### `unitree_sdk2_cpp.idl.go2.UwbState.distance_est`

底层 `unitree_go::msg::dds_::UwbState_` 的 `distance_est` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def distance_est(self) -> float

@distance_est.setter
def distance_est(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::UwbState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/UwbState_.hpp:29`

**用法**

```python
current_value = obj.distance_est
obj.distance_est = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-uwbstate-yaw-est"></a>
#### `unitree_sdk2_cpp.idl.go2.UwbState.yaw_est`

底层 `unitree_go::msg::dds_::UwbState_` 的 `yaw_est` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def yaw_est(self) -> float

@yaw_est.setter
def yaw_est(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::UwbState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/UwbState_.hpp:30`

**用法**

```python
current_value = obj.yaw_est
obj.yaw_est = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-uwbstate-tag-roll"></a>
#### `unitree_sdk2_cpp.idl.go2.UwbState.tag_roll`

底层 `unitree_go::msg::dds_::UwbState_` 的 `tag_roll` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def tag_roll(self) -> float

@tag_roll.setter
def tag_roll(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::UwbState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/UwbState_.hpp:31`

**用法**

```python
current_value = obj.tag_roll
obj.tag_roll = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-uwbstate-tag-pitch"></a>
#### `unitree_sdk2_cpp.idl.go2.UwbState.tag_pitch`

底层 `unitree_go::msg::dds_::UwbState_` 的 `tag_pitch` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def tag_pitch(self) -> float

@tag_pitch.setter
def tag_pitch(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::UwbState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/UwbState_.hpp:32`

**用法**

```python
current_value = obj.tag_pitch
obj.tag_pitch = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-uwbstate-tag-yaw"></a>
#### `unitree_sdk2_cpp.idl.go2.UwbState.tag_yaw`

底层 `unitree_go::msg::dds_::UwbState_` 的 `tag_yaw` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def tag_yaw(self) -> float

@tag_yaw.setter
def tag_yaw(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::UwbState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/UwbState_.hpp:33`

**用法**

```python
current_value = obj.tag_yaw
obj.tag_yaw = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-uwbstate-base-roll"></a>
#### `unitree_sdk2_cpp.idl.go2.UwbState.base_roll`

底层 `unitree_go::msg::dds_::UwbState_` 的 `base_roll` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def base_roll(self) -> float

@base_roll.setter
def base_roll(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::UwbState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/UwbState_.hpp:34`

**用法**

```python
current_value = obj.base_roll
obj.base_roll = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-uwbstate-base-pitch"></a>
#### `unitree_sdk2_cpp.idl.go2.UwbState.base_pitch`

底层 `unitree_go::msg::dds_::UwbState_` 的 `base_pitch` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def base_pitch(self) -> float

@base_pitch.setter
def base_pitch(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::UwbState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/UwbState_.hpp:35`

**用法**

```python
current_value = obj.base_pitch
obj.base_pitch = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-uwbstate-base-yaw"></a>
#### `unitree_sdk2_cpp.idl.go2.UwbState.base_yaw`

底层 `unitree_go::msg::dds_::UwbState_` 的 `base_yaw` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def base_yaw(self) -> float

@base_yaw.setter
def base_yaw(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::UwbState_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/UwbState_.hpp:36`

**用法**

```python
current_value = obj.base_yaw
obj.base_yaw = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-uwbstate-joystick"></a>
#### `unitree_sdk2_cpp.idl.go2.UwbState.joystick`

底层 `unitree_go::msg::dds_::UwbState_` 的 `joystick` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def joystick(self) -> list[float]

@joystick.setter
def joystick(self, value: Sequence[float]) -> None
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

- 类：`unitree_go::msg::dds_::UwbState_`
- 字段类型：`std::array<float, 2>`
- 声明位置：`include/unitree/idl/go2/UwbState_.hpp:37`

**用法**

```python
current_value = obj.joystick
obj.joystick = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-uwbstate-error-state"></a>
#### `unitree_sdk2_cpp.idl.go2.UwbState.error_state`

底层 `unitree_go::msg::dds_::UwbState_` 的 `error_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def error_state(self) -> int

@error_state.setter
def error_state(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::UwbState_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/go2/UwbState_.hpp:38`

**用法**

```python
current_value = obj.error_state
obj.error_state = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-uwbstate-buttons"></a>
#### `unitree_sdk2_cpp.idl.go2.UwbState.buttons`

底层 `unitree_go::msg::dds_::UwbState_` 的 `buttons` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def buttons(self) -> int

@buttons.setter
def buttons(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::UwbState_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/go2/UwbState_.hpp:39`

**用法**

```python
current_value = obj.buttons
obj.buttons = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-uwbstate-enabled-from-app"></a>
#### `unitree_sdk2_cpp.idl.go2.UwbState.enabled_from_app`

底层 `unitree_go::msg::dds_::UwbState_` 的 `enabled_from_app` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def enabled_from_app(self) -> int

@enabled_from_app.setter
def enabled_from_app(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::UwbState_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/go2/UwbState_.hpp:40`

**用法**

```python
current_value = obj.enabled_from_app
obj.enabled_from_app = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-uwbswitch"></a>
### `unitree_sdk2_cpp.idl.go2.UwbSwitch`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.go2 import UwbSwitch
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-go2-uwbswitch-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-go2-uwbswitch-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-go2-uwbswitch-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`enabled`](#unitree-sdk2-cpp-idl-go2-uwbswitch-enabled) | `int` | `int` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-go2-uwbswitch-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.go2.UwbSwitch.__init__`

初始化 `UwbSwitch` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree_go::msg::dds_::UwbSwitch_`
- 签名：`UwbSwitch_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/go2/UwbSwitch_.hpp:26`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = UwbSwitch()
```

<a id="unitree-sdk2-cpp-idl-go2-uwbswitch-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.go2.UwbSwitch.__eq__`

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

- 类：`unitree_go::msg::dds_::UwbSwitch_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-go2-uwbswitch-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.go2.UwbSwitch.__ne__`

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

- 类：`unitree_go::msg::dds_::UwbSwitch_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-go2-uwbswitch-enabled"></a>
#### `unitree_sdk2_cpp.idl.go2.UwbSwitch.enabled`

底层 `unitree_go::msg::dds_::UwbSwitch_` 的 `enabled` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

**签名**

```python
@property
def enabled(self) -> int

@enabled.setter
def enabled(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::UwbSwitch_`
- 字段类型：`uint8_t`
- 声明位置：`include/unitree/idl/go2/UwbSwitch_.hpp:23`

**用法**

```python
current_value = obj.enabled
obj.enabled = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-voxelmapcompressed"></a>
### `unitree_sdk2_cpp.idl.go2.VoxelMapCompressed`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.go2 import VoxelMapCompressed
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-go2-voxelmapcompressed-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-go2-voxelmapcompressed-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-go2-voxelmapcompressed-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`stamp`](#unitree-sdk2-cpp-idl-go2-voxelmapcompressed-stamp) | `float` | `float` | `AVAILABLE` |
| [`frame_id`](#unitree-sdk2-cpp-idl-go2-voxelmapcompressed-frame-id) | `str` | `str` | `AVAILABLE` |
| [`resolution`](#unitree-sdk2-cpp-idl-go2-voxelmapcompressed-resolution) | `float` | `float` | `AVAILABLE` |
| [`origin`](#unitree-sdk2-cpp-idl-go2-voxelmapcompressed-origin) | `list[float]` | `Sequence[float]` | `AVAILABLE` |
| [`width`](#unitree-sdk2-cpp-idl-go2-voxelmapcompressed-width) | `list[int]` | `Sequence[int]` | `AVAILABLE` |
| [`src_size`](#unitree-sdk2-cpp-idl-go2-voxelmapcompressed-src-size) | `int` | `int` | `AVAILABLE` |
| [`data`](#unitree-sdk2-cpp-idl-go2-voxelmapcompressed-data) | `list[int]` | `Sequence[int]` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-go2-voxelmapcompressed-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.go2.VoxelMapCompressed.__init__`

初始化 `VoxelMapCompressed` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree_go::msg::dds_::VoxelMapCompressed_`
- 签名：`VoxelMapCompressed_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/go2/VoxelMapCompressed_.hpp:35`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = VoxelMapCompressed()
```

<a id="unitree-sdk2-cpp-idl-go2-voxelmapcompressed-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.go2.VoxelMapCompressed.__eq__`

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

- 类：`unitree_go::msg::dds_::VoxelMapCompressed_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-go2-voxelmapcompressed-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.go2.VoxelMapCompressed.__ne__`

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

- 类：`unitree_go::msg::dds_::VoxelMapCompressed_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-go2-voxelmapcompressed-stamp"></a>
#### `unitree_sdk2_cpp.idl.go2.VoxelMapCompressed.stamp`

底层 `unitree_go::msg::dds_::VoxelMapCompressed_` 的 `stamp` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def stamp(self) -> float

@stamp.setter
def stamp(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::VoxelMapCompressed_`
- 字段类型：`double`
- 声明位置：`include/unitree/idl/go2/VoxelMapCompressed_.hpp:26`

**用法**

```python
current_value = obj.stamp
obj.stamp = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-voxelmapcompressed-frame-id"></a>
#### `unitree_sdk2_cpp.idl.go2.VoxelMapCompressed.frame_id`

底层 `unitree_go::msg::dds_::VoxelMapCompressed_` 的 `frame_id` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

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

- 类：`unitree_go::msg::dds_::VoxelMapCompressed_`
- 字段类型：`std::string`
- 声明位置：`include/unitree/idl/go2/VoxelMapCompressed_.hpp:27`

**用法**

```python
current_value = obj.frame_id
obj.frame_id = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-voxelmapcompressed-resolution"></a>
#### `unitree_sdk2_cpp.idl.go2.VoxelMapCompressed.resolution`

底层 `unitree_go::msg::dds_::VoxelMapCompressed_` 的 `resolution` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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

- 类：`unitree_go::msg::dds_::VoxelMapCompressed_`
- 字段类型：`double`
- 声明位置：`include/unitree/idl/go2/VoxelMapCompressed_.hpp:28`

**用法**

```python
current_value = obj.resolution
obj.resolution = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-voxelmapcompressed-origin"></a>
#### `unitree_sdk2_cpp.idl.go2.VoxelMapCompressed.origin`

底层 `unitree_go::msg::dds_::VoxelMapCompressed_` 的 `origin` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def origin(self) -> list[float]

@origin.setter
def origin(self, value: Sequence[float]) -> None
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

- 类：`unitree_go::msg::dds_::VoxelMapCompressed_`
- 字段类型：`std::array<double, 3>`
- 声明位置：`include/unitree/idl/go2/VoxelMapCompressed_.hpp:29`

**用法**

```python
current_value = obj.origin
obj.origin = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-voxelmapcompressed-width"></a>
#### `unitree_sdk2_cpp.idl.go2.VoxelMapCompressed.width`

底层 `unitree_go::msg::dds_::VoxelMapCompressed_` 的 `width` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：取值范围为 0 到 65535。

**签名**

```python
@property
def width(self) -> list[int]

@width.setter
def width(self, value: Sequence[int]) -> None
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

- 类：`unitree_go::msg::dds_::VoxelMapCompressed_`
- 字段类型：`std::array<uint16_t, 3>`
- 声明位置：`include/unitree/idl/go2/VoxelMapCompressed_.hpp:30`

**用法**

```python
current_value = obj.width
obj.width = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-voxelmapcompressed-src-size"></a>
#### `unitree_sdk2_cpp.idl.go2.VoxelMapCompressed.src_size`

底层 `unitree_go::msg::dds_::VoxelMapCompressed_` 的 `src_size` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 18446744073709551615。

**签名**

```python
@property
def src_size(self) -> int

@src_size.setter
def src_size(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::VoxelMapCompressed_`
- 字段类型：`uint64_t`
- 声明位置：`include/unitree/idl/go2/VoxelMapCompressed_.hpp:31`

**用法**

```python
current_value = obj.src_size
obj.src_size = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-voxelmapcompressed-data"></a>
#### `unitree_sdk2_cpp.idl.go2.VoxelMapCompressed.data`

底层 `unitree_go::msg::dds_::VoxelMapCompressed_` 的 `data` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector；元素约束：取值范围为 0 到 255。

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

- 类：`unitree_go::msg::dds_::VoxelMapCompressed_`
- 字段类型：`std::vector<uint8_t>`
- 声明位置：`include/unitree/idl/go2/VoxelMapCompressed_.hpp:32`

**用法**

```python
current_value = obj.data
obj.data = new_value
```

> [!TIP]
> 读取容器或嵌套值后应遵循“读取、修改、重新赋值”。只修改 getter 返回的副本不会可靠地更新原 C++ 消息。

<a id="unitree-sdk2-cpp-idl-go2-wirelesscontroller"></a>
### `unitree_sdk2_cpp.idl.go2.WirelessController`

可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

**导入**

```python
from unitree_sdk2_cpp.idl.go2 import WirelessController
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`__init__`](#unitree-sdk2-cpp-idl-go2-wirelesscontroller-dunder-init-1) | `def __init__(self) -> None` | `AVAILABLE` | `VALUE_TYPE` |
| [`__eq__`](#unitree-sdk2-cpp-idl-go2-wirelesscontroller-dunder-eq-1) | `def __eq__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`__ne__`](#unitree-sdk2-cpp-idl-go2-wirelesscontroller-dunder-ne-1) | `def __ne__(self, other: object) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

**属性索引**

| 属性 | 读取类型 | 写入类型 | 状态 |
| --- | --- | --- | --- |
| [`lx`](#unitree-sdk2-cpp-idl-go2-wirelesscontroller-lx) | `float` | `float` | `AVAILABLE` |
| [`ly`](#unitree-sdk2-cpp-idl-go2-wirelesscontroller-ly) | `float` | `float` | `AVAILABLE` |
| [`rx`](#unitree-sdk2-cpp-idl-go2-wirelesscontroller-rx) | `float` | `float` | `AVAILABLE` |
| [`ry`](#unitree-sdk2-cpp-idl-go2-wirelesscontroller-ry) | `float` | `float` | `AVAILABLE` |
| [`keys`](#unitree-sdk2-cpp-idl-go2-wirelesscontroller-keys) | `int` | `int` | `AVAILABLE` |

<a id="unitree-sdk2-cpp-idl-go2-wirelesscontroller-dunder-init-1"></a>
#### `unitree_sdk2_cpp.idl.go2.WirelessController.__init__`

初始化 `WirelessController` 实例。是否能实际构造取决于下方可用性状态。

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

- 类：`unitree_go::msg::dds_::WirelessController_`
- 签名：`WirelessController_()`
- 绑定策略：`未单独标注`
- 声明位置：`include/unitree/idl/go2/WirelessController_.hpp:30`

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
value = WirelessController()
```

<a id="unitree-sdk2-cpp-idl-go2-wirelesscontroller-dunder-eq-1"></a>
#### `unitree_sdk2_cpp.idl.go2.WirelessController.__eq__`

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

- 类：`unitree_go::msg::dds_::WirelessController_`
- 签名：`operator==(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
same = left == right
```

<a id="unitree-sdk2-cpp-idl-go2-wirelesscontroller-dunder-ne-1"></a>
#### `unitree_sdk2_cpp.idl.go2.WirelessController.__ne__`

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

- 类：`unitree_go::msg::dds_::WirelessController_`
- 签名：`operator!=(const value &) const`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
different = left != right
```

<a id="unitree-sdk2-cpp-idl-go2-wirelesscontroller-lx"></a>
#### `unitree_sdk2_cpp.idl.go2.WirelessController.lx`

底层 `unitree_go::msg::dds_::WirelessController_` 的 `lx` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def lx(self) -> float

@lx.setter
def lx(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::WirelessController_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/WirelessController_.hpp:23`

**用法**

```python
current_value = obj.lx
obj.lx = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-wirelesscontroller-ly"></a>
#### `unitree_sdk2_cpp.idl.go2.WirelessController.ly`

底层 `unitree_go::msg::dds_::WirelessController_` 的 `ly` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def ly(self) -> float

@ly.setter
def ly(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::WirelessController_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/WirelessController_.hpp:24`

**用法**

```python
current_value = obj.ly
obj.ly = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-wirelesscontroller-rx"></a>
#### `unitree_sdk2_cpp.idl.go2.WirelessController.rx`

底层 `unitree_go::msg::dds_::WirelessController_` 的 `rx` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def rx(self) -> float

@rx.setter
def rx(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::WirelessController_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/WirelessController_.hpp:25`

**用法**

```python
current_value = obj.rx
obj.rx = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-wirelesscontroller-ry"></a>
#### `unitree_sdk2_cpp.idl.go2.WirelessController.ry`

底层 `unitree_go::msg::dds_::WirelessController_` 的 `ry` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

**签名**

```python
@property
def ry(self) -> float

@ry.setter
def ry(self, value: float) -> None
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

- 类：`unitree_go::msg::dds_::WirelessController_`
- 字段类型：`float`
- 声明位置：`include/unitree/idl/go2/WirelessController_.hpp:26`

**用法**

```python
current_value = obj.ry
obj.ry = new_value
```

<a id="unitree-sdk2-cpp-idl-go2-wirelesscontroller-keys"></a>
#### `unitree_sdk2_cpp.idl.go2.WirelessController.keys`

底层 `unitree_go::msg::dds_::WirelessController_` 的 `keys` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 65535。

**签名**

```python
@property
def keys(self) -> int

@keys.setter
def keys(self, value: int) -> None
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

- 类：`unitree_go::msg::dds_::WirelessController_`
- 字段类型：`uint16_t`
- 声明位置：`include/unitree/idl/go2/WirelessController_.hpp:27`

**用法**

```python
current_value = obj.keys
obj.keys = new_value
```

---

[返回 API 总索引](../API_REFERENCE_ZH.md)
