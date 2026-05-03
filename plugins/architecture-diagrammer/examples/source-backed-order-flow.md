# Source-Backed Order Flow Example

## Diagram Purpose

Show the confirmed order-submission flow from customer request to downstream search projection.

## Source Text

Customer mobile clients submit orders through the public API gateway. The API gateway forwards valid order commands to the Order Service. The Order Service owns order lifecycle state and writes confirmed orders to PostgreSQL as the authoritative store. After commit, the Order Service publishes `order.confirmed` events to the event backbone. The Search Projection consumes those events and updates a read model for product and order lookup. Search Projection is downstream and is not a source of truth.

## Boundary Inventory

| Element | Type | Boundary | Scope | Why it is needed | Source evidence |
|---------|------|----------|-------|------------------|-----------------|
| Customer mobile client | Actor | External client | Confirmed | Starts order submission | "Customer mobile clients submit orders..." |
| Public API gateway | Gateway | Public edge | Confirmed | Forwards valid commands to domain service | "through the public API gateway" |
| Order Service | Domain service | Owning service | Confirmed | Owns lifecycle and publishes event | "Order Service owns order lifecycle state" |
| PostgreSQL orders | Data store | Authoritative store | Confirmed | Stores confirmed orders | "PostgreSQL as the authoritative store" |
| Event backbone | Event stream | Async integration | Confirmed | Carries `order.confirmed` | "publishes `order.confirmed` events" |
| Search Projection | Downstream projection | Read model | Confirmed | Updates search lookup | "consumes those events and updates a read model" |

## Assumptions

None.
