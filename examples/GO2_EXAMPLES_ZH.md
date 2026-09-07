# Go2 Python 示例

这些脚本使用本仓库的 `unitree_sdk2_cpp` binding。需要在支持的 Linux
环境安装原生包；仅安装 stubs 只能获得类型提示，不能连接机器人。
以下命令从 `unitree_sdk2_bindings` 目录运行，把 `eth0` 换成连接 Go2 的网卡名。
默认使用 DDS domain 0。脚本可以分别运行，无需先运行其他示例。

## 1. 查看服务列表

```bash
python examples/go2_service_list.py -n eth0
```

打印服务的 `name`、`status`、`protect` 原始值，不启停服务。
核心调用是 `status, services = client.service_list()`：只有 `status == 0`
时才能使用返回的数据，失败时程序输出错误码并以非零状态退出。

## 2. 查看语音、音量和灯光状态

```bash
python examples/go2_vui_status.py -n eth0
```

依次调用 `get_switch()`、`get_volume()`、`get_brightness()`，只读不修改。
每个函数返回 `(错误码, 值)`，示例里的 `require_value()` 负责检查错误码。

## 3. 订阅运动状态

```bash
python examples/go2_state_monitor.py -n eth0 --seconds 10
```

订阅 `rt/sportmodestate`，消息类型是 `unitree_sdk2_cpp.idl.go2.SportModeState`。
收到第一条消息后，持续打印 10 秒，每秒最多两次。输出包括模式、步态、位置（米）、
速度（米/秒）和 RPY 姿态（弧度）。模式和步态保留原始编号，请结合设备固件解释。

DDS 回调把消息字段复制到不可变的 `Snapshot` 数据结构中；主线程通过锁读取快照。
回调内不打印、不控制机器人。5 秒内没收到首条消息，或后续数据超过 2 秒未更新，
程序报错退出。退出时先关闭订阅，再释放 DDS。

## 4. 起立、趴下、停止和短距离移动

这些命令会控制实体 Go2。请在空旷平地使用，保留遥控器停止手段，
确保没有其他程序同时发送控制指令。移动前先让机器人处于可行走状态。

```bash
# 每次只执行一个动作；除 stop 外，输入 GO2 确认后才发送。
python examples/go2_sport.py -n eth0 stand-up
python examples/go2_sport.py -n eth0 stand-down
python examples/go2_sport.py -n eth0 stop

# 以 0.1 m/s 向前发送 2 秒速度指令，随后发送 stop_move。
python examples/go2_sport.py -n eth0 move --vx 0.1 --seconds 2

# 原地左转：角速度为 0.2 rad/s，持续 1 秒。
python examples/go2_sport.py -n eth0 move --vyaw 0.2 --seconds 1
```

`vx` 为前向速度，`vy` 为左向速度，`vyaw` 为偏航角速度；负值表示反方向。
三个速度默认都是 0。示例限制 `|vx|`、`|vy|` 不超过 0.3 m/s，
`|vyaw|` 不超过 0.5 rad/s，持续时间在 0 到 10 秒之间，不含 0。
这些是示例限制，不代表机器人的能力上限。

移动循环在 RPC 调用之间最多等待 20 ms；这是高层控制示例，不是实时控制器。
持续时间表示发送指令的时间窗口，RPC 延迟可能使实际耗时更长，也不保证精确行走距离。
程序不会自动起立或切换控制服务。

正常结束、SDK 错误或 Ctrl+C 中断移动时，`finally` 都会尝试 `stop_move()`，
随后释放 DDS。停止调用失败会报错；断网、进程被强制杀死等情况下，不能靠此脚本保证停止。
起立/趴下调用返回成功仅表示请求被接受，不表示物理动作已经完成。

## 从示例开始写自己的程序

- 单次查询先看 `go2_service_list.py`，结构最简单。
- 函数返回 `int` 时检查是否为 0；返回 `(int, value)` 时先检查状态再使用值。
- 连续状态用订阅回调接收，自己的业务数据用 `dataclass`，不要把整个 DDS 消息长期跨线程共享。
- 初始化和调用放在 `try` 内，清理放在 `finally` 内，`main()` 负责打印错误和返回退出码。

完整签名见 [Go2 Client API](../docs/api/robot-go2.md) 和
[Go2 DDS 消息 API](../docs/api/idl-go2.md)。
