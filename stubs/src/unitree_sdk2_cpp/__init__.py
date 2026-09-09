"""Generated source companion. Full types and Chinese help are in the PEP 561 stubs.
Robot APIs are provided exclusively by the separately installed native extension.
"""
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from . import channel as channel

    from . import idl as idl

    from . import robot as robot

    class OsHelper:
        pass

# This function lives in the source companion package's __init__.py. Do not
# rename the binary or use a different module name: PyInit_unitree_sdk2_cpp is
# the existing extension ABI. Only a native extension can satisfy this loader.
def _load_native() -> None:
    import os
    import sys
    from importlib.machinery import EXTENSION_SUFFIXES, ExtensionFileLoader, FileFinder
    from importlib.util import module_from_spec
    from pathlib import Path

    installed_root = str(Path(__file__).resolve().parent.parent)
    # The adjacent binary is preferred. Additional paths support an editable
    # native installation whose extension is exposed through a .pth file.
    for entry in dict.fromkeys([installed_root, *sys.path]):
        if not isinstance(entry, str):
            continue
        finder = FileFinder(entry or os.getcwd(), (ExtensionFileLoader, EXTENSION_SUFFIXES))
        spec = finder.find_spec(__name__)
        if spec is None or not isinstance(spec.loader, ExtensionFileLoader):
            continue
        # Preserve real linker/ABI errors rather than hiding them as a missing
        # package or falling back to a mock implementation.
        native = module_from_spec(spec)
        sys.modules[__name__] = native
        spec.loader.exec_module(native)
        return
    raise ImportError(
        "unitree-sdk2-cpp-stubs supplies type hints, not the robot runtime. "
        "Install unitree-sdk2-cpp into this Python environment on supported Linux "
        "x86_64/aarch64 to execute the API."
    )


if not TYPE_CHECKING:
    _load_native()
