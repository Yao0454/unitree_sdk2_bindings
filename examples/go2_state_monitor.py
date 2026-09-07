#!/usr/bin/env python3
"""Subscribe to Go2 rt/sportmodestate without sending motion commands."""

from __future__ import annotations

import argparse
import logging
import math
import threading
import time
from dataclasses import dataclass

from unitree_sdk2_cpp import channel
from unitree_sdk2_cpp.idl.go2 import SportModeState


@dataclass(frozen=True, slots=True)
class Snapshot:
    mode: int
    gait_type: int
    position: tuple[float, ...]
    velocity: tuple[float, ...]
    rpy: tuple[float, ...]
    received_at: float


def monitor(interface: str, seconds: float) -> None:
    lock = threading.Lock()
    first_message = threading.Event()
    latest: Snapshot | None = None

    def on_state(message: SportModeState) -> None:
        nonlocal latest
        try:
            # Copy DDS values into an immutable snapshot owned by this program.
            snapshot = Snapshot(
                message.mode, message.gait_type,
                tuple(message.position), tuple(message.velocity),
                tuple(message.imu_state.rpy), time.monotonic(),
            )
            with lock:
                latest = snapshot
            first_message.set()
        except Exception:
            logging.exception("Go2 state callback failed")

    ready = False
    subscriber: channel.ChannelSubscriber[SportModeState] | None = None
    try:
        channel.initialize(0, interface)
        ready = True
        subscriber = channel.ChannelSubscriber(
            "rt/sportmodestate", SportModeState, on_state, queue_length=1,
        )
        subscriber.init_channel()
        if not first_message.wait(5.0):
            raise TimeoutError("no Go2 sport state received within 5 seconds")

        deadline = time.monotonic() + seconds
        while time.monotonic() < deadline:
            with lock:
                snapshot = latest
            if snapshot is not None:
                age = time.monotonic() - snapshot.received_at
                if age > 2.0:
                    raise TimeoutError("Go2 sport state stream stopped")
                print(
                    f"mode={snapshot.mode} gait={snapshot.gait_type} "
                    f"position_m={snapshot.position} "
                    f"velocity_m_s={snapshot.velocity} "
                    f"rpy_rad={snapshot.rpy} age_s={age:.3f}"
                )
            time.sleep(min(0.5, max(0.0, deadline - time.monotonic())))
    finally:
        try:
            if subscriber is not None:
                subscriber.close_channel()
        finally:
            if ready:
                channel.release()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-n", "--network", required=True, help="DDS network interface")
    parser.add_argument("--seconds", type=float, default=10.0)
    args = parser.parse_args()
    if not math.isfinite(args.seconds) or args.seconds <= 0:
        parser.error("--seconds must be finite and positive")
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    try:
        monitor(args.network, args.seconds)
        return 0
    except KeyboardInterrupt:
        return 130
    except Exception:
        logging.exception("Go2 state monitor failed")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
