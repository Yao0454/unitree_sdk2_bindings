"""Full SDK signature preview; see api_manifest.json for availability."""
from __future__ import annotations

import enum
from collections.abc import Callable, Mapping, Sequence
from typing import Any, overload

from . import Client, ClientBase

class ConfigClient(Client):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::go2::ConfigClient::ConfigClient()."""
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
        """AVAILABLE | HARDWARE_SIDE_EFFECT | OUTPUT_WRAPPER. C++: Meta(const std::string &, unitree::robot::go2::ConfigMeta &)."""
        ...
    def meta_string(self, name: str) -> tuple[int, str]:
        """AVAILABLE | HARDWARE_SIDE_EFFECT | OUTPUT_WRAPPER. C++: Meta(const std::string &, std::string &)."""
        ...
    def subscribe_change_status(self, name: str, callback: Callable[[str, str], None]) -> None:
        """AVAILABLE | HARDWARE_SIDE_EFFECT | CALLBACK_MANUAL. C++: SubscribeChangeStatus(const std::string &, const unitree::robot::go2::ConfigChangeStatusCallback &)."""
        ...

class ConfigDelParameter(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::go2::ConfigDelParameter::ConfigDelParameter()."""
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
        """AVAILABLE; C++: unitree::robot::go2::ConfigGetData::ConfigGetData()."""
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
        """AVAILABLE; C++: unitree::robot::go2::ConfigGetParameter::ConfigGetParameter()."""
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
        """AVAILABLE; C++: unitree::robot::go2::ConfigMeta::ConfigMeta()."""
        ...
    name: str
    last_modified: str
    size: int
    epoch: int

