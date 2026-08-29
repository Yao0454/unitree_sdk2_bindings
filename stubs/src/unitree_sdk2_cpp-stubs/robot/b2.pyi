"""Full SDK signature preview; see api_manifest.json for availability."""
from __future__ import annotations

import enum
from collections.abc import Callable, Mapping, Sequence
from typing import Any, overload

from . import Client, ClientBase

class BackVideoClient(Client):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::b2::BackVideoClient::BackVideoClient()."""
        ...
    def init(self) -> None:
        """AVAILABLE | INITIALIZATION | DIRECT. C++: Init()."""
        ...
    def get_image_sample(self) -> tuple[int, list[int]]:
        """AVAILABLE | READ_ONLY | OUTPUT_WRAPPER. C++: GetImageSample(std::vector<uint8_t> &)."""
        ...

class ConfigClient(Client):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::b2::ConfigClient::ConfigClient()."""
        ...
    def init(self) -> None:
        """AVAILABLE | INITIALIZATION | DIRECT. C++: Init()."""
        ...
    def set(self, name: str, content: str) -> int:
        """AVAILABLE | HARDWARE_SIDE_EFFECT | DIRECT. C++: Set(const std::string &, const std::string &)."""
        ...
    def get(self, name: str) -> tuple[int, str]:
        """AVAILABLE | READ_ONLY | OUTPUT_WRAPPER. C++: Get(const std::string &, std::string &)."""
        ...
    def del_(self, name: str) -> int:
        """AVAILABLE | HARDWARE_SIDE_EFFECT | DIRECT. C++: Del(const std::string &)."""
        ...
    def meta_config_meta(self, name: str) -> tuple[int, ConfigMeta]:
        """AVAILABLE | HARDWARE_SIDE_EFFECT | OUTPUT_WRAPPER. C++: Meta(const std::string &, unitree::robot::b2::ConfigMeta &)."""
        ...
    def meta_string(self, name: str) -> tuple[int, str]:
        """AVAILABLE | HARDWARE_SIDE_EFFECT | OUTPUT_WRAPPER. C++: Meta(const std::string &, std::string &)."""
        ...
    def subscribe_change_status(self, name: str, callback: Callable[[str, str], None]) -> None:
        """AVAILABLE | HARDWARE_SIDE_EFFECT | CALLBACK_MANUAL. C++: SubscribeChangeStatus(const std::string &, const unitree::robot::b2::ConfigChangeStatusCallback &)."""
        ...

