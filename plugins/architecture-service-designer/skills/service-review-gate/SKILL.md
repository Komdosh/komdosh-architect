---
name: service-review-gate
description: Review a service-design brief for domain alignment, responsibility clarity, source-of-truth ownership, collaboration quality, consistency boundaries, dependency rules, adapter coverage, operational fit, and stage discipline.
---

# Service Review Gate

## Purpose

Review the service or component structure before later architecture design.
Find weak decomposition, hidden ownership, over-splitting, missing collaboration rules, and premature low-level design.

## Required Inputs

Require:

- service-design brief or exact diff
- domain model or scope summary when available
- diagrams when produced

If only a service brief is provided, review internal coherence and state that source alignment was not verified.

## STRUCT Review

Use `STRUCT`:

| Check | Question |
|-------|----------|
| `S` Scope | Does the design stay inside one bounded scope? |
| `T` Truth | Is source-of-truth ownership clear and not shared accidentally? |
| `R` Responsibility | Does every unit have clear owned and not-owned responsibilities? |
| `U` Usefulness | Does each split improve ownership, changeability, scale, security, or operability? |
| `C` Collaboration | Are contracts, sync/async choices, and process boundaries clear? |
| `T` Technical restraint | Does the output avoid low-level schema, cloud, framework, and endpoint detail? |

Also check:

- dependency direction and coupling rules
- transaction and consistency boundaries
- external adapters and anti-corruption layers
- operational ownership and support readiness
- diagram consistency

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

- central source-of-truth ownership is hidden or contradictory
- multiple units write the same authoritative state without an explicit reason
- service split is technology-layered rather than domain-responsibility-based
- design creates unavoidable chatty synchronous coupling
- critical invariant crosses boundaries without process or consistency ownership
- external provider language leaks into core domain components
- diagrams contradict the written responsibilities
- output jumps to detailed API, database, cloud, or framework design

## Output

Return either:

```text
STRUCT: pass
Service readiness: pass
```

or:

```text
STRUCT: needs changes
- Blocker/Major/Minor: <issue and fix>
```

When the user asks to improve the service design, provide the corrected section or full revised service-design brief.
