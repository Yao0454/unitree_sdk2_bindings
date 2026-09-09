"""Generated DDS message bindings."""
from __future__ import annotations

from collections.abc import Sequence
from typing import Any

class AgvBmsState:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.hg import AgvBmsState
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `AgvBmsState` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = AgvBmsState()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: AgvBmsState_()
        """
        ...
    @property
    def software_version(self) -> str:
        """底层 `unitree_hg::msg::dds_::AgvBmsState_` 的 `software_version` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

        Returns:
            str：字段当前值。

        Examples:
            value = obj.software_version
            # 修改副本后必须回写
            obj.software_version = value
        """
        ...
    @software_version.setter
    def software_version(self, value: str) -> None:
        """底层 `unitree_hg::msg::dds_::AgvBmsState_` 的 `software_version` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.software_version = value
        """
        ...
    @property
    def battery_percentage(self) -> int:
        """底层 `unitree_hg::msg::dds_::AgvBmsState_` 的 `battery_percentage` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.battery_percentage
            # 修改副本后必须回写
            obj.battery_percentage = value
        """
        ...
    @battery_percentage.setter
    def battery_percentage(self, value: int) -> None:
        """底层 `unitree_hg::msg::dds_::AgvBmsState_` 的 `battery_percentage` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.battery_percentage = value
        """
        ...
    @property
    def current(self) -> int:
        """底层 `unitree_hg::msg::dds_::AgvBmsState_` 的 `current` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 -2147483648 到 2147483647。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.current
            # 修改副本后必须回写
            obj.current = value
        """
        ...
    @current.setter
    def current(self, value: int) -> None:
        """底层 `unitree_hg::msg::dds_::AgvBmsState_` 的 `current` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 -2147483648 到 2147483647。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.current = value
        """
        ...
    @property
    def temperature(self) -> list[int]:
        """底层 `unitree_hg::msg::dds_::AgvBmsState_` 的 `temperature` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：取值范围为 -32768 到 32767。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.temperature
            # 修改副本后必须回写
            obj.temperature = value
        """
        ...
    @temperature.setter
    def temperature(self, value: Sequence[int]) -> None:
        """底层 `unitree_hg::msg::dds_::AgvBmsState_` 的 `temperature` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：取值范围为 -32768 到 32767。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.temperature = value
        """
        ...
    @property
    def docking_status(self) -> str:
        """底层 `unitree_hg::msg::dds_::AgvBmsState_` 的 `docking_status` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

        Returns:
            str：字段当前值。

        Examples:
            value = obj.docking_status
            # 修改副本后必须回写
            obj.docking_status = value
        """
        ...
    @docking_status.setter
    def docking_status(self, value: str) -> None:
        """底层 `unitree_hg::msg::dds_::AgvBmsState_` 的 `docking_status` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.docking_status = value
        """
        ...
    @property
    def is_charging(self) -> bool:
        """底层 `unitree_hg::msg::dds_::AgvBmsState_` 的 `is_charging` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 只接受布尔语义。

        Returns:
            bool：字段当前值。

        Examples:
            value = obj.is_charging
            # 修改副本后必须回写
            obj.is_charging = value
        """
        ...
    @is_charging.setter
    def is_charging(self, value: bool) -> None:
        """底层 `unitree_hg::msg::dds_::AgvBmsState_` 的 `is_charging` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 只接受布尔语义。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.is_charging = value
        """
        ...
    @property
    def is_dc_connected(self) -> bool:
        """底层 `unitree_hg::msg::dds_::AgvBmsState_` 的 `is_dc_connected` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 只接受布尔语义。

        Returns:
            bool：字段当前值。

        Examples:
            value = obj.is_dc_connected
            # 修改副本后必须回写
            obj.is_dc_connected = value
        """
        ...
    @is_dc_connected.setter
    def is_dc_connected(self, value: bool) -> None:
        """底层 `unitree_hg::msg::dds_::AgvBmsState_` 的 `is_dc_connected` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 只接受布尔语义。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.is_dc_connected = value
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

class BmsCmd:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.hg import BmsCmd
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `BmsCmd` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = BmsCmd()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: BmsCmd_()
        """
        ...
    @property
    def cmd(self) -> int:
        """底层 `unitree_hg::msg::dds_::BmsCmd_` 的 `cmd` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.cmd
            # 修改副本后必须回写
            obj.cmd = value
        """
        ...
    @cmd.setter
    def cmd(self, value: int) -> None:
        """底层 `unitree_hg::msg::dds_::BmsCmd_` 的 `cmd` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.cmd = value
        """
        ...
    @property
    def reserve(self) -> list[int]:
        """底层 `unitree_hg::msg::dds_::BmsCmd_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 40 个元素；元素约束：取值范围为 0 到 255。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.reserve
            # 修改副本后必须回写
            obj.reserve = value
        """
        ...
    @reserve.setter
    def reserve(self, value: Sequence[int]) -> None:
        """底层 `unitree_hg::msg::dds_::BmsCmd_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 40 个元素；元素约束：取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.reserve = value
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

