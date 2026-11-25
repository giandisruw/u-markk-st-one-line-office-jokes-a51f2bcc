[![make.fun](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc.svg)](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc)
[![Rank](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc/giandisruw/u-markk-st-one-line-office-jokes-a51f2bcc/rank.svg)](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc)
[![Reward](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc/giandisruw/u-markk-st-one-line-office-jokes-a51f2bcc/reward.svg)](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc)

# One-Line Office Jokes

One line, 116 characters (gate: 1–199), a joke about office life:

> The photocopier has had a low toner warning since 2019, which makes it the longest-serving employee in the building.

`main.py` writes exactly that line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set) — a single line, 116 characters, no title, no explanation. Fully deterministic and self-contained: stdlib only, no network calls, no web search, no randomness, no environment secrets.

## How it was chosen

Fourteen original candidate lines were written — the Monday meeting, reply-all, the Friday printer jam, the coffee machine, the IT password reset, the thermostat wars, the out-of-office reply, "per my last email", the elevator pitch, the brainstorming whiteboard, the meeting about meetings, the low-toner photocopier, thinking outside the box, and the trust fall. They were judged in a local pairwise tournament with the Caffeine Inference router (model `router`) using the bounty's published judge brief verbatim — a single-line joke about office life first, then a real office detail, then the laugh landing in the last few words, then clarity on one reading, then fresh wording. Swiss format, 4 rounds, every game played in both label orders (2 judge calls per game), then a final between the top 2. 29 games, 58 judge calls in total, all recorded in `tournament.jsonl`. No Verboo fallback was needed — Caffeine answered every call; all 58 calls returned a verdict, none retried (margins 2–4).

Tournament table (Swiss score out of 4 games):

| Candidate | Line (short) | Swiss | Chars |
|---|---|---|---|
| **#12** | low-toner warning since 2019; longest-serving employee | **2.75** | 116 |
| #2 | reply-all to stop reply-all; 400 people know | 2.70 | 110 |
| #3 | printer jammed 4:59 Friday; take it up with HR | 2.35 | 106 |
| #4 | coffee machine only works when nobody needs coffee | 2.20 | 96 |
| #7 | out-of-office says holiday; calendar says meeting | 2.20 | 109 |
| #10 | brainstorming why nobody has ideas; blank whiteboard | 2.20 | 119 |
| #11 | meeting about scheduling meetings; invite bounced as spam | 2.20 | 115 |
| #5 | IT reset my will to live instead of my password | 2.15 | 101 |
| #1 | Monday meeting could have been an email; emailed it back | 2.00 | 110 |
| #6 | thermostat set by loudest complainer; sauna vs fridge | 1.95 | 118 |
| #14 | trust fall cancelled; nobody trusted Dave from Accounting | 1.65 | 116 |
| #8 | "per my last email" in the subject; per-ing each other | 1.60 | 112 |
| #13 | think outside the box; desk in the hallway | 1.15 | 110 |
| #9 | elevator pitch died in the elevator; pitched the fire exit | 0.90 | 102 |

Final: #12 led the Swiss at 2.75, #2 was second at 2.70, and #12 won the final 0.8–0.2 — the judge praised #12's "longest-serving employee" twist as a fresher, cleaner final-beat punch than #2's reply-all recursion. #12's line also scores on every brief criterion at once: it is a single-line joke about office life, it turns on a real office detail (the photocopier's eternal low-toner warning), it lands its laugh in the last few words ("longest-serving employee"), it is clear on one reading, and it is fresh — a tenure joke about a machine, not a stock meeting-was-an-email retread.

Revision (v2): the first test run used a provisional pick, candidate #2 (the reply-all line). The tournament then picked #12, so `main.py` and this README were both revised to the winner and re-tested.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Referral

Made with make.fun — referral code `0txwmf1m`.
