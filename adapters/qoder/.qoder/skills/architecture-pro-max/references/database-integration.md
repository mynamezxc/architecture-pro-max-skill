# Database and integration design

## Default ownership

- Server-side business data has one authoritative owner.
- Client apps use explicit APIs/contracts.
- Local client databases are caches/work queues/offline stores unless the product is intentionally local-first.
- In a modular monolith, one DB cluster is acceptable; ownership is enforced at module/schema/table and code boundaries.
- In microservices, avoid shared-write databases between services.

## Relational-first heuristic

For CRM/CMS/ERP/business workflows, a relational database is often the safest default because transactions, constraints, joins and reporting are central. Add specialized stores for measured needs:

- search engine for advanced full-text/faceting;
- object storage for files;
- time-series store for high-volume metrics;
- cache for latency/throughput hotspots;
- warehouse/lake for analytics workloads.

Do not create polyglot persistence by default.

## Migrations

Every schema change must specify:

1. forward migration;
2. compatibility window between old/new app versions if rolling deploys exist;
3. backfill strategy;
4. rollback or roll-forward strategy;
5. large-table locking/online migration considerations;
6. tests against representative data.

Prefer expand/contract for breaking changes:

```text
expand schema → deploy compatible writers/readers → backfill → switch reads → remove legacy field
```

## Seeds, fixtures and factories

Keep distinct purposes:

- `seeds/` — deterministic baseline/demo/reference data;
- `fixtures/` — stable test scenarios;
- `factories/` — programmatic builders for variable tests;
- `migrations/` — schema/data evolution, not demo data.

Seeds must be idempotent or explicitly resettable. Do not depend on random IDs without a stable mapping when tests/docs reference them.

## Wizard/bootstrap flows

When a product has onboarding/setup wizard:

- model wizard state explicitly;
- make steps resumable/idempotent;
- validate permissions and prerequisites per step;
- separate configuration writes from irreversible external side effects;
- log progress and failures;
- test resume, skip, retry and rollback paths;
- provide seeded/demo mode separately from production bootstrap.

## API choice

REST/OpenAPI is a strong default for multi-platform business applications because generation, caching, observability and tooling are mature.

Consider GraphQL when clients require flexible graph-shaped reads and the team can operate schema governance/cost controls.

Consider gRPC for trusted service-to-service or strongly typed high-throughput internal communication, not automatically for browser clients.

## Events

Use events for facts and asynchronous decoupling, not to hide synchronous dependencies.

Good:

```text
OpportunityWon → analytics projection / email / commission workflow
```

Questionable:

```text
CreateCustomerRequested → ten event hops → user waits for response
```

## Outbox

Use a transactional outbox when a DB state change and published event must not diverge.

```text
DB transaction:
  update aggregate
  insert outbox row

publisher:
  read outbox
  publish
  mark delivered
```

Consumers still need idempotency.

## Integration adapters

External systems should normally sit behind adapters when:
- provider APIs are volatile;
- multiple providers exist;
- test isolation matters;
- vendor models differ from domain models.

Do not wrap stable standard library calls simply to claim hexagonal architecture.
