# Udacity Coursework

Workspace for my Udacity courses, one folder per course, with a small shared harness planned on top. This README grows as the project does.

## Structure

```
udacity_ms/
├── CLAUDE.md      # rules for Claude Code in this folder
├── README.md      # this file
├── <course-slug>/ # one folder per course (none yet)
└── NN-<topic>/    # one numbered folder per study topic (see below)
    ├── README.md
    ├── udacity_files/        # original files from the Udacity platform
    ├── study_files/          # study notebooks I build from udacity_files/
    ├── agent/                # markdown agent(s) distilling what I learned
    └── project/
        ├── instructions/     # project brief and starter files
        └── done/             # the project adjusted to the instructions
```

## Adding a study topic

Topics are numbered in the order I study them (`01-...`, `02-...`). Each has the same subfolders shown above. The workflow for a topic:

1. `/scaffold-topic <topic name>` creates the numbered folder: it picks the next number, slugifies the name and builds the structure.
2. Put the original platform files in `udacity_files/`.
3. `/create-study-files` builds one Colab-friendly study notebook per lesson topic in `study_files/`.
4. `/create-agent` distills the study notebooks into a markdown agent in `agent/`, used to solve the project.
5. The project brief and starter files go in `project/instructions/`; the adjusted project goes in `project/done/`.

These are local skills (not in the repo), so on a fresh clone create the folders by hand. Rules are in `CLAUDE.md`.

## Courses

| Course | Folder | Status |
|---|---|---|
| _none yet_ | | |

Study topics so far: `01-agentic-basics/` (role-based prompting, chain-of-thought and ReAct, prompt refinement, prompt chaining, feedback loops; project: AgentsVille trip planner).

## Harness

Not built yet. This section will document setup, commands and conventions once it exists.

## Working with Claude Code

Claude Code is configured through `CLAUDE.md` (tracked). The local agentic layer (`.claude/` and related tool config) is gitignored, so it isn't part of the repo. Skill usage rules are in `CLAUDE.md`.
