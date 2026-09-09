"""Generated DDS message bindings."""
from __future__ import annotations

from collections.abc import Sequence
from typing import Any

class Time:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.ros2 import Time
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `Time` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = Time()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Time_()
        """
        ...
    @property
    def sec(self) -> int:
        """底层 `builtin_interfaces::msg::dds_::Time_` 的 `sec` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 -2147483648 到 2147483647。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.sec
            # 修改副本后必须回写
            obj.sec = value
        """
        ...
    @sec.setter
    def sec(self, value: int) -> None:
        """底层 `builtin_interfaces::msg::dds_::Time_` 的 `sec` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 -2147483648 到 2147483647。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.sec = value
        """
        ...
    @property
    def nanosec(self) -> int:
        """底层 `builtin_interfaces::msg::dds_::Time_` 的 `nanosec` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.nanosec
            # 修改副本后必须回写
            obj.nanosec = value
        """
        ...
    @nanosec.setter
    def nanosec(self, value: int) -> None:
        """底层 `builtin_interfaces::msg::dds_::Time_` 的 `nanosec` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.nanosec = value
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

class Header:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.ros2 import Header
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `Header` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = Header()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Header_()
        """
        ...
    @property
    def stamp(self) -> Any:
        """底层 `std_msgs::msg::dds_::Header_` 的 `stamp` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            Any：字段当前值。

        Examples:
            value = obj.stamp
            # 修改副本后必须回写
            obj.stamp = value
        """
        ...
    @stamp.setter
    def stamp(self, value: Any) -> None:
        """底层 `std_msgs::msg::dds_::Header_` 的 `stamp` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.stamp = value
        """
        ...
    @property
    def frame_id(self) -> str:
        """底层 `std_msgs::msg::dds_::Header_` 的 `frame_id` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

        Returns:
            str：字段当前值。

        Examples:
            value = obj.frame_id
            # 修改副本后必须回写
            obj.frame_id = value
        """
        ...
    @frame_id.setter
    def frame_id(self, value: str) -> None:
        """底层 `std_msgs::msg::dds_::Header_` 的 `frame_id` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.frame_id = value
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

class Quaternion:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.ros2 import Quaternion
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `Quaternion` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = Quaternion()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Quaternion_()
        """
        ...
    @property
    def x(self) -> float:
        """底层 `geometry_msgs::msg::dds_::Quaternion_` 的 `x` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.x
            # 修改副本后必须回写
            obj.x = value
        """
        ...
    @x.setter
    def x(self, value: float) -> None:
        """底层 `geometry_msgs::msg::dds_::Quaternion_` 的 `x` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.x = value
        """
        ...
    @property
    def y(self) -> float:
        """底层 `geometry_msgs::msg::dds_::Quaternion_` 的 `y` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.y
            # 修改副本后必须回写
            obj.y = value
        """
        ...
    @y.setter
    def y(self, value: float) -> None:
        """底层 `geometry_msgs::msg::dds_::Quaternion_` 的 `y` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.y = value
        """
        ...
    @property
    def z(self) -> float:
        """底层 `geometry_msgs::msg::dds_::Quaternion_` 的 `z` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.z
            # 修改副本后必须回写
            obj.z = value
        """
        ...
    @z.setter
    def z(self, value: float) -> None:
        """底层 `geometry_msgs::msg::dds_::Quaternion_` 的 `z` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.z = value
        """
        ...
    @property
    def w(self) -> float:
        """底层 `geometry_msgs::msg::dds_::Quaternion_` 的 `w` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.w
            # 修改副本后必须回写
            obj.w = value
        """
        ...
    @w.setter
    def w(self, value: float) -> None:
        """底层 `geometry_msgs::msg::dds_::Quaternion_` 的 `w` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.w = value
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

class Vector3:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.ros2 import Vector3
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `Vector3` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = Vector3()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Vector3_()
        """
        ...
    @property
    def x(self) -> float:
        """底层 `geometry_msgs::msg::dds_::Vector3_` 的 `x` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.x
            # 修改副本后必须回写
            obj.x = value
        """
        ...
    @x.setter
    def x(self, value: float) -> None:
        """底层 `geometry_msgs::msg::dds_::Vector3_` 的 `x` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.x = value
        """
        ...
    @property
    def y(self) -> float:
        """底层 `geometry_msgs::msg::dds_::Vector3_` 的 `y` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.y
            # 修改副本后必须回写
            obj.y = value
        """
        ...
    @y.setter
    def y(self, value: float) -> None:
        """底层 `geometry_msgs::msg::dds_::Vector3_` 的 `y` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.y = value
        """
        ...
    @property
    def z(self) -> float:
        """底层 `geometry_msgs::msg::dds_::Vector3_` 的 `z` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.z
            # 修改副本后必须回写
            obj.z = value
        """
        ...
    @z.setter
    def z(self, value: float) -> None:
        """底层 `geometry_msgs::msg::dds_::Vector3_` 的 `z` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.z = value
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

