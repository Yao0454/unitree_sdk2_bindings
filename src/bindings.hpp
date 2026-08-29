#pragma once

#include <pybind11/pybind11.h>

inline pybind11::module_ EnsureSubmodule(pybind11::module_ parent,
                                         const char *name) {
    if (pybind11::hasattr(parent, name)) {
        return pybind11::reinterpret_borrow<pybind11::module_>(parent.attr(name));
    }
    return parent.def_submodule(name);
}

void BindCommon(pybind11::module_ &module);
void BindGo2Idl(pybind11::module_ &module);
void BindHgIdl(pybind11::module_ &module);
void BindG1Support(pybind11::module_ &module);
void BindHgDoubleImuIdl(pybind11::module_ &module);
void BindRos2Idl(pybind11::module_ &module);
void BindRobotClients(pybind11::module_ &module);
namespace unitree_sdk2_binding {
void BindChannels(pybind11::module_ &module);
}
