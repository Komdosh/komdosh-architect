---
name: data-volume-growth-estimator
description: Estimate records, events, logs, audit data, payload sizes, storage growth, retention impact, bandwidth, and data-volume pressure for architecture decisions.
---

# Data Volume Growth Estimator

## Purpose

Estimate how data grows over time.
Storage, retention, audit, analytics, and bandwidth often become architecture constraints before CPU does.

## Required Inputs

Require at least one of:

- data design
- data subjects and retention needs
- business transaction volume
- event/log/audit expectations
- payload size assumptions

## Estimation Rules

Use simple formulas:

- `records per period = business events per period * records per event`
- `raw storage = record count * average record size`
- `retained storage = daily storage * retention days`
- `replicated storage = retained storage * replication/copy factor`
- `bandwidth = message size * message count`
- `log volume = requests * average log bytes`

Include overhead ranges when physical storage is unknown.

## Metrics To Cover

- authoritative records
- read models and projections
- events and messages
- logs and audit records
- file/media payloads when relevant
- daily and monthly growth
- retention-driven total storage
- backup/export multiplier
- network and egress pressure
- analytics/reporting volume

## Output

Return:

| Data area | Daily growth | Retention | Estimated total | Formula | Decision impact |
|-----------|--------------|-----------|-----------------|---------|-----------------|

Then list:

- dominant data growth drivers
- retention and audit pressure
- bandwidth or egress risks
- assumptions and validation metrics