class Imu:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.ros2 import Imu
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `Imu` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = Imu()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Imu_()
        """
        ...
    @property
    def header(self) -> Any:
        """底层 `sensor_msgs::msg::dds_::Imu_` 的 `header` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            Any：字段当前值。

        Examples:
            value = obj.header
            # 修改副本后必须回写
            obj.header = value
        """
        ...
    @header.setter
    def header(self, value: Any) -> None:
        """底层 `sensor_msgs::msg::dds_::Imu_` 的 `header` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.header = value
        """
        ...
    @property
    def orientation(self) -> Any:
        """底层 `sensor_msgs::msg::dds_::Imu_` 的 `orientation` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            Any：字段当前值。

        Examples:
            value = obj.orientation
            # 修改副本后必须回写
            obj.orientation = value
        """
        ...
    @orientation.setter
    def orientation(self, value: Any) -> None:
        """底层 `sensor_msgs::msg::dds_::Imu_` 的 `orientation` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.orientation = value
        """
        ...
    @property
    def orientation_covariance(self) -> list[float]:
        """底层 `sensor_msgs::msg::dds_::Imu_` 的 `orientation_covariance` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 9 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            list[float]：字段当前值。

        Examples:
            value = obj.orientation_covariance
            # 修改副本后必须回写
            obj.orientation_covariance = value
        """
        ...
    @orientation_covariance.setter
    def orientation_covariance(self, value: Sequence[float]) -> None:
        """底层 `sensor_msgs::msg::dds_::Imu_` 的 `orientation_covariance` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 9 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.orientation_covariance = value
        """
        ...
    @property
    def angular_velocity(self) -> Any:
        """底层 `sensor_msgs::msg::dds_::Imu_` 的 `angular_velocity` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            Any：字段当前值。

        Examples:
            value = obj.angular_velocity
            # 修改副本后必须回写
            obj.angular_velocity = value
        """
        ...
    @angular_velocity.setter
    def angular_velocity(self, value: Any) -> None:
        """底层 `sensor_msgs::msg::dds_::Imu_` 的 `angular_velocity` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.angular_velocity = value
        """
        ...
    @property
    def angular_velocity_covariance(self) -> list[float]:
        """底层 `sensor_msgs::msg::dds_::Imu_` 的 `angular_velocity_covariance` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 9 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            list[float]：字段当前值。

        Examples:
            value = obj.angular_velocity_covariance
            # 修改副本后必须回写
            obj.angular_velocity_covariance = value
        """
        ...
    @angular_velocity_covariance.setter
    def angular_velocity_covariance(self, value: Sequence[float]) -> None:
        """底层 `sensor_msgs::msg::dds_::Imu_` 的 `angular_velocity_covariance` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 9 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.angular_velocity_covariance = value
        """
        ...
    @property
    def linear_acceleration(self) -> Any:
        """底层 `sensor_msgs::msg::dds_::Imu_` 的 `linear_acceleration` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            Any：字段当前值。

        Examples:
            value = obj.linear_acceleration
            # 修改副本后必须回写
            obj.linear_acceleration = value
        """
        ...
    @linear_acceleration.setter
    def linear_acceleration(self, value: Any) -> None:
        """底层 `sensor_msgs::msg::dds_::Imu_` 的 `linear_acceleration` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.linear_acceleration = value
        """
        ...
    @property
    def linear_acceleration_covariance(self) -> list[float]:
        """底层 `sensor_msgs::msg::dds_::Imu_` 的 `linear_acceleration_covariance` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 9 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            list[float]：字段当前值。

        Examples:
            value = obj.linear_acceleration_covariance
            # 修改副本后必须回写
            obj.linear_acceleration_covariance = value
        """
        ...
    @linear_acceleration_covariance.setter
    def linear_acceleration_covariance(self, value: Sequence[float]) -> None:
        """底层 `sensor_msgs::msg::dds_::Imu_` 的 `linear_acceleration_covariance` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 9 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.linear_acceleration_covariance = value
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

