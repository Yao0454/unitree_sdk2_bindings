import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest


SDK_ROOT = Path(__file__).parents[2]
SCANNER = SDK_ROOT / "unitree_sdk2_bindings" / "generator" / "scan_headers.py"
sys.path.insert(0, str(SDK_ROOT / "unitree_sdk2_bindings" / "generator"))
from scan_headers import (  # noqa: E402
    _parameters,
    _headers_from_arguments,
    decode_clang_ast_stream,
    discover_declarations,
)


def _parameter(expression: dict, type_name: str = "int") -> dict:
    return {
        "kind": "ParmVarDecl",
        "name": "value",
        "type": {"qualType": type_name},
        "init": "c",
        "inner": [expression],
    }


@pytest.mark.parametrize(
    ("expression", "type_name", "expected"),
    [
        ({"kind": "CXXBoolLiteralExpr", "value": False}, "bool", "false"),
        ({"kind": "IntegerLiteral", "value": "42"}, "int", "42"),
        ({"kind": "FloatingLiteral", "value": "1"}, "float", "1.0"),
        ({"kind": "StringLiteral", "value": '"eth0"'}, "const char *", '"eth0"'),
        (
            {
                "kind": "UnaryOperator",
                "opcode": "-",
                "inner": [{"kind": "IntegerLiteral", "value": "1"}],
            },
            "int",
            "-1",
        ),
        (
            {
                "kind": "ImplicitCastExpr",
                "inner": [
                    {
                        "kind": "DeclRefExpr",
                        "type": {"qualType": "demo::Mode"},
                        "referencedDecl": {
                            "kind": "EnumConstantDecl",
                            "name": "PASSIVE",
                        },
                    }
                ],
            },
            "Mode",
            "demo::Mode::PASSIVE",
        ),
    ],
)
def test_parameter_defaults_extract_safe_literals(
    expression: dict, type_name: str, expected: str
) -> None:
    parameter = _parameters({"inner": [_parameter(expression, type_name)]})[0]
    assert parameter.has_default
    assert parameter.default_value == expected


def test_parameter_default_rejects_function_calls() -> None:
    parameter = _parameters({"inner": [_parameter({"kind": "CallExpr", "inner": []})]})[
        0
    ]
    assert parameter.has_default
    assert parameter.default_value is None


def test_declaration_discovery_ignores_struct_return_types() -> None:
    candidates = discover_declarations(SDK_ROOT / "include/unitree/common/os.hpp")
    names = {candidate.name for candidate in candidates}
    assert "OsHelper" in names
    assert "UT_SCHED_POLICY" in names
    assert "passwd" not in names


def test_clang_10_dump_prefixes_are_accepted() -> None:
    output = 'Dumping demo::A:\n{"kind": "A"}\nDumping demo::B:\n{"kind": "B"}\n'
    assert decode_clang_ast_stream(output) == [{"kind": "A"}, {"kind": "B"}]


def test_header_discovery_ignores_macos_appledouble_files(tmp_path: Path) -> None:
    include = tmp_path / "include"
    include.mkdir()
    (include / "message.hpp").write_text("struct Message {};\n", encoding="utf-8")
    (include / "._message.hpp").write_bytes(b"\x00\x05\x16\x07")
    assert _headers_from_arguments(tmp_path, ["include"]) == [include / "message.hpp"]


@pytest.mark.skipif(shutil.which("clang++") is None, reason="clang++ is required")
def test_scanner_extracts_idl_overloads_and_types(tmp_path: Path) -> None:
    output = tmp_path / "inventory.json"
    result = subprocess.run(
        [
            sys.executable,
            str(SCANNER),
            "--sdk-root",
            str(SDK_ROOT),
            "--output",
            str(output),
            "include/unitree/idl/go2/MotorState_.hpp",
            "include/unitree/idl/go2/IMUState_.hpp",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr

    inventory = json.loads(output.read_text(encoding="utf-8"))
    classes = {item["name"]: item for item in inventory["classes"]}
    assert set(classes) == {"IMUState_", "MotorState_"}
    assert classes["MotorState_"]["namespace"] == "unitree_go::msg::dds_"

    motor_methods = classes["MotorState_"]["methods"]
    q_overloads = [method for method in motor_methods if method["name"] == "q"]
    assert len(q_overloads) == 3
    assert {method["return_type"] for method in q_overloads} == {
        "float",
        "float &",
        "void",
    }

    imu_fields = {field["name"]: field for field in classes["IMUState_"]["fields"]}
    assert imu_fields["quaternion_"]["type"] == "std::array<float, 4>"
    assert inventory["diagnostics"] == []


@pytest.mark.skipif(shutil.which("clang++") is None, reason="clang++ is required")
def test_scanner_extracts_literal_default_values_from_clang(tmp_path: Path) -> None:
    header = tmp_path / "defaults.hpp"
    header.write_text(
        """
#include <string>
namespace demo {
enum class Mode { Passive };
class Defaults {
public:
  void Configure(bool enabled = false, int stage = -1, float duration = 1.f,
                 const std::string& label = "ready",
                 Mode mode = Mode::Passive);
};
}
""",
        encoding="utf-8",
    )
    output = tmp_path / "inventory.json"
    result = subprocess.run(
        [
            sys.executable,
            str(SCANNER),
            "--sdk-root",
            str(SDK_ROOT),
            "--output",
            str(output),
            str(header),
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr

    inventory = json.loads(output.read_text(encoding="utf-8"))
    defaults = inventory["classes"][0]["methods"][0]["parameters"]
    assert [item["default_value"] for item in defaults] == [
        "false",
        "-1",
        "1.0",
        '"ready"',
        "demo::Mode::Passive",
    ]
