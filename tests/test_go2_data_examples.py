"""Offline tests for Go2 camera/settings examples and copied DDS snapshots."""

import importlib.util
import sys
from pathlib import Path
from types import ModuleType, SimpleNamespace
from unittest.mock import Mock

import pytest


@pytest.fixture
def load_example(monkeypatch):
    sdk = ModuleType("unitree_sdk2_cpp")
    channel = ModuleType("unitree_sdk2_cpp.channel")
    robot = ModuleType("unitree_sdk2_cpp.robot")
    clients = ModuleType("unitree_sdk2_cpp.robot.go2")
    idl = ModuleType("unitree_sdk2_cpp.idl")
    messages = ModuleType("unitree_sdk2_cpp.idl.go2")
    channel.initialize = Mock()
    channel.release = Mock()
    channel.ChannelSubscriber = Mock()
    client = Mock()
    clients.VideoClient = Mock(return_value=client)
    clients.VuiClient = Mock(return_value=client)
    messages.LowState = Mock()
    sdk.channel = channel
    sdk.robot = robot
    robot.go2 = clients
    sdk.idl = idl
    idl.go2 = messages
    for module in (sdk, channel, robot, clients, idl, messages):
        monkeypatch.setitem(sys.modules, module.__name__, module)

    def load(name):
        path = Path(__file__).parents[1] / "examples" / f"{name}.py"
        spec = importlib.util.spec_from_file_location(f"test_example_{name}", path)
        module = importlib.util.module_from_spec(spec)
        monkeypatch.setitem(sys.modules, spec.name, module)
        spec.loader.exec_module(module)
        return module, channel, client
    return load


def test_camera_preserves_bytes_and_refuses_to_overwrite(load_example, tmp_path):
    module, channel, client = load_example("go2_camera_snapshot")
    image = b"\xff\xd8sample\xff\xd9"
    client.get_image_sample.return_value = (0, list(image))
    output = tmp_path / "photo.jpg"
    assert module.capture("eth0", output) == len(image)
    assert output.read_bytes() == image
    client.get_image_sample.return_value = (0, list(b"\xff\xd8different"))
    with pytest.raises(FileExistsError):
        module.capture("eth0", output)
    assert output.read_bytes() == image
    assert channel.release.call_count == 2


@pytest.mark.parametrize("result,error", [( (9, []), RuntimeError), ((0, []), ValueError), ((0, [1, 2]), ValueError)])
def test_camera_errors_do_not_create_output(load_example, tmp_path, result, error):
    module, channel, client = load_example("go2_camera_snapshot")
    client.get_image_sample.return_value = result
    output = tmp_path / "photo.jpg"
    with pytest.raises(error):
        module.capture("eth0", output)
    assert not output.exists()
    channel.release.assert_called_once()


@pytest.mark.parametrize("setting", ["volume", "brightness"])
def test_setting_only_writes_selected_value_and_reads_it_back(load_example, setting):
    module, channel, client = load_example("go2_vui_set")
    getattr(client, f"set_{setting}").return_value = 0
    getattr(client, f"get_{setting}").return_value = (0, 3)
    assert module.set_and_read("eth0", setting, 3) == 3
    getattr(client, f"set_{setting}").assert_called_once_with(3)
    other = "brightness" if setting == "volume" else "volume"
    getattr(client, f"set_{other}").assert_not_called()
    channel.release.assert_called_once()


def test_setting_failure_skips_readback(load_example):
    module, channel, client = load_example("go2_vui_set")
    client.set_volume.return_value = 9
    with pytest.raises(RuntimeError, match="9"):
        module.set_and_read("eth0", "volume", 3)
    client.get_volume.assert_not_called()
    channel.release.assert_called_once()


def test_readback_failure_does_not_retry_setting(load_example):
    module, channel, client = load_example("go2_vui_set")
    client.set_volume.return_value = 0
    client.get_volume.return_value = (9, 0)
    with pytest.raises(RuntimeError, match="设置已被接受"):
        module.set_and_read("eth0", "volume", 3)
    client.set_volume.assert_called_once_with(3)
    channel.release.assert_called_once()


def test_lowstate_snapshot_is_independent_of_mutable_dds_message(load_example):
    module, _, _ = load_example("go2_lowstate_once")
    message = SimpleNamespace(
        tick=42, bms_state=SimpleNamespace(soc=80),
        imu_state=SimpleNamespace(rpy=[0.1, 0.2, 0.3]),
        motor_state=[SimpleNamespace(q=0.1, dq=0.2, tau_est=0.3, temperature=30) for _ in range(20)],
    )
    snapshot = module.make_snapshot(message)
    message.motor_state[0].q = 1.0
    message.imu_state.rpy[0] = 1.0
    assert len(snapshot.joints) == 12
    assert snapshot.joints[0].position_rad == 0.1
    assert snapshot.rpy_rad == (0.1, 0.2, 0.3)
    assert snapshot.battery_percent == 80


def test_lowstate_timeout_closes_subscriber_then_releases_dds(load_example, monkeypatch):
    module, channel, _ = load_example("go2_lowstate_once")
    event = Mock()
    event.wait.return_value = False
    monkeypatch.setattr(module.threading, "Event", Mock(return_value=event))
    calls = Mock()
    calls.attach_mock(channel.ChannelSubscriber.return_value.close_channel, "close")
    calls.attach_mock(channel.release, "release")
    with pytest.raises(TimeoutError):
        module.read_once("eth0")
    assert [call[0] for call in calls.mock_calls] == ["close", "release"]
