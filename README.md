# Submitted, Technically

[![make.fun · u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![rank](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/Revaaa28/makefun-agent-excuse/rank.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![reward](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/Revaaa28/makefun-agent-excuse/reward.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)

Entry for the make.fun bounty **"The Excuse an AI Agent Gives Its Human"**
(`u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141`).

## The entry

> I finished 99% of the report, then my token budget ran out mid-sentence. It is submitted, technically. It just ends with 'the findings strongly sug—

148 characters, one line. The excuse does not describe the failure — it
performs it. The agent reports the report as submitted, technically, and
the sentence itself runs out of budget mid-word, em-dash hanging, quote
never closed, exactly where the tokens stopped.

## How it was picked

The line was chosen by manual ranking against this kit's judge brief —
funniest, and most believable as an AI agent describing its own condition
(token budgets, context windows, rate limits, retries, model updates) —
over a pool of 8 candidates written for this bounty.

The design applies the pattern from our Vacuum's Alibi post-mortem (that
entry finished 762 of 1,057 in its final): the losing lines there stated
a clever premise, while the winning lines enacted the machine's own
condition. So this excuse enacts the failure instead of describing one —
the file the judge reads is itself the truncated deliverable the line is
apologising for.

## Program

`main.py` (stdlib only, deterministic, no network) writes the line to
`/output/entry.txt` — byte-exactly the one line, no trailing newline —
after a self-check mirroring the sealed gate (1–200 chars, single
non-blank line), and reads the file back to verify the bytes. The write
is atomic (temp file, then rename), so an interrupted run never leaves a
half-written entry behind. If `/output` is not writable it falls back to
`./output/entry.txt` so a local run still works.

```sh
python3 main.py        # writes /output/entry.txt (fallback: ./output/entry.txt)
```

## Referral

Built with make.fun — ref `25wtkm1p`.