class ConfigMetaData(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::go2::ConfigMetaData::ConfigMetaData()."""
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
        """AVAILABLE; C++: unitree::robot::go2::ConfigMetaParameter::ConfigMetaParameter()."""
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
        """AVAILABLE; C++: unitree::robot::go2::ConfigSetParameter::ConfigSetParameter()."""
        ...
    name: str
    content: str
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class JsonizeCommObjInt(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::go2::JsonizeCommObjInt::JsonizeCommObjInt()."""
        ...
    value: int
    name: str
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class JsonizeConfigMeta(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::go2::JsonizeConfigMeta::JsonizeConfigMeta()."""
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

class JsonizeDataBool(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::go2::JsonizeDataBool::JsonizeDataBool()."""
        ...
    data: bool
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class JsonizeDataDouble(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::go2::JsonizeDataDouble::JsonizeDataDouble()."""
        ...
    data: float
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class JsonizeDataFloat(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::go2::JsonizeDataFloat::JsonizeDataFloat()."""
        ...
    data: float
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class JsonizeDataInt(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::go2::JsonizeDataInt::JsonizeDataInt()."""
        ...
    data: int
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class JsonizeDataString(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::go2::JsonizeDataString::JsonizeDataString()."""
        ...
    data: str
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class JsonizeFlagBool(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::go2::JsonizeFlagBool::JsonizeFlagBool()."""
        ...
    flag: bool
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class JsonizePathPoint(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::go2::JsonizePathPoint::JsonizePathPoint()."""
        ...
    time_from_start: float
    x: float
    y: float
    yaw: float
    vx: float
    vy: float
    vyaw: float
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class JsonizeQuat(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::go2::JsonizeQuat::JsonizeQuat()."""
        ...
    x: float
    y: float
    z: float
    w: float
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class JsonizeVec3(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::go2::JsonizeVec3::JsonizeVec3()."""
        ...
    x: float
    y: float
    z: float
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class ObstaclesAvoidClient(Client):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::go2::ObstaclesAvoidClient::ObstaclesAvoidClient()."""
        ...
    def init(self) -> None:
        """AVAILABLE | INITIALIZATION | DIRECT. C++: Init()."""
        ...
    def switch_set(self, enable: bool) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: SwitchSet(bool)."""
        ...
    def switch_get(self) -> tuple[int, bool]:
        """AVAILABLE | MOTION_COMMAND | OUTPUT_WRAPPER. C++: SwitchGet(bool &)."""
        ...
    def move(self, x: float, y: float, yaw: float) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Move(float, float, float)."""
        ...
    def use_remote_command_from_api(self, is_remote_commands_from_api: bool) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: UseRemoteCommandFromApi(bool)."""
        ...
    def move_to_absolute_position(self, x: float, y: float, yaw: float) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: MoveToAbsolutePosition(float, float, float)."""
        ...
    def move_to_increment_position(self, x: float, y: float, yaw: float) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: MoveToIncrementPosition(float, float, float)."""
        ...

class ObstaclesAvoidMoveParameter(object):
    m_x: float
    m_y: float
    m_yaw: float
    m_mode: int
    def __init__(self) -> None:
        """AVAILABLE; C++ aggregate: unitree::robot::go2::ObstaclesAvoidMoveParameter."""
        ...
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class ObstaclesAvoidRemoteCommandSource(object):
    m_is_remote_commands_from_api: bool
    def __init__(self) -> None:
        """AVAILABLE; C++ aggregate: unitree::robot::go2::ObstaclesAvoidRemoteCommandSource."""
        ...
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class ObstaclesAvoidSwitchGetData(object):
    m_enable: bool
    def __init__(self) -> None:
        """AVAILABLE; C++ aggregate: unitree::robot::go2::ObstaclesAvoidSwitchGetData."""
        ...
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class ObstaclesAvoidSwitchSetParameter(object):
    m_enable: bool
    def __init__(self) -> None:
        """AVAILABLE; C++ aggregate: unitree::robot::go2::ObstaclesAvoidSwitchSetParameter."""
        ...
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class RobotStateClient(Client):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::go2::RobotStateClient::RobotStateClient()."""
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

class ServiceState(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::go2::ServiceState::ServiceState()."""
        ...
    name: str
    status: int
    protect: int

class ServiceStateData(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::go2::ServiceStateData::ServiceStateData()."""
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
        """AVAILABLE; C++: unitree::robot::go2::ServiceSwitchData::ServiceSwitchData()."""
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
        """AVAILABLE; C++: unitree::robot::go2::ServiceSwitchParameter::ServiceSwitchParameter()."""
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
        """AVAILABLE; C++: unitree::robot::go2::SetReportFreqParameter::SetReportFreqParameter()."""
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
        """AVAILABLE; C++: unitree::robot::go2::SportClient::SportClient(bool)."""
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
    def sit(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Sit()."""
        ...
    def rise_sit(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: RiseSit()."""
        ...
    def speed_level(self, level: int) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: SpeedLevel(int)."""
        ...
    def hello(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Hello()."""
        ...
    def stretch(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Stretch()."""
        ...
    def switch_joystick(self, flag: bool) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: SwitchJoystick(bool)."""
        ...
    def content(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Content()."""
        ...
    def heart(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Heart()."""
        ...
    def pose(self, flag: bool) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Pose(bool)."""
        ...
    def scrape(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Scrape()."""
        ...
    def front_flip(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: FrontFlip()."""
        ...
    def front_jump(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: FrontJump()."""
        ...
    def front_pounce(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: FrontPounce()."""
        ...
    def dance1(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Dance1()."""
        ...
    def dance2(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: Dance2()."""
        ...
    def left_flip(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: LeftFlip()."""
        ...
    def back_flip(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: BackFlip()."""
        ...
    def hand_stand(self, flag: bool) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: HandStand(bool)."""
        ...
    def free_walk(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: FreeWalk()."""
        ...
    def free_bound(self, flag: bool) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: FreeBound(bool)."""
        ...
    def free_jump(self, flag: bool) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: FreeJump(bool)."""
        ...
    def free_avoid(self, flag: bool) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: FreeAvoid(bool)."""
        ...
    def classic_walk(self, flag: bool) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: ClassicWalk(bool)."""
        ...
    def walk_upright(self, flag: bool) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: WalkUpright(bool)."""
        ...
    def cross_step(self, flag: bool) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: CrossStep(bool)."""
        ...
    def auto_recover_set(self, flag: bool) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: AutoRecoverSet(bool)."""
        ...
    def auto_recover_get(self) -> tuple[int, bool]:
        """AVAILABLE | MOTION_COMMAND | OUTPUT_WRAPPER. C++: AutoRecoverGet(bool &)."""
        ...
    def static_walk(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: StaticWalk()."""
        ...
    def trot_run(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: TrotRun()."""
        ...
    def economic_gait(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: EconomicGait()."""
        ...
    def switch_avoid_mode(self) -> int:
        """AVAILABLE | MOTION_COMMAND | DIRECT. C++: SwitchAvoidMode()."""
        ...

class UtrackClient(Client):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::go2::UtrackClient::UtrackClient()."""
        ...
    def init(self) -> None:
        """AVAILABLE | INITIALIZATION | DIRECT. C++: Init()."""
        ...
    def switch_set(self, enable: bool) -> int:
        """AVAILABLE | HARDWARE_SIDE_EFFECT | DIRECT. C++: SwitchSet(bool)."""
        ...
    def switch_get(self) -> tuple[int, bool]:
        """AVAILABLE | HARDWARE_SIDE_EFFECT | OUTPUT_WRAPPER. C++: SwitchGet(bool &)."""
        ...
    def is_tracking(self) -> tuple[int, bool]:
        """AVAILABLE | READ_ONLY | OUTPUT_WRAPPER. C++: IsTracking(bool &)."""
        ...

class UtrackSwitchGetData(object):
    m_enable: int
    def __init__(self) -> None:
        """AVAILABLE; C++ aggregate: unitree::robot::go2::UtrackSwitchGetData."""
        ...
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class UtrackSwitchSetParameter(object):
    m_enable: int
    def __init__(self) -> None:
        """AVAILABLE; C++ aggregate: unitree::robot::go2::UtrackSwitchSetParameter."""
        ...
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class VideoClient(Client):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::go2::VideoClient::VideoClient()."""
        ...
    def init(self) -> None:
        """AVAILABLE | INITIALIZATION | DIRECT. C++: Init()."""
        ...
    def get_image_sample(self) -> tuple[int, list[int]]:
        """AVAILABLE | READ_ONLY | OUTPUT_WRAPPER. C++: GetImageSample(std::vector<uint8_t> &)."""
        ...

class VuiClient(Client):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::go2::VuiClient::VuiClient()."""
        ...
    def init(self) -> None:
        """AVAILABLE | INITIALIZATION | DIRECT. C++: Init()."""
        ...
    def set_switch(self, enable: int) -> int:
        """AVAILABLE | HARDWARE_SIDE_EFFECT | DIRECT. C++: SetSwitch(int)."""
        ...
    def get_switch(self) -> tuple[int, int]:
        """AVAILABLE | READ_ONLY | OUTPUT_WRAPPER. C++: GetSwitch(int &)."""
        ...
    def set_volume(self, level: int) -> int:
        """AVAILABLE | HARDWARE_SIDE_EFFECT | DIRECT. C++: SetVolume(int)."""
        ...
    def get_volume(self) -> tuple[int, int]:
        """AVAILABLE | READ_ONLY | OUTPUT_WRAPPER. C++: GetVolume(int &)."""
        ...
    def set_brightness(self, level: int) -> int:
        """AVAILABLE | HARDWARE_SIDE_EFFECT | DIRECT. C++: SetBrightness(int)."""
        ...
    def get_brightness(self) -> tuple[int, int]:
        """AVAILABLE | READ_ONLY | OUTPUT_WRAPPER. C++: GetBrightness(int &)."""
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
        """AVAILABLE; C++ aggregate: unitree::robot::go2::stPathPoint."""
        ...

PathPoint = stPathPoint
