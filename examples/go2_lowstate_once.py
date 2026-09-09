#!/usr/bin/env python3
"""读取一条 Go2 底层状态，打印电量、姿态和关节状态；不发送控制命令。"""

from __future__ import annotations

import argparse
import json
import logging
import threading
from dataclasses import asdict, dataclass

from unitree_sdk2_cpp import channel
from unitree_sdk2_cpp.idl.go2 import LowState


@dataclass(frozen=True, slots=True)
class JointState:
    position_rad: float
    velocity_rad_s: float
    estimated_torque_nm: float
    temperature_c: int


@dataclass(frozen=True, slots=True)
class Snapshot:
    tick: int
    battery_percent: int
    rpy_rad: tuple[float, ...]
    joints: tuple[JointState, ...]


def make_snapshot(message: LowState) -> Snapshot:
    return Snapshot(
        tick=message.tick,
        battery_percent=message.bms_state.soc,
        rpy_rad=tuple(message.imu_state.rpy),
        joints=tuple(
            JointState(m.q, m.dq, m.tau_est, m.temperature)
            for m in message.motor_state[:12]
        ),
    )


def read_once(interface: str) -> Snapshot:
    received = threading.Event()
    lock = threading.Lock()
    snapshot: Snapshot | None = None
    subscriber: channel.ChannelSubscriber[LowState] | None = None
    ready = False

    def on_state(message: LowState) -> None:
        nonlocal snapshot
        try:
            with lock:
                if snapshot is None:
                    snapshot = make_snapshot(message)
                    received.set()
        except Exception:
            logging.exception("转换 Go2 底层状态失败")

    try:
        channel.initialize(0, interface)
        ready = True
        subscriber = channel.ChannelSubscriber("rt/lowstate", LowState, on_state, queue_length=1)
        subscriber.init_channel()
        if not received.wait(5.0):
            raise TimeoutError("5 秒内未收到 rt/lowstate，请检查网卡和机器人连接")
        with lock:
            assert snapshot is not None
            return snapshot
    finally:
        try:
            if subscriber is not None:
                subscriber.close_channel()
        finally:
            if ready:
                channel.release()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-n", "--network", required=True, help="连接 Go2 的网卡名")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    try:
        print(json.dumps(asdict(read_once(args.network)), indent=2, ensure_ascii=False))
        return 0
    except KeyboardInterrupt:
        return 130
    except Exception:
        logging.exception("读取 Go2 底层状态失败")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
