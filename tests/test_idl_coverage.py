import json
from pathlib import Path


BINDINGS_ROOT = Path(__file__).parents[1]


def test_checked_in_idl_inventory_and_reports_are_complete() -> None:
    inventory = json.loads(
        (BINDINGS_ROOT / "generated" / "idl_inventory.json").read_text(
            encoding="utf-8"
        )
    )
    assert len(inventory["headers"]) == 64
    assert len(inventory["classes"]) == 64
    assert inventory["diagnostics"] == []

    expected_classes = {
        "idl_go2_report.json": 26,
        "idl_hg_report.json": 13,
        "idl_hg_doubleimu_report.json": 1,
        "idl_ros2_report.json": 24,
    }
    covered_classes = 0
    covered_properties = 0
    for name, expected_count in expected_classes.items():
        report = json.loads(
            (BINDINGS_ROOT / "generated" / name).read_text(encoding="utf-8")
        )
        assert len(report["classes"]) == expected_count
        assert all(not item["skipped_fields"] for item in report["classes"])
        covered_classes += len(report["classes"])
        covered_properties += sum(
            len(item["properties"]) for item in report["classes"]
        )

    assert covered_classes == 64
    assert covered_properties == 341

    channel_report = json.loads(
        (BINDINGS_ROOT / "generated" / "channel_registry_report.json").read_text(
            encoding="utf-8"
        )
    )
    assert len(channel_report["registered_types"]) == 64
    assert len(set(channel_report["registered_types"])) == 64

    parity_report = json.loads(
        (BINDINGS_ROOT / "generated" / "idl_parity_report.json").read_text(
            encoding="utf-8"
        )
    )
    assert parity_report["classes"]["coverage"] == 1.0
    assert parity_report["fields"]["missing"] == []
    assert parity_report["methods"]["missing"] == []
