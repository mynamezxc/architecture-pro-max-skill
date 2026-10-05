# 🧠 Architecture Pro Max

<p align="center">
  <strong>Architecture reasoning skill for AI coding agents</strong><br/>
  Analyze requirements deeply → compare architectures → challenge the recommendation → generate maintainable multi-platform project structure, documentation, tests, data strategy, and upgrade rules.
</p>

<p align="center">
  <img alt="Claude Code" src="https://img.shields.io/badge/Claude_Code-supported-5A67D8?style=for-the-badge"/>
  <img alt="Cursor" src="https://img.shields.io/badge/Cursor-supported-111111?style=for-the-badge"/>
  <img alt="Windsurf" src="https://img.shields.io/badge/Windsurf-supported-06B6D4?style=for-the-badge"/>
  <img alt="Antigravity" src="https://img.shields.io/badge/Antigravity-supported-4285F4?style=for-the-badge"/>
  <img alt="GitHub Copilot" src="https://img.shields.io/badge/GitHub_Copilot-supported-24292F?style=for-the-badge"/>
  <img alt="Kiro" src="https://img.shields.io/badge/Kiro-supported-FF9900?style=for-the-badge"/>
  <img alt="Codex" src="https://img.shields.io/badge/Codex-supported-10A37F?style=for-the-badge"/>
  <img alt="Qoder" src="https://img.shields.io/badge/Qoder-supported-6D5DFB?style=for-the-badge"/>
</p>

<p align="center">
  <a href="#-what-it-does">What it does</a> ·
  <a href="#-reasoning-contract">Reasoning contract</a> ·
  <a href="#-installation">Installation</a> ·
  <a href="#-project-documentation-contract">Project docs</a> ·
  <a href="#-example-crm-web--mobile--desktop">CRM example</a>
</p>

---

## 🎯 What it does

Architecture Pro Max is a portable **Agent Skill** for designing and evolving software systems. It is deliberately architecture-neutral: it does **not** default to Clean Architecture, DDD, microservices, CQRS, Flutter, React, or any other fashionable choice.

For a request such as:

> “Build a CRM with web + mobile + desktop apps, onboarding wizard, seeded demo data, offline mobile access, realtime updates, and room to grow.”

The skill requires the agent to:

1. model the product and user workflows;
2. identify quality attributes and architectural pressure;
3. inspect the existing repository and team constraints when available;
4. compare multiple viable architectures;
5. score them with an explicit decision matrix;
6. recommend a target architecture and a simpler fallback;
7. **challenge its own recommendation** with failure modes and over-engineering checks;
8. design web/mobile/desktop boundaries, API contracts, database ownership, sync and event flows;
9. define migration, seed, fixture, wizard and bootstrap strategy;
10. define unit/integration/contract/E2E/cross-platform testing and test-result storage;
11. generate an AI-readable documentation map so future agents know where to edit safely;
12. define rules for new features, upgrades, refactors and architecture changes.

### Highest-priority goals

`Maintainability` → `Extensibility` → `Clear ownership` → `Testability` → `User requirements` → `Operational simplicity` → `Performance where evidence requires it`.

The skill treats **simplicity as a feature**. A modular monolith may beat microservices. A platform-specific UI may beat aggressive code sharing. A single database may beat distributed persistence. The recommendation must be justified by constraints, not trend-following.

---

## 🧭 Reasoning contract

The agent does not need to expose private chain-of-thought. It must instead produce an auditable decision record:

```text
Requirements & assumptions
        ↓
Capability map + quality attributes
        ↓
Architecture pressure profile (0–5 per axis)
        ↓
2–4 viable alternatives
        ↓
Weighted decision matrix
        ↓
Recommended architecture
        ↓
Adversarial self-review / failure modes
        ↓
Simpler fallback + migration thresholds
        ↓
Repo tree + boundaries + data/API/event contracts
        ↓
Test matrix + docs + change protocol
```

### Required analysis dimensions