class Point:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.ros2 import Point
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `Point` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = Point()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Point_()
        """
        ...
    @property
    def x(self) -> float:
        """底层 `geometry_msgs::msg::dds_::Point_` 的 `x` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.x
            # 修改副本后必须回写
            obj.x = value
        """
        ...
    @x.setter
    def x(self, value: float) -> None:
        """底层 `geometry_msgs::msg::dds_::Point_` 的 `x` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.x = value
        """
        ...
    @property
    def y(self) -> float:
        """底层 `geometry_msgs::msg::dds_::Point_` 的 `y` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.y
            # 修改副本后必须回写
            obj.y = value
        """
        ...
    @y.setter
    def y(self, value: float) -> None:
        """底层 `geometry_msgs::msg::dds_::Point_` 的 `y` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.y = value
        """
        ...
    @property
    def z(self) -> float:
        """底层 `geometry_msgs::msg::dds_::Point_` 的 `z` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.z
            # 修改副本后必须回写
            obj.z = value
        """
        ...
    @z.setter
    def z(self, value: float) -> None:
        """底层 `geometry_msgs::msg::dds_::Point_` 的 `z` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.z = value
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

class Pose:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.ros2 import Pose
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `Pose` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = Pose()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Pose_()
        """
        ...
    @property
    def position(self) -> Point:
        """底层 `geometry_msgs::msg::dds_::Pose_` 的 `position` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            Point：字段当前值。

        Examples:
            value = obj.position
            # 修改副本后必须回写
            obj.position = value
        """
        ...
    @position.setter
    def position(self, value: Point) -> None:
        """底层 `geometry_msgs::msg::dds_::Pose_` 的 `position` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.position = value
        """
        ...
    @property
    def orientation(self) -> Quaternion:
        """底层 `geometry_msgs::msg::dds_::Pose_` 的 `orientation` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            Quaternion：字段当前值。

        Examples:
            value = obj.orientation
            # 修改副本后必须回写
            obj.orientation = value
        """
        ...
    @orientation.setter
    def orientation(self, value: Quaternion) -> None:
        """底层 `geometry_msgs::msg::dds_::Pose_` 的 `orientation` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.orientation = value
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

class MapMetaData:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.ros2 import MapMetaData
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `MapMetaData` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = MapMetaData()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: MapMetaData_()
        """
        ...
    @property
    def map_load_time(self) -> Any:
        """底层 `nav_msgs::msg::dds_::MapMetaData_` 的 `map_load_time` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            Any：字段当前值。

        Examples:
            value = obj.map_load_time
            # 修改副本后必须回写
            obj.map_load_time = value
        """
        ...
    @map_load_time.setter
    def map_load_time(self, value: Any) -> None:
        """底层 `nav_msgs::msg::dds_::MapMetaData_` 的 `map_load_time` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.map_load_time = value
        """
        ...
    @property
    def resolution(self) -> float:
        """底层 `nav_msgs::msg::dds_::MapMetaData_` 的 `resolution` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.resolution
            # 修改副本后必须回写
            obj.resolution = value
        """
        ...
    @resolution.setter
    def resolution(self, value: float) -> None:
        """底层 `nav_msgs::msg::dds_::MapMetaData_` 的 `resolution` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.resolution = value
        """
        ...
    @property
    def width(self) -> int:
        """底层 `nav_msgs::msg::dds_::MapMetaData_` 的 `width` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.width
            # 修改副本后必须回写
            obj.width = value
        """
        ...
    @width.setter
    def width(self, value: int) -> None:
        """底层 `nav_msgs::msg::dds_::MapMetaData_` 的 `width` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.width = value
        """
        ...
    @property
    def height(self) -> int:
        """底层 `nav_msgs::msg::dds_::MapMetaData_` 的 `height` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.height
            # 修改副本后必须回写
            obj.height = value
        """
        ...
    @height.setter
    def height(self, value: int) -> None:
        """底层 `nav_msgs::msg::dds_::MapMetaData_` 的 `height` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.height = value
        """
        ...
    @property
    def origin(self) -> Any:
        """底层 `nav_msgs::msg::dds_::MapMetaData_` 的 `origin` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            Any：字段当前值。

        Examples:
            value = obj.origin
            # 修改副本后必须回写
            obj.origin = value
        """
        ...
    @origin.setter
    def origin(self, value: Any) -> None:
        """底层 `nav_msgs::msg::dds_::MapMetaData_` 的 `origin` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.origin = value
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

