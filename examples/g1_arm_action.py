#!/usr/bin/env python3
"""List, execute, or stop G1 arm actions through the SDK2 Python binding."""

from __future__ import annotations

import argparse
import sys
from typing import Protocol, cast

from unitree_sdk2_cpp import channel
from unitree_sdk2_cpp.robot.g1 import G1ArmActionClient


ARM_ACTION_ERRORS = {
    7400: "The topic rt/armsdk is occupied.",
    7401: (
        "The arm is holding. Expecting release action (99) or the same last "
        "action id."
    ),
    7402: "Invalid action id.",
    7404: (
        "The actions are only supported in FSM IDs {500, 501, 801}.\n"
        "Subscribe to rt/sportmodestate to check the current FSM ID.\n"
        "In FSM 801, actions are supported only in FSM modes {0, 3}.\n"
        "If this error is still returned in a supported state, ignore the action."
    ),
}


class Arguments(Protocol):
    network: str
    list_actions: bool
    action_id: int | None
    action_name: str | None
    yes: bool


def parse_args() -> Arguments:
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.add_argument(
        "-n",
        "--network",
        default="",
        help="DDS network interface, for example eth0",
    )

    operation = parser.add_mutually_exclusive_group(required=True)
    _ = operation.add_argument(
        "-l",
        "--list",
        dest="list_actions",
        action="store_true",
        help="list all supported actions",
    )
    _ = operation.add_argument(
        "-i",
        "--id",
        dest="action_id",
        type=int,
        help="predefined action ID to execute; 0 lists all actions",
    )
    _ = operation.add_argument(
        "--name",
        dest="action_name",
        help="custom action name to execute",
    )
    _ = operation.add_argument(
        "--stop",
        action="store_true",
        help="stop the current custom action",
    )
    _ = parser.add_argument(
        "--yes",
        action="store_true",
        help="execute an action without the interactive safety confirmation",
    )
    return cast(Arguments, cast(object, parser.parse_args()))


def report_error(operation: str, status: int) -> int:
    message = ARM_ACTION_ERRORS.get(status, f"Unknown error code: {status}")
    print(f"{operation} failed ({status}): {message}", file=sys.stderr)
    return 1


def confirm_motion(args: Arguments) -> bool:
    if (
        args.yes
        or args.list_actions
        or args.action_id == 0
        or (args.action_id is None and args.action_name is None)
    ):
        return True

    action = (
        f"action ID {args.action_id}"
        if args.action_id is not None
        else f"custom action {args.action_name!r}"
    )
    print(f"WARNING: this will command the physical G1 to execute {action}.")
    return input('Type "G1" to continue: ').strip() == "G1"


def main() -> int:
    args = parse_args()
    if not confirm_motion(args):
        print("Cancelled.")
        return 0

    channel_initialized = False
    try:
        channel.initialize(0, args.network)
        channel_initialized = True

        client = G1ArmActionClient()
        client.init()
        # Built-in actions finish within 10 seconds. Increase this timeout if a
        # custom action is expected to run longer.
        client.set_timeout(10.0)

        if args.list_actions or args.action_id == 0:
            status, action_list = client.get_action_list()
            if status != 0:
                return report_error("Get action list", status)
            print("Available actions:")
            print(action_list)
            return 0

        if args.action_id is not None:
            status = client.execute_action(args.action_id)
            return 0 if status == 0 else report_error("Execute action", status)

        if args.action_name is not None:
            status = client.execute_action(args.action_name)
            return (
                0
                if status == 0
                else report_error("Execute custom action", status)
            )

        status = client.stop_custom_action()
        return 0 if status == 0 else report_error("Stop custom action", status)
    finally:
        if channel_initialized:
            channel.release()


if __name__ == "__main__":
    raise SystemExit(main())
