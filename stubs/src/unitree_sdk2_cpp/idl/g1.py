"""Generated source companion. Full types and Chinese help are in the PEP 561 stubs.
Robot APIs are provided exclusively by the separately installed native extension.
"""
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .hg import AgvBmsState as AgvBmsState, BmsCmd as BmsCmd, BmsState as BmsState, MotorCmd as MotorCmd, HandCmd as HandCmd, IMUState as IMUState, MotorState as MotorState, PressSensorState as PressSensorState, HandState as HandState, LowCmd as LowCmd, LowState as LowState, MainBoardState as MainBoardState, SportModeState as SportModeState

    def compute_crc(*args: Any, **kwargs: Any) -> Any: ...

    def update_crc(*args: Any, **kwargs: Any) -> Any: ...

    def validate_crc(*args: Any, **kwargs: Any) -> Any: ...

if not TYPE_CHECKING:
    raise ImportError("This source companion has no runtime API; install unitree-sdk2-cpp.")
