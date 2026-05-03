---
name: product-goal-discovery
description: Clarify product goals, users, stakeholders, domain context, success metrics, constraints, and assumptions before software architecture requirements are written.
---

# Product Goal Discovery

## Purpose

Understand what the product is trying to achieve before defining requirements.
Architecture requirements must start from product value, not from preferred technology.

## Required Inputs

Require at least one of:

- product idea or feature goal
- business problem
- target user or stakeholder description
- existing product or domain context

If the user provides only a vague idea, infer a first-pass goal model and label it as assumptions.

## Discovery Checklist

Identify:

- primary product goal
- business outcomes and success metrics
- target users, personas, and jobs to be done
- stakeholder groups and their incentives
- domain language and core objects
- operational context, support expectations, and lifecycle
- monetization, compliance, policy, or risk drivers when relevant
- market or field-specific expectations that affect requirements
- existing systems, migration constraints, and integration environment
- constraints around cost, schedule, team, maintainability, and support

## Field-Aware Thinking

Think beyond the obvious feature:

- what users are really trying to accomplish
- what can go wrong in normal use
- what abuse, fraud, misuse, or operator mistakes are plausible
- what data must be trusted, retained, corrected, deleted, or audited
- what changes are likely when the product grows
- what support team, operations team, or business team will need after launch
- what regulations, policies, accessibility needs, localization, or regional expectations may apply

## Output

Return:

- concise product purpose
- stakeholder and persona list
- business goals and success metrics
- domain glossary
- known facts
- assumptions
- open questions that materially affect requirements or architecture
