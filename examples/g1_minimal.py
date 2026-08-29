#!/usr/bin/env python3
"""Smallest example that publishes one default (passive) G1 LowCmd."""

import sys

from unitree_sdk2_cpp import channel
from unitree_sdk2_cpp.idl import g1


interface = sys.argv[1] if len(sys.argv) > 1 else "eth0"

channel.initialize(0, interface)
publisher = channel.ChannelPublisher("rt/lowcmd", g1.LowCmd)
publisher.init_channel()

command = g1.LowCmd()
command.motor_cmd = [g1.MotorCmd() for _ in range(35)]
g1.update_crc(command)
print("published:", publisher.write(command))

publisher.close_channel()
channel.release()
