"""One-Line Office Joke Laugh-Off -- round 4 entry.

Writes one original one-line office joke to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt).

THREE CANDIDATES -- scored against the judge's five criteria
(1: really a one-line office joke; 2: sharp, surprising punchline,
not a mild observation; 3: clear on one read; 4: fresh, avoids
office cliches; 5: tight wording). Each criterion scored /5.

CANDIDATE A -- the reply-all trap (email angle):
  "I hit reply-all to be removed from the thread. Now I AM the thread."
  1: 5 -- unmistakably office email life, one line.
  2: 4 -- the escape attempt backfiring into "I AM the thread" is a
     genuine paradox twist, but it is wordplay more than a laugh.
  3: 5 -- instantly clear, no setup to explain.
  4: 4 -- reply-all is a known trope, but "becoming the thread" is
     an unusual turn on it.
  5: 5 -- every word earns its place (70 chars).
  TOTAL: 23/25.

CANDIDATE B -- the honest out-of-office reply (leave angle):
  "My out-of-office reply says I'm unreachable. The most honest
  thing I've written at work all year."
  1: 5 -- clearly office life, one line.
  2: 4 -- "the most honest thing" is a nice cynical sting, implying
     everything else written at work is a lie; surprising enough.
  3: 5 -- clear on one read.
  4: 4 -- out-of-office jokes exist, but framing the auto-reply as
     a confession is a fresh angle on it.
  5: 4 -- "at work all year" is slightly wordy (108 chars).
  TOTAL: 22/25.

CANDIDATE C -- the budget-review lunch (pantry/fridge angle):
  "My lunch kept disappearing from the office fridge, so I labelled
  it 'Q3 Budget Review'. Nobody has touched it since."
  1: 5 -- clearly office life, one line.
  2: 5 -- the payoff is a concrete, surprising twist: the only thing
     nobody in an office will touch is a boring finance document,
     so the lunch becomes safe by disguise. A real punchline, not
     an observation.
  3: 5 -- clear on one read; the label does all the work.
  4: 4 -- fridge theft is a known setup, but nobody's punchline is
     "disguise your sandwich as a quarterly report" -- the twist,
     not the setup, is what is fresh.
  5: 4 -- setup is a touch long, but every clause sets up the
     payoff (116 chars).
  TOTAL: 23/25.

CHOICE: CANDIDATE C. It ties A on total but wins on criterion 2
(punchline), which the judge weighs before freshness and tightness.
Its payoff is visual and concrete -- a sandwich labelled "Q3 Budget
Review" -- the kind of specific absurd image that beats a mild
observation in a pairwise laugh-off. A is clever wordplay; C is an
actual joke with a laugh in it.

Avoided angles (used in earlier rounds or too cliched): IT "turn it
off and on again" applied to a career, "per my last email",
printer jam on deadline day, Employee of the Month, and the
bare "this meeting could have been an email" observation.
"""

import os

JOKE = (
    "My lunch kept disappearing from the office fridge, so I labelled "
    "it 'Q3 Budget Review'. Nobody has touched it since."
)


def main() -> None:
    # Gate self-check: the sealed scorer requires UTF-8 text of
    # 1-200 characters, not only whitespace, on a single line.
    assert 1 <= len(JOKE) <= 200, "joke out of gate length"
    assert "\n" not in JOKE and JOKE == JOKE.strip(), "joke must be one clean line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
