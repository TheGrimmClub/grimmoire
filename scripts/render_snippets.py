#!/usr/bin/env python3
"""Inject shared solution code into the docs from python/beginners/snippets/*.py.

Zensical can't include external files, so each solution lives as a real .py file
(the single source of truth, with English code per the club's "narrative German,
code English" rule) and is expanded into every language page between
HTML-comment markers:

    <!-- snippet: 03-enter.py -->
    ```python
    ...injected from snippets/03-enter.py...
    ```
    <!-- endsnippet -->

To author a page, just write the two markers with nothing between them:

    <!-- snippet: 03-enter.py -->
    <!-- endsnippet -->

...then run `python scripts/render_snippets.py` (or `task docs:render`).

The injection is idempotent — run it as often as you like. `--check` writes
nothing and exits non-zero if any page is out of date (used in CI).
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "python" / "beginners"
SNIPPETS = DOCS / "snippets"

# Everything from an opening marker to the next endsnippet marker.
BLOCK = re.compile(
    r"(?P<indent>[ \t]*)<!-- snippet: (?P<name>[^\n]+?) -->.*?<!-- endsnippet -->",
    re.DOTALL,
)


def render_block(indent: str, name: str) -> str:
    path = SNIPPETS / name.strip()
    if not path.is_file():
        raise SystemExit(f"error: snippet not found: {path}")
    code = path.read_text(encoding="utf-8").rstrip("\n").splitlines()
    out = [f"{indent}<!-- snippet: {name} -->", f"{indent}```python"]
    # Re-indent each code line to the marker's indentation (e.g. inside an
    # admonition). Blank lines stay blank, no trailing whitespace.
    out += [f"{indent}{line}".rstrip() if line == "" else f"{indent}{line}" for line in code]
    out += [f"{indent}```", f"{indent}<!-- endsnippet -->"]
    return "\n".join(out)


def process(text: str) -> str:
    return BLOCK.sub(lambda m: render_block(m["indent"], m["name"]), text)


def main() -> int:
    check = "--check" in sys.argv
    pages = sorted(DOCS.glob("*/*.md"))
    stale = []
    for page in pages:
        original = page.read_text(encoding="utf-8")
        updated = process(original)
        if updated != original:
            if check:
                stale.append(page.relative_to(ROOT))
            else:
                page.write_text(updated, encoding="utf-8")

    if check and stale:
        print("Out-of-date snippet blocks in:")
        for p in stale:
            print(f"  {p}")
        print("Run: task docs:render")
        return 1
    action = "checked" if check else "rendered"
    print(f"Snippets {action} in {len(pages)} pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