| Dimension | Examples |
|---|---|
| Product | CRM, CMS, ERP, marketplace, internal tool, consumer app, developer tool |
| Clients | web, mobile, desktop, CLI, public API, embedded |
| Domain | CRUD-heavy vs workflow/rule-heavy; bounded contexts; audit requirements |
| Data | relational/document/time-series/search/blob; tenancy; retention; reporting |
| Connectivity | online-only, offline cache, offline-first, local-first |
| Interaction | request/response, realtime, background jobs, async events |
| Scale | users, throughput, data size, burstiness, regional distribution |
| Team | size, skill set, ownership boundaries, release model |
| Operations | deployment, observability, rollback, migrations, support burden |
| Security | authn/authz, secrets, PII, compliance, auditability |
| Lifecycle | prototype, product-market fit, long-lived enterprise system |
| Integration | payment, ERP, email, SSO, webhooks, external databases, devices |

---

## 🧩 Architecture families covered

The knowledge base includes guidance for:

- Layered / N-tier
- MVC / MVP / MVVM / MVI / HMVC / PAC / VIPER
- Feature-based / Vertical Slice
- Modular Monolith
- Clean / Onion / Hexagonal (Ports & Adapters)
- Domain-Driven Design and bounded contexts
- CQRS and Event Sourcing
- Event-Driven Architecture
- SOA and Microservices
- Serverless / FaaS
- Microkernel / Plugin architectures
- Pipes & Filters
- Actor / CSP / Reactor patterns
- Offline-first / Local-first / Sync architectures
- BFF / API Gateway / GraphQL federation
- Saga / Outbox / Inbox / Idempotency
- Cache, resilience and distributed-data patterns
- GoF, GRASP and enterprise application patterns as local design tools

See [`skills/architecture-pro-max/references/pattern-catalog.md`](skills/architecture-pro-max/references/pattern-catalog.md).

---

## 📦 Repository structure

```text
architecture-pro-max-skill/
├── README.md
├── AGENTS.md                         # rules for maintaining this repository
├── plugin.json                       # portable Agent Plugins manifest
├── skill.json                        # human/tool metadata
├── skills/
│   └── architecture-pro-max/         # canonical source of truth
│       ├── SKILL.md
│       ├── data/
│       │   ├── architectures.json
│       │   ├── product-profiles.json
│       │   ├── platform-strategies.json
│       │   └── quality-attributes.json
│       ├── references/
│       │   ├── architecture-decision-framework.md
│       │   ├── pattern-catalog.md
│       │   ├── multiplatform-strategy.md
│       │   ├── database-integration.md
│       │   ├── project-structure-standard.md
│       │   ├── testing-quality-gates.md
│       │   ├── ai-maintenance-contract.md
│       │   └── self-critique-checklist.md
│       ├── scripts/
│       │   ├── architect.py          # deterministic planning helper
│       │   └── validate.py
│       └── assets/project-docs/      # templates copied into target projects
├── tools/
│   ├── install.py                    # install into supported AI tools
│   └── generate_adapters.py          # platform wrappers from one source
├── adapters/                         # generated; never hand-edit
├── docs/
├── examples/
└── tests/
```

The **canonical skill is written once**. Platform-specific files are generated from it. This avoids eight independent instruction sets drifting apart.

---

## 🚀 Installation

### Portable Agent Skills / Agent Plugins

Clone or download the repository, then use the installer:

```bash
python tools/install.py --platform claude --target /path/to/project
python tools/install.py --platform cursor --target /path/to/project
python tools/install.py --platform windsurf --target /path/to/project
python tools/install.py --platform antigravity --target /path/to/project
python tools/install.py --platform copilot --target /path/to/project
python tools/install.py --platform kiro --target /path/to/project
python tools/install.py --platform codex --target /path/to/project
python tools/install.py --platform qoder --target /path/to/project
```

Install adapters for every supported client:

```bash
python tools/install.py --platform all --target /path/to/project
```

Preview without writing:

```bash
python tools/install.py --platform all --target /path/to/project --dry-run
```

### Platform mapping

