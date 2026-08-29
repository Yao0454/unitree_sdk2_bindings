import pytest

unitree_sdk2_cpp = pytest.importorskip("unitree_sdk2_cpp")


def test_os_helper_safe_api() -> None:
    helper = unitree_sdk2_cpp.OsHelper.instance()
    assert helper.get_page_size() > 0
    assert helper.get_processor_number() > 0
    assert helper.get_hostname()