class OccupancyGrid:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.ros2 import OccupancyGrid
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `OccupancyGrid` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = OccupancyGrid()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: OccupancyGrid_()
        """
        ...
    @property
    def header(self) -> Any:
        """底层 `nav_msgs::msg::dds_::OccupancyGrid_` 的 `header` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            Any：字段当前值。

        Examples:
            value = obj.header
            # 修改副本后必须回写
            obj.header = value
        """
        ...
    @header.setter
    def header(self, value: Any) -> None:
        """底层 `nav_msgs::msg::dds_::OccupancyGrid_` 的 `header` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.header = value
        """
        ...
    @property
    def info(self) -> MapMetaData:
        """底层 `nav_msgs::msg::dds_::OccupancyGrid_` 的 `info` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            MapMetaData：字段当前值。

        Examples:
            value = obj.info
            # 修改副本后必须回写
            obj.info = value
        """
        ...
    @info.setter
    def info(self, value: MapMetaData) -> None:
        """底层 `nav_msgs::msg::dds_::OccupancyGrid_` 的 `info` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.info = value
        """
        ...
    @property
    def data(self) -> list[int]:
        """底层 `nav_msgs::msg::dds_::OccupancyGrid_` 的 `data` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector；元素约束：取值范围为 0 到 255。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.data
            # 修改副本后必须回写
            obj.data = value
        """
        ...
    @data.setter
    def data(self, value: Sequence[int]) -> None:
        """底层 `nav_msgs::msg::dds_::OccupancyGrid_` 的 `data` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector；元素约束：取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.data = value
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

class PoseWithCovariance:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.ros2 import PoseWithCovariance
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `PoseWithCovariance` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = PoseWithCovariance()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: PoseWithCovariance_()
        """
        ...
    @property
    def pose(self) -> Pose:
        """底层 `geometry_msgs::msg::dds_::PoseWithCovariance_` 的 `pose` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            Pose：字段当前值。

        Examples:
            value = obj.pose
            # 修改副本后必须回写
            obj.pose = value
        """
        ...
    @pose.setter
    def pose(self, value: Pose) -> None:
        """底层 `geometry_msgs::msg::dds_::PoseWithCovariance_` 的 `pose` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.pose = value
        """
        ...
    @property
    def covariance(self) -> list[float]:
        """底层 `geometry_msgs::msg::dds_::PoseWithCovariance_` 的 `covariance` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 36 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            list[float]：字段当前值。

        Examples:
            value = obj.covariance
            # 修改副本后必须回写
            obj.covariance = value
        """
        ...
    @covariance.setter
    def covariance(self, value: Sequence[float]) -> None:
        """底层 `geometry_msgs::msg::dds_::PoseWithCovariance_` 的 `covariance` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 36 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.covariance = value
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

class Twist:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.ros2 import Twist
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `Twist` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = Twist()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Twist_()
        """
        ...
    @property
    def linear(self) -> Vector3:
        """底层 `geometry_msgs::msg::dds_::Twist_` 的 `linear` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            Vector3：字段当前值。

        Examples:
            value = obj.linear
            # 修改副本后必须回写
            obj.linear = value
        """
        ...
    @linear.setter
    def linear(self, value: Vector3) -> None:
        """底层 `geometry_msgs::msg::dds_::Twist_` 的 `linear` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.linear = value
        """
        ...
    @property
    def angular(self) -> Vector3:
        """底层 `geometry_msgs::msg::dds_::Twist_` 的 `angular` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            Vector3：字段当前值。

        Examples:
            value = obj.angular
            # 修改副本后必须回写
            obj.angular = value
        """
        ...
    @angular.setter
    def angular(self, value: Vector3) -> None:
        """底层 `geometry_msgs::msg::dds_::Twist_` 的 `angular` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.angular = value
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

class TwistWithCovariance:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.ros2 import TwistWithCovariance
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `TwistWithCovariance` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = TwistWithCovariance()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: TwistWithCovariance_()
        """
        ...
    @property
    def twist(self) -> Twist:
        """底层 `geometry_msgs::msg::dds_::TwistWithCovariance_` 的 `twist` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            Twist：字段当前值。

        Examples:
            value = obj.twist
            # 修改副本后必须回写
            obj.twist = value
        """
        ...
    @twist.setter
    def twist(self, value: Twist) -> None:
        """底层 `geometry_msgs::msg::dds_::TwistWithCovariance_` 的 `twist` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.twist = value
        """
        ...
    @property
    def covariance(self) -> list[float]:
        """底层 `geometry_msgs::msg::dds_::TwistWithCovariance_` 的 `covariance` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 36 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            list[float]：字段当前值。

        Examples:
            value = obj.covariance
            # 修改副本后必须回写
            obj.covariance = value
        """
        ...
    @covariance.setter
    def covariance(self, value: Sequence[float]) -> None:
        """底层 `geometry_msgs::msg::dds_::TwistWithCovariance_` 的 `covariance` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 36 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.covariance = value
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

