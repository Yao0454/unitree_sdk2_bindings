"""Generated source companion. Full types and Chinese help are in the PEP 561 stubs.
Robot APIs are provided exclusively by the separately installed native extension.
"""
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from . import g1 as g1

    from . import go2 as go2

    from . import hg as hg

    from . import hg_doubleimu as hg_doubleimu

    from . import ros2 as ros2

if not TYPE_CHECKING:
    raise ImportError("This source companion has no runtime API; install unitree-sdk2-cpp.")
