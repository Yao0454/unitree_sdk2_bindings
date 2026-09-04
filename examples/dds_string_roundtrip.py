#!/usr/bin/env python3
"""Publish and receive a String on a non-robot tutorial DDS topic."""

from __future__ import annotations

import argparse
import logging
import threading
import time
from dataclasses import dataclass

from unitree_sdk2_cpp import channel
from unitree_sdk2_cpp.idl.ros2 import String


logger = logging.getLogger(__name__)
DEFAULT_TOPIC = "tutorial/hello"


@dataclass(frozen=True, slots=True)
class Config:
    interface: str
    domain_id: int
    topic: str
    text: str
    timeout_s: float


class Inbox:
    """Thread-safe hand-off from the DDS callback to the main thread."""

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._ready = threading.Event()
        self._text: str | None = None

    def put(self, text: str) -> None:
        with self._lock:
            self._text = text
            self._ready.set()

    def wait(self, timeout_s: float) -> str | None:
        if not self._ready.wait(timeout_s):
            return None
        with self._lock:
            return self._text


def parse_args() -> Config:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-n", "--network", default="")
    parser.add_argument("--domain-id", type=int, default=0)
    parser.add_argument("--topic", default=DEFAULT_TOPIC)
    parser.add_argument("--text", default="hello from unitree_sdk2_cpp")
    parser.add_argument("--timeout", type=float, default=5.0)
    args = parser.parse_args()

    if args.timeout <= 0:
        parser.error("--timeout must be positive")
    if args.topic.startswith("rt/"):
        parser.error("this tutorial refuses robot rt/* topics")
    return Config(
        interface=args.network,
        domain_id=args.domain_id,
        topic=args.topic,
        text=args.text,
        timeout_s=args.timeout,
    )


def run(config: Config) -> str:
    inbox = Inbox()
    channel_ready = False
    subscriber_ready = False
    publisher_ready = False
    subscriber: channel.ChannelSubscriber[String] | None = None
    publisher: channel.ChannelPublisher[String] | None = None

    def on_message(message: String) -> None:
        try:
            inbox.put(message.data)
        except Exception:
            logger.exception("DDS callback failed")

    try:
        channel.initialize(config.domain_id, config.interface)
        channel_ready = True

        subscriber = channel.ChannelSubscriber(
            config.topic,
            String,
            on_message,
            queue_length=1,
        )
        subscriber.init_channel()
        subscriber_ready = True

        publisher = channel.ChannelPublisher(config.topic, String)
        publisher.init_channel()
        publisher_ready = True

        message = String()
        message.data = config.text

        deadline = time.monotonic() + config.timeout_s
        while time.monotonic() < deadline:
            if not publisher.write(message):
                raise RuntimeError("DDS publisher rejected the message")
            received = inbox.wait(timeout_s=0.2)
            if received is not None:
                return received
        raise TimeoutError(f"no loopback message received on {config.topic!r}")
    finally:
        if publisher is not None and publisher_ready:
            publisher.close_channel()
        if subscriber is not None and subscriber_ready:
            subscriber.close_channel()
        if channel_ready:
            channel.release()


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    try:
        config = parse_args()
        received = run(config)
        print(f"received: {received!r}")
        return 0
    except KeyboardInterrupt:
        logger.info("interrupted")
        return 130
    except Exception:
        logger.exception("DDS roundtrip failed")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
