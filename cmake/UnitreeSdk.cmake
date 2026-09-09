# Keep SDK discovery independent of the caller's working directory.
get_filename_component(_unitree_bindings_root "${CMAKE_CURRENT_LIST_DIR}/.." ABSOLUTE)
set(UNITREE_SDK_ROOT "" CACHE PATH "Path to the Unitree SDK2 source tree")

if(NOT UNITREE_SDK_ROOT)
  if(DEFINED ENV{UNITREE_SDK_ROOT} AND NOT "$ENV{UNITREE_SDK_ROOT}" STREQUAL "")
    set(UNITREE_SDK_ROOT "$ENV{UNITREE_SDK_ROOT}")
  elseif(EXISTS "${_unitree_bindings_root}/thirdparty/unitree_sdk2")
    set(UNITREE_SDK_ROOT "${_unitree_bindings_root}/thirdparty/unitree_sdk2")
  elseif(EXISTS "${_unitree_bindings_root}/../include/unitree/robot/channel/channel_factory.hpp")
    # Compatibility with older SDK checkouts containing this bindings folder.
    set(UNITREE_SDK_ROOT "${_unitree_bindings_root}/..")
  else()
    message(FATAL_ERROR
      "Unitree SDK2 not found. In the bindings repository, run:\n"
      "  git clone https://github.com/unitreerobotics/unitree_sdk2.git thirdparty/unitree_sdk2\n"
      "Or pass -DUNITREE_SDK_ROOT=/absolute/path/to/unitree_sdk2.")
  endif()
endif()

get_filename_component(UNITREE_SDK_ROOT "${UNITREE_SDK_ROOT}" ABSOLUTE
  BASE_DIR "${_unitree_bindings_root}")
set(UNITREE_SDK_ROOT "${UNITREE_SDK_ROOT}" CACHE PATH
  "Path to the Unitree SDK2 source tree" FORCE)

foreach(_unitree_header IN ITEMS
    include/unitree/robot/channel/channel_factory.hpp
    include/unitree/robot/go2/sport/sport_client.hpp
    include/unitree/idl/go2/LowState_.hpp
    thirdparty/include/dds/dds.h
    thirdparty/include/ddscxx/dds/dds.hpp)
  if(NOT EXISTS "${UNITREE_SDK_ROOT}/${_unitree_header}")
    message(FATAL_ERROR
      "Incomplete Unitree SDK2 source tree: ${UNITREE_SDK_ROOT}/${_unitree_header} is missing. "
      "Clone the full SDK repository, or correct UNITREE_SDK_ROOT.")
  endif()
endforeach()

set(UNITREE_SDK_LIBRARY "${UNITREE_SDK_ROOT}/lib/${UNITREE_ARCH}/libunitree_sdk2.a")
set(UNITREE_DDS_LIBRARY "${UNITREE_SDK_ROOT}/thirdparty/lib/${UNITREE_ARCH}/libddsc.so")
set(UNITREE_DDSXX_LIBRARY "${UNITREE_SDK_ROOT}/thirdparty/lib/${UNITREE_ARCH}/libddscxx.so")
foreach(_unitree_library IN ITEMS
    "${UNITREE_SDK_LIBRARY}" "${UNITREE_DDS_LIBRARY}" "${UNITREE_DDSXX_LIBRARY}")
  if(NOT EXISTS "${_unitree_library}")
    message(FATAL_ERROR "Required Unitree library for ${UNITREE_ARCH} not found: ${_unitree_library}")
  endif()
endforeach()
message(STATUS "Unitree SDK2 root: ${UNITREE_SDK_ROOT} (${UNITREE_ARCH})")
