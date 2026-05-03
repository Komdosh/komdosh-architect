---
name: load-review-gate
description: Review load estimates for decision clarity, metric coverage, assumptions, formulas, confidence, bottleneck analysis, optimization relevance, validation plan, and concision.
---

# Load Review Gate

## Purpose

Review load estimates before they are used for architecture decisions.
Find fake precision, missing workload drivers, missing bottlenecks, and unclear decision implications.

## Required Inputs

Require:

- load-estimation brief or exact diff
- architecture decision context when available

If only estimates are provided, review internal coherence and state that source alignment was not verified.

## METRIC Review

Use `METRIC`:

| Check | Question |
|-------|----------|
| `M` Metrics | Are multiple relevant metrics covered, not only RPS? |
| `E` Evidence | Are known facts, assumptions, formulas, and confidence clear? |
| `T` Traffic | Are baseline, peak, burst, fan-out, concurrency, and queues considered where relevant? |
| `R` Resources | Are data growth, storage, network, CPU, memory, IO, workers, and external limits considered where relevant? |
| `I` Implications | Does each important metric support a decision or optimization option? |
| `C` Concision | Is the final brief clear and short enough for architecture review? |

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

- precise numbers with no assumptions or formulas
- no stated decision context
- missing peak or burst estimate for user-facing systems
- missing storage/data growth estimate for data-heavy systems
- missing external dependency rate or limit for integration-heavy systems
- bottleneck risks ignored
- no validation or observability plan
- estimates too verbose or unclear to support a decision
- benchmark certainty claimed without measured evidence

## Output

Return either:

```text
METRIC: pass
Load decision readiness: pass
```

or:

```text
METRIC: needs changes
- Blocker/Major/Minor: <issue and fix>
```

When the user asks to improve the estimate, provide the corrected section or full revised load-estimation brief.
