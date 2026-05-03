---
name: quality-attribute-requirements
description: Define measurable non-functional requirements and quality scenarios for architecture readiness, including reliability, performance, scalability, security, privacy, operability, maintainability, and extensibility.
---

# Quality Attribute Requirements

## Purpose

Define how well the system must behave.
Non-functional requirements must be measurable enough to guide architecture tradeoffs.

## Required Inputs

Require:

- product goal or functional scope
- user and operational context
- expected scale or explicit assumptions when scale is unknown

## Quality Attribute Coverage

Consider every relevant category:

- availability and resilience
- reliability, data integrity, and recovery
- performance, latency, throughput, and concurrency
- scalability and elasticity
- security, authentication, authorization, abuse resistance, and auditability
- privacy, data minimization, consent, retention, deletion, and regional data rules
- compliance and policy enforcement
- observability, monitoring, alerting, diagnostics, and supportability
- maintainability, modularity, testability, and deployment safety
- extensibility for future products, markets, rules, integrations, and business models
- interoperability and API evolution
- accessibility, localization, internationalization, and device/browser support
- cost, resource efficiency, and operational limits
- migration, backward compatibility, and data portability

## Quality Scenario Format

Prefer concrete quality scenarios:

| ID | Attribute | Stimulus | Environment | Response | Measure |
|----|-----------|----------|-------------|----------|---------|

Example measures:

- p95 latency target for a critical workflow
- recovery point objective and recovery time objective
- maximum acceptable duplicate or lost event behavior
- audit log retention period
- support diagnostic time target
- expected growth multiplier over 12 to 24 months

## Output

Return:

- non-functional requirements table with IDs, priority, and measurable target
- quality scenarios for the most architecture-sensitive requirements
- assumptions behind each target when the product context is incomplete
- tradeoff notes where one quality attribute conflicts with another
- open questions that materially change architecture
