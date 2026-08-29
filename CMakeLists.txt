cmake_minimum_required(VERSION 3.16)
project(unitree_sdk2_cpp LANGUAGES CXX)

option(UNITREE_REGENERATE_BINDINGS
  "Regenerate checked-in binding sources from Clang AST" OFF)

if(NOT CMAKE_SYSTEM_NAME STREQUAL "Linux")
  message(FATAL_ERROR
    "The bundled Unitree SDK2 and CycloneDDS libraries are Linux ELF binaries; "
    "this proof of concept must be built on Linux.")
endif()

if(CMAKE_SYSTEM_PROCESSOR MATCHES "^(x86_64|amd64|AMD64)$")
  set(UNITREE_ARCH x86_64)
elseif(CMAKE_SYSTEM_PROCESSOR MATCHES "^(aarch64|arm64)$")
  set(UNITREE_ARCH aarch64)
else()
  message(FATAL_ERROR "Unsupported architecture: ${CMAKE_SYSTEM_PROCESSOR}")
endif()

set(UNITREE_SDK_ROOT "${CMAKE_CURRENT_LIST_DIR}/.." CACHE PATH
  "Path to the unitree_sdk2 source tree")

find_package(Python REQUIRED COMPONENTS Interpreter Development.Module)
find_package(pybind11 CONFIG REQUIRED)
find_package(Threads REQUIRED)

