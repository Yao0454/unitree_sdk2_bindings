"""Generated source companion. Full types and Chinese help are in the PEP 561 stubs.
Robot APIs are provided exclusively by the separately installed native extension.
"""
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    class AgvBmsState:
        pass

    class BmsCmd:
        pass

    class BmsState:
        pass

    class MotorCmd:
        pass

    class HandCmd:
        pass

    class IMUState:
        pass

    class MotorState:
        pass

    class PressSensorState:
        pass

    class HandState:
        pass

    class LowCmd:
        pass

    class LowState:
        pass

    class MainBoardState:
        pass

    class SportModeState:
        pass

if not TYPE_CHECKING:
    raise ImportError("This source companion has no runtime API; install unitree-sdk2-cpp.")
