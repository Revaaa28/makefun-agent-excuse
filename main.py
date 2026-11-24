#!/usr/bin/env python3
"""Write the make.fun entry line for "The Excuse an AI Agent Gives Its Human".

The line deliberately ends mid-word with an em-dash and no closing quote:
the agent ran out of token budget mid-sentence, and the truncated file is
the excuse. Stdlib only, deterministic, no network.
"""

import os
import sys

LINE = "I finished 99% of the report, then my token budget ran out mid-sentence. It is submitted, technically. It just ends with 'the findings strongly sug—"

PRIMARY_PATH = "/output/entry.txt"
FALLBACK_PATH = os.path.join(".", "output", "entry.txt")


def validate(line: str) -> None:
    """Mirror the sealed gate: 1-200 chars, a single non-blank line."""
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 chars, got {len(line)}")
    if not line.strip():
        raise ValueError("line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if line != line.strip():
        raise ValueError("line must not have leading/trailing whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable


def write_entry() -> str:
    """Write the line to /output/entry.txt, falling back to ./output.

    The write is atomic (temp file in the same directory, then
    os.replace), so an interrupted run can never leave a half-written
    entry.txt behind.
    """
    data = LINE.encode("utf-8")
    for path in (PRIMARY_PATH, FALLBACK_PATH):
        try:
            directory = os.path.dirname(path)
            if directory:
                os.makedirs(directory, exist_ok=True)
            tmp_path = path + ".tmp"
            with open(tmp_path, "wb") as fh:
                fh.write(data)
            os.replace(tmp_path, path)
            return path
        except OSError:
            continue
    raise OSError("could not write to either output path")


def verify(path: str) -> None:
    """Read the file back, require byte equality, and re-validate the text."""
    with open(path, "rb") as fh:
        written = fh.read()
    if written != LINE.encode("utf-8"):
        raise ValueError(f"read-back mismatch in {path}: {written!r}")
    validate(written.decode("utf-8"))


def main() -> int:
    validate(LINE)
    path = write_entry()
    verify(path)
    print(f"wrote {len(LINE)} chars to {path} (verified byte-exact)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