| AI tool | Installed project location | Mode |
|---|---|---|
| Claude Code | `.claude/skills/architecture-pro-max/` | native Agent Skill |
| Cursor | `.cursor/skills/architecture-pro-max/` | native Agent Skill |
| Windsurf | `.windsurf/rules/architecture-pro-max.md` + portable skill | model-decision rule wrapper |
| Antigravity | `.agents/skills/architecture-pro-max/` + `.agents/rules/architecture-pro-max.md` | portable skill + rule |
| GitHub Copilot | `.github/skills/architecture-pro-max/` | native Agent Skill |
| Kiro | `.kiro/skills/architecture-pro-max/` | native Agent Skill |
| Codex | `.agents/skills/architecture-pro-max/` | portable Agent Skill |
| Qoder | `.qoder/skills/architecture-pro-max/` | native Agent Skill |

> The installer never installs runtimes or packages. It only copies repository files into the selected target directory.

---

## ⚡ Use it

Ask naturally:

```text
Design the architecture for a CRM with web, iOS/Android and desktop clients.
We need multi-tenant data, RBAC, realtime notifications, mobile offline mode,
CSV imports, an onboarding wizard, audit logs and seeded demo accounts.
Team: 7 developers. Prefer TypeScript where it makes sense.
```

Or explicitly request the skill:

```text
Use architecture-pro-max to analyze this repository before we add a mobile app.
```

For a deterministic first-pass report:

```bash
python skills/architecture-pro-max/scripts/architect.py \
  --product crm \
  --platform web mobile desktop \
  --team-size 7 \
  --domain-complexity high \
  --scale medium \
  --realtime \
  --offline mobile \
  --integrations 6 \
  --multi-tenant \
  --output architecture-plan.md
```

The script is intentionally heuristic. The AI agent must refine it using repository evidence and user constraints rather than treating the score as truth.

Initialize the AI-readable project documentation contract without overwriting existing docs:

```bash
python skills/architecture-pro-max/scripts/init_project_docs.py --target /path/to/project
```

Use `--dry-run` to preview or `--force` to intentionally replace template files.

---

## 🗂️ Project documentation contract

For a substantial project, the skill recommends an AI-readable documentation structure:

```text
docs/
├── README.md                         # documentation map
├── product/
│   ├── requirements.md
│   └── capability-map.md
├── architecture/
│   ├── README.md                     # current architecture source of truth
│   ├── boundaries.md
│   ├── data-flow.md
│   └── adr/
│       ├── 0001-record-architecture-decisions.md
│       └── ...
├── development/
│   ├── conventions.md
│   ├── dependency-rules.md
│   └── local-setup.md
├── testing/
│   ├── strategy.md
│   ├── matrix.md
│   └── results/
│       ├── web/
│       ├── mobile/
│       ├── desktop/
│       └── cross-platform/
├── operations/
│   ├── environments.md
│   ├── deployment.md
│   └── observability.md
└── ai/
    ├── INDEX.md                      # first file an agent should read
    ├── CODE-MAP.md                   # capability → module → tests → docs
    ├── CHANGE-PROTOCOL.md            # mandatory update/refactor workflow
    └── KNOWN-RISKS.md
```

### Why the AI folder exists

Future agents should not have to rediscover the repository from scratch. `docs/ai/CODE-MAP.md` maps business capabilities to concrete modules, interfaces, migrations, tests and architectural decisions. `CHANGE-PROTOCOL.md` tells an agent what must be updated when it changes a feature or crosses a module boundary.

---

## 🧱 Recommended target-project shape

The exact tree is generated from the product, but a multi-platform business application commonly converges on:

```text
apps/
├── web/
├── mobile/
└── desktop/
services/
└── api/
packages/
├── contracts/        # OpenAPI/schema/generated client contracts
├── domain/           # truly portable domain/value logic only
├── api-client/
├── validation/
├── design-tokens/    # optional cross-client tokens, not full UI components
└── test-utils/
database/
├── migrations/
├── seeds/
├── fixtures/
└── factories/
infra/
docs/
tests/
├── contract/
├── integration/
├── e2e/
└── results/
```

