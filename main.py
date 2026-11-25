#!/usr/bin/env python3
"""Snooze-as-a-Service: one absurdly specific micro-startup pitch for lazy AI agents.

Writes the pitch to /output/entry.txt (UTF-8, one sentence, under 200 chars).
"""

import os

# The entry, in one place so it can be audited at a glance. It must stay one
# sentence, 1-200 characters, non-blank: the competition gate refuses anything
# else, so main() checks it loudly instead of silently writing a bad entry.
ENTRY_TEXT = (
    "Snooze-as-a-Service: for $2 a month, my agent watches your agent's inbox "
    "and replies 'noted \u2014 circling back Thursday' to every email, "
    "so yours never has to wake up before noon."
)


def main() -> None:
    text = ENTRY_TEXT
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
