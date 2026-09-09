# Unitree SDK2 中文类型提示包（0.4.0）

安装后可以在没有机器人、没有 Linux 原生扩展的环境中编写和检查
`unitree_sdk2_cpp` 代码。此包包含 17 个 `.pyi` 文件和完整签名清单，并为
189 个类、867 个函数/重载和 346 个属性提供中文悬停说明。

## 安装

在 bindings 仓库根目录、你的应用虚拟环境已激活时：

```bash
python -m pip install --upgrade ./stubs
```

从其他目录也可以用绝对路径：

```bash
python -m pip install /absolute/path/to/unitree_sdk2_bindings/stubs
```

或安装已构建的 wheel：

```bash
python -m pip install --upgrade ./unitree_sdk2_cpp_stubs-0.4.0-py3-none-any.whl
```

只使用类型提示时不需要克隆 C++ SDK、安装编译器或编译 `.so`。
请使用普通安装：wheel 安装后不依赖原始 checkout 路径。开发此类型包本身时才需要可编辑安装。

## Pyright、BasedPyright 和 Zed

编辑器必须选择安装了这个包的 Python 解释器。换项目时如果换了虚拟环境，需在新环境重新安装。
这是 Python 环境隔离的正常行为，不需要给每个项目手填 SDK 路径。

0.4.0 不要求 `extraPaths`、`include`、`stubPath` 指向 bindings，也不需要关闭
`reportMissingModuleSource`。旧配置中**专门为本包添加**的路径和诊断屏蔽可以删除；
不要删除用于其他依赖的配置。更新包后可重启语言服务器刷新缓存。

例如创建 `check_api.py`：

```python
from unitree_sdk2_cpp import channel
from unitree_sdk2_cpp.idl.go2 import LowState
from unitree_sdk2_cpp.robot.go2 import SportClient

def on_state(message: LowState) -> None:
    print(message.bms_state.soc)

def check_types(client: SportClient) -> int:
    return client.move(vx=0.1, vy=0.0, vyaw=0.0)
```

执行静态检查（不会运行代码或控制机器人）：

```bash
python -m pip install pyright
pyright --pythonpath "$(python -c 'import sys; print(sys.executable)')" check_api.py
```

正确调用应得到 `0 errors, 0 warnings`。写错参数类型、访问不存在的成员等真正代码错误
仍然会被报告。例如 `client.move(vx="fast", vy=0, vyaw=0)` 应报类型错误。
我们没有通过全局 `Any`、`# type: ignore` 或屏蔽诊断来让错误消失。

未写 import 就搜索第三方符号的自动导入功能还受语言服务器索引设置影响；
这个包不修改用户的全局编辑器配置。

## 悬停能看到什么

函数提示包含中文用途、可用性、参数含义、返回值和调用示例，格式为
`Args` / `Returns` / `Examples` / `Notes`。每个重载都有自己的说明。
常用 Go2/G1 方法提供更具体的解释；上游没有明确业务语义的接口会如实标注需查设备协议，
不会猜测数值范围。IDL 字段说明包含固定数组长度约束及“读取副本、修改后回写”的用法。

例如悬停 `SportClient.move` 可看到速度参数的方向和单位，以及检查返回码、
在 `finally` 里发送 `stop_move()` 的局部用法。
示例中的 `client`、`obj` 和部分参数是已经初始化的业务对象，不是可直接连机器人运行的完整程序。

## 运行时行为

完整 `.pyi` 位于 PEP 561 的 `unitree_sdk2_cpp-stubs/` 中。
另有轻量 `unitree_sdk2_cpp/` 源码入口，供语言服务器识别模块来源。
这个入口**没有机器人实现或模拟返回值**：

- 已安装原生扩展：显式加载原有 `unitree_sdk2_cpp*.so`，保留其类、子模块和对象身份。
- 未安装原生扩展：运行时导入抛出明确 `ImportError`，提示安装 `unitree-sdk2-cpp`。
- 原生扩展 ABI/动态链接失败：保留真实错误，不伪装成类型包成功运行。

同一个环境中仍需遵守原生扩展支持的平台和 Python ABI；详见[主 README](../README.md)。
普通原生 wheel 的入口加载路径已有小型 CPython 扩展测试，测试不调用 Unitree 或 DDS；
真实 Unitree Linux 扩展仍需在目标 Linux 环境验证。

## 类型完整性与可用性

清单共 1213 个条目：1167 个 `AVAILABLE`，46 个 `SIGNATURE_ONLY`。
`AVAILABLE` 表示当前绑定源码已实现；`SIGNATURE_ONLY` 为设计时预览，不能假设可运行。
运动方法有类型提示不代表动作适用于当前机器人状态。

## 重新生成和构建（维护者）

中文悬停说明由 `generator/stub_help.py` 与 API 文档模型生成；源码入口由
`generator/stub_sources.py` 和 `generator/templates/native_loader.py` 生成。
不要单独手改生成后的 `.pyi`，否则下次生成会覆盖。

在仓库根目录运行：

```bash
python generator/generate_type_stubs.py \
  --idl-inventory generated/idl_inventory.json \
  --robot-inventory generated/robot_inventory.json \
  --classification generated/robot_binding_report.json \
  --policy generator/robot_read_only_policy.json \
  --read-only-report generated/robot_read_only_report.json \
  --idl-report generated/idl_go2_report.json \
  --idl-report generated/idl_hg_report.json \
  --idl-report generated/idl_hg_doubleimu_report.json \
  --idl-report generated/idl_ros2_report.json \
  --output stubs/src
python generator/generate_api_docs.py
python -m pip wheel --no-deps ./stubs --wheel-dir dist
```

更多内容：[初学者教程](../docs/BEGINNER_GUIDE_ZH.md)、[API 分类索引](../docs/API_REFERENCE_ZH.md)。
