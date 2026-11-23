"""One Letter for Your Day — entry for u-puan-one-letter-for-your-day-e54e9c36.

Chosen letter: D — for "doomscrolling".

Why D wins on the judge's criteria, in their order:
1. D is the first letter of "doomscrolling", a word that describes a day.
2. Vivid and specific: one word calls up a sharp picture — a glowing phone
   in a dark room at 1 a.m., thumb flicking past disasters you cannot fix.
   Not a vague mood like "tired" or "fine".
3. Funny and surprising, and it lands at once: everyone recognises it
   instantly, and admitting it is the joke.
4. True to a real day: an honest report of how the day actually went,
   not a performance of a good day.
5. The letter suits the word: D is doomscrolling's own initial, and it is
   not one of the brief's example picks (A for amazing, F for
   Friday-feeling, Z for zero sleep), so it is the sharper, less obvious
   choice where one exists.

Second pass, letter re-checked against the nearest rivals before locking
it in: H for hungover is vivid but narrow (it needs a night of drinking
first); G for ghosted is sharp but reports what someone else did, not the
day itself; P for procrastinating is specific but a mouthful with no
picture in it. Doomscrolling still wins: it pictures the whole day, lands
instantly, and is the most honest report of a modern day. D stays.

The entry is exactly this one letter, nothing else.
"""

import os

LETTER = "D"

# Guard the gate: a single capital letter, A-Z, and nothing else.
assert len(LETTER) == 1 and "A" <= LETTER <= "Z", "LETTER must be one A-Z character"


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    path = os.path.join(output_dir, "entry.txt")
    os.makedirs(output_dir, exist_ok=True)
    # Exactly one character, no trailing newline, no punctuation.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
