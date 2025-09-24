#!/usr/bin/env bash
set -euo pipefail
HOST=${1:-127.0.0.1}
PORT=${2:-12006}
uv run python3 main.py --mode http --host "$HOST" --port "$PORT"
