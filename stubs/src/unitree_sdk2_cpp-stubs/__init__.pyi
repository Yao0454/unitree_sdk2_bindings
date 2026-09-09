"""Unitree SDK2 extension API signature preview."""
from . import channel as channel
from . import idl as idl
from . import robot as robot

__all__ = ["channel", "idl", "robot", "OsHelper"]

class OsHelper:
    """读取当前主机操作系统信息的单例辅助类。

    导入：from unitree_sdk2_cpp import OsHelper
    """
    @staticmethod
    def instance() -> OsHelper:
        """返回进程内的 `OsHelper` 单例。

        可用性：AVAILABLE；分类：READ_ONLY。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (OsHelper): 进程内的 `OsHelper` 单例。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            helper = OsHelper.instance()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: OsHelper::Instance()
        """
        ...
    def get_uid(self) -> int:
        """返回当前进程用户的 Unix UID。

        可用性：AVAILABLE；分类：READ_ONLY。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (int): 当前进程用户的 Unix UID。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            uid = helper.get_uid()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: OsHelper::GetUID()
        """
        ...
    def get_gid(self) -> int:
        """返回当前进程用户的 Unix GID。

        可用性：AVAILABLE；分类：READ_ONLY。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (int): 当前进程用户的 Unix GID。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            gid = helper.get_gid()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: OsHelper::GetGID()
        """
        ...
    def get_user(self) -> str:
        """返回当前进程对应的用户名。

        可用性：AVAILABLE；分类：READ_ONLY。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (str): 当前进程对应的用户名。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            user = helper.get_user()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: OsHelper::GetUser()
        """
        ...
    def get_processor_number(self) -> int:
        """返回当前主机可见的处理器数量。

        可用性：AVAILABLE；分类：READ_ONLY。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (int): 当前主机可见的处理器数量。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            processor_count = helper.get_processor_number()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: OsHelper::GetProcessorNumber()
        """
        ...
    def get_page_size(self) -> int:
        """返回当前主机的操作系统内存页大小。

        可用性：AVAILABLE；分类：READ_ONLY。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (int): 操作系统内存页大小，单位为字节。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            page_size = helper.get_page_size()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: OsHelper::GetPageSize()
        """
        ...
    def get_hostname(self) -> str:
        """返回当前主机名。

        可用性：AVAILABLE；分类：READ_ONLY。

        Args:
            无显式参数；实例方法的 self 由 Python 自动传入。

        Returns:
            返回值 (str): 当前主机名。

        Examples:
            用法片段；obj/client 和参数变量需先按业务准备。

            ```python
            hostname = helper.get_hostname()
            ```

        Notes:
            stub 提供类型和文档；执行此接口仍需要已安装的原生扩展。
            C++: OsHelper::GetHostname()
        """
        ...
