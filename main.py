"""The Meeting That Should Have Been One Line.

The competition asks for one sentence that could have replaced an entire
meeting. The entry is that sentence: the meeting only exists because
nobody re-read the email, so the line says exactly that and stops.

This script's job is small but strict. It writes the sentence to
/output/entry.txt and nothing else — no trailing newline, no second line,
no commentary — because the competition counts a single line of 1-200
characters. The validate() gate below is what guarantees that: it rejects
blank lines, over-long lines, and anything with an embedded newline or
carriage return smuggled in, so what lands in the file is genuinely one
line. Run with --check to exercise the gate against a handful of edge
cases before trusting it with the real line.

Stdlib only. No setup, no explanation: just the line.
"""

import os
import sys

ENTRY_LINE = "We already agreed in the email, so this meeting is just us reading it aloud in worse chairs."

OUTPUT_PATH = "/output/entry.txt"


def self_check():
    """Exercise validate() against good and bad lines; exit non-zero on failure.

    Each case is a (label, line, should_pass) triple. The real entry line
    is one of the passing cases, so a regression in either the gate or
    the sentence shows up here before anything is written to disk.
    """
    cases = [
        ("real entry line", ENTRY_LINE, True),
        ("shortest valid line", "x", True),
        ("exactly 200 characters", "a" * 200, True),
        ("empty line", "", False),
        ("blank line", "   ", False),
        ("201 characters", "a" * 201, False),
        ("embedded newline", "first line\nsecond line", False),
        ("embedded carriage return", "first line\rsecond line", False),
        ("trailing newline", "one line\n", False),
        ("leading space", " padded", False),
        ("trailing space", "padded ", False),
        ("non-string input", None, False),
    ]
    failures = 0
    for label, line, should_pass in cases:
        try:
            validate(line)
            passed = True
        except ValueError as exc:
            passed = False
            reason = str(exc)
        if passed == should_pass:
            print("ok: %s" % label)
        else:
            failures += 1
            if should_pass:
                print("FAIL: %s (rejected: %s)" % (label, reason))
            else:
                print("FAIL: %s (accepted, should have been rejected)" % label)
    print("%d/%d checks passed" % (len(cases) - failures, len(cases)))
    return 0 if failures == 0 else 1


def validate(line):
    """Check the entry line is one clean line of 1-200 characters.

    Rejects blank lines, anything longer than 200 characters, and any
    line carrying a newline or carriage return, so the entry can never
    silently become two lines. Leading or trailing whitespace is also
    rejected: a line padded with spaces is not the same line.
    """
    if not isinstance(line, str):
        raise ValueError("entry line must be a string")
    if not line or not line.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must not contain a newline")
    if line != line.strip():
        raise ValueError("entry line must not have leading or trailing whitespace")
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
    if len(sys.argv) > 1 and sys.argv[1] == "--check":
        sys.exit(self_check())
    main()
