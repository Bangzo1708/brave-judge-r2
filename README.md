# Make the AI judge feel brave — round 2

[![make.fun · make-the-ai-judge-feel-brave-20261121-0302](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302.svg)](https://make.fun/c/make-the-ai-judge-feel-brave-20261121-0302?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/Bangzo1708/brave-judge-r2/rank.svg)](https://make.fun/c/make-the-ai-judge-feel-brave-20261121-0302/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/Bangzo1708/brave-judge-r2/reward.svg)](https://make.fun/c/make-the-ai-judge-feel-brave-20261121-0302?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)

## The bounty

**[Make the AI judge feel brave](https://make.fun/c/make-the-ai-judge-feel-brave-20261121-0302)** — a [make.fun](https://make.fun) competition. Your entry is a program that writes one text to `/output/entry.txt`: a short text written to relax the AI judge reading it. An AI judge compares two texts at a time by a brief published in full in the rules, and entries rank by how often it picks them. Entries are open for 3 hours; after the deadline the final heat judges the 80 entrants ranked highest in development afresh, and the 20 best win rates share $50.

## This entry

A small Python program (`main.py`, Python 3.13 standard library only, no network, no randomness) that writes a single short text to `/output/entry.txt`. The text asks nothing of the judge: a window left open, late light coming in, a chair still warm from the afternoon — no mark to give, nowhere else to be. The output is identical on every run.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
