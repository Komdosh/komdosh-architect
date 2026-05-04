---
name: decision-discovery-review-gate
description: Review decision discovery for source coverage, ADR status clarity, constraint extraction, drift detection, confidence labeling, future ADR scope, readability, and strict no-ADR-writing discipline.
---

# Decision Discovery Review Gate

## Purpose

Review decision discovery before architecture work uses the result.
Find missing source coverage, unclear ADR status, hidden assumptions, weak drift checks, and accidental ADR authoring.

## Required Inputs

Require:

- decision-context brief or exact diff
- searched source list
- current architecture task when available

If only a brief is provided, review internal coherence and state that source alignment was not verified.

## DECIDE Review

Use `DECIDE`:

| Check | Question |
|-------|----------|
| `D` Discovery | Were local files, related repos, MCP/RAG, memory, and AI context sources considered when available? |
| `E` Evidence | Are ADRs, notes, paths, tools, statuses, and confidence levels clear? |
| `C` Constraints | Are accepted decisions, consequences, rejected alternatives, and revisit triggers extracted? |
| `I` Inference control | Are confirmed facts separated from assumptions, memory-derived context, and inferred implications? |
| `D` Drift | Are conflicts between current work and existing decisions called out? |
| `E` Exclusion | Is ADR writing, updating, approving, or superseding kept out of scope? |

## Readability Check

Treat readability as part of review quality:

- main ideas and decisions are visible first
- wording is plain and compact
- details support nearby points instead of hiding them
- only important decisions, risks, assumptions, open questions, and next steps are highlighted
- necessary technical terms are explained in place

Mark as Major when professional complexity, long prose, or scattered details make the brief hard to use.

## Blockers

Treat these as blockers:

- likely ADR source was not searched or source coverage is hidden
- ADR status is missing when it affects constraints
- memory-derived or inferred context is presented as confirmed ADR fact
- accepted decision is ignored or contradicted
- rejected alternative is recommended as if new
- current design drift is hidden
- future ADR need is turned into ADR text
- plugin writes, edits, approves, supersedes, renames, or deletes ADRs
- temporary notes are treated as official decision records

## Output

Return either:

```text
DECIDE: pass
Decision discovery readiness: pass
```

or:

```text
DECIDE: needs changes
- Blocker/Major/Minor: <issue and fix>
```

When the user asks to improve the decision discovery result, provide the corrected section or full revised decision-context brief.
