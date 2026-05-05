---
name: stateful-placement-planner
description: Place databases, caches, queues, brokers, object stores, search, file storage, and other stateful dependencies with ownership, HA, backup, restore, locality, retention, and operational responsibility.
---

# Stateful Dependency Placement Planner

## Purpose

Design where state lives and who operates it.
Stateful dependencies are recovery anchors and should never be placed without ownership, backup, restore, and failure expectations.

## Required Inputs

Require:

- data design or stateful dependency list
- runtime topology
- availability, retention, or compliance constraints when available

## Placement Concerns

Define:

- database, cache, queue, broker, object store, search, and file storage placement
- managed versus self-operated posture at architecture level
- ownership and support boundary
- region/AZ placement and data locality
- backup, restore, retention, and archival expectations
- replication, failover, and recovery role
- latency and throughput sensitivity
- connection limits and pooling expectations
- migration and schema-change coordination
- observability and operational runbook needs

## Output

Return:

| Dependency | Role | Placement | HA/recovery posture | Data concern | Owner |
|------------|------|-----------|---------------------|--------------|-------|

Then list:

- recovery anchors
- stateful dependencies requiring isolation
- backup and restore expectations
- migration coordination needs
- open stateful-placement questions
