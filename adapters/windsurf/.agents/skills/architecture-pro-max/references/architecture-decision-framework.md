# Architecture decision framework

## Principle

Select the **least complex architecture that satisfies current constraints and preserves a credible evolution path**.

## Candidate families

| Family | Best fit | Main strength | Main cost / warning |
|---|---|---|---|
| Layered monolith | simple CRUD, small teams | low cognitive/operational cost | horizontal layers become tangled as capabilities grow |
| Feature-based monolith | product-oriented CRUD | high discoverability | weak boundaries unless dependencies are enforced |
| Modular monolith | medium/large business systems | strong boundaries + simple deployment | requires disciplined module APIs and ownership |
| Hexagonal / Clean / Onion | volatile infrastructure or test-heavy domain | isolates domain/use cases from adapters | unnecessary interfaces can become ceremony |
| Vertical Slice | use-case-driven API/product | localizes change by feature | cross-cutting rules need deliberate handling |
| DDD | complex rules/workflows/vocabulary | aligns model with business boundaries | overkill for data-entry CRUD |
| CQRS | read/write models materially differ | independently optimized models | more models, consistency and operational complexity |
| Event Sourcing | history is core domain truth | perfect audit/replay/temporal reasoning | versioning, projections and mental model are expensive |
| Microservices | autonomous teams/deploy/scale requirements | organizational and runtime independence | network, consistency, observability, deployment cost |
| Serverless | event/burst workloads, narrow functions | elastic operations | fragmentation, cold starts, distributed transactions |
| Microkernel / Plugin | extensible product ecosystem | stable core + optional capabilities | plugin contracts/versioning become critical |
| Local-first / Offline-first | unreliable connectivity / device autonomy | strong offline UX | conflict resolution and sync protocol are difficult |

## Pressure-to-pattern mapping

Do not use a single score as a verdict. Use it to highlight pressure:

- **High domain complexity + low deploy pressure** → modular monolith + DDD selectively.
- **High deploy/team autonomy + high operational maturity** → consider microservices.
- **High read complexity + stable write domain** → consider CQRS read projections, not necessarily full CQRS.
- **High audit/temporal truth** → consider event sourcing for bounded areas, not automatically the whole system.
- **High integration volatility** → ports/adapters around external systems.
- **High offline pressure** → explicit local store, sync states, conflict semantics, idempotent server APIs.
- **High extension/plugin pressure** → microkernel and versioned extension contracts.
- **Low everything / early validation** → straightforward feature-based monolith.

## Weighted decision matrix

Suggested criteria (adjust weights):

| Criterion | Typical weight |
|---|---:|
| Delivery speed | 15 |
| Maintainability | 20 |
| Domain clarity | 15 |
| Testability | 10 |
| Operational simplicity | 15 |
| Independent scale/deploy | 10 |
| Multi-platform fit | 5 |
| Data consistency | 5 |
| Reversibility/evolution | 5 |

Score 1–5. Explain any score that materially changes the winner.

## Decision rules

1. **Boundaries before processes.** A poor modular monolith becomes poor microservices with a network.
2. **One database is not automatically bad.** In a modular monolith, module-owned tables/schemas can enforce ownership while preserving transactions.
3. **Microservices require an organizational reason.** Independent deployment, scaling, availability, regulation or team ownership must be real.
4. **DDD is selective.** Use rich domain models where rules justify them; CRUD/reference modules may remain simple.
5. **CQRS is divisible.** Add a read model for one expensive query before creating a system-wide command bus.
6. **Events are contracts.** Version and test them like APIs.
7. **No infrastructure abstraction without volatility.** Wrap external systems that are unstable/replaceable; do not create interfaces around every class.
8. **Prefer reversible choices.** Explicit module APIs, contracts, migrations and tests preserve extraction paths.

## Migration thresholds

Document triggers, for example:

```text
Extract module to service only if >= 2 are true:
- independent release cadence repeatedly blocks another team;
- workload scaling differs by >10x for sustained periods;
- availability/SLO differs materially;
- separate compliance/security boundary is required;
- module has stable API/event contract and owned data;
- operating team can support deployment/observability/on-call independently.
```

Avoid calendar-based migrations such as “move to microservices in phase 2” without evidence.
