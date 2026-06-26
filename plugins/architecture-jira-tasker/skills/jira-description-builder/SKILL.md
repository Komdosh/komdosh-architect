---
name: jira-description-builder
description: Write a human-readable Jira issue description with QA-checkable acceptance criteria and no leaked development details.
---

# Jira Description Builder

## Purpose

Write the Jira description for an architecture-derived delivery task.
The description must be complete enough for humans to understand the outcome, scope, QA expectations, release context, and review requirements.
Treat the description as the working contract: what must be done, why, what is in and out of scope, and how the result will be verified.
It must not expose development details that belong in architecture docs, pull requests, or private execution notes.
The Jira summary and description body must be written in Russian, including section headings and all acceptance criteria text. Keep product names, Jira field names, labels, API names, paths, commands, error messages, canonical labels, and exact user-provided terms unchanged when translating them would reduce clarity.
It must satisfy the 30-second rule: a team lead or colleague should understand the task quickly, without reading a long implementation specification.
Important agreements, constraints, risks, blockers, and verification expectations must be in the description itself, not only in private messages, calls, or Jira comments.

## Required Inputs

Require:

- scope contract
- filled Jira metadata
- architecture docs, ADRs, diagrams, and implementation notes
- Jira format/profile docs when provided
- product area, service, application, component, release, QA, security, deployment, and observability context when applicable

## Description Rules

Write in Jira-friendly Markdown or the format required by the Jira tool.

- write the Jira summary and description body in Russian
- use Russian section headings unless the target Jira format profile requires exact headings
- start with the outcome, not background
- keep the description compact, usually 5-7 short sections and no longer than one screen
- use the section order required by the target Jira format profile when one is provided
- include source document links when they are required for execution, review, QA, release, or support
- translate architecture decisions into human-readable behavior, constraints, and verification expectations
- make scope and out-of-scope boundaries explicit
- include acceptance criteria split into `Проверяет разработчик` and `Проверяет ручной тестировщик`
- use `DEV` and `QA` as subsection headings only when the target Jira format profile or board explicitly requires those exact labels; preserve the same developer/manual QA separation
- put developer/reviewer evidence only in `Проверяет разработчик`: code completion, compilation, lint/static checks, type checks, automated tests, unit tests, integration tests, schema/contract checks, MR artifacts, and other engineering quality gates
- put manual checks only in `Проверяет ручной тестировщик`: UI, UX, user actions, animations, visible functionality, negative paths, permissions, notifications, copy, documentation, release behavior, and operator-facing behavior
- keep a subsection even when it does not apply, and write `Not applicable` with a short reason instead of deleting the responsibility boundary
- include a mandatory `Проверка` section that names where evidence will live: CI job, MR, test report, QA note, demo, environment, build, artifact, or linked test plan
- include documentation updates and release notes when the change is user-facing or operator-facing
- keep human work in the review checklist
- do not include file paths, class names, method names, internal package/module plans, developer commands, database migration instructions, or code-level sequencing
- mention APIs, logs, dashboards, or operational tools only when they are approved QA or operations verification surfaces
- do not include hidden requirements that only the task author knows, oral agreements without written task text, confidential data, secrets, tokens, private incident details, or personal data
- do not include estimates, story points, hours, long justifications, filler, or detailed inventories of existing code
- avoid specific OS/device versions in Jira; use general phrasing such as `older devices`, `low-end devices`, or `slow network` unless the format profile requires exact values

## Required Description Shape

Use this compact structure for normal Story/Task issues:

