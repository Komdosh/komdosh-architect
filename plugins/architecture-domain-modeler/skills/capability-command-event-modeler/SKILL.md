---
name: capability-command-event-modeler
description: Map domain capabilities, commands, queries, business events, actors, triggers, read concerns, and domain signals without designing final APIs or message schemas.
---

# Capability Command Event Modeler

## Purpose

Connect the domain model to behavior.
Capabilities, commands, queries, and events give later architecture steps a business vocabulary for services, APIs, workflows, and integrations.

## Required Inputs

Require:

- domain concepts
- actors or use cases
- lifecycle and rule notes when available

## Capability Mapping

For each capability, identify:

- business goal
- actor or initiating system
- commands that request change
- queries that read information
- events that represent completed business facts
- rules and invariants involved
- source-of-truth candidate
- external systems involved
- read concerns or projection candidates

## Vocabulary Rules

- Commands use imperative business names such as `ApproveSeller`, `ReserveInventory`, `CancelBooking`.
- Events use past-tense business facts such as `SellerApproved`, `InventoryReserved`, `BookingCancelled`.
- Queries use information names such as `FindAvailableSlots`, `GetSellerStatus`.
- Avoid transport or technology names such as `POST /approve`, `KafkaMessage`, or `DBUpdate`.

## Output

Return:

| Capability | Commands | Queries | Events | Actor/system | Rules involved |
|------------|----------|---------|--------|--------------|----------------|

Then list:

- event vocabulary
- command vocabulary
- read concerns
- domain signals useful for integrations
- ambiguity that blocks API or service design
