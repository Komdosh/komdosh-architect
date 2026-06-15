---
name: jira-description-builder
description: Write a human-readable Jira issue description with QA-checkable acceptance criteria and no leaked development details.
---

# Jira Description Builder

## Purpose

Write the Jira description for an architecture-derived delivery task.
The description must be complete enough for humans to understand the outcome, scope, QA expectations, release context, and review requirements.
It must not expose development details that belong in architecture docs, pull requests, or private execution notes.
The Jira description body must be written in Russian, including section headings and all acceptance criteria text. Keep product names, Jira field names, labels, API names, and exact user-provided terms unchanged when translating them would reduce clarity.
It must satisfy the 30-second rule: a team lead or colleague should understand the task quickly, without reading a long implementation specification.

## Required Inputs

Require:

- scope contract
- filled Jira metadata
- architecture docs, ADRs, diagrams, and implementation notes
- Jira format/profile docs when provided
- product area, service, application, component, release, QA, security, deployment, and observability context when applicable

## Description Rules

Write in Jira-friendly Markdown or the format required by the Jira tool.

- write the Jira description body in Russian
- use Russian section headings unless the target Jira format profile requires exact headings
- start with the outcome, not background
- keep the description compact, usually 5-7 short sections and no longer than one screen
- use the section order required by the target Jira format profile when one is provided
- include source document links only when useful for human review
- translate architecture decisions into human-readable behavior, constraints, and verification expectations
- make scope and out-of-scope boundaries explicit
- include acceptance criteria split into `DEV` and `QA`
- put developer-accepted checks only in `DEV`: code completion, compilation, lint/static checks, type checks, automated tests, unit tests, integration tests, schema/contract checks, and other engineering quality gates
- put manual checks only in `QA`: UI, UX, user actions, animations, visible functionality, negative paths, permissions, notifications, copy, documentation, release behavior, and operator-facing behavior
- include testing guidance that is either a one-line verification or a link/path to a separate QA test plan
- include documentation updates and release notes when the change is user-facing or operator-facing
- keep human work in the review checklist
- do not include file paths, class names, method names, internal package/module plans, developer commands, database migration instructions, or code-level sequencing
- mention APIs, logs, dashboards, or operational tools only when they are approved QA or operations verification surfaces
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

**Известные ограничения (не блокер)**

<короткое ограничение с классификацией блокера и местом для follow-up. Убрать, если ограничений нет.>

**Критерии приемки**

DEV
- <проверка, которую может принять разработчик: код завершен, сборка/компиляция проходит, lint/typecheck проходит, автоматические или unit-тесты покрывают ожидаемое поведение>
- <другая инженерная проверка качества без файловых путей, имен классов, локальных команд или внутренней последовательности реализации>

QA
- <ручная проверка, которую QA может выполнить в продукте или согласованном инструменте>
- <ручная проверка UI/UX, действия, анимации, функциональности, негативного сценария, прав доступа, уведомлений, документации или release-поведения>

**Тестирование**

Проверка: <одна ручная, build или QA-проверка>.
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
```

## Acceptance Criteria Rules

Acceptance criteria must:

- be written in Russian
- be split into `DEV` and `QA`
- keep `DEV` for developer-accepted checks such as code completion, compilation, lint/static checks, type checks, automated tests, unit tests, integration tests, schema/contract checks, and other engineering quality gates
- keep `QA` understandable by manual QA without reading code, implementation plans, pull requests, or architecture internals
- make `QA` observable through UI behavior, approved API behavior, user-visible output, operator-visible output, documentation, support workflow, release state, or agreed QA tools
- include success and failure paths when behavior has branching logic
- cover documentation, regression, release, and operational validation when relevant
- avoid vague criteria such as `works correctly`, `is scalable`, or `is secure`
- avoid leaking developer-only implementation detail such as unit test names, source files, migration scripts, class names, internal package names, local commands, or code-level sequencing

## Testing Section Rules

Decide whether the task needs a separate QA test plan.

- use a one-line `Проверка:` entry for simple technical tasks that cannot be meaningfully verified in a running app, database, or networked environment
- point to a separate test plan when the result can be touched or verified in a running app, database, or networked environment
- always require a separate test plan for bugs, because reproduction and regression checks must be explicit
- when a separate test plan is needed, keep detailed steps out of Jira and reference the plan from the `Тестирование` section
- when a format profile defines test-plan templates or paths, follow that path convention

## Known Limitations Rules

Use `Известные ограничения (не блокер)` inside the Russian Jira description for long-lived task facts.

- keep each limitation to 3-5 sentences
- classify it as `not a blocker`, `blocker until <date/event>`, or `MVP blocker`
- state where the follow-up belongs, such as a separate ticket or epic
- do not use Jira comments to document stable task limitations; comments are for process discussion

## Output

Return the final Jira description and mention any formatting constraints required by the target Jira tool.
