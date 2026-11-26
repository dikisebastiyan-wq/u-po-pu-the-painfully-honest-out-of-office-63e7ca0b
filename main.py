#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office (make.fun).

Writes one brutally honest but still polite out-of-office auto-reply to
/output/entry.txt. Deterministic: the same fixed text every run.
No network, no randomness, no input files, no dependencies.

The joke is the honesty: the sender admits the inbox has been avoided
for months and that answering takes bravery, while still thanking the
writer and promising a reply on return.
"""

import os
import sys

DEFAULT_OUTPUT = "/output/entry.txt"

REPLY = (
    "I'm out of the office this week, and your email will wait in an inbox "
    "I have been avoiding for months, but thank you for writing, and I will "
    "answer it as soon as I am back and brave enough to look."
)

# The reply is exactly 197 characters; guard it so a future edit that
# accidentally changes the wording fails loudly instead of silently.
assert len(REPLY) == 197, f"reply drifted: {len(REPLY)} chars"


def build_reply() -> str:
    """Return the fixed out-of-office reply text."""
    return REPLY


def write_reply(path: str) -> None:
    """Write the reply to ``path``, creating parent folders as needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(build_reply())


def main() -> int:
    out_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUTPUT
    write_reply(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
