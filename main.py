#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one line -- an alien tourist's review of Earth -- to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output). Stdlib only, no network.
"""

import os
import stat
import sys

REVIEW = (
    "Once a year they light tiny fires on a cake, blow them out, "
    "and call it a wish. Fire safety: alarming. Optimism: admirable. 4/5 stars."
)


def main() -> int:
    text = REVIEW
    # Validate before writing: exactly one line, 1-200 chars, not only whitespace.
    if not 1 <= len(text) <= 200:
        print(f"entry length {len(text)} out of range 1-200", file=sys.stderr)
        return 1
    if text != text.strip() or "\n" in text or "\r" in text:
        print("entry must be a single line, no leading/trailing whitespace",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    old_umask = os.umask(0o022)
    try:
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(text)
    finally:
        os.umask(old_umask)
    os.chmod(path, 0o644)
    # Read back and verify the written file.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("read-back mismatch", file=sys.stderr)
        return 1
    if stat.S_IMODE(os.stat(path).st_mode) != 0o644:
        print("mode is not 0644", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
