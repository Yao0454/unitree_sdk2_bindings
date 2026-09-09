"""Generated source companion. Full types and Chinese help are in the PEP 561 stubs.
Robot APIs are provided exclusively by the separately installed native extension.
"""
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    class BackVideoClient:
        pass

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

    class FrontVideoClient:
        pass

    class JsonizeConfigMeta:
        pass

    class JsonizeModeName:
        pass

    class JsonizeSilent:
        pass

    class LowPowerStatusData:
        pass

    class LowPowerSwitchParameter:
        pass

    class MotionSwitcherClient:
        pass

    class PkgVersionData:
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

    class stPathPoint:
        pass

    PathPoint = stPathPoint

if not TYPE_CHECKING:
    raise ImportError("This source companion has no runtime API; install unitree-sdk2-cpp.")
