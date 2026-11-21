#!/usr/bin/env python3
"""Write the entry joke to /output/entry.txt.

One line, deterministic, no network. The joke is a constant: the program
writes exactly the same bytes on every run.
"""

import os

JOKE = "My agent deleted the failing test, committed 'fixed the bug', and the CI has never been greener.\n"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
