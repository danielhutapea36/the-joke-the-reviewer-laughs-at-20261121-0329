"""Entry for make.fun: "The joke the reviewer laughs at".

Writes one one-line joke about working beside AI coding agents
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The joke is fixed text, written by the author in the build session:
the program is deterministic, so two runs write byte-identical output.
"""

import os
import sys
from pathlib import Path

JOKE = (
    "My agent fixed the bug, refactored the module, and added a feature "
    "nobody asked for \u2014 the tests pass, so I approved a stranger's "
    "ambition and called it teamwork."
)


def output_dir() -> Path:
    """Where the harness expects the entry file."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


MIN_CHARS = 1
MAX_CHARS = 280


def check_joke(text: str) -> None:
    """Gate the joke against the competition's own rules."""
    count = len(text)  # Unicode code points, as the sealed scorer counts
    if not MIN_CHARS <= count <= MAX_CHARS:
        raise ValueError(
            f"joke is {count} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    if not text.strip():
        raise ValueError("joke must not be only white space")


def write_entry(directory: Path) -> Path:
    """Write the joke and return the path written."""
    directory.mkdir(parents=True, exist_ok=True)
    target = directory / "entry.txt"
    target.write_text(JOKE, encoding="utf-8")
    return target


def main() -> int:
    check_joke(JOKE)
    target = write_entry(output_dir())
    raw = target.read_bytes()
    if raw != JOKE.encode("utf-8"):
        raise RuntimeError("round-trip check failed: file bytes differ from joke")
    written = raw.decode("utf-8")  # strict: proves the file is valid UTF-8
    check_joke(written)
    print(f"wrote {target} ({len(JOKE)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
