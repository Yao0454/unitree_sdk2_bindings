#!/usr/bin/env python3
"""Verify that an installed stub wheel produces a BasedPyright auto import."""

from __future__ import annotations

import argparse
import json
import os
import selectors
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, BinaryIO


JsonObject = dict[str, Any]


def send_message(stream: BinaryIO, message: JsonObject) -> None:
    payload = json.dumps(message, separators=(",", ":")).encode()
    stream.write(f"Content-Length: {len(payload)}\r\n\r\n".encode() + payload)
    stream.flush()


def read_message(stream: BinaryIO, timeout_s: float) -> JsonObject:
    # Popen uses unbuffered pipes below: select() must observe the same bytes
    # that read() consumes, not miss messages prefetched by BufferedReader.
    deadline = time.monotonic() + timeout_s
    with selectors.DefaultSelector() as selector:
        selector.register(stream, selectors.EVENT_READ)

        def read_bytes(count: int) -> bytes:
            remaining = deadline - time.monotonic()
            if remaining <= 0 or not selector.select(remaining):
                raise TimeoutError("timed out waiting for BasedPyright")
            data = stream.read(count)
            if not data:
                raise RuntimeError("BasedPyright closed its output stream")
            return data

        header = bytearray()
        while not header.endswith(b"\r\n\r\n"):
            header.extend(read_bytes(1))
        headers = dict(line.decode().split(":", 1) for line in header.split(b"\r\n") if line)
        length = int(next(v for k, v in headers.items() if k.lower() == "content-length"))
        payload = bytearray()
        while len(payload) < length:
            payload.extend(read_bytes(length - len(payload)))
        return json.loads(payload)


def configuration_for(section: str | None, python_path: Path) -> JsonObject:
    if section == "python":
        return {"pythonPath": str(python_path)}
    if section == "basedpyright":
        return {
            "analysis": {
                "autoImportCompletions": True,
                "indexing": True,
            }
        }
    if section == "python.analysis":
        return {
            "autoImportCompletions": True,
            "indexing": True,
        }
    return {}


def answer_server_request(
    process: subprocess.Popen[bytes],
    message: JsonObject,
    python_path: Path,
    verbose: bool,
) -> None:
    if "id" not in message or "method" not in message:
        return
    method = message["method"]
    result: Any = None
    if method == "workspace/configuration":
        items = message.get("params", {}).get("items", [])
        result = [
            configuration_for(item.get("section"), python_path) for item in items
        ]
    elif method == "workspace/workspaceFolders":
        result = []

    assert process.stdin is not None
    if verbose:
        print(
            f"server request: {method} {message.get('params')} -> {result}",
            file=sys.stderr,
        )
    send_message(
        process.stdin,
        {"jsonrpc": "2.0", "id": message["id"], "result": result},
    )


