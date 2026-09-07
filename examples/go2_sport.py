#!/usr/bin/env python3
"""Execute one Go2 high-level action, or a short velocity command sequence."""

from __future__ import annotations

import argparse
import logging
import math
import time
from dataclasses import dataclass

from unitree_sdk2_cpp import channel
from unitree_sdk2_cpp.robot.go2 import SportClient


@dataclass(frozen=True, slots=True)
class Config:
    interface: str
    action: str
    vx: float
    vy: float
    vyaw: float
    seconds: float


def require_success(status: int, operation: str) -> None:
    if status != 0:
        raise RuntimeError(f"{operation} failed: {status}")


def parse_args() -> Config:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-n", "--network", required=True, help="DDS network interface")
    parser.add_argument("action", choices=("stand-up", "stand-down", "stop", "move"))
    parser.add_argument("--vx", type=float, default=0.0, help="forward speed (m/s)")
    parser.add_argument("--vy", type=float, default=0.0, help="leftward speed (m/s)")
    parser.add_argument("--vyaw", type=float, default=0.0, help="yaw rate (rad/s)")
    parser.add_argument("--seconds", type=float, default=2.0)
    args = parser.parse_args()
    # These are conservative example limits, not the robot's capability limits.
    for name, value, limit in (
        ("vx", args.vx, 0.3), ("vy", args.vy, 0.3), ("vyaw", args.vyaw, 0.5),
    ):
        if not math.isfinite(value) or abs(value) > limit:
            parser.error(f"--{name} must be finite and between {-limit} and {limit}")
    if not math.isfinite(args.seconds) or not 0 < args.seconds <= 10:
        parser.error("--seconds must be finite and in (0, 10]")
    if args.action != "move" and any((args.vx, args.vy, args.vyaw)):
        parser.error("velocity arguments require the move action")
    return Config(args.network, args.action, args.vx, args.vy, args.vyaw, args.seconds)


def run(config: Config) -> None:
    ready = False
    client: SportClient | None = None
    move_attempted = False
    try:
        channel.initialize(0, config.interface)
        ready = True
        client = SportClient()
        client.set_timeout(1.0)
        client.init()

        if config.action == "move":
            deadline = time.monotonic() + config.seconds
            while time.monotonic() < deadline:
                # Even a failed/timed-out request might have reached the robot.
                move_attempted = True
                require_success(client.move(config.vx, config.vy, config.vyaw), "move")
                time.sleep(min(0.02, max(0.0, deadline - time.monotonic())))
        else:
            actions = {
                "stand-up": client.stand_up,
                "stand-down": client.stand_down,
                "stop": client.stop_move,
            }
            require_success(actions[config.action](), config.action)
            print(f"{config.action}: request accepted")
    finally:
        try:
            if move_attempted and client is not None:
                require_success(client.stop_move(), "stop_move during cleanup")
        finally:
            if ready:
                channel.release()


def main() -> int:
    config = parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    try:
        # Do not delay an explicitly requested stop with a confirmation prompt.
        if config.action != "stop":
            print(f"This will command the physical Go2: {config}")
            if input('Type "GO2" to continue: ').strip() != "GO2":
                print("Cancelled")
                return 0
        run(config)
        return 0
    except KeyboardInterrupt:
        return 130
    except Exception:
        logging.exception("Go2 sport command failed")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
