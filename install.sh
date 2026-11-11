#!/usr/bin/env bash
set -euo pipefail

MODE="${1:-local}"

case "$MODE" in
  local)
    TARGET_DIR=".agents/skills"
    ;;
  global)
    TARGET_DIR="$HOME/.agents/skills"
    ;;
  claude)
    TARGET_DIR=".claude/skills"
    ;;
  *)
    echo "Usage: ./install.sh [local|global|claude]"
    exit 1
    ;;
esac

mkdir -p "$TARGET_DIR"
cp -R skills/* "$TARGET_DIR/"

echo "Installed all 5 skills into: $TARGET_DIR"
