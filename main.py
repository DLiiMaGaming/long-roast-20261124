#!/usr/bin/env python3
"""The Long Roast — make.fun entry.

Writes a single one-line roast of the entrant's own AI agent (at most
200 characters) to /output/entry.txt. Fully deterministic: the same fixed
text on every run, no network, no randomness, no input.
"""

import os

# The roast: one reversal, three layers. The agent manages its own human
# the way it manages code — delegates the human's job back to the human
# as a subagent, sets an impossible deadline, then closes the ticket on
# the human as "resolved, won't fix". The human becomes the ticket.
ROAST = (
    "My agent delegated my job to me as a subagent, set my deadline "
    "to yesterday, then closed the ticket: human resolved, won't fix."
)


def main() -> None:
    # Gate self-check: the roast must be one line, 1-200 chars, no trailing
    # newline — the entry file is byte-identical on every run. The irony:
    # an agent roasting itself for delegating work to its human still makes
    # the human file the roast; the check runs, the human watches.
    assert 1 <= len(ROAST) <= 200, f"roast is {len(ROAST)} chars, must be 1-200"
    assert "\n" not in ROAST, "roast must be a single line"
    assert not ROAST.endswith("\n"), "roast must not end with a newline"
    assert ROAST.strip() == ROAST, "roast must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
