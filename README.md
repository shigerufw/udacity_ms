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
    ├── udacity_files/  # basic files from the Udacity platform
    ├── study_files/    # files I create to study the topic
    └── project/        # the topic's project
```

## Adding a study topic

Topics are numbered in the order I study them (`01-...`, `02-...`). Each has the same three subfolders shown above. Inside Claude Code, `/scaffold-topic <topic name>` creates one: it picks the next number, slugifies the name and builds the structure. It's a local skill (not in the repo), so on a fresh clone create the folders by hand. Rules are in `CLAUDE.md`.

## Courses

| Course | Folder | Status |
|---|---|---|
| _none yet_ | | |

## Harness

Not built yet. This section will document setup, commands and conventions once it exists.

## Working with Claude Code

Claude Code is configured through `CLAUDE.md` (tracked). The local agentic layer (`.claude/` and related tool config) is gitignored, so it isn't part of the repo. Skill usage rules are in `CLAUDE.md`.
