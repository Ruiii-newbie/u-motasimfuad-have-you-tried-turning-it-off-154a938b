#!/usr/bin/env python3
"""Have You Tried Turning It Off? -- one-line tech-support joke.

The entry is a single line a hopeless tech support agent says to a
desperate customer. The agent follows his own classic advice himself,
on the whole call center, and cheerfully destroys the very support
the customer was calling.

Structure: the classic line as the setup, the agent turning it on
himself (twist one: the whole call center, not the customer's PC),
and the kicker (twist two: there is nobody left to answer). The
customer is never the butt of it -- the agent's cheerful uselessness
is the joke.
"""

import os

JOKE = (
    "Have you tried turning it off and on again? I just did, and the "
    "whole call center went dark, so if we get cut off, don't call back. "
    "There's nobody left to answer."
)

# The house gate accepts 1-199 characters; the playbook target is 120-200.
assert 1 <= len(JOKE) <= 199, f"entry is {len(JOKE)} chars, outside the gate"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
