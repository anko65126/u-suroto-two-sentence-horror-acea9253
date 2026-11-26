"""Entry point for the Two-Sentence Horror bounty.

Writes one horror story of exactly two sentences to /output/entry.txt.
The story is at most 400 characters, deterministic, and needs no
network access. The second sentence reframes the first: the comfort
of the monitor turns out to be the threat itself.
"""
from pathlib import Path

STORY = (
    "The baby monitor finally showed my daughter sleeping peacefully, "
    "so I went upstairs to kiss her goodnight. "
    "She was already standing behind me, asking why I was still watching the empty crib."
)

TARGET = Path("/output/entry.txt")


def main():
    text = STORY.strip()
    assert 1 <= len(text) <= 400, f"story is {len(text)} characters"
    assert text.count(".") == 2, "story must be exactly two sentences"
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(text + "\n", encoding="utf-8")
    print(f"wrote {len(text)} characters to {TARGET}")


if __name__ == "__main__":
    main()
