"""Prove source companions forward to a real native module without an SDK/robot.

The tiny CPython extension below is a loader fixture, not a robot emulator.
"""

import json
import shutil
import subprocess
import sys
import sysconfig
from pathlib import Path

import pytest


SOURCES = Path(__file__).parents[1] / "stubs/src/unitree_sdk2_cpp"
NATIVE_SOURCE = r'''
#include <Python.h>
static struct PyModuleDef definition = {
    PyModuleDef_HEAD_INIT, "unitree_sdk2_cpp", "native loader fixture", -1, NULL
};
PyMODINIT_FUNC PyInit_unitree_sdk2_cpp(void) {
    PyObject *module = PyModule_Create(&definition);
    if (!module) return NULL;
    PyModule_AddStringConstant(module, "implementation", "native");
    PyObject *robot = PyModule_New("unitree_sdk2_cpp.robot");
    PyObject *go2 = PyModule_New("unitree_sdk2_cpp.robot.go2");
    PyModule_AddStringConstant(go2, "implementation", "native-go2");
    PyDict_SetItemString(PyImport_GetModuleDict(), "unitree_sdk2_cpp.robot", robot);
    PyDict_SetItemString(PyImport_GetModuleDict(), "unitree_sdk2_cpp.robot.go2", go2);
    PyModule_AddObject(robot, "go2", go2);
    PyModule_AddObject(module, "robot", robot);
    return module;
}
'''


def probe(paths, code):
    script = f"import sys; sys.path[:0] = {json.dumps([str(p) for p in paths])}\n{code}"
    return subprocess.run([sys.executable, "-I", "-c", script], capture_output=True, text=True)


def install_companions(site):
    shutil.copytree(SOURCES, site / "unitree_sdk2_cpp", ignore=shutil.ignore_patterns("__pycache__"))


def test_missing_native_has_explicit_error_not_fake_objects(tmp_path):
    install_companions(tmp_path)
    result = probe([tmp_path], "from unitree_sdk2_cpp.robot.go2 import SportClient")
    assert result.returncode != 0
    assert "supplies type hints, not the robot runtime" in result.stderr


@pytest.fixture
def native(tmp_path):
    compiler = shutil.which("cc")
    if not compiler or sys.platform not in {"linux", "darwin"}:
        pytest.skip("a C compiler on Linux/macOS is required")
    include = sysconfig.get_path("include")
    if not (Path(include) / "Python.h").exists():
        pytest.skip("Python development headers are required")
    binary_dir = tmp_path / "native site"
    binary_dir.mkdir()
    source = tmp_path / "fixture.c"
    source.write_text(NATIVE_SOURCE)
    binary = binary_dir / f"unitree_sdk2_cpp{sysconfig.get_config_var('EXT_SUFFIX')}"
    flags = ["-bundle", "-undefined", "dynamic_lookup"] if sys.platform == "darwin" else ["-shared", "-fPIC"]
    result = subprocess.run([compiler, *flags, f"-I{include}", str(source), "-o", str(binary)], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    return binary_dir, binary


@pytest.mark.parametrize("separate", [False, True])
def test_native_is_loaded_and_submodules_keep_their_identity(tmp_path, native, separate):
    native_site, binary = native
    source_site = tmp_path / "source site" if separate else native_site
    install_companions(source_site)
    result = probe([source_site, native_site], """
import importlib
import unitree_sdk2_cpp as u
from unitree_sdk2_cpp.robot import go2
from unitree_sdk2_cpp.robot.go2 import implementation
assert u.implementation == 'native'
assert implementation == 'native-go2'
assert go2 is u.robot.go2
assert importlib.import_module('unitree_sdk2_cpp') is u
print(u.__file__)
""")
    assert result.returncode == 0, result.stderr
    assert str(binary) in result.stdout


def test_real_linker_errors_are_not_hidden(tmp_path):
    install_companions(tmp_path)
    binary = tmp_path / f"unitree_sdk2_cpp{sysconfig.get_config_var('EXT_SUFFIX')}"
    binary.write_bytes(b"invalid test binary")
    result = probe([tmp_path], "import unitree_sdk2_cpp")
    assert result.returncode != 0
    assert str(binary) in result.stderr
    assert "supplies type hints" not in result.stderr
