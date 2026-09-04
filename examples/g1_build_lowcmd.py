#!/usr/bin/env python3
"""Build and inspect a G1 LowCmd without initializing DDS or sending it."""

from __future__ import annotations

from dataclasses import dataclass

from unitree_sdk2_cpp.idl import g1


NUM_G1_MOTORS = 35


@dataclass(frozen=True, slots=True)
class JointCommand:
    """Application-owned joint settings, with units in the field names."""

    position_rad: float = 0.0
    velocity_rad_s: float = 0.0
    kp: float = 0.0
    kd: float = 0.0
    torque_nm: float = 0.0


def make_motor_command(settings: JointCommand) -> g1.MotorCmd:
    motor = g1.MotorCmd()
    motor.mode = 0
    motor.q = settings.position_rad
    motor.dq = settings.velocity_rad_s
    motor.kp = settings.kp
    motor.kd = settings.kd
    motor.tau = settings.torque_nm
    motor.reserve = 0
    return motor


def make_command(settings: JointCommand) -> g1.LowCmd:
    command = g1.LowCmd()
    command.mode_pr = 0
    command.mode_machine = 0
    command.reserve = [0, 0, 0, 0]
    command.motor_cmd = [
        make_motor_command(settings) for _ in range(NUM_G1_MOTORS)
    ]

    if len(command.motor_cmd) != NUM_G1_MOTORS:
        raise RuntimeError("G1 LowCmd must contain exactly 35 motor commands")

    g1.update_crc(command)
    return command


def replace_joint(
    command: g1.LowCmd,
    joint_index: int,
    settings: JointCommand,
) -> None:
    if not 0 <= joint_index < NUM_G1_MOTORS:
        raise IndexError(f"joint index must be in [0, {NUM_G1_MOTORS})")

    # pybind11 returns arrays by value. Read the complete list, modify it, and
    # assign the complete list back to the message.
    motors = command.motor_cmd
    motors[joint_index] = make_motor_command(settings)
    command.motor_cmd = motors
    g1.update_crc(command)


def main() -> int:
    command = make_command(JointCommand())
    replace_joint(command, 0, JointCommand(position_rad=0.1))

    if not g1.validate_crc(command):
        raise RuntimeError("generated LowCmd has an invalid CRC")

    print(f"motor count: {len(command.motor_cmd)}")
    print(f"motor[0].q: {command.motor_cmd[0].q:.3f} rad")
    print(f"crc: {command.crc:#010x}")
    print("No DDS channel was initialized; nothing was sent to a robot.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
