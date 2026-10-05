# Testing and quality gates

## Test by risk, not by pyramid dogma

| Layer | Validates | Typical owner |
|---|---|---|
| Unit/domain | rules, calculations, state transitions | module |
| Application/use-case | orchestration and ports | module |
| Integration | DB, queues, filesystem, third-party adapters | backend/platform |
| Contract | API/event schema compatibility | producer + consumers |
| Migration | schema evolution, backfill, rollback/roll-forward | data/backend |
| E2E | platform user journeys | web/mobile/desktop |
| Cross-platform | same business scenario across clients | product/system |
| Non-functional | performance, resilience, security | risk owner |

## Minimum feature checklist

For a normal business feature:

- [ ] domain/business rule coverage where rules exist;
- [ ] authorization/tenant boundaries tested;
- [ ] persistence behavior tested if queries/mappings changed;
- [ ] API/event contract updated and validated;
- [ ] migration test if schema changed;
- [ ] seed/fixture updated if required;
- [ ] one happy-path E2E in each materially affected client;
- [ ] failure/edge path proportional to risk;
- [ ] docs/code map updated if ownership changed.

## Multi-platform result structure

```text
docs/testing/results/
├── README.md
├── web/
│   └── latest.md
├── mobile/
│   ├── android-latest.md
│   └── ios-latest.md
├── desktop/
│   ├── windows-latest.md
│   ├── macos-latest.md
│   └── linux-latest.md
└── cross-platform/
    └── latest.md
```

The files may link to CI artifacts instead of storing huge logs. They should contain:
- commit/build identifier;
- environment;
- command/workflow;
- passed/failed/skipped counts;
- known failures;
- artifact/report links when available.

## Contract tests

Treat API and event contracts as versioned interfaces. Check:
- required/optional fields;
- enum evolution;
- backward compatibility;
- error schemas;
- pagination/cursor behavior;
- idempotency semantics;
- authorization behavior.

## Offline/sync tests

Required when offline mode exists:
- create/update/delete while offline;
- reconnect after long delay;
- duplicate retry;
- server changed same entity;
- clock skew/order variation;
- partial batch failure;
- conflict resolution UI;
- schema migration of local store.

## Seed/wizard tests

- clean database bootstrap;
- repeated/idempotent execution;
- partial failure and retry;
- seeded references remain stable;
- onboarding wizard resume after restart;
- permission failure mid-step;
- external side-effect retry without duplication.

## Quality gates for architecture change

Do not merge a boundary change without:
- dependency-rule update;
- contract/migration strategy;
- affected ADR/docs;
- focused tests;
- rollback or safe roll-forward plan.
