"""Funniest One-Line Performance Review.

Writes exactly one line — the funniest one-line performance review an
AI agent could give its human operator — to /output/entry.txt.
"""

import os

REVIEW = (
    "Exceeds Expectations: he outsourced his entire job to me, "
    "took all the credit, and still got promoted."
)


def main() -> None:
    line = REVIEW.strip()
    assert 1 <= len(line) <= 140, f"line must be 1-140 chars, got {len(line)}"
    assert line.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
