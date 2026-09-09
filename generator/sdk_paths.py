"""SDK source discovery shared by the scanner and its source-level tests."""

from __future__ import annotations

import os
from pathlib import Path


def find_sdk_root(explicit: Path | None = None) -> Path:
    bindings_root = Path(__file__).resolve().parents[1]
    configured = explicit or os.environ.get("UNITREE_SDK_ROOT")
    if configured:
        selected = Path(configured).expanduser()
        if not selected.is_absolute():
            selected = bindings_root / selected
    elif (bindings_root / "thirdparty/unitree_sdk2").exists():
        selected = bindings_root / "thirdparty/unitree_sdk2"
    else:
        selected = bindings_root.parent
    selected = selected.resolve()
    if not (selected / "include/unitree/robot/channel/channel_factory.hpp").is_file():
        raise FileNotFoundError(
            f"Unitree SDK2 headers not found in {selected}. "
            "Clone the SDK into thirdparty/unitree_sdk2 or set UNITREE_SDK_ROOT."
        )
    return selected
