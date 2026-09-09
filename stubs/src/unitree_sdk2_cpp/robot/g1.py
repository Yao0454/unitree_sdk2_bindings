"""Generated source companion. Full types and Chinese help are in the PEP 561 stubs.
Robot APIs are provided exclusively by the separately installed native extension.
"""
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    class InternalFsmMode:
        pass

    class AgvClient:
        pass

    class AudioClient:
        pass

    class G1ArmActionClient:
        pass

    class JsonizeDataVecFloat:
        pass

    class JsonizeVelocityCommand:
        pass

    class LedControlParameter:
        pass

    class LocoClient:
        pass

    class MoveParameter:
        pass

    class PlayStopParameter:
        pass

    class PlayStreamParameter:
        pass

    class TtsMakerParameter:
        pass

    def bad_orientation(*args: Any, **kwargs: Any) -> Any: ...

    def joint_vel_out_of_limit(*args: Any, **kwargs: Any) -> Any: ...

    def ang_vel_out_of_limit(*args: Any, **kwargs: Any) -> Any: ...

    def motor_winding_overheat(*args: Any, **kwargs: Any) -> Any: ...

    def motor_casing_overheat(*args: Any, **kwargs: Any) -> Any: ...

    def low_battery(*args: Any, **kwargs: Any) -> Any: ...

    def lost_connection(*args: Any, **kwargs: Any) -> Any: ...

if not TYPE_CHECKING:
    raise ImportError("This source companion has no runtime API; install unitree-sdk2-cpp.")