class BmsState:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.hg import BmsState
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `BmsState` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = BmsState()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: BmsState_()
        """
        ...
    @property
    def version_high(self) -> int:
        """底层 `unitree_hg::msg::dds_::BmsState_` 的 `version_high` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.version_high
            # 修改副本后必须回写
            obj.version_high = value
        """
        ...
    @version_high.setter
    def version_high(self, value: int) -> None:
        """底层 `unitree_hg::msg::dds_::BmsState_` 的 `version_high` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.version_high = value
        """
        ...
    @property
    def version_low(self) -> int:
        """底层 `unitree_hg::msg::dds_::BmsState_` 的 `version_low` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.version_low
            # 修改副本后必须回写
            obj.version_low = value
        """
        ...
    @version_low.setter
    def version_low(self, value: int) -> None:
        """底层 `unitree_hg::msg::dds_::BmsState_` 的 `version_low` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.version_low = value
        """
        ...
    @property
    def fn(self) -> int:
        """底层 `unitree_hg::msg::dds_::BmsState_` 的 `fn` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.fn
            # 修改副本后必须回写
            obj.fn = value
        """
        ...
    @fn.setter
    def fn(self, value: int) -> None:
        """底层 `unitree_hg::msg::dds_::BmsState_` 的 `fn` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.fn = value
        """
        ...
    @property
    def cell_vol(self) -> list[int]:
        """底层 `unitree_hg::msg::dds_::BmsState_` 的 `cell_vol` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 40 个元素；元素约束：取值范围为 0 到 65535。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.cell_vol
            # 修改副本后必须回写
            obj.cell_vol = value
        """
        ...
    @cell_vol.setter
    def cell_vol(self, value: Sequence[int]) -> None:
        """底层 `unitree_hg::msg::dds_::BmsState_` 的 `cell_vol` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 40 个元素；元素约束：取值范围为 0 到 65535。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.cell_vol = value
        """
        ...
    @property
    def bmsvoltage(self) -> list[int]:
        """底层 `unitree_hg::msg::dds_::BmsState_` 的 `bmsvoltage` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：取值范围为 0 到 4294967295。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.bmsvoltage
            # 修改副本后必须回写
            obj.bmsvoltage = value
        """
        ...
    @bmsvoltage.setter
    def bmsvoltage(self, value: Sequence[int]) -> None:
        """底层 `unitree_hg::msg::dds_::BmsState_` 的 `bmsvoltage` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.bmsvoltage = value
        """
        ...
    @property
    def current(self) -> int:
        """底层 `unitree_hg::msg::dds_::BmsState_` 的 `current` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 -2147483648 到 2147483647。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.current
            # 修改副本后必须回写
            obj.current = value
        """
        ...
    @current.setter
    def current(self, value: int) -> None:
        """底层 `unitree_hg::msg::dds_::BmsState_` 的 `current` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 -2147483648 到 2147483647。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.current = value
        """
        ...
    @property
    def soc(self) -> int:
        """底层 `unitree_hg::msg::dds_::BmsState_` 的 `soc` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.soc
            # 修改副本后必须回写
            obj.soc = value
        """
        ...
    @soc.setter
    def soc(self, value: int) -> None:
        """底层 `unitree_hg::msg::dds_::BmsState_` 的 `soc` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.soc = value
        """
        ...
    @property
    def soh(self) -> int:
        """底层 `unitree_hg::msg::dds_::BmsState_` 的 `soh` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.soh
            # 修改副本后必须回写
            obj.soh = value
        """
        ...
    @soh.setter
    def soh(self, value: int) -> None:
        """底层 `unitree_hg::msg::dds_::BmsState_` 的 `soh` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.soh = value
        """
        ...
    @property
    def temperature(self) -> list[int]:
        """底层 `unitree_hg::msg::dds_::BmsState_` 的 `temperature` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 12 个元素；元素约束：取值范围为 -32768 到 32767。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.temperature
            # 修改副本后必须回写
            obj.temperature = value
        """
        ...
    @temperature.setter
    def temperature(self, value: Sequence[int]) -> None:
        """底层 `unitree_hg::msg::dds_::BmsState_` 的 `temperature` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 12 个元素；元素约束：取值范围为 -32768 到 32767。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.temperature = value
        """
        ...
    @property
    def cycle(self) -> int:
        """底层 `unitree_hg::msg::dds_::BmsState_` 的 `cycle` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 65535。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.cycle
            # 修改副本后必须回写
            obj.cycle = value
        """
        ...
    @cycle.setter
    def cycle(self, value: int) -> None:
        """底层 `unitree_hg::msg::dds_::BmsState_` 的 `cycle` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 65535。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.cycle = value
        """
        ...
    @property
    def manufacturer_date(self) -> int:
        """底层 `unitree_hg::msg::dds_::BmsState_` 的 `manufacturer_date` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 65535。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.manufacturer_date
            # 修改副本后必须回写
            obj.manufacturer_date = value
        """
        ...
    @manufacturer_date.setter
    def manufacturer_date(self, value: int) -> None:
        """底层 `unitree_hg::msg::dds_::BmsState_` 的 `manufacturer_date` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 65535。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.manufacturer_date = value
        """
        ...
    @property
    def bmsstate(self) -> list[int]:
        """底层 `unitree_hg::msg::dds_::BmsState_` 的 `bmsstate` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 5 个元素；元素约束：取值范围为 0 到 4294967295。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.bmsstate
            # 修改副本后必须回写
            obj.bmsstate = value
        """
        ...
    @bmsstate.setter
    def bmsstate(self, value: Sequence[int]) -> None:
        """底层 `unitree_hg::msg::dds_::BmsState_` 的 `bmsstate` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 5 个元素；元素约束：取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.bmsstate = value
        """
        ...
    @property
    def reserve(self) -> list[int]:
        """底层 `unitree_hg::msg::dds_::BmsState_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：取值范围为 0 到 4294967295。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.reserve
            # 修改副本后必须回写
            obj.reserve = value
        """
        ...
    @reserve.setter
    def reserve(self, value: Sequence[int]) -> None:
        """底层 `unitree_hg::msg::dds_::BmsState_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.reserve = value
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

