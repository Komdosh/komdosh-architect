---
name: temporary-decision-note-builder
description: Create short temporary working notes from discovered decisions to help absorb context, while clearly marking them as non-authoritative and not an ADR.
---

# Temporary Decision Note Builder

## Purpose

Create short working notes only when they help understand discovered decision context.
These notes are not architecture records.

## Required Inputs

Require:

- ADR summaries, decision constraints, or source excerpts
- reason a temporary note is useful

## Note Rules

Temporary notes must:

- be short
- be clearly marked as temporary
- list sources used
- separate confirmed decisions from assumptions
- avoid new architecture decisions
- avoid ADR language such as Accepted, Superseded, or Proposed unless quoting source status
- not be committed
- not replace source citations

Prefer returning the note in the response.
Write a temp file only when the user or workflow needs a scratch artifact.

## Output

Return:

```text
Temporary working note, not an ADR
Purpose: <why this note exists>
Sources: <paths/tools>
Confirmed decisions: <short bullets>
Assumptions: <short bullets>
Open questions: <short bullets>
Use for: <current architecture task only>
```
