"""Full SDK signature preview; see api_manifest.json for availability."""
from __future__ import annotations

import enum
from collections.abc import Callable, Mapping, Sequence
from typing import Any, overload

class ApplyLeaseData(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::ApplyLeaseData::ApplyLeaseData()."""
        ...
    id: int
    term: int
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class ApplyLeaseParameter(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::ApplyLeaseParameter::ApplyLeaseParameter()."""
        ...
    name: str
    def from_json(self, value: Mapping[str, Any]) -> None:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_INPUT. C++: fromJson(common::JsonMap &)."""
        ...
    def to_json(self) -> dict[str, Any]:
        """AVAILABLE | UNCLASSIFIED | JSON_DICT_OUTPUT. C++: toJson(common::JsonMap &) const."""
        ...

class ChannelFactory(object):
    def instance(self) -> ChannelFactory:
        """SIGNATURE_ONLY | UNCLASSIFIED | SIGNATURE_PREVIEW. C++: Instance()."""
        ...
    @overload
    def init(self, domain_id: int, network_interface: str = ...) -> None:
        """SIGNATURE_ONLY | UNCLASSIFIED | SIGNATURE_PREVIEW. C++: Init(int32_t, const std::string &)."""
        ...
    @overload
    def init(self, config_file_name: str = ...) -> None:
        """SIGNATURE_ONLY | UNCLASSIFIED | SIGNATURE_PREVIEW. C++: Init(const std::string &)."""
        ...
    @overload
    def init(self, json_map: dict[str, Any]) -> None:
        """SIGNATURE_ONLY | UNCLASSIFIED | SIGNATURE_PREVIEW. C++: Init(const common::JsonMap &)."""
        ...
    def release(self) -> None:
        """SIGNATURE_ONLY | UNCLASSIFIED | SIGNATURE_PREVIEW. C++: Release()."""
        ...

class ChannelNamer(object):
    def get_send_channel_name(self, name: str) -> str:
        """SIGNATURE_ONLY | UNCLASSIFIED | SIGNATURE_PREVIEW. C++: GetSendChannelName(const std::string &)."""
        ...
    def get_recv_channel_name(self, name: str) -> str:
        """SIGNATURE_ONLY | UNCLASSIFIED | SIGNATURE_PREVIEW. C++: GetRecvChannelName(const std::string &)."""
        ...

class Client(ClientBase):
    def __init__(self, name: str, enable_lease: bool = False) -> None:
        """SIGNATURE_ONLY; C++: unitree::robot::Client::Client(const std::string &, bool)."""
        ...
    def wait_lease_applied(self) -> None:
        """AVAILABLE | INITIALIZATION | DIRECT. C++: WaitLeaseApplied()."""
        ...
    def get_lease_id(self) -> int:
        """SIGNATURE_ONLY | READ_ONLY | DIRECT. C++: GetLeaseId()."""
        ...
    def get_api_version(self) -> str:
        """AVAILABLE | READ_ONLY | REFERENCE_POLICY. C++: GetApiVersion() const."""
        ...
    def get_server_api_version(self) -> str:
        """AVAILABLE | READ_ONLY | DIRECT. C++: GetServerApiVersion()."""
        ...

class ClientBase(object):
    def __init__(self, name: str) -> None:
        """SIGNATURE_ONLY; C++: unitree::robot::ClientBase::ClientBase(const std::string &)."""
        ...
    def init(self) -> None:
        """SIGNATURE_ONLY | INITIALIZATION | DIRECT. C++: Init()."""
        ...
    def set_timeout_microseconds(self, microseconds: int) -> None:
        """AVAILABLE | INITIALIZATION | DIRECT. C++: SetTimeout(int64_t)."""
        ...
    def set_timeout(self, seconds: float) -> None:
        """AVAILABLE | INITIALIZATION | DIRECT. C++: SetTimeout(float)."""
        ...

class ClientChannelNamer(ChannelNamer):
    def __init__(self) -> None:
        """SIGNATURE_ONLY; C++: unitree::robot::ClientChannelNamer::ClientChannelNamer()."""
        ...

class ClientStub(object):
    def __init__(self) -> None:
        """SIGNATURE_ONLY; C++: unitree::robot::ClientStub::ClientStub()."""
        ...
    def init(self, name: str) -> None:
        """SIGNATURE_ONLY | INITIALIZATION | DIRECT. C++: Init(const std::string &)."""
        ...
    def send(self, req: Any, wait_timeout: int) -> bool:
        """SIGNATURE_ONLY | HARDWARE_SIDE_EFFECT | DIRECT. C++: Send(const unitree::robot::Request &, int64_t)."""
        ...
    def send_request(self, req: Any, wait_timeout: int) -> RequestFuture:
        """SIGNATURE_ONLY | HARDWARE_SIDE_EFFECT | DIRECT. C++: SendRequest(const unitree::robot::Request &, int64_t)."""
        ...

class LeaseCache(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::LeaseCache::LeaseCache()."""
        ...
    def set(self, id: int, m_name: str, last_modified: int = 0) -> None:
        """AVAILABLE | UNCLASSIFIED | DIRECT. C++: Set(int64_t, const std::string &, int64_t)."""
        ...
    def renewal(self, last_modified: int = 0) -> None:
        """AVAILABLE | UNCLASSIFIED | DIRECT. C++: Renewal(int64_t)."""
        ...
    def clear(self) -> None:
        """AVAILABLE | UNCLASSIFIED | DIRECT. C++: Clear()."""
        ...
    def get_last_modified(self) -> int:
        """AVAILABLE | UNCLASSIFIED | DIRECT. C++: GetLastModified() const."""
        ...
    def get_id(self) -> int:
        """AVAILABLE | UNCLASSIFIED | DIRECT. C++: GetId() const."""
        ...
    def get_name(self) -> str:
        """AVAILABLE | UNCLASSIFIED | DIRECT. C++: GetName() const."""
        ...

class LeaseClient(ClientBase):
    def __init__(self, name: str) -> None:
        """AVAILABLE; C++: unitree::robot::LeaseClient::LeaseClient(const std::string &)."""
        ...
    def init(self) -> None:
        """AVAILABLE | INITIALIZATION | DIRECT. C++: Init()."""
        ...
    def wait_applied(self) -> None:
        """AVAILABLE | INITIALIZATION | DIRECT. C++: WaitApplied()."""
        ...
    def get_id(self) -> int:
        """AVAILABLE | READ_ONLY | DIRECT. C++: GetId()."""
        ...
    def applied(self) -> bool:
        """AVAILABLE | READ_ONLY | DIRECT. C++: Applied()."""
        ...

class LeaseContext(object):
    def __init__(self) -> None:
        """AVAILABLE; C++: unitree::robot::LeaseContext::LeaseContext()."""
        ...
    def update(self, id: int, term: int) -> None:
        """AVAILABLE | UNCLASSIFIED | DIRECT. C++: Update(int64_t, int64_t)."""
        ...
    def reset(self) -> None:
        """AVAILABLE | UNCLASSIFIED | DIRECT. C++: Reset()."""
        ...
    def valid(self) -> bool:
        """AVAILABLE | UNCLASSIFIED | DIRECT. C++: Valid() const."""
        ...
    def get_id(self) -> int:
        """AVAILABLE | UNCLASSIFIED | DIRECT. C++: GetId() const."""
        ...
    def get_term(self) -> int:
        """AVAILABLE | UNCLASSIFIED | DIRECT. C++: GetTerm() const."""
        ...

class LeaseServer(ServerBase):
    def __init__(self, name: str, term: int) -> None:
        """SIGNATURE_ONLY; C++: unitree::robot::LeaseServer::LeaseServer(const std::string &, int64_t)."""
        ...
    def init(self) -> None:
        """SIGNATURE_ONLY | UNCLASSIFIED | SIGNATURE_PREVIEW. C++: Init()."""
        ...
    def check_request_lease_denied(self, lease_id: int) -> bool:
        """SIGNATURE_ONLY | UNCLASSIFIED | SIGNATURE_PREVIEW. C++: CheckRequestLeaseDenied(int64_t)."""
        ...

class RequestFuture(object):
    @overload
    def __init__(self) -> None:
        """SIGNATURE_ONLY; C++: unitree::robot::RequestFuture::RequestFuture()."""
        ...
    @overload
    def __init__(self, request_id: int) -> None:
        """SIGNATURE_ONLY; C++: unitree::robot::RequestFuture::RequestFuture(int64_t)."""
        ...
    def set_request_id(self, request_id: int) -> None:
        """SIGNATURE_ONLY | UNCLASSIFIED | SIGNATURE_PREVIEW. C++: SetRequestId(int64_t)."""
        ...
    def get_request_id(self) -> int:
        """SIGNATURE_ONLY | UNCLASSIFIED | SIGNATURE_PREVIEW. C++: GetRequestId() const."""
        ...
    def set_queue(self, future_queue_ptr: RequestFutureQueue) -> bool:
        """SIGNATURE_ONLY | UNCLASSIFIED | SIGNATURE_PREVIEW. C++: SetQueue(const std::shared_ptr<RequestFutureQueue> &)."""
        ...
    def get_response(self, microsec: int) -> Any:
        """SIGNATURE_ONLY | UNCLASSIFIED | SIGNATURE_PREVIEW. C++: GetResponse(int64_t)."""
        ...
    def ready(self, request_ptr: Any) -> None:
        """SIGNATURE_ONLY | UNCLASSIFIED | SIGNATURE_PREVIEW. C++: Ready(const unitree::robot::ResponsePtr &)."""
        ...

class RequestFutureQueue(object):
    def __init__(self) -> None:
        """SIGNATURE_ONLY; C++: unitree::robot::RequestFutureQueue::RequestFutureQueue()."""
        ...
    def get(self, request_id: int) -> RequestFuture:
        """SIGNATURE_ONLY | UNCLASSIFIED | SIGNATURE_PREVIEW. C++: Get(int64_t)."""
        ...
    def put(self, request_id: int, future_ptr: RequestFuture) -> bool:
        """SIGNATURE_ONLY | UNCLASSIFIED | SIGNATURE_PREVIEW. C++: Put(int64_t, const unitree::robot::RequestFuturePtr &)."""
        ...
    def remove(self, request_id: int) -> None:
        """SIGNATURE_ONLY | UNCLASSIFIED | SIGNATURE_PREVIEW. C++: Remove(int64_t)."""
        ...
    def size(self) -> int:
        """SIGNATURE_ONLY | UNCLASSIFIED | SIGNATURE_PREVIEW. C++: Size()."""
        ...

class Server(ServerBase):
    def __init__(self, name: str) -> None:
        """SIGNATURE_ONLY; C++: unitree::robot::Server::Server(const std::string &)."""
        ...
    def init(self) -> None:
        """SIGNATURE_ONLY | UNCLASSIFIED | SIGNATURE_PREVIEW. C++: Init()."""
        ...
    @overload
    def start_lease(self, lease_term: int) -> None:
        """SIGNATURE_ONLY | UNCLASSIFIED | SIGNATURE_PREVIEW. C++: StartLease(int64_t)."""
        ...
    @overload
    def start_lease(self, lease_term: float) -> None:
        """SIGNATURE_ONLY | UNCLASSIFIED | SIGNATURE_PREVIEW. C++: StartLease(float)."""
        ...
    def get_name(self) -> str:
        """SIGNATURE_ONLY | UNCLASSIFIED | SIGNATURE_PREVIEW. C++: GetName()."""
        ...
    def get_api_version(self) -> str:
        """SIGNATURE_ONLY | UNCLASSIFIED | SIGNATURE_PREVIEW. C++: GetApiVersion() const."""
        ...
    def get_current_api_id(self) -> int:
        """SIGNATURE_ONLY | UNCLASSIFIED | SIGNATURE_PREVIEW. C++: GetCurrentApiId() const."""
        ...

class ServerBase(object):
    def __init__(self, name: str) -> None:
        """SIGNATURE_ONLY; C++: unitree::robot::ServerBase::ServerBase(const std::string &)."""
        ...
    def init(self) -> None:
        """SIGNATURE_ONLY | UNCLASSIFIED | SIGNATURE_PREVIEW. C++: Init()."""
        ...
    def start(self, enable_proi_queue: bool = ...) -> None:
        """SIGNATURE_ONLY | UNCLASSIFIED | SIGNATURE_PREVIEW. C++: Start(bool)."""
        ...
    def get_name(self) -> str:
        """SIGNATURE_ONLY | UNCLASSIFIED | SIGNATURE_PREVIEW. C++: GetName() const."""
        ...

class ServerChannelNamer(ChannelNamer):
    def __init__(self) -> None:
        """SIGNATURE_ONLY; C++: unitree::robot::ServerChannelNamer::ServerChannelNamer()."""
        ...

class ServerStub(object):
    def __init__(self) -> None:
        """SIGNATURE_ONLY; C++: unitree::robot::ServerStub::ServerStub()."""
        ...
    def init(self, name: str, handler: Callable[..., Any], enable_proi_queue: bool) -> None:
        """SIGNATURE_ONLY | UNCLASSIFIED | SIGNATURE_PREVIEW. C++: Init(const std::string &, const unitree::robot::ServerRequestHandler &, bool)."""
        ...
    def send(self, response: Any, timeout: int = ...) -> bool:
        """SIGNATURE_ONLY | UNCLASSIFIED | SIGNATURE_PREVIEW. C++: Send(const unitree::robot::Response &, int64_t)."""
        ...
