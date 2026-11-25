#!/usr/bin/env python3
"""Write a single-line fridge roast to /output/entry.txt.

One line, at most 200 characters, roasting the crisper drawer of my own
fridge: the vegetables go in fresh and come out as something else entirely.
No external dependencies; standard library only.
"""

import os

ENTRY = (
    "My fridge's crisper drawer is a hospice for vegetables: "
    "the lettuce went in dreaming of salads and came out as soup "
    "with a last will and testament."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.umask(0o022)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"

    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")

    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
