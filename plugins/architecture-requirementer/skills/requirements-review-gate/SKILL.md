---
name: requirements-review-gate
description: Review software requirements for architecture readiness, completeness, self-containment, traceability, functional coverage, non-functional coverage, assumptions, risks, and future expansion support.
---

# Requirements Review Gate

## Purpose

Review a requirements brief before architecture work starts.
Find missing requirements, hidden assumptions, vague quality targets, and architecture risks.

## Required Inputs

Require:

- requirements brief or exact requirements diff
- product goal or goal summary when available
- known constraints or source context when the requirements must align with an existing product

If only a requirements brief is provided, review it for internal completeness and clearly mark that source alignment was not verified.

## RADIANT Review

Use `RADIANT`:

| Check | Question |
|-------|----------|
| `R` Rationale | Are product goals, user needs, and business outcomes clear? |
| `A` Actors | Are users, stakeholders, operators, admins, and external systems covered? |
| `D` Domain | Is domain language, data, lifecycle, and context understandable? |
| `I` Interactions | Are functional requirements, workflows, integrations, and edge cases complete? |
| `A` Attributes | Are non-functional requirements measurable and architecture-relevant? |
| `N` Next Growth | Are future expansion, support, migration, and maintainability considered? |
| `T` Traceability | Can an architect trace goals to requirements, assumptions, and open questions? |

## Readability Check

Treat readability as part of review quality:

- main ideas and decisions are visible first
- wording is plain and compact
- details support nearby points instead of hiding them
- only important decisions, risks, assumptions, open questions, and next steps are highlighted
- necessary technical terms are explained in place

Mark as Major when professional complexity, long prose, or scattered details make the document hard to use.

## Blockers

Treat these as blockers:

- no clear product goal
- functional-only requirements with no quality attributes
- quality attributes that are vague or not measurable
- hidden assumptions that materially affect architecture
- missing security, privacy, compliance, or data lifecycle requirements when the domain implies them
- missing failure paths for critical workflows
- missing support, observability, or operability requirements for a production system
- no distinction between confirmed scope, assumptions, and open questions
- requirements that prescribe a detailed architecture without enough justification
- no traceability from goals to requirements

## Findings

Classify issues:

- `Blocker`: architecture work would be misleading or unsafe.
- `Major`: architecture work can start, but a meaningful risk or gap remains.
- `Minor`: the requirements are usable but can be clearer.

## Output

Return either:

```text
RADIANT: pass
Architecture readiness: pass
```

or:

```text
RADIANT: needs changes
- Blocker/Major/Minor: <issue and fix>
```

When the user asks to improve the requirements, provide the corrected requirements section or full revised brief.