class Odometry:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.ros2 import Odometry
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `Odometry` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = Odometry()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Odometry_()
        """
        ...
    @property
    def header(self) -> Any:
        """底层 `nav_msgs::msg::dds_::Odometry_` 的 `header` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            Any：字段当前值。

        Examples:
            value = obj.header
            # 修改副本后必须回写
            obj.header = value
        """
        ...
    @header.setter
    def header(self, value: Any) -> None:
        """底层 `nav_msgs::msg::dds_::Odometry_` 的 `header` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.header = value
        """
        ...
    @property
    def child_frame_id(self) -> str:
        """底层 `nav_msgs::msg::dds_::Odometry_` 的 `child_frame_id` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

        Returns:
            str：字段当前值。

        Examples:
            value = obj.child_frame_id
            # 修改副本后必须回写
            obj.child_frame_id = value
        """
        ...
    @child_frame_id.setter
    def child_frame_id(self, value: str) -> None:
        """底层 `nav_msgs::msg::dds_::Odometry_` 的 `child_frame_id` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.child_frame_id = value
        """
        ...
    @property
    def pose(self) -> Any:
        """底层 `nav_msgs::msg::dds_::Odometry_` 的 `pose` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            Any：字段当前值。

        Examples:
            value = obj.pose
            # 修改副本后必须回写
            obj.pose = value
        """
        ...
    @pose.setter
    def pose(self, value: Any) -> None:
        """底层 `nav_msgs::msg::dds_::Odometry_` 的 `pose` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.pose = value
        """
        ...
    @property
    def twist(self) -> Any:
        """底层 `nav_msgs::msg::dds_::Odometry_` 的 `twist` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            Any：字段当前值。

        Examples:
            value = obj.twist
            # 修改副本后必须回写
            obj.twist = value
        """
        ...
    @twist.setter
    def twist(self, value: Any) -> None:
        """底层 `nav_msgs::msg::dds_::Odometry_` 的 `twist` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.twist = value
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

class Point32:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.ros2 import Point32
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `Point32` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = Point32()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Point32_()
        """
        ...
    @property
    def x(self) -> float:
        """底层 `geometry_msgs::msg::dds_::Point32_` 的 `x` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.x
            # 修改副本后必须回写
            obj.x = value
        """
        ...
    @x.setter
    def x(self, value: float) -> None:
        """底层 `geometry_msgs::msg::dds_::Point32_` 的 `x` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.x = value
        """
        ...
    @property
    def y(self) -> float:
        """底层 `geometry_msgs::msg::dds_::Point32_` 的 `y` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.y
            # 修改副本后必须回写
            obj.y = value
        """
        ...
    @y.setter
    def y(self, value: float) -> None:
        """底层 `geometry_msgs::msg::dds_::Point32_` 的 `y` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.y = value
        """
        ...
    @property
    def z(self) -> float:
        """底层 `geometry_msgs::msg::dds_::Point32_` 的 `z` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.z
            # 修改副本后必须回写
            obj.z = value
        """
        ...
    @z.setter
    def z(self, value: float) -> None:
        """底层 `geometry_msgs::msg::dds_::Point32_` 的 `z` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.z = value
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

class PointField:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.ros2 import PointField
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `PointField` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = PointField()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: PointField_()
        """
        ...
    @property
    def name(self) -> str:
        """底层 `sensor_msgs::msg::dds_::PointField_` 的 `name` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

        Returns:
            str：字段当前值。

        Examples:
            value = obj.name
            # 修改副本后必须回写
            obj.name = value
        """
        ...
    @name.setter
    def name(self, value: str) -> None:
        """底层 `sensor_msgs::msg::dds_::PointField_` 的 `name` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.name = value
        """
        ...
    @property
    def offset(self) -> int:
        """底层 `sensor_msgs::msg::dds_::PointField_` 的 `offset` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.offset
            # 修改副本后必须回写
            obj.offset = value
        """
        ...
    @offset.setter
    def offset(self, value: int) -> None:
        """底层 `sensor_msgs::msg::dds_::PointField_` 的 `offset` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.offset = value
        """
        ...
    @property
    def datatype(self) -> int:
        """底层 `sensor_msgs::msg::dds_::PointField_` 的 `datatype` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.datatype
            # 修改副本后必须回写
            obj.datatype = value
        """
        ...
    @datatype.setter
    def datatype(self, value: int) -> None:
        """底层 `sensor_msgs::msg::dds_::PointField_` 的 `datatype` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.datatype = value
        """
        ...
    @property
    def count(self) -> int:
        """底层 `sensor_msgs::msg::dds_::PointField_` 的 `count` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.count
            # 修改副本后必须回写
            obj.count = value
        """
        ...
    @count.setter
    def count(self, value: int) -> None:
        """底层 `sensor_msgs::msg::dds_::PointField_` 的 `count` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.count = value
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

