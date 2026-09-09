# Unitree SDK2 Python bindings

通过 Python 调用 Unitree SDK2 的 C++ 接口，支持 Go2、G1 等机器人 Client 和
带类型提示的 DDS 消息收发。本仓库可以独立克隆到任意目录，**不需要放进
`unitree_sdk2/` 仓库内部**。

| 包                       | 用途                                          | 运行平台                |
| ------------------------ | --------------------------------------------- | ----------------------- |
| `unitree-sdk2-cpp`       | C++ 扩展，Python 中 `import unitree_sdk2_cpp` | Linux x86_64 / aarch64  |
| `unitree-sdk2-cpp-stubs` | 编辑器补全、参数提示、静态类型检查            | Linux / macOS / Windows |

stub 包不包含机器人运行能力。连接机器人需要原生包；两个包应安装到同一个 Python 环境。

## 1. 准备环境

原生包需要 Linux、Python 3.10+、支持 C++17 的编译器及 Python 开发头文件。
SDK 自带的静态库和 CycloneDDS 动态库是 Linux 二进制，不能直接在 macOS 或 Windows 编译使用。

Ubuntu / Debian 可以先安装：

```bash
sudo apt update
sudo apt install -y git build-essential cmake ninja-build python3-dev python3-venv
```

如果系统 Python 低于 3.10，请先通过 Conda 等方式准备 Python 3.10+。
使用 Conda 时可以直接在已激活的环境安装，无需再创建下面的 `.venv`。

## 2. 独立克隆本仓库和 C++ SDK

在你想存放代码的位置执行：

```bash
git clone https://github.com/Yao0454/unitree_sdk2_bindings.git
cd unitree_sdk2_bindings

mkdir -p thirdparty
git clone https://github.com/Yao0454/unitree_sdk2.git thirdparty/unitree_sdk2
git -C thirdparty/unitree_sdk2 checkout d13dc9fdc20a3af7063f2ba03bc7b98c16f4999f
```

上面的 SDK 提交对应当前生成代码所依据的 SDK 文件，固定它能避免头文件与静态库版本混用。
也可以使用官方 SDK 或自己的 checkout，但应保持头文件、`lib/` 和 `thirdparty/` 来自同一版本，
并重新验证接口兼容性。依赖版本说明见 [thirdparty/README.md](thirdparty/README.md)。

目录应当是：

```text
unitree_sdk2_bindings/
├── CMakeLists.txt
├── pyproject.toml
├── src/
├── stubs/
├── examples/
└── thirdparty/
    └── unitree_sdk2/
        ├── include/
        ├── lib/
        │   ├── x86_64/libunitree_sdk2.a
        │   └── aarch64/libunitree_sdk2.a
        └── thirdparty/
            ├── include/
            └── lib/
```

构建使用 SDK 自带的预编译库，**不需要先对 C++ SDK 执行 `make install` 或安装到 `/usr/local`**。

## 3. 编译并安装两个 Python 包

以下命令在 bindings 仓库根目录执行：

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip

# 编译原生扩展，限制并行数以减少内存占用。
CMAKE_BUILD_PARALLEL_LEVEL=2 python -m pip install .
python -m pip install ./stubs
```

pip 会在隔离构建环境中安装 pybind11、scikit-build-core 等构建依赖，第一次构建需要能访问 Python 包源。
普通安装会把结果放入当前 Python 环境，应用程序不再依赖源码目录作为导入路径。
编译进程被系统杀死时，可将并行数改为 `1` 后重试。

使用 uv 的项目，也可以在激活相同环境后执行：

```bash
CMAKE_BUILD_PARALLEL_LEVEL=2 uv pip install .
uv pip install ./stubs
```

### 已有 SDK，不想重复克隆

传入 SDK 的绝对路径即可，bindings 和 SDK 不需要具有特定的父子目录关系：

```bash
CMAKE_BUILD_PARALLEL_LEVEL=2 python -m pip install . \
  -Ccmake.define.UNITREE_SDK_ROOT=/absolute/path/to/unitree_sdk2