if(UNITREE_REGENERATE_BINDINGS)
  find_program(UNITREE_CLANG_EXECUTABLE NAMES clang++ REQUIRED)
  file(GLOB_RECURSE UNITREE_IDL_HEADERS CONFIGURE_DEPENDS
    "${UNITREE_SDK_ROOT}/include/unitree/idl/*.hpp")
  file(GLOB_RECURSE UNITREE_ROBOT_HEADERS CONFIGURE_DEPENDS
    "${UNITREE_SDK_ROOT}/include/unitree/robot/*.hpp")
  set(UNITREE_IDL_INVENTORY
    "${CMAKE_CURRENT_LIST_DIR}/generated/idl_inventory.json")
  set(UNITREE_IDL_REPORT_GO2
    "${CMAKE_CURRENT_LIST_DIR}/generated/idl_go2_report.json")
  set(UNITREE_IDL_REPORT_HG
    "${CMAKE_CURRENT_LIST_DIR}/generated/idl_hg_report.json")
  set(UNITREE_IDL_REPORT_HG_DOUBLEIMU
    "${CMAKE_CURRENT_LIST_DIR}/generated/idl_hg_doubleimu_report.json")
  set(UNITREE_IDL_REPORT_ROS2
    "${CMAKE_CURRENT_LIST_DIR}/generated/idl_ros2_report.json")
  set(UNITREE_IDL_BINDING_GO2
    "${CMAKE_CURRENT_LIST_DIR}/src/generated/idl/go2.cpp")
  set(UNITREE_IDL_BINDING_HG
    "${CMAKE_CURRENT_LIST_DIR}/src/generated/idl/hg.cpp")
  set(UNITREE_IDL_BINDING_HG_DOUBLEIMU
    "${CMAKE_CURRENT_LIST_DIR}/src/generated/idl/hg_doubleimu.cpp")
  set(UNITREE_IDL_BINDING_ROS2
    "${CMAKE_CURRENT_LIST_DIR}/src/generated/idl/ros2.cpp")
  set(UNITREE_CHANNEL_REGISTRY
    "${CMAKE_CURRENT_LIST_DIR}/src/generated/channel_registry.cpp")
  set(UNITREE_CHANNEL_REGISTRY_REPORT
    "${CMAKE_CURRENT_LIST_DIR}/generated/channel_registry_report.json")
  set(UNITREE_ROBOT_INVENTORY
    "${CMAKE_CURRENT_LIST_DIR}/generated/robot_inventory.json")
  set(UNITREE_ROBOT_CLASSIFICATION_REPORT
    "${CMAKE_CURRENT_LIST_DIR}/generated/robot_binding_report.json")
  set(UNITREE_ROBOT_READ_ONLY_BINDING
    "${CMAKE_CURRENT_LIST_DIR}/src/generated/robot_read_only.cpp")
  set(UNITREE_ROBOT_READ_ONLY_REPORT
    "${CMAKE_CURRENT_LIST_DIR}/generated/robot_read_only_report.json")
  add_custom_command(
    OUTPUT
      "${UNITREE_IDL_INVENTORY}"
      "${UNITREE_IDL_REPORT_GO2}"
      "${UNITREE_IDL_REPORT_HG}"
      "${UNITREE_IDL_REPORT_HG_DOUBLEIMU}"
      "${UNITREE_IDL_REPORT_ROS2}"
      "${UNITREE_IDL_BINDING_GO2}"
      "${UNITREE_IDL_BINDING_HG}"
      "${UNITREE_IDL_BINDING_HG_DOUBLEIMU}"
      "${UNITREE_IDL_BINDING_ROS2}"
      "${UNITREE_CHANNEL_REGISTRY}"
      "${UNITREE_CHANNEL_REGISTRY_REPORT}"
      "${UNITREE_ROBOT_INVENTORY}"
      "${UNITREE_ROBOT_CLASSIFICATION_REPORT}"
      "${UNITREE_ROBOT_READ_ONLY_BINDING}"
      "${UNITREE_ROBOT_READ_ONLY_REPORT}"
    COMMAND "${Python_EXECUTABLE}"
      "${CMAKE_CURRENT_LIST_DIR}/generator/scan_headers.py"
      --sdk-root "${UNITREE_SDK_ROOT}"
      --clang "${UNITREE_CLANG_EXECUTABLE}"
      --output "${UNITREE_IDL_INVENTORY}"
      include/unitree/idl
    COMMAND "${Python_EXECUTABLE}"
      "${CMAKE_CURRENT_LIST_DIR}/generator/generate_bindings.py"
      --inventory "${UNITREE_IDL_INVENTORY}"
      --overrides "${CMAKE_CURRENT_LIST_DIR}/generator/overrides.yaml"
      --namespace-prefix unitree_go::msg::dds_
      --function BindGo2Idl
      --module idl
      --module go2
      --output "${UNITREE_IDL_BINDING_GO2}"
      --report "${UNITREE_IDL_REPORT_GO2}"
    COMMAND "${Python_EXECUTABLE}"
      "${CMAKE_CURRENT_LIST_DIR}/generator/generate_bindings.py"
      --inventory "${UNITREE_IDL_INVENTORY}"
      --overrides "${CMAKE_CURRENT_LIST_DIR}/generator/overrides.yaml"
      --namespace-prefix unitree_hg::msg::dds_
      --function BindHgIdl
      --module idl
      --module hg
      --output "${UNITREE_IDL_BINDING_HG}"
      --report "${UNITREE_IDL_REPORT_HG}"
    COMMAND "${Python_EXECUTABLE}"
      "${CMAKE_CURRENT_LIST_DIR}/generator/generate_bindings.py"
      --inventory "${UNITREE_IDL_INVENTORY}"
      --overrides "${CMAKE_CURRENT_LIST_DIR}/generator/overrides.yaml"
      --namespace-prefix unitree_hg_doubleimu::msg::dds_
      --function BindHgDoubleImuIdl
      --module idl
      --module hg_doubleimu
      --output "${UNITREE_IDL_BINDING_HG_DOUBLEIMU}"
      --report "${UNITREE_IDL_REPORT_HG_DOUBLEIMU}"
    COMMAND "${Python_EXECUTABLE}"
      "${CMAKE_CURRENT_LIST_DIR}/generator/generate_bindings.py"
      --inventory "${UNITREE_IDL_INVENTORY}"
      --overrides "${CMAKE_CURRENT_LIST_DIR}/generator/overrides.yaml"
      --namespace-prefix builtin_interfaces::msg::dds_
      --namespace-prefix geometry_msgs::msg::dds_
      --namespace-prefix nav_msgs::msg::dds_
      --namespace-prefix sensor_msgs::msg::dds_
      --namespace-prefix std_msgs::msg::dds_
      --function BindRos2Idl
      --module idl
      --module ros2
      --output "${UNITREE_IDL_BINDING_ROS2}"
      --report "${UNITREE_IDL_REPORT_ROS2}"
    COMMAND "${Python_EXECUTABLE}"
      "${CMAKE_CURRENT_LIST_DIR}/generator/generate_channel_registry.py"
      --inventory "${UNITREE_IDL_INVENTORY}"
      --output "${UNITREE_CHANNEL_REGISTRY}"
      --report "${UNITREE_CHANNEL_REGISTRY_REPORT}"
    COMMAND "${Python_EXECUTABLE}"
      "${CMAKE_CURRENT_LIST_DIR}/generator/scan_headers.py"
      --sdk-root "${UNITREE_SDK_ROOT}"
      --clang "${UNITREE_CLANG_EXECUTABLE}"
      --output "${UNITREE_ROBOT_INVENTORY}"
      include/unitree/robot
    COMMAND "${Python_EXECUTABLE}"
      "${CMAKE_CURRENT_LIST_DIR}/generator/classify_robot_api.py"
      --inventory "${UNITREE_ROBOT_INVENTORY}"
      --output "${UNITREE_ROBOT_CLASSIFICATION_REPORT}"
    COMMAND "${Python_EXECUTABLE}"
      "${CMAKE_CURRENT_LIST_DIR}/generator/generate_robot_read_only_bindings.py"
      --inventory "${UNITREE_ROBOT_INVENTORY}"
      --classification "${UNITREE_ROBOT_CLASSIFICATION_REPORT}"
      --policy "${CMAKE_CURRENT_LIST_DIR}/generator/robot_read_only_policy.json"
      --output "${UNITREE_ROBOT_READ_ONLY_BINDING}"
      --report "${UNITREE_ROBOT_READ_ONLY_REPORT}"
    DEPENDS
      "${CMAKE_CURRENT_LIST_DIR}/generator/model.py"
      "${CMAKE_CURRENT_LIST_DIR}/generator/scan_headers.py"
      "${CMAKE_CURRENT_LIST_DIR}/generator/generate_bindings.py"
      "${CMAKE_CURRENT_LIST_DIR}/generator/generate_channel_registry.py"
      "${CMAKE_CURRENT_LIST_DIR}/generator/classify_robot_api.py"
      "${CMAKE_CURRENT_LIST_DIR}/generator/generate_robot_read_only_bindings.py"
      "${CMAKE_CURRENT_LIST_DIR}/generator/robot_read_only_policy.json"
      "${CMAKE_CURRENT_LIST_DIR}/generator/overrides.yaml"
      ${UNITREE_IDL_HEADERS}
      ${UNITREE_ROBOT_HEADERS}
  VERBATIM)
  add_custom_target(generate_bindings DEPENDS
    "${UNITREE_IDL_INVENTORY}"
    "${UNITREE_IDL_REPORT_GO2}"
    "${UNITREE_IDL_REPORT_HG}"
    "${UNITREE_IDL_REPORT_HG_DOUBLEIMU}"
    "${UNITREE_IDL_REPORT_ROS2}"
    "${UNITREE_IDL_BINDING_GO2}"
    "${UNITREE_IDL_BINDING_HG}"
    "${UNITREE_IDL_BINDING_HG_DOUBLEIMU}"
    "${UNITREE_IDL_BINDING_ROS2}"
    "${UNITREE_CHANNEL_REGISTRY}"
    "${UNITREE_CHANNEL_REGISTRY_REPORT}"
    "${UNITREE_ROBOT_INVENTORY}"
    "${UNITREE_ROBOT_CLASSIFICATION_REPORT}"
    "${UNITREE_ROBOT_READ_ONLY_BINDING}"
    "${UNITREE_ROBOT_READ_ONLY_REPORT}")
