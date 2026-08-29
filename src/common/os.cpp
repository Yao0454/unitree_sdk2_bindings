#include "bindings.hpp"

#include <unitree/common/os.hpp>

namespace py = pybind11;

void BindCommon(py::module_ &module) {
    py::class_<unitree::common::OsHelper>(module, "OsHelper")
        .def_static("instance", &unitree::common::OsHelper::Instance,
                    py::return_value_policy::reference)
        .def("get_uid", &unitree::common::OsHelper::GetUID)
        .def("get_gid", &unitree::common::OsHelper::GetGID)
        .def("get_user", &unitree::common::OsHelper::GetUser)
        .def("get_processor_number", &unitree::common::OsHelper::GetProcessorNumber)
        .def("get_page_size", &unitree::common::OsHelper::GetPageSize)
        .def("get_hostname", &unitree::common::OsHelper::GetHostname,
             py::return_value_policy::reference_internal);
}
