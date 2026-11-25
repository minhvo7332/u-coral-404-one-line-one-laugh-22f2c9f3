#!/usr/bin/env python3
"""One Line, One Laugh — v1 probe entry.

Writes exactly one line (<=200 chars) to /output/entry.txt.
Deterministic: fixed text, no randomness, no network, no clock.
Standard library only.
"""

import os

LINE = "I bought a lie detector for my parrot, and now the bird only talks to my lawyer."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be whitespace-only"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
