# Unitree SDK2 Python API 参考分卷

[返回 API 总索引](../API_REFERENCE_ZH.md) · [阅读从零开始指南](../BEGINNER_GUIDE_ZH.md)

> [!WARNING]
> 本分卷同时包含 `AVAILABLE` 和 `SIGNATURE_ONLY`。后者只是设计期类型签名。运动及硬件副作用方法即使标记为 `AVAILABLE`，也不表示当前环境可安全执行。

> [!NOTE]
> 本文件由 `generator/generate_api_docs.py` 自动生成，请勿手工维护 API 条目。

---

<a id="unitree-sdk2-cpp-idl-g1"></a>
## unitree_sdk2_cpp.idl.g1

模块：`unitree_sdk2_cpp.idl.g1`

### 模块函数导入

```python
from unitree_sdk2_cpp.idl.g1 import compute_crc, compute_crc, update_crc, validate_crc, validate_crc
```

下面的函数用法片段假设已经完成上述导入。

### 模块函数索引

| 函数 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`compute_crc()`](#unitree-sdk2-cpp-idl-g1-compute-crc-1) | `def compute_crc(message: LowCmd) -> int` | `AVAILABLE` | `VALUE_TYPE` |
| [`compute_crc()`](#unitree-sdk2-cpp-idl-g1-compute-crc-1) | `def compute_crc(message: LowState) -> int` | `AVAILABLE` | `VALUE_TYPE` |
| [`update_crc()`](#unitree-sdk2-cpp-idl-g1-update-crc-1) | `def update_crc(message: LowCmd) -> int` | `AVAILABLE` | `VALUE_TYPE` |
| [`validate_crc()`](#unitree-sdk2-cpp-idl-g1-validate-crc-1) | `def validate_crc(message: LowCmd) -> bool` | `AVAILABLE` | `VALUE_TYPE` |
| [`validate_crc()`](#unitree-sdk2-cpp-idl-g1-validate-crc-1) | `def validate_crc(message: LowState) -> bool` | `AVAILABLE` | `VALUE_TYPE` |

<a id="unitree-sdk2-cpp-idl-g1-compute-crc-1"></a>
#### `unitree_sdk2_cpp.idl.g1.compute_crc`（重载 1/2）

对应 C++ SDK 操作 `crc32_core(LowCmd_)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
@overload
def compute_crc(message: LowCmd) -> int
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `message` | `LowCmd` | 必填 | 要写入 DDS 的消息实例；类型必须与 Publisher 构造时声明的消息类完全一致。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | 返回 `int`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::LowCmd_`
- 签名：`crc32_core(LowCmd_)`
- 绑定策略：`CRC_WRAPPER`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = compute_crc(message=message)
```

<a id="unitree-sdk2-cpp-idl-g1-compute-crc-2"></a>
#### `unitree_sdk2_cpp.idl.g1.compute_crc`（重载 2/2）

对应 C++ SDK 操作 `crc32_core(LowState_)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
@overload
def compute_crc(message: LowState) -> int
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `message` | `LowState` | 必填 | 要写入 DDS 的消息实例；类型必须与 Publisher 构造时声明的消息类完全一致。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | 返回 `int`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::LowState_`
- 签名：`crc32_core(LowState_)`
- 绑定策略：`CRC_WRAPPER`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = compute_crc(message=message)
```

<a id="unitree-sdk2-cpp-idl-g1-update-crc-1"></a>
#### `unitree_sdk2_cpp.idl.g1.update_crc`

对应 C++ SDK 操作 `crc32_core(LowCmd_); LowCmd_::crc(uint32_t)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
def update_crc(message: LowCmd) -> int
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `message` | `LowCmd` | 必填 | 要写入 DDS 的消息实例；类型必须与 Publisher 构造时声明的消息类完全一致。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | 返回 `int`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::LowCmd_`
- 签名：`crc32_core(LowCmd_); LowCmd_::crc(uint32_t)`
- 绑定策略：`CRC_WRAPPER`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = update_crc(message=message)
```

<a id="unitree-sdk2-cpp-idl-g1-validate-crc-1"></a>
#### `unitree_sdk2_cpp.idl.g1.validate_crc`（重载 1/2）

对应 C++ SDK 操作 `LowCmd_::crc() == crc32_core(LowCmd_)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
@overload
def validate_crc(message: LowCmd) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `message` | `LowCmd` | 必填 | 要写入 DDS 的消息实例；类型必须与 Publisher 构造时声明的消息类完全一致。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::LowCmd_`
- 签名：`LowCmd_::crc() == crc32_core(LowCmd_)`
- 绑定策略：`CRC_WRAPPER`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = validate_crc(message=message)
```

<a id="unitree-sdk2-cpp-idl-g1-validate-crc-2"></a>
#### `unitree_sdk2_cpp.idl.g1.validate_crc`（重载 2/2）

对应 C++ SDK 操作 `LowState_::crc() == crc32_core(LowState_)`。上游头文件没有可直接生成的业务说明时，本参考只保证签名映射，精确语义需查目标型号协议。

**签名**

```python
@overload
def validate_crc(message: LowState) -> bool
```

**可用性与安全性**

**`AVAILABLE` / `VALUE_TYPE`**：当前绑定源码已实现该消息值操作。

**参数**

| 名称 | Python 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `message` | `LowState` | 必填 | 要写入 DDS 的消息实例；类型必须与 Publisher 构造时声明的消息类完全一致。 |

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `bool` | 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。 |

**对应 C++**

- 类：`unitree_hg::msg::dds_::LowState_`
- 签名：`LowState_::crc() == crc32_core(LowState_)`
- 绑定策略：`CRC_WRAPPER`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
result = validate_crc(message=message)
```

---

[返回 API 总索引](../API_REFERENCE_ZH.md)
