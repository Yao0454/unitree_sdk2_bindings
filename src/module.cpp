#include <pybind11/pybind11.h>

#include "bindings.hpp"

namespace py = pybind11;

PYBIND11_MODULE(unitree_sdk2_cpp, module) {
    module.doc() =
        "Unitree SDK2 C++ bindings with generated IDL messages and typed DDS channels";
    BindCommon(module);
    BindGo2Idl(module);
    BindHgIdl(module);
    BindHgDoubleImuIdl(module);
    BindRos2Idl(module);
    unitree_sdk2_binding::BindChannels(module);
    BindG1Support(module);
    BindRobotClients(module);
}
