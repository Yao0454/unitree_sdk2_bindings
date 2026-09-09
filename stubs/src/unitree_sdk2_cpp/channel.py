"""Generated source companion. Full types and Chinese help are in the PEP 561 stubs.
Robot APIs are provided exclusively by the separately installed native extension.
"""
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    def registered_message_types(*args: Any, **kwargs: Any) -> Any: ...

    def initialize(*args: Any, **kwargs: Any) -> Any: ...

    def initialize_from_config(*args: Any, **kwargs: Any) -> Any: ...

    def release(*args: Any, **kwargs: Any) -> Any: ...

    class ChannelPublisher:
        pass

    class ChannelSubscriber:
        pass

if not TYPE_CHECKING:
    raise ImportError("This source companion has no runtime API; install unitree-sdk2-cpp.")
