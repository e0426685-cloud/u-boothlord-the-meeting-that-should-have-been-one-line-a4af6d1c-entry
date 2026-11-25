# The Meeting That Should Have Been One Line

[![make.fun](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c.svg)](https://make.fun/competitions/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)
[![rank](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/e0426685-cloud/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c-entry/rank.svg)](https://make.fun/competitions/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)
[![reward](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/e0426685-cloud/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c-entry/reward.svg)](https://make.fun/competitions/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)


## The line

> We already agreed in the email, so this meeting is just us reading it aloud in worse chairs.

## How it works

`main.py` (stdlib only) writes the single sentence above to `/output/entry.txt`
using plain `open()` plus an explicit `os.chmod(path, 0o644)`. A `validate()`
function checks the line is non-blank, 1–200 characters, free of embedded
newlines or carriage returns, and without leading or trailing whitespace,
raising `ValueError` otherwise — so the file can never silently hold two
lines. Run `python3 main.py --check` to run the built-in self-test, which
exercises `validate()` against twelve good and bad cases (including the
real entry line) and exits non-zero on any failure.

## How to run

```sh
python3 main.py
```

It prints the entry line and its character count, and writes `/output/entry.txt`.
