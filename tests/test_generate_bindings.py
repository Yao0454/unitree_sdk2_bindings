import json
import subprocess
import sys
from pathlib import Path


SDK_ROOT = Path(__file__).parents[2]
SCANNER = SDK_ROOT / "unitree_sdk2_bindings" / "generator" / "scan_headers.py"
GENERATOR = (
    SDK_ROOT / "unitree_sdk2_bindings" / "generator" / "generate_bindings.py"
)
CHANNEL_GENERATOR = (
    SDK_ROOT / "unitree_sdk2_bindings" / "generator" / "generate_channel_registry.py"
)
OVERRIDES = SDK_ROOT / "unitree_sdk2_bindings" / "generator" / "overrides.yaml"


def test_simple_idl_generator_uses_properties_and_reports_coverage(
    tmp_path: Path,
) -> None:
    inventory = tmp_path / "inventory.json"
    source = tmp_path / "go2.cpp"
    report = tmp_path / "report.json"
    subprocess.run(
        [
            sys.executable,
            str(SCANNER),
            "--sdk-root",
            str(SDK_ROOT),
            "--output",
            str(inventory),
            "include/unitree/idl/go2/MotorState_.hpp",
            "include/unitree/idl/go2/IMUState_.hpp",
        ],
        check=True,
    )
    subprocess.run(
        [
            sys.executable,
            str(GENERATOR),
            "--inventory",
            str(inventory),
            "--overrides",
            str(OVERRIDES),
            "--namespace-prefix",
            "unitree_go::msg::dds_",
            "--function",
            "BindGo2Idl",
            "--module",
            "idl",
            "--module",
            "go2",
            "--output",
            str(source),
            "--report",
            str(report),
        ],
        check=True,
    )

    generated = source.read_text(encoding="utf-8")
    assert "py::class_<unitree_go::msg::dds_::MotorState_>" in generated
    assert '"q"' in generated
    assert "std::array<float, 4>" in generated

    coverage = json.loads(report.read_text(encoding="utf-8"))
    classes = {item["python_name"]: item for item in coverage["classes"]}
    assert set(classes) == {"IMUState", "MotorState"}
    assert classes["IMUState"]["skipped_fields"] == []
    assert classes["MotorState"]["skipped_fields"] == []


def test_generator_supports_nested_idl_value_types(tmp_path: Path) -> None:
    inventory = tmp_path / "inventory.json"
    source = tmp_path / "go2.cpp"
    report = tmp_path / "report.json"
    subprocess.run(
        [
            sys.executable,
            str(SCANNER),
            "--sdk-root",
            str(SDK_ROOT),
            "--output",
            str(inventory),
            "include/unitree/idl/go2/BmsCmd_.hpp",
            "include/unitree/idl/go2/MotorCmd_.hpp",
            "include/unitree/idl/go2/LowCmd_.hpp",
        ],
        check=True,
    )
    subprocess.run(
        [
            sys.executable,
            str(GENERATOR),
            "--inventory",
            str(inventory),
            "--overrides",
            str(OVERRIDES),
            "--namespace-prefix",
            "unitree_go::msg::dds_",
            "--function",
            "BindGo2Idl",
            "--module",
            "idl",
            "--module",
            "go2",
            "--output",
            str(source),
            "--report",
            str(report),
        ],
        check=True,
    )

    generated = source.read_text(encoding="utf-8")
    assert generated.index('module, "MotorCmd"') < generated.index('module, "LowCmd"')
    assert "const std::array<::unitree_go::msg::dds_::MotorCmd_, 20>& value" in generated
    assert "const unitree_go::msg::dds_::BmsCmd_& value" in generated

    coverage = json.loads(report.read_text(encoding="utf-8"))
    classes = {item["python_name"]: item for item in coverage["classes"]}
    assert classes["LowCmd"]["skipped_fields"] == []


def test_channel_registry_generator_maps_python_message_modules(tmp_path: Path) -> None:
    inventory = tmp_path / "inventory.json"
    source = tmp_path / "channel_registry.cpp"
    report = tmp_path / "report.json"
    subprocess.run(
        [
            sys.executable,
            str(SCANNER),
            "--sdk-root",
            str(SDK_ROOT),
            "--output",
            str(inventory),
            "include/unitree/idl/go2/MotorState_.hpp",
            "include/unitree/idl/hg/IMUState_.hpp",
        ],
        check=True,
    )
    subprocess.run(
        [
            sys.executable,
            str(CHANNEL_GENERATOR),
            "--inventory",
            str(inventory),
            "--output",
            str(source),
            "--report",
            str(report),
        ],
        check=True,
    )

    generated = source.read_text(encoding="utf-8")
    assert '"unitree_sdk2_cpp.idl.go2.MotorState"' in generated
    assert '"unitree_sdk2_cpp.idl.hg.IMUState"' in generated
    assert len(json.loads(report.read_text(encoding="utf-8"))["registered_types"]) == 2
