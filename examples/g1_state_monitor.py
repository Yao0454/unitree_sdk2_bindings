#!/usr/bin/env python3
"""Monitor G1 LowState using a small immutable application snapshot."""

from __future__ import annotations

import argparse
import logging
import threading
import time
from dataclasses import dataclass

from unitree_sdk2_cpp import channel
from unitree_sdk2_cpp.idl import g1
from unitree_sdk2_cpp.robot import g1 as g1_robot

logger = logging.getLogger(__name__)
LOWSTATE_TOPIC = "rt/lowstate"


@dataclass(frozen=True, slots=True)
class Config:
    interface: str
    domain_id: int
    duration_s: float
    report_period_s: float


@dataclass(frozen=True, slots=True)
class G1Snapshot:
    tick: int
    mode_pr: int
    mode_machine: int
    roll_rad: float
    pitch_rad: float
    yaw_rad: float
    received_at_s: float


class LatestState:
    """Owns the synchronization between the DDS and main threads."""

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._ready = threading.Event()
        self._snapshot: G1Snapshot | None = None

    def update(self, snapshot: G1Snapshot) -> None:
        with self._lock:
            self._snapshot = snapshot
            self._ready.set()

    def wait_until_ready(self, timeout_s: float) -> bool:
        return self._ready.wait(timeout_s)

    def get(self) -> G1Snapshot | None:
        with self._lock:
            return self._snapshot


def parse_args() -> Config:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-n", "--network", default="")
    parser.add_argument("--domain-id", type=int, default=0)
    parser.add_argument("--seconds", type=float, default=10.0)
    parser.add_argument("--report-period", type=float, default=1.0)
    args = parser.parse_args()

    if args.seconds <= 0:
        parser.error("--seconds must be positive")
    if args.report_period <= 0:
        parser.error("--report-period must be positive")
    return Config(
        interface=args.network,
        domain_id=args.domain_id,
        duration_s=args.seconds,
        report_period_s=args.report_period,
    )


def make_snapshot(message: g1.LowState) -> G1Snapshot:
    rpy = message.imu_state.rpy
    if len(rpy) != 3:
        raise ValueError(f"expected three RPY values, got {len(rpy)}")
    return G1Snapshot(
        tick=message.tick,
        mode_pr=message.mode_pr,
        mode_machine=message.mode_machine,
        roll_rad=rpy[0],
        pitch_rad=rpy[1],
        yaw_rad=rpy[2],
        received_at_s=time.monotonic(),
    )


def run(config: Config) -> None:
    latest = LatestState()
    channel_ready = False
    subscriber_ready = False
    subscriber: channel.ChannelSubscriber[g1.LowState] | None = None

    def on_low_state(message: g1.LowState) -> None:
        try:
            if not g1.validate_crc(message):
                return
            latest.update(make_snapshot(message))
        except Exception:
            logger.exception("LowState callback failed")

    try:
        channel.initialize(config.domain_id, config.interface)
        channel_ready = True

        subscriber = channel.ChannelSubscriber(
            LOWSTATE_TOPIC,
            g1.LowState,
            on_low_state,
            queue_length=1,
        )
        subscriber.init_channel()
        subscriber_ready = True

        if not latest.wait_until_ready(timeout_s=5.0):
            raise TimeoutError("no valid G1 LowState received within 5 seconds")

        deadline = time.monotonic() + config.duration_s
        next_report = time.monotonic()
        while (now := time.monotonic()) < deadline:
            if g1_robot.lost_connection(subscriber, timeout_ms=1000):
                raise ConnectionError("G1 LowState connection lost")

            if now >= next_report:
                snapshot = latest.get()
                if snapshot is not None:
                    age_s = now - snapshot.received_at_s
                    print(
                        f"tick={snapshot.tick} "
                        f"mode=({snapshot.mode_pr}, {snapshot.mode_machine}) "
                        f"rpy=({snapshot.roll_rad:+.3f}, "
                        f"{snapshot.pitch_rad:+.3f}, "
                        f"{snapshot.yaw_rad:+.3f}) "
                        f"age={age_s:.3f}s"
                    )
                next_report = now + config.report_period_s

            # Check connection health at least ten times per second, even when
            # status output is configured to be much less frequent.
            time.sleep(min(0.1, max(0.0, deadline - now)))
    finally:
        if subscriber is not None and subscriber_ready:
            subscriber.close_channel()
        if channel_ready:
            channel.release()


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    try:
        run(parse_args())
        return 0
    except KeyboardInterrupt:
        logger.info("interrupted")
        return 130
    except Exception:
        logger.exception("G1 state monitor failed")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
