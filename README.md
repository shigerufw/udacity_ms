# Udacity Coursework

A personal workspace for studying Udacity courses with Claude Code as a study partner. It turns the original course material into study notebooks, distills them into a knowledge agent, and uses that agent to work through each topic's graded project.

## What this project does

For every topic I study, the repo holds the whole path from raw course files to a finished project:

1. **Original material.** The notebooks and files exactly as Udacity gives them.
2. **Study notebooks.** One Colab-friendly deep-dive notebook per lesson, with explanations, experiments and exercises. Also kept in Google Drive.
3. **A knowledge agent.** A single markdown file that distills what the study notebooks teach and maps it onto the topic's project. It is written as a Claude Code subagent definition, so it can be loaded as an agent or attached as context.
4. **The project.** The brief and starter files as given, and my adjusted version that follows the instructions.

The work is coursework, so Claude explains and reviews rather than handing over graded answers (see `CLAUDE.md`).

## How it works

Topics are numbered in the order I study them (`01-...`, `02-...`). Each topic is built in four steps with local Claude Code skills:

| Step | Command | Result |
|---|---|---|
| 1. Scaffold | `/scaffold-topic <topic name>` | Creates the next numbered folder with the standard structure. Picks the number, slugifies the name and refuses to touch an existing folder. |
| 2. Add the material | (manual) | Put the original platform files in `udacity_files/` and the project brief and starter files in `project/instructions/`. |
| 3. Study notebooks | `/create-study-files <topic>` | Builds one notebook per lesson topic in `study_files/`. |
| 4. Knowledge agent | `/create-agent <topic>` | Distills the study notebooks into `agent/agent-basic-knowledge.md`, including a table that maps each project step to the lessons that apply. |
| 5. Project | (manual, with the agent's help) | The adjusted project goes in `project/done/`. |

The skills live in `.claude/` (local only, gitignored), so on a fresh clone they won't exist: create the folders by hand following the structure below.

## Structure

```
udacity_ms/
├── CLAUDE.md      # rules for Claude Code in this folder
├── README.md      # this file
└── NN-<topic>/    # one numbered folder per study topic
    ├── README.md             # table explaining each folder
    ├── udacity_files/        # original files from the Udacity platform
    ├── study_files/          # study notebooks built from udacity_files/
    ├── agent/                # markdown knowledge agent used to solve the project
    └── project/
        ├── instructions/     # project brief and starter files
        └── done/             # the project adjusted to the instructions
```

Topic folders go at the workspace root unless they belong inside a course folder; numbering then counts within that folder. Empty subfolders carry a `.gitkeep` so git tracks them.

## Topics

| # | Topic | What it covers | Project |
|---|---|---|---|
| 01 | [`01-agentic-basics/`](01-agentic-basics/) | Role-based prompting, chain-of-thought and ReAct, prompt refinement, prompt chaining, LLM feedback loops | AgentsVille trip planner: a multi-agent travel assistant that plans, evaluates and revises an itinerary |
| 02 | [`02-agentic-workflows/`](02-agentic-workflows/) | Scaffolded, no material added yet | Not added yet |

Status: for `01-agentic-basics/` the udacity files, study notebooks, knowledge agent and project are all in place. `02-agentic-workflows/` is scaffolded and still empty.

## Conventions

- **README stays current.** Any change to structure, commands, dependencies or workflow updates this file in the same change.
- **Nothing that isn't mine to share.** Datasets, credentials and Udacity material I can't redistribute are not committed. `.gitignore` excludes `data/`, `*.csv`, `*.parquet`, `*.pt` and similar; each topic's README says how to get such files.
- **Commits** follow Conventional Commits (`feat(agentic-basics): ...`), and I commit only when I ask.
- **Claude Code config.** `CLAUDE.md` is tracked so the rules travel with the repo. `.claude/` (settings, skills, agents, commands, memory) and other tool config are gitignored.

## Harness

Not built yet. Course folders must not depend on each other; shared tooling will go in a `harness/` folder, and this section will document setup and commands once it exists.
