---
name: data-flow-mapper
description: Map data movement between services, components, external systems, read models, analytics, and operational tools with direction, freshness, consistency, failure, and reconciliation expectations.
---

# Data Flow Mapper

## Purpose

Explain how data moves without designing transport details.
Data movement should preserve ownership, privacy, and consistency expectations.

## Required Inputs

Require:

- data owners or data boundaries
- service/component collaboration notes
- external systems when relevant

## Flow Analysis

For each flow, identify:

- source owner
- target consumer
- data subject
- business reason
- direction
- push, pull, event, batch, query, export, import, or manual style at a high level
- freshness expectation
- consistency expectation
- failure and retry concern
- reconciliation need
- privacy or audit concern

## Output

Return:

| From | To | Data subject | Purpose | Style | Freshness | Failure concern |
|------|----|--------------|---------|-------|-----------|-----------------|

Then list:

- high-risk data flows
- stale or duplicate data concerns
- reconciliation responsibilities
- open data-flow questions