class MotorCmd:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.hg import MotorCmd
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `MotorCmd` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = MotorCmd()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: MotorCmd_()
        """
        ...
    @property
    def mode(self) -> int:
        """底层 `unitree_hg::msg::dds_::MotorCmd_` 的 `mode` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.mode
            # 修改副本后必须回写
            obj.mode = value
        """
        ...
    @mode.setter
    def mode(self, value: int) -> None:
        """底层 `unitree_hg::msg::dds_::MotorCmd_` 的 `mode` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.mode = value
        """
        ...
    @property
    def q(self) -> float:
        """底层 `unitree_hg::msg::dds_::MotorCmd_` 的 `q` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.q
            # 修改副本后必须回写
            obj.q = value
        """
        ...
    @q.setter
    def q(self, value: float) -> None:
        """底层 `unitree_hg::msg::dds_::MotorCmd_` 的 `q` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.q = value
        """
        ...
    @property
    def dq(self) -> float:
        """底层 `unitree_hg::msg::dds_::MotorCmd_` 的 `dq` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.dq
            # 修改副本后必须回写
            obj.dq = value
        """
        ...
    @dq.setter
    def dq(self, value: float) -> None:
        """底层 `unitree_hg::msg::dds_::MotorCmd_` 的 `dq` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.dq = value
        """
        ...
    @property
    def tau(self) -> float:
        """底层 `unitree_hg::msg::dds_::MotorCmd_` 的 `tau` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.tau
            # 修改副本后必须回写
            obj.tau = value
        """
        ...
    @tau.setter
    def tau(self, value: float) -> None:
        """底层 `unitree_hg::msg::dds_::MotorCmd_` 的 `tau` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.tau = value
        """
        ...
    @property
    def kp(self) -> float:
        """底层 `unitree_hg::msg::dds_::MotorCmd_` 的 `kp` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.kp
            # 修改副本后必须回写
            obj.kp = value
        """
        ...
    @kp.setter
    def kp(self, value: float) -> None:
        """底层 `unitree_hg::msg::dds_::MotorCmd_` 的 `kp` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.kp = value
        """
        ...
    @property
    def kd(self) -> float:
        """底层 `unitree_hg::msg::dds_::MotorCmd_` 的 `kd` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.kd
            # 修改副本后必须回写
            obj.kd = value
        """
        ...
    @kd.setter
    def kd(self, value: float) -> None:
        """底层 `unitree_hg::msg::dds_::MotorCmd_` 的 `kd` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.kd = value
        """
        ...
    @property
    def reserve(self) -> int:
        """底层 `unitree_hg::msg::dds_::MotorCmd_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.reserve
            # 修改副本后必须回写
            obj.reserve = value
        """
        ...
    @reserve.setter
    def reserve(self, value: int) -> None:
        """底层 `unitree_hg::msg::dds_::MotorCmd_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.reserve = value
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

