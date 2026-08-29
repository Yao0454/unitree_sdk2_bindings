"""Classify robot client methods by binding strategy and hardware risk."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


MOTION_CLIENTS = {
    "AgvClient",
    "G1ArmActionClient",
    "H2ArmActionClient",
    "LocoClient",
    "ObstaclesAvoidClient",
    "SportClient",
}
READ_ONLY_NAMES = {
    "Applied",
    "ServiceList",
}
LIFECYCLE_NAMES = {
    "Init",
    "SetTimeout",
    "WaitApplied",
    "WaitLeaseApplied",
}
CLIENT_BASE_NAMES = {"Client", "ClientBase", "ClientStub", "LeaseClient"}


def qualified_name(item: dict[str, Any]) -> str:
    namespace = item.get("namespace", "")
    return f"{namespace}::{item['name']}" if namespace else item["name"]


def method_signature(method: dict[str, Any]) -> str:
    parameters = ", ".join(item["type"] for item in method["parameters"])
    suffix = " const" if method.get("is_const") else ""
    return f"{method['name']}({parameters}){suffix}"


def binding_strategy(method: dict[str, Any]) -> tuple[str, str]:
    types = [method.get("return_type", ""), *(
        item["type"] for item in method.get("parameters", [])
    )]
    if method["name"].startswith("Subscribe") or any(
        "Callback" in type_name or "std::function" in type_name
        for type_name in types
    ):
        return "CALLBACK_MANUAL", "callback lifetime and GIL handling are required"
    if any("*" in type_name for type_name in types):
        return "POINTER_MANUAL", "raw pointer ownership cannot be inferred"
    mutable_outputs = [
        item["name"] or f"arg{index}"
        for index, item in enumerate(method.get("parameters", []))
        if "&" in item["type"] and not item["type"].lstrip().startswith("const ")
    ]
    if mutable_outputs:
        return (
            "OUTPUT_WRAPPER",
            "mutable C++ outputs should be returned as Python values: "
            + ", ".join(mutable_outputs),
        )
    if "&" in method.get("return_type", ""):
        return "REFERENCE_POLICY", "reference return needs an explicit lifetime policy"
    return "DIRECT", "arguments and return value have direct pybind11 conversions"


def safety_class(client: dict[str, Any], method: dict[str, Any]) -> tuple[str, str]:
    name = method["name"]
    if name in LIFECYCLE_NAMES:
        return "INITIALIZATION", "creates or configures client-side SDK state"
    if name.startswith("Subscribe"):
        return "HARDWARE_SIDE_EFFECT", "installs a live DDS callback"
    if name in READ_ONLY_NAMES or name.startswith(("Get", "Check", "Is")):
        return "READ_ONLY", "queries state without an intended command side effect"
    if client["name"] in MOTION_CLIENTS:
        return "MOTION_COMMAND", "may change robot posture, gait, arm, or velocity"
    if client["name"] == "MotionSwitcherClient" and name not in {
        "CheckMode",
        "GetSilent",
    }:
        return "MOTION_COMMAND", "changes the active robot motion service or mode"
    return "HARDWARE_SIDE_EFFECT", "changes robot or service state"


def classify(inventory: dict[str, Any]) -> dict[str, Any]:
    clients = [
        item
        for item in inventory.get("classes", [])
        if item["name"].endswith("Client") or item["name"] in CLIENT_BASE_NAMES
    ]
    class_reports: list[dict[str, Any]] = []
    safety_counts: Counter[str] = Counter()
    strategy_counts: Counter[str] = Counter()
    for client in clients:
        methods: list[dict[str, str]] = []
        for method in client.get("methods", []):
            if method.get("access") != "public":
                continue
            safety, safety_reason = safety_class(client, method)
            strategy, strategy_reason = binding_strategy(method)
            safety_counts[safety] += 1
            strategy_counts[strategy] += 1
            methods.append(
                {
                    "name": method["name"],
                    "signature": method_signature(method),
                    "safety": safety,
                    "safety_reason": safety_reason,
                    "binding_strategy": strategy,
                    "binding_reason": strategy_reason,
                }
            )
        class_reports.append(
            {
                "qualified_name": qualified_name(client),
                "binding_status": "MANUAL",
                "reason": "RPC/DDS lifetime and hardware risk require an explicit binding policy",
                "methods": methods,
            }
        )

    return {
        "schema_version": 1,
        "source": "generated/robot_inventory.json",
        "summary": {
            "headers": len(inventory.get("headers", [])),
            "classes": len(inventory.get("classes", [])),
            "enums": len(inventory.get("enums", [])),
            "client_classes": len(clients),
            "client_methods": sum(len(item["methods"]) for item in class_reports),
            "safety": dict(sorted(safety_counts.items())),
            "binding_strategy": dict(sorted(strategy_counts.items())),
            "diagnostics": len(inventory.get("diagnostics", [])),
        },
        "clients": class_reports,
        "diagnostics": inventory.get("diagnostics", []),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()
    inventory = json.loads(arguments.inventory.read_text(encoding="utf-8"))
    report = classify(inventory)
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        f"Classified {report['summary']['client_classes']} clients and "
        f"{report['summary']['client_methods']} public methods"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
