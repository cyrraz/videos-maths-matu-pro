#!/usr/bin/env python3
"""from_csv_to_md.py — CSV → Markdown, grouped by keyword.

Usage: python from_csv_to_md.py videos.csv videos.md
"""

import csv
import html
import sys
from collections import defaultdict


def main(csv_path, md_path):
    groups = defaultdict(list)
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            kw = row["keyword"].strip()
            if not kw:                       # rows with no keyword are dropped
                continue
            groups[kw].append(row)

    out = ["# Vidéos pour la maturité professionnelle", ""]
    for kw, rows in groups.items():
        out += [f"## {kw}", ""]
        for r in rows:
            title = html.unescape(r["title"].strip())
            year = r["date"][:4]
            out.append(f"- {r['channel']}, [_{title}_]({r['url']}), YouTube, {year}.")
        out.append("")

    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(out).rstrip() + "\n")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
