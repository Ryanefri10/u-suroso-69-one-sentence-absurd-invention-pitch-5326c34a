"""One-Sentence Absurd Invention Pitch — make.fun entry.

Writes a single-sentence pitch (at most 220 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt, the artifact the house judge reads.

The pitch: a smoke detector that stops shrieking at burnt toast and
instead quietly disposes of the evidence — a cover-up machine for a
tiny everyday annoyance.
"""

import os
from pathlib import Path

PITCH = (
    "A smoke detector that, instead of shrieking at burnt toast, "
    "quietly drops it through a trapdoor into a fireproof vault "
    "and texts you that it never happened."
)


def main() -> None:
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    # Gate, mirrored from the kit: /output/entry.txt must be UTF-8 text
    # of 1 to 220 characters, not only white space, and the brief asks
    # for a single sentence. Fail loudly here rather than emit an
    # invalid entry the judge never sees.
    text = PITCH.strip()
    if not 1 <= len(text) <= 220:
        raise SystemExit(f"pitch must be 1-220 chars, got {len(text)}")
    if not text.strip() or text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("pitch must be one sentence, no trailing newline")
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")
    print(f"wrote entry.txt ({len(text)} chars)")


if __name__ == "__main__":
    main()