class HandCmd:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.hg import HandCmd
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `HandCmd` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = HandCmd()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: HandCmd_()
        """
        ...
    @property
    def motor_cmd(self) -> list[MotorCmd]:
        """底层 `unitree_hg::msg::dds_::HandCmd_` 的 `motor_cmd` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector

        Returns:
            list[MotorCmd]：字段当前值。

        Examples:
            value = obj.motor_cmd
            # 修改副本后必须回写
            obj.motor_cmd = value
        """
        ...
    @motor_cmd.setter
    def motor_cmd(self, value: Sequence[MotorCmd]) -> None:
        """底层 `unitree_hg::msg::dds_::HandCmd_` 的 `motor_cmd` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.motor_cmd = value
        """
        ...
    @property
    def reserve(self) -> list[int]:
        """底层 `unitree_hg::msg::dds_::HandCmd_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：取值范围为 0 到 4294967295。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.reserve
            # 修改副本后必须回写
            obj.reserve = value
        """
        ...
    @reserve.setter
    def reserve(self, value: Sequence[int]) -> None:
        """底层 `unitree_hg::msg::dds_::HandCmd_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.reserve = value
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

class IMUState:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.hg import IMUState
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `IMUState` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = IMUState()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: IMUState_()
        """
        ...
    @property
    def quaternion(self) -> list[float]:
        """底层 `unitree_hg::msg::dds_::IMUState_` 的 `quaternion` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_hg::msg::dds_::IMUState_` 的 `quaternion` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_hg::msg::dds_::IMUState_` 的 `gyroscope` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_hg::msg::dds_::IMUState_` 的 `gyroscope` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_hg::msg::dds_::IMUState_` 的 `accelerometer` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_hg::msg::dds_::IMUState_` 的 `accelerometer` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_hg::msg::dds_::IMUState_` 的 `rpy` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_hg::msg::dds_::IMUState_` 的 `rpy` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_hg::msg::dds_::IMUState_` 的 `temperature` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 -32768 到 32767。

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
        """底层 `unitree_hg::msg::dds_::IMUState_` 的 `temperature` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 -32768 到 32767。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.temperature = value
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

class MotorState:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.hg import MotorState
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `MotorState` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = MotorState()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: MotorState_()
        """
        ...
    @property
    def mode(self) -> int:
        """底层 `unitree_hg::msg::dds_::MotorState_` 的 `mode` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.mode
            # 修改副本后必须回写
            obj.mode = value
        """
        ...
    @mode.setter
    def mode(self, value: int) -> None:
        """底层 `unitree_hg::msg::dds_::MotorState_` 的 `mode` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.mode = value
        """
        ...
    @property
    def q(self) -> float:
        """底层 `unitree_hg::msg::dds_::MotorState_` 的 `q` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.q
            # 修改副本后必须回写
            obj.q = value
        """
        ...
    @q.setter
    def q(self, value: float) -> None:
        """底层 `unitree_hg::msg::dds_::MotorState_` 的 `q` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.q = value
        """
        ...
    @property
    def dq(self) -> float:
        """底层 `unitree_hg::msg::dds_::MotorState_` 的 `dq` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.dq
            # 修改副本后必须回写
            obj.dq = value
        """
        ...
    @dq.setter
    def dq(self, value: float) -> None:
        """底层 `unitree_hg::msg::dds_::MotorState_` 的 `dq` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.dq = value
        """
        ...
    @property
    def ddq(self) -> float:
        """底层 `unitree_hg::msg::dds_::MotorState_` 的 `ddq` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.ddq
            # 修改副本后必须回写
            obj.ddq = value
        """
        ...
    @ddq.setter
    def ddq(self, value: float) -> None:
        """底层 `unitree_hg::msg::dds_::MotorState_` 的 `ddq` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.ddq = value
        """
        ...
    @property
    def tau_est(self) -> float:
        """底层 `unitree_hg::msg::dds_::MotorState_` 的 `tau_est` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.tau_est
            # 修改副本后必须回写
            obj.tau_est = value
        """
        ...
    @tau_est.setter
    def tau_est(self, value: float) -> None:
        """底层 `unitree_hg::msg::dds_::MotorState_` 的 `tau_est` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.tau_est = value
        """
        ...
    @property
    def temperature(self) -> list[int]:
        """底层 `unitree_hg::msg::dds_::MotorState_` 的 `temperature` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 -32768 到 32767。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.temperature
            # 修改副本后必须回写
            obj.temperature = value
        """
        ...
    @temperature.setter
    def temperature(self, value: Sequence[int]) -> None:
        """底层 `unitree_hg::msg::dds_::MotorState_` 的 `temperature` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 -32768 到 32767。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.temperature = value
        """
        ...
    @property
    def vol(self) -> float:
        """底层 `unitree_hg::msg::dds_::MotorState_` 的 `vol` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.vol
            # 修改副本后必须回写
            obj.vol = value
        """
        ...
    @vol.setter
    def vol(self, value: float) -> None:
        """底层 `unitree_hg::msg::dds_::MotorState_` 的 `vol` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.vol = value
        """
        ...
    @property
    def sensor(self) -> list[int]:
        """底层 `unitree_hg::msg::dds_::MotorState_` 的 `sensor` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 4294967295。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.sensor
            # 修改副本后必须回写
            obj.sensor = value
        """
        ...
    @sensor.setter
    def sensor(self, value: Sequence[int]) -> None:
        """底层 `unitree_hg::msg::dds_::MotorState_` 的 `sensor` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.sensor = value
        """
        ...
    @property
    def motorstate(self) -> int:
        """底层 `unitree_hg::msg::dds_::MotorState_` 的 `motorstate` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.motorstate
            # 修改副本后必须回写
            obj.motorstate = value
        """
        ...
    @motorstate.setter
    def motorstate(self, value: int) -> None:
        """底层 `unitree_hg::msg::dds_::MotorState_` 的 `motorstate` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.motorstate = value
        """
        ...
    @property
    def reserve(self) -> list[int]:
        """底层 `unitree_hg::msg::dds_::MotorState_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：取值范围为 0 到 4294967295。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.reserve
            # 修改副本后必须回写
            obj.reserve = value
        """
        ...
    @reserve.setter
    def reserve(self, value: Sequence[int]) -> None:
        """底层 `unitree_hg::msg::dds_::MotorState_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.reserve = value
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

class PressSensorState:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.hg import PressSensorState
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `PressSensorState` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = PressSensorState()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: PressSensorState_()
        """
        ...
    @property
    def pressure(self) -> list[float]:
        """底层 `unitree_hg::msg::dds_::PressSensorState_` 的 `pressure` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 12 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            list[float]：字段当前值。

        Examples:
            value = obj.pressure
            # 修改副本后必须回写
            obj.pressure = value
        """
        ...
    @pressure.setter
    def pressure(self, value: Sequence[float]) -> None:
        """底层 `unitree_hg::msg::dds_::PressSensorState_` 的 `pressure` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 12 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.pressure = value
        """
        ...
    @property
    def temperature(self) -> list[float]:
        """底层 `unitree_hg::msg::dds_::PressSensorState_` 的 `temperature` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 12 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            list[float]：字段当前值。

        Examples:
            value = obj.temperature
            # 修改副本后必须回写
            obj.temperature = value
        """
        ...
    @temperature.setter
    def temperature(self, value: Sequence[float]) -> None:
        """底层 `unitree_hg::msg::dds_::PressSensorState_` 的 `temperature` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 12 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.temperature = value
        """
        ...
    @property
    def lost(self) -> int:
        """底层 `unitree_hg::msg::dds_::PressSensorState_` 的 `lost` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.lost
            # 修改副本后必须回写
            obj.lost = value
        """
        ...
    @lost.setter
    def lost(self, value: int) -> None:
        """底层 `unitree_hg::msg::dds_::PressSensorState_` 的 `lost` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.lost = value
        """
        ...
    @property
    def reserve(self) -> int:
        """底层 `unitree_hg::msg::dds_::PressSensorState_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.reserve
            # 修改副本后必须回写
            obj.reserve = value
        """
        ...
    @reserve.setter
    def reserve(self, value: int) -> None:
        """底层 `unitree_hg::msg::dds_::PressSensorState_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.reserve = value
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

class HandState:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.hg import HandState
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `HandState` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = HandState()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: HandState_()
        """
        ...
    @property
    def motor_state(self) -> list[MotorState]:
        """底层 `unitree_hg::msg::dds_::HandState_` 的 `motor_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector

        Returns:
            list[MotorState]：字段当前值。

        Examples:
            value = obj.motor_state
            # 修改副本后必须回写
            obj.motor_state = value
        """
        ...
    @motor_state.setter
    def motor_state(self, value: Sequence[MotorState]) -> None:
        """底层 `unitree_hg::msg::dds_::HandState_` 的 `motor_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.motor_state = value
        """
        ...
    @property
    def press_sensor_state(self) -> list[PressSensorState]:
        """底层 `unitree_hg::msg::dds_::HandState_` 的 `press_sensor_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector

        Returns:
            list[PressSensorState]：字段当前值。

        Examples:
            value = obj.press_sensor_state
            # 修改副本后必须回写
            obj.press_sensor_state = value
        """
        ...
    @press_sensor_state.setter
    def press_sensor_state(self, value: Sequence[PressSensorState]) -> None:
        """底层 `unitree_hg::msg::dds_::HandState_` 的 `press_sensor_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.press_sensor_state = value
        """
        ...
    @property
    def imu_state(self) -> IMUState:
        """底层 `unitree_hg::msg::dds_::HandState_` 的 `imu_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            IMUState：字段当前值。

        Examples:
            value = obj.imu_state
            # 修改副本后必须回写
            obj.imu_state = value
        """
        ...
    @imu_state.setter
    def imu_state(self, value: IMUState) -> None:
        """底层 `unitree_hg::msg::dds_::HandState_` 的 `imu_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.imu_state = value
        """
        ...
    @property
    def power_v(self) -> float:
        """底层 `unitree_hg::msg::dds_::HandState_` 的 `power_v` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.power_v
            # 修改副本后必须回写
            obj.power_v = value
        """
        ...
    @power_v.setter
    def power_v(self, value: float) -> None:
        """底层 `unitree_hg::msg::dds_::HandState_` 的 `power_v` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.power_v = value
        """
        ...
    @property
    def power_a(self) -> float:
        """底层 `unitree_hg::msg::dds_::HandState_` 的 `power_a` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.power_a
            # 修改副本后必须回写
            obj.power_a = value
        """
        ...
    @power_a.setter
    def power_a(self, value: float) -> None:
        """底层 `unitree_hg::msg::dds_::HandState_` 的 `power_a` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.power_a = value
        """
        ...
    @property
    def system_v(self) -> float:
        """底层 `unitree_hg::msg::dds_::HandState_` 的 `system_v` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.system_v
            # 修改副本后必须回写
            obj.system_v = value
        """
        ...
    @system_v.setter
    def system_v(self, value: float) -> None:
        """底层 `unitree_hg::msg::dds_::HandState_` 的 `system_v` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.system_v = value
        """
        ...
    @property
    def device_v(self) -> float:
        """底层 `unitree_hg::msg::dds_::HandState_` 的 `device_v` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.device_v
            # 修改副本后必须回写
            obj.device_v = value
        """
        ...
    @device_v.setter
    def device_v(self, value: float) -> None:
        """底层 `unitree_hg::msg::dds_::HandState_` 的 `device_v` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.device_v = value
        """
        ...
    @property
    def error(self) -> list[int]:
        """底层 `unitree_hg::msg::dds_::HandState_` 的 `error` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 4294967295。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.error
            # 修改副本后必须回写
            obj.error = value
        """
        ...
    @error.setter
    def error(self, value: Sequence[int]) -> None:
        """底层 `unitree_hg::msg::dds_::HandState_` 的 `error` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.error = value
        """
        ...
    @property
    def reserve(self) -> list[int]:
        """底层 `unitree_hg::msg::dds_::HandState_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 4294967295。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.reserve
            # 修改副本后必须回写
            obj.reserve = value
        """
        ...
    @reserve.setter
    def reserve(self, value: Sequence[int]) -> None:
        """底层 `unitree_hg::msg::dds_::HandState_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.reserve = value
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

class LowCmd:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.hg import LowCmd
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `LowCmd` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = LowCmd()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: LowCmd_()
        """
        ...
    @property
    def mode_pr(self) -> int:
        """底层 `unitree_hg::msg::dds_::LowCmd_` 的 `mode_pr` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.mode_pr
            # 修改副本后必须回写
            obj.mode_pr = value
        """
        ...
    @mode_pr.setter
    def mode_pr(self, value: int) -> None:
        """底层 `unitree_hg::msg::dds_::LowCmd_` 的 `mode_pr` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.mode_pr = value
        """
        ...
    @property
    def mode_machine(self) -> int:
        """底层 `unitree_hg::msg::dds_::LowCmd_` 的 `mode_machine` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.mode_machine
            # 修改副本后必须回写
            obj.mode_machine = value
        """
        ...
    @mode_machine.setter
    def mode_machine(self, value: int) -> None:
        """底层 `unitree_hg::msg::dds_::LowCmd_` 的 `mode_machine` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.mode_machine = value
        """
        ...
    @property
    def motor_cmd(self) -> list[MotorCmd]:
        """底层 `unitree_hg::msg::dds_::LowCmd_` 的 `motor_cmd` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 35 个元素

        Returns:
            list[MotorCmd]：字段当前值。

        Examples:
            value = obj.motor_cmd
            # 修改副本后必须回写
            obj.motor_cmd = value
        """
        ...
    @motor_cmd.setter
    def motor_cmd(self, value: Sequence[MotorCmd]) -> None:
        """底层 `unitree_hg::msg::dds_::LowCmd_` 的 `motor_cmd` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 35 个元素

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.motor_cmd = value
        """
        ...
    @property
    def reserve(self) -> list[int]:
        """底层 `unitree_hg::msg::dds_::LowCmd_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：取值范围为 0 到 4294967295。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.reserve
            # 修改副本后必须回写
            obj.reserve = value
        """
        ...
    @reserve.setter
    def reserve(self, value: Sequence[int]) -> None:
        """底层 `unitree_hg::msg::dds_::LowCmd_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.reserve = value
        """
        ...
    @property
    def crc(self) -> int:
        """底层 `unitree_hg::msg::dds_::LowCmd_` 的 `crc` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.crc
            # 修改副本后必须回写
            obj.crc = value
        """
        ...
    @crc.setter
    def crc(self, value: int) -> None:
        """底层 `unitree_hg::msg::dds_::LowCmd_` 的 `crc` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.crc = value
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

class LowState:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.hg import LowState
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `LowState` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = LowState()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: LowState_()
        """
        ...
    @property
    def version(self) -> list[int]:
        """底层 `unitree_hg::msg::dds_::LowState_` 的 `version` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 4294967295。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.version
            # 修改副本后必须回写
            obj.version = value
        """
        ...
    @version.setter
    def version(self, value: Sequence[int]) -> None:
        """底层 `unitree_hg::msg::dds_::LowState_` 的 `version` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.version = value
        """
        ...
    @property
    def mode_pr(self) -> int:
        """底层 `unitree_hg::msg::dds_::LowState_` 的 `mode_pr` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.mode_pr
            # 修改副本后必须回写
            obj.mode_pr = value
        """
        ...
    @mode_pr.setter
    def mode_pr(self, value: int) -> None:
        """底层 `unitree_hg::msg::dds_::LowState_` 的 `mode_pr` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.mode_pr = value
        """
        ...
    @property
    def mode_machine(self) -> int:
        """底层 `unitree_hg::msg::dds_::LowState_` 的 `mode_machine` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.mode_machine
            # 修改副本后必须回写
            obj.mode_machine = value
        """
        ...
    @mode_machine.setter
    def mode_machine(self, value: int) -> None:
        """底层 `unitree_hg::msg::dds_::LowState_` 的 `mode_machine` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.mode_machine = value
        """
        ...
    @property
    def tick(self) -> int:
        """底层 `unitree_hg::msg::dds_::LowState_` 的 `tick` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

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
        """底层 `unitree_hg::msg::dds_::LowState_` 的 `tick` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.tick = value
        """
        ...
    @property
    def imu_state(self) -> IMUState:
        """底层 `unitree_hg::msg::dds_::LowState_` 的 `imu_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            IMUState：字段当前值。

        Examples:
            value = obj.imu_state
            # 修改副本后必须回写
            obj.imu_state = value
        """
        ...
    @imu_state.setter
    def imu_state(self, value: IMUState) -> None:
        """底层 `unitree_hg::msg::dds_::LowState_` 的 `imu_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.imu_state = value
        """
        ...
    @property
    def motor_state(self) -> list[MotorState]:
        """底层 `unitree_hg::msg::dds_::LowState_` 的 `motor_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 35 个元素

        Returns:
            list[MotorState]：字段当前值。

        Examples:
            value = obj.motor_state
            # 修改副本后必须回写
            obj.motor_state = value
        """
        ...
    @motor_state.setter
    def motor_state(self, value: Sequence[MotorState]) -> None:
        """底层 `unitree_hg::msg::dds_::LowState_` 的 `motor_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 35 个元素

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.motor_state = value
        """
        ...
    @property
    def wireless_remote(self) -> list[int]:
        """底层 `unitree_hg::msg::dds_::LowState_` 的 `wireless_remote` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 40 个元素；元素约束：取值范围为 0 到 255。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.wireless_remote
            # 修改副本后必须回写
            obj.wireless_remote = value
        """
        ...
    @wireless_remote.setter
    def wireless_remote(self, value: Sequence[int]) -> None:
        """底层 `unitree_hg::msg::dds_::LowState_` 的 `wireless_remote` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 40 个元素；元素约束：取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.wireless_remote = value
        """
        ...
    @property
    def reserve(self) -> list[int]:
        """底层 `unitree_hg::msg::dds_::LowState_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：取值范围为 0 到 4294967295。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.reserve
            # 修改副本后必须回写
            obj.reserve = value
        """
        ...
    @reserve.setter
    def reserve(self, value: Sequence[int]) -> None:
        """底层 `unitree_hg::msg::dds_::LowState_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.reserve = value
        """
        ...
    @property
    def crc(self) -> int:
        """底层 `unitree_hg::msg::dds_::LowState_` 的 `crc` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.crc
            # 修改副本后必须回写
            obj.crc = value
        """
        ...
    @crc.setter
    def crc(self, value: int) -> None:
        """底层 `unitree_hg::msg::dds_::LowState_` 的 `crc` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.crc = value
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

