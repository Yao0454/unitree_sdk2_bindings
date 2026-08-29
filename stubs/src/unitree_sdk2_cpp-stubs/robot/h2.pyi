"""Full SDK signature preview; see api_manifest.json for availability."""
from __future__ import annotations

import enum
from collections.abc import Callable, Mapping, Sequence
from typing import Any, overload

from . import Client, ClientBase

class FsmIdInfo(object):
    @overload
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::h2::FsmIdInfo::FsmIdInfo()."""
        ...
    @overload
    def __init__(self, i: int, n: str) -> None:
        """AVAILABLE; C++: unitree::robot::h2::FsmIdInfo::FsmIdInfo(int, const std::string &)."""
        ...
    id: int
    name: str

class H2ArmActionClient(Client):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::h2::H2ArmActionClient::H2ArmActionClient()."""
        ...
    def init(self) -> None:
        """AVAILABLE | INITIALIZATION | DIRECT. C++: Init()."""
        ...
    @overload
    def execute_action(self, action_id: int) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: ExecuteAction(int32_t)."""
        ...
    @overload
    def execute_action(self, action_name: str) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: ExecuteAction(const std::string &)."""
        ...
    def stop_custom_action(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: StopCustomAction()."""
        ...
    def get_action_list(self) -> tuple[int, str]:
        """AVAILABLE | READ_ONLY | OUTPUT_WRAPPER. C++: GetActionList(std::string &)."""
        ...

class JsonizeArmActionCommand(object):
    action_id: int
    def __init__(self) -> None:
        """AVAILABLE; C++ aggregate: unitree::robot::h2::JsonizeArmActionCommand."""
        ...
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class JsonizeArmActionName(object):
    action_name: str
    def __init__(self) -> None:
        """AVAILABLE; C++ aggregate: unitree::robot::h2::JsonizeArmActionName."""
        ...
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class JsonizeDataVecFloat(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::h2::JsonizeDataVecFloat::JsonizeDataVecFloat()."""
        ...
    data: list[float]
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class JsonizeFsmIdList(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::h2::JsonizeFsmIdList::JsonizeFsmIdList()."""
        ...
    fsm_ids: list[FsmIdInfo]
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class JsonizeVelocityCommand(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::h2::JsonizeVelocityCommand::JsonizeVelocityCommand()."""
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
        """AVAILABLE; C++: unitree::robot::h2::LocoClient::LocoClient()."""
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
    def get_arm_sdk_status(self) -> tuple[int, bool]:
        """AVAILABLE | READ_ONLY | OUTPUT_WRAPPER. C++: GetArmSdkStatus(bool &)."""
        ...
    def get_available_fsm_ids(self) -> tuple[int, list[int], list[str]]:
        """AVAILABLE | READ_ONLY | OUTPUT_WRAPPER. C++: GetAvailableFsmIds(std::vector<int> &, std::vector<std::string> &)."""
        ...
    def set_fsm_id(self, fsm_id: int) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: SetFsmId(int)."""
        ...
    def set_balance_mode(self, balance_mode: int) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: SetBalanceMode(int)."""
        ...
    def set_punch_api(self, punch_api: Sequence[float]) -> int:
        """AVAILABLE | MOTION_COMMAND | MUTABLE_INPUT_COPY. C++: SetPunchApi(std::vector<float> &)."""
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
    def set_task_id(self, task_id: int) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: SetTaskId(int)."""
        ...
    def set_arm_sdk_status(self, arm_sdk_status: bool) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: SetArmSdkStatus(bool)."""
        ...
    def damp(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Damp()."""
        ...
    def start(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Start()."""
        ...
    def squat(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Squat()."""
        ...
    def sit(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Sit()."""
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
    def wave_hand(self, turn_flag: bool = False) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: WaveHand(bool)."""
        ...
    def shake_hand(self, stage: int = -1) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: ShakeHand(int)."""
        ...
    def set_speed_mode(self, speed_mode: int) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: SetSpeedMode(int)."""
        ...
    def enable_arm_sdk(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: EnableArmSDK()."""
        ...
    def disable_arm_sdk(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: DisableArmSDK()."""
        ...
