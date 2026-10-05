# Change protocol

## New feature
- Identify owner capability and acceptance scenarios.
- Define contract changes before editing multiple consumers.
- Keep implementation inside the owning boundary.
- Add deterministic migrations/seeds/fixtures when needed.
- Add tests at appropriate layers and record evidence.
- Update CODE-MAP/docs when ownership/data flow changes.

## Upgrade
- Read migration/release notes.
- List affected modules/platforms.
- Prefer incremental compatibility steps for major upgrades.
- Run affected platform plus cross-platform suites.

## Architecture change
- Create/update ADR with alternatives, trade-offs and migration plan.
- Define rollback or safe roll-forward.
- Update boundaries/data-flow/dependency rules.