endif()

set(UNITREE_SDK_LIBRARY
  "${UNITREE_SDK_ROOT}/lib/${UNITREE_ARCH}/libunitree_sdk2.a")
set(UNITREE_DDS_LIBRARY
  "${UNITREE_SDK_ROOT}/thirdparty/lib/${UNITREE_ARCH}/libddsc.so")
set(UNITREE_DDSXX_LIBRARY
  "${UNITREE_SDK_ROOT}/thirdparty/lib/${UNITREE_ARCH}/libddscxx.so")

foreach(required_file IN ITEMS
    "${UNITREE_SDK_LIBRARY}"
    "${UNITREE_DDS_LIBRARY}"
    "${UNITREE_DDSXX_LIBRARY}")
  if(NOT EXISTS "${required_file}")
    message(FATAL_ERROR "Required Unitree library not found: ${required_file}")
  endif()
endforeach()

add_library(unitree_sdk2 STATIC IMPORTED GLOBAL)
set_target_properties(unitree_sdk2 PROPERTIES
  IMPORTED_LOCATION "${UNITREE_SDK_LIBRARY}")

add_library(unitree_ddsc SHARED IMPORTED GLOBAL)
set_target_properties(unitree_ddsc PROPERTIES
  IMPORTED_LOCATION "${UNITREE_DDS_LIBRARY}"
  IMPORTED_NO_SONAME TRUE)

