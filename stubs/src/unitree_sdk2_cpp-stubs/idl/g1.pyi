"""G1-friendly aliases for the unitree_hg DDS message types."""
from typing import overload

from .hg import (
    AgvBmsState as AgvBmsState,
    BmsCmd as BmsCmd,
    BmsState as BmsState,
    MotorCmd as MotorCmd,
    HandCmd as HandCmd,
    IMUState as IMUState,
    MotorState as MotorState,
    PressSensorState as PressSensorState,
    HandState as HandState,
    LowCmd as LowCmd,
    LowState as LowState,
    MainBoardState as MainBoardState,
    SportModeState as SportModeState,
)

@overload
def compute_crc(message: LowCmd) -> int:
    """计算 G1 消息的 CRC，不修改消息。

    可用性：AVAILABLE；分类：VALUE_TYPE。

    Args:
        message: 要写入 DDS 的消息实例；类型必须与 Publisher 构造时声明的消息类完全一致。

    Returns:
        返回值 (int): 返回 `int`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

    Examples:
        用法片段；obj/client 和参数变量需先按业务准备。

        ```python
        checksum = compute_crc(message)
        ```

    Notes:
        stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
        C++: crc32_core(LowCmd_)
    """
    ...
@overload
def compute_crc(message: LowState) -> int:
    """计算 G1 消息的 CRC，不修改消息。

    可用性：AVAILABLE；分类：VALUE_TYPE。

    Args:
        message: 要写入 DDS 的消息实例；类型必须与 Publisher 构造时声明的消息类完全一致。

    Returns:
        返回值 (int): 返回 `int`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

    Examples:
        用法片段；obj/client 和参数变量需先按业务准备。

        ```python
        checksum = compute_crc(message)
        ```

    Notes:
        stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
        C++: crc32_core(LowState_)
    """
    ...
def update_crc(message: LowCmd) -> int:
    """计算并回写 G1 LowCmd.crc，返回新的 CRC。修改字段后应重新计算。

    可用性：AVAILABLE；分类：VALUE_TYPE。

    Args:
        message: 要写入 DDS 的消息实例；类型必须与 Publisher 构造时声明的消息类完全一致。

    Returns:
        返回值 (int): 返回 `int`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

    Examples:
        用法片段；obj/client 和参数变量需先按业务准备。

        ```python
        checksum = update_crc(command)
        assert command.crc == checksum
        ```

    Notes:
        stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
        C++: crc32_core(LowCmd_); LowCmd_::crc(uint32_t)
    """
    ...
@overload
def validate_crc(message: LowCmd) -> bool:
    """比较 G1 消息内容与 crc 字段是否匹配；不等价于运动安全检查。

    可用性：AVAILABLE；分类：VALUE_TYPE。

    Args:
        message: 要写入 DDS 的消息实例；类型必须与 Publisher 构造时声明的消息类完全一致。

    Returns:
        返回值 (bool): 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

    Examples:
        用法片段；obj/client 和参数变量需先按业务准备。

        ```python
        valid = validate_crc(message)
        ```

    Notes:
        stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
        C++: LowCmd_::crc() == crc32_core(LowCmd_)
    """
    ...
@overload
def validate_crc(message: LowState) -> bool:
    """比较 G1 消息内容与 crc 字段是否匹配；不等价于运动安全检查。

    可用性：AVAILABLE；分类：VALUE_TYPE。

    Args:
        message: 要写入 DDS 的消息实例；类型必须与 Publisher 构造时声明的消息类完全一致。

    Returns:
        返回值 (bool): 返回 `bool`。更精确的业务含义见该方法用途、C++ 签名和目标型号协议。

    Examples:
        用法片段；obj/client 和参数变量需先按业务准备。

        ```python
        valid = validate_crc(message)
        ```

    Notes:
        stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
        C++: LowState_::crc() == crc32_core(LowState_)
    """
    ...