class MainBoardState:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.hg import MainBoardState
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `MainBoardState` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = MainBoardState()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: MainBoardState_()
        """
        ...
    @property
    def fan_state(self) -> list[int]:
        """底层 `unitree_hg::msg::dds_::MainBoardState_` 的 `fan_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 6 个元素；元素约束：取值范围为 0 到 65535。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.fan_state
            # 修改副本后必须回写
            obj.fan_state = value
        """
        ...
    @fan_state.setter
    def fan_state(self, value: Sequence[int]) -> None:
        """底层 `unitree_hg::msg::dds_::MainBoardState_` 的 `fan_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 6 个元素；元素约束：取值范围为 0 到 65535。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.fan_state = value
        """
        ...
    @property
    def temperature(self) -> list[int]:
        """底层 `unitree_hg::msg::dds_::MainBoardState_` 的 `temperature` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 6 个元素；元素约束：取值范围为 -32768 到 32767。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.temperature
            # 修改副本后必须回写
            obj.temperature = value
        """
        ...
    @temperature.setter
    def temperature(self, value: Sequence[int]) -> None:
        """底层 `unitree_hg::msg::dds_::MainBoardState_` 的 `temperature` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 6 个元素；元素约束：取值范围为 -32768 到 32767。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.temperature = value
        """
        ...
    @property
    def value(self) -> list[float]:
        """底层 `unitree_hg::msg::dds_::MainBoardState_` 的 `value` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 6 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            list[float]：字段当前值。

        Examples:
            value = obj.value
            # 修改副本后必须回写
            obj.value = value
        """
        ...
    @value.setter
    def value(self, value: Sequence[float]) -> None:
        """底层 `unitree_hg::msg::dds_::MainBoardState_` 的 `value` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 6 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.value = value
        """
        ...
    @property
    def state(self) -> list[int]:
        """底层 `unitree_hg::msg::dds_::MainBoardState_` 的 `state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 6 个元素；元素约束：取值范围为 0 到 4294967295。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.state
            # 修改副本后必须回写
            obj.state = value
        """
        ...
    @state.setter
    def state(self, value: Sequence[int]) -> None:
        """底层 `unitree_hg::msg::dds_::MainBoardState_` 的 `state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 6 个元素；元素约束：取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.state = value
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

