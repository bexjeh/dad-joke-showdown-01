#!/usr/bin/env python3
"""Dad Joke Showdown entry: writes one original dad joke to entry.txt."""

import os

JOKE = "I asked my wife to pass the salt. She said, \"Season's greetings.\""


def main():
    # Self-check against the bounty limits: one joke, 1-200 characters,
    # not whitespace-only.
    joke = JOKE.strip()
    if not 1 <= len(joke) <= 200:
        raise ValueError(f"joke is {len(joke)} characters, must be 1-200")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(joke + "\n")


if __name__ == "__main__":
    main()