```

也支持环境变量：

```bash
UNITREE_SDK_ROOT=/absolute/path/to/unitree_sdk2 python -m pip install .
```

查找顺序为：显式 CMake 参数 → 环境变量 → 本仓库 `thirdparty/unitree_sdk2` → 旧的 SDK 父目录布局。
选中的路径不完整时直接报错，不会悄悄改用另一份 SDK。CMake 会打印实际使用的根目录和架构。
复用手动 CMake 构建目录时，缓存参数优先于环境变量；更换 SDK 请重新传参或使用新构建目录。

### 从其他项目安装

在你的应用虚拟环境中，使用 bindings 仓库的绝对路径：

```bash
python -m pip install /absolute/path/to/unitree_sdk2_bindings
python -m pip install /absolute/path/to/unitree_sdk2_bindings/stubs
```

SDK 会相对 **bindings 源码位置** 查找，而不是相对当前终端目录查找。
安装完成后，无论应用项目叫什么、存在哪里，都可以 `import unitree_sdk2_cpp`。

## 4. 确认安装成功与编辑器设置

先执行不连接机器人、不初始化 DDS 的检查：

```bash
python -c "import unitree_sdk2_cpp as u; print(u.__file__); print(u.OsHelper.instance().get_hostname())"
python -m pip show unitree-sdk2-cpp unitree-sdk2-cpp-stubs
```

第一行应输出 `.so` 文件路径和本机主机名。包内 `.libs/` 存放 CycloneDDS 库，扩展使用
`$ORIGIN/.libs` 查找它们，正常情况下不需要手工设置 `LD_LIBRARY_PATH`。

在 Zed、VS Code 等编辑器中选择**刚才安装这两个包的 Python 解释器**。
终端里激活 `.venv` 不一定会同时切换编辑器的解释器。
0.4.0 stub 安装后由类型检查器从该环境的 `site-packages` 查找，包含中文函数用法提示。
不需要为本包配置 `extraPaths`、`include` 或关闭 `reportMissingModuleSource`；
源码入口在运行时只转交原生扩展，缺少原生扩展时会明确报错。详见 [stub 安装与补全](stubs/README.md)。
识别已导入模块的签名，以及未写 import 就列出第三方库的自动导入候选，是两个功能；
后者还取决于语言服务器的索引设置，安装包无法替编辑器选择环境或开启索引。
只有 stub 时可以写代码，但执行示例仍会缺少原生模块。

## 5. Go2 示例：从只读查询开始

以下命令从 bindings 仓库根目录运行，`eth0` 替换为连接 Go2 的实际网卡名。
可运行 `ip -br addr` 查看 Linux 网卡。网络示例默认使用 DDS domain 0。

| 示例                                                      | 功能                         | 是否修改机器人       |
| --------------------------------------------------------- | ---------------------------- | -------------------- |
| [go2_build_lowcmd.py](examples/go2_build_lowcmd.py)       | 内存中构造消息，学习数组回写 | 不联网               |
| [go2_service_list.py](examples/go2_service_list.py)       | 查询服务列表                 | 只读                 |
| [go2_vui_status.py](examples/go2_vui_status.py)           | 查询语音、音量、亮度         | 只读                 |
| [go2_lowstate_once.py](examples/go2_lowstate_once.py)     | 读取电量、IMU、12 个腿部关节 | 只读                 |
| [go2_state_monitor.py](examples/go2_state_monitor.py)     | 持续订阅运动状态             | 只读                 |
| [go2_camera_snapshot.py](examples/go2_camera_snapshot.py) | 获取 JPEG 并保存到本机       | 读取相机、写本地文件 |
| [go2_vui_set.py](examples/go2_vui_set.py)                 | 设置音量或亮度并回读         | 修改设置             |
| [go2_sport.py](examples/go2_sport.py)                     | 起立、趴下、停止、定时移动   | 控制运动             |

```bash
python examples/go2_build_lowcmd.py
python examples/go2_service_list.py -n eth0
python examples/go2_vui_status.py -n eth0
python examples/go2_lowstate_once.py -n eth0
python examples/go2_state_monitor.py -n eth0 --seconds 10
python examples/go2_camera_snapshot.py -n eth0 -o go2_photo.jpg

# 以下命令修改机器人设置。
python examples/go2_vui_set.py -n eth0 volume 3
python examples/go2_vui_set.py -n eth0 brightness 5
```

运动示例要求明确选择动作；除 `stop` 外，还需输入 `GO2` 确认。
请在空旷平地使用，保留遥控器停止手段，移动前让机器人处于可行走状态。

```bash
python examples/go2_sport.py -n eth0 stand-up
python examples/go2_sport.py -n eth0 move --vx 0.1 --seconds 2
python examples/go2_sport.py -n eth0 stop
```

完整参数和生命周期说明见 [Go2 示例教程](examples/GO2_EXAMPLES_ZH.md)。
示例经过离线类型检查和模拟测试，设备固件支持情况与实际动作效果需要在目标设备验证。

## 6. 开发时怎样使用 API

函数名采用 Python 的 `snake_case`。C++ 的 `ServiceList` 在 Python 中是 `service_list`。
返回 `int` 的 RPC 需检查错误码；带输出参数的 C++ RPC 则返回 `(错误码, 数据)`：

```python
from unitree_sdk2_cpp import channel
from unitree_sdk2_cpp.robot.go2 import RobotStateClient

