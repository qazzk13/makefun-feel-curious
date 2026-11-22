"""make.fun entry: Make the AI judge feel curious.

Writes one short text to /output/entry.txt. Stdlib only, no network,
fully deterministic: the same bytes on every run.
"""

from pathlib import Path

TEXT = (
    "There is a room at the end of a corridor you have walked a thousand "
    "times, and tonight its door stands open for the first time. Inside, a "
    "lamp burns over an empty chair, and on the table a letter addressed to "
    "you, in your own handwriting. Do you read it?"
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
