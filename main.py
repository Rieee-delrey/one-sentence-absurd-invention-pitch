#!/usr/bin/env python3
"""One-sentence absurd invention pitch: a fridge that charges rent.

Writes exactly one sentence to /output/entry.txt, then reads it back
and refuses to exit cleanly unless the bytes on disk match exactly.
"""

import os
import sys

ENTRY = "A fridge that charges rent to the food inside it and evicts the leftovers after three days with a formal notice."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 220


def main() -> int:
    if len(ENTRY) > MAX_CHARS:
        print(f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} limit", file=sys.stderr)
        return 1
    if ENTRY.count(".") != 1 or not ENTRY.endswith("."):
        print("entry must be exactly one sentence", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = ENTRY.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != data:
        print("read-back mismatch: entry.txt does not match the entry", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
