---
description: "Intelligent support ticket routing system that classifies tickets by urgency and category and routes them to the right team"
tools:
  - bash
  - read
  - grep
  - glob
---

# Support Ticket System

Intelligent support ticket routing: Claude reads incoming tickets, decides how urgent they are and what kind of problem they describe, and sends each one to the right team.

## Project Overview

This system analyzes and routes 5,000+ support tickets every day.

**Main features:**
- **Classification**: assigns each ticket an urgency (URGENT, HIGH, MEDIUM, LOW) and a category (technical, billing, general)
- **Routing**: sends the ticket to Engineering, Finance, Support, or Escalation
- **SLA monitoring**: calculates the response deadline from the customer tier (Enterprise or Standard)

**Target users:**
- Support teams, who get tickets pre-sorted and prioritized
- Customers, who get faster, more accurate responses

## Architecture

This system uses:
- **`ticket-analyzer` subagent** (`.claude/agents/ticket-analyzer.md`): a specialist that reads one ticket and returns a JSON analysis (urgency, category, routing, summary, recommended action, SLA deadline). It is limited to read-only tools (Read, Grep, Glob) and runs on a fast, low-cost model (Haiku) because it handles high volume.
- **`ticket-classification` skill** (`.claude/skills/ticket-classification/SKILL.md`): the domain knowledge the analyzer relies on: the urgency matrix, urgency keywords, category rules, and worked examples.

```
User request
    │
    ▼
CLAUDE.md (project context + SLAs)
    │
    ▼
ticket-analyzer subagent ──uses──▶ ticket-classification skill
    │
    ▼
JSON result → routing (Engineering | Finance | Support | Escalation)
```

## How to Use

```bash
# Analyze a single ticket
claude "Analyze the ticket in sample-tickets/technical.txt"

# Classify all tickets and route them
claude "Classify all tickets in sample-tickets/ and route appropriately"

# Check SLA status
claude "Check the SLA deadline for each ticket in sample-tickets/ based on customer tier"
```

## Ticket Categories

- **Technical** (routed to Engineering): errors, API failures, timeouts, integrations
- **Billing** (routed to Finance): payments, invoices, subscriptions, refunds
- **General** (routed to Support): how-to questions, account settings, feature inquiries

## SLA Requirements

- **Enterprise customers**: response in under 1 hour
- **Standard customers**: response in under 4 hours (LOW urgency tickets: under 24 hours)
- **URGENT tickets** (system down, security breach, data loss): immediate response and escalation, regardless of tier

## System Instructions

When analyzing support tickets:

1. Delegate each ticket to the `ticket-analyzer` subagent, which applies the `ticket-classification` skill.
2. Read the customer tier from the ticket and base urgency on real impact, not on words like "ASAP".
3. Return the result as JSON (urgency, category, routing, summary, recommended_action, sla_deadline).
4. When classifying several tickets, return one JSON result per ticket and then a short summary of how they were routed.
5. Never modify ticket files; this system only reads and classifies.

## Build Commands

There is nothing to build or install: the project is configuration only (Markdown files in `.claude/`) plus sample tickets. To test it, run the commands in "How to Use" from this folder.

## Key Takeaway

This configuration shows how to:
- Use CLAUDE.md to give Claude persistent project context, SLAs and instructions
- Use a subagent with restricted tools and a cheaper model for a focused, repeatable job
- Use a skill to package domain knowledge (classification rules and examples) that is loaded when relevant
