# AI maintenance contract

## Purpose

Make the repository legible to both humans and coding agents without stuffing every rule into always-on context.

## Documentation map

```text
docs/
├── README.md
├── product/
│   ├── requirements.md
│   └── capability-map.md
├── architecture/
│   ├── README.md
│   ├── boundaries.md
│   ├── data-flow.md
│   └── adr/
├── development/
│   ├── conventions.md
│   ├── dependency-rules.md
│   └── local-setup.md
├── testing/
│   ├── strategy.md
│   ├── matrix.md
│   └── results/
├── operations/
│   ├── environments.md
│   ├── deployment.md
│   └── observability.md
└── ai/
    ├── INDEX.md
    ├── CODE-MAP.md
    ├── CHANGE-PROTOCOL.md
    └── KNOWN-RISKS.md
```

## `docs/ai/INDEX.md`

Keep short. It tells an agent what to read next based on task type.

Example:

```markdown
# AI index

Before code changes: read architecture/README.md and ai/CODE-MAP.md.
For DB changes: also read architecture/data-flow.md and database migration rules.
For web: read apps/web/AGENTS.md if present.
For mobile: read apps/mobile/AGENTS.md if present.
For architecture changes: read all applicable ADRs and ai/CHANGE-PROTOCOL.md.
```

## `CODE-MAP.md`

Map capabilities to code and tests:

| Capability | Owner module | Public contract | DB ownership | Tests | Docs |
|---|---|---|---|---|---|
| Opportunities | `services/api/.../sales` | `contracts/sales` | `sales.*` | `sales/tests` | ADR-012 |

This file should link, not duplicate entire designs.

## `CHANGE-PROTOCOL.md`

Mandatory rules for agents and humans:

### New feature
1. identify owner capability;
2. define acceptance scenarios;
3. define/extend contract;
4. implement inside owner module;
5. add migrations/seeds/fixtures;
6. tests at required layers;
7. update CODE-MAP/docs if new ownership exists.

### Refactor
- preserve public contracts unless change is intentional;
- use characterization tests for risky legacy behavior;
- separate mechanical moves from behavior changes where possible.

### Dependency upgrade
- read release/migration notes;
- list affected modules;
- update one boundary at a time for major upgrades;
- run platform-specific and cross-platform suites;
- record compatibility decisions.

### Architecture change
- create ADR before or with implementation;
- include alternatives and migration plan;
- define rollback/roll-forward;
- update diagrams, CODE-MAP and dependency rules.

## Local instructions

Large monorepos should put scoped `AGENTS.md`/rules beside major apps/modules when the tooling supports hierarchical instructions. Keep local files about local invariants; keep the canonical architecture in docs.
