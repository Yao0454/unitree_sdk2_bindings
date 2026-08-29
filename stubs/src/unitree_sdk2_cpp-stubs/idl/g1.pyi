"""G1-friendly aliases for the unitree_hg DDS message types."""
from typing import overload

from .hg import (
    AgvBmsState,
    BmsCmd,
    BmsState,
    MotorCmd,
    HandCmd,
    IMUState,
    MotorState,
    PressSensorState,
    HandState,
    LowCmd,
    LowState,
    MainBoardState,
    SportModeState,
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
