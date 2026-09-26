# agentic_basics

Topic 01 of my Udacity studies. Five lessons on prompting techniques for LLM agents, a study notebook for each, a knowledge agent that distills them, and the AgentsVille Trip Planner project that applies them.

## Folders

| Folder | What goes in it |
|---|---|
| `udacity_files/` | Original files from the Udacity platform (notebooks, PDFs, CSVs, docs, scripts). The base of what we study. Check that they're mine to redistribute before committing; if not, leave them out of git and note where to get them here. |
| `study_files/` | Study notebooks (`.ipynb`, Colab-friendly) built from `udacity_files/`, one per lesson topic. Also uploaded to the topic's Google Drive folder. |
| `agent/` | Markdown agent(s) that distill what the topic taught, used to solve the project. `agent-basic-knowledge.md` covers the five lessons and maps each step of the AgentsVille project to them. |
| `project/instructions/` | The project brief and starter files exactly as Udacity gives them. |
| `project/done/` | The project adjusted to follow the instructions. |

## Lessons

Each lesson has an original Udacity notebook (`udacity_files/`) and a study notebook that goes deeper (`study_files/`).

### 1. Role-based prompting

Tell the model who it is in the system message, so it samples the kind of text a person in that role would write.

- **Notebooks:** `udacity_files/lesson-1-role-based-prompting.ipynb` (an Einstein interviewer, built up step by step), `study_files/deep-dive-1-role-based-prompting.ipynb`
- **Learnings:**
  - A structured persona (role, expertise, audience, tone, constraints) beats a one-line role.
  - A role changes vocabulary, depth and framing, but does not guarantee correctness.
  - Personas drift over long conversations, so re-inject them, and sensitive domains need explicit guardrails.
  - Different personas on the same question give different perspectives, which is useful for brainstorming.

### 2. Chain-of-Thought (CoT) and ReAct

CoT asks for the reasoning before the answer. ReAct interleaves reasoning with tool calls.

- **Notebooks:** `udacity_files/lesson-2-chain-of-thought-and-react-prompting-part-i.ipynb` (CoT, demand-spike detective), `udacity_files/lesson-2-chain-of-thought-and-react-prompting-part-ii.ipynb` (ReAct), `study_files/deep-dive-2-chain-of-thought-and-react.ipynb`
- **Learnings:**
  - Reasoning tokens are scratch space, because the model generates left to right and its own reasoning becomes context.
  - CoT levels: direct, zero-shot ("think step by step"), few-shot, and structured (reasoning followed by a parseable JSON block).
  - ReAct loop: Thought, Action (exactly one tool call), Observation (written by Python, never by the model), repeated until a `final_answer` call.
  - Always cap the number of steps, return parse errors as observations so the model can recover, and never use bare `eval` for a calculator tool.
  - Use a single CoT call when the data fits in the prompt, and ReAct when it needs lookups or computation.

### 3. Prompt instruction refinement

Prompt engineering as a cycle: draft, run, evaluate, find the weakest component, refine.

- **Notebooks:** `udacity_files/lesson-3-prompt-instruction-refinement.ipynb` (recipe vs. dietary restriction classifier), `study_files/deep-dive-3-prompt-instruction-refinement.ipynb` (a product description refined from V0 to V5)
- **Learnings:**
  - Components: role, context, task, output format, constraints, positive and negative examples, evaluation criteria.
  - Add one component at a time and re-measure, so you learn which part carries the result.
  - Few-shot examples help with complex formats, and negative examples help when one specific error keeps recurring.
  - A rubric-based LLM evaluator that returns JSON scores lets you measure improvements instead of judging by eye.
  - Ablation (removing one component) shows what actually matters.

### 4. Chaining prompts

Split a complex task into focused prompts, each output feeding the next.

- **Notebooks:** `udacity_files/lesson-4-chaining-prompts-for-agentic-reasoning.ipynb` (insurance first-notice-of-loss triage: extraction, severity, routing), `study_files/deep-dive-4-chaining-prompts.ipynb`
- **Learnings:**
  - One job per step, structured data between steps, and a retry cap.
  - Gate checks between stages stop garbage from propagating: format gate (valid JSON, keys present), logic gate (self-consistent), LLM gate (a model judges quality).
  - Also covered in the study notebook: branching (a classifier picks the next prompt) and fan-out/fan-in (specialist prompts, then a synthesis prompt).

### 5. LLM feedback loops

Generate, evaluate, feed the failures back into a new generation, repeat until it passes or the budget runs out.

- **Notebooks:** `udacity_files/lesson-5-implementing-llm-feedback-loops.ipynb` (code-generation assistant with tests), `study_files/deep-dive-5-llm-feedback-loops.ipynb`
- **Learnings:**
  - Feedback sources: rule-based checks, code execution with tests, an LLM critic, self-critique, or a mix.
  - Prefer deterministic code checks, and pass the failing checks back verbatim.
  - Always set a max iteration count, detect stuck loops (same failure twice), and log every iteration.

## Knowledge agent

`agent/agent-basic-knowledge.md` is a Claude Code subagent (tools: Read, Grep, Glob, Bash, Edit) that acts as a coach for the AgentsVille project. It contains:

- **What we learned:** a condensed version of the five lessons above (concept, pattern, pitfalls).
- **The project:** goal, provided helpers in `project_lib.py`, the mocked APIs and their data range, setup constraints, and the seven notebook steps.
- **From knowledge to project:** a table mapping each project step to the lessons that apply and how to apply them.
- **Working rules:** it guides with hints, checks and reviews and does not hand over graded code unless asked, verifies claims against the course files, and never hardcodes API keys.

## Project: AgentsVille Trip Planner

A multi-agent travel assistant. It builds a day-by-day `TravelPlan` for the fictional city of AgentsVille from traveler details, weather and activities, evaluates the plan, then revises it with a ReAct agent until it passes all evals and honors the traveler feedback. Brief and starter files are in `project/instructions/`, my solution in `project/done/`.

| Project step | Lessons used |
|---|---|
| Itinerary agent prompt (structured persona, step-by-step task, two-section output) | 1, 2, 3, 4 |
| Weather-compatibility eval (LLM judge) | 1, 3, 4 |
| Tools and their docstrings | 2, 5 |
| Revision agent (ReAct loop driven by eval feedback) | 2, 5 |
