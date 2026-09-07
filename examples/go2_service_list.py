#!/usr/bin/env python3
"""List Go2 services without changing their state."""

from __future__ import annotations

import argparse
import logging

from unitree_sdk2_cpp import channel
from unitree_sdk2_cpp.robot.go2 import RobotStateClient


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-n", "--network", required=True, help="DDS network interface")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    ready = False
    try:
        channel.initialize(0, args.network)
        ready = True
        client = RobotStateClient()
        client.set_timeout(5.0)
        client.init()

        status, services = client.service_list()
        if status != 0:
            raise RuntimeError(f"service_list failed: {status}")
        print(f"{'SERVICE':<32} {'STATUS':>8} {'PROTECT':>8}")
        for service in services:
            print(f"{service.name:<32} {service.status:>8} {service.protect:>8}")
        return 0
    except KeyboardInterrupt:
        return 130
    except Exception:
        logging.exception("Go2 service query failed")
        return 1
    finally:
        if ready:
            channel.release()


if __name__ == "__main__":
    raise SystemExit(main())
