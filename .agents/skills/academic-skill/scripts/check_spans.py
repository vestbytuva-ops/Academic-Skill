"""Compare exact counts of editor-selected strings in two local UTF-8 texts."""

import json
import re
import sys
from pathlib import Path


def occurrence_count(text, span):
    """Count overlapping literal matches, rejecting partial numbers at the edges."""
    # At a digit edge, adjacent digits or a decimal separator joining two
    # digits extend the number. A final period in a sentence is still allowed.
    left = r"(?<!\d)(?<!\d[.,])" if span[0].isdecimal() else ""
    right = r"(?!\d|[.,]\d)" if span[-1].isdecimal() else ""
    pattern = re.compile(left + re.escape(span) + right)
    count = 0
    match = pattern.search(text)
    while match:
        count += 1
        match = pattern.search(text, match.start() + 1)
    return count


def check_spans(source, revised, spans):
    """Return (exit code, report lines). Indices refer to the zero-based JSON list.

    Codes: 0 for equal counts, 1 for a change, 2 for invalid input. This
    comparison checks literal strings only. No locations or text are reported.
    """
    if not isinstance(source, str) or not isinstance(revised, str):
        return 2, ["FAIL"]
    if not isinstance(spans, list) or not spans:
        return 2, ["FAIL"]

    changes = []
    for index, span in enumerate(spans):
        if not isinstance(span, str) or not span:
            return 2, [f"FAIL index={index}"]
        source_count = occurrence_count(source, span)
        if source_count == 0:
            return 2, [f"FAIL index={index} source_count=0"]
        revised_count = occurrence_count(revised, span)
        if revised_count != source_count:
            changes.append(
                f"FAIL index={index} source_count={source_count} revised_count={revised_count}"
            )
    if changes:
        return 1, changes
    return 0, ["PASS"]


def read_utf8(path):
    # Reading bytes preserves CR, LF, and CRLF inside quoted material.
    return Path(path).read_bytes().decode("utf-8-sig")


def main(arguments):
    """Read three positional paths: source text, revised text, JSON span list."""
    if len(arguments) != 3:
        print("FAIL")
        return 2
    try:
        source = read_utf8(arguments[0])
        revised = read_utf8(arguments[1])
        spans = json.loads(read_utf8(arguments[2]))
    except (OSError, ValueError, RecursionError):
        print("FAIL")
        return 2
    status, lines = check_spans(source, revised, spans)
    for line in lines:
        print(line)
    return status


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
