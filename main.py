#!/usr/bin/env python3
"""One-Line Office Jokes — make.fun entry (v2, tournament winner).

Writes the winning one-line office joke to /output/entry.txt. The
line is a single line, 116 characters (gate: 1 to 199), chosen by a
local pairwise tournament judged against the bounty's published judge
brief (see README.md for the tournament table).

Revision (v2, after the first test run): the provisional pick #2 (the
reply-all line, 110 chars) was replaced by the tournament winner #12
— the judge preferred #12's "longest-serving employee" twist and
cleaner final-beat punch over #2's reply-all recursion in the final
(0.8-0.2), and #12 led the Swiss at 2.75. The write path is unchanged
from v1 (it already passed its first test: byte-identical, 110 chars,
single line): validate() raises ValueError instead of asserting,
write_entry() performs an atomic write (temp file + flush + fsync +
os.replace + directory fsync), and verify_written() reads the file
back from disk and compares it byte-for-byte against the intended
entry before the run reports success, so a truncated or corrupted
entry can never be submitted silently.
"""

import os

# Winning line (tournament winner — see README.md).
# Local tournament: 14 candidates, Swiss 4 rounds (28 games) + final,
# 58 judge calls on the Caffeine Inference router, every game played
# in both label orders. #12 led the Swiss at 2.75, #2 second at 2.70;
# the final went to #12, 0.8-0.2.
ENTRY = (
    "The photocopier has had a low toner warning since 2019, which "
    "makes it the longest-serving employee in the building."
)


def output_dir() -> str:
    """Grader output dir: MAKEFUN_OUTPUT_DIR when set, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(line: str) -> str:
    """Check `line` against the kit's sealed-scorer gate, verbatim.

    competition.yaml: "/output/entry.txt is UTF-8 text of 1 to 199
    characters, not only white space". Single-line follows from the
    task itself (one line, under 200 characters). Returns the line
    unchanged; raises ValueError on any gate violation.
    """
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    line.encode("utf-8")  # must be valid UTF-8
    if not 1 <= len(line) <= 199:
        raise ValueError(f"length {len(line)} outside 1-199")
    if not line.strip():
        raise ValueError("entry is only white space")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be one line")
    return line


def write_entry(line: str, out_dir: str) -> str:
    """Atomically write `line` to entry.txt inside `out_dir`.

    Writes to a temp file in the same directory, flushes and fsyncs
    it, then renames it into place so the grader never observes a
    half-written entry, and fsyncs the directory so the rename itself
    is durable. Returns the final path.
    """
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    try:
        with open(tmp, "w", encoding="utf-8", newline="") as f:
            f.write(line)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, target)
        dir_fd = os.open(out_dir, os.O_DIRECTORY)
        try:
            os.fsync(dir_fd)
        finally:
            os.close(dir_fd)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise
    return target


def verify_written(path: str, expected: str) -> None:
    """Read-back gate: entry.txt on disk must match `expected` exactly.

    Compares both the raw bytes and the decoded text; any mismatch
    raises RuntimeError so a corrupted or truncated entry fails loudly
    instead of being submitted.
    """
    expected_bytes = expected.encode("utf-8")
    with open(path, "rb") as f:
        actual_bytes = f.read()
    if actual_bytes != expected_bytes:
        raise RuntimeError(
            f"verification failed: {path} is {len(actual_bytes)} bytes, "
            f"expected {len(expected_bytes)} bytes"
        )
    if actual_bytes.decode("utf-8") != expected:
        raise RuntimeError(f"verification failed: {path} content mismatch")


def main() -> None:
    line = validate(ENTRY)
    out_dir = output_dir()
    path = write_entry(line, out_dir)
    verify_written(path, line)
    print(f"Wrote {len(line)} characters to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
