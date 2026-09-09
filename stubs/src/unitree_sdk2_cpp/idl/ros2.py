"""Generated source companion. Full types and Chinese help are in the PEP 561 stubs.
Robot APIs are provided exclusively by the separately installed native extension.
"""
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    class Time:
        pass

    class Header:
        pass

    class Quaternion:
        pass

    class Vector3:
        pass

    class Imu:
        pass

    class Point:
        pass

    class Pose:
        pass

    class MapMetaData:
        pass

    class OccupancyGrid:
        pass

    class PoseWithCovariance:
        pass

    class Twist:
        pass

    class TwistWithCovariance:
        pass

    class Odometry:
        pass

    class Point32:
        pass

    class PointField:
        pass

    class PointCloud2:
        pass

    class PointStamped:
        pass

    class Pose2D:
        pass

    class PoseStamped:
        pass

    class PoseWithCovarianceStamped:
        pass

    class QuaternionStamped:
        pass

    class String:
        pass

    class TwistStamped:
        pass

    class TwistWithCovarianceStamped:
        pass

if not TYPE_CHECKING:
    raise ImportError("This source companion has no runtime API; install unitree-sdk2-cpp.")
