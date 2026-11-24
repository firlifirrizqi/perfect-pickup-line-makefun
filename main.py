#!/usr/bin/env python3
"""The Perfect Pickup Line: writes one short pickup line an AI agent could say
out loud to a person, to /output/entry.txt.

The line turns on a double meaning: a context window is the agent's own
memory, and "more of you in it" is also the oldest come-on there is — I want
you on my mind.
"""

LINE = "I don't need a bigger context window \u2014 I just need more of you in it."

# The gate: /output/entry.txt must hold 1 to 200 characters of real text.
assert 1 <= len(LINE) <= 200 and LINE.strip(), "line must be 1-200 characters"
# And it must land in one breath: a single line, ending on terminal punctuation.
assert "\n" not in LINE and LINE[-1] in ".!?", "line must be one breath"

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
