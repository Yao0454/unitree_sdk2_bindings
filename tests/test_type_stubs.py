import ast
import json
import sys
import tomllib
from argparse import Namespace
from pathlib import Path


ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT / "generator"))

from generate_type_stubs import generate  # noqa: E402


STUB_ROOT = ROOT / "stubs" / "src"
PACKAGE_ROOT = STUB_ROOT / "unitree_sdk2_cpp-stubs"


def _arguments(output: Path) -> Namespace:
    return Namespace(
        idl_inventory=ROOT / "generated" / "idl_inventory.json",
        robot_inventory=ROOT / "generated" / "robot_inventory.json",
        classification=ROOT / "generated" / "robot_binding_report.json",
        policy=ROOT / "generator" / "robot_read_only_policy.json",
        read_only_report=ROOT / "generated" / "robot_read_only_report.json",
        idl_report=[
            ROOT / "generated" / "idl_go2_report.json",
            ROOT / "generated" / "idl_hg_report.json",
            ROOT / "generated" / "idl_hg_doubleimu_report.json",
            ROOT / "generated" / "idl_ros2_report.json",
        ],
        output=output,
    )


def test_checked_in_stubs_are_current(tmp_path: Path) -> None:
    manifest = generate(_arguments(tmp_path))
    expected_paths = {
        path.relative_to(STUB_ROOT)
        for package in (PACKAGE_ROOT, STUB_ROOT / "unitree_sdk2_cpp")
        for path in package.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts
    }
    actual_paths = {
        path.relative_to(tmp_path) for path in tmp_path.rglob("*") if path.is_file()
    }
    assert actual_paths == expected_paths
    for relative_path in expected_paths:
        assert (tmp_path / relative_path).read_bytes() == (
            STUB_ROOT / relative_path
        ).read_bytes()

    assert manifest["summary"] == {
        "idl_classes": 64,
        "idl_properties": 341,
        "manifest_entries": 1213,
        "robot_classes": 121,
        "robot_public_signatures": 634,
        "status": {"AVAILABLE": 1167, "SIGNATURE_ONLY": 46},
    }


def test_every_stub_is_valid_python_syntax() -> None:
    for path in PACKAGE_ROOT.rglob("*.pyi"):
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))


def test_top_level_modules_are_explicitly_reexported_for_auto_import() -> None:
    root_stub = (PACKAGE_ROOT / "__init__.pyi").read_text(encoding="utf-8")
    for module_name in ("channel", "idl", "robot"):
        assert f"from . import {module_name} as {module_name}" in root_stub
    assert '__all__ = ["channel", "idl", "robot", "OsHelper"]' in root_stub


def test_g1_message_aliases_are_explicitly_reexported() -> None:
    g1_stub = (PACKAGE_ROOT / "idl" / "g1.pyi").read_text(encoding="utf-8")
    for name in (
        "AgvBmsState",
        "BmsCmd",
        "BmsState",
        "MotorCmd",
        "HandCmd",
        "IMUState",
        "MotorState",
        "PressSensorState",
        "HandState",
        "LowCmd",
        "LowState",
        "MainBoardState",
        "SportModeState",
    ):
        assert f"{name} as {name}" in g1_stub


def test_stub_distribution_uses_importable_package_layout() -> None:
    configuration = tomllib.loads(
        (ROOT / "stubs" / "pyproject.toml").read_text(encoding="utf-8")
    )
    setuptools = configuration["tool"]["setuptools"]
    assert "py-modules" not in setuptools
    assert setuptools["packages"] == [
        "unitree_sdk2_cpp-stubs",
        "unitree_sdk2_cpp-stubs.idl",
        "unitree_sdk2_cpp-stubs.robot",
        "unitree_sdk2_cpp",
        "unitree_sdk2_cpp.idl",
        "unitree_sdk2_cpp.robot",
    ]
    assert PACKAGE_ROOT.name == "unitree_sdk2_cpp-stubs"
    assert not (STUB_ROOT / "unitree_sdk2_cpp.py").exists()


def test_distribution_contains_only_pep561_stub_files() -> None:
    stub_paths = set(PACKAGE_ROOT.rglob("*.pyi"))
    assert len(stub_paths) == 17
    assert not list(PACKAGE_ROOT.rglob("*.py"))


