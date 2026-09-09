"""Generated DDS message bindings."""
from __future__ import annotations

from collections.abc import Sequence
from typing import Any

class doubleIMUState:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.hg_doubleimu import doubleIMUState
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `doubleIMUState` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = doubleIMUState()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: doubleIMUState_()
        """
        ...
    @property
    def quaternion(self) -> list[float]:
        """底层 `unitree_hg_doubleimu::msg::dds_::doubleIMUState_` 的 `quaternion` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            list[float]：字段当前值。

        Examples:
            value = obj.quaternion
            # 修改副本后必须回写
            obj.quaternion = value
        """
        ...
    @quaternion.setter
    def quaternion(self, value: Sequence[float]) -> None:
        """底层 `unitree_hg_doubleimu::msg::dds_::doubleIMUState_` 的 `quaternion` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.quaternion = value
        """
        ...
    @property
    def gyroscope(self) -> list[float]:
        """底层 `unitree_hg_doubleimu::msg::dds_::doubleIMUState_` 的 `gyroscope` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            list[float]：字段当前值。

        Examples:
            value = obj.gyroscope
            # 修改副本后必须回写
            obj.gyroscope = value
        """
        ...
    @gyroscope.setter
    def gyroscope(self, value: Sequence[float]) -> None:
        """底层 `unitree_hg_doubleimu::msg::dds_::doubleIMUState_` 的 `gyroscope` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.gyroscope = value
        """
        ...
    @property
    def accelerometer(self) -> list[float]:
        """底层 `unitree_hg_doubleimu::msg::dds_::doubleIMUState_` 的 `accelerometer` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            list[float]：字段当前值。

        Examples:
            value = obj.accelerometer
            # 修改副本后必须回写
            obj.accelerometer = value
        """
        ...
    @accelerometer.setter
    def accelerometer(self, value: Sequence[float]) -> None:
        """底层 `unitree_hg_doubleimu::msg::dds_::doubleIMUState_` 的 `accelerometer` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.accelerometer = value
        """
        ...
    @property
    def rpy(self) -> list[float]:
        """底层 `unitree_hg_doubleimu::msg::dds_::doubleIMUState_` 的 `rpy` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            list[float]：字段当前值。

        Examples:
            value = obj.rpy
            # 修改副本后必须回写
            obj.rpy = value
        """
        ...
    @rpy.setter
    def rpy(self, value: Sequence[float]) -> None:
        """底层 `unitree_hg_doubleimu::msg::dds_::doubleIMUState_` 的 `rpy` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.rpy = value
        """
        ...
    @property
    def temperature(self) -> int:
        """底层 `unitree_hg_doubleimu::msg::dds_::doubleIMUState_` 的 `temperature` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 -32768 到 32767。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.temperature
            # 修改副本后必须回写
            obj.temperature = value
        """
        ...
    @temperature.setter
    def temperature(self, value: int) -> None:
        """底层 `unitree_hg_doubleimu::msg::dds_::doubleIMUState_` 的 `temperature` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 -32768 到 32767。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.temperature = value
        """
        ...
    @property
    def tick(self) -> int:
        """底层 `unitree_hg_doubleimu::msg::dds_::doubleIMUState_` 的 `tick` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.tick
            # 修改副本后必须回写
            obj.tick = value
        """
        ...
    @tick.setter
    def tick(self, value: int) -> None:
        """底层 `unitree_hg_doubleimu::msg::dds_::doubleIMUState_` 的 `tick` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.tick = value
        """
        ...
    def __eq__(self, other: object) -> bool:
        """按底层 IDL 消息内容比较两个对象是否相等。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            other: 用于比较的另一个 Python 对象。类型不兼容时比较结果通常为 `False`。

        Returns:
            返回值 (bool): 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            same = left == right
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: operator==(const value &) const
        """
        ...
    def __ne__(self, other: object) -> bool:
        """按底层 IDL 消息内容比较两个对象是否不相等。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            other: 用于比较的另一个 Python 对象。类型不兼容时比较结果通常为 `False`。

        Returns:
            返回值 (bool): 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            different = left != right
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: operator!=(const value &) const
        """
        ...
