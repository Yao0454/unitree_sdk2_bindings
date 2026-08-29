#include "channels.hpp"

#include <atomic>
#include <limits>
#include <stdexcept>
#include <utility>

#include <pybind11/stl.h>

namespace unitree_sdk2_binding {
namespace {

std::atomic<bool> channel_factory_initialized{false};

void RequireChannelFactoryInitialized() {
    if (!channel_factory_initialized.load(std::memory_order_acquire)) {
        throw std::runtime_error(
            "DDS channel factory is not initialized; call "
            "unitree_sdk2_cpp.channel.initialize(...) first");
    }
}

int32_t ValidateQueueLength(int64_t queue_length) {
    // The SDK's DDS queue API stores this value in int32_t.  Reject values
    // that would otherwise silently wrap when crossing the Python boundary.
    if (queue_length < std::numeric_limits<int32_t>::min() ||
        queue_length > std::numeric_limits<int32_t>::max()) {
        throw py::value_error("queue_length exceeds the SDK int32_t limit");
    }
    return static_cast<int32_t>(queue_length);
}

}  // namespace

ChannelTypeRegistry &GetChannelTypeRegistry() {
    static auto *instance = new ChannelTypeRegistry();
    return *instance;
}

struct ChannelPublisher::Concept {
    Concept(const std::string &topic, const ChannelTypeRegistry::Entry &entry)
        : topic(topic), entry(entry), storage(entry.publisher_factory(topic)) {}

    ~Concept() {
        if (storage) {
            entry.publisher_close(storage.get());
        }
    }

    std::string topic;
    ChannelTypeRegistry::Entry entry;
    std::shared_ptr<void> storage;
};

struct ChannelSubscriber::Concept {
    Concept(const std::string &topic, const ChannelTypeRegistry::Entry &entry,
            py::function callback, int32_t queue_length)
        : topic(topic), entry(entry), callback_state(
              std::make_shared<PythonCallbackState>(std::move(callback))),
          storage(entry.subscriber_factory(topic, callback_state,
                                            ValidateQueueLength(queue_length))) {}

    ~Concept() {
        callback_state->deactivate();
        if (storage) {
            entry.subscriber_close(storage.get());
        }
    }

