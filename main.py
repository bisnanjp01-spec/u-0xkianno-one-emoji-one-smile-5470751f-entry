"""One Emoji, One Smile — write exactly one emoji to /output/entry.txt.

The entry is a single yellow heart (U+1F49B), the warmest emoji for a
stranger's smile: warm at first glance, universal, a deliberate pick
rather than the default smiley or the default red heart, and friendly
rather than intimate when it comes from someone unknown.

The program is deterministic: every run writes the same four UTF-8
bytes and nothing else. Python standard library only, no network.
"""

import os

# The one emoji this entry sends: YELLOW HEART, U+1F49B.
EMOJI = "\U0001F49B"

OUTPUT_PATH = "/output/entry.txt"


def entry_bytes() -> bytes:
    """Encode the single emoji as UTF-8, with no extra characters."""
    return EMOJI.encode("utf-8")


def main() -> None:
    # Guard the gate: the entry must be exactly one character, never
    # empty and never more, so refuse to write anything else.
    if len(EMOJI) != 1:
        raise ValueError("entry must be exactly one emoji")
    data = entry_bytes()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(data)
    print(EMOJI)


if __name__ == "__main__":
    main()
