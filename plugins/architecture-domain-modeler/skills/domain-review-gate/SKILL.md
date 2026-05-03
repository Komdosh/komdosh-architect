---
name: domain-review-gate
description: Review a domain-modeling brief for language clarity, concept coverage, lifecycle coverage, invariants, capability vocabulary, traceability, ambiguity, and design-stage discipline.
---

# Domain Review Gate

## Purpose

Review the domain model before later architecture design.
Find unclear terms, missing lifecycles, weak invariants, implementation leakage, and risks that would make service or data design premature.

## Required Inputs

Require:

- domain-modeling brief or exact diff
- requirements or scope summary when available
- diagrams when produced

If only a domain brief is provided, review internal coherence and state that source alignment was not verified.

## MODEL Review

Use `MODEL`:

| Check | Question |
|-------|----------|
| `M` Meaning | Are domain terms clear, canonical, and not overloaded? |
| `O` Objects | Are core concepts, relationships, and ownership candidates covered? |
| `D` Dynamics | Are key lifecycles, transitions, and exception states modeled? |
| `E` Enforcement | Are rules, policies, invariants, and consistency expectations explicit? |
| `L` Language | Are commands, queries, events, and capabilities named in business language? |

Also check design-stage discipline:

| Check | Question |
|-------|----------|
| Traceability | Can concepts trace to requirements, scope, assumptions, or open questions? |
| Ambiguity | Are unstable terms and unresolved source-of-truth decisions visible? |
| Diagrams | Do diagrams match the written model and avoid implementation detail? |
| Stage fit | Does the output avoid service, database, API, and deployment decisions? |

## Blockers

Treat these as blockers:

- no clear domain scope
- core terms are ambiguous or overloaded
- missing lifecycle for a central concept
- missing invariants for a stateful or policy-heavy domain
- source-of-truth ownership hidden as an assumption
- event vocabulary is technical instead of business factual
- diagram contradicts the written domain model
- output jumps to microservices, tables, queues, or APIs before domain readiness

## Output

Return either:

```text
MODEL: pass
Domain readiness: pass
```

or:

```text
MODEL: needs changes
- Blocker/Major/Minor: <issue and fix>
```

When the user asks to improve the domain model, provide the corrected section or full revised domain-modeling brief.
