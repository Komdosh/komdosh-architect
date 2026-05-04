# Architecture Risk Evaluator

Architecture Risk Evaluator is a Codex plugin for architecture-stage risk review.
It comes after enough requirements, scope, domain, service, data, load, integration, deployment, security, observability, and decision context exists to assess implementation risk.

## Scope Fit

Use this plugin when the requested outcome is:

- technical, product, security, data, integration, deployment, operational, delivery, and decision risks
- assumptions that can fail
- architecture tradeoffs that need validation
- risk severity, likelihood, impact, owner, mitigation, and trigger
- spikes, prototypes, benchmarks, or research needed before commitment
- go/no-go readiness for implementation
- compact risk register for architects and stakeholders
- risk diagrams or heat maps when useful

This plugin makes risk visible, prioritized, and actionable.
It should not rewrite the architecture, solve every risk, create a project plan, or replace specialist reviews.

## Human-Readable Output

Prefer readability over professional complexity.
Outputs should be compact, self-contained, and easy to scan.

- put the main idea or decision first
- use plain words before specialist terms
- highlight only important decisions, risks, assumptions, open questions, and next steps
- keep details close to the point they explain
- avoid long paragraphs and decorative wording
- explain necessary technical terms in place

## Skill Grouping

- `$architecture-risk-evaluator:architecture-risk-evaluator`: orchestrates the full risk-evaluation pass.
- `$architecture-risk-evaluator:risk-context-inventory`: identifies architecture scope, source context, decisions, assumptions, and evaluation boundaries.
- `$architecture-risk-evaluator:assumption-risk-analyzer`: finds assumptions that may fail and the signals needed to validate them.
- `$architecture-risk-evaluator:cross-cutting-risk-cataloger`: catalogs product, technical, data, integration, security, deployment, operations, and delivery risks.
- `$architecture-risk-evaluator:impact-likelihood-prioritizer`: ranks risks by likelihood, impact, urgency, confidence, and blast radius.
- `$architecture-risk-evaluator:validation-spike-planner`: defines spikes, benchmarks, prototypes, research, and proof points needed before commitment.
- `$architecture-risk-evaluator:mitigation-owner-planner`: assigns mitigation options, owners, triggers, fallback paths, and residual risk.
- `$architecture-risk-evaluator:readiness-go-no-go-advisor`: produces go/no-go readiness guidance and conditions to proceed.
- `$architecture-risk-evaluator:risk-register-builder`: builds the compact architecture risk register.
- `$architecture-risk-evaluator:risk-diagrammer`: creates risk maps, heat maps, dependency-risk maps, or readiness diagrams.
- `$architecture-risk-evaluator:risk-review-gate`: reviews the risk evaluation for usefulness, coverage, and scope discipline.

Use the namespaced skill form above in Codex prompts.
The short skill names are directory names, not the guaranteed runtime invocation names.

## Quality Bar

A good output is clear, prioritized, and action-oriented.
It should tell an architect which risks matter now, why they matter, who owns them, and what evidence is needed.

Reject or revise a risk evaluation when it:

- lists generic risks without architecture evidence
- treats every risk as equal priority
- hides assumptions, unknowns, owner gaps, or residual risk
- proposes vague mitigations such as "monitor" or "make scalable" without action
- ignores validation work needed before commitment
- confuses risk evaluation with redesign or project planning
- is too verbose to use in an architecture decision meeting

## Required Output Shape

The main output should be a risk-evaluation brief with:

- evaluation purpose and source context
- risk scope and coverage limits
- top risk summary
- assumption risks
- cross-cutting risk register
- impact, likelihood, urgency, confidence, and blast-radius ranking
- validation spikes, benchmarks, prototypes, and proof points
- mitigation owners, triggers, fallback paths, and residual risk
- go/no-go readiness recommendation
- risks to accept, mitigate, transfer, defer, or escalate
- risk diagrams when useful
- open questions and next steps
