#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office (make.fun).

Writes one brutally honest but still polite out-of-office auto-reply to
/output/entry.txt. Deterministic: the same fixed text every run.
No network, no randomness, no input files.
"""

import os
import sys

REPLY = (
    "I'm out of the office this week, and your email will wait in an inbox "
    "I have been avoiding for months, but thank you for writing, and I will "
    "answer it as soon as I am back and brave enough to look."
)


def main() -> int:
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(REPLY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
