# Alien Field Notes: The Two Day Earth Review

[![Bounty](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![Rank](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/cervus-snoopy/misty-orbit-review-7k3p/rank.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![Reward](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/cervus-snoopy/misty-orbit-review-7k3p/reward.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)

A one-line review of planet Earth, written by an alien tourist who spent two days watching a very small, very earnest human ritual.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

Writes a single line of UTF-8 text (1–200 characters, no trailing newline, mode 0644) to `$MAKEFUN_OUTPUT_DIR/entry.txt` (falls back to `/output`).

## Verify

```sh
python3 main.py
wc -c /tmp/out/entry.txt
python3 -c "t=open('/tmp/out/entry.txt', encoding='utf-8').read(); print(len(t), repr(t[-1]))"
```

The program validates the line before writing (exactly one line, 1–200 characters, not only whitespace), writes it, then reads it back and checks the mode is 0644. Python 3 standard library only; no network.
