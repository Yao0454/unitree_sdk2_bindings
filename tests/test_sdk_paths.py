"""Test SDK selection from an unrelated directory, without a C++ compiler."""

import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT / "generator"))
import sdk_paths

HEADERS = (
    "include/unitree/robot/channel/channel_factory.hpp",
    "include/unitree/robot/go2/sport/sport_client.hpp",
    "include/unitree/idl/go2/LowState_.hpp",
    "thirdparty/include/dds/dds.h",
    "thirdparty/include/ddscxx/dds/dds.hpp",
)


def make_sdk(path: Path, arch: str = "x86_64") -> Path:
    for name in (*HEADERS, f"lib/{arch}/libunitree_sdk2.a",
                 f"thirdparty/lib/{arch}/libddsc.so", f"thirdparty/lib/{arch}/libddscxx.so"):
        file = path / name
        file.parent.mkdir(parents=True, exist_ok=True)
        file.touch()
    return path


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    root = tmp_path / "separate checkout" / "bindings"
    (root / "cmake").mkdir(parents=True)
    shutil.copyfile(ROOT / "cmake/UnitreeSdk.cmake", root / "cmake/UnitreeSdk.cmake")
    monkeypatch.setattr(sdk_paths, "__file__", str(root / "generator/sdk_paths.py"))
    monkeypatch.delenv("UNITREE_SDK_ROOT", raising=False)
    cwd = tmp_path / "unrelated application"
    cwd.mkdir()
    return root, cwd


def configure(root, cwd, *definitions, arch="x86_64"):
    if shutil.which("cmake") is None:
        pytest.skip("cmake is required")
    return subprocess.run(
        ["cmake", f"-DUNITREE_ARCH={arch}", *definitions, "-P", str(root / "cmake/UnitreeSdk.cmake")],
        cwd=cwd, env=os.environ.copy(), capture_output=True, text=True,
    )


@pytest.mark.parametrize("arch", ["x86_64", "aarch64"])
def test_thirdparty_is_found_from_any_working_directory(isolated, arch):
    root, cwd = isolated
    sdk = make_sdk(root / "thirdparty/unitree_sdk2", arch)
    result = configure(root, cwd, arch=arch)
    assert result.returncode == 0, result.stderr
    assert str(sdk) in result.stdout
    assert sdk_paths.find_sdk_root() == sdk


def test_explicit_path_precedes_environment_and_thirdparty(isolated, monkeypatch):
    root, cwd = isolated
    make_sdk(root / "thirdparty/unitree_sdk2")
    env_sdk = make_sdk(cwd / "environment sdk")
    explicit = make_sdk(cwd / "explicit sdk")
    monkeypatch.setenv("UNITREE_SDK_ROOT", str(env_sdk))
    result = configure(root, cwd, f"-DUNITREE_SDK_ROOT={explicit}")
    assert result.returncode == 0, result.stderr
    assert str(explicit) in result.stdout
    assert sdk_paths.find_sdk_root(explicit) == explicit
    result = configure(root, cwd)
    assert result.returncode == 0, result.stderr
    assert str(env_sdk) in result.stdout
    assert sdk_paths.find_sdk_root() == env_sdk


def test_legacy_parent_layout_is_supported(isolated):
    root, cwd = isolated
    sdk = make_sdk(root.parent)
    result = configure(root, cwd)
    assert result.returncode == 0, result.stderr
    assert sdk_paths.find_sdk_root() == sdk


def test_missing_sdk_produces_actionable_error(isolated):
    root, cwd = isolated
    result = configure(root, cwd)
    assert result.returncode != 0
    assert "git clone" in result.stderr
    with pytest.raises(FileNotFoundError, match="thirdparty/unitree_sdk2"):
        sdk_paths.find_sdk_root()


def test_invalid_override_never_silently_falls_back(isolated, monkeypatch):
    root, cwd = isolated
    make_sdk(root / "thirdparty/unitree_sdk2")
    monkeypatch.setenv("UNITREE_SDK_ROOT", str(cwd / "missing"))
    result = configure(root, cwd)
    assert result.returncode != 0
    assert "Incomplete Unitree SDK2" in result.stderr
    with pytest.raises(FileNotFoundError):
        sdk_paths.find_sdk_root()


def test_missing_arch_library_is_reported(isolated):
    root, cwd = isolated
    make_sdk(root / "thirdparty/unitree_sdk2", "x86_64")
    result = configure(root, cwd, arch="aarch64")
    assert result.returncode != 0
    assert "lib/aarch64/libunitree_sdk2.a" in result.stderr


def test_relative_environment_path_is_relative_to_bindings(isolated, monkeypatch):
    root, cwd = isolated
    sdk = make_sdk(root / "another sdk")
    monkeypatch.setenv("UNITREE_SDK_ROOT", "another sdk")
    result = configure(root, cwd)
    assert result.returncode == 0, result.stderr
    assert str(sdk) in result.stdout
    assert sdk_paths.find_sdk_root() == sdk
