import json
from pathlib import Path

import pytest


ROOT = Path(__file__).parents[1]
unitree_sdk2_cpp = pytest.importorskip("unitree_sdk2_cpp")


def _resolve(path: str):
    value = unitree_sdk2_cpp
    for part in path.removeprefix("unitree_sdk2_cpp.").split("."):
        value = getattr(value, part)
    return value


def test_robot_client_surface_is_registered_without_construction() -> None:
    report = json.loads(
        (ROOT / "generated/robot_read_only_report.json").read_text(encoding="utf-8")
    )
    assert hasattr(unitree_sdk2_cpp.robot.ClientBase, "set_timeout")
    assert hasattr(unitree_sdk2_cpp.robot.Client, "get_api_version")
    for item in report["classes"]:
        client_type = getattr(_resolve(item["python_module"]), item["python_name"])
        for method in item["methods"]:
            assert hasattr(client_type, method["python_name"])


def test_complete_surface_is_inspected_without_hardware_calls() -> None:
    assert hasattr(unitree_sdk2_cpp.robot.LeaseClient, "applied")
    assert hasattr(unitree_sdk2_cpp.robot.g1.LocoClient, "move")
    assert hasattr(unitree_sdk2_cpp.robot.g1.LocoClient, "stand_up")
    assert hasattr(unitree_sdk2_cpp.robot.h2.H2ArmActionClient, "execute_action")
    assert hasattr(unitree_sdk2_cpp.robot.go2.VuiClient, "set_volume")
    assert hasattr(unitree_sdk2_cpp.robot.b2.ConfigClient, "subscribe_change_status")


def test_missing_sdk_symbol_is_not_referenced_by_the_extension() -> None:
    source = (ROOT / "src" / "generated" / "robot_read_only.cpp").read_text(
        encoding="utf-8"
    )
    assert '"get_lease_id"' not in source
    report = json.loads(
        (ROOT / "generated" / "robot_read_only_report.json").read_text(
            encoding="utf-8"
        )
    )
    assert any(
        item["qualified_name"] == "unitree::robot::Client"
        and item["signature"] == "GetLeaseId()"
        for item in report["unbound_methods"]
    )


def test_json_value_objects_round_trip_without_dds() -> None:
    value = unitree_sdk2_cpp.robot.go2.JsonizeDataFloat()
    value.from_json({"data": 1.25})
    assert value.data == pytest.approx(1.25)
    assert value.to_json() == {"data": pytest.approx(1.25)}

    command = unitree_sdk2_cpp.robot.g1.MoveParameter()
    command.from_json({"vx": 0.1, "vy": -0.2, "vyaw": 0.3})
    assert command.vx == pytest.approx(0.1)
    assert command.vy == pytest.approx(-0.2)
    assert command.vyaw == pytest.approx(0.3)
    assert command.to_json() == {
        "vx": pytest.approx(0.1),
        "vy": pytest.approx(-0.2),
        "vyaw": pytest.approx(0.3),
    }


def test_lease_value_objects_do_not_initialize_dds() -> None:
    context = unitree_sdk2_cpp.robot.LeaseContext()
    assert not context.valid()
    context.update(42, 3000)
    assert context.valid()
    assert context.get_id() == 42
    assert context.get_term() == 3000
    context.reset()
    assert not context.valid()

    cache = unitree_sdk2_cpp.robot.LeaseCache()
    cache.set(7, "agent", 100)
    assert cache.get_id() == 7
    assert cache.get_name() == "agent"
    assert cache.get_last_modified() == 100
    cache.renewal()
    cache.clear()
    assert cache.get_id() == 0
