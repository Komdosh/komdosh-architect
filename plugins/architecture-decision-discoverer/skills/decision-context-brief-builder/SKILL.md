---
name: decision-context-brief-builder
description: Build a compact, human-readable decision-context brief from discovered ADRs, source coverage, constraints, consequences, assumptions, drift risks, and future ADR questions.
---

# Decision Context Brief Builder

## Purpose

Package discovered decisions into a brief an architect can use.
The result should be compact and decision-focused, not a full ADR catalog.

## Required Inputs

Require:

- searched source list
- ADR summaries
- extracted constraints
- drift findings or current task context when available

## Brief Rules

- cite source locations or tools
- show coverage limits
- put important constraints first
- keep rejected alternatives visible
- keep consequences near the decisions they came from
- separate confirmed decisions, inferred implications, memory-derived context, and open questions
- include future ADR candidates without writing ADR text

## Output

Return:

1. Decision context summary
2. Sources searched
3. Relevant ADRs and decision notes
4. Constraints for current work
5. Rejected alternatives and forbidden paths
6. Consequences and tradeoffs
7. Conflicts or drift risks
8. Future ADR candidates
9. Open questions
10. Architect handoff notes
