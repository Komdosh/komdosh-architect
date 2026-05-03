---
name: batch-file-integration-planner
description: Plan batch, import/export, file, reconciliation, cutover, large-volume transfer, schedule, partial failure, and operational support integration semantics.
---

# Batch File Integration Planner

## Purpose

Design batch and file integrations deliberately.
Batch and files are often long-lived operational contracts and need lifecycle, reconciliation, and support rules.

## Required Inputs

Require at least one of:

- batch or file integration candidate
- migration/import/export requirement
- reporting or partner exchange requirement

## Batch/File Concerns

Define:

- producer and consumer
- schedule or trigger
- file or batch business meaning
- volume and size expectation
- completeness and validation rules
- partial failure handling
- deduplication and idempotency
- reconciliation responsibility
- retention and reprocessing window
- manual support process
- compatibility and versioning

## Output

Return:

| Integration | Producer | Consumer | Schedule/trigger | Validation | Failure handling | Support owner |
|-------------|----------|----------|------------------|------------|------------------|---------------|

Then list:

- reconciliation rules
- reprocessing expectations
- compatibility concerns
- operational runbook needs
- deferred file/schema decisions