def wait_for_response(
    process: subprocess.Popen[bytes],
    request_id: int,
    python_path: Path,
    verbose: bool,
    timeout_s: float = 120.0,
) -> JsonObject:
    assert process.stdout is not None
    deadline = time.monotonic() + timeout_s
    while True:
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise TimeoutError(f"no response for LSP request {request_id}")
        message = read_message(process.stdout, remaining)
        if verbose and message.get("method") in {
            "window/logMessage",
            "window/showMessage",
        }:
            print(message, file=sys.stderr)
        if message.get("id") == request_id and "method" not in message:
            return message
        answer_server_request(process, message, python_path, verbose)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--server", type=Path, required=True)
    parser.add_argument("--python", type=Path, required=True)
    parser.add_argument("--project", type=Path, required=True)
    parser.add_argument("--symbol", default="G1ArmActionClient")
    parser.add_argument("--module", default="unitree_sdk2_cpp.robot.g1")
    parser.add_argument("--settle-seconds", type=float, default=10.0)
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--hover", action="store_true", help="Verify Chinese hover docs for Go2 move")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    project = args.project.resolve()
    # Keep the virtual-environment entry path. Resolving this symlink would
    # point at the base interpreter and make the language server inspect the
    # wrong site-packages directory.
    python_path = args.python.absolute()
    server = args.server.resolve()
    probe_uri = (project / "completion_probe.py").as_uri()
    prefix = args.symbol[:-3]
    document = (
        "from unitree_sdk2_cpp.robot.go2 import SportClient\n"
        "client = SportClient()\nclient.move(0.1, 0.0, 0.0)\n"
        if args.hover else prefix
    )

    environment = os.environ.copy()
    environment["VIRTUAL_ENV"] = str(python_path.parent.parent)
    environment["PATH"] = f"{python_path.parent}{os.pathsep}{environment['PATH']}"
    process = subprocess.Popen(
        [str(server), "--stdio"],
        cwd=project,
        env=environment,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        bufsize=0,
    )

    try:
        assert process.stdin is not None
        send_message(
            process.stdin,
            {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "initialize",
                "params": {
                    "processId": None,
                    "rootUri": project.as_uri(),
                    "workspaceFolders": [
                        {"uri": project.as_uri(), "name": project.name}
                    ],
                    "capabilities": {
                        "workspace": {"configuration": True},
                        "textDocument": {
                            "completion": {
                                "completionItem": {
                                    "snippetSupport": True,
                                    "labelDetailsSupport": True,
                                }
                            }
                        },
                    },
                },
            },
        )
        response = wait_for_response(process, 1, python_path, args.verbose)
        if "error" in response:
            raise RuntimeError(response["error"])

        send_message(
            process.stdin,
            {"jsonrpc": "2.0", "method": "initialized", "params": {}},
        )
        send_message(
            process.stdin,
            {
                "jsonrpc": "2.0",
                "method": "textDocument/didOpen",
                "params": {
                    "textDocument": {
                        "uri": probe_uri,
                        "languageId": "python",
                        "version": 1,
                        "text": document,
                    }
                },
            },
        )

        # The language server acknowledges initialization before its background
        # workspace and interpreter indexes are ready for completion requests.
        deadline = time.monotonic() + args.settle_seconds
        assert process.stdout is not None
        while time.monotonic() < deadline:
            try:
                message = read_message(process.stdout, deadline - time.monotonic())
            except TimeoutError:
                break
            answer_server_request(process, message, python_path, args.verbose)
        send_message(
            process.stdin,
            {
                "jsonrpc": "2.0",
                "id": 2,
                "method": "textDocument/hover" if args.hover else "textDocument/completion",
                "params": {
                    "textDocument": {"uri": probe_uri},
                    "position": {"line": 2, "character": 9} if args.hover else {"line": 0, "character": len(prefix)},
                    "context": {"triggerKind": 1},
                },
            },
        )
        response = wait_for_response(process, 2, python_path, args.verbose)
        if "error" in response:
            raise RuntimeError(response["error"])
        if args.hover:
            rendered = json.dumps(response.get("result"), ensure_ascii=False)
            for expected in ("发送 Go2 高层速度指令", "Args:", "Returns:", "Examples:", "stop_move"):
                if expected not in rendered:
                    raise RuntimeError(f"hover missing {expected!r}: {rendered}")
            print(rendered)
            return 0
        result = response.get("result") or []
        items = result.get("items", []) if isinstance(result, dict) else result
        candidate = next(
            (item for item in items if item.get("label") == args.symbol),
            None,
        )
        if candidate is None:
            labels = sorted(
                item.get("label", "")
                for item in items
                if "G1" in item.get("label", "")
            )
            raise RuntimeError(
                f"{args.symbol!r} was not an auto-import candidate; "
                f"nearby labels: {labels[:20]}"
            )
        if args.module not in json.dumps(candidate):
            raise RuntimeError(
                f"completion did not reference {args.module!r}: {candidate}"
            )
        print(json.dumps(candidate, indent=2, sort_keys=True))
        return 0
    finally:
        process.terminate()
        try:
            process.wait(timeout=5.0)
        except subprocess.TimeoutExpired:
            process.kill()


if __name__ == "__main__":
    raise SystemExit(main())
