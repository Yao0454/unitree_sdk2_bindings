#!/usr/bin/env python3
"""显式设置 Go2 音量或灯光亮度，并回读当前值。"""

from __future__ import annotations

import argparse
import logging

from unitree_sdk2_cpp import channel
from unitree_sdk2_cpp.robot.go2 import VuiClient


def set_and_read(interface: str, setting: str, level: int) -> int:
    ready = False
    try:
        channel.initialize(0, interface)
        ready = True
        client = VuiClient()
        client.set_timeout(5.0)
        client.init()
        if setting == "volume":
            status = client.set_volume(level)
        elif setting == "brightness":
            status = client.set_brightness(level)
        else:
            raise ValueError(f"未知设置：{setting}")
        if status != 0:
            raise RuntimeError(f"设置 {setting} 失败，错误码：{status}")
        status, actual = (
            client.get_volume() if setting == "volume" else client.get_brightness()
        )
        if status != 0:
            raise RuntimeError(f"设置已被接受，但回读 {setting} 失败，错误码：{status}")
        return actual
    finally:
        if ready:
            channel.release()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-n", "--network", required=True, help="连接 Go2 的网卡名")
    parser.add_argument("setting", choices=("volume", "brightness"))
    parser.add_argument("level", type=int, choices=range(11), help="等级 0 到 10")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    try:
        actual = set_and_read(args.network, args.setting, args.level)
        print(f"{args.setting}: 请求值={args.level}，回读值={actual}")
        if actual != args.level:
            logging.warning("回读值与请求值不同，请检查固件支持范围或其他控制程序")
        return 0
    except KeyboardInterrupt:
        return 130
    except Exception:
        logging.exception("Go2 VUI 设置失败")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
