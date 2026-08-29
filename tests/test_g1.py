import json
from pathlib import Path

import pytest


ROOT = Path(__file__).parents[1]
unitree_sdk2_cpp = pytest.importorskip("unitree_sdk2_cpp")


def test_all_g1_idl_types_are_constructible_aliases() -> None:
    report = json.loads(
        (ROOT / "generated/idl_hg_report.json").read_text(encoding="utf-8")
    )
    g1 = unitree_sdk2_cpp.idl.g1
    hg = unitree_sdk2_cpp.idl.hg

    assert len(report["classes"]) == 13
    for item in report["classes"]:
        g1_type = getattr(g1, item["python_name"])
        assert g1_type is getattr(hg, item["python_name"])
        assert isinstance(g1_type(), g1_type)


def test_g1_low_command_has_fixed_35_motor_value_semantics() -> None:
    g1 = unitree_sdk2_cpp.idl.g1
    motor = g1.MotorCmd()
    motor.mode = 1
    motor.q = 0.25
    motor.kp = 20.0

    command = g1.LowCmd()
    command.mode_pr = 1
    command.mode_machine = 5
    command.motor_cmd = [motor] * 35

    returned = command.motor_cmd
    assert len(returned) == 35
    returned[0].q = 1.5
    assert command.motor_cmd[0].q == pytest.approx(0.25)

    with pytest.raises(TypeError):
        command.motor_cmd = [motor] * 34


def test_g1_crc_uses_the_sdk_implementation() -> None:
    g1 = unitree_sdk2_cpp.idl.g1
    command = g1.LowCmd()
    command.motor_cmd = [g1.MotorCmd()] * 35

    computed = g1.compute_crc(command)
    command.crc = computed ^ 0xFFFFFFFF
    assert not g1.validate_crc(command)
    assert g1.update_crc(command) == computed
    assert command.crc == computed
    assert g1.validate_crc(command)

    state = g1.LowState()
    state.crc = g1.compute_crc(state)
    assert g1.validate_crc(state)
    state.tick += 1
    assert not g1.validate_crc(state)


def test_g1_safety_checks_use_the_official_sdk_implementation() -> None:
    messages = unitree_sdk2_cpp.idl.g1
    safety = unitree_sdk2_cpp.robot.g1

    state = messages.LowState()
    imu = messages.IMUState()
    imu.quaternion = [1.0, 0.0, 0.0, 0.0]
    imu.gyroscope = [0.0, 0.0, 0.0]
    state.imu_state = imu

    motors = [messages.MotorState() for _ in range(35)]
    for motor in motors:
        motor.temperature = [25, 30]
    state.motor_state = motors

    assert not safety.bad_orientation(state)
    assert not safety.joint_vel_out_of_limit(state)
    assert not safety.ang_vel_out_of_limit(state)
    assert not safety.motor_winding_overheat(state)
    assert not safety.motor_casing_overheat(state)

    imu.quaternion = [0.0, 1.0, 0.0, 0.0]
    imu.gyroscope = [6.5, 0.0, 0.0]
    state.imu_state = imu
    motors[0].dq = 10.5
    motors[1].temperature = [86, 30]
    motors[2].temperature = [25, 121]
    state.motor_state = motors

    assert safety.bad_orientation(state)
    assert safety.bad_orientation(state, 0.5)
    assert safety.joint_vel_out_of_limit(state)
    assert safety.joint_vel_out_of_limit(state, 5.0)
    assert safety.ang_vel_out_of_limit(state)
    assert safety.ang_vel_out_of_limit(state, 3.0)
    assert safety.motor_winding_overheat(state)
    assert safety.motor_winding_overheat(state, 100.0)
    assert safety.motor_casing_overheat(state)
    assert safety.motor_casing_overheat(state, 80.0)

    battery = messages.BmsState()
    battery.soc = 21
    assert not safety.low_battery(battery)
    battery.soc = 19
    assert safety.low_battery(battery)
    assert safety.low_battery(battery, 50.0)


def test_g1_channel_types_are_registered_without_dds_initialization() -> None:
    channel = unitree_sdk2_cpp.channel
    g1 = unitree_sdk2_cpp.idl.g1
    safety = unitree_sdk2_cpp.robot.g1
    registered = channel.registered_message_types()

    expected = {
        "unitree_sdk2_cpp.idl.hg.LowCmd",
        "unitree_sdk2_cpp.idl.hg.LowState",
        "unitree_sdk2_cpp.idl.hg.HandCmd",
        "unitree_sdk2_cpp.idl.hg.HandState",
    }
    assert expected <= set(registered)

    publisher = channel.ChannelPublisher("rt/lowcmd", g1.LowCmd)
    assert publisher.message_type_name == "unitree_sdk2_cpp.idl.hg.LowCmd"
    with pytest.raises(RuntimeError, match="channel factory is not initialized"):
        publisher.init_channel()

    subscriber = channel.ChannelSubscriber(
        "rt/lowstate", g1.LowState, lambda _: None
    )
    assert safety.lost_connection(subscriber)
    assert safety.lost_connection(subscriber, 10)

    wrong_type = channel.ChannelSubscriber("rt/lowcmd", g1.LowCmd, lambda _: None)
    with pytest.raises(TypeError, match="must use.*LowState"):
        safety.lost_connection(wrong_type)


def test_all_g1_clients_and_methods_are_registered_without_construction() -> None:
    report = json.loads(
        (ROOT / "generated/robot_read_only_report.json").read_text(encoding="utf-8")
    )
    g1_clients = [
        item
        for item in report["classes"]
        if item["qualified_name"].startswith("unitree::robot::g1::")
    ]

    assert {item["python_name"] for item in g1_clients} == {
        "AgvClient",
        "AudioClient",
        "G1ArmActionClient",
        "LocoClient",
    }
    assert sum(len(item["methods"]) for item in g1_clients) == 49
    for item in g1_clients:
        client_type = getattr(unitree_sdk2_cpp.robot.g1, item["python_name"])
        for method in item["methods"]:
            assert hasattr(client_type, method["python_name"])
