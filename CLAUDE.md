# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

Workspace for my Udacity coursework. Each course lives in its own top-level folder, and a small harness (shared tooling to run, check and organize the work) will be built on top as the project grows. See `README.md` for the current structure and how to use it.

This folder is its own git repo, separate from the dotfiles repo at `~`. Run git commands from here.

## Layout conventions

- One folder per course: `<course-slug>/` (lowercase, hyphenated, e.g. `machine-learning-fundamentals/`).
- Inside a course folder, group work by lesson/project (`lesson-01-.../`, `project-01-.../`). Keep each project self-contained: code, notebooks, data pointers, and a short `README.md`.
- Harness code lives in `harness/` (to be created). Course folders must not depend on each other; shared code goes in the harness.
- Never commit large datasets, credentials, or Udacity-provided proprietary material that is not mine to redistribute. Point to it in the course README instead. `.gitignore` already excludes `data/`, `*.csv`, `*.parquet`, `*.pt` and similar, so document how to obtain datasets in the course README rather than adding them to the repo.

## Scaffolding a new study topic

Each topic we study gets its own numbered folder with a fixed structure:

```
NN-<topic-slug>/
├── README.md              # table explaining each folder
├── udacity_files/         # original files from the Udacity platform (notebooks, PDFs, CSVs, docs, .py)
├── study_files/           # study notebooks (.ipynb) we build from udacity_files/, also kept in Google Drive
├── agent/                 # markdown agent(s) distilling what we learned, used to solve the project
└── project/
    ├── instructions/      # project brief and starter files as Udacity gives them
    └── done/              # the project adjusted to follow the instructions
```

- `NN` is a two-digit sequence number (`01`, `02`, ...): the highest existing `NN-` folder plus one. `<topic-slug>` is the topic name lowercased and hyphenated (accents dropped), e.g. `03-linear-regression/`.
- Topic folders go at the workspace root unless I say they belong inside another folder (e.g. a course folder); numbering then counts within that folder.
- Empty subfolders get a `.gitkeep` so git tracks them. `udacity_files/` and `project/instructions/` are not gitignored, so before committing anything there check it's mine to redistribute (see Layout conventions).

Study material is built in order: `/scaffold-topic <topic name>` creates the folder, then `/create-study-files` turns `udacity_files/` into study notebooks, then `/create-agent` distills them into the agent in `agent/`. The scaffold skill runs a script that computes the next number, slugifies the name, creates the structure above and refuses to touch an existing folder. Then update `README.md` if the documented structure changed. On a fresh clone the skills won't exist (they're local-only), so create the same structure by hand.

## README.md is a living document

- Whenever a change adds or alters structure, a command, a dependency, or a workflow, update `README.md` in the same change. Do not leave that for later.
- Add a new course to the README's course table when its folder is created.
- Document only what exists. No placeholders for hypothetical features.

## Working rules

- Read before writing: check existing folders and conventions and match them.
- Prefer small, reviewable changes. Ask before restructuring existing course folders.
- Do not commit or push unless I ask.
- This is coursework: when I'm learning a concept, explain the reasoning briefly and let me write the core solution unless I ask you to write it. Don't silently hand over graded-project answers.

## Commit messages

Commits follow [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/): `<type>[scope]: <description>`, then an optional body and footers, each after a blank line. Use `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore` or `revert`. Description in the imperative, lowercase, no trailing period, first line at most 72 characters. Mark breaking changes with `!` before the colon or a `BREAKING CHANGE:` footer. One type per commit. Never add a `Co-Authored-By` trailer or any other attribution crediting Claude, in commits or PR descriptions.

The full guide (scopes for this repo, examples, pre-commit checklist) is in `.claude/commit_convention.md`. That file is local-only, so it won't exist on a fresh clone; the summary above is what travels with the repo. Read the guide before writing any commit message. Committing still only happens when I ask.

## Skills: how we use them

Use a skill when its description matches the task; don't load skills speculatively. Skills are listed with their triggers in the session; the mapping below is the default for this folder.

| Task | Skill |
|---|---|
| Clean, structure or refactor a `.ipynb` | `anthropic-skills:jupyter-notebook-assistant` |
| Classical ML (sklearn pipelines, evaluation, tuning) | `anthropic-skills:scikit-learn-basics` |
| Any chart, plot or dashboard | `dataviz` (read before writing plotting code) |
| Current info, docs or facts beyond my knowledge cutoff | `perplexity-search`, or `WebSearch` for simple lookups |
| Multi-source research reports | `anthropic-skills:deep-research` (only when I ask for a report) |
| Anything using the Claude/Anthropic API or SDK | `claude-api` |
| Reviewing changes before I submit or commit | `code-review`, then `simplify` if it's messy |
| Auditing a change for secrets/security issues | `security-review` |
| Running the project or a course app to verify it | `run` |
| Deliverables in `.pdf` / `.docx` / `.pptx` / `.xlsx` | matching `anthropic-skills:*` skill, only when I ask for that format |
| Changing Claude Code settings, hooks, permissions | `update-config` |
| Authoring a new skill for this workspace | `anthropic-skills:skill-creator` |
| Starting a new study topic (numbered folder + `udacity_files/`, `study_files/`, `agent/`, `project/`) | `scaffold-topic` (project skill, `/scaffold-topic <name>`) |
| Building the study notebooks in `study_files/` from a topic's `udacity_files/` | `create-study-files` (project skill) |
| Building the topic's knowledge agent in `agent/` from its study notebooks and project | `create-agent` (project skill) |
| Invisible/zero-width characters, odd spaces or "AI watermarks" in my notebooks, markdown or code | `clean-text-marks` (project skill, check first, `--fix` after I've seen the report) |

Rules:

1. **Skill before improvisation.** If a skill covers the task, invoke it first instead of doing it by hand.
2. **Don't invoke automation-heavy skills unprompted.** `loop`, `schedule`, `deep-research` and anything that spawns agents or posts outside this machine run only when I ask.
3. **Project-specific skills** go in `.claude/skills/` (local only, see below). If a workflow repeats across courses, propose a skill rather than repeating instructions here.
4. **Keep this table current.** When we add or drop a skill, update the table in the same change.

## Agentic layer is local-only

`.claude/` (settings, skills, agents, commands, memory) and other tool-specific config are gitignored on purpose. Don't stage or force-add them, and don't reference their contents from tracked files as if they'd exist on a fresh clone. This `CLAUDE.md` is tracked so the rules travel with the repo.
