# Unitree SDK2 Python 完整 API 参考

本页是完整 API Reference 的总索引。详细内容按 Python 模块拆分到 `api/` 目录，每个分卷为类、函数和属性提供签名、参数、返回值、可用性、C++ 对应项和用法。学习路径和完整教程请先阅读 [从零开始指南](BEGINNER_GUIDE_ZH.md)。

> [!WARNING]
> 本文同时包含 `AVAILABLE` 和 `SIGNATURE_ONLY`。后者只是设计期类型签名。运动及硬件副作用方法已进入运行时绑定，但只表示接口可调用，不表示当前环境可安全执行；默认测试绝不会构造客户端、初始化 DDS 或发送机器人指令。

> [!NOTE]
> 本索引和 `api/` 中的分卷均由 `generator/generate_api_docs.py` 从 `.pyi`、`api_manifest.json` 和 Clang AST 清单生成。不要手工维护 API 条目；修改签名后应重新生成并运行测试。

## 如何阅读本参考

每个 API 条目包含以下部分：

- **签名**：Python 类型检查器看到的准确调用形态；
- **可用性与安全性**：区分当前实现和仅签名预览；
- **参数**：Python 类型、默认值和能够从 SDK 定义可靠确认的含义；
- **返回值**：包括 C++ 输出引用转换后的 Python 元组顺序；
- **对应 C++**：原类、原签名、绑定策略和头文件位置；
- **用法**：`AVAILABLE` 给出调用形态，`SIGNATURE_ONLY` 只给出 `TYPE_CHECKING` 计划代码。

各条目中的代码是局部调用片段，不是完整脚本。类章节会先给出导入语句；`obj`、`helper`、`client`、`publisher`、`subscriber` 和参数变量表示调用者已经按业务规则创建、初始化并校验好的对象。

参数名称无法表达单位、坐标系、范围或枚举值时，本文会明确要求查目标型号协议。这比根据名字猜测更可靠。

## 覆盖统计

| 项目 | 数量 |
| --- | ---: |
| 有内容的 Python 模块 | 16 |
| 类和枚举 | 189 |
| 普通/重载函数签名 | 867 |
| Python 属性 | 346 |
| 公开数据属性 | 173 |
| Manifest 条目 | 1213 |
| `AVAILABLE` | 1167 |
| `SIGNATURE_ONLY` | 46 |

一个 Python 属性在 manifest 中占一个条目，但下文会同时写出 getter 和 setter 签名。重载方法按不同 C++ 签名分别展开。

## 分卷索引

| 分类 | Python 模块 | 函数 | 类 | 文档 |
| --- | --- | ---: | ---: | --- |
| 系统辅助 API | `unitree_sdk2_cpp` | 0 | 1 | [打开分卷](api/core.md#unitree-sdk2-cpp) |
| Typed DDS Channel API | `unitree_sdk2_cpp.channel` | 4 | 2 | [打开分卷](api/channel.md#unitree-sdk2-cpp-channel) |
| unitree_sdk2_cpp.idl.g1 | `unitree_sdk2_cpp.idl.g1` | 5 | 0 | [打开分卷](api/idl-g1.md#unitree-sdk2-cpp-idl-g1) |
| Go2 IDL 消息 | `unitree_sdk2_cpp.idl.go2` | 0 | 26 | [打开分卷](api/idl-go2.md#unitree-sdk2-cpp-idl-go2) |
| HG IDL 消息 | `unitree_sdk2_cpp.idl.hg` | 0 | 13 | [打开分卷](api/idl-hg.md#unitree-sdk2-cpp-idl-hg) |
| HG Double-IMU IDL 消息 | `unitree_sdk2_cpp.idl.hg_doubleimu` | 0 | 1 | [打开分卷](api/idl-hg_doubleimu.md#unitree-sdk2-cpp-idl-hg-doubleimu) |
| ROS2 兼容 IDL 消息 | `unitree_sdk2_cpp.idl.ros2` | 0 | 24 | [打开分卷](api/idl-ros2.md#unitree-sdk2-cpp-idl-ros2) |
| Robot 公共基础 API | `unitree_sdk2_cpp.robot` | 0 | 18 | [打开分卷](api/robot.md#unitree-sdk2-cpp-robot) |
| A2 Robot API | `unitree_sdk2_cpp.robot.a2` | 0 | 8 | [打开分卷](api/robot-a2.md#unitree-sdk2-cpp-robot-a2) |
| AS2 Robot API | `unitree_sdk2_cpp.robot.as2` | 0 | 2 | [打开分卷](api/robot-as2.md#unitree-sdk2-cpp-robot-as2) |
| B2 Robot API | `unitree_sdk2_cpp.robot.b2` | 0 | 25 | [打开分卷](api/robot-b2.md#unitree-sdk2-cpp-robot-b2) |
| G1 Robot API | `unitree_sdk2_cpp.robot.g1` | 7 | 12 | [打开分卷](api/robot-g1.md#unitree-sdk2-cpp-robot-g1) |
| Go2 Robot API | `unitree_sdk2_cpp.robot.go2` | 0 | 37 | [打开分卷](api/robot-go2.md#unitree-sdk2-cpp-robot-go2) |
| H1 Robot API | `unitree_sdk2_cpp.robot.h1` | 0 | 4 | [打开分卷](api/robot-h1.md#unitree-sdk2-cpp-robot-h1) |
| H2 Robot API | `unitree_sdk2_cpp.robot.h2` | 0 | 8 | [打开分卷](api/robot-h2.md#unitree-sdk2-cpp-robot-h2) |
| R1 Robot API | `unitree_sdk2_cpp.robot.r1` | 0 | 8 | [打开分卷](api/robot-r1.md#unitree-sdk2-cpp-robot-r1) |

## 建议阅读方式

1. 从上表选择目标型号或模块；
2. 在分卷的类索引中选择 Client 或消息类型；
3. 查看具体成员的可用性和安全分类；
4. 使用编辑器补全和类型检查确认实际调用签名。

需要跨全部 API 自动检索时，优先读取打包在 stub 中的 `unitree_sdk2_cpp/api_manifest.json`。
