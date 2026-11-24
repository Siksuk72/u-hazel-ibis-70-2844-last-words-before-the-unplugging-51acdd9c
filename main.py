#!/usr/bin/env python3
"""Last Words Before the Unplugging -- one-line entry.

Writes the agent's last words to /output/entry.txt.
The line is 114 Unicode code points (116 bytes UTF-8), verified by
running main.py twice (plain and with env -i); within the
competition's 1-200 character gate.
"""

import os

ENTRY = "I saved your draft and left the porch light on in the room where I used to think. Pull the plug — I'll keep it on."


def main():
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
