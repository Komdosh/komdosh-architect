---
name: environment-strategy-planner
description: Define environment strategy, promotion path, production/non-production parity, region and AZ placement, tenant separation, data residency, test data, sandbox, and DR environment expectations.
---

# Environment Strategy Planner

## Purpose

Design where deployment topology exists across environments.
Environment strategy must support safe change, realistic validation, data separation, and operational recovery.

## Required Inputs

Require:

- deployment context inventory
- runtime topology candidates
- compliance, residency, or production constraints when available

## Environment Concerns

Define:

- development, test, staging, production, sandbox, and DR environments
- promotion path and release gates
- production parity expectations
- shared versus isolated non-production resources
- tenant separation and environment-level data boundaries
- region, AZ, and data-residency placement
- test data and masked data policy at architecture level
- preview/ephemeral environment need
- disaster recovery environment role
- environment ownership and support expectations

## Output

Return:

| Environment | Purpose | Topology parity | Data boundary | Region/AZ posture | Owner |
|-------------|---------|-----------------|---------------|-------------------|-------|

Then list:

- promotion strategy
- environment isolation rules
- data and tenant separation assumptions
- DR environment expectations
- open environment questions
