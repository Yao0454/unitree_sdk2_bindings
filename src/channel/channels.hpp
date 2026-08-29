#pragma once

#include <atomic>
#include <cstdint>
#include <functional>
#include <memory>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

#include <pybind11/pybind11.h>

#include <unitree/robot/channel/channel_publisher.hpp>
#include <unitree/robot/channel/channel_subscriber.hpp>

namespace unitree_sdk2_binding {

namespace py = pybind11;

inline bool IsPythonRuntimeActive() noexcept {
    if (!Py_IsInitialized()) {
        return false;
    }
#if PY_VERSION_HEX >= 0x030D0000
    return !Py_IsFinalizing();
#else
    return !_Py_IsFinalizing();
#endif
}

class PythonCallbackState {
public:
    explicit PythonCallbackState(py::function callback)
        : callback_(std::move(callback)) {}

    ~PythonCallbackState() {
        if (!IsPythonRuntimeActive()) {
            (void)callback_.release();
        } else if (PyGILState_Check()) {
            py::function callback = std::move(callback_);
        } else {
            py::gil_scoped_acquire gil;
            py::function callback = std::move(callback_);
        }
    }

    template <typename Message>
    void invoke(const Message &message) noexcept {
        if (!active_.load(std::memory_order_acquire) ||
            !IsPythonRuntimeActive()) {
            return;
        }
        py::gil_scoped_acquire gil;
        if (!active_.load(std::memory_order_relaxed)) {
            return;
        }
        try {
            py::object value =
                py::cast(Message(message), py::return_value_policy::move);
            callback_(std::move(value));
        } catch (py::error_already_set &error) {
            error.discard_as_unraisable("Unitree DDS subscriber callback");
        } catch (...) {
            PyErr_SetString(PyExc_RuntimeError,
                            "unknown exception in Unitree DDS callback");
            PyErr_WriteUnraisable(callback_.ptr());
        }
    }

    void deactivate() noexcept {
        active_.store(false, std::memory_order_release);
    }

    void activate() noexcept {
        active_.store(true, std::memory_order_release);
    }

private:
    py::function callback_;
    std::atomic<bool> active_{true};
};

class ChannelTypeRegistry {
public:
    using PublisherFactory = std::function<std::shared_ptr<void>(const std::string &)>;
    using SubscriberFactory = std::function<std::shared_ptr<void>(
        const std::string &, std::shared_ptr<PythonCallbackState>, int32_t)>;
    using CloseFunction = std::function<void(void *)>;
    using PublisherInitFunction = std::function<void(void *)>;
    using PublisherWriteFunction = std::function<bool(void *, py::handle, int64_t)>;
    using SubscriberInitFunction = std::function<void(void *)>;
    using SubscriberTimeFunction = std::function<int64_t(const void *)>;

    struct Entry {
        std::string name;
        PublisherFactory publisher_factory;
        SubscriberFactory subscriber_factory;
        PublisherInitFunction publisher_init;
        PublisherWriteFunction publisher_write;
        CloseFunction publisher_close;
        SubscriberInitFunction subscriber_init;
        CloseFunction subscriber_close;
        SubscriberTimeFunction subscriber_time;
    };

    template <typename Message>
    void add(const char *name) {
        py::type type = py::type::of<Message>();
        Entry entry{
            name,
            [](const std::string &topic) {
                return std::static_pointer_cast<void>(
                    std::make_shared<unitree::robot::ChannelPublisher<Message>>(topic));
            },
            [](const std::string &topic, std::shared_ptr<PythonCallbackState> state,
               int32_t queue_length) {
                auto subscriber = std::make_shared<
                    unitree::robot::ChannelSubscriber<Message>>(
                    topic,
                    [state = std::move(state)](const void *value) {
                        state->invoke(*static_cast<const Message *>(value));
                    },
                    queue_length);
                return std::static_pointer_cast<void>(std::move(subscriber));
            },
            [](void *value) {
                static_cast<unitree::robot::ChannelPublisher<Message> *>(value)
                    ->InitChannel();
            },
            [](void *value, py::handle message, int64_t wait_microsec) {
                Message typed;
                try {
                    typed = message.cast<Message>();
                } catch (const py::cast_error &) {
                    throw py::type_error(
                        "message is not an instance of the publisher's "
                        "registered DDS message type");
                }
                py::gil_scoped_release release;
                return static_cast<unitree::robot::ChannelPublisher<Message> *>(value)
                    ->Write(typed, wait_microsec);
            },
            [](void *value) {
                static_cast<unitree::robot::ChannelPublisher<Message> *>(value)
                    ->CloseChannel();
            },
            [](void *value) {
                static_cast<unitree::robot::ChannelSubscriber<Message> *>(value)
                    ->InitChannel();
            },
            [](void *value) {
                static_cast<unitree::robot::ChannelSubscriber<Message> *>(value)
                    ->CloseChannel();
            },
            [](const void *value) {
                return static_cast<const unitree::robot::ChannelSubscriber<Message> *>(
                           value)
                    ->GetLastDataAvailableTime();
            }};
        PyObject *key = type.ptr();
        auto [iter, inserted] = entries_.emplace(key, std::move(entry));
        if (inserted) {
            names_.push_back(iter->second.name);
        }
    }

    const Entry &find(py::handle type) const {
        auto iter = entries_.find(type.ptr());
        if (iter == entries_.end()) {
            throw py::type_error(
                "message_type is not a registered Unitree SDK2 DDS message class");
        }
        return iter->second;
    }

    const std::vector<std::string> &names() const { return names_; }

private:
    std::unordered_map<PyObject *, Entry> entries_;
    std::vector<std::string> names_;
};

class ChannelPublisher {
public:
    ChannelPublisher(const std::string &topic, py::handle message_type);
    ~ChannelPublisher();

    void init_channel();
    void close_channel();
    bool write(py::handle message, int64_t wait_microsec = 0);
    const std::string &topic() const;
    const std::string &message_type_name() const;

private:
    struct Concept;
    std::unique_ptr<Concept> concept_;
};

class ChannelSubscriber {
public:
    ChannelSubscriber(const std::string &topic, py::handle message_type,
                      py::function callback, int64_t queue_length = 0);
    ~ChannelSubscriber();

    void init_channel();
    void close_channel();
    int64_t last_data_available_time() const;
    const std::string &topic() const;
    const std::string &message_type_name() const;

private:
    struct Concept;
    std::unique_ptr<Concept> concept_;
};

void BindChannels(py::module_ &module);
ChannelTypeRegistry &GetChannelTypeRegistry();
void RegisterGeneratedChannelTypes(ChannelTypeRegistry &registry);

}  // namespace unitree_sdk2_binding
