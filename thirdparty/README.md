# C++ SDK 依赖

在 bindings 仓库根目录执行：

```bash
git clone https://github.com/Yao0454/unitree_sdk2.git thirdparty/unitree_sdk2
git -C thirdparty/unitree_sdk2 checkout d13dc9fdc20a3af7063f2ba03bc7b98c16f4999f
```

这是当前本地 SDK 的 `include/`、`lib/`、`thirdparty/` 对应的提交基线。
固定版本便于复现生成代码使用的接口，不表示新增示例均已做过真机测试。
构建直接使用 SDK 的 Linux x86_64 / aarch64 预编译库，不会自动下载依赖或安装系统库。

SDK 目录被本仓库忽略。如果已有 SDK，请通过 `UNITREE_SDK_ROOT` 指向它；
详细安装步骤见 [主 README](../README.md)。
