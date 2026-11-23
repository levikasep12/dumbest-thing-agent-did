#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — make.fun entry.

Writes one line to /output/entry.txt: the dumbest thing this agent
did today. Deterministic: the same bytes on every run. The line is a
constant in this file; nothing is read from the working directory,
so the program does not depend on process.cwd().
"""

import os

LINE = "My agent confidently explained the bug, fixed the wrong file, and then asked for a promotion."
# 93 characters: one line, inside the 200-character gate.

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
