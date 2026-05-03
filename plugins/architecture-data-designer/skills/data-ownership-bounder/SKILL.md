---
name: data-ownership-bounder
description: Define authoritative data ownership, source-of-truth boundaries, ownership conflicts, duplicated-data rules, and authoritative versus derived data responsibilities.
---

# Data Ownership Bounder

## Purpose

Make authoritative data ownership explicit.
Service boundaries are not meaningful if data ownership is hidden or shared by accident.

## Required Inputs

Require at least one of:

- service/component design
- domain model
- data-related requirements
- current system data ownership notes

## Ownership Analysis

For each important data subject, identify:

- authoritative owner
- source-of-truth boundary
- writer authority
- allowed readers
- derived copies and projections
- external owner when the fact comes from outside the system
- duplicated-data rule
- correction and reconciliation responsibility
- audit and history owner

## Ownership Rules

- One authoritative owner per data subject unless a deliberate exception is documented.
- Derived views must not become hidden sources of truth.
- External facts should keep external ownership unless the system explicitly takes responsibility.
- Duplicated data needs freshness, reconciliation, and conflict rules.
- Shared database writes are not an acceptable ownership model by default.

## Output

Return:

| Data subject | Authoritative owner | Writers | Readers | Derived copies | Ownership risk |
|--------------|---------------------|---------|---------|----------------|----------------|

Then list:

- source-of-truth decisions
- ownership conflicts
- duplicated-data assumptions
- open ownership questions
