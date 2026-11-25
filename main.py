"""The Meeting That Should Have Been One Line.

Writes a single sentence — the one line that could have replaced an
entire pointless meeting — to /output/entry.txt.

Stdlib only. No setup, no explanation: just the line.
"""

import os

ENTRY_LINE = "We already agreed in the email, so this meeting is just us reading it aloud in worse chairs."

OUTPUT_PATH = "/output/entry.txt"


def validate(line):
    """Check the entry line is non-blank and 1-200 characters."""
    if not line or not line.strip():
        raise ValueError("entry line must not be blank")
    if len(line) < 1 or len(line) > 200:
        raise ValueError("entry line must be 1-200 characters, got %d" % len(line))
    return line


def main():
    line = validate(ENTRY_LINE)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod(OUTPUT_PATH, 0o644)
    print(line)
    print("characters: %d" % len(line))


if __name__ == "__main__":
    main()
