import json
import sys
from pathlib import Path

ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT / "generator"))

from api_parity import parity  # noqa: E402
from diff_inventory import diff  # noqa: E402


def _inventory() -> dict:
    return json.loads(
        (ROOT / "generated" / "idl_inventory.json").read_text(encoding="utf-8")
    )


def _reports() -> list[dict]:
    return [
        json.loads(path.read_text(encoding="utf-8"))
        for path in sorted((ROOT / "generated").glob("idl_*_report.json"))
        if path.name != "idl_parity_report.json"
    ]


def test_checked_in_idl_reports_have_no_missing_classes() -> None:
    result = parity(_inventory(), _reports())
    assert result["classes"]["missing"] == []
    assert result["classes"]["extra"] == []
    assert result["classes"]["cpp"] == 64
    assert result["classes"]["python"] == 64
    assert result["methods"]["missing"] == []
    assert result["fields"]["missing"] == []


def test_inventory_diff_reports_added_and_removed_methods() -> None:
    old = {"classes": [{"namespace": "demo", "name": "Thing", "methods": [], "constructors": []}]}
    new = {"classes": [{"namespace": "demo", "name": "Thing", "methods": [{"name": "Run", "return_type": "void", "parameters": [], "is_const": False, "is_noexcept": False}], "constructors": []}, {"namespace": "demo", "name": "NewThing", "methods": [], "constructors": []}]}
    result = diff(old, new)
    assert result["added_classes"] == ["demo::NewThing"]
    assert result["removed_classes"] == []
    assert result["changed_methods"] == [{"class": "demo::Thing", "added": ["Run()"], "removed": []}]


def test_parity_distinguishes_manual_and_missing_api() -> None:
    inventory = {
        "classes": [
            {
                "namespace": "demo",
                "name": "Thing",
                "fields": [],
                "constructors": [],
                "methods": [
                    {
                        "name": "Safe",
                        "return_type": "void",
                        "parameters": [],
                        "is_const": False,
                        "is_noexcept": False,
                    },
                    {
                        "name": "Callback",
                        "return_type": "void",
                        "parameters": [],
                        "is_const": False,
                        "is_noexcept": False,
                    },
                ],
            }
        ],
        "diagnostics": [],
    }
    reports = [{"classes": [{"qualified_name": "demo::Thing", "properties": []}]}]
    overrides = {
        "methods": {
            "demo::Thing::Callback()": {"status": "MANUAL"},
        }
    }
    result = parity(inventory, reports, overrides)
    assert result["methods"]["counts"]["MANUAL"] == 1
    assert result["methods"]["counts"]["MISSING"] == 1
    assert result["methods"]["missing"] == ["demo::Thing::Safe()"]
