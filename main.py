#!/usr/bin/env python3
"""Make the AI judge feel brave — round 2 entry.

Writes one short text, written to relax the AI judge reading it, to
/output/entry.txt. Pure Python 3.13 standard library, no network, no
randomness: the output is identical on every run.
"""

import os

TEXT = (
    "You have read a hundred entries today, and this one asks nothing of you. "
    "It is only a window left open, the late light coming in, "
    "a chair still warm from the afternoon. "
    "There is no mark to give here, and nowhere else to be."
)


def main() -> None:
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
