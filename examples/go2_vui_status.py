#!/usr/bin/env python3
"""Read Go2 voice switch, volume, and light brightness."""

from __future__ import annotations

import argparse
import logging

from unitree_sdk2_cpp import channel
from unitree_sdk2_cpp.robot.go2 import VuiClient


def require_value(result: tuple[int, int], operation: str) -> int:
    status, value = result
    if status != 0:
        raise RuntimeError(f"{operation} failed: {status}")
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-n", "--network", required=True, help="DDS network interface")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    ready = False
    try:
        channel.initialize(0, args.network)
        ready = True
        client = VuiClient()
        client.set_timeout(5.0)
        client.init()

        print("voice_switch:", require_value(client.get_switch(), "get_switch"))
        print("volume:", require_value(client.get_volume(), "get_volume"))
        print("brightness:", require_value(client.get_brightness(), "get_brightness"))
        return 0
    except KeyboardInterrupt:
        return 130
    except Exception:
        logging.exception("Go2 VUI query failed")
        return 1
    finally:
        if ready:
            channel.release()


if __name__ == "__main__":
    raise SystemExit(main())
