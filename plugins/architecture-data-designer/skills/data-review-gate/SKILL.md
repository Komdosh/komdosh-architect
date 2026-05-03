---
name: data-review-gate
description: Review a data-design brief for source-of-truth clarity, data ownership, flow correctness, projection discipline, lifecycle, privacy, migration, contracts, and stage discipline.
---

# Data Review Gate

## Purpose

Review data architecture before later storage and integration design.
Find hidden ownership, shared-write coupling, missing privacy lifecycle, weak projection discipline, and premature physical schema design.

## Required Inputs

Require:

- data-design brief or exact diff
- service design or domain model when available
- diagrams when produced

If only a data brief is provided, review internal coherence and state that source alignment was not verified.

## SOURCE Review

Use `SOURCE`:

| Check | Question |
|-------|----------|
| `S` Source | Is authoritative source-of-truth ownership clear? |
| `O` Ownership | Are writers, readers, derived copies, and external owners explicit? |
| `U` Usage | Are read models, projections, reporting, search, analytics, and caches distinguished from writes? |
| `R` Retention | Are lifecycle, retention, deletion, privacy, residency, and audit needs covered? |
| `C` Contracts | Are producer/consumer responsibilities and compatibility expectations clear? |
| `E` Evolution | Are migration, backfill, reconciliation, and schema-evolution risks visible without physical design? |

Also check:

- data flow direction and freshness
- consistency and duplicated-data rules
- diagram consistency
- stage discipline

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

- central data has no authoritative owner
- multiple components write the same authoritative data without an explicit decision
- read models or projections are shown as sources of truth
- shared database coupling is normalized
- sensitive data lacks privacy, retention, deletion, or audit expectations
- migration or backfill is required but ignored
- data contracts have consumers but no producer ownership
- diagrams contradict the written ownership model
- output jumps to physical database, table, index, partition, or storage-product design

## Output

Return either:

```text
SOURCE: pass
Data readiness: pass
```

or:

```text
SOURCE: needs changes
- Blocker/Major/Minor: <issue and fix>
```

When the user asks to improve the data design, provide the corrected section or full revised data-design brief.
