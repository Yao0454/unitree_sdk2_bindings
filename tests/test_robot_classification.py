import sys
from pathlib import Path


ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT / "generator"))

from classify_robot_api import binding_strategy, classify, safety_class  # noqa: E402


def _method(name: str, *types: str) -> dict:
    return {
        "name": name,
        "return_type": "int32_t",
        "parameters": [
            {"name": f"arg{index}", "type": type_name}
            for index, type_name in enumerate(types)
        ],
        "access": "public",
        "is_const": False,
    }


def test_client_safety_classification_is_conservative() -> None:
    loco = {"name": "LocoClient"}
    video = {"name": "VideoClient"}
    assert safety_class(loco, _method("GetFsmId", "int &"))[0] == "READ_ONLY"
    assert safety_class(loco, _method("Move", "float"))[0] == "MOTION_COMMAND"
    assert safety_class(video, _method("GetImageSample", "std::vector<uint8_t> &"))[0] == "READ_ONLY"
    assert safety_class(video, _method("Init"))[0] == "INITIALIZATION"


def test_binding_strategy_detects_outputs_callbacks_and_pointers() -> None:
    assert binding_strategy(_method("Get", "std::string &"))[0] == "OUTPUT_WRAPPER"
    assert binding_strategy(_method("Subscribe", "const DemoCallback &"))[0] == "CALLBACK_MANUAL"
    assert binding_strategy(_method("Handle", "const void *"))[0] == "POINTER_MANUAL"
    assert binding_strategy(_method("Set", "int32_t"))[0] == "DIRECT"


def test_report_only_includes_public_client_methods() -> None:
    inventory = {
        "headers": ["demo.hpp"],
        "enums": [],
        "diagnostics": [],
        "classes": [
            {
                "namespace": "demo",
                "name": "DemoClient",
                "methods": [
                    _method("GetValue", "int &"),
                    {**_method("Internal"), "access": "private"},
                ],
            },
            {"namespace": "demo", "name": "Value", "methods": []},
        ],
    }
    report = classify(inventory)
    assert report["summary"]["client_classes"] == 1
    assert report["summary"]["client_methods"] == 1
    assert report["clients"][0]["methods"][0]["name"] == "GetValue"