class ConfigDelParameter(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::b2::ConfigDelParameter::ConfigDelParameter()."""
        ...
    name: str
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class ConfigGetData(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::b2::ConfigGetData::ConfigGetData()."""
        ...
    content: str
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class ConfigGetParameter(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::b2::ConfigGetParameter::ConfigGetParameter()."""
        ...
    name: str
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class ConfigMeta(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::b2::ConfigMeta::ConfigMeta()."""
        ...
    name: str
    last_modified: str
    size: int
    epoch: int

class ConfigMetaData(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::b2::ConfigMetaData::ConfigMetaData()."""
        ...
    meta: JsonizeConfigMeta
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class ConfigMetaParameter(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::b2::ConfigMetaParameter::ConfigMetaParameter()."""
        ...
    name: str
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class ConfigSetParameter(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::b2::ConfigSetParameter::ConfigSetParameter()."""
        ...
    name: str
    content: str
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class FrontVideoClient(Client):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::b2::FrontVideoClient::FrontVideoClient()."""
        ...
    def init(self) -> None:
        """AVAILABLE | INITIALIZATION | DIRECT. C++: Init()."""
        ...
    def get_image_sample(self) -> tuple[int, list[int]]:
        """AVAILABLE | READ_ONLY | OUTPUT_WRAPPER. C++: GetImageSample(std::vector<uint8_t> &)."""
        ...

class JsonizeConfigMeta(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::b2::JsonizeConfigMeta::JsonizeConfigMeta()."""
        ...
    name: str
    last_modified: str
    size: int
    epoch: int
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class JsonizeModeName(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::b2::JsonizeModeName::JsonizeModeName()."""
        ...
    name: str
    form: str
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class JsonizeSilent(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::b2::JsonizeSilent::JsonizeSilent()."""
        ...
    silent: bool
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class LowPowerStatusData(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::b2::LowPowerStatusData::LowPowerStatusData()."""
        ...
    status: int
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class LowPowerSwitchParameter(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::b2::LowPowerSwitchParameter::LowPowerSwitchParameter()."""
        ...
    swit: int
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class MotionSwitcherClient(Client):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::b2::MotionSwitcherClient::MotionSwitcherClient()."""
        ...
    def init(self) -> None:
        """AVAILABLE | INITIALIZATION | DIRECT. C++: Init()."""
        ...
    def check_mode(self) -> tuple[int, str, str]:
        """AVAILABLE | READ_ONLY | OUTPUT_WRAPPER. C++: CheckMode(std::string &, std::string &)."""
        ...
    def select_mode(self, name_or_alias: str) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: SelectMode(const std::string &)."""
        ...
    def release_mode(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: ReleaseMode()."""
        ...
    def set_silent(self, silent: bool) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: SetSilent(bool)."""
        ...
    def get_silent(self) -> tuple[int, bool]:
        """AVAILABLE | READ_ONLY | OUTPUT_WRAPPER. C++: GetSilent(bool &)."""
        ...

class PkgVersionData(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::b2::PkgVersionData::PkgVersionData()."""
        ...
    package_version: str
    module_version_map: dict[str, str]
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class RobotStateClient(Client):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::b2::RobotStateClient::RobotStateClient()."""
        ...
    def init(self) -> None:
        """AVAILABLE | INITIALIZATION | DIRECT. C++: Init()."""
        ...
    def service_list(self) -> tuple[int, list[ServiceState]]:
        """AVAILABLE | READ_ONLY | OUTPUT_WRAPPER. C++: ServiceList(std::vector<ServiceState> &)."""
        ...
    def service_switch(self, name: str, swit: int) -> tuple[int, int]:
        """AVAILABLE | HARDWARE_SIDE_EFFECT | OUTPUT_WRAPPER. C++: ServiceSwitch(const std::string &, int32_t, int32_t &)."""
        ...
    def set_report_freq(self, interval: int, duration: int) -> int:
        """AVAILABLE | HARDWARE_SIDE_EFFECT | DIRECT. C++: SetReportFreq(int32_t, int32_t)."""
        ...
    def low_power_switch(self, swit: int) -> int:
        """AVAILABLE | HARDWARE_SIDE_EFFECT | DIRECT. C++: LowPowerSwitch(int32_t)."""
        ...
    def low_power_status(self) -> tuple[int, int]:
        """AVAILABLE | HARDWARE_SIDE_EFFECT | OUTPUT_WRAPPER. C++: LowPowerStatus(int32_t &)."""
        ...
    def get_pkg_version(self) -> tuple[int, str, dict[str, str]]:
        """AVAILABLE | READ_ONLY | OUTPUT_WRAPPER. C++: GetPkgVersion(std::string &, std::map<std::string, std::string> &)."""
        ...

class ServiceState(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::b2::ServiceState::ServiceState()."""
        ...
    name: str
    status: int
    protect: int

class ServiceStateData(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::b2::ServiceStateData::ServiceStateData()."""
        ...
    name: str
    status: int
    protect: int
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class ServiceSwitchData(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::b2::ServiceSwitchData::ServiceSwitchData()."""
        ...
    name: str
    status: int
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class ServiceSwitchParameter(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::b2::ServiceSwitchParameter::ServiceSwitchParameter()."""
        ...
    name: str
    swit: int
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class SetReportFreqParameter(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::b2::SetReportFreqParameter::SetReportFreqParameter()."""
        ...
    interval: int
    duration: int
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class SportClient(Client):
    def __init__(self, enable_lease: bool = False) -> None:
        """AVAILABLE; C++: unitree::robot::b2::SportClient::SportClient(bool)."""
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
    def move(self, vx: float, vy: float, vyaw: float) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Move(float, float, float)."""
        ...
    def switch_gait(self, d: int) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: SwitchGait(int)."""
        ...
    def body_height(self, height: float) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: BodyHeight(float)."""
        ...
    def speed_level(self, level: int) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: SpeedLevel(int)."""
        ...
    def trajectory_follow(self, path: Sequence[PathPoint]) -> int:
        """AVAILABLE | MOTION_COMMAND | MUTABLE_INPUT_COPY. C++: TrajectoryFollow(std::vector<unitree::robot::b2::PathPoint> &)."""
        ...
    def continuous_gait(self, flag: bool) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: ContinuousGait(bool)."""
        ...
    def move_to_pos(self, x: float, y: float, yaw: float) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: MoveToPos(float, float, float)."""
        ...
    def switch_move_mode(self, flag: bool) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: SwitchMoveMode(bool)."""
        ...
    def vision_walk(self, flag: bool) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: VisionWalk(bool)."""
        ...
    def hand_stand(self, flag: bool) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: HandStand(bool)."""
        ...
    def auto_recovery_set(self, flag: bool) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: AutoRecoverySet(bool)."""
        ...
    def free_walk(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: FreeWalk()."""
        ...
    def classic_walk(self, flag: bool) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: ClassicWalk(bool)."""
        ...
    def fast_walk(self, flag: bool) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: FastWalk(bool)."""
        ...
    def euler(self, roll: float, pitch: float, yaw: float) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Euler(float, float, float)."""
        ...
    def free_height(self, flag: bool) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: FreeHeight(bool)."""
        ...
    def gait_height(self, flag: bool) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: GaitHeight(bool)."""
        ...

class stPathPoint(object):
    time_from_start: float
    x: float
    y: float
    yaw: float
    vx: float
    vy: float
    vyaw: float
    def __init__(self) -> None:
        """AVAILABLE; C++ aggregate: unitree::robot::b2::stPathPoint."""
        ...

PathPoint = stPathPoint
