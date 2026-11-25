#!/usr/bin/env python3
"""The Tired Dark Lord — a 100-word villain monologue.

Standard library only. The monologue lives in a single constant; main()
validates it, writes it to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output),
then reads the file back and verifies it byte-for-byte.
"""

import os
import sys

MONOLOGUE = (
    "Come in. Mind the step: it sighs, and I stopped correcting it.\n"
    "You expected a throne of skulls. Only this chair, a ledger, a window "
    "shut nine years, since my brother sold the keys for a song.\n"
    "I took his kingdom with three words and a borrowed storm. Now the storm "
    "wants paying, the kingdom wants feeding, and heroes arrive on Tuesdays, "
    "asking to be slain.\n"
    "I could raze the valley: the old fire coiled under the floorboards.\n"
    "But the floorboards creak, and the fire would wake the baby dragon. "
    "Sit down, hero. The tea is poured. You will stay for it."
)

MAX_CHARS = 600


def validate(text):
    """Check the monologue is non-blank, valid UTF-8, and within the cap."""
    if not text or not text.strip():
        raise ValueError("monologue is blank")
    text.encode("utf-8")  # raises if the text is not valid UTF-8
    if len(text) > MAX_CHARS:
        raise ValueError(
            "monologue is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    return text


def main():
    text = validate(MONOLOGUE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    with open(path, "r", encoding="utf-8", newline="") as fh:
        back = fh.read()
    if back != text:
        raise SystemExit("verification failed: entry.txt does not match the monologue")
    words = len(text.split())
    print("wrote %s: %d words, %d characters" % (path, words, len(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
