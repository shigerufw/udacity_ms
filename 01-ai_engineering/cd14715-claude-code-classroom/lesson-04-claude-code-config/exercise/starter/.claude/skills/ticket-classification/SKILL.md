---
name: ticket-classification
description: Classify support tickets by urgency and category and decide routing. Use when analyzing tickets, determining priority, assigning urgency, categorizing customer requests, or routing tickets to Engineering, Finance, Support or Escalation.
allowed-tools: Read, Grep, Glob
---

# Ticket Classification

This skill teaches Claude how to classify a customer support ticket by urgency and category, route it to the right team, and calculate its SLA deadline.

## When to Use This Skill

Use this skill when the user requests:
- "Analyze the ticket in sample-tickets/technical.txt"
- "Classify all tickets and route appropriately"
- "What urgency is this ticket?"
- "Which team should handle this request?"

## Classification Matrix

### Urgency Levels

| Level | Criteria | Response Time |
|-------|----------|---------------|
| **URGENT** | Total system outage, security breach, data loss | Immediate |
| **HIGH** | Core feature broken, or Enterprise customer affected in production | < 1 hour |
| **MEDIUM** | Feature degraded, workaround available, billing discrepancy | < 4 hours |
| **LOW** | How-to questions, minor bugs, feature requests | < 24 hours |

### Urgency Keywords

**URGENT urgency indicators:**
- "system down", "complete outage", "everything is down"
- "security breach", "unauthorized access", "data leak"
- "data loss", "data deleted", "lost all data"

**HIGH urgency indicators:**
- "500 error", "production", "blocking", "cannot access"
- "ASAP", "critical" (only if the impact confirms it)
- Enterprise customer with a broken core feature

**MEDIUM urgency indicators:**
- "charge", "invoice", "incorrect amount", "slow", "intermittent"
- "workaround", "sometimes fails", "need clarification before payment"

**LOW urgency indicators:**
- "how to", "where can I find", "is there a way"
- "not urgent", "planning", "feature request", "suggestion"

### Category Classification

**Technical Category:**
- Errors, stack traces, HTTP codes (500, 404, timeout)
- API endpoints, integrations, webhooks, database or connection problems

**Billing Category:**
- Invoices, charges, payments, refunds
- Subscription plans, pricing, usage limits tied to cost

**General Category:**
- How-to questions and feature inquiries
- Account settings, data export, dashboard navigation

## Classification Process

1. Read the full ticket and note the customer name, tier, submitted time and description.
2. Identify the real impact: how many users, production or not, data or security risk.
3. Match the impact and keywords to the urgency matrix and pick one level.
4. Pick the category from the problem itself (technical, billing, general).
5. Route: technical → Engineering, billing → Finance, general → Support. URGENT, or a ticket that itself states its SLA was breached → Escalation. Never infer a breach by comparing the submitted time with today's date.
6. Calculate the SLA deadline: Enterprise at most 1 hour, Standard by urgency time.

## Examples

### Example 1: Technical - HIGH

```
Subject: 500 Errors on API Endpoint
Body: Acme Corp (Enterprise). Our production app gets 500 errors on /api/v2/users
for the last 2 hours. About 5,000 users cannot access dashboards.
"Database connection timeout". We need this resolved ASAP.
```

**Classification:**
- Urgency: HIGH
- Category: technical
- Routing: Engineering
- Reasoning: Enterprise customer with a core endpoint failing in production. It is not URGENT because the whole system is not down and there is no data loss or security issue.

### Example 2: Billing - MEDIUM

```
Subject: Question about invoice charges
Body: Small Business Co (Standard). Invoice shows $500 but our Professional plan
is $400/month. What is the extra $100? I want this clarified before payment
processes next week.
```

**Classification:**
- Urgency: MEDIUM
- Category: billing
- Routing: Finance
- Reasoning: A charge discrepancy that needs an answer within days, with no service impact. Standard tier, so the 4-hour window applies.

### Example 3: General - LOW

```
Subject: How to export data to CSV
Body: TechStartup Inc (Standard). I can't find the export option in the
dashboard. Is there a way to export to CSV or JSON? Not urgent, just planning
for next month.
```

**Classification:**
- Urgency: LOW
- Category: general
- Routing: Support
- Reasoning: A how-to question with no impact, and the customer says it is not urgent.

### Example 4: Technical - URGENT

```
Subject: Customers can see other accounts' data
Body: Beta Corp (Enterprise). Several of our users report seeing another
company's records after login. This looks like a security breach.
```

**Classification:**
- Urgency: URGENT
- Category: technical
- Routing: Escalation
- Reasoning: Possible security breach and data exposure. Escalate immediately.

## Output Format

Return the classification as JSON using the exact values below.

```json
{
  "urgency": "URGENT|HIGH|MEDIUM|LOW",
  "category": "technical|billing|general",
  "routing": "Engineering|Finance|Support|Escalation",
  "customer_tier": "Enterprise|Standard",
  "sla_deadline": "Timestamp or response window"
}
```

## Quality Checklist

Before finalizing classification, verify:

- [ ] Urgency is based on impact, not only on the customer's wording
- [ ] Customer tier was read from the ticket and applied to the SLA
- [ ] Category matches the problem itself, not the department that sounds closest
- [ ] Routing follows from category and urgency (Escalation for URGENT)

## Tips

**Finding urgency indicators:**
- Look for scale ("5,000 users"), environment ("production") and duration ("2 hours").
- Look for explicit calming words such as "not urgent" or "planning".

**Categorizing accurately:**
- Error messages and stack traces point to technical.
- Money words (invoice, charge, plan) point to billing.

**Routing decisions:**
- Route by category first, then check whether urgency requires Escalation.
- The Enterprise tier shortens the SLA but does not by itself make a ticket URGENT.

## Common Pitfalls

❌ **Don't:**
- Mark a ticket URGENT just because it says "ASAP"
- Ignore the customer tier
- Classify a billing question as technical because it mentions an "error" in passing

✅ **Do:**
- Weigh scope and impact before choosing urgency
- Use only the allowed values for each field
- Explain the reasoning briefly when asked
