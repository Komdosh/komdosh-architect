---
name: error-taxonomy-diagnostics-designer
description: Define architecture-level error taxonomy, failure categories, user impact, retryability, ownership, diagnostic fields, external dependency errors, support codes, and incident classification.
---

# Error Taxonomy Diagnostics Designer

## Purpose

Define how failures are named and understood.
Clear error categories help users, support, engineers, and alerts speak the same language.

## Required Inputs

Require:

- service, API, integration, or support context
- observability context inventory
- logging or alerting needs when available

## Error Concerns

Define:

- user-visible error categories
- internal failure categories
- retryable versus non-retryable failures
- dependency failures and external-provider errors
- validation, authorization, quota, conflict, timeout, data, and partial-failure categories
- diagnostic fields and support-safe error references
- ownership by category
- incident severity mapping
- consistency with API and integration contracts

## Output

Return:

| Error category | User impact | Retryable? | Owner | Required diagnostics | Alert/support rule |
|----------------|-------------|------------|-------|----------------------|--------------------|

Then list:

- core error taxonomy
- support-facing diagnostics
- incident severity mapping
- external dependency error rules
- open error-taxonomy questions
