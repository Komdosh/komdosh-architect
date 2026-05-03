---
name: workload-scenario-profiler
description: Define workload scenarios, user populations, active usage, peak factors, burst behavior, seasonality, background jobs, integrations, and workload assumptions for load estimation.
---

# Workload Scenario Profiler

## Purpose

Describe what load means for the product.
Architecture load estimates must start from business activity, not infrastructure guesses.

## Required Inputs

Require at least one of:

- product or service description
- user/tenant volume
- business transaction volume
- existing metrics
- explicit permission to make assumptions

## Workload Dimensions

Capture:

- total users, active users, tenants, organizations, devices, or actors
- daily, hourly, and peak active users
- business transactions per day
- peak factor and burst factor
- seasonality or campaign spikes
- read/write ratio
- background jobs and schedules
- batch imports/exports
- external integrations and callbacks
- operational/admin traffic
- retry, replay, and failure traffic

## Output

Return:

| Scenario | Metric | Estimate | Formula/source | Confidence |
|----------|--------|----------|----------------|------------|

Then list:

- baseline scenario
- peak scenario
- burst or failure scenario
- explicit assumptions
- missing inputs that materially affect the estimate