def test_public_declarations_include_hover_help() -> None:
    counts = {"classes": 0, "functions": 0, "properties": 0}
    for path in PACKAGE_ROOT.rglob("*.pyi"):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                assert ast.get_docstring(node), (path, node.name)
                counts["classes"] += 1
            elif isinstance(node, ast.FunctionDef):
                text = ast.get_docstring(node) or ""
                assert "Examples:" in text, (path, node.name)
                if any(isinstance(d, ast.Name) and d.id == "property" for d in node.decorator_list):
                    counts["properties"] += 1
                elif not any(isinstance(d, ast.Attribute) and d.attr == "setter" for d in node.decorator_list):
                    assert "Args:" in text and "Returns:" in text
                    assert "AVAILABLE" in text or "SIGNATURE_ONLY" in text
                    counts["functions"] += 1
    assert counts == {"classes": 189, "functions": 867, "properties": 346}


def test_namespaces_are_reexported_and_sources_cannot_fake_api() -> None:
    for namespace, names in {
        "idl": ("g1", "go2", "hg", "hg_doubleimu", "ros2"),
        "robot": ("a2", "as2", "b2", "g1", "go2", "h1", "h2", "r1"),
    }.items():
        source = (PACKAGE_ROOT / namespace / "__init__.pyi").read_text()
        for name in names:
            assert f"from . import {name} as {name}" in source
    sources = STUB_ROOT / "unitree_sdk2_cpp"
    assert {p.relative_to(sources).with_suffix(".pyi") for p in sources.rglob("*.py")} == {
        p.relative_to(PACKAGE_ROOT) for p in PACKAGE_ROOT.rglob("*.pyi")
    }
    for path in sources.rglob("*.py"):
        tree = ast.parse(path.read_text())
        # Public API declarations may only exist in the TYPE_CHECKING branch.
        assert not any(isinstance(n, (ast.ClassDef, ast.FunctionDef)) and not n.name.startswith("_") for n in tree.body)


def test_manifest_exposes_motion_signatures_without_executing_them() -> None:
    manifest = json.loads(
        (PACKAGE_ROOT / "api_manifest.json").read_text(encoding="utf-8")
    )
    g1_move = [
        item
        for item in manifest["entries"]
        if item["python_path"] == "unitree_sdk2_cpp.robot.g1.LocoClient.move"
    ]
    assert len(g1_move) == 2
    assert {item["status"] for item in g1_move} == {"AVAILABLE"}
    assert {item["safety"] for item in g1_move} == {"MOTION_COMMAND"}

    get_fsm_id = next(
        item
        for item in manifest["entries"]
        if item["python_path"] == "unitree_sdk2_cpp.robot.g1.LocoClient.get_fsm_id"
    )
    assert get_fsm_id["status"] == "AVAILABLE"
    assert get_fsm_id["python_return"] == "tuple[int, int]"

    for path in {
        "unitree_sdk2_cpp.robot.b2.ServiceState.__init__",
        "unitree_sdk2_cpp.robot.go2.ServiceState.__init__",
    }:
        constructor = next(
            item for item in manifest["entries"] if item["python_path"] == path
        )
        assert constructor["status"] == "AVAILABLE"

    set_velocity = next(
        item
        for item in manifest["entries"]
        if item["python_path"] == "unitree_sdk2_cpp.robot.g1.LocoClient.set_velocity"
    )
    assert set_velocity["status"] == "AVAILABLE"

    trajectory = next(
        item
        for item in manifest["entries"]
        if item["python_path"]
        == "unitree_sdk2_cpp.robot.b2.SportClient.trajectory_follow"
    )
    assert trajectory["binding_strategy"] == "MUTABLE_INPUT_COPY"

    json_value = next(
        item
        for item in manifest["entries"]
        if item["python_path"]
        == "unitree_sdk2_cpp.robot.g1.MoveParameter.to_json"
    )
    assert json_value["status"] == "AVAILABLE"
    assert json_value["binding_strategy"] == "JSON_DICT_OUTPUT"
    assert json_value["python_return"] == "dict[str, Any]"

    lease_cache = next(
        item
        for item in manifest["entries"]
        if item["python_path"] == "unitree_sdk2_cpp.robot.LeaseCache.renewal"
    )
    assert lease_cache["status"] == "AVAILABLE"
    assert lease_cache["binding_strategy"] == "DIRECT"

    crc_entries = [
        item
        for item in manifest["entries"]
        if item["python_path"] == "unitree_sdk2_cpp.idl.g1.compute_crc"
    ]
    assert len(crc_entries) == 2
    assert {item["status"] for item in crc_entries} == {"AVAILABLE"}
    assert {item["binding_strategy"] for item in crc_entries} == {"CRC_WRAPPER"}
