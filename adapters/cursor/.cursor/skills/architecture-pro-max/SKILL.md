---
name: architecture-pro-max
description: Deeply analyze software requirements and existing repositories, compare architecture options, design maintainable web/mobile/desktop/backend systems, define module boundaries, data/API/event communication, database migrations/seeds/wizards, testing and AI-readable project documentation. Use for new system architecture, major features, multi-platform products, CRM/CMS/ERP/SaaS design, refactors, monolith-vs-microservices decisions, DDD/Clean/Hexagonal/Vertical Slice choices, offline/realtime design, or when a project needs clear folder/rule/test/documentation structure.
license: MIT
metadata:
  version: 0.1.0
  category: software-architecture
---

# Architecture Pro Max

Design architecture from **requirements and constraints**, not from pattern popularity.

## Core contract

For substantial architecture work, produce an auditable decision summary rather than hidden chain-of-thought. Include:

- requirements and assumptions;
- capability map and quality attributes;
- architecture-pressure profile;
- 2–4 viable alternatives;
- weighted decision matrix or equivalent explicit comparison;
- recommendation and why it wins;
- rejected alternatives and what would make them win later;
- adversarial self-review / failure modes;
- simpler fallback;
- migration and extraction thresholds;
- repository/folder structure;
- module ownership and dependency direction;
- API/event/data contracts;
- database, migration, seed and fixture strategy;
- wizard/bootstrap/onboarding implications when relevant;
- test matrix and result locations;
- AI-readable documentation/change protocol.

Never claim one architecture is universally best.

## Step 0 — Determine task mode

Choose one:

1. **Greenfield architecture** — product/system does not exist yet.
2. **Repository evolution** — inspect current structure before proposing changes.
3. **Feature architecture** — scope a new capability inside an existing system.
4. **Architecture review** — critique current boundaries, coupling, tests and operational complexity.
5. **Migration** — define safe intermediate states, compatibility windows and rollback.

For repository evolution/review, inspect existing manifests, modules, DB schema/migrations, APIs, tests, CI and architecture docs before selecting patterns.

## Step 1 — Build the requirement model

Extract or infer, marking uncertain items as assumptions:

- product type and primary user journeys;
- business capabilities and workflows;
- platforms: web/mobile/desktop/CLI/public API/embedded;
- roles, permissions, tenancy and audit needs;
- domain complexity: CRUD vs rule/workflow intensive;
- data shapes, consistency and reporting/search needs;
- realtime/background/asynchronous requirements;
- offline/local-first requirements and conflict policy;
- external integrations and failure characteristics;
- expected scale and growth uncertainty;
- team size, skills, ownership and deployment maturity;
- security/compliance/privacy requirements;
- product lifecycle: prototype vs long-lived system;
- release cadence and backward-compatibility requirements.

If missing information materially changes the architecture, state the branching assumptions. Do not stall a user with many questions when a bounded assumption can keep progress moving.

## Step 2 — Build a capability map

Group features by cohesive business capability before choosing technical services/modules.

Example CRM capabilities:

```text
Identity & Access
Customer / Account
Lead & Opportunity
Activity / Communication
Workflow / Automation
Catalog / Pricing
Reporting / Analytics
Import / Export
Notification
Administration / Tenant Settings
```

Do not map each database table or screen to a service.

## Step 3 — Score architectural pressure

Use 0–5 values for the relevant axes:

- domain complexity;
- independent deployment pressure;
- independent scaling pressure;
- team autonomy pressure;
- integration volatility;
- realtime/event pressure;
- offline/sync pressure;
- compliance/audit pressure;
- data consistency pressure;
- cross-platform reuse pressure;
- operational maturity;
- change frequency / longevity.

Use `scripts/architect.py` for a deterministic first pass when useful. Treat its result as evidence to challenge, not as authority.

## Step 4 — Compare alternatives

Normally compare at least three candidates from `references/architecture-decision-framework.md`.

Typical baseline:

- simplest workable architecture;
- recommended balanced architecture;
- more distributed/scalable architecture.

Examples:

```text
Layered monolith
vs Modular Monolith + Hexagonal boundaries
vs Microservices
```

or:

```text
Web-only responsive/PWA
vs Web + cross-platform client
vs Native clients
```

Do not compare fake strawman alternatives.

## Step 5 — Select boundaries before technologies

Define:

- modules/bounded contexts;
- allowed dependency direction;
- public module interfaces;
- transaction boundaries;
- data ownership;
- sync/event ownership;
- client/server contracts.

