#!/usr/bin/env python3
"""Educational G1 low-level example using the Unitree SDK2 Python binding.

The default mode only subscribes to ``rt/lowstate`` and prints telemetry.  A
real low-level command loop is enabled only with ``--send`` and an interactive
confirmation because it can move a physical robot.

This example is intentionally simple.  Python scheduling is not hard
real-time, so use the C++ SDK for production control loops.
"""

from __future__ import annotations

import argparse
import threading
import time
from dataclasses import dataclass, field

from unitree_sdk2_cpp import channel, robot
from unitree_sdk2_cpp.idl import g1


NUM_G1_MOTORS = 35
LOWCMD_TOPIC = "rt/lowcmd"
LOWSTATE_TOPIC = "rt/lowstate"


@dataclass
class StateStore:
    """Small synchronized hand-off from the DDS callback to the main loop."""

    state: g1.LowState | None = None
    valid_samples: int = 0
    lock: threading.Lock = field(default_factory=threading.Lock)
    ready: threading.Event = field(default_factory=threading.Event)

    def update(self, state: g1.LowState) -> None:
        with self.lock:
            self.state = state
            self.valid_samples += 1
            self.ready.set()

    def snapshot(self) -> g1.LowState | None:
        with self.lock:
            return self.state


def safety_fault(state: g1.LowState) -> str | None:
    """Return the first official G1 safety check that reports a fault."""

    checks = (
        ("bad_orientation", robot.g1.bad_orientation(state)),
        ("joint_vel_out_of_limit", robot.g1.joint_vel_out_of_limit(state)),
        ("ang_vel_out_of_limit", robot.g1.ang_vel_out_of_limit(state)),
        ("motor_winding_overheat", robot.g1.motor_winding_overheat(state)),
        ("motor_casing_overheat", robot.g1.motor_casing_overheat(state)),
    )
    for name, failed in checks:
        if failed:
            return name
    return None


def make_hold_command(state: g1.LowState) -> g1.LowCmd:
    """Build a command that holds the current measured joint positions.

    ``motor_state`` and ``motor_cmd`` are returned by value.  We therefore
    construct and assign a complete 35-element list instead of trying to edit
    ``command.motor_cmd[0]`` in place.
    """

    command = g1.LowCmd()
    command.mode_pr = state.mode_pr
    command.mode_machine = state.mode_machine
    command.reserve = [0, 0, 0, 0]

    motors: list[g1.MotorCmd] = []
    for measured in state.motor_state:
        motor = g1.MotorCmd()
        motor.mode = 1
        motor.q = measured.q
        motor.dq = 0.0
        motor.kp = 20.0
        motor.kd = 0.5
        motor.tau = 0.0
        motor.reserve = 0
        motors.append(motor)

    if len(motors) != NUM_G1_MOTORS:
        raise RuntimeError(
            f"expected {NUM_G1_MOTORS} G1 motors, got {len(motors)}"
        )
    command.motor_cmd = motors
    g1.update_crc(command)
    return command


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--interface",
        default="",
        help="network interface passed to ChannelFactory (for example eth0)",
    )
    parser.add_argument("--domain-id", type=int, default=0)
    parser.add_argument(
        "--seconds",
        type=float,
        default=10.0,
        help="how long to observe or send commands (default: 10)",
    )
    parser.add_argument(
        "--send",
        action="store_true",
        help="send a current-position hold command; this can move the robot",
    )
    parser.add_argument(
        "--period-ms",
        type=float,
        default=2.0,
        help="send-loop period in milliseconds (default: 2; Python is not real-time)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.seconds <= 0:
        raise SystemExit("--seconds must be positive")
    if args.period_ms <= 0:
        raise SystemExit("--period-ms must be positive")

    if args.send:
        print("WARNING: --send enables physical G1 low-level control.")
        print("Keep the robot suspended or otherwise mechanically safe.")
        if input('Type "G1" to continue: ').strip() != "G1":
            print("Cancelled.")
            return 0

    store = StateStore()
    subscriber: channel.ChannelSubscriber[g1.LowState] | None = None
    publisher: channel.ChannelPublisher[g1.LowCmd] | None = None
    client: robot.g1.LocoClient | None = None
    subscriber_initialized = False
    publisher_initialized = False
    channel_initialized = False

    def on_low_state(state: g1.LowState) -> None:
        if not g1.validate_crc(state):
            return
        store.update(state)

    try:
        channel.initialize(args.domain_id, args.interface)
        channel_initialized = True

        subscriber = channel.ChannelSubscriber(
            LOWSTATE_TOPIC, g1.LowState, on_low_state, queue_length=1
        )
        subscriber.init_channel()
        subscriber_initialized = True

        if not store.ready.wait(timeout=5.0):
            raise RuntimeError("no valid G1 LowState received within 5 seconds")

        if args.send:
            publisher = channel.ChannelPublisher(LOWCMD_TOPIC, g1.LowCmd)
            publisher.init_channel()
            publisher_initialized = True

            client = robot.g1.LocoClient()
            client.set_timeout(5.0)
            client.init()
            status, fsm_id = client.get_fsm_id()
            if status != 0:
                raise RuntimeError(f"GetFsmId failed with status {status}")
            print(f"Current G1 FSM id: {fsm_id}")
            status = client.switch_to_user_ctrl()
            if status != 0:
                raise RuntimeError(
                    f"SwitchToUserCtrl failed with status {status}"
                )

        deadline = time.monotonic() + args.seconds
        next_send = time.monotonic()
        last_report = 0.0
        while time.monotonic() < deadline:
            state = store.snapshot()
            if state is None:
                continue

            fault = safety_fault(state)
            if fault is not None:
                raise RuntimeError(f"G1 safety check failed: {fault}")
            if subscriber is None or robot.g1.lost_connection(subscriber, 1000):
                raise RuntimeError("G1 LowState connection lost")

            now = time.monotonic()
            if args.send and now >= next_send:
                command = make_hold_command(state)
                assert publisher is not None
                if not publisher.write(command):
                    raise RuntimeError("failed to publish G1 LowCmd")
                next_send = now + args.period_ms / 1000.0
            elif not args.send and now - last_report >= 1.0:
                imu = state.imu_state
                print(
                    f"tick={state.tick} samples={store.valid_samples} "
                    f"rpy=({imu.rpy[0]:+.3f}, {imu.rpy[1]:+.3f}, {imu.rpy[2]:+.3f})"
                )
                last_report = now
            else:
                time.sleep(0.001)
    finally:
        if client is not None:
            try:
                client.damp()
            except Exception as error:
                print(f"warning: failed to damp G1 during shutdown: {error}")
        if publisher is not None and publisher_initialized:
            publisher.close_channel()
        if subscriber is not None and subscriber_initialized:
            subscriber.close_channel()
        if channel_initialized:
            channel.release()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
