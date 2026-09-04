"""Full SDK signature preview; see api_manifest.json for availability."""
from __future__ import annotations

import enum
from collections.abc import Callable, Mapping, Sequence
from typing import Any, overload

from . import Client, ClientBase

class AudioClient(Client):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::r1::AudioClient::AudioClient()."""
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

class JsonizeDataVecFloat(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::r1::JsonizeDataVecFloat::JsonizeDataVecFloat()."""
        ...
    data: list[float]
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class JsonizeVelocityCommand(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::r1::JsonizeVelocityCommand::JsonizeVelocityCommand()."""
        ...
    velocity: list[float]
    duration: float
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class LedControlParameter(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::r1::LedControlParameter::LedControlParameter()."""
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

class LocoClient(Client):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::r1::LocoClient::LocoClient()."""
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
    def set_fsm_id(self, fsm_id: int) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: SetFsmId(int)."""
        ...
    def set_velocity(self, vx: float, vy: float, omega: float, duration: float = 1.0) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: SetVelocity(float, float, float, float)."""
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
    @overload
    def move(self, vx: float, vy: float, vyaw: float, continous_move: bool) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Move(float, float, float, bool)."""
        ...
    @overload
    def move(self, vx: float, vy: float, vyaw: float) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Move(float, float, float)."""
        ...
    def switch_move_mode(self, flag: bool) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: SwitchMoveMode(bool)."""
        ...
    def set_speed_mode(self, speed_mode: int) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: SetSpeedMode(int)."""
        ...

class PlayStopParameter(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::r1::PlayStopParameter::PlayStopParameter()."""
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
        """AVAILABLE; C++: unitree::robot::r1::PlayStreamParameter::PlayStreamParameter()."""
        ...
    app_name: str
    stream_id: str
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class TtsMakerParameter(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::r1::TtsMakerParameter::TtsMakerParameter()."""
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