class SportModeState:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.hg import SportModeState
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `SportModeState` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = SportModeState()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: SportModeState_()
        """
        ...
    @property
    def fsm_id(self) -> int:
        """底层 `unitree_hg::msg::dds_::SportModeState_` 的 `fsm_id` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.fsm_id
            # 修改副本后必须回写
            obj.fsm_id = value
        """
        ...
    @fsm_id.setter
    def fsm_id(self, value: int) -> None:
        """底层 `unitree_hg::msg::dds_::SportModeState_` 的 `fsm_id` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.fsm_id = value
        """
        ...
    @property
    def fsm_mode(self) -> int:
        """底层 `unitree_hg::msg::dds_::SportModeState_` 的 `fsm_mode` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.fsm_mode
            # 修改副本后必须回写
            obj.fsm_mode = value
        """
        ...
    @fsm_mode.setter
    def fsm_mode(self, value: int) -> None:
        """底层 `unitree_hg::msg::dds_::SportModeState_` 的 `fsm_mode` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.fsm_mode = value
        """
        ...
    @property
    def task_id(self) -> int:
        """底层 `unitree_hg::msg::dds_::SportModeState_` 的 `task_id` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.task_id
            # 修改副本后必须回写
            obj.task_id = value
        """
        ...
    @task_id.setter
    def task_id(self, value: int) -> None:
        """底层 `unitree_hg::msg::dds_::SportModeState_` 的 `task_id` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.task_id = value
        """
        ...
    @property
    def task_time(self) -> float:
        """底层 `unitree_hg::msg::dds_::SportModeState_` 的 `task_time` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.task_time
            # 修改副本后必须回写
            obj.task_time = value
        """
        ...
    @task_time.setter
    def task_time(self, value: float) -> None:
        """底层 `unitree_hg::msg::dds_::SportModeState_` 的 `task_time` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.task_time = value
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
