---
name: load-decision-brief
description: Produce a concise architecture decision brief from load estimates, including key numbers, assumptions, confidence, risks, optimizations, validation metrics, and recommendation.
---

# Load Decision Brief

## Purpose

Make the estimate usable.
The decision brief should be short enough for architecture review and precise enough to support action.

## Required Inputs

Require:

- workload, traffic, data, or resource estimates
- bottleneck or optimization notes
- decision context

## Brief Rules

- Lead with the decision implication.
- Keep the main summary compact.
- Include only the metrics that change the decision.
- Show formulas only for important numbers.
- State confidence and assumptions.
- Separate recommendation from validation plan.
- Do not bury the answer in exhaustive tables.

## Output

Return:

```text
Decision: <what the architect can decide>
Confidence: High | Medium | Low
Load summary: <3-6 key numbers>
Main risk: <one or two risks>
Recommendation: <action>
Validate next: <metrics/tests/logs>
```

Then include a compact metric table:

| Metric | Estimate | Confidence | Why it matters |
|--------|----------|------------|----------------|
