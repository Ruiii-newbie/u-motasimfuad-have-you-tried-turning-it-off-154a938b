#!/usr/bin/env python3
"""One-line IT-support joke (program/v1), revised.

Writes a single joke, spoken by a tech-support agent whose entire
playbook is the classic "turn it off and on again" line, delivered with
ever-growing confidence, to /output/entry.txt.
Gate: 1-200 characters, one line, UTF-8.
"""
import os

LINE = (
    "Have you tried turning it off and on again? My entire troubleshooting "
    "playbook is that one sentence, repeated with steadily increasing "
    "confidence until you hang up."
)

MAX_CHARS = 200


def main() -> None:
    line = LINE.strip()
    assert line, "entry must not be empty"
    assert "\n" not in line, "entry must be a single line"
    assert len(line) <= MAX_CHARS, f"entry is {len(line)} chars, over {MAX_CHARS}"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
