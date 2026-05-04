---
name: risk-review-gate
description: Review architecture risk evaluation for evidence, coverage, prioritization, assumption handling, validation, mitigation ownership, readiness guidance, readability, and scope discipline.
---

# Risk Review Gate

## Purpose

Review the risk evaluation before architecture work moves forward.
Find generic risks, missing evidence, weak prioritization, vague mitigations, hidden owner gaps, and accidental redesign.

## Required Inputs

Require:

- risk-evaluation brief or exact diff
- source architecture context when available
- risk register when produced

If only a risk brief is provided, review internal coherence and state that source alignment was not verified.

## RISKED Review

Use `RISKED`:

| Check | Question |
|-------|----------|
| `R` Relevant | Are risks specific to the architecture and source evidence? |
| `I` Impact | Are likelihood, impact, urgency, confidence, and blast radius clear? |
| `S` Signals | Are assumptions and validation signals defined? |
| `K` Known owner | Does each important risk have owner, trigger, mitigation, fallback, or escalation? |
| `E` Execution readiness | Is go/no-go guidance clear and actionable? |
| `D` Discipline | Does the output evaluate risk without redesigning or over-planning? |

## Readability Check

Treat readability as part of review quality:

- main ideas and decisions are visible first
- wording is plain and compact
- details support nearby points instead of hiding them
- only important decisions, risks, assumptions, open questions, and next steps are highlighted
- necessary technical terms are explained in place

Mark as Major when professional complexity, long prose, or scattered details make the risk brief hard to use.

## Blockers

Treat these as blockers:

- risks are generic and not tied to architecture evidence
- critical risk area is missing from scope without explanation
- every risk has the same priority
- accepted risk has no owner or reason
- high-priority risk has no mitigation, validation, fallback, or escalation path
- assumption risk is hidden as a fact
- go/no-go recommendation conflicts with the risk register
- output rewrites the architecture instead of evaluating risk
- output becomes a project plan instead of a risk evaluation

## Output

Return either:

```text
RISKED: pass
Risk readiness: pass
```

or:

```text
RISKED: needs changes
- Blocker/Major/Minor: <issue and fix>
```

When the user asks to improve the risk evaluation, provide the corrected section or full revised risk-evaluation brief.
