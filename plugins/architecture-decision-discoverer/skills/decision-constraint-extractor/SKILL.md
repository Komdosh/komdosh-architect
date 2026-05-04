---
name: decision-constraint-extractor
description: Extract architecture constraints, defaults, forbidden choices, required patterns, ownership rules, assumptions, consequences, and revisit triggers from discovered ADRs and decision notes.
---

# Decision Constraint Extractor

## Purpose

Turn decisions into usable constraints.
Architects need to know what must be followed, what is allowed, and what has already been rejected.

## Required Inputs

Require:

- ADR summaries or decision notes
- current architecture task or design area

## Extraction Rules

Extract:

- hard constraints
- preferred defaults
- forbidden or rejected paths
- ownership and boundary rules
- technology, data, API, deployment, security, or operations constraints
- assumptions that still affect current work
- consequences that create tradeoffs
- revisit triggers and expiry conditions

Separate:

- confirmed ADR constraints
- inferred implications
- memory-derived context
- open questions

## Output

Return:

| Constraint | Source | Applies to | Strength | Reason | Risk if ignored |
|------------|--------|------------|----------|--------|-----------------|

Then list:

- hard constraints
- useful defaults
- forbidden paths
- assumptions to verify
- revisit triggers
