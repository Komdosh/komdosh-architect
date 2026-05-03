---
name: event-webhook-designer
description: Frame event, webhook, callback, delivery, ordering, duplicate, subscription, replay, consumer, and business-fact semantics without final message schemas.
---

# Event Webhook Designer

## Purpose

Design asynchronous contracts clearly.
Events, webhooks, and callbacks need explicit semantics because consumers will build behavior around them.

## Required Inputs

Require:

- event/webhook/callback candidates
- producer and consumer context
- data ownership and lifecycle facts when available

## Semantics To Define

For each event, webhook, or callback, define:

- business meaning
- producer
- consumers
- trigger
- delivery expectation
- duplicate delivery expectation
- ordering expectation
- retry behavior
- replay or backfill expectation
- subscription or routing ownership
- schema evolution responsibility
- failure and dead-letter ownership

## Rules

- Name events as past-tense business facts.
- Do not use events as opaque technical notifications when business meaning matters.
- State whether consumers may treat the event as authoritative.
- Make duplicate and out-of-order handling explicit.
- For webhooks, assume providers may retry unless the source says otherwise.

## Output

Return:

| Signal | Type | Meaning | Producer | Consumers | Delivery semantics | Evolution risk |
|--------|------|---------|----------|-----------|--------------------|----------------|

Then list:

- ordering and duplicate rules
- replay/backfill expectations
- webhook retry assumptions
- consumer support concerns
- deferred schema decisions
