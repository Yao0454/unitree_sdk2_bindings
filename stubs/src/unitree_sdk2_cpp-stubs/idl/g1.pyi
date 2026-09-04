"""G1-friendly aliases for the unitree_hg DDS message types."""
from typing import overload

from .hg import (
    AgvBmsState as AgvBmsState,
    BmsCmd as BmsCmd,
    BmsState as BmsState,
    MotorCmd as MotorCmd,
    HandCmd as HandCmd,
    IMUState as IMUState,
    MotorState as MotorState,
    PressSensorState as PressSensorState,
    HandState as HandState,
    LowCmd as LowCmd,
    LowState as LowState,
    MainBoardState as MainBoardState,
    SportModeState as SportModeState,
)

@overload
def compute_crc(message: LowCmd) -> int: ...
@overload
def compute_crc(message: LowState) -> int: ...
def update_crc(message: LowCmd) -> int: ...
@overload
def validate_crc(message: LowCmd) -> bool: ...
@overload
def validate_crc(message: LowState) -> bool: ...
