"""Full SDK signature preview; see api_manifest.json for availability."""
from __future__ import annotations

import enum
from collections.abc import Callable, Mapping, Sequence
from typing import Any, overload

from . import Client, ClientBase

class AudioClient(Client):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::a2::AudioClient::AudioClient()."""
        ...
    def init(self) -> None:
        """AVAILABLE | INITIALIZATION | DIRECT. C++: Init()."""
        ...
    def tts_maker(self, text: str, speaker_id: int) -> int:
        """AVAILABLE | HARDWARE_SIDE_EFFECT | DIRECT. C++: TtsMaker(const std::string &, int32_t)."""
        ...
    def get_volume(self) -> tuple[int, int]:
        """AVAILABLE | READ_ONLY | OUTPUT_WRAPPER. C++: GetVolume(uint8_t &)."""
        ...
    def set_volume(self, volume: int) -> int:
        """AVAILABLE | HARDWARE_SIDE_EFFECT | DIRECT. C++: SetVolume(uint8_t)."""
        ...
    def play_stream(self, app_name: str, stream_id: str, pcm_data: Sequence[int]) -> int:
        """AVAILABLE | HARDWARE_SIDE_EFFECT | DIRECT. C++: PlayStream(std::string, std::string, std::vector<uint8_t>)."""
        ...
    def play_stop(self, app_name: str) -> int:
        """AVAILABLE | HARDWARE_SIDE_EFFECT | DIRECT. C++: PlayStop(std::string)."""
        ...
    def led_control(self, r: int, g: int, b: int) -> int:
        """AVAILABLE | HARDWARE_SIDE_EFFECT | DIRECT. C++: LedControl(uint8_t, uint8_t, uint8_t)."""
        ...

class LedControlParameter(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::a2::LedControlParameter::LedControlParameter()."""
        ...
    r: int
    g: int
    b: int
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class PathPoint(object):
    t_from_start: float
    x: float
    y: float
    yaw: float
    def __init__(self) -> None:
        """AVAILABLE; C++ aggregate: unitree::robot::a2::PathPoint."""
        ...

class PlayStopParameter(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::a2::PlayStopParameter::PlayStopParameter()."""
        ...
    app_name: str
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class PlayStreamParameter(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::a2::PlayStreamParameter::PlayStreamParameter()."""
        ...
    app_name: str
    stream_id: str
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class PoseVec4(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::a2::PoseVec4::PoseVec4()."""
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
        """AVAILABLE; C++: unitree::robot::a2::SportClient::SportClient()."""
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
    def reset_estimator(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: ResetEstimator()."""
        ...
    def trajectory(self, path: Sequence[PathPoint], feedback_mode: int = 0, external_x: float = 0.0, external_y: float = 0.0, external_yaw: float = 0.0) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Trajectory(const std::vector<PathPoint> &, int, float, float, float)."""
        ...
    def set_auto_recovery(self, switch_on: int) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: SetAutoRecovery(int)."""
        ...
    def get_state(self) -> tuple[int, dict[str, str]]:
        """AVAILABLE | READ_ONLY | OUTPUT_WRAPPER. C++: GetState(std::map<std::string, std::string> &)."""
        ...

class TtsMakerParameter(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::a2::TtsMakerParameter::TtsMakerParameter()."""
        ...
    index: int
    speaker_id: int
    text: str
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...
