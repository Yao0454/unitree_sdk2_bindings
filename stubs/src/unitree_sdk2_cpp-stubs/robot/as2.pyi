"""Full SDK signature preview; see api_manifest.json for availability."""
from __future__ import annotations

import enum
from collections.abc import Callable, Mapping, Sequence
from typing import Any, overload

from . import Client, ClientBase

class PoseVec4(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::as2::PoseVec4::PoseVec4()."""
        ...
    x: float
    y: float
    z: float
    yaw: float
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class SportClient(Client):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::as2::SportClient::SportClient()."""
        ...
    def init(self) -> None:
        """AVAILABLE | INITIALIZATION | DIRECT. C++: Init()."""
        ...
    def damp(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Damp()."""
        ...
    def balance_stand(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: BalanceStand()."""
        ...
    def stop_move(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: StopMove()."""
        ...
    def stand_up(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: StandUp()."""
        ...
    def stand_down(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: StandDown()."""
        ...
    def recovery_stand(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: RecoveryStand()."""
        ...
    def euler(self, roll: float, pitch: float, yaw: float) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Euler(float, float, float)."""
        ...
    def move(self, vx: float, vy: float, vyaw: float) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Move(float, float, float)."""
        ...
    def switch_gait(self, gait_type: int) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: SwitchGait(int)."""
        ...
    def body_height(self, height: float) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: BodyHeight(float)."""
        ...
    def speed_level(self, level: int) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: SpeedLevel(int)."""
        ...
    def body_position(self, x: float, y: float, z: float, yaw: float) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: BodyPosition(float, float, float, float)."""
        ...
    def left_side_gait(self, enter: int) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: LeftSideGait(int)."""
        ...
    def right_side_gait(self, enter: int) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: RightSideGait(int)."""
        ...
    def hand_stand(self, enter: int) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: HandStand(int)."""
        ...
    def biped_stand(self, enter: int) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: BipedStand(int)."""
        ...
    def front_flip(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: FrontFlip()."""
        ...
    def back_flip(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: BackFlip()."""
        ...
    def greeting(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Greeting()."""
        ...
    def heart(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Heart()."""
        ...
    def content(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Content()."""
        ...
    def dance1(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Dance1()."""
        ...
    def dance2(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Dance2()."""
        ...
    def handshake(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Handshake()."""
        ...
    def stretch(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Stretch()."""
        ...
    def sit(self, enter: int) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Sit(int)."""
        ...
    def front_jump(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: FrontJump()."""
        ...
    def push_up(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: PushUp()."""
        ...
    def up_jump(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: UpJump()."""
        ...
    def set_auto_recovery(self, switch_on: int) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: SetAutoRecovery(int)."""
        ...
    def switch_joystick(self, switch_on: int) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: SwitchJoystick(int)."""
        ...
    def get_state(self) -> tuple[int, dict[str, str]]:
        """AVAILABLE | READ_ONLY | OUTPUT_WRAPPER. C++: GetState(std::map<std::string, std::string> &)."""
        ...
