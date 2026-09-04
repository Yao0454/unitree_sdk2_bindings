# Unitree SDK2 Python API 参考分卷

[返回 API 总索引](../API_REFERENCE_ZH.md) · [阅读从零开始指南](../BEGINNER_GUIDE_ZH.md)

> [!WARNING]
> 本分卷同时包含 `AVAILABLE` 和 `SIGNATURE_ONLY`。后者只是设计期类型签名。运动及硬件副作用方法即使标记为 `AVAILABLE`，也不表示当前环境可安全执行。

> [!NOTE]
> 本文件由 `generator/generate_api_docs.py` 自动生成，请勿手工维护 API 条目。

---

<a id="unitree-sdk2-cpp"></a>
## 系统辅助 API

模块：`unitree_sdk2_cpp`

### 类索引

| 类 | 公开函数签名 | 属性 |
| --- | ---: | ---: |
| [`OsHelper`](#unitree-sdk2-cpp-oshelper) | 7 | 0 |

<a id="unitree-sdk2-cpp-oshelper"></a>
### `unitree_sdk2_cpp.OsHelper`

读取当前主机操作系统信息的单例辅助类。

**导入**

```python
from unitree_sdk2_cpp import OsHelper
```

**方法索引**

| 方法 | Python 签名 | 状态 | 安全分类 |
| --- | --- | --- | --- |
| [`instance`](#unitree-sdk2-cpp-oshelper-instance-1) | `def instance() -> OsHelper` | `AVAILABLE` | `READ_ONLY` |
| [`get_uid`](#unitree-sdk2-cpp-oshelper-get-uid-1) | `def get_uid(self) -> int` | `AVAILABLE` | `READ_ONLY` |
| [`get_gid`](#unitree-sdk2-cpp-oshelper-get-gid-1) | `def get_gid(self) -> int` | `AVAILABLE` | `READ_ONLY` |
| [`get_user`](#unitree-sdk2-cpp-oshelper-get-user-1) | `def get_user(self) -> str` | `AVAILABLE` | `READ_ONLY` |
| [`get_processor_number`](#unitree-sdk2-cpp-oshelper-get-processor-number-1) | `def get_processor_number(self) -> int` | `AVAILABLE` | `READ_ONLY` |
| [`get_page_size`](#unitree-sdk2-cpp-oshelper-get-page-size-1) | `def get_page_size(self) -> int` | `AVAILABLE` | `READ_ONLY` |
| [`get_hostname`](#unitree-sdk2-cpp-oshelper-get-hostname-1) | `def get_hostname(self) -> str` | `AVAILABLE` | `READ_ONLY` |

<a id="unitree-sdk2-cpp-oshelper-instance-1"></a>
#### `unitree_sdk2_cpp.OsHelper.instance`

返回进程内的 `OsHelper` 单例。

**签名**

```python
@staticmethod
def instance() -> OsHelper
```

**可用性与安全性**

**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现本机信息读取。该方法不初始化 DDS，也不访问机器人。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `OsHelper` | 进程内的 `OsHelper` 单例。 |

**对应 C++**

- 类：`unitree_sdk2_cpp.OsHelper`
- 签名：`OsHelper::Instance()`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
helper = OsHelper.instance()
```

<a id="unitree-sdk2-cpp-oshelper-get-uid-1"></a>
#### `unitree_sdk2_cpp.OsHelper.get_uid`

返回当前进程用户的 Unix UID。

**签名**

```python
def get_uid(self) -> int
```

**可用性与安全性**

**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现本机信息读取。该方法不初始化 DDS，也不访问机器人。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | 当前进程用户的 Unix UID。 |

**对应 C++**

- 类：`unitree_sdk2_cpp.OsHelper`
- 签名：`OsHelper::GetUID()`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
uid = helper.get_uid()
```

<a id="unitree-sdk2-cpp-oshelper-get-gid-1"></a>
#### `unitree_sdk2_cpp.OsHelper.get_gid`

返回当前进程用户的 Unix GID。

**签名**

```python
def get_gid(self) -> int
```

**可用性与安全性**

**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现本机信息读取。该方法不初始化 DDS，也不访问机器人。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | 当前进程用户的 Unix GID。 |

**对应 C++**

- 类：`unitree_sdk2_cpp.OsHelper`
- 签名：`OsHelper::GetGID()`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
gid = helper.get_gid()
```

<a id="unitree-sdk2-cpp-oshelper-get-user-1"></a>
#### `unitree_sdk2_cpp.OsHelper.get_user`

返回当前进程对应的用户名。

**签名**

```python
def get_user(self) -> str
```

**可用性与安全性**

**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现本机信息读取。该方法不初始化 DDS，也不访问机器人。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `str` | 当前进程对应的用户名。 |

**对应 C++**

- 类：`unitree_sdk2_cpp.OsHelper`
- 签名：`OsHelper::GetUser()`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
user = helper.get_user()
```

<a id="unitree-sdk2-cpp-oshelper-get-processor-number-1"></a>
#### `unitree_sdk2_cpp.OsHelper.get_processor_number`

返回当前主机可见的处理器数量。

**签名**

```python
def get_processor_number(self) -> int
```

**可用性与安全性**

**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现本机信息读取。该方法不初始化 DDS，也不访问机器人。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | 当前主机可见的处理器数量。 |

**对应 C++**

- 类：`unitree_sdk2_cpp.OsHelper`
- 签名：`OsHelper::GetProcessorNumber()`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
processor_count = helper.get_processor_number()
```

<a id="unitree-sdk2-cpp-oshelper-get-page-size-1"></a>
#### `unitree_sdk2_cpp.OsHelper.get_page_size`

返回当前主机的操作系统内存页大小。

**签名**

```python
def get_page_size(self) -> int
```

**可用性与安全性**

**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现本机信息读取。该方法不初始化 DDS，也不访问机器人。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `int` | 操作系统内存页大小，单位为字节。 |

**对应 C++**

- 类：`unitree_sdk2_cpp.OsHelper`
- 签名：`OsHelper::GetPageSize()`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
page_size = helper.get_page_size()
```

<a id="unitree-sdk2-cpp-oshelper-get-hostname-1"></a>
#### `unitree_sdk2_cpp.OsHelper.get_hostname`

返回当前主机名。

**签名**

```python
def get_hostname(self) -> str
```

**可用性与安全性**

**`AVAILABLE` / `READ_ONLY`**：当前绑定源码已实现本机信息读取。该方法不初始化 DDS，也不访问机器人。

**参数**

无显式参数。实例方法中的 `self` 由 Python 自动传入。

**返回值**

| 位置 | 类型 | 含义 |
| --- | --- | --- |
| 返回值 | `str` | 当前主机名。 |

**对应 C++**

- 类：`unitree_sdk2_cpp.OsHelper`
- 签名：`OsHelper::GetHostname()`
- 绑定策略：`未单独标注`
- 声明位置：由 pybind11 手工绑定或生成注册表提供；manifest 未记录独立头文件行号。

**说明**

- 示例是局部调用片段；`obj` 和参数变量表示已经按上层业务校验并准备好的对象。

**用法**

```python
hostname = helper.get_hostname()
```

---

[返回 API 总索引](../API_REFERENCE_ZH.md)
