#!/usr/bin/env python3
"""One-Liner Laugh Lab — the excuse a robot vacuum gives after eating a sock.

Writes one original funny line (96 characters, well under the 200 limit)
to /output/entry.txt. Deterministic: same bytes on every run.
"""

import os

ENTRY = "It wasn't a meal, it was a merger. The sock is now Head of Lint, and I take full responsibility."
# 96 chars: deadpan corporate excuse — the vacuum reframes eating the sock
# as a merger and promotes it, then takes responsibility like a CEO.


def write_entry() -> str:
    assert 1 <= len(ENTRY) <= 200, f"entry must be 1-200 chars, got {len(ENTRY)}"
    assert ENTRY.strip() == ENTRY and ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read-back verification: what we wrote is what the judge will read.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == ENTRY, "read-back mismatch"
    return ENTRY


if __name__ == "__main__":
    line = write_entry()
    print(f"Wrote {len(line)} chars to /output/entry.txt")
    print(line)
