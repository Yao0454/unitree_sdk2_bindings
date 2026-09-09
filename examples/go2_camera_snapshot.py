#!/usr/bin/env python3
"""获取一张 Go2 相机图片，保存原始 JPEG 字节；无需 OpenCV。"""

from __future__ import annotations

import argparse
import logging
from pathlib import Path

from unitree_sdk2_cpp import channel
from unitree_sdk2_cpp.robot.go2 import VideoClient


def capture(interface: str, output: Path) -> int:
    ready = False
    try:
        channel.initialize(0, interface)
        ready = True
        client = VideoClient()
        client.set_timeout(5.0)
        client.init()
        status, data = client.get_image_sample()
        if status != 0:
            raise RuntimeError(f"get_image_sample 失败，错误码：{status}")
        image = bytes(data)
        if not image:
            raise ValueError("相机返回了空图片")
        # 返回值是 SDK 编码后的图片字节，不是 RGB 像素数组。
        if not image.startswith(b"\xff\xd8"):
            raise ValueError("相机返回的数据不是 JPEG，请检查固件支持的图片格式")
        # xb 防止覆盖用户已有的照片；父目录需由用户先创建。
        with output.open("xb") as stream:
            stream.write(image)
        return len(image)
    finally:
        if ready:
            channel.release()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-n", "--network", required=True, help="连接 Go2 的网卡名")
    parser.add_argument("-o", "--output", type=Path, default=Path("go2_snapshot.jpg"))
    args = parser.parse_args()
    if args.output.exists():
        parser.error(f"文件已存在，请指定新的 --output：{args.output}")
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    try:
        size = capture(args.network, args.output)
        print(f"已保存 {size} 字节：{args.output.resolve()}")
        return 0
    except KeyboardInterrupt:
        return 130
    except Exception:
        logging.exception("Go2 拍照失败")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
