#!/usr/bin/env python3
"""Smallest example that publishes one default (passive) G1 LowCmd."""

import sys

from unitree_sdk2_cpp import channel
from unitree_sdk2_cpp.idl import g1


def main() -> int:
    interface = sys.argv[1] if len(sys.argv) > 1 else "eth0"
    channel_ready = False
    publisher: channel.ChannelPublisher[g1.LowCmd] | None = None
    publisher_ready = False

    try:
        channel.initialize(0, interface)
        channel_ready = True

        publisher = channel.ChannelPublisher("rt/lowcmd", g1.LowCmd)
        publisher.init_channel()
        publisher_ready = True

        command = g1.LowCmd()
        command.motor_cmd = [g1.MotorCmd() for _ in range(35)]
        g1.update_crc(command)
        print("published:", publisher.write(command))
        return 0
    finally:
        if publisher is not None and publisher_ready:
            publisher.close_channel()
        if channel_ready:
            channel.release()


if __name__ == "__main__":
    raise SystemExit(main())