```markdown
**Цель**

<одно-два предложения: что получает пользователь, оператор или команда после закрытия задачи.>

**Контекст**

<откуда появилась задача, что она разблокирует или что ее блокирует. Убрать, если не нужно.>

**Что входит**

- <видимый для человека результат или поведение>
- <видимый для человека результат или поведение>

**Не входит**

- <явная нецель, если полезно>

**Ограничения / блокеры**

<допущение, известное ограничение, блокер или Not applicable. Для блокера указать владельца или следующее действие.>

**Критерии приемки**

_Проверяет разработчик_
- <проверка, которую может принять разработчик: код завершен, сборка/компиляция проходит, lint/typecheck проходит, автоматические или unit-тесты покрывают ожидаемое поведение>
- <другая инженерная проверка качества без файловых путей, имен классов, локальных команд или внутренней последовательности реализации>

_Проверяет ручной тестировщик_
- <ручная проверка, которую QA может выполнить в продукте или согласованном инструменте>
- <ручная проверка UI/UX, действия, анимации, функциональности, негативного сценария, прав доступа, уведомлений, документации или release-поведения>

**Проверка**

<где будет подтверждение: CI job, MR, test report, QA note, demo, окружение, build, artifact или linked test plan>.
Или: см. `<test-plan-path>`, если нужен отдельный QA test plan.

**Зависимости**

- <зависимость или Нет>
```

For Bug issues, use this structure:

```markdown
**Описание**

<что сломано, одним предложением.>

**Шаги воспроизведения**

1. <шаг>
2. <шаг>

**Ожидаемый результат**

<что должно происходить.>

**Фактический результат**

<что происходит сейчас.>

**Окружение**

- Платформа: <платформа>
- Версия приложения / commit: <версия или commit>
- Устройство / emulator: <общий класс или точное значение только когда bug report этого требует>
- Особые условия: <network/offline/slow network/etc. или Нет>

**Критерии приемки**

_Проверяет разработчик_
- <техническое подтверждение исправления и регрессии без внутренних файловых путей, имен классов или локальных команд>

_Проверяет ручной тестировщик_
- <ручная проверка воспроизведения и регрессии на согласованном окружении>

**Проверка**

<ссылка на bug regression test plan, QA note, build, окружение или другой evidence>.
```

## Acceptance Criteria Rules

Acceptance criteria must:

- be written in Russian
- be split into `Проверяет разработчик` and `Проверяет ручной тестировщик`, or board-required equivalent headings with the same meaning
- keep developer checks for developer/reviewer evidence such as code completion, compilation, lint/static checks, type checks, automated tests, unit tests, integration tests, schema/contract checks, MR artifacts, and other engineering quality gates
- keep manual tester checks understandable by manual QA without reading code, implementation plans, pull requests, or architecture internals
- make manual tester checks observable through UI behavior, approved API behavior, user-visible output, operator-visible output, documentation, support workflow, release state, or agreed QA tools
- keep both responsibility subsections present, using `Not applicable` with a short reason when one does not apply
- include success and failure paths when behavior has branching logic
- cover documentation, regression, release, and operational validation when relevant
- avoid vague criteria such as `works correctly`, `is scalable`, or `is secure`
- avoid leaking developer-only implementation detail such as unit test names, source files, migration scripts, class names, internal package names, local commands, or code-level sequencing

## Verification Section Rules

Decide whether the task needs a separate QA test plan.

- the `Проверка` section is mandatory
- state where developer and manual QA evidence will be recorded: CI job, MR, test report, QA note, demo, environment, build, artifact, or linked test plan
- use one short evidence line for simple technical tasks that cannot be meaningfully verified in a running app, database, or networked environment
- point to a separate test plan when the result can be touched or verified in a running app, database, or networked environment
- always require a separate test plan for bugs, because reproduction and regression checks must be explicit
- when a separate test plan is needed, keep detailed steps out of Jira and reference the plan from the `Проверка` section
- when a format profile defines test-plan templates or paths, follow that path convention

## Constraints And Blockers Rules

Use `Ограничения / блокеры` inside the Russian Jira description for assumptions, known limitations, risks, blockers, and facts that materially affect execution or verification.

- keep each limitation to 3-5 sentences
- classify it as `not a blocker`, `blocker until <date/event>`, or `MVP blocker`
- state the owner or next action for blockers and open questions
- state where the follow-up belongs, such as a separate ticket or epic
- do not use Jira comments to document stable task limitations or blockers; comments are for process discussion, while durable task facts belong in the description

## Output

Return the final Jira description and mention any formatting constraints required by the target Jira tool.
