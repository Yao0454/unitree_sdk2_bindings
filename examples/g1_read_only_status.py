#!/usr/bin/env python3
"""Query read-only G1 locomotion status with a production-style lifecycle."""

from __future__ import annotations

import argparse
import logging
from dataclasses import dataclass
from typing import TypeVar

from unitree_sdk2_cpp import channel
from unitree_sdk2_cpp.robot.g1 import LocoClient


logger = logging.getLogger(__name__)
ValueT = TypeVar("ValueT")


class SdkStatusError(RuntimeError):
    def __init__(self, operation: str, status: int) -> None:
        super().__init__(f"{operation} failed with status {status}")
        self.operation = operation
        self.status = status


@dataclass(frozen=True, slots=True)
class Config:
    interface: str
    domain_id: int
    timeout_s: float


@dataclass(frozen=True, slots=True)
class G1Status:
    fsm_id: int
    fsm_mode: int
    balance_mode: int
    stand_height_m: float


def require_value(result: tuple[int, ValueT], operation: str) -> ValueT:
    status, value = result
    if status != 0:
        raise SdkStatusError(operation, status)
    return value


def parse_args() -> Config:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-n", "--network", default="")
    parser.add_argument("--domain-id", type=int, default=0)
    parser.add_argument("--timeout", type=float, default=5.0)
    args = parser.parse_args()

    if args.timeout <= 0:
        parser.error("--timeout must be positive")
    return Config(args.network, args.domain_id, args.timeout)


def query_status(client: LocoClient) -> G1Status:
    return G1Status(
        fsm_id=require_value(client.get_fsm_id(), "get FSM ID"),
        fsm_mode=require_value(client.get_fsm_mode(), "get FSM mode"),
        balance_mode=require_value(
            client.get_balance_mode(),
            "get balance mode",
        ),
        stand_height_m=require_value(
            client.get_stand_height(),
            "get stand height",
        ),
    )


def run(config: Config) -> G1Status:
    channel_ready = False
    try:
        channel.initialize(config.domain_id, config.interface)
        channel_ready = True

        client = LocoClient()
        client.init()
        client.set_timeout(config.timeout_s)
        return query_status(client)
    finally:
        if channel_ready:
            channel.release()


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    try:
        status = run(parse_args())
        print(f"fsm_id: {status.fsm_id}")
        print(f"fsm_mode: {status.fsm_mode}")
        print(f"balance_mode: {status.balance_mode}")
        print(f"stand_height: {status.stand_height_m:.3f} m")
        return 0
    except KeyboardInterrupt:
        logger.info("interrupted")
        return 130
    except SdkStatusError as error:
        logger.error("%s", error)
        return 1
    except Exception:
        logger.exception("unexpected G1 query failure")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