Only then map technologies/frameworks based on current repo, team competence, ecosystem and platform constraints. When the user asks for stack/language selection or the choice materially affects architecture, load `references/stack-selection.md`.

## Step 6 — Multi-platform strategy

When more than one client exists, load `references/multiplatform-strategy.md`.

Classify every candidate shared asset:

```text
Share aggressively:
- schemas/contracts
- generated API clients
- validation rules that are truly platform-neutral
- domain/value logic without UI/runtime dependencies
- design tokens
- test fixtures

Share cautiously:
- state management
- navigation abstractions
- storage wrappers

Usually keep platform-specific:
- navigation lifecycle
- native integrations
- accessibility semantics
- windowing/input behavior
- platform UI components when interaction models differ
```

Do not optimize for a single “code reuse percentage.” Optimize for change cost and platform quality.

## Step 7 — Data and communication design

Load `references/database-integration.md` when data or integration is material.

Required decisions:

- source of truth per data set;
- transaction boundary;
- direct calls vs async events;
- API style and versioning;
- idempotency strategy;
- outbox/inbox only when reliability needs justify them;
- cache ownership/invalidation;
- offline store and sync conflict policy;
- migration, rollback, seed, fixture and factory strategy;
- reporting/search projections where necessary.

Client applications should normally access server data through explicit APIs/contracts rather than directly sharing the production database.

## Step 8 — Folder and documentation architecture

Load `references/project-structure-standard.md`.

Folder structure must communicate product boundaries. Prefer capability/module names over giant global `controllers/`, `services/`, `repositories/` folders once a project grows.

For substantial systems, create or recommend the documentation contract described in `references/ai-maintenance-contract.md`. When the user wants it scaffolded, run `scripts/init_project_docs.py --target <project-root>`; preserve existing files unless replacement is explicitly intended.

## Step 9 — Testing architecture

Load `references/testing-quality-gates.md`.

Tests must mirror architectural boundaries and risk:

- domain unit tests;
- module/application tests;
- DB/adapter integration tests;
- contract/schema tests;
- migration + seed tests;
- per-platform E2E;
- cross-platform journeys;
- offline/sync tests;
- authorization/tenant isolation;
- resilience/performance/security only where risk warrants.

Record stable test commands and expected result locations so future agents can verify changes.

## Step 10 — Mandatory self-critique

Before finalizing, apply `references/self-critique-checklist.md`.

At minimum ask:

- Am I solving current requirements or imagined scale?
- Could one process/database satisfy this with stronger module boundaries?
- Which complexity is irreversible?
- What is the failure mode if the recommendation is wrong?
- Which part will the team struggle to operate?
- Is code sharing harming platform UX?
- Are events/CQRS/DDD improving clarity or just adding ceremony?
- What measurable trigger justifies the next architecture step?

Revise the recommendation if the critique exposes unnecessary complexity.

## Step 11 — Change protocol for implementation

For implementation or refactor work:

1. read `docs/ai/INDEX.md` if it exists;
2. locate the capability/module and its tests;
3. read relevant ADRs and module-local agent/rule files;
4. define the contract change before modifying multiple consumers;
5. implement inside the owning boundary;
6. update migrations/seeds/fixtures deterministically;
7. run focused tests, then required integration/cross-platform suites;
8. record or link test results;
9. update CODE-MAP/docs when file ownership or data flow changes;
10. create an ADR for expensive-to-reverse decisions.

## Output template

Use sections appropriate to the task:

```markdown
# Architecture Decision

## 1. Problem and scope
## 2. Assumptions / unknowns
## 3. Capability map
## 4. Quality attributes and pressure profile
## 5. Alternatives
## 6. Decision matrix
## 7. Recommended architecture
## 8. Module boundaries and dependency rules
## 9. Web/mobile/desktop strategy
## 10. Data, API, event and sync design
## 11. Database migrations, seeds, fixtures, wizard/bootstrap
## 12. Repository tree
## 13. Test strategy and result layout
## 14. AI documentation/change protocol
## 15. Self-critique and risks
## 16. Simpler fallback
## 17. Migration/extraction triggers
```

Be concrete: show trees, dependency arrows, interface ownership, test locations and migration rules. Avoid naming patterns without explaining which problem they solve here.

## References

Load on demand:

- `references/architecture-decision-framework.md`
- `references/pattern-catalog.md`
- `references/multiplatform-strategy.md`
- `references/stack-selection.md`
- `references/database-integration.md`
- `references/project-structure-standard.md`
- `references/testing-quality-gates.md`
- `references/ai-maintenance-contract.md`
- `references/self-critique-checklist.md`
