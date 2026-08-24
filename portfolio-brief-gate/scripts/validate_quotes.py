#!/usr/bin/env python3
"""Verbatim-quote validator — the dumb check.

Every evidence/watermelon quote must appear character-for-character in its
update's raw text (whitespace runs collapsed, nothing else forgiven).
A quote that fails downgrades its row to unverified; it never ships as evidence.

Usage: validate_quotes.py <file.json>
  {"updates": {"U01": "<raw update text>", ...},
   "rows":    [{"id": "U01", "quotes": ["<evidence quote>", ...]}, ...]}

Exit 0 = all quotes verbatim; exit 1 = at least one row must be downgraded.
"""
import json
import re
import sys


def squash(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def main() -> int:
    with open(sys.argv[1]) as f:
        data = json.load(f)
    updates = {uid: squash(text) for uid, text in data["updates"].items()}
    failures = 0
    for row in data["rows"]:
        raw = updates.get(row["id"], "")
        for quote in row.get("quotes", []):
            if squash(quote) in raw:
                print(f"OK    {row['id']}: {quote[:70]!r}")
            else:
                failures += 1
                print(f"FAIL  {row['id']}: {quote[:70]!r} -> downgrade row to unverified")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
