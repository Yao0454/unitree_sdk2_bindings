"""Full SDK signature preview; see api_manifest.json for availability."""
from __future__ import annotations

import enum
from collections.abc import Callable, Mapping, Sequence
from typing import Any, overload

from . import Client, ClientBase

class JsonizeDataVecFloat(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::h1::JsonizeDataVecFloat::JsonizeDataVecFloat()."""
        ...
    data: list[float]
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class JsonizeTargetPos(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::h1::JsonizeTargetPos::JsonizeTargetPos()."""
        ...
    x: float
    y: float
    yaw: float
    relative: bool
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class JsonizeVelocityCommand(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::h1::JsonizeVelocityCommand::JsonizeVelocityCommand()."""
        ...
    velocity: list[float]
    duration: float
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class LocoClient(Client):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::h1::LocoClient::LocoClient()."""
        ...
    def init(self) -> None:
        """AVAILABLE | INITIALIZATION | DIRECT. C++: Init()."""
        ...
    def get_fsm_id(self) -> tuple[int, int]:
        """AVAILABLE | READ_ONLY | OUTPUT_WRAPPER. C++: GetFsmId(int &)."""
        ...
    def get_fsm_mode(self) -> tuple[int, int]:
        """AVAILABLE | READ_ONLY | OUTPUT_WRAPPER. C++: GetFsmMode(int &)."""
        ...
    def get_balance_mode(self) -> tuple[int, int]:
        """AVAILABLE | READ_ONLY | OUTPUT_WRAPPER. C++: GetBalanceMode(int &)."""
        ...
    def get_swing_height(self) -> tuple[int, float]:
        """AVAILABLE | READ_ONLY | OUTPUT_WRAPPER. C++: GetSwingHeight(float &)."""
        ...
    def get_stand_height(self) -> tuple[int, float]:
        """AVAILABLE | READ_ONLY | OUTPUT_WRAPPER. C++: GetStandHeight(float &)."""
        ...
    def get_phase(self) -> tuple[int, list[float]]:
        """AVAILABLE | READ_ONLY | OUTPUT_WRAPPER. C++: GetPhase(std::vector<float> &)."""
        ...
    def enable_odom(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: EnableOdom()."""
        ...
    def disable_odom(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: DisableOdom()."""
        ...
    def get_odom(self) -> tuple[int, float, float, float]:
        """AVAILABLE | READ_ONLY | OUTPUT_WRAPPER. C++: GetOdom(float &, float &, float &)."""
        ...
    def set_fsm_id(self, fsm_id: int) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: SetFsmId(int)."""
        ...
    def set_balance_mode(self, balance_mode: int) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: SetBalanceMode(int)."""
        ...
    def set_swing_height(self, swing_height: float) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: SetSwingHeight(float)."""
        ...
    def set_stand_height(self, stand_height: float) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: SetStandHeight(float)."""
        ...
    def set_velocity(self, vx: float, vy: float, omega: float, duration: float = 1.0) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: SetVelocity(float, float, float, float)."""
        ...
    def set_phase(self, phase: Sequence[float]) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: SetPhase(std::vector<float>)."""
        ...
    def set_target_pos(self, x: float, y: float, yaw: float, relative: bool = True) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: SetTargetPos(float, float, float, bool)."""
        ...
    def set_task_id(self, task_id: int) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: SetTaskId(int)."""
        ...
    def damp(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Damp()."""
        ...
    def start(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Start()."""
        ...
    def stand_up(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: StandUp()."""
        ...
    def zero_torque(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: ZeroTorque()."""
        ...
    def stop_move(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: StopMove()."""
        ...
    def high_stand(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: HighStand()."""
        ...
    def low_stand(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: LowStand()."""
        ...
    @overload
    def move(self, vx: float, vy: float, vyaw: float, continous_move: bool) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Move(float, float, float, bool)."""
        ...
    @overload
    def move(self, vx: float, vy: float, vyaw: float) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Move(float, float, float)."""
        ...
    def balance_stand(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: BalanceStand()."""
        ...
    def continuous_gait(self, flag: bool) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: ContinuousGait(bool)."""
        ...
    def switch_move_mode(self, flag: bool) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: SwitchMoveMode(bool)."""
        ...
    def set_next_foot(self, foot: bool) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: SetNextFoot(bool)."""
        ...
    def wave_hand(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: WaveHand()."""
        ...
    def shake_hand(self, stage: int = -1) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: ShakeHand(int)."""
        ...
