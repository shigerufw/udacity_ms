---
title: "Harness Engineering with Claude and Claude Code Project"
source: "https://learn.udacity.com/nd7426?version=1.0.70&partKey=cd15315&lessonKey=28f00d79-5c6d-40bf-afa0-624f48875a62&conceptKey=e282152b-5cf2-4716-806d-f17decdbece3"
author:
published:
created: 2026-11-22
description:
tags:
  - "clippings"
---
## Instructions

## Project Instructions

Work through the tasks in order. Task 1 gets all four environments healthy. Tasks 2–5 run each system and capture its evidence. Tasks 6–7 organize the evidence and complete the brief.

Every task maps to a rubric criterion. Keep every terminal log and run artifact — you submit them.

![[Pasted image 20261122114615.png]]

Complete these in order. Tasks 2–5 each produce an evidence artifact; task 7 produces your brief.

## Verify Your Implementation

Run each scenario and confirm the output before submitting.

**Tests pass**

```bash
pytest tests/ -v # run inside each system's own venv → 30, 30, 35, 33
```

**Agentic loop** — `python -m claims_intake.run --all` → `runs/<ts>/` with `summary.md`, `traces/`, `queues/*.jsonl`, `escalations.jsonl`; exit 0.

**Context strategy** — `python -m retail_context.run --all` → `budget.json` ≥50% reduction; `eval.jsonl` ≥5/6; control regresses on ≥1.

**Claude Code config** — `python -m ecommerce_team_config .` → `OK`, exit 0.

**Orchestrated shift** — `run-shift … --since 2026-04-01T00:00:00Z --recorded-response …` → `shift C: 17 new defects`, summary prints; `hot_state.json` updates, under ~5 KB; a line appends to `shift_scratchpad.jsonl`.

## Writing the Brief

Two rules separate a passing brief from a generic one:

- **Cite your own artifacts.** Every answer references something only your runs produced — a run ID, a token count from `budget.json`, a claim outcome from `summary.md`, the size of `hot_state.json`, a trace line. An answer identical for every learner does not pass.
- **Synthesize across systems.** Part 2 asks you to connect two or more systems: locate the three layers, contrast deterministic enforcement with prompt guidance, compare context management within one conversation vs across sessions.

## Submission Instructions

Confirm you have included:

Package the four evidence folders (system1/tosystem4/) and the brief at the top level of one.zip, with no wrapper folder, and submit.

## How It's Evaluated

Your reviewer checks two things: that the evidence shows all four systems built, run, and passing tests; and that the brief is accurate and grounded in that evidence. Cited numbers are cross-checked against your artifacts.

Valid runs vary — token counts, turns, and outcomes differ by model and input. There is no single correct set of numbers. What matters is that your analysis fits the behavior *your* runs produced. See the project rubric in the classroom for full criteria and stand-out suggestions.