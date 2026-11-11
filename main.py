#!/usr/bin/env python3
"""make.fun news-summary-01 entry: writes the summary of 11 November 2026 world news to /output/entry.txt."""
import os

def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "summary.txt"), "r", encoding="utf-8") as f:
        text = f.read()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as out:
        out.write(text)

if __name__ == "__main__":
    main()