    std::string topic;
    ChannelTypeRegistry::Entry entry;
    std::shared_ptr<PythonCallbackState> callback_state;
    std::shared_ptr<void> storage;
    std::atomic<bool> initialized{false};
};

ChannelPublisher::ChannelPublisher(const std::string &topic, py::handle message_type)
    : concept_(std::make_unique<Concept>(
          topic, GetChannelTypeRegistry().find(message_type))) {}

ChannelPublisher::~ChannelPublisher() {
    if (!concept_) {
        return;
    }
    if (IsPythonRuntimeActive() && PyGILState_Check()) {
        py::gil_scoped_release release;
        concept_.reset();
    } else {
        concept_.reset();
    }
}

void ChannelPublisher::init_channel() {
    RequireChannelFactoryInitialized();
    py::gil_scoped_release release;
    concept_->entry.publisher_init(concept_->storage.get());
}

void ChannelPublisher::close_channel() {
    py::gil_scoped_release release;
    concept_->entry.publisher_close(concept_->storage.get());
}

bool ChannelPublisher::write(py::handle message, int64_t wait_microsec) {
    return concept_->entry.publisher_write(concept_->storage.get(), message, wait_microsec);
}

const std::string &ChannelPublisher::topic() const { return concept_->topic; }

const std::string &ChannelPublisher::message_type_name() const {
    return concept_->entry.name;
}

ChannelSubscriber::ChannelSubscriber(const std::string &topic, py::handle message_type,
                                     py::function callback, int64_t queue_length)
    : concept_(nullptr) {
    const int32_t validated_queue_length = ValidateQueueLength(queue_length);
    concept_ = std::make_unique<Concept>(
        topic, GetChannelTypeRegistry().find(message_type), std::move(callback),
        validated_queue_length);
}

ChannelSubscriber::~ChannelSubscriber() {
    if (!concept_) {
        return;
    }
    concept_->callback_state->deactivate();
    if (!IsPythonRuntimeActive() &&
        concept_->initialized.load(std::memory_order_acquire)) {
        // An active DDS worker may be waiting for the GIL while Python is
        // finalizing. The process will reclaim this reader; destroying it here
        // could deadlock finalization or enter the Python C API too late.
        (void)concept_.release();
    } else if (IsPythonRuntimeActive() && PyGILState_Check()) {
        py::gil_scoped_release release;
        concept_.reset();
    } else {
        concept_.reset();
    }
}

void ChannelSubscriber::init_channel() {
    RequireChannelFactoryInitialized();
    // A subscriber may be closed and initialized again.  Closing disables
    // callbacks before destroying the DDS reader; re-enable the same callback
    // state before installing a new reader.
    concept_->callback_state->activate();
    {
        py::gil_scoped_release release;
        concept_->entry.subscriber_init(concept_->storage.get());
    }
    concept_->initialized.store(true, std::memory_order_release);
}

void ChannelSubscriber::close_channel() {
    concept_->callback_state->deactivate();
    {
        py::gil_scoped_release release;
        concept_->entry.subscriber_close(concept_->storage.get());
    }
    concept_->initialized.store(false, std::memory_order_release);
}

int64_t ChannelSubscriber::last_data_available_time() const {
    return concept_->entry.subscriber_time(concept_->storage.get());
}

const std::string &ChannelSubscriber::topic() const { return concept_->topic; }

const std::string &ChannelSubscriber::message_type_name() const {
    return concept_->entry.name;
}

void BindChannels(py::module_ &module) {
    auto channel = module.def_submodule("channel");
    RegisterGeneratedChannelTypes(GetChannelTypeRegistry());
    channel.def("registered_message_types", []() {
        return GetChannelTypeRegistry().names();
    });
    channel.def(
        "initialize",
        [](int32_t domain_id, const std::string &network_interface) {
            py::gil_scoped_release release;
            unitree::robot::ChannelFactory::Instance()->Init(domain_id,
                                                              network_interface);
            channel_factory_initialized.store(true, std::memory_order_release);
        },
        py::arg("domain_id") = 0, py::arg("network_interface") = "");
    channel.def(
        "initialize_from_config",
        [](const std::string &config_file) {
            py::gil_scoped_release release;
            unitree::robot::ChannelFactory::Instance()->Init(config_file);
            channel_factory_initialized.store(true, std::memory_order_release);
        },
        py::arg("config_file") = "");
    channel.def("release", []() {
        py::gil_scoped_release release;
        unitree::robot::ChannelFactory::Instance()->Release();
        channel_factory_initialized.store(false, std::memory_order_release);
    });
    py::class_<ChannelPublisher>(channel, "ChannelPublisher")
        .def(py::init<const std::string &, py::handle>(), py::arg("topic"),
             py::arg("message_type"))
        .def("init_channel", &ChannelPublisher::init_channel)
        .def("close_channel", &ChannelPublisher::close_channel)
        .def("write", &ChannelPublisher::write, py::arg("message"),
             py::arg("wait_microsec") = 0)
        .def_property_readonly("topic", &ChannelPublisher::topic)
        .def_property_readonly("message_type_name", &ChannelPublisher::message_type_name);

    py::class_<ChannelSubscriber>(channel, "ChannelSubscriber")
        .def(py::init<const std::string &, py::handle, py::function, int64_t>(),
             py::arg("topic"), py::arg("message_type"), py::arg("callback"),
             py::arg("queue_length") = 0)
        .def("init_channel", &ChannelSubscriber::init_channel)
        .def("close_channel", &ChannelSubscriber::close_channel)
        .def_property_readonly("last_data_available_time",
                               &ChannelSubscriber::last_data_available_time)
        .def_property_readonly("topic", &ChannelSubscriber::topic)
        .def_property_readonly("message_type_name", &ChannelSubscriber::message_type_name);

}

}  // namespace unitree_sdk2_binding
