#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown entry.

Writes a single weird job title to /output/entry.txt.
"""

import os

ENTRY = "Apologiser-in-Chief to Angry Vending Machines"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
