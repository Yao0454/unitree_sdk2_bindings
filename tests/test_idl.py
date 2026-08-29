import pytest

pytest.importorskip("unitree_sdk2_cpp")

from unitree_sdk2_cpp.idl.go2 import IMUState, MotorState


def test_motor_state_scalar_and_fixed_array_fields() -> None:
    state = MotorState()
    state.mode = 1
    state.q = 1.25
    state.dq = -0.5
    state.tau_est = 2.75
    state.temperature = 42
    state.lost = 3
    state.reserve = [7, 9]

    assert state.mode == 1
    assert state.q == pytest.approx(1.25)
    assert state.dq == pytest.approx(-0.5)
    assert state.tau_est == pytest.approx(2.75)
    assert state.temperature == 42
    assert state.lost == 3
    assert state.reserve == [7, 9]


def test_imu_state_fixed_arrays_are_copied_consistently() -> None:
    state = IMUState()
    state.quaternion = [1.0, 0.0, 0.0, 0.0]
    state.gyroscope = [0.1, 0.2, 0.3]
    state.accelerometer = [1.0, 2.0, 3.0]
    state.rpy = [0.4, 0.5, 0.6]
    state.temperature = 35

    assert state.quaternion == pytest.approx([1.0, 0.0, 0.0, 0.0])
    assert state.gyroscope == pytest.approx([0.1, 0.2, 0.3])
    assert state.accelerometer == pytest.approx([1.0, 2.0, 3.0])
    assert state.rpy == pytest.approx([0.4, 0.5, 0.6])
    assert state.temperature == 35


def test_fixed_array_length_is_checked() -> None:
    state = IMUState()
    with pytest.raises(TypeError):
        state.quaternion = [1.0, 0.0, 0.0]


def test_nested_go2_messages_use_value_semantics() -> None:
    from unitree_sdk2_cpp.idl.go2 import BmsCmd, LowCmd, MotorCmd

    motor = MotorCmd()
    motor.q = 0.25
    command = LowCmd()
    command.bms_cmd = BmsCmd()
    command.motor_cmd = [motor] * 20

    returned = command.motor_cmd
    returned[0].q = 1.5
    assert command.motor_cmd[0].q == pytest.approx(0.25)


def test_hg_and_ros2_modules_are_available() -> None:
    from unitree_sdk2_cpp.idl.hg import IMUState as HgIMUState
    from unitree_sdk2_cpp.idl.hg_doubleimu import doubleIMUState
    from unitree_sdk2_cpp.idl.ros2 import Header, Time

    hg_imu = HgIMUState()
    hg_imu.temperature = -2
    assert hg_imu.temperature == -2

    double_imu = doubleIMUState()
    double_imu.tick = 17
    assert double_imu.tick == 17

    stamp = Time()
    stamp.sec = 10
    header = Header()
    header.stamp = stamp
    assert header.stamp.sec == 10


def test_channel_metadata_and_safe_initialization_guard() -> None:
    import unitree_sdk2_cpp

    from unitree_sdk2_cpp.idl.go2 import MotorState

    channel = unitree_sdk2_cpp.channel
    registered = channel.registered_message_types()
    assert len(registered) == 64
    assert "unitree_sdk2_cpp.idl.go2.MotorState" in registered

    publisher = channel.ChannelPublisher("rt/test", MotorState)
    assert publisher.topic == "rt/test"
    assert publisher.message_type_name == "unitree_sdk2_cpp.idl.go2.MotorState"
    with pytest.raises(RuntimeError, match="channel factory is not initialized"):
        publisher.init_channel()

    subscriber = channel.ChannelSubscriber("rt/test", MotorState, lambda _: None)
    assert subscriber.topic == "rt/test"
    assert subscriber.message_type_name == "unitree_sdk2_cpp.idl.go2.MotorState"
    with pytest.raises(RuntimeError, match="channel factory is not initialized"):
        subscriber.init_channel()

    # Closing an uninitialized subscriber is intentionally safe and keeps the
    # object reusable.  A subsequent init on a real DDS-enabled host restores
    # callback delivery through the same Python callback state.
    subscriber.close_channel()
    assert subscriber.last_data_available_time == -1

    with pytest.raises(ValueError, match="int32_t limit"):
        channel.ChannelSubscriber("rt/test", MotorState, lambda _: None, 2**31)
    with pytest.raises(ValueError, match="int32_t limit"):
        channel.ChannelSubscriber("rt/test", MotorState, lambda _: None, -(2**31) - 1)


def test_channel_rejects_unknown_message_types_and_uninitialized_writes() -> None:
    import unitree_sdk2_cpp

    from unitree_sdk2_cpp.idl.go2 import MotorState

    channel = unitree_sdk2_cpp.channel
    with pytest.raises(TypeError, match="not a registered"):
        channel.ChannelPublisher("rt/test", int)

    publisher = channel.ChannelPublisher("rt/test", MotorState)
    with pytest.raises(RuntimeError, match="channel factory is not initialized"):
        publisher.init_channel()
    assert publisher.write(MotorState()) is False
    with pytest.raises(TypeError):
        publisher.write(object())
