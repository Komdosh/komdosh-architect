---
name: scope-review-gate
description: Review a scope-boundary brief for focus, boundary clarity, actor coverage, external-system coverage, use-case coverage, exception paths, diagram consistency, and design-stage discipline.
---

# Scope Review Gate

## Purpose

Review the scope-boundary brief before the architecture workflow moves to later steps.
Find boundary drift, missing actors, missing external systems, and premature detailed design.

## Required Inputs

Require:

- scope-boundary brief or exact diff
- product area or system of interest when available
- context or landscape diagrams when produced

If only a scope brief is provided, review internal coherence and state that source alignment was not verified.

## BOUNDED Review

Use `BOUNDED`:

| Check | Question |
|-------|----------|
| `B` Boundary | Is the system of interest clear and focused on one part? |
| `O` Outside | Are adjacent and out-of-scope responsibilities explicit? |
| `U` Users | Are human roles, operators, and non-human actors covered? |
| `N` Neighbors | Are external systems and integration surfaces identified? |
| `D` Dynamics | Are high-level use cases, alternate paths, and exception paths covered? |
| `E` Edges | Are trust, data, command, event, and operational boundaries visible? |
| `D` Design discipline | Does the brief avoid premature detailed implementation? |

## Blockers

Treat these as blockers:

- no clear system of interest
- multiple unrelated scopes mixed together
- missing external systems for a clearly integration-heavy product area
- missing actors or operators that materially affect architecture
- no exception or failure paths for critical use cases
- diagrams contradict the written boundary
- hidden ownership or trust boundary assumptions
- detailed implementation decisions presented before boundary clarity

## Output

Return either:

```text
BOUNDED: pass
Scope readiness: pass
```

or:

```text
BOUNDED: needs changes
- Blocker/Major/Minor: <issue and fix>
```

When the user asks to improve the scope, provide the corrected section or full revised scope brief.
