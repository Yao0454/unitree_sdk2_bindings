"""Generated source companion. Full types and Chinese help are in the PEP 561 stubs.
Robot APIs are provided exclusively by the separately installed native extension.
"""
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    class AudioClient:
        pass

    class JsonizeDataVecFloat:
        pass

    class JsonizeVelocityCommand:
        pass

    class LedControlParameter:
        pass

    class LocoClient:
        pass

    class PlayStopParameter:
        pass

    class PlayStreamParameter:
        pass

    class TtsMakerParameter:
        pass

if not TYPE_CHECKING:
    raise ImportError("This source companion has no runtime API; install unitree-sdk2-cpp.")
