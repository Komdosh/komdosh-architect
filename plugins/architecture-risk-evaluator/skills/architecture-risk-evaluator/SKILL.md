---
name: architecture-risk-evaluator
description: Evaluate architecture risks from requirements, scope, domain, service, data, load, integration, deployment, security, observability, and decision context, covering assumptions, tradeoffs, validation, mitigations, owners, readiness, risk registers, diagrams, and handoff readiness.
---

# Architecture Risk Evaluator

## Purpose

Make architecture risks visible before implementation starts.
The result must help an architect understand which risks matter, why they matter, who owns them, and what validation or mitigation is needed.

Use this skill when the user asks for architecture risk review, risk register, implementation readiness, go/no-go advice, validation spikes, risk prioritization, assumption review, or risk diagrams.

## Human Readability Rule

Every output must be easy for humans to read:

- start each section with the main idea or decision in plain words
- keep the document compact and remove decorative explanation
- use short sections, tables, and bullets for scanning
- prefer clear words over professional-sounding complexity
- keep details near the point they explain
- highlight only important decisions, risks, assumptions, open questions, and handoff steps
- explain necessary technical terms in place

## Core Rule

Evaluate risk; do not rewrite the architecture:

- base risks on architecture evidence, assumptions, decisions, source gaps, and known constraints
- cover technical, product, security, data, integration, deployment, operational, delivery, and decision risks
- rank risks by likelihood, impact, urgency, confidence, and blast radius
- make fragile assumptions explicit
- define validation work before commitment when evidence is missing
- assign owners, triggers, mitigation options, fallback paths, and residual risk
- separate accepted, mitigated, deferred, transferred, and escalated risks
- do not redesign the system unless the user explicitly asks for risk-driven redesign

## Required Inputs

Load the minimum needed context:

- current architecture brief, design proposal, or stage output
- requirements, scope, domain, service, data, load, integration, deployment, security, observability, and decision context when available
- ADRs or decision-context brief when available
- known constraints, deadlines, budget, team capability, compliance, and support expectations when available

If context is missing, infer low-risk assumptions and label them.
Ask when missing context would materially change risk ranking or go/no-go readiness.

## Skill Flow

1. Use `$architecture-risk-evaluator:risk-context-inventory` to identify source context, evaluation boundary, assumptions, and coverage gaps.
2. Use `$architecture-risk-evaluator:assumption-risk-analyzer` to identify assumptions that can fail and validation signals.
3. Use `$architecture-risk-evaluator:cross-cutting-risk-cataloger` to catalog product, technical, data, integration, security, deployment, operations, delivery, and decision risks.
4. Use `$architecture-risk-evaluator:impact-likelihood-prioritizer` to rank risks by likelihood, impact, urgency, confidence, and blast radius.
5. Use `$architecture-risk-evaluator:validation-spike-planner` to define spikes, benchmarks, prototypes, research, and proof points.
6. Use `$architecture-risk-evaluator:mitigation-owner-planner` to define mitigation options, owners, triggers, fallback paths, and residual risk.
7. Use `$architecture-risk-evaluator:readiness-go-no-go-advisor` to provide readiness and go/no-go guidance.
8. Use `$architecture-risk-evaluator:risk-register-builder` to produce the compact risk register.
9. Use `$architecture-risk-evaluator:risk-diagrammer` when a risk map or readiness diagram clarifies the result.
10. Use `$architecture-risk-evaluator:risk-review-gate` before final delivery.

## Output Contract

Return a self-contained risk-evaluation brief with this structure unless the user asks for another format:

1. Evaluation purpose
2. Source context
3. Risk scope and coverage limits
4. Top risk summary
5. Assumption risks
6. Cross-cutting risk register
7. Impact, likelihood, urgency, confidence, and blast-radius ranking
8. Validation spikes, benchmarks, prototypes, and proof points
9. Mitigation owners, triggers, fallback paths, and residual risk
10. Go/no-go readiness recommendation
11. Risks to accept, mitigate, transfer, defer, or escalate
12. Risk diagrams when useful
13. Open questions
14. Next steps

## Risk Discipline

Do not dilute the register:

- do not list obvious generic risks unless they apply to this architecture
- do not make every risk high priority
- do not hide weak confidence behind strong wording
- do not call an uncertainty solved when it only has a mitigation idea
- do not replace validation with optimism
- do not create a full project plan
- do not move implementation decisions into this plugin

You may state risk-level conclusions:

- proceed only if the external dependency latency is measured against the target workload
- accept this risk for MVP because the blast radius is isolated and rollback is simple
- mitigate this risk before implementation because it can invalidate the service boundary
- escalate this risk because it needs a product or compliance decision, not an engineering guess

## Stop Conditions

Stop and ask when:

- the architecture proposal is missing and risks would become generic
- a legal, medical, financial, safety, security, or compliance risk is central and unknown
- the user asks for go/no-go readiness without enough scope or source context
- a risk requires a business decision and the user asks for a technical fix