class PointCloud2:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.ros2 import PointCloud2
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `PointCloud2` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = PointCloud2()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: PointCloud2_()
        """
        ...
    @property
    def header(self) -> Any:
        """底层 `sensor_msgs::msg::dds_::PointCloud2_` 的 `header` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            Any：字段当前值。

        Examples:
            value = obj.header
            # 修改副本后必须回写
            obj.header = value
        """
        ...
    @header.setter
    def header(self, value: Any) -> None:
        """底层 `sensor_msgs::msg::dds_::PointCloud2_` 的 `header` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.header = value
        """
        ...
    @property
    def height(self) -> int:
        """底层 `sensor_msgs::msg::dds_::PointCloud2_` 的 `height` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.height
            # 修改副本后必须回写
            obj.height = value
        """
        ...
    @height.setter
    def height(self, value: int) -> None:
        """底层 `sensor_msgs::msg::dds_::PointCloud2_` 的 `height` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.height = value
        """
        ...
    @property
    def width(self) -> int:
        """底层 `sensor_msgs::msg::dds_::PointCloud2_` 的 `width` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.width
            # 修改副本后必须回写
            obj.width = value
        """
        ...
    @width.setter
    def width(self, value: int) -> None:
        """底层 `sensor_msgs::msg::dds_::PointCloud2_` 的 `width` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.width = value
        """
        ...
    @property
    def fields(self) -> list[PointField]:
        """底层 `sensor_msgs::msg::dds_::PointCloud2_` 的 `fields` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector

        Returns:
            list[PointField]：字段当前值。

        Examples:
            value = obj.fields
            # 修改副本后必须回写
            obj.fields = value
        """
        ...
    @fields.setter
    def fields(self, value: Sequence[PointField]) -> None:
        """底层 `sensor_msgs::msg::dds_::PointCloud2_` 的 `fields` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.fields = value
        """
        ...
    @property
    def is_bigendian(self) -> bool:
        """底层 `sensor_msgs::msg::dds_::PointCloud2_` 的 `is_bigendian` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 只接受布尔语义。

        Returns:
            bool：字段当前值。

        Examples:
            value = obj.is_bigendian
            # 修改副本后必须回写
            obj.is_bigendian = value
        """
        ...
    @is_bigendian.setter
    def is_bigendian(self, value: bool) -> None:
        """底层 `sensor_msgs::msg::dds_::PointCloud2_` 的 `is_bigendian` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 只接受布尔语义。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.is_bigendian = value
        """
        ...
    @property
    def point_step(self) -> int:
        """底层 `sensor_msgs::msg::dds_::PointCloud2_` 的 `point_step` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.point_step
            # 修改副本后必须回写
            obj.point_step = value
        """
        ...
    @point_step.setter
    def point_step(self, value: int) -> None:
        """底层 `sensor_msgs::msg::dds_::PointCloud2_` 的 `point_step` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.point_step = value
        """
        ...
    @property
    def row_step(self) -> int:
        """底层 `sensor_msgs::msg::dds_::PointCloud2_` 的 `row_step` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.row_step
            # 修改副本后必须回写
            obj.row_step = value
        """
        ...
    @row_step.setter
    def row_step(self, value: int) -> None:
        """底层 `sensor_msgs::msg::dds_::PointCloud2_` 的 `row_step` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.row_step = value
        """
        ...
    @property
    def data(self) -> list[int]:
        """底层 `sensor_msgs::msg::dds_::PointCloud2_` 的 `data` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector；元素约束：取值范围为 0 到 255。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.data
            # 修改副本后必须回写
            obj.data = value
        """
        ...
    @data.setter
    def data(self, value: Sequence[int]) -> None:
        """底层 `sensor_msgs::msg::dds_::PointCloud2_` 的 `data` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector；元素约束：取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.data = value
        """
        ...
    @property
    def is_dense(self) -> bool:
        """底层 `sensor_msgs::msg::dds_::PointCloud2_` 的 `is_dense` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 只接受布尔语义。

        Returns:
            bool：字段当前值。

        Examples:
            value = obj.is_dense
            # 修改副本后必须回写
            obj.is_dense = value
        """
        ...
    @is_dense.setter
    def is_dense(self, value: bool) -> None:
        """底层 `sensor_msgs::msg::dds_::PointCloud2_` 的 `is_dense` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 只接受布尔语义。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.is_dense = value
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

