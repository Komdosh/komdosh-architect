# Structure, Data, and Integration

## Services, components, and modules

- Choose the coarsest boundary that satisfies ownership, change cadence, deployability, scaling, security, and consistency needs. Do not default to microservices.
- For every candidate, state responsibilities, non-responsibilities, authoritative state, lifecycle authority, operational owner, and public contract.
- Describe collaboration by intent and ownership. Select synchronous, asynchronous, event, command, query, or batch interaction from latency, coupling, consistency, and failure requirements.
- Make transaction and consistency boundaries explicit, including idempotency, retries, compensation, orchestration or choreography ownership, and partial-failure behavior.
- Define dependency direction and isolate external or legacy models behind an adapter when their semantics must not leak into the domain.

## Data

- Identify authoritative, write, reference, duplicated, derived, cached, and analytical data, with an owner for each.
- For each material flow, capture producer, consumer, purpose, freshness, consistency, delivery, idempotency, failure, and reconciliation expectations.
- Read models and projections need a source of truth, freshness target, rebuild strategy, and failure owner.
- Cover classification, minimization, consent where relevant, retention, deletion, residency, export, audit/history, and legal hold requirements.
- For migration, define coexistence, historical scope, backfill, validation, reconciliation, cutover, rollback, and the point at which the old source stops being authoritative.
- Data contracts need producer/consumer responsibility, compatibility rules, quality expectations, evolution, and deprecation. Design physical schemas only when requested.

## APIs and integrations

- Inventory each surface and name its provider, consumers, contract owner, business purpose, data sensitivity, and support owner.
- Define semantics before transport: commands versus queries, resource/action boundaries, errors, pagination, rate limits, and idempotency.
- Events represent stable business facts. Specify identity, ordering scope, delivery guarantees, duplicates, replay, retention, schema evolution, and poison-message handling where relevant.
- Webhooks and callbacks need authentication or signatures, retry and timeout behavior, deduplication, delivery visibility, and consumer recovery.
- Batch and file flows need schedule, volume, atomicity, partial-failure rules, reconciliation, retention, and rerun semantics.
- Prefer additive evolution. Name breaking changes, compatibility windows, consumer migration, deprecation signals, and removal criteria.
- Include authentication, authorization, exposure, timeouts, retry budgets, circuit breaking, quotas, diagnostics, and ownership only to the depth required by the risk.

Conclude with accepted decisions, viable candidates, and unresolved choices; do not present all three as equally settled.
