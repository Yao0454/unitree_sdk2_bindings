"""Report API changes between two Clang JSON inventories."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

try:
    from .api_parity import class_signatures, qualified_name
except ImportError:  # Support direct execution: python generator/diff_inventory.py
    from api_parity import class_signatures, qualified_name


def diff(old: dict[str, Any], new: dict[str, Any]) -> dict[str, Any]:
    old_classes = {qualified_name(item): item for item in old.get("classes", [])}
    new_classes = {qualified_name(item): item for item in new.get("classes", [])}
    added_classes = sorted(set(new_classes) - set(old_classes))
    removed_classes = sorted(set(old_classes) - set(new_classes))
    changed_methods: list[dict[str, Any]] = []
    for name in sorted(set(old_classes) & set(new_classes)):
        before = class_signatures(old_classes[name])
        after = class_signatures(new_classes[name])
        added = sorted(after - before)
        removed = sorted(before - after)
        if added or removed:
            changed_methods.append(
                {"class": name, "added": added, "removed": removed}
            )
    return {
        "schema_version": 1,
        "added_classes": added_classes,
        "removed_classes": removed_classes,
        "changed_methods": changed_methods,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("old", type=Path)
    parser.add_argument("new", type=Path)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    result = diff(
        json.loads(arguments.old.read_text(encoding="utf-8")),
        json.loads(arguments.new.read_text(encoding="utf-8")),
    )
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if arguments.output:
        arguments.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
