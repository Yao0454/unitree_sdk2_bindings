"""Design-time placeholder for the Linux ``unitree_sdk2_cpp`` extension.

The companion ``unitree_sdk2_cpp-stubs`` package supplies the type surface.
When the compiled extension is installed in the same environment, Python loads
the extension before this source module.
"""

from types import ModuleType as _ModuleType


channel: _ModuleType
idl: _ModuleType
robot: _ModuleType


class OsHelper:
    """Indexed here for auto-import; its full signature lives in the stub."""


__all__ = ["channel", "idl", "robot", "OsHelper"]


raise ImportError(
    "unitree-sdk2-cpp-stubs provides IDE completion only; install the compiled "
    "unitree-sdk2-cpp extension on supported Linux x86_64 or aarch64 systems "
    "to import unitree_sdk2_cpp at runtime"
)
