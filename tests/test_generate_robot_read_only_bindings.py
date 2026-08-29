import copy
import json
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT / "generator"))

from generate_robot_read_only_bindings import generate  # noqa: E402


def _load(name: str) -> dict:
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def test_checked_in_robot_client_binding_is_current() -> None:
    source, report = generate(
        _load("generated/robot_inventory.json"),
        _load("generated/robot_binding_report.json"),
        _load("generator/robot_read_only_policy.json"),
    )
    assert source == (ROOT / "src/generated/robot_read_only.cpp").read_text(
        encoding="utf-8"
    )
    assert report == _load("generated/robot_read_only_report.json")
    assert report["summary"] == {
        "client_classes": 26,
        "client_methods": 336,
        "enums": 1,
        "hardware_side_effect_methods_exposed": 36,
        "motion_methods_exposed": 220,
        "read_only_methods": 50,
        "unbound_methods": 5,
        "utility_classes": 2,
        "utility_methods": 11,
        "value_classes": 80,
        "value_methods": 144,
    }
    assert {item["qualified_name"] for item in report["value_classes"]} >= {
        "unitree::robot::a2::PathPoint",
        "unitree::robot::b2::ConfigMeta",
        "unitree::robot::b2::ServiceState",
        "unitree::robot::go2::ConfigMeta",
        "unitree::robot::go2::ServiceState",
    }
    assert "void BindRobotClients" in source
    assert '"move"' in source
    assert '"subscribe_change_status"' in source
    assert "py::gil_scoped_acquire acquire" in source
    assert 'py::arg("duration") = 1.0' in source
    assert 'robot_go2_JsonizeDataFloat.def("from_json"' in source
    assert 'robot_go2_JsonizeDataFloat.def("to_json"' in source
    assert "int32_t status{};\n        int32_t status{};" not in source
    assert {
        item["qualified_name"]
        for item in report["value_classes"]
        if item.get("methods")
    } >= {
        "unitree::robot::ApplyLeaseData",
        "unitree::robot::go2::JsonizeDataFloat",
        "unitree::robot::h2::JsonizeFsmIdList",
    }
    assert {item["qualified_name"] for item in report["utility_classes"]} == {
        "unitree::robot::LeaseCache",
        "unitree::robot::LeaseContext",
    }
    assert {
        (item["qualified_name"], item["signature"])
        for item in report["unbound_methods"]
    } == {
        ("unitree::robot::Client", "GetLeaseId()"),
        ("unitree::robot::ClientBase", "Init()"),
        ("unitree::robot::ClientStub", "Init(const std::string &)"),
        (
            "unitree::robot::ClientStub",
            "Send(const unitree::robot::Request &, int64_t)",
        ),
        (
            "unitree::robot::ClientStub",
            "SendRequest(const unitree::robot::Request &, int64_t)",
        ),
    }


def test_policy_rejects_a_motion_method_even_if_named_explicitly() -> None:
    policy = copy.deepcopy(_load("generator/robot_read_only_policy.json"))
    policy["classes"]["unitree::robot::g1::LocoClient"].append(
        "Move(float, float, float)"
    )
    with pytest.raises(ValueError, match="no longer classified as safe read-only"):
        generate(
            _load("generated/robot_inventory.json"),
            _load("generated/robot_binding_report.json"),
            policy,
        )


def test_mutable_input_policy_is_validated() -> None:
    policy = copy.deepcopy(_load("generator/robot_read_only_policy.json"))
    policy["mutable_inputs"]["unitree::robot::b2::SportClient"].append(
        "Missing(std::vector<float> &)"
    )
    with pytest.raises(ValueError, match="mutable input policy entries are missing"):
        generate(
            _load("generated/robot_inventory.json"),
            _load("generated/robot_binding_report.json"),
            policy,
        )


def test_utility_policy_is_validated() -> None:
    policy = copy.deepcopy(_load("generator/robot_read_only_policy.json"))
    policy["utility_classes"]["unitree::robot::LeaseCache"].append("Missing()")
    with pytest.raises(ValueError, match="utility policy entries are missing"):
        generate(
            _load("generated/robot_inventory.json"),
            _load("generated/robot_binding_report.json"),
            policy,
        )
