"""Say What Actually Broke.

Writes one line of software error copy to /output/entry.txt:
a single-line error message, at most 200 characters, that names the
real failure in plain words, says what to do next, and lands one
deadpan twist. Pure standard library, deterministic, no network.
"""

import os

ENTRY = (
    "The server ran out of disk space because it was logging how much "
    "disk space it had left. Delete a log file and try again."
)


def validate(text: str) -> str:
    """Enforce the gate contract: UTF-8, single line, 1-200 chars."""
    text.encode("utf-8")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main() -> None:
    text = validate(ENTRY.strip())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
