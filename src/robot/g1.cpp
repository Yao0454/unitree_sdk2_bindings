#include "bindings.hpp"
#include "channel/channels.hpp"

#include <cstdint>

#include <pybind11/pybind11.h>

#include <unitree/dds_wrapper/common/crc.h>
#include <unitree/idl/hg/LowCmd_.hpp>
#include <unitree/idl/hg/LowState_.hpp>
#include <unitree/robot/g1/common/terminations.hpp>

namespace py = pybind11;

namespace {

template <typename Message> uint32_t ComputeG1Crc(const Message &message) {
    static_assert(sizeof(Message) % sizeof(uint32_t) == 0);
    static_assert(alignof(Message) >= alignof(uint32_t));
    auto *words = reinterpret_cast<uint32_t *>(const_cast<Message *>(&message));
    return crc32_core(words, static_cast<uint32_t>(sizeof(Message) / sizeof(uint32_t) - 1));
}

} // namespace

void BindG1Support(py::module_ &root) {
    py::module_ idl = EnsureSubmodule(root, "idl");
    py::module_ hg = EnsureSubmodule(idl, "hg");
    py::module_ g1 = EnsureSubmodule(idl, "g1");

    for (const char *name : {
             "AgvBmsState",
             "BmsCmd",
             "BmsState",
             "HandCmd",
             "HandState",
             "IMUState",
             "LowCmd",
             "LowState",
             "MainBoardState",
             "MotorCmd",
             "MotorState",
             "PressSensorState",
             "SportModeState",
         }) {
        g1.attr(name) = hg.attr(name);
    }

    using LowCmd = unitree_hg::msg::dds_::LowCmd_;
    using LowState = unitree_hg::msg::dds_::LowState_;

    g1.def(
        "compute_crc", [](const LowCmd &message) { return ComputeG1Crc(message); },
        py::arg("message"));
    g1.def(
        "compute_crc", [](const LowState &message) { return ComputeG1Crc(message); },
        py::arg("message"));
    g1.def(
        "update_crc",
        [](LowCmd &message) {
            const uint32_t value = ComputeG1Crc(message);
            message.crc(value);
            return value;
        },
        py::arg("message"));
    g1.def(
        "validate_crc",
        [](const LowCmd &message) { return message.crc() == ComputeG1Crc(message); },
        py::arg("message"));
    g1.def(
        "validate_crc",
        [](const LowState &message) { return message.crc() == ComputeG1Crc(message); },
        py::arg("message"));

    py::module_ robot = EnsureSubmodule(root, "robot");
    py::module_ robot_g1 = EnsureSubmodule(robot, "g1");
    robot_g1.def("bad_orientation", &unitree::robot::g1::bad_orientation, py::arg("low_state"),
                 py::arg("limit_angle") = 1.0F);
    robot_g1.def("joint_vel_out_of_limit", &unitree::robot::g1::joint_vel_out_of_limit,
                 py::arg("low_state"), py::arg("limit_vel") = 10.0F);
    robot_g1.def("ang_vel_out_of_limit", &unitree::robot::g1::ang_vel_out_of_limit,
                 py::arg("low_state"), py::arg("limit_vel") = 6.0F);
    robot_g1.def("motor_winding_overheat", &unitree::robot::g1::motor_winding_overheat,
                 py::arg("low_state"), py::arg("limit_temp") = 120.0F);
    robot_g1.def("motor_casing_overheat", &unitree::robot::g1::motor_casing_overheat,
                 py::arg("low_state"), py::arg("limit_temp") = 85.0F);
    robot_g1.def("low_battery", &unitree::robot::g1::low_battery, py::arg("bms_state"),
                 py::arg("limit_soc") = 20.0F);
    robot_g1.def(
        "lost_connection",
        [](const unitree_sdk2_binding::ChannelSubscriber &subscriber, int64_t timeout_ms) {
            if (subscriber.message_type_name() != "unitree_sdk2_cpp.idl.hg.LowState") {
                throw py::type_error("subscriber must use unitree_sdk2_cpp.idl.g1.LowState");
            }
            const int64_t last_data_time = subscriber.last_data_available_time();
            if (last_data_time < 0) {
                return true;
            }
            const auto now = unitree::common::GetCurrentMonotonicTimeNanosecond();
            const double elapsed_ms = (now - static_cast<uint64_t>(last_data_time)) / 1e6;
            return elapsed_ms > timeout_ms;
        },
        py::arg("subscriber"), py::arg("timeout_ms") = 1000);
}
