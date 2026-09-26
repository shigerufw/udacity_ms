# agentic workflows

Topic 02 of my Udacity studies. Six lessons on the patterns that wire LLM agents into workflows, a study notebook for each, a knowledge agent that distills them, and the AI-Powered Agentic Workflow for Project Management project that applies them.

## Folders

| Folder | What goes in it |
|---|---|
| `udacity_files/` | Original files from the Udacity platform (notebooks, PDFs, CSVs, docs, scripts). The base of what we study. Check that they're mine to redistribute before committing; if not, leave them out of git and note where to get them here. |
| `study_files/` | Study notebooks (`.ipynb`, Colab-friendly) built from `udacity_files/`, one per lesson topic. Also uploaded to the topic's Google Drive folder. |
| `agent/` | Markdown agent(s) that distill what the topic taught, used to solve the project. `agent-basic-knowledge.md` covers the six lessons and maps each step of the project to them. |
| `project/instructions/` | The project brief and starter files exactly as Udacity gives them. |
| `project/done/` | The project adjusted to follow the instructions. |

## Lessons

Each lesson has one or more original class scripts (`udacity_files/`) and a study notebook that re-teaches it in a new domain (`study_files/`). The notebooks call the OpenAI API, so they are meant to be run in Colab with `OPENAI_API_KEY` set as a Colab secret. Deep dive 1 needs no key until its last section.

| # | Lesson | Class files | Study notebook |
|---|---|---|---|
| 1 | Agentic workflow fundamentals: agents as components with one interface, workflows as agents in sequence, flags, traces | `class_01-agentic.py` | `deep-dive-1-agentic-workflow-fundamentals.ipynb` |
| 2 | Prompt chaining with agents: output contracts, per-agent temperature, fan-in, glue steps, gates and retries | `class_02-chaining-prompt.py`, `class_03-example_chaining.py` | `deep-dive-2-prompt-chaining-with-agents.ipynb` |
| 3 | Routing: specialist agents, LLM routers, validation and fallback, prerequisites, embedding routers with cosine similarity | `class_04-routing.py`, `class_05-example_routing.py` | `deep-dive-3-routing.ipynb` |
| 4 | Parallelization: sectioning and voting, threads and `ThreadPoolExecutor`, fan-in, failure modes | `class_06-Parallelization.py` | `deep-dive-4-parallelization.ipynb` |
| 5 | Evaluator-optimizer: generator and evaluator, hard and soft checks, bounded loop, conflicting constraints | `class_06-evaluator optimizer.py` (setup only) | `deep-dive-5-evaluator-optimizer.ipynb` |
| 6 | Orchestrator-workers: dynamic plans in XML tags, a robust parser, worker dispatch, synthesis | `class_07-orchestrator.py` | `deep-dive-6-orchestrator-workers.ipynb` |

Embedding-based routing (lesson 3) and the full evaluator-optimizer loop (lesson 5) go beyond the class files because the project needs them. Each notebook ends with exercises whose core is left for me to write, and the class scripts with `TODO`s (parallel contract analysis, the orchestrator's `get_worker`) are still mine to solve.

## Knowledge agent

`agent/agent-basic-knowledge.md` is a Claude Code subagent (tools: Read, Grep, Glob, Bash, Edit) that acts as a coach for the project. It contains:

- **What we learned:** a condensed version of the six lessons (concept, patterns, pitfalls).
- **The project:** the seven agent classes of Phase 1, the twelve TODOs of Phase 2, deliverables, constraints, and a list of things in the starter code worth checking early.
- **From knowledge to project:** a table mapping each project step to the lessons that apply and how to apply them.
- **Working rules:** it guides with hints, checks and reviews and does not hand over graded code unless asked, verifies claims against the course files, and never hardcodes API keys.

## Project: AI-Powered Agentic Workflow for Project Management

For the fictional client InnovateNext Solutions, in two phases. Brief and starter files are in `project/instructions/`, my solution goes in `project/done/`.

- **Phase 1:** a reusable `workflow_agents` package with seven agent classes (`DirectPromptAgent`, `AugmentedPromptAgent`, `KnowledgeAugmentedPromptAgent`, `RAGKnowledgePromptAgent` (provided), `EvaluationAgent`, `RoutingAgent`, `ActionPlanningAgent`), each with a test script and its output.
- **Phase 2:** `agentic_workflow.py`, a general-purpose workflow that turns the Email Router product spec into user stories, features and engineering tasks, using an action planning agent, a routing agent and knowledge agent plus evaluation agent pairs for the Product Manager, Program Manager and Development Engineer.

| Project part | Lessons used |
|---|---|
| Direct, augmented and knowledge-augmented agents | 1 |
| Evaluation agent | 5 |
| Routing agent | 3 |
| Action planning agent | 2, 6 |
| The Phase 2 workflow and its support functions | 1, 2, 3, 5 |
