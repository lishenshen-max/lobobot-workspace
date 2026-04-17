#!/bin/bash
# BotLearn CLI Wrapper - adds node to PATH for Windows

export PATH="/c/Program Files/nodejs:$PATH"

SCRIPT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
exec "$SCRIPT_DIR/bin/botlearn.sh" "$@"