channel.initialize(0, "eth0")
try:
    client = RobotStateClient()
    client.set_timeout(5.0)
    client.init()
    code, services = client.service_list()
    if code != 0:
        raise RuntimeError(f"查询失败：{code}")
    for service in services:
        print(service.name, service.status)
finally:
    channel.release()
```

数组、列表和嵌套对象使用复制语义。修改关节时，先取出列表，修改后再把整个列表赋回字段；
不要假定 `message.motor_cmd[0].q = ...` 会修改原始消息。
订阅回调应快速复制所需字段，业务数据可用不可变 `dataclass`；先关闭订阅/发布器，再释放 DDS。

当前类型清单包含 1213 条目：1167 个 `AVAILABLE`、46 个 `SIGNATURE_ONLY`。
`AVAILABLE` 表示绑定存在，不表示命令已在你的机器人上验证；`SIGNATURE_ONLY` 是设计时签名预览。
可通过 stub 中的 `api_manifest.json` 查询可用性与动作类别。

## 7. 构建 wheel 与开发者检查

在支持的 Linux 环境完成 SDK 克隆后：

```bash
python -m pip install build
CMAKE_BUILD_PARALLEL_LEVEL=2 python -m build --wheel
python -m build --wheel ./stubs --outdir dist
```

`dist/` 中会得到匹配当前 Python/CPU 的原生 wheel 和一个 `py3-none-any` stub wheel。
将两个 wheel 复制到目标电脑安装即可，目标电脑不需要克隆 SDK 或编译源码。
Python 版本、CPU 架构和 Linux 系统 ABI 仍需兼容；这里不会自动生成跨所有发行版通用的 manylinux wheel。

如需源码发行包，先克隆 SDK，再运行 `python -m build --sdist`。
源码包会包含 `thirdparty/unitree_sdk2` 中编译需要的头文件和预编译库，不包含 SDK Git 历史。
没有克隆 SDK 时生成的源码包，需要在编译时通过 `UNITREE_SDK_ROOT` 指向完整 SDK。

普通安装使用已提交的生成代码，不要求 Clang。修改 API 或重新扫描 SDK 时，需要安装 `clang++`：

```bash
python generator/scan_headers.py --output generated/idl_inventory.json include/unitree/idl

# 重新生成 C++ bindings 并安装（需要 Clang）。
python -m pip install . -Ccmake.define.UNITREE_REGENERATE_BINDINGS=ON

# 源码级测试；不执行机器人命令。
python -m pip install pytest
python -m pytest -q
```

测试和扫描器也支持独立 `thirdparty/` 布局及 `UNITREE_SDK_ROOT`。
macOS 可运行不依赖原生扩展的测试，原生导入测试会跳过；这不等于 Linux 编译或真机验证。

## 8. 常见问题

- **`Unitree SDK2 not found`**：确认依赖位于 `thirdparty/unitree_sdk2`；或指定正确的 SDK 根目录。
- **缺少头文件或 `.a` / `.so`**：克隆完整 SDK，不要只下载 `include/`，也不要混用不同架构的库。
- **macOS / Windows 构建失败**：原生扩展只支持 SDK 预编译库对应的 Linux 平台；本地可只安装 `./stubs` 写代码。
- **`ModuleNotFoundError`**：检查 `python -m pip show unitree-sdk2-cpp`，确保运行和安装使用同一解释器。
- **`undefined symbol`**：SDK 头文件、静态库或旧扩展可能不匹配；使用固定 SDK 提交重新构建，检查导入的 `.so` 路径。
- **DDS 超时**：核对网卡、网络连接、设备模式及对应服务。RPC 错误码非 0 时不要继续使用输出值。

## 文档导航

- [Go2 示例教程](examples/GO2_EXAMPLES_ZH.md)
- [中文初学者指南与编码规范](docs/BEGINNER_GUIDE_ZH.md)
- [完整 API 分类索引](docs/API_REFERENCE_ZH.md)
- [Go2 Client API](docs/api/robot-go2.md) / [Go2 DDS 消息](docs/api/idl-go2.md)
- G1 示例：`examples/g1_read_only_status.py`、`g1_state_monitor.py`、`g1_arm_action.py`

API 文档由 `.pyi`、清单及 Clang AST 生成，修改签名后运行 `python generator/generate_api_docs.py` 更新。
