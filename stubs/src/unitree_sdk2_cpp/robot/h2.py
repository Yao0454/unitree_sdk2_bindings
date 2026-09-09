"""Generated source companion. Full types and Chinese help are in the PEP 561 stubs.
Robot APIs are provided exclusively by the separately installed native extension.
"""
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    class FsmIdInfo:
        pass

    class H2ArmActionClient:
        pass

    class JsonizeArmActionCommand:
        pass

    class JsonizeArmActionName:
        pass

    class JsonizeDataVecFloat:
        pass

    class JsonizeFsmIdList:
        pass

    class JsonizeVelocityCommand:
        pass

    class LocoClient:
        pass

if not TYPE_CHECKING:
    raise ImportError("This source companion has no runtime API; install unitree-sdk2-cpp.")
