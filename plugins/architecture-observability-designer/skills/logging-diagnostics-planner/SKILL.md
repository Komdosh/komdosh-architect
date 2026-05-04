---
name: logging-diagnostics-planner
description: Define architecture-level logging strategy, diagnostic context, structured fields, sensitive-data controls, support usefulness, error evidence, audit-adjacent records, and log ownership.
---

# Logging Diagnostics Planner

## Purpose

Design logs that help people diagnose issues.
Logs should explain what happened, where, for whom, and why, without leaking sensitive data.

## Required Inputs

Require:

- observability context inventory
- error, security, or support needs when available

## Logging Concerns

Define:

- log purpose by component or flow
- required diagnostic context and structured fields
- correlation and causality fields
- error, retry, timeout, degradation, and external dependency evidence
- sensitive data masking, redaction, and exclusion rules
- support-safe identifiers
- log levels at architecture level
- ownership, retention, and access concerns
- cases where audit records are separate from application logs

## Output

Return:

| Flow/component | Log purpose | Required context | Sensitive-data rule | User/support use | Owner |
|----------------|-------------|------------------|---------------------|------------------|-------|

Then list:

- critical diagnostic fields
- sensitive-data restrictions
- support investigation needs
- audit-versus-log boundaries
- open logging questions
