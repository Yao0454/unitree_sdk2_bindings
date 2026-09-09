"""Generated source companion. Full types and Chinese help are in the PEP 561 stubs.
Robot APIs are provided exclusively by the separately installed native extension.
"""
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    class ApplyLeaseData:
        pass

    class ApplyLeaseParameter:
        pass

    class ChannelFactory:
        pass

    class ChannelNamer:
        pass

    class Client:
        pass

    class ClientBase:
        pass

    class ClientChannelNamer:
        pass

    class ClientStub:
        pass

    class LeaseCache:
        pass

    class LeaseClient:
        pass

    class LeaseContext:
        pass

    class LeaseServer:
        pass

    class RequestFuture:
        pass

    class RequestFutureQueue:
        pass

    class Server:
        pass

    class ServerBase:
        pass

    class ServerChannelNamer:
        pass

    class ServerStub:
        pass

    from . import a2 as a2

    from . import as2 as as2

    from . import b2 as b2

    from . import g1 as g1

    from . import go2 as go2

    from . import h1 as h1

    from . import h2 as h2

    from . import r1 as r1

if not TYPE_CHECKING:
    raise ImportError("This source companion has no runtime API; install unitree-sdk2-cpp.")
