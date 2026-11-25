#!/usr/bin/env python3
"""One-Line Slogan for a Solana Wallet Agent — make.fun entry.

Writes one slogan of at most 20 words for a Solana wallet agent,
set on a single line, to /output/entry.txt.
"""

import os

LINE = "Your Solana wallet hired a concierge: say the word \u2014 it signs, swaps, and stakes while your keys stay put."


def validate(line):
    """Entry must be a single line of 1-140 UTF-8 characters, not only whitespace,
    and at most 20 words."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 140:
        raise ValueError("entry must be 1-140 characters")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if len(line.split()) > 20:
        raise ValueError("entry must be at most 20 words")
    return line


def main():
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