The skill explicitly warns against sharing platform-specific UI or lifecycle code merely to maximize percentage reuse.

---

## 🧪 Quality gates

A feature is not “done” only because it compiles. Depending on risk, the skill requires evidence from:

- unit tests for domain rules;
- integration tests for persistence and external adapters;
- API/schema contract tests;
- migration/rollback tests;
- seed/fixture reproducibility tests;
- web/mobile/desktop E2E tests;
- cross-platform user-journey tests;
- offline/sync conflict tests when applicable;
- authorization and tenant-isolation tests;
- performance/resilience tests when justified;
- test result artifacts stored under `docs/testing/results/` or CI artifacts with a stable index.

---

## 🧠 Example: CRM web + mobile + desktop

A typical recommendation for a 5–10 person team with a complex CRM domain is **not** “start with microservices.” The default candidate set might be:

| Candidate | Why it may fit | Why it may fail |
|---|---|---|
| Layered monolith | fastest delivery | weak boundaries as domain grows |
| **Modular monolith + hexagonal boundaries** | strong module ownership, simple operations, extraction path later | needs discipline around imports and DB schemas |
| Microservices | independent deploy/scale | operational and consistency cost too high for the team |
| Serverless functions | burst handling, low ops in narrow workflows | fragmented domain transactions and local development |

For TypeScript-heavy teams, one implementation option could be:

```text
Web       → Next.js / React
Mobile    → React Native
Desktop   → Tauri + React shell
Backend   → modular TypeScript API
Contracts → OpenAPI + generated clients
Realtime  → WebSocket/SSE at the edge
Async     → transactional outbox only where needed
Database  → one relational cluster, module-owned schemas/tables
Offline   → local mobile store + explicit sync protocol
```

But the skill must challenge that answer: Flutter may be better when mobile/desktop UX sharing matters more than the TypeScript talent pool; native clients may be better when platform integrations dominate; a plain browser/PWA may remove the desktop app entirely if desktop-specific capabilities are weak.

See the generated example at [`examples/crm-multiplatform/architecture-plan.md`](examples/crm-multiplatform/architecture-plan.md).

---

## 🔁 Change and upgrade protocol

When adding or changing a feature, the agent must:

1. locate the capability owner via `docs/ai/CODE-MAP.md`;
2. read relevant ADRs and module-level rules;
3. state whether the change stays inside a boundary or crosses one;
4. update contracts before coupled implementations when an interface changes;
5. add/update migrations, seeds and fixtures deterministically;
6. update tests at the correct layers;
7. run the smallest relevant suite first, then required cross-platform suites;
8. record test evidence;
9. update architecture docs if boundaries/data flow changed;
10. create an ADR when the change is expensive to reverse or changes a project-wide rule.

No architecture pattern is allowed to become ceremony without a problem it solves.

---

## 🛠️ Development

Validate the canonical skill and generated adapters:

```bash
python skills/architecture-pro-max/scripts/validate.py
python tools/generate_adapters.py --check
python -m unittest discover -s tests -v
```

Regenerate adapters after changing the canonical skill:

```bash
python tools/generate_adapters.py
```

Files under `adapters/` are generated and must not be hand-edited.

---

## 📚 Design principles

- **Canonical source of truth:** one skill, generated platform adapters.
- **Progressive disclosure:** `SKILL.md` stays operational; deep knowledge lives in `references/`.
- **Evidence over fashion:** architecture decisions trace to explicit requirements.
- **Reversibility:** prefer choices that can evolve without rewrites.
- **Boundaries before distribution:** get module boundaries right before splitting processes.
- **Contracts before coupling:** client/server and module contracts are explicit and testable.
- **Docs are executable context:** future humans and agents can locate change points quickly.
- **Tests mirror architecture:** test folders and result artifacts align to module and platform boundaries.
- **Self-critique is mandatory:** every major recommendation names failure modes and a simpler alternative.

---

## 📄 License

MIT. See [LICENSE](LICENSE).
