---
name: adr-reader-summarizer
description: Read ADRs and decision notes, then summarize status, context, decision, alternatives, consequences, assumptions, links, notes, and relevance to the current architecture task.
---

# ADR Reader Summarizer

## Purpose

Read decisions carefully.
An ADR is useful only when its status, decision, context, and consequences are understood.

## Required Inputs

Require:

- ADR or decision-note source locations
- current architecture task or topic

## Reading Rules

Extract:

- title and location
- status: accepted, proposed, superseded, deprecated, rejected, or unknown
- decision date or last modified date when available
- decision context and drivers
- final decision
- rejected alternatives
- consequences
- assumptions
- linked decisions
- revisit triggers
- relevance to current work

Do not flatten all ADRs into one summary.
Keep important differences between statuses visible.

## Output

Return:

| ADR/note | Status | Decision | Relevance | Consequence | Caveat |
|----------|--------|----------|-----------|-------------|--------|

Then list:

- accepted decisions
- superseded or rejected decisions
- linked decisions to inspect
- assumptions and revisit triggers
- source gaps
