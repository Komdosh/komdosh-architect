---
name: decision-drift-detector
description: Compare current architecture work against discovered ADRs and decisions to find conflicts, drift, missing alignment, superseded assumptions, forbidden paths, and decisions needing review.
---

# Decision Drift Detector

## Purpose

Find when current work conflicts with existing decisions.
Drift is cheaper to catch before a design is finalized.

## Required Inputs

Require:

- extracted decision constraints
- current architecture brief, diff, plan, or proposal

## Drift Checks

Check for:

- direct conflict with accepted ADRs
- use of rejected alternatives
- assumptions that contradict current decision records
- missing follow-up required by an ADR
- ignored revisit triggers
- decisions based on superseded ADRs
- unclear status that affects current design
- gaps where a new future ADR may be needed

## Output

Return:

| Finding | Severity | Current work | Decision source | Why it matters | Suggested next step |
|---------|----------|--------------|-----------------|----------------|---------------------|

Severity:

- `Blocker`: current work conflicts with an accepted decision or uses a rejected path.
- `Major`: alignment is unclear and could change architecture direction.
- `Minor`: context should be cited or clarified.

Then list:

- safe alignments
- drift risks
- source gaps
- decisions needing architect review
