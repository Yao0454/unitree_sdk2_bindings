"""Exercise Go2 example control flow with no native library or DDS connection."""

import importlib.util
import sys
from pathlib import Path
from types import ModuleType
from unittest.mock import Mock

import pytest


@pytest.fixture
def sport(monkeypatch):
    sdk = ModuleType("unitree_sdk2_cpp")
    channel = ModuleType("unitree_sdk2_cpp.channel")
    robot = ModuleType("unitree_sdk2_cpp.robot")
    go2 = ModuleType("unitree_sdk2_cpp.robot.go2")
    client = Mock()
    client.move.return_value = 0
    client.stop_move.return_value = 0
    client.stand_up.return_value = 0
    channel.initialize = Mock()
    channel.release = Mock()
    go2.SportClient = Mock(return_value=client)
    sdk.channel = channel
    sdk.robot = robot
    robot.go2 = go2
    for module in (sdk, channel, robot, go2):
        monkeypatch.setitem(sys.modules, module.__name__, module)

    path = Path(__file__).parents[1] / "examples" / "go2_sport.py"
    spec = importlib.util.spec_from_file_location("go2_sport_example_test", path)
    module = importlib.util.module_from_spec(spec)
    monkeypatch.setitem(sys.modules, spec.name, module)
    spec.loader.exec_module(module)
    monkeypatch.setattr(module.time, "monotonic", Mock(side_effect=[0.0, 0.0, 2.0, 2.0]))
    monkeypatch.setattr(module.time, "sleep", Mock())
    return module, channel, client


@pytest.mark.parametrize("failure", [None, 7404, RuntimeError("RPC timeout"), KeyboardInterrupt()])
def test_move_always_attempts_stop_before_releasing_dds(sport, failure):
    module, channel, client = sport
    calls = Mock()
    calls.attach_mock(client.move, "move")
    calls.attach_mock(client.stop_move, "stop")
    calls.attach_mock(channel.release, "release")
    if isinstance(failure, BaseException):
        client.move.side_effect = failure
    elif failure is not None:
        client.move.return_value = failure
    config = module.Config("eth0", "move", 0.1, 0.0, 0.0, 1.0)

    if failure is None:
        module.run(config)
    else:
        expected = KeyboardInterrupt if isinstance(failure, KeyboardInterrupt) else RuntimeError
        with pytest.raises(expected):
            module.run(config)
    assert [call[0] for call in calls.mock_calls] == ["move", "stop", "release"]
    client.move.assert_called_once_with(0.1, 0.0, 0.0)


@pytest.mark.parametrize("failure", [5, RuntimeError("stop RPC timeout")])
def test_stop_failure_is_reported_and_dds_is_still_released(sport, failure):
    module, channel, client = sport
    if isinstance(failure, Exception):
        client.stop_move.side_effect = failure
    else:
        client.stop_move.return_value = failure
    with pytest.raises(RuntimeError):
        module.run(module.Config("eth0", "move", 0.1, 0.0, 0.0, 1.0))
    channel.release.assert_called_once()


def test_client_init_failure_releases_dds_without_motion(sport):
    module, channel, client = sport
    client.init.side_effect = RuntimeError("init failed")
    with pytest.raises(RuntimeError):
        module.run(module.Config("eth0", "move", 0.1, 0.0, 0.0, 1.0))
    client.move.assert_not_called()
    client.stop_move.assert_not_called()
    channel.release.assert_called_once()


def test_rejected_confirmation_does_not_initialize_dds(sport, monkeypatch):
    module, channel, _ = sport
    monkeypatch.setattr(sys, "argv", ["go2_sport.py", "-n", "eth0", "stand-up"])
    monkeypatch.setattr("builtins.input", lambda _: "no")
    assert module.main() == 0
    channel.initialize.assert_not_called()


def test_explicit_stop_does_not_prompt(sport, monkeypatch):
    module, channel, client = sport
    monkeypatch.setattr(sys, "argv", ["go2_sport.py", "-n", "eth0", "stop"])
    monkeypatch.setattr("builtins.input", Mock(side_effect=AssertionError("unexpected prompt")))
    assert module.main() == 0
    client.stop_move.assert_called_once()
    client.move.assert_not_called()
    channel.release.assert_called_once()


@pytest.mark.parametrize("option,value", [
    ("--seconds", "nan"), ("--seconds", "inf"), ("--seconds", "0"),
    ("--seconds", "11"), ("--vx", "nan"), ("--vx", "0.31"),
    ("--vy", "-0.31"), ("--vyaw", "inf"), ("--vyaw", "0.51"),
])
def test_invalid_motion_arguments_are_rejected(sport, monkeypatch, option, value):
    module, channel, _ = sport
    monkeypatch.setattr(sys, "argv", ["go2_sport.py", "-n", "eth0", "move", option, value])
    with pytest.raises(SystemExit) as error:
        module.main()
    assert error.value.code == 2
    channel.initialize.assert_not_called()