add_library(unitree_ddscxx SHARED IMPORTED GLOBAL)
set_target_properties(unitree_ddscxx PROPERTIES
  IMPORTED_LOCATION "${UNITREE_DDSXX_LIBRARY}"
  IMPORTED_NO_SONAME TRUE)

pybind11_add_module(unitree_sdk2_cpp MODULE
  src/module.cpp
  src/common/os.cpp
  src/channel/channels.cpp
  src/generated/channel_registry.cpp
  src/generated/idl/go2.cpp
  src/generated/idl/hg.cpp
  src/robot/g1.cpp
  src/generated/idl/hg_doubleimu.cpp
  src/generated/idl/ros2.cpp
  src/generated/robot_read_only.cpp)
if(TARGET generate_bindings)
  add_dependencies(unitree_sdk2_cpp generate_bindings)
endif()
target_compile_features(unitree_sdk2_cpp PRIVATE cxx_std_17)
target_include_directories(unitree_sdk2_cpp PRIVATE
  "${CMAKE_CURRENT_LIST_DIR}/src"
  "${UNITREE_SDK_ROOT}/include"
  "${UNITREE_SDK_ROOT}/thirdparty/include"
  "${UNITREE_SDK_ROOT}/thirdparty/include/ddscxx")
target_link_libraries(unitree_sdk2_cpp PRIVATE
  unitree_sdk2
  unitree_ddsc
  unitree_ddscxx
  Threads::Threads)
target_link_options(unitree_sdk2_cpp PRIVATE "LINKER:--no-as-needed")

set_target_properties(unitree_sdk2_cpp PROPERTIES
  BUILD_RPATH "${UNITREE_SDK_ROOT}/thirdparty/lib/${UNITREE_ARCH}"
  INSTALL_RPATH "$ORIGIN/.libs")

install(TARGETS unitree_sdk2_cpp LIBRARY DESTINATION .)
install(FILES "${UNITREE_DDS_LIBRARY}" DESTINATION .libs)
install(FILES "${UNITREE_DDS_LIBRARY}"
  DESTINATION .libs RENAME libddsc.so.0)
install(FILES "${UNITREE_DDSXX_LIBRARY}" DESTINATION .libs)
install(FILES "${UNITREE_DDSXX_LIBRARY}"
  DESTINATION .libs RENAME libddscxx.so.0)
