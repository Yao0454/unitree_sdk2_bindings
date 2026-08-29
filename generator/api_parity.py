"""Compare a Clang inventory with checked-in generated binding reports."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from collections import Counter
from typing import Any, Iterable


STATUSES = {"SUPPORTED", "MANUAL", "UNSUPPORTED", "IGNORED", "MISSING"}


def qualified_name(item: dict[str, Any]) -> str:
    namespace = item.get("namespace", "")
    return f"{namespace}::{item['name']}" if namespace else item["name"]


def class_signatures(item: dict[str, Any]) -> set[str]:
    signatures: set[str] = set()
    for method in [*item.get("constructors", []), *item.get("methods", [])]:
        parameters = ", ".join(parameter["type"] for parameter in method["parameters"])
        suffix = " const" if method.get("is_const") else ""
        if method.get("is_noexcept"):
            suffix += " noexcept"
        signatures.add(f"{method['name']}({parameters}){suffix}")
    return signatures


def method_signature(method: dict[str, Any]) -> str:
    parameters = ", ".join(parameter["type"] for parameter in method["parameters"])
    suffix = " const" if method.get("is_const") else ""
    if method.get("is_noexcept"):
        suffix += " noexcept"
    return f"{method['name']}({parameters}){suffix}"


def override_status(value: dict[str, Any] | None) -> str | None:
    if not value:
        return None
    if "status" in value:
        status = str(value["status"]).upper()
        if status not in STATUSES:
            raise ValueError(f"invalid binding status: {status}")
        return status
    if value.get("manual"):
        return "MANUAL"
    if value.get("unsupported"):
        return "UNSUPPORTED"
    if value.get("ignored"):
        return "IGNORED"
    return None


def classify_method(
    cpp_name: str,
    method: dict[str, Any],
    class_status: str,
    properties: set[str],
    overrides: dict[str, Any],
) -> str:
    key = f"{cpp_name}::{method_signature(method)}"
    status = override_status(overrides.get("methods", {}).get(key))
    if status:
        return status
    if class_status != "SUPPORTED":
        return class_status
    if method.get("is_constructor"):
        return "SUPPORTED" if not method["parameters"] else "IGNORED"
    if method["name"] in {"operator==", "operator!="}:
        return "SUPPORTED"
    if method["name"] not in properties:
        return "MISSING"
    if not method["parameters"] and method.get("is_const"):
        return "SUPPORTED"
    if len(method["parameters"]) == 1 and method.get("return_type") == "void":
        return "IGNORED" if "&&" in method["parameters"][0]["type"] else "SUPPORTED"
    # Mutable-reference getters cannot be exposed safely with the generator's
    # copy-semantics policy; the const getter already represents the property.
    return "IGNORED"


def parity(
    inventory: dict[str, Any],
    reports: Iterable[dict[str, Any]],
    overrides: dict[str, Any] | None = None,
) -> dict[str, Any]:
    overrides = overrides or {}
    cpp_classes = {qualified_name(item): item for item in inventory.get("classes", [])}
    bound_classes = {
        item["qualified_name"]: item
        for report in reports
        for item in report.get("classes", [])
    }
    missing = sorted(set(cpp_classes) - set(bound_classes))
    extra = sorted(set(bound_classes) - set(cpp_classes))
    class_details: list[dict[str, Any]] = []
    method_details: list[dict[str, Any]] = []
    field_details: list[dict[str, Any]] = []
    for name, cpp_class in sorted(cpp_classes.items()):
        class_override = overrides.get("classes", {}).get(name)
        class_status = override_status(class_override)
        if class_status is None:
            class_status = "SUPPORTED" if name in bound_classes else "MISSING"
        class_details.append({"name": name, "status": class_status})
        report = bound_classes.get(name, {})
        properties = set(report.get("properties", []))
        for method in [
            *cpp_class.get("constructors", []),
            *cpp_class.get("methods", []),
        ]:
            method_details.append(
                {
                    "name": f"{name}::{method_signature(method)}",
                    "status": classify_method(
                        name, method, class_status, properties, overrides
                    ),
                }
            )
        for field in cpp_class.get("fields", []):
            property_name = field["name"].removesuffix("_")
            field_details.append(
                {
                    "name": f"{name}::{field['name']}",
                    "status": (
                        class_status
                        if class_status != "SUPPORTED"
                        else "SUPPORTED"
                        if property_name in properties
                        else "MISSING"
                    ),
                }
            )

    def status_summary(details: list[dict[str, Any]]) -> dict[str, Any]:
        counts = Counter(item["status"] for item in details)
        return {
            "counts": {status: counts.get(status, 0) for status in sorted(STATUSES)},
            "missing": [item["name"] for item in details if item["status"] == "MISSING"],
        }

    return {
        "schema_version": 2,
        "classes": {
            "cpp": len(cpp_classes),
            "python": len(bound_classes),
            "missing": missing,
            "extra": extra,
            "coverage": (len(bound_classes) / len(cpp_classes) if cpp_classes else 0.0),
        },
        "methods": {
            "cpp": sum(len(class_signatures(item)) for item in cpp_classes.values()),
            "generated_properties": sum(
                len(item.get("properties", []))
                for item in bound_classes.values()
            ),
            **status_summary(method_details),
        },
        "fields": {"cpp": len(field_details), **status_summary(field_details)},
        "status": {
            "classes": status_summary(class_details),
            "methods": status_summary(method_details),
            "fields": status_summary(field_details),
        },
        "diagnostics": inventory.get("diagnostics", []),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--report", type=Path, action="append", required=True)
    parser.add_argument("--overrides", type=Path)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    inventory = json.loads(arguments.inventory.read_text(encoding="utf-8"))
    reports = [
        json.loads(path.read_text(encoding="utf-8")) for path in arguments.report
    ]
    overrides = (
        json.loads(arguments.overrides.read_text(encoding="utf-8"))
        if arguments.overrides
        else {}
    )
    result = parity(inventory, reports, overrides)
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if arguments.output:
        arguments.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    print(
        f"Classes: {result['classes']['python']}/{result['classes']['cpp']} "
        f"({len(result['classes']['missing'])} missing)",
    )
    return 1 if result["classes"]["missing"] or result["diagnostics"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
