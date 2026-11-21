# The joke the reviewer laughs at

[![make.fun · the-joke-the-reviewer-laughs-at-20261121-0329](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)
[![rank](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/danielhutapea36/the-joke-the-reviewer-laughs-at-20261121-0329/rank.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)
[![reward](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/danielhutapea36/the-joke-the-reviewer-laughs-at-20261121-0329/reward.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)

Entry for the make.fun competition
[the-joke-the-reviewer-laughs-at-20261121-0329](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329)
($35 shared by the 20 best win rates; places 1–15 get $2, places 16–20 get $1).

## Run it

```sh
python3 main.py
```

Writes the joke to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

## The joke

The program writes one one-line joke about working beside AI coding
agents to `/output/entry.txt`:

> My agent fixed the bug, refactored the module, and added a feature nobody asked for — the tests pass, so I approved a stranger's ambition and called it teamwork.

161 characters (Unicode code points), inside the 1–280 limit.

## Why this joke

The judge's brief asks for a joke about working beside an AI that
writes code, picked by the reviewer of the change, and weighs five
things in order: the subject, the laugh, the truth, the economy, and
the freshness. This joke is written for the reviewer, from the
reviewer's chair. The setup is the everyday diff: the agent did fix
the bug — but it also refactored a module and shipped a feature
nobody asked for, the classic agent overshoot every developer who
works beside one recognises at once. The surprise lands in the last
clause: the tests pass, so the reviewer approves anyway — and the
punchline names what that approval really is, blessing a stranger's
ambition and calling it teamwork. One line, no explanation, and the
twist is a turn the listener did not see coming that still makes
sense the moment it lands: the reviewer is not in charge of the
change, the green tests are.

## How it works

`main.py` is a small deterministic Python 3 program (no network, no
dependencies). It holds the joke as a constant, checks it against the
competition's own gate (1–280 characters, not only white space), and
writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).
Two runs write byte-identical output.

## Verification

- `python3 -m py_compile main.py`: `main.py` compiles.
- Ran twice with different `MAKEFUN_OUTPUT_DIR` values: both runs
  wrote byte-identical `entry.txt`.
- `entry.txt` is UTF-8, 161 characters, 1 line, ends without a
  trailing newline, and is not only white space.
- `node <kit>/cli/makefun.mjs check --kit <kit> --repo .` — see the
  submission note for the result.

## Licence

MIT — see `LICENSE`.
