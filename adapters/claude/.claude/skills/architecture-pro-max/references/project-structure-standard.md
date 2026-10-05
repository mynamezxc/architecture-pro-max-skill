# Project structure standard

## Primary rule

A developer or AI agent should locate a business capability and its tests/docs without scanning the whole repository.

## Multi-platform monorepo baseline

```text
apps/
├── web/
│   ├── src/
│   └── tests/
├── mobile/
│   ├── src/
│   └── tests/
└── desktop/
    ├── src/
    └── tests/
services/
└── api/
    └── src/
        └── modules/
            ├── identity/
            ├── customers/
            ├── sales/
            └── reporting/
packages/
├── contracts/
├── api-client/
├── domain/
├── validation/
├── design-tokens/
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

Adapt to the stack. Do not create empty layers only to mirror the diagram.

## Backend module shape

For complex modules:

```text
sales/
├── domain/
│   ├── opportunity.*
│   ├── value-objects/
│   └── events/
├── application/
│   ├── create-opportunity.*
│   ├── qualify-lead.*
│   └── ports/
├── infrastructure/
│   ├── persistence/
│   └── integrations/
├── api/
└── tests/
```

For simple CRUD/reference data, a lighter vertical slice is preferred:

```text
countries/
├── routes.*
├── service.*
├── repository.*
└── tests/
```

Do not force rich domain layers into trivial modules.

## Dependency rules

Recommended conceptual direction:

```text
API/UI adapters → application/use cases → domain
Infrastructure adapters → application/domain ports
```

Modules communicate through public interfaces/contracts, not imports into another module's internals.

Examples of enforceable rules:
- `sales` may import `identity/public`, not `identity/internal`;
- apps may import `packages/contracts`, not backend ORM models;
- generated API client is versioned from the canonical schema;
- database code cannot leak ORM entities into client contracts.

## Names

Prefer product language:

```text
customers/
opportunities/
workflow/
reporting/
```

over vague technical buckets when scale grows:

```text
helpers/
utils/
managers/
common/
services/
```

`shared/` is allowed only with a clear ownership rule; it must not become a dumping ground.

## Test/result layout

Tests may live near modules for locality, while cross-module/platform tests stay centralized:

```text
module/tests/               # unit/application
integration-tests/          # external adapters/DB
contract-tests/             # APIs/events
apps/*/e2e/                 # platform E2E
tests/cross-platform/       # shared journeys
docs/testing/results/       # human-readable evidence/index
```
