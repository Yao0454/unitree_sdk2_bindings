"""Generated DDS message bindings."""
from __future__ import annotations

from collections.abc import Sequence
from typing import Any

class AudioData:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.go2 import AudioData
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `AudioData` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = AudioData()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: AudioData_()
        """
        ...
    @property
    def time_frame(self) -> int:
        """底层 `unitree_go::msg::dds_::AudioData_` 的 `time_frame` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 18446744073709551615。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.time_frame
            # 修改副本后必须回写
            obj.time_frame = value
        """
        ...
    @time_frame.setter
    def time_frame(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::AudioData_` 的 `time_frame` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 18446744073709551615。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.time_frame = value
        """
        ...
    @property
    def data(self) -> list[int]:
        """底层 `unitree_go::msg::dds_::AudioData_` 的 `data` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector；元素约束：取值范围为 0 到 255。

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
        """底层 `unitree_go::msg::dds_::AudioData_` 的 `data` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector；元素约束：取值范围为 0 到 255。

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

class BmsCmd:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.go2 import BmsCmd
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
    def off(self) -> int:
        """底层 `unitree_go::msg::dds_::BmsCmd_` 的 `off` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.off
            # 修改副本后必须回写
            obj.off = value
        """
        ...
    @off.setter
    def off(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::BmsCmd_` 的 `off` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.off = value
        """
        ...
    @property
    def reserve(self) -> list[int]:
        """底层 `unitree_go::msg::dds_::BmsCmd_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：取值范围为 0 到 255。

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
        """底层 `unitree_go::msg::dds_::BmsCmd_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：取值范围为 0 到 255。

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

    导入：from unitree_sdk2_cpp.idl.go2 import BmsState
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
        """底层 `unitree_go::msg::dds_::BmsState_` 的 `version_high` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

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
        """底层 `unitree_go::msg::dds_::BmsState_` 的 `version_high` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

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
        """底层 `unitree_go::msg::dds_::BmsState_` 的 `version_low` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

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
        """底层 `unitree_go::msg::dds_::BmsState_` 的 `version_low` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.version_low = value
        """
        ...
    @property
    def status(self) -> int:
        """底层 `unitree_go::msg::dds_::BmsState_` 的 `status` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.status
            # 修改副本后必须回写
            obj.status = value
        """
        ...
    @status.setter
    def status(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::BmsState_` 的 `status` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.status = value
        """
        ...
    @property
    def soc(self) -> int:
        """底层 `unitree_go::msg::dds_::BmsState_` 的 `soc` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

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
        """底层 `unitree_go::msg::dds_::BmsState_` 的 `soc` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.soc = value
        """
        ...
    @property
    def current(self) -> int:
        """底层 `unitree_go::msg::dds_::BmsState_` 的 `current` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 -2147483648 到 2147483647。

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
        """底层 `unitree_go::msg::dds_::BmsState_` 的 `current` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 -2147483648 到 2147483647。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.current = value
        """
        ...
    @property
    def cycle(self) -> int:
        """底层 `unitree_go::msg::dds_::BmsState_` 的 `cycle` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 65535。

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
        """底层 `unitree_go::msg::dds_::BmsState_` 的 `cycle` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 65535。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.cycle = value
        """
        ...
    @property
    def bq_ntc(self) -> list[int]:
        """底层 `unitree_go::msg::dds_::BmsState_` 的 `bq_ntc` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 255。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.bq_ntc
            # 修改副本后必须回写
            obj.bq_ntc = value
        """
        ...
    @bq_ntc.setter
    def bq_ntc(self, value: Sequence[int]) -> None:
        """底层 `unitree_go::msg::dds_::BmsState_` 的 `bq_ntc` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.bq_ntc = value
        """
        ...
    @property
    def mcu_ntc(self) -> list[int]:
        """底层 `unitree_go::msg::dds_::BmsState_` 的 `mcu_ntc` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 255。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.mcu_ntc
            # 修改副本后必须回写
            obj.mcu_ntc = value
        """
        ...
    @mcu_ntc.setter
    def mcu_ntc(self, value: Sequence[int]) -> None:
        """底层 `unitree_go::msg::dds_::BmsState_` 的 `mcu_ntc` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.mcu_ntc = value
        """
        ...
    @property
    def cell_vol(self) -> list[int]:
        """底层 `unitree_go::msg::dds_::BmsState_` 的 `cell_vol` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 15 个元素；元素约束：取值范围为 0 到 65535。

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
        """底层 `unitree_go::msg::dds_::BmsState_` 的 `cell_vol` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 15 个元素；元素约束：取值范围为 0 到 65535。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.cell_vol = value
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

class ConfigChangeStatus:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.go2 import ConfigChangeStatus
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `ConfigChangeStatus` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = ConfigChangeStatus()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: ConfigChangeStatus_()
        """
        ...
    @property
    def name(self) -> str:
        """底层 `unitree_go::msg::dds_::ConfigChangeStatus_` 的 `name` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

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
        """底层 `unitree_go::msg::dds_::ConfigChangeStatus_` 的 `name` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.name = value
        """
        ...
    @property
    def content(self) -> str:
        """底层 `unitree_go::msg::dds_::ConfigChangeStatus_` 的 `content` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

        Returns:
            str：字段当前值。

        Examples:
            value = obj.content
            # 修改副本后必须回写
            obj.content = value
        """
        ...
    @content.setter
    def content(self, value: str) -> None:
        """底层 `unitree_go::msg::dds_::ConfigChangeStatus_` 的 `content` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.content = value
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

class Error:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.go2 import Error
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `Error` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = Error()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Error_()
        """
        ...
    @property
    def source(self) -> int:
        """底层 `unitree_go::msg::dds_::Error_` 的 `source` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.source
            # 修改副本后必须回写
            obj.source = value
        """
        ...
    @source.setter
    def source(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::Error_` 的 `source` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.source = value
        """
        ...
    @property
    def state(self) -> int:
        """底层 `unitree_go::msg::dds_::Error_` 的 `state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.state
            # 修改副本后必须回写
            obj.state = value
        """
        ...
    @state.setter
    def state(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::Error_` 的 `state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

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

class Go2FrontVideoData:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.go2 import Go2FrontVideoData
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `Go2FrontVideoData` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = Go2FrontVideoData()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Go2FrontVideoData_()
        """
        ...
    @property
    def time_frame(self) -> int:
        """底层 `unitree_go::msg::dds_::Go2FrontVideoData_` 的 `time_frame` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 18446744073709551615。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.time_frame
            # 修改副本后必须回写
            obj.time_frame = value
        """
        ...
    @time_frame.setter
    def time_frame(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::Go2FrontVideoData_` 的 `time_frame` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 18446744073709551615。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.time_frame = value
        """
        ...
    @property
    def video720p(self) -> list[int]:
        """底层 `unitree_go::msg::dds_::Go2FrontVideoData_` 的 `video720p` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector；元素约束：取值范围为 0 到 255。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.video720p
            # 修改副本后必须回写
            obj.video720p = value
        """
        ...
    @video720p.setter
    def video720p(self, value: Sequence[int]) -> None:
        """底层 `unitree_go::msg::dds_::Go2FrontVideoData_` 的 `video720p` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector；元素约束：取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.video720p = value
        """
        ...
    @property
    def video360p(self) -> list[int]:
        """底层 `unitree_go::msg::dds_::Go2FrontVideoData_` 的 `video360p` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector；元素约束：取值范围为 0 到 255。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.video360p
            # 修改副本后必须回写
            obj.video360p = value
        """
        ...
    @video360p.setter
    def video360p(self, value: Sequence[int]) -> None:
        """底层 `unitree_go::msg::dds_::Go2FrontVideoData_` 的 `video360p` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector；元素约束：取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.video360p = value
        """
        ...
    @property
    def video180p(self) -> list[int]:
        """底层 `unitree_go::msg::dds_::Go2FrontVideoData_` 的 `video180p` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector；元素约束：取值范围为 0 到 255。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.video180p
            # 修改副本后必须回写
            obj.video180p = value
        """
        ...
    @video180p.setter
    def video180p(self, value: Sequence[int]) -> None:
        """底层 `unitree_go::msg::dds_::Go2FrontVideoData_` 的 `video180p` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector；元素约束：取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.video180p = value
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

class HeightMap:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.go2 import HeightMap
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `HeightMap` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = HeightMap()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: HeightMap_()
        """
        ...
    @property
    def stamp(self) -> float:
        """底层 `unitree_go::msg::dds_::HeightMap_` 的 `stamp` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.stamp
            # 修改副本后必须回写
            obj.stamp = value
        """
        ...
    @stamp.setter
    def stamp(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::HeightMap_` 的 `stamp` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::HeightMap_` 的 `frame_id` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

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
        """底层 `unitree_go::msg::dds_::HeightMap_` 的 `frame_id` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.frame_id = value
        """
        ...
    @property
    def resolution(self) -> float:
        """底层 `unitree_go::msg::dds_::HeightMap_` 的 `resolution` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::HeightMap_` 的 `resolution` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::HeightMap_` 的 `width` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

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
        """底层 `unitree_go::msg::dds_::HeightMap_` 的 `width` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

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
        """底层 `unitree_go::msg::dds_::HeightMap_` 的 `height` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

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
        """底层 `unitree_go::msg::dds_::HeightMap_` 的 `height` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.height = value
        """
        ...
    @property
    def origin(self) -> list[float]:
        """底层 `unitree_go::msg::dds_::HeightMap_` 的 `origin` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            list[float]：字段当前值。

        Examples:
            value = obj.origin
            # 修改副本后必须回写
            obj.origin = value
        """
        ...
    @origin.setter
    def origin(self, value: Sequence[float]) -> None:
        """底层 `unitree_go::msg::dds_::HeightMap_` 的 `origin` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.origin = value
        """
        ...
    @property
    def data(self) -> list[float]:
        """底层 `unitree_go::msg::dds_::HeightMap_` 的 `data` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            list[float]：字段当前值。

        Examples:
            value = obj.data
            # 修改副本后必须回写
            obj.data = value
        """
        ...
    @data.setter
    def data(self, value: Sequence[float]) -> None:
        """底层 `unitree_go::msg::dds_::HeightMap_` 的 `data` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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

class IMUState:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.go2 import IMUState
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
        """底层 `unitree_go::msg::dds_::IMUState_` 的 `quaternion` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::IMUState_` 的 `quaternion` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::IMUState_` 的 `gyroscope` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::IMUState_` 的 `gyroscope` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::IMUState_` 的 `accelerometer` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::IMUState_` 的 `accelerometer` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::IMUState_` 的 `rpy` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::IMUState_` 的 `rpy` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::IMUState_` 的 `temperature` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

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
        """底层 `unitree_go::msg::dds_::IMUState_` 的 `temperature` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

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

class InterfaceConfig:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.go2 import InterfaceConfig
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `InterfaceConfig` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = InterfaceConfig()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: InterfaceConfig_()
        """
        ...
    @property
    def mode(self) -> int:
        """底层 `unitree_go::msg::dds_::InterfaceConfig_` 的 `mode` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

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
        """底层 `unitree_go::msg::dds_::InterfaceConfig_` 的 `mode` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.mode = value
        """
        ...
    @property
    def value(self) -> int:
        """底层 `unitree_go::msg::dds_::InterfaceConfig_` 的 `value` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.value
            # 修改副本后必须回写
            obj.value = value
        """
        ...
    @value.setter
    def value(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::InterfaceConfig_` 的 `value` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.value = value
        """
        ...
    @property
    def reserve(self) -> list[int]:
        """底层 `unitree_go::msg::dds_::InterfaceConfig_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 255。

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
        """底层 `unitree_go::msg::dds_::InterfaceConfig_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 255。

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

class LidarState:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.go2 import LidarState
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `LidarState` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = LidarState()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: LidarState_()
        """
        ...
    @property
    def stamp(self) -> float:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `stamp` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.stamp
            # 修改副本后必须回写
            obj.stamp = value
        """
        ...
    @stamp.setter
    def stamp(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `stamp` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.stamp = value
        """
        ...
    @property
    def firmware_version(self) -> str:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `firmware_version` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

        Returns:
            str：字段当前值。

        Examples:
            value = obj.firmware_version
            # 修改副本后必须回写
            obj.firmware_version = value
        """
        ...
    @firmware_version.setter
    def firmware_version(self, value: str) -> None:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `firmware_version` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.firmware_version = value
        """
        ...
    @property
    def software_version(self) -> str:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `software_version` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

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
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `software_version` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.software_version = value
        """
        ...
    @property
    def sdk_version(self) -> str:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `sdk_version` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

        Returns:
            str：字段当前值。

        Examples:
            value = obj.sdk_version
            # 修改副本后必须回写
            obj.sdk_version = value
        """
        ...
    @sdk_version.setter
    def sdk_version(self, value: str) -> None:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `sdk_version` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.sdk_version = value
        """
        ...
    @property
    def sys_rotation_speed(self) -> float:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `sys_rotation_speed` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.sys_rotation_speed
            # 修改副本后必须回写
            obj.sys_rotation_speed = value
        """
        ...
    @sys_rotation_speed.setter
    def sys_rotation_speed(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `sys_rotation_speed` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.sys_rotation_speed = value
        """
        ...
    @property
    def com_rotation_speed(self) -> float:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `com_rotation_speed` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.com_rotation_speed
            # 修改副本后必须回写
            obj.com_rotation_speed = value
        """
        ...
    @com_rotation_speed.setter
    def com_rotation_speed(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `com_rotation_speed` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.com_rotation_speed = value
        """
        ...
    @property
    def error_state(self) -> int:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `error_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.error_state
            # 修改副本后必须回写
            obj.error_state = value
        """
        ...
    @error_state.setter
    def error_state(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `error_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.error_state = value
        """
        ...
    @property
    def dirty_percentage(self) -> int:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `dirty_percentage` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.dirty_percentage
            # 修改副本后必须回写
            obj.dirty_percentage = value
        """
        ...
    @dirty_percentage.setter
    def dirty_percentage(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `dirty_percentage` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.dirty_percentage = value
        """
        ...
    @property
    def cloud_frequency(self) -> float:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `cloud_frequency` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.cloud_frequency
            # 修改副本后必须回写
            obj.cloud_frequency = value
        """
        ...
    @cloud_frequency.setter
    def cloud_frequency(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `cloud_frequency` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.cloud_frequency = value
        """
        ...
    @property
    def cloud_packet_loss_rate(self) -> float:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `cloud_packet_loss_rate` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.cloud_packet_loss_rate
            # 修改副本后必须回写
            obj.cloud_packet_loss_rate = value
        """
        ...
    @cloud_packet_loss_rate.setter
    def cloud_packet_loss_rate(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `cloud_packet_loss_rate` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.cloud_packet_loss_rate = value
        """
        ...
    @property
    def cloud_size(self) -> int:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `cloud_size` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.cloud_size
            # 修改副本后必须回写
            obj.cloud_size = value
        """
        ...
    @cloud_size.setter
    def cloud_size(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `cloud_size` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.cloud_size = value
        """
        ...
    @property
    def cloud_scan_num(self) -> int:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `cloud_scan_num` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.cloud_scan_num
            # 修改副本后必须回写
            obj.cloud_scan_num = value
        """
        ...
    @cloud_scan_num.setter
    def cloud_scan_num(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `cloud_scan_num` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.cloud_scan_num = value
        """
        ...
    @property
    def imu_frequency(self) -> float:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `imu_frequency` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.imu_frequency
            # 修改副本后必须回写
            obj.imu_frequency = value
        """
        ...
    @imu_frequency.setter
    def imu_frequency(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `imu_frequency` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.imu_frequency = value
        """
        ...
    @property
    def imu_packet_loss_rate(self) -> float:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `imu_packet_loss_rate` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.imu_packet_loss_rate
            # 修改副本后必须回写
            obj.imu_packet_loss_rate = value
        """
        ...
    @imu_packet_loss_rate.setter
    def imu_packet_loss_rate(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `imu_packet_loss_rate` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.imu_packet_loss_rate = value
        """
        ...
    @property
    def imu_rpy(self) -> list[float]:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `imu_rpy` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            list[float]：字段当前值。

        Examples:
            value = obj.imu_rpy
            # 修改副本后必须回写
            obj.imu_rpy = value
        """
        ...
    @imu_rpy.setter
    def imu_rpy(self, value: Sequence[float]) -> None:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `imu_rpy` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.imu_rpy = value
        """
        ...
    @property
    def serial_recv_stamp(self) -> float:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `serial_recv_stamp` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.serial_recv_stamp
            # 修改副本后必须回写
            obj.serial_recv_stamp = value
        """
        ...
    @serial_recv_stamp.setter
    def serial_recv_stamp(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `serial_recv_stamp` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.serial_recv_stamp = value
        """
        ...
    @property
    def serial_buffer_size(self) -> int:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `serial_buffer_size` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.serial_buffer_size
            # 修改副本后必须回写
            obj.serial_buffer_size = value
        """
        ...
    @serial_buffer_size.setter
    def serial_buffer_size(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `serial_buffer_size` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.serial_buffer_size = value
        """
        ...
    @property
    def serial_buffer_read(self) -> int:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `serial_buffer_read` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.serial_buffer_read
            # 修改副本后必须回写
            obj.serial_buffer_read = value
        """
        ...
    @serial_buffer_read.setter
    def serial_buffer_read(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::LidarState_` 的 `serial_buffer_read` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.serial_buffer_read = value
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

    导入：from unitree_sdk2_cpp.idl.go2 import MotorCmd
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
        """底层 `unitree_go::msg::dds_::MotorCmd_` 的 `mode` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

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
        """底层 `unitree_go::msg::dds_::MotorCmd_` 的 `mode` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

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
        """底层 `unitree_go::msg::dds_::MotorCmd_` 的 `q` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::MotorCmd_` 的 `q` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::MotorCmd_` 的 `dq` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::MotorCmd_` 的 `dq` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::MotorCmd_` 的 `tau` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::MotorCmd_` 的 `tau` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::MotorCmd_` 的 `kp` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::MotorCmd_` 的 `kp` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::MotorCmd_` 的 `kd` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::MotorCmd_` 的 `kd` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.kd = value
        """
        ...
    @property
    def reserve(self) -> list[int]:
        """底层 `unitree_go::msg::dds_::MotorCmd_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：取值范围为 0 到 4294967295。

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
        """底层 `unitree_go::msg::dds_::MotorCmd_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：取值范围为 0 到 4294967295。

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

    导入：from unitree_sdk2_cpp.idl.go2 import LowCmd
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
    def head(self) -> list[int]:
        """底层 `unitree_go::msg::dds_::LowCmd_` 的 `head` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 255。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.head
            # 修改副本后必须回写
            obj.head = value
        """
        ...
    @head.setter
    def head(self, value: Sequence[int]) -> None:
        """底层 `unitree_go::msg::dds_::LowCmd_` 的 `head` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.head = value
        """
        ...
    @property
    def level_flag(self) -> int:
        """底层 `unitree_go::msg::dds_::LowCmd_` 的 `level_flag` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.level_flag
            # 修改副本后必须回写
            obj.level_flag = value
        """
        ...
    @level_flag.setter
    def level_flag(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::LowCmd_` 的 `level_flag` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.level_flag = value
        """
        ...
    @property
    def frame_reserve(self) -> int:
        """底层 `unitree_go::msg::dds_::LowCmd_` 的 `frame_reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.frame_reserve
            # 修改副本后必须回写
            obj.frame_reserve = value
        """
        ...
    @frame_reserve.setter
    def frame_reserve(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::LowCmd_` 的 `frame_reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.frame_reserve = value
        """
        ...
    @property
    def sn(self) -> list[int]:
        """底层 `unitree_go::msg::dds_::LowCmd_` 的 `sn` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 4294967295。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.sn
            # 修改副本后必须回写
            obj.sn = value
        """
        ...
    @sn.setter
    def sn(self, value: Sequence[int]) -> None:
        """底层 `unitree_go::msg::dds_::LowCmd_` 的 `sn` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.sn = value
        """
        ...
    @property
    def version(self) -> list[int]:
        """底层 `unitree_go::msg::dds_::LowCmd_` 的 `version` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 4294967295。

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
        """底层 `unitree_go::msg::dds_::LowCmd_` 的 `version` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.version = value
        """
        ...
    @property
    def bandwidth(self) -> int:
        """底层 `unitree_go::msg::dds_::LowCmd_` 的 `bandwidth` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 65535。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.bandwidth
            # 修改副本后必须回写
            obj.bandwidth = value
        """
        ...
    @bandwidth.setter
    def bandwidth(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::LowCmd_` 的 `bandwidth` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 65535。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.bandwidth = value
        """
        ...
    @property
    def motor_cmd(self) -> list[MotorCmd]:
        """底层 `unitree_go::msg::dds_::LowCmd_` 的 `motor_cmd` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 20 个元素

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
        """底层 `unitree_go::msg::dds_::LowCmd_` 的 `motor_cmd` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 20 个元素

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.motor_cmd = value
        """
        ...
    @property
    def bms_cmd(self) -> BmsCmd:
        """底层 `unitree_go::msg::dds_::LowCmd_` 的 `bms_cmd` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            BmsCmd：字段当前值。

        Examples:
            value = obj.bms_cmd
            # 修改副本后必须回写
            obj.bms_cmd = value
        """
        ...
    @bms_cmd.setter
    def bms_cmd(self, value: BmsCmd) -> None:
        """底层 `unitree_go::msg::dds_::LowCmd_` 的 `bms_cmd` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.bms_cmd = value
        """
        ...
    @property
    def wireless_remote(self) -> list[int]:
        """底层 `unitree_go::msg::dds_::LowCmd_` 的 `wireless_remote` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 40 个元素；元素约束：取值范围为 0 到 255。

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
        """底层 `unitree_go::msg::dds_::LowCmd_` 的 `wireless_remote` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 40 个元素；元素约束：取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.wireless_remote = value
        """
        ...
    @property
    def led(self) -> list[int]:
        """底层 `unitree_go::msg::dds_::LowCmd_` 的 `led` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 12 个元素；元素约束：取值范围为 0 到 255。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.led
            # 修改副本后必须回写
            obj.led = value
        """
        ...
    @led.setter
    def led(self, value: Sequence[int]) -> None:
        """底层 `unitree_go::msg::dds_::LowCmd_` 的 `led` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 12 个元素；元素约束：取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.led = value
        """
        ...
    @property
    def fan(self) -> list[int]:
        """底层 `unitree_go::msg::dds_::LowCmd_` 的 `fan` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 255。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.fan
            # 修改副本后必须回写
            obj.fan = value
        """
        ...
    @fan.setter
    def fan(self, value: Sequence[int]) -> None:
        """底层 `unitree_go::msg::dds_::LowCmd_` 的 `fan` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.fan = value
        """
        ...
    @property
    def gpio(self) -> int:
        """底层 `unitree_go::msg::dds_::LowCmd_` 的 `gpio` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.gpio
            # 修改副本后必须回写
            obj.gpio = value
        """
        ...
    @gpio.setter
    def gpio(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::LowCmd_` 的 `gpio` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.gpio = value
        """
        ...
    @property
    def reserve(self) -> int:
        """底层 `unitree_go::msg::dds_::LowCmd_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

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
        """底层 `unitree_go::msg::dds_::LowCmd_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

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
        """底层 `unitree_go::msg::dds_::LowCmd_` 的 `crc` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

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
        """底层 `unitree_go::msg::dds_::LowCmd_` 的 `crc` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

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

class MotorState:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.go2 import MotorState
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
        """底层 `unitree_go::msg::dds_::MotorState_` 的 `mode` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

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
        """底层 `unitree_go::msg::dds_::MotorState_` 的 `mode` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

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
        """底层 `unitree_go::msg::dds_::MotorState_` 的 `q` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::MotorState_` 的 `q` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::MotorState_` 的 `dq` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::MotorState_` 的 `dq` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::MotorState_` 的 `ddq` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::MotorState_` 的 `ddq` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::MotorState_` 的 `tau_est` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::MotorState_` 的 `tau_est` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.tau_est = value
        """
        ...
    @property
    def q_raw(self) -> float:
        """底层 `unitree_go::msg::dds_::MotorState_` 的 `q_raw` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.q_raw
            # 修改副本后必须回写
            obj.q_raw = value
        """
        ...
    @q_raw.setter
    def q_raw(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::MotorState_` 的 `q_raw` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.q_raw = value
        """
        ...
    @property
    def dq_raw(self) -> float:
        """底层 `unitree_go::msg::dds_::MotorState_` 的 `dq_raw` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.dq_raw
            # 修改副本后必须回写
            obj.dq_raw = value
        """
        ...
    @dq_raw.setter
    def dq_raw(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::MotorState_` 的 `dq_raw` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.dq_raw = value
        """
        ...
    @property
    def ddq_raw(self) -> float:
        """底层 `unitree_go::msg::dds_::MotorState_` 的 `ddq_raw` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.ddq_raw
            # 修改副本后必须回写
            obj.ddq_raw = value
        """
        ...
    @ddq_raw.setter
    def ddq_raw(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::MotorState_` 的 `ddq_raw` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.ddq_raw = value
        """
        ...
    @property
    def temperature(self) -> int:
        """底层 `unitree_go::msg::dds_::MotorState_` 的 `temperature` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

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
        """底层 `unitree_go::msg::dds_::MotorState_` 的 `temperature` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

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
        """底层 `unitree_go::msg::dds_::MotorState_` 的 `lost` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

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
        """底层 `unitree_go::msg::dds_::MotorState_` 的 `lost` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.lost = value
        """
        ...
    @property
    def reserve(self) -> list[int]:
        """底层 `unitree_go::msg::dds_::MotorState_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 4294967295。

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
        """底层 `unitree_go::msg::dds_::MotorState_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 4294967295。

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

class LowState:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.go2 import LowState
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
    def head(self) -> list[int]:
        """底层 `unitree_go::msg::dds_::LowState_` 的 `head` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 255。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.head
            # 修改副本后必须回写
            obj.head = value
        """
        ...
    @head.setter
    def head(self, value: Sequence[int]) -> None:
        """底层 `unitree_go::msg::dds_::LowState_` 的 `head` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.head = value
        """
        ...
    @property
    def level_flag(self) -> int:
        """底层 `unitree_go::msg::dds_::LowState_` 的 `level_flag` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.level_flag
            # 修改副本后必须回写
            obj.level_flag = value
        """
        ...
    @level_flag.setter
    def level_flag(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::LowState_` 的 `level_flag` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.level_flag = value
        """
        ...
    @property
    def frame_reserve(self) -> int:
        """底层 `unitree_go::msg::dds_::LowState_` 的 `frame_reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.frame_reserve
            # 修改副本后必须回写
            obj.frame_reserve = value
        """
        ...
    @frame_reserve.setter
    def frame_reserve(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::LowState_` 的 `frame_reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.frame_reserve = value
        """
        ...
    @property
    def sn(self) -> list[int]:
        """底层 `unitree_go::msg::dds_::LowState_` 的 `sn` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 4294967295。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.sn
            # 修改副本后必须回写
            obj.sn = value
        """
        ...
    @sn.setter
    def sn(self, value: Sequence[int]) -> None:
        """底层 `unitree_go::msg::dds_::LowState_` 的 `sn` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.sn = value
        """
        ...
    @property
    def version(self) -> list[int]:
        """底层 `unitree_go::msg::dds_::LowState_` 的 `version` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 4294967295。

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
        """底层 `unitree_go::msg::dds_::LowState_` 的 `version` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.version = value
        """
        ...
    @property
    def bandwidth(self) -> int:
        """底层 `unitree_go::msg::dds_::LowState_` 的 `bandwidth` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 65535。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.bandwidth
            # 修改副本后必须回写
            obj.bandwidth = value
        """
        ...
    @bandwidth.setter
    def bandwidth(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::LowState_` 的 `bandwidth` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 65535。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.bandwidth = value
        """
        ...
    @property
    def imu_state(self) -> IMUState:
        """底层 `unitree_go::msg::dds_::LowState_` 的 `imu_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

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
        """底层 `unitree_go::msg::dds_::LowState_` 的 `imu_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

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
        """底层 `unitree_go::msg::dds_::LowState_` 的 `motor_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 20 个元素

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
        """底层 `unitree_go::msg::dds_::LowState_` 的 `motor_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 20 个元素

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.motor_state = value
        """
        ...
    @property
    def bms_state(self) -> BmsState:
        """底层 `unitree_go::msg::dds_::LowState_` 的 `bms_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            BmsState：字段当前值。

        Examples:
            value = obj.bms_state
            # 修改副本后必须回写
            obj.bms_state = value
        """
        ...
    @bms_state.setter
    def bms_state(self, value: BmsState) -> None:
        """底层 `unitree_go::msg::dds_::LowState_` 的 `bms_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.bms_state = value
        """
        ...
    @property
    def foot_force(self) -> list[int]:
        """底层 `unitree_go::msg::dds_::LowState_` 的 `foot_force` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：取值范围为 -32768 到 32767。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.foot_force
            # 修改副本后必须回写
            obj.foot_force = value
        """
        ...
    @foot_force.setter
    def foot_force(self, value: Sequence[int]) -> None:
        """底层 `unitree_go::msg::dds_::LowState_` 的 `foot_force` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：取值范围为 -32768 到 32767。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.foot_force = value
        """
        ...
    @property
    def foot_force_est(self) -> list[int]:
        """底层 `unitree_go::msg::dds_::LowState_` 的 `foot_force_est` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：取值范围为 -32768 到 32767。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.foot_force_est
            # 修改副本后必须回写
            obj.foot_force_est = value
        """
        ...
    @foot_force_est.setter
    def foot_force_est(self, value: Sequence[int]) -> None:
        """底层 `unitree_go::msg::dds_::LowState_` 的 `foot_force_est` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：取值范围为 -32768 到 32767。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.foot_force_est = value
        """
        ...
    @property
    def tick(self) -> int:
        """底层 `unitree_go::msg::dds_::LowState_` 的 `tick` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

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
        """底层 `unitree_go::msg::dds_::LowState_` 的 `tick` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.tick = value
        """
        ...
    @property
    def wireless_remote(self) -> list[int]:
        """底层 `unitree_go::msg::dds_::LowState_` 的 `wireless_remote` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 40 个元素；元素约束：取值范围为 0 到 255。

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
        """底层 `unitree_go::msg::dds_::LowState_` 的 `wireless_remote` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 40 个元素；元素约束：取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.wireless_remote = value
        """
        ...
    @property
    def bit_flag(self) -> int:
        """底层 `unitree_go::msg::dds_::LowState_` 的 `bit_flag` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.bit_flag
            # 修改副本后必须回写
            obj.bit_flag = value
        """
        ...
    @bit_flag.setter
    def bit_flag(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::LowState_` 的 `bit_flag` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.bit_flag = value
        """
        ...
    @property
    def adc_reel(self) -> float:
        """底层 `unitree_go::msg::dds_::LowState_` 的 `adc_reel` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.adc_reel
            # 修改副本后必须回写
            obj.adc_reel = value
        """
        ...
    @adc_reel.setter
    def adc_reel(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::LowState_` 的 `adc_reel` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.adc_reel = value
        """
        ...
    @property
    def temperature_ntc1(self) -> int:
        """底层 `unitree_go::msg::dds_::LowState_` 的 `temperature_ntc1` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.temperature_ntc1
            # 修改副本后必须回写
            obj.temperature_ntc1 = value
        """
        ...
    @temperature_ntc1.setter
    def temperature_ntc1(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::LowState_` 的 `temperature_ntc1` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.temperature_ntc1 = value
        """
        ...
    @property
    def temperature_ntc2(self) -> int:
        """底层 `unitree_go::msg::dds_::LowState_` 的 `temperature_ntc2` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.temperature_ntc2
            # 修改副本后必须回写
            obj.temperature_ntc2 = value
        """
        ...
    @temperature_ntc2.setter
    def temperature_ntc2(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::LowState_` 的 `temperature_ntc2` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.temperature_ntc2 = value
        """
        ...
    @property
    def power_v(self) -> float:
        """底层 `unitree_go::msg::dds_::LowState_` 的 `power_v` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::LowState_` 的 `power_v` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::LowState_` 的 `power_a` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::LowState_` 的 `power_a` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.power_a = value
        """
        ...
    @property
    def fan_frequency(self) -> list[int]:
        """底层 `unitree_go::msg::dds_::LowState_` 的 `fan_frequency` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：取值范围为 0 到 65535。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.fan_frequency
            # 修改副本后必须回写
            obj.fan_frequency = value
        """
        ...
    @fan_frequency.setter
    def fan_frequency(self, value: Sequence[int]) -> None:
        """底层 `unitree_go::msg::dds_::LowState_` 的 `fan_frequency` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：取值范围为 0 到 65535。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.fan_frequency = value
        """
        ...
    @property
    def reserve(self) -> int:
        """底层 `unitree_go::msg::dds_::LowState_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

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
        """底层 `unitree_go::msg::dds_::LowState_` 的 `reserve` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

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
        """底层 `unitree_go::msg::dds_::LowState_` 的 `crc` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

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
        """底层 `unitree_go::msg::dds_::LowState_` 的 `crc` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

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

class MotorCmds:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.go2 import MotorCmds
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `MotorCmds` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = MotorCmds()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: MotorCmds_()
        """
        ...
    @property
    def cmds(self) -> list[MotorCmd]:
        """底层 `unitree_go::msg::dds_::MotorCmds_` 的 `cmds` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector

        Returns:
            list[MotorCmd]：字段当前值。

        Examples:
            value = obj.cmds
            # 修改副本后必须回写
            obj.cmds = value
        """
        ...
    @cmds.setter
    def cmds(self, value: Sequence[MotorCmd]) -> None:
        """底层 `unitree_go::msg::dds_::MotorCmds_` 的 `cmds` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.cmds = value
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

class MotorStates:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.go2 import MotorStates
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `MotorStates` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = MotorStates()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: MotorStates_()
        """
        ...
    @property
    def states(self) -> list[MotorState]:
        """底层 `unitree_go::msg::dds_::MotorStates_` 的 `states` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector

        Returns:
            list[MotorState]：字段当前值。

        Examples:
            value = obj.states
            # 修改副本后必须回写
            obj.states = value
        """
        ...
    @states.setter
    def states(self, value: Sequence[MotorState]) -> None:
        """底层 `unitree_go::msg::dds_::MotorStates_` 的 `states` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.states = value
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

class PathPoint:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.go2 import PathPoint
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `PathPoint` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = PathPoint()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: PathPoint_()
        """
        ...
    @property
    def t_from_start(self) -> float:
        """底层 `unitree_go::msg::dds_::PathPoint_` 的 `t_from_start` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.t_from_start
            # 修改副本后必须回写
            obj.t_from_start = value
        """
        ...
    @t_from_start.setter
    def t_from_start(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::PathPoint_` 的 `t_from_start` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.t_from_start = value
        """
        ...
    @property
    def x(self) -> float:
        """底层 `unitree_go::msg::dds_::PathPoint_` 的 `x` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::PathPoint_` 的 `x` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::PathPoint_` 的 `y` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::PathPoint_` 的 `y` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.y = value
        """
        ...
    @property
    def yaw(self) -> float:
        """底层 `unitree_go::msg::dds_::PathPoint_` 的 `yaw` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.yaw
            # 修改副本后必须回写
            obj.yaw = value
        """
        ...
    @yaw.setter
    def yaw(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::PathPoint_` 的 `yaw` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.yaw = value
        """
        ...
    @property
    def vx(self) -> float:
        """底层 `unitree_go::msg::dds_::PathPoint_` 的 `vx` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.vx
            # 修改副本后必须回写
            obj.vx = value
        """
        ...
    @vx.setter
    def vx(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::PathPoint_` 的 `vx` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.vx = value
        """
        ...
    @property
    def vy(self) -> float:
        """底层 `unitree_go::msg::dds_::PathPoint_` 的 `vy` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.vy
            # 修改副本后必须回写
            obj.vy = value
        """
        ...
    @vy.setter
    def vy(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::PathPoint_` 的 `vy` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.vy = value
        """
        ...
    @property
    def vyaw(self) -> float:
        """底层 `unitree_go::msg::dds_::PathPoint_` 的 `vyaw` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.vyaw
            # 修改副本后必须回写
            obj.vyaw = value
        """
        ...
    @vyaw.setter
    def vyaw(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::PathPoint_` 的 `vyaw` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.vyaw = value
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

class Req:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.go2 import Req
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `Req` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = Req()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Req_()
        """
        ...
    @property
    def uuid(self) -> str:
        """底层 `unitree_go::msg::dds_::Req_` 的 `uuid` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

        Returns:
            str：字段当前值。

        Examples:
            value = obj.uuid
            # 修改副本后必须回写
            obj.uuid = value
        """
        ...
    @uuid.setter
    def uuid(self, value: str) -> None:
        """底层 `unitree_go::msg::dds_::Req_` 的 `uuid` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.uuid = value
        """
        ...
    @property
    def body(self) -> str:
        """底层 `unitree_go::msg::dds_::Req_` 的 `body` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

        Returns:
            str：字段当前值。

        Examples:
            value = obj.body
            # 修改副本后必须回写
            obj.body = value
        """
        ...
    @body.setter
    def body(self, value: str) -> None:
        """底层 `unitree_go::msg::dds_::Req_` 的 `body` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.body = value
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

class Res:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.go2 import Res
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `Res` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = Res()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: Res_()
        """
        ...
    @property
    def uuid(self) -> str:
        """底层 `unitree_go::msg::dds_::Res_` 的 `uuid` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

        Returns:
            str：字段当前值。

        Examples:
            value = obj.uuid
            # 修改副本后必须回写
            obj.uuid = value
        """
        ...
    @uuid.setter
    def uuid(self, value: str) -> None:
        """底层 `unitree_go::msg::dds_::Res_` 的 `uuid` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.uuid = value
        """
        ...
    @property
    def data(self) -> list[int]:
        """底层 `unitree_go::msg::dds_::Res_` 的 `data` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector；元素约束：取值范围为 0 到 255。

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
        """底层 `unitree_go::msg::dds_::Res_` 的 `data` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector；元素约束：取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.data = value
        """
        ...
    @property
    def body(self) -> str:
        """底层 `unitree_go::msg::dds_::Res_` 的 `body` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

        Returns:
            str：字段当前值。

        Examples:
            value = obj.body
            # 修改副本后必须回写
            obj.body = value
        """
        ...
    @body.setter
    def body(self, value: str) -> None:
        """底层 `unitree_go::msg::dds_::Res_` 的 `body` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.body = value
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

class SportModeCmd:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.go2 import SportModeCmd
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `SportModeCmd` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = SportModeCmd()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: SportModeCmd_()
        """
        ...
    @property
    def mode(self) -> int:
        """底层 `unitree_go::msg::dds_::SportModeCmd_` 的 `mode` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

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
        """底层 `unitree_go::msg::dds_::SportModeCmd_` 的 `mode` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.mode = value
        """
        ...
    @property
    def gait_type(self) -> int:
        """底层 `unitree_go::msg::dds_::SportModeCmd_` 的 `gait_type` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.gait_type
            # 修改副本后必须回写
            obj.gait_type = value
        """
        ...
    @gait_type.setter
    def gait_type(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::SportModeCmd_` 的 `gait_type` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.gait_type = value
        """
        ...
    @property
    def speed_level(self) -> int:
        """底层 `unitree_go::msg::dds_::SportModeCmd_` 的 `speed_level` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.speed_level
            # 修改副本后必须回写
            obj.speed_level = value
        """
        ...
    @speed_level.setter
    def speed_level(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::SportModeCmd_` 的 `speed_level` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.speed_level = value
        """
        ...
    @property
    def foot_raise_height(self) -> float:
        """底层 `unitree_go::msg::dds_::SportModeCmd_` 的 `foot_raise_height` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.foot_raise_height
            # 修改副本后必须回写
            obj.foot_raise_height = value
        """
        ...
    @foot_raise_height.setter
    def foot_raise_height(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::SportModeCmd_` 的 `foot_raise_height` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.foot_raise_height = value
        """
        ...
    @property
    def body_height(self) -> float:
        """底层 `unitree_go::msg::dds_::SportModeCmd_` 的 `body_height` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.body_height
            # 修改副本后必须回写
            obj.body_height = value
        """
        ...
    @body_height.setter
    def body_height(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::SportModeCmd_` 的 `body_height` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.body_height = value
        """
        ...
    @property
    def position(self) -> list[float]:
        """底层 `unitree_go::msg::dds_::SportModeCmd_` 的 `position` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            list[float]：字段当前值。

        Examples:
            value = obj.position
            # 修改副本后必须回写
            obj.position = value
        """
        ...
    @position.setter
    def position(self, value: Sequence[float]) -> None:
        """底层 `unitree_go::msg::dds_::SportModeCmd_` 的 `position` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.position = value
        """
        ...
    @property
    def euler(self) -> list[float]:
        """底层 `unitree_go::msg::dds_::SportModeCmd_` 的 `euler` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            list[float]：字段当前值。

        Examples:
            value = obj.euler
            # 修改副本后必须回写
            obj.euler = value
        """
        ...
    @euler.setter
    def euler(self, value: Sequence[float]) -> None:
        """底层 `unitree_go::msg::dds_::SportModeCmd_` 的 `euler` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.euler = value
        """
        ...
    @property
    def velocity(self) -> list[float]:
        """底层 `unitree_go::msg::dds_::SportModeCmd_` 的 `velocity` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            list[float]：字段当前值。

        Examples:
            value = obj.velocity
            # 修改副本后必须回写
            obj.velocity = value
        """
        ...
    @velocity.setter
    def velocity(self, value: Sequence[float]) -> None:
        """底层 `unitree_go::msg::dds_::SportModeCmd_` 的 `velocity` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.velocity = value
        """
        ...
    @property
    def yaw_speed(self) -> float:
        """底层 `unitree_go::msg::dds_::SportModeCmd_` 的 `yaw_speed` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.yaw_speed
            # 修改副本后必须回写
            obj.yaw_speed = value
        """
        ...
    @yaw_speed.setter
    def yaw_speed(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::SportModeCmd_` 的 `yaw_speed` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.yaw_speed = value
        """
        ...
    @property
    def bms_cmd(self) -> BmsCmd:
        """底层 `unitree_go::msg::dds_::SportModeCmd_` 的 `bms_cmd` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            BmsCmd：字段当前值。

        Examples:
            value = obj.bms_cmd
            # 修改副本后必须回写
            obj.bms_cmd = value
        """
        ...
    @bms_cmd.setter
    def bms_cmd(self, value: BmsCmd) -> None:
        """底层 `unitree_go::msg::dds_::SportModeCmd_` 的 `bms_cmd` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.bms_cmd = value
        """
        ...
    @property
    def path_point(self) -> list[PathPoint]:
        """底层 `unitree_go::msg::dds_::SportModeCmd_` 的 `path_point` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 30 个元素

        Returns:
            list[PathPoint]：字段当前值。

        Examples:
            value = obj.path_point
            # 修改副本后必须回写
            obj.path_point = value
        """
        ...
    @path_point.setter
    def path_point(self, value: Sequence[PathPoint]) -> None:
        """底层 `unitree_go::msg::dds_::SportModeCmd_` 的 `path_point` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 30 个元素

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.path_point = value
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

class TimeSpec:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.go2 import TimeSpec
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `TimeSpec` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = TimeSpec()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: TimeSpec_()
        """
        ...
    @property
    def sec(self) -> int:
        """底层 `unitree_go::msg::dds_::TimeSpec_` 的 `sec` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 -2147483648 到 2147483647。

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
        """底层 `unitree_go::msg::dds_::TimeSpec_` 的 `sec` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 -2147483648 到 2147483647。

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
        """底层 `unitree_go::msg::dds_::TimeSpec_` 的 `nanosec` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

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
        """底层 `unitree_go::msg::dds_::TimeSpec_` 的 `nanosec` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

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

class SportModeState:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.go2 import SportModeState
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
    def stamp(self) -> TimeSpec:
        """底层 `unitree_go::msg::dds_::SportModeState_` 的 `stamp` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Returns:
            TimeSpec：字段当前值。

        Examples:
            value = obj.stamp
            # 修改副本后必须回写
            obj.stamp = value
        """
        ...
    @stamp.setter
    def stamp(self, value: TimeSpec) -> None:
        """底层 `unitree_go::msg::dds_::SportModeState_` 的 `stamp` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.stamp = value
        """
        ...
    @property
    def error_code(self) -> int:
        """底层 `unitree_go::msg::dds_::SportModeState_` 的 `error_code` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.error_code
            # 修改副本后必须回写
            obj.error_code = value
        """
        ...
    @error_code.setter
    def error_code(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::SportModeState_` 的 `error_code` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 4294967295。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.error_code = value
        """
        ...
    @property
    def imu_state(self) -> IMUState:
        """底层 `unitree_go::msg::dds_::SportModeState_` 的 `imu_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

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
        """底层 `unitree_go::msg::dds_::SportModeState_` 的 `imu_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.imu_state = value
        """
        ...
    @property
    def mode(self) -> int:
        """底层 `unitree_go::msg::dds_::SportModeState_` 的 `mode` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

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
        """底层 `unitree_go::msg::dds_::SportModeState_` 的 `mode` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.mode = value
        """
        ...
    @property
    def progress(self) -> float:
        """底层 `unitree_go::msg::dds_::SportModeState_` 的 `progress` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.progress
            # 修改副本后必须回写
            obj.progress = value
        """
        ...
    @progress.setter
    def progress(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::SportModeState_` 的 `progress` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.progress = value
        """
        ...
    @property
    def gait_type(self) -> int:
        """底层 `unitree_go::msg::dds_::SportModeState_` 的 `gait_type` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.gait_type
            # 修改副本后必须回写
            obj.gait_type = value
        """
        ...
    @gait_type.setter
    def gait_type(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::SportModeState_` 的 `gait_type` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.gait_type = value
        """
        ...
    @property
    def foot_raise_height(self) -> float:
        """底层 `unitree_go::msg::dds_::SportModeState_` 的 `foot_raise_height` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.foot_raise_height
            # 修改副本后必须回写
            obj.foot_raise_height = value
        """
        ...
    @foot_raise_height.setter
    def foot_raise_height(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::SportModeState_` 的 `foot_raise_height` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.foot_raise_height = value
        """
        ...
    @property
    def position(self) -> list[float]:
        """底层 `unitree_go::msg::dds_::SportModeState_` 的 `position` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            list[float]：字段当前值。

        Examples:
            value = obj.position
            # 修改副本后必须回写
            obj.position = value
        """
        ...
    @position.setter
    def position(self, value: Sequence[float]) -> None:
        """底层 `unitree_go::msg::dds_::SportModeState_` 的 `position` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.position = value
        """
        ...
    @property
    def body_height(self) -> float:
        """底层 `unitree_go::msg::dds_::SportModeState_` 的 `body_height` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.body_height
            # 修改副本后必须回写
            obj.body_height = value
        """
        ...
    @body_height.setter
    def body_height(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::SportModeState_` 的 `body_height` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.body_height = value
        """
        ...
    @property
    def velocity(self) -> list[float]:
        """底层 `unitree_go::msg::dds_::SportModeState_` 的 `velocity` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            list[float]：字段当前值。

        Examples:
            value = obj.velocity
            # 修改副本后必须回写
            obj.velocity = value
        """
        ...
    @velocity.setter
    def velocity(self, value: Sequence[float]) -> None:
        """底层 `unitree_go::msg::dds_::SportModeState_` 的 `velocity` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.velocity = value
        """
        ...
    @property
    def yaw_speed(self) -> float:
        """底层 `unitree_go::msg::dds_::SportModeState_` 的 `yaw_speed` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.yaw_speed
            # 修改副本后必须回写
            obj.yaw_speed = value
        """
        ...
    @yaw_speed.setter
    def yaw_speed(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::SportModeState_` 的 `yaw_speed` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.yaw_speed = value
        """
        ...
    @property
    def range_obstacle(self) -> list[float]:
        """底层 `unitree_go::msg::dds_::SportModeState_` 的 `range_obstacle` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            list[float]：字段当前值。

        Examples:
            value = obj.range_obstacle
            # 修改副本后必须回写
            obj.range_obstacle = value
        """
        ...
    @range_obstacle.setter
    def range_obstacle(self, value: Sequence[float]) -> None:
        """底层 `unitree_go::msg::dds_::SportModeState_` 的 `range_obstacle` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.range_obstacle = value
        """
        ...
    @property
    def foot_force(self) -> list[int]:
        """底层 `unitree_go::msg::dds_::SportModeState_` 的 `foot_force` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：取值范围为 -32768 到 32767。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.foot_force
            # 修改副本后必须回写
            obj.foot_force = value
        """
        ...
    @foot_force.setter
    def foot_force(self, value: Sequence[int]) -> None:
        """底层 `unitree_go::msg::dds_::SportModeState_` 的 `foot_force` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 4 个元素；元素约束：取值范围为 -32768 到 32767。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.foot_force = value
        """
        ...
    @property
    def foot_position_body(self) -> list[float]:
        """底层 `unitree_go::msg::dds_::SportModeState_` 的 `foot_position_body` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 12 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            list[float]：字段当前值。

        Examples:
            value = obj.foot_position_body
            # 修改副本后必须回写
            obj.foot_position_body = value
        """
        ...
    @foot_position_body.setter
    def foot_position_body(self, value: Sequence[float]) -> None:
        """底层 `unitree_go::msg::dds_::SportModeState_` 的 `foot_position_body` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 12 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.foot_position_body = value
        """
        ...
    @property
    def foot_speed_body(self) -> list[float]:
        """底层 `unitree_go::msg::dds_::SportModeState_` 的 `foot_speed_body` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 12 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            list[float]：字段当前值。

        Examples:
            value = obj.foot_speed_body
            # 修改副本后必须回写
            obj.foot_speed_body = value
        """
        ...
    @foot_speed_body.setter
    def foot_speed_body(self, value: Sequence[float]) -> None:
        """底层 `unitree_go::msg::dds_::SportModeState_` 的 `foot_speed_body` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 12 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.foot_speed_body = value
        """
        ...
    @property
    def path_point(self) -> list[PathPoint]:
        """底层 `unitree_go::msg::dds_::SportModeState_` 的 `path_point` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 10 个元素

        Returns:
            list[PathPoint]：字段当前值。

        Examples:
            value = obj.path_point
            # 修改副本后必须回写
            obj.path_point = value
        """
        ...
    @path_point.setter
    def path_point(self, value: Sequence[PathPoint]) -> None:
        """底层 `unitree_go::msg::dds_::SportModeState_` 的 `path_point` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 10 个元素

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.path_point = value
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

class UwbState:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.go2 import UwbState
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `UwbState` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = UwbState()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: UwbState_()
        """
        ...
    @property
    def version(self) -> list[int]:
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `version` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 255。

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
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `version` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.version = value
        """
        ...
    @property
    def channel(self) -> int:
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `channel` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.channel
            # 修改副本后必须回写
            obj.channel = value
        """
        ...
    @channel.setter
    def channel(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `channel` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.channel = value
        """
        ...
    @property
    def joy_mode(self) -> int:
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `joy_mode` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.joy_mode
            # 修改副本后必须回写
            obj.joy_mode = value
        """
        ...
    @joy_mode.setter
    def joy_mode(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `joy_mode` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.joy_mode = value
        """
        ...
    @property
    def orientation_est(self) -> float:
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `orientation_est` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.orientation_est
            # 修改副本后必须回写
            obj.orientation_est = value
        """
        ...
    @orientation_est.setter
    def orientation_est(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `orientation_est` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.orientation_est = value
        """
        ...
    @property
    def pitch_est(self) -> float:
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `pitch_est` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.pitch_est
            # 修改副本后必须回写
            obj.pitch_est = value
        """
        ...
    @pitch_est.setter
    def pitch_est(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `pitch_est` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.pitch_est = value
        """
        ...
    @property
    def distance_est(self) -> float:
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `distance_est` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.distance_est
            # 修改副本后必须回写
            obj.distance_est = value
        """
        ...
    @distance_est.setter
    def distance_est(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `distance_est` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.distance_est = value
        """
        ...
    @property
    def yaw_est(self) -> float:
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `yaw_est` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.yaw_est
            # 修改副本后必须回写
            obj.yaw_est = value
        """
        ...
    @yaw_est.setter
    def yaw_est(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `yaw_est` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.yaw_est = value
        """
        ...
    @property
    def tag_roll(self) -> float:
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `tag_roll` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.tag_roll
            # 修改副本后必须回写
            obj.tag_roll = value
        """
        ...
    @tag_roll.setter
    def tag_roll(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `tag_roll` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.tag_roll = value
        """
        ...
    @property
    def tag_pitch(self) -> float:
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `tag_pitch` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.tag_pitch
            # 修改副本后必须回写
            obj.tag_pitch = value
        """
        ...
    @tag_pitch.setter
    def tag_pitch(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `tag_pitch` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.tag_pitch = value
        """
        ...
    @property
    def tag_yaw(self) -> float:
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `tag_yaw` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.tag_yaw
            # 修改副本后必须回写
            obj.tag_yaw = value
        """
        ...
    @tag_yaw.setter
    def tag_yaw(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `tag_yaw` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.tag_yaw = value
        """
        ...
    @property
    def base_roll(self) -> float:
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `base_roll` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.base_roll
            # 修改副本后必须回写
            obj.base_roll = value
        """
        ...
    @base_roll.setter
    def base_roll(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `base_roll` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.base_roll = value
        """
        ...
    @property
    def base_pitch(self) -> float:
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `base_pitch` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.base_pitch
            # 修改副本后必须回写
            obj.base_pitch = value
        """
        ...
    @base_pitch.setter
    def base_pitch(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `base_pitch` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.base_pitch = value
        """
        ...
    @property
    def base_yaw(self) -> float:
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `base_yaw` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.base_yaw
            # 修改副本后必须回写
            obj.base_yaw = value
        """
        ...
    @base_yaw.setter
    def base_yaw(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `base_yaw` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.base_yaw = value
        """
        ...
    @property
    def joystick(self) -> list[float]:
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `joystick` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            list[float]：字段当前值。

        Examples:
            value = obj.joystick
            # 修改副本后必须回写
            obj.joystick = value
        """
        ...
    @joystick.setter
    def joystick(self, value: Sequence[float]) -> None:
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `joystick` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 2 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.joystick = value
        """
        ...
    @property
    def error_state(self) -> int:
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `error_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.error_state
            # 修改副本后必须回写
            obj.error_state = value
        """
        ...
    @error_state.setter
    def error_state(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `error_state` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.error_state = value
        """
        ...
    @property
    def buttons(self) -> int:
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `buttons` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.buttons
            # 修改副本后必须回写
            obj.buttons = value
        """
        ...
    @buttons.setter
    def buttons(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `buttons` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.buttons = value
        """
        ...
    @property
    def enabled_from_app(self) -> int:
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `enabled_from_app` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.enabled_from_app
            # 修改副本后必须回写
            obj.enabled_from_app = value
        """
        ...
    @enabled_from_app.setter
    def enabled_from_app(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::UwbState_` 的 `enabled_from_app` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.enabled_from_app = value
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

class UwbSwitch:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.go2 import UwbSwitch
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `UwbSwitch` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = UwbSwitch()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: UwbSwitch_()
        """
        ...
    @property
    def enabled(self) -> int:
        """底层 `unitree_go::msg::dds_::UwbSwitch_` 的 `enabled` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.enabled
            # 修改副本后必须回写
            obj.enabled = value
        """
        ...
    @enabled.setter
    def enabled(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::UwbSwitch_` 的 `enabled` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 255。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.enabled = value
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

class VoxelMapCompressed:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.go2 import VoxelMapCompressed
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `VoxelMapCompressed` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = VoxelMapCompressed()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: VoxelMapCompressed_()
        """
        ...
    @property
    def stamp(self) -> float:
        """底层 `unitree_go::msg::dds_::VoxelMapCompressed_` 的 `stamp` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.stamp
            # 修改副本后必须回写
            obj.stamp = value
        """
        ...
    @stamp.setter
    def stamp(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::VoxelMapCompressed_` 的 `stamp` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::VoxelMapCompressed_` 的 `frame_id` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

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
        """底层 `unitree_go::msg::dds_::VoxelMapCompressed_` 的 `frame_id` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为字符串；长度、编码和允许值由具体协议决定。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.frame_id = value
        """
        ...
    @property
    def resolution(self) -> float:
        """底层 `unitree_go::msg::dds_::VoxelMapCompressed_` 的 `resolution` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

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
        """底层 `unitree_go::msg::dds_::VoxelMapCompressed_` 的 `resolution` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.resolution = value
        """
        ...
    @property
    def origin(self) -> list[float]:
        """底层 `unitree_go::msg::dds_::VoxelMapCompressed_` 的 `origin` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            list[float]：字段当前值。

        Examples:
            value = obj.origin
            # 修改副本后必须回写
            obj.origin = value
        """
        ...
    @origin.setter
    def origin(self, value: Sequence[float]) -> None:
        """底层 `unitree_go::msg::dds_::VoxelMapCompressed_` 的 `origin` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.origin = value
        """
        ...
    @property
    def width(self) -> list[int]:
        """底层 `unitree_go::msg::dds_::VoxelMapCompressed_` 的 `width` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：取值范围为 0 到 65535。

        Returns:
            list[int]：字段当前值。

        Examples:
            value = obj.width
            # 修改副本后必须回写
            obj.width = value
        """
        ...
    @width.setter
    def width(self, value: Sequence[int]) -> None:
        """底层 `unitree_go::msg::dds_::VoxelMapCompressed_` 的 `width` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是固定长度数组，写入序列必须正好包含 3 个元素；元素约束：取值范围为 0 到 65535。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.width = value
        """
        ...
    @property
    def src_size(self) -> int:
        """底层 `unitree_go::msg::dds_::VoxelMapCompressed_` 的 `src_size` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 18446744073709551615。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.src_size
            # 修改副本后必须回写
            obj.src_size = value
        """
        ...
    @src_size.setter
    def src_size(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::VoxelMapCompressed_` 的 `src_size` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 18446744073709551615。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.src_size = value
        """
        ...
    @property
    def data(self) -> list[int]:
        """底层 `unitree_go::msg::dds_::VoxelMapCompressed_` 的 `data` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector；元素约束：取值范围为 0 到 255。

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
        """底层 `unitree_go::msg::dds_::VoxelMapCompressed_` 的 `data` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层是可变长度 vector；元素约束：取值范围为 0 到 255。

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

class WirelessController:
    """可由 Python 读写的 DDS/IDL 消息值类型。字段采用复制语义。

    导入：from unitree_sdk2_cpp.idl.go2 import WirelessController
    构造可用性：AVAILABLE。
    """
    def __init__(self) -> None:
        """初始化 `WirelessController` 实例。是否能实际构造取决于下方可用性状态。

        可用性：AVAILABLE；分类：VALUE_TYPE。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            无 (None): `__init__` 本身不返回值；调用类对象时，在构造函数可用的前提下得到该类实例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            value = WirelessController()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: WirelessController_()
        """
        ...
    @property
    def lx(self) -> float:
        """底层 `unitree_go::msg::dds_::WirelessController_` 的 `lx` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.lx
            # 修改副本后必须回写
            obj.lx = value
        """
        ...
    @lx.setter
    def lx(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::WirelessController_` 的 `lx` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.lx = value
        """
        ...
    @property
    def ly(self) -> float:
        """底层 `unitree_go::msg::dds_::WirelessController_` 的 `ly` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.ly
            # 修改副本后必须回写
            obj.ly = value
        """
        ...
    @ly.setter
    def ly(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::WirelessController_` 的 `ly` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.ly = value
        """
        ...
    @property
    def rx(self) -> float:
        """底层 `unitree_go::msg::dds_::WirelessController_` 的 `rx` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.rx
            # 修改副本后必须回写
            obj.rx = value
        """
        ...
    @rx.setter
    def rx(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::WirelessController_` 的 `rx` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.rx = value
        """
        ...
    @property
    def ry(self) -> float:
        """底层 `unitree_go::msg::dds_::WirelessController_` 的 `ry` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Returns:
            float：字段当前值。

        Examples:
            value = obj.ry
            # 修改副本后必须回写
            obj.ry = value
        """
        ...
    @ry.setter
    def ry(self, value: float) -> None:
        """底层 `unitree_go::msg::dds_::WirelessController_` 的 `ry` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 底层为浮点数；类型本身不说明单位、坐标系或业务安全范围。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.ry = value
        """
        ...
    @property
    def keys(self) -> int:
        """底层 `unitree_go::msg::dds_::WirelessController_` 的 `keys` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 65535。

        Returns:
            int：字段当前值。

        Examples:
            value = obj.keys
            # 修改副本后必须回写
            obj.keys = value
        """
        ...
    @keys.setter
    def keys(self, value: int) -> None:
        """底层 `unitree_go::msg::dds_::WirelessController_` 的 `keys` 字段。类型签名只说明 Python 表示；单位、数值范围、数组固定长度和枚举含义需查对应 IDL 头文件。 取值范围为 0 到 65535。

        Args:
            value: 写入的新值；固定数组长度必须与 SDK 一致。

        Returns:
            None

        Examples:
            obj.keys = value
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
