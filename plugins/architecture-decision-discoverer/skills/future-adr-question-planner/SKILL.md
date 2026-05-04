---
name: future-adr-question-planner
description: Identify architecture questions, unresolved decisions, drift risks, and design choices that likely need a future ADR, without writing or updating the ADR.
---

# Future ADR Question Planner

## Purpose

Find decisions that still need formal attention.
This skill identifies future ADR needs but does not write ADRs.

## Required Inputs

Require:

- decision context brief or extracted constraints
- current architecture task or proposal

## Future ADR Signals

Flag when:

- a current design choice is high impact and not covered by existing ADRs
- an accepted ADR has a revisit trigger that is now active
- an old assumption no longer matches current reality
- there are competing architecture options with meaningful tradeoffs
- governance, compliance, security, data, deployment, API, or operational policy may change
- teams need a recorded decision before implementation

## Output

Return:

| Question | Why it may need ADR | Related source | Urgency | Owner/next step |
|----------|---------------------|----------------|---------|-----------------|

Then list:

- future ADR candidates
- decisions that can remain informal
- review triggers
- source gaps
- what not to write yet
