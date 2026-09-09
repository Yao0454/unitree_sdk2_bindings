"""Generated source companion. Full types and Chinese help are in the PEP 561 stubs.
Robot APIs are provided exclusively by the separately installed native extension.
"""
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    class ConfigClient:
        pass

    class ConfigDelParameter:
        pass

    class ConfigGetData:
        pass

    class ConfigGetParameter:
        pass

    class ConfigMeta:
        pass

    class ConfigMetaData:
        pass

    class ConfigMetaParameter:
        pass

    class ConfigSetParameter:
        pass

    class JsonizeCommObjInt:
        pass

    class JsonizeConfigMeta:
        pass

    class JsonizeDataBool:
        pass

    class JsonizeDataDouble:
        pass

    class JsonizeDataFloat:
        pass

    class JsonizeDataInt:
        pass

    class JsonizeDataString:
        pass

    class JsonizeFlagBool:
        pass

    class JsonizePathPoint:
        pass

    class JsonizeQuat:
        pass

    class JsonizeVec3:
        pass

    class ObstaclesAvoidClient:
        pass

    class ObstaclesAvoidMoveParameter:
        pass

    class ObstaclesAvoidRemoteCommandSource:
        pass

    class ObstaclesAvoidSwitchGetData:
        pass

    class ObstaclesAvoidSwitchSetParameter:
        pass

    class RobotStateClient:
        pass

    class ServiceState:
        pass

    class ServiceStateData:
        pass

    class ServiceSwitchData:
        pass

    class ServiceSwitchParameter:
        pass

    class SetReportFreqParameter:
        pass

    class SportClient:
        pass

    class UtrackClient:
        pass

    class UtrackSwitchGetData:
        pass

    class UtrackSwitchSetParameter:
        pass

    class VideoClient:
        pass

    class VuiClient:
        pass

    class stPathPoint:
        pass

    PathPoint = stPathPoint

if not TYPE_CHECKING:
    raise ImportError("This source companion has no runtime API; install unitree-sdk2-cpp.")