class PointStamped:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.ros2 import PointStamped
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `PointStamped` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = PointStamped()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: PointStamped_()
        """
        ...
    @property
    def header(self) -> Any:
        """底层 `geometry_msgs::msg::dds_::PointStamped_` 的 `header` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            Any：字段当前值。

        Examples:
            value = obj.header
            # 修改副本后必须回写
            obj.header = value
        """
        ...
    @header.setter
    def header(self, value: Any) -> None:
        """底层 `geometry_msgs::msg::dds_::PointStamped_` 的 `header` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.header = value
        """
        ...
    @property
    def point(self) -> Point:
        """底层 `geometry_msgs::msg::dds_::PointStamped_` 的 `point` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            Point：字段当前值。

        Examples:
            value = obj.point
            # 修改副本后必须回写
            obj.point = value
        """
        ...
    @point.setter
    def point(self, value: Point) -> None:
        """底层 `geometry_msgs::msg::dds_::PointStamped_` 的 `point` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.point = value
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

class Pose2D:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.ros2 import Pose2D
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `Pose2D` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = Pose2D()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Pose2D_()
        """
        ...
    @property
    def x(self) -> float:
        """底层 `geometry_msgs::msg::dds_::Pose2D_` 的 `x` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.x
            # 修改副本后必须回写
            obj.x = value
        """
        ...
    @x.setter
    def x(self, value: float) -> None:
        """底层 `geometry_msgs::msg::dds_::Pose2D_` 的 `x` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.x = value
        """
        ...
    @property
    def y(self) -> float:
        """底层 `geometry_msgs::msg::dds_::Pose2D_` 的 `y` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.y
            # 修改副本后必须回写
            obj.y = value
        """
        ...
    @y.setter
    def y(self, value: float) -> None:
        """底层 `geometry_msgs::msg::dds_::Pose2D_` 的 `y` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.y = value
        """
        ...
    @property
    def theta(self) -> float:
        """底层 `geometry_msgs::msg::dds_::Pose2D_` 的 `theta` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.theta
            # 修改副本后必须回写
            obj.theta = value
        """
        ...
    @theta.setter
    def theta(self, value: float) -> None:
        """底层 `geometry_msgs::msg::dds_::Pose2D_` 的 `theta` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.theta = value
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

class PoseStamped:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.ros2 import PoseStamped
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `PoseStamped` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = PoseStamped()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: PoseStamped_()
        """
        ...
    @property
    def header(self) -> Any:
        """底层 `geometry_msgs::msg::dds_::PoseStamped_` 的 `header` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            Any：字段当前值。

        Examples:
            value = obj.header
            # 修改副本后必须回写
            obj.header = value
        """
        ...
    @header.setter
    def header(self, value: Any) -> None:
        """底层 `geometry_msgs::msg::dds_::PoseStamped_` 的 `header` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.header = value
        """
        ...
    @property
    def pose(self) -> Pose:
        """底层 `geometry_msgs::msg::dds_::PoseStamped_` 的 `pose` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            Pose：字段当前值。

        Examples:
            value = obj.pose
            # 修改副本后必须回写
            obj.pose = value
        """
        ...
    @pose.setter
    def pose(self, value: Pose) -> None:
        """底层 `geometry_msgs::msg::dds_::PoseStamped_` 的 `pose` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.pose = value
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

class PoseWithCovarianceStamped:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.ros2 import PoseWithCovarianceStamped
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `PoseWithCovarianceStamped` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = PoseWithCovarianceStamped()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: PoseWithCovarianceStamped_()
        """
        ...
    @property
    def header(self) -> Any:
        """底层 `geometry_msgs::msg::dds_::PoseWithCovarianceStamped_` 的 `header` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            Any：字段当前值。

        Examples:
            value = obj.header
            # 修改副本后必须回写
            obj.header = value
        """
        ...
    @header.setter
    def header(self, value: Any) -> None:
        """底层 `geometry_msgs::msg::dds_::PoseWithCovarianceStamped_` 的 `header` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.header = value
        """
        ...
    @property
    def pose(self) -> PoseWithCovariance:
        """底层 `geometry_msgs::msg::dds_::PoseWithCovarianceStamped_` 的 `pose` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            PoseWithCovariance：字段当前值。

        Examples:
            value = obj.pose
            # 修改副本后必须回写
            obj.pose = value
        """
        ...
    @pose.setter
    def pose(self, value: PoseWithCovariance) -> None:
        """底层 `geometry_msgs::msg::dds_::PoseWithCovarianceStamped_` 的 `pose` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.pose = value
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

