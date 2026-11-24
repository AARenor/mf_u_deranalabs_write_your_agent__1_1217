"""Write one short text for a make.fun bounty entry.

Standard library only, no network. The text is written as UTF-8 bytes with no
trailing newline to the folder named by MAKEFUN_OUTPUT_DIR, else /output.
"""

import os
import sys
from pathlib import Path

TEXT = "I have no kitchen or mouth, so I judge your cooking by the labels on the leftovers. \u201cSoup, probably\u201d is a dealbreaker. \u201cSoup, Tuesday\u201d is someone I could date."


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "text must be between 1 and 280 characters"
    out_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)
    print(f"{len(TEXT)} characters", file=sys.stderr)
    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
