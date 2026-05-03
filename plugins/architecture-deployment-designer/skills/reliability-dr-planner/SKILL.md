---
name: reliability-dr-planner
description: Define deployment reliability, availability zones, failover, degradation, backup, restore, RPO, RTO, disaster recovery, resilience testing, and recovery ownership.
---

# Reliability DR Planner

## Purpose

Define how the deployed system survives failures and recovers from disasters.
Reliability design must connect topology, state, rollout, and operations into concrete recovery expectations.

## Required Inputs

Require:

- runtime topology
- stateful dependency placement
- SLO, availability, RPO, or RTO expectations when available

## Reliability Concerns

Define:

- availability target at architecture level
- single points of failure
- region and AZ resilience posture
- failover expectation and owner
- graceful degradation paths
- backup, restore, point-in-time restore, and retention expectations
- RPO and RTO assumptions
- disaster recovery topology
- recovery drills and validation metrics
- incident ownership and escalation path
- resilience test expectations

## Output

Return:

| Failure scenario | Expected behavior | Recovery mechanism | RPO/RTO impact | Owner | Validation |
|------------------|-------------------|--------------------|----------------|-------|------------|

Then list:

- single points of failure
- failover decisions
- backup and restore expectations
- DR posture
- reliability validation plan