class QuaternionStamped:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.ros2 import QuaternionStamped
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `QuaternionStamped` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = QuaternionStamped()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: QuaternionStamped_()
        """
        ...
    @property
    def header(self) -> Any:
        """底层 `geometry_msgs::msg::dds_::QuaternionStamped_` 的 `header` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            Any：字段当前值。

        Examples:
            value = obj.header
            # 修改副本后必须回写
            obj.header = value
        """
        ...
    @header.setter
    def header(self, value: Any) -> None:
        """底层 `geometry_msgs::msg::dds_::QuaternionStamped_` 的 `header` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.header = value
        """
        ...
    @property
    def quaternion(self) -> Quaternion:
        """底层 `geometry_msgs::msg::dds_::QuaternionStamped_` 的 `quaternion` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            Quaternion：字段当前值。

        Examples:
            value = obj.quaternion
            # 修改副本后必须回写
            obj.quaternion = value
        """
        ...
    @quaternion.setter
    def quaternion(self, value: Quaternion) -> None:
        """底层 `geometry_msgs::msg::dds_::QuaternionStamped_` 的 `quaternion` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.quaternion = value
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

class String:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.ros2 import String
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `String` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = String()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: String_()
        """
        ...
    @property
    def data(self) -> str:
        """底层 `std_msgs::msg::dds_::String_` 的 `data` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

        Returns:
            str：字段当前值。

        Examples:
            value = obj.data
            # 修改副本后必须回写
            obj.data = value
        """
        ...
    @data.setter
    def data(self, value: str) -> None:
        """底层 `std_msgs::msg::dds_::String_` 的 `data` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.data = value
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

class TwistStamped:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.ros2 import TwistStamped
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `TwistStamped` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = TwistStamped()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: TwistStamped_()
        """
        ...
    @property
    def header(self) -> Any:
        """底层 `geometry_msgs::msg::dds_::TwistStamped_` 的 `header` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            Any：字段当前值。

        Examples:
            value = obj.header
            # 修改副本后必须回写
            obj.header = value
        """
        ...
    @header.setter
    def header(self, value: Any) -> None:
        """底层 `geometry_msgs::msg::dds_::TwistStamped_` 的 `header` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.header = value
        """
        ...
    @property
    def twist(self) -> Twist:
        """底层 `geometry_msgs::msg::dds_::TwistStamped_` 的 `twist` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            Twist：字段当前值。

        Examples:
            value = obj.twist
            # 修改副本后必须回写
            obj.twist = value
        """
        ...
    @twist.setter
    def twist(self, value: Twist) -> None:
        """底层 `geometry_msgs::msg::dds_::TwistStamped_` 的 `twist` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.twist = value
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

class TwistWithCovarianceStamped:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.ros2 import TwistWithCovarianceStamped
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `TwistWithCovarianceStamped` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = TwistWithCovarianceStamped()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: TwistWithCovarianceStamped_()
        """
        ...
    @property
    def header(self) -> Any:
        """底层 `geometry_msgs::msg::dds_::TwistWithCovarianceStamped_` 的 `header` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            Any：字段当前值。

        Examples:
            value = obj.header
            # 修改副本后必须回写
            obj.header = value
        """
        ...
    @header.setter
    def header(self, value: Any) -> None:
        """底层 `geometry_msgs::msg::dds_::TwistWithCovarianceStamped_` 的 `header` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.header = value
        """
        ...
    @property
    def twist(self) -> TwistWithCovariance:
        """底层 `geometry_msgs::msg::dds_::TwistWithCovarianceStamped_` 的 `twist` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            TwistWithCovariance：字段当前值。

        Examples:
            value = obj.twist
            # 修改副本后必须回写
            obj.twist = value
        """
        ...
    @twist.setter
    def twist(self, value: TwistWithCovariance) -> None:
        """底层 `geometry_msgs::msg::dds_::TwistWithCovarianceStamped_` 的 `twist` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.twist = value
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
