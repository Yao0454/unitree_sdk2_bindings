#!/usr/bin/env python3
"""只在内存构造 Go2 LowCmd，演示数组回写；不初始化 DDS，不发送命令。"""

from __future__ import annotations

from dataclasses import dataclass

from unitree_sdk2_cpp.idl.go2 import LowCmd, MotorCmd

NUM_MESSAGE_MOTORS = 20  # DDS 消息有 20 个槽位，Go2 腿部关节使用前 12 个。


@dataclass(frozen=True, slots=True)
class JointSettings:
    position_rad: float = 0.0
    velocity_rad_s: float = 0.0
    kp: float = 0.0
    kd: float = 0.0
    torque_nm: float = 0.0


def make_motor(settings: JointSettings) -> MotorCmd:
    motor = MotorCmd()
    motor.mode = 0
    motor.q = settings.position_rad
    motor.dq = settings.velocity_rad_s
    motor.kp = settings.kp
    motor.kd = settings.kd
    motor.tau = settings.torque_nm
    motor.reserve = [0, 0, 0]
    return motor


def replace_joint(command: LowCmd, index: int, settings: JointSettings) -> None:
    if not 0 <= index < 12:
        raise IndexError("Go2 腿部关节编号必须在 0 到 11 之间")
    # getter 返回副本：必须把修改后的整个列表赋回 message.motor_cmd。
    motors = command.motor_cmd
    motors[index] = make_motor(settings)
    command.motor_cmd = motors


def main() -> int:
    command = LowCmd()
    command.motor_cmd = [make_motor(JointSettings()) for _ in range(NUM_MESSAGE_MOTORS)]
    replace_joint(command, 0, JointSettings(position_rad=0.1))
    print(f"消息电机槽位数：{len(command.motor_cmd)}")
    print(f"第 0 个关节的目标位置：{command.motor_cmd[0].q:.3f} rad")
    print("仅演示数据结构；未设置发送所需的消息头、控制模式或 CRC，不能直接发送。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
