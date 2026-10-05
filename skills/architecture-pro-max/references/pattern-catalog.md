# Pattern catalog — selection reference

This is a decision index, not a requirement to use every pattern.

## UI / presentation

| Pattern | Use when | Avoid when / weakness |
|---|---|---|
| MVC | conventional web/UI separation | controller becomes a dumping ground |
| MVP | presenter-driven, highly testable UI | excessive interfaces/boilerplate |
| MVVM | rich binding/reactive state | giant ViewModels |
| MVI / Redux / Elm style | deterministic unidirectional state | too verbose for simple forms |
| HMVC | hierarchical UI/modules | nested controllers become hard to trace |
| PAC | complex hierarchical interactive agents | uncommon, high learning cost |
| VIPER / VIP | large mobile feature modules | too many types/files for small apps |
| Coordinator | navigation must be separated from screens | unnecessary for shallow flows |

## GoF creational

- Factory Method — runtime creation variation.
- Abstract Factory — consistent family of implementations.
- Builder — complex optional construction.
- Prototype — clone configured objects.
- Singleton — truly process-unique resource; beware global state.

## GoF structural

- Adapter — normalize third-party/provider interfaces.
- Bridge — independent abstraction and implementation dimensions.
- Composite — tree structures with uniform leaf/container behavior.
- Decorator — stack cross-cutting behavior without changing core object.
- Facade — simplify a subsystem boundary.
- Flyweight — share repeated immutable state.
- Proxy — remote/lazy/protection/caching indirection.

## GoF behavioral

- Chain of Responsibility — middleware/validation pipeline.
- Command — queueable/undoable/action object; CQRS commands.
- Interpreter — small DSL/grammar; prefer parser tools for large languages.
- Iterator — encapsulated traversal.
- Mediator — reduce many-to-many object coordination.
- Memento — snapshots/undo.
- Observer — in-process event notification.
- State — behavior varies by explicit lifecycle state.
- Strategy — interchangeable algorithm/policy.
- Template Method — stable algorithm skeleton with overridable steps.
- Visitor — add operations to stable object hierarchies/ASTs.

## Enterprise application

- Transaction Script — simple use cases/CRUD.
- Domain Model — rich business behavior.
- Service Layer / Application Service — use-case boundary.
- Active Record — fast CRUD, persistence-coupled objects.
- Data Mapper — persistence-independent domain model.
- Repository — aggregate/domain collection abstraction.
- Unit of Work — transactional change tracking.
- Identity Map — one in-memory identity per persistence context.
- Specification — composable business predicates.
- Query Object — explicit complex query representation.

## Architectural

- Layered / N-tier — simple separation by technical responsibility.
- Feature folders — locality by product capability.
- Vertical Slice — one use case end-to-end.
- Modular Monolith — module boundaries in one deployable.
- Hexagonal / Ports & Adapters — isolate core from external adapters.
- Onion / Clean — dependency direction toward stable core.
- DDD — strategic and tactical domain modeling.
- Microkernel — plugin/extensibility architecture.
- Pipes & Filters — transformation pipelines/ETL/compiler.
- Event-Driven — async decoupling and integration.
- Microservices — independently owned/deployed runtime services.
- Serverless — managed event/function runtime.

## Distributed / integration

- Pub/Sub — one event to many subscribers.
- Message Queue / Competing Consumers — distribute jobs.
- Saga — long-running distributed transaction with compensation.
- Transactional Outbox — atomically persist state + event intent.
- Inbox / deduplication — idempotent message consumption.
- Idempotency Key — retry-safe external mutation.
- Circuit Breaker — stop hammering failing dependencies.
- Retry + backoff + jitter — transient recovery.
- Bulkhead — isolate resource pools/failure domains.
- Timeout — bound external wait.
- API Gateway — unified ingress/routing/policy.
- BFF — client-specific backend aggregation.
- Strangler Fig — incremental legacy replacement.
- Anti-Corruption Layer — isolate foreign domain models.

## Data / cache

- Cache Aside — application-managed read cache.
- Read Through / Write Through / Write Behind — cache-managed persistence flows.
- Materialized View — precomputed read projection.
- CDC — derive change stream from DB log.
- Sharding — partition data for scale/ownership.
- Replication — read/availability copies.
- Event-Carried State Transfer — event contains consumer-required state.

## Concurrency

- Producer–Consumer — queue between producers/workers.
- Worker Pool — bounded parallel execution.
- Reactor — readiness/event loop for many IO sources.
- Proactor — completion-based async IO.
- Actor Model — isolated state + messages.
- CSP — communicating processes/channels.
- Future/Promise — handle eventual result.

## DDD tactical

- Entity — identity-based domain object.
- Value Object — immutable value semantics.
- Aggregate / Aggregate Root — consistency and modification boundary.
- Domain Service — domain operation with no natural entity owner.
- Domain Event — business fact.
- Repository — aggregate access abstraction.
- Factory — enforce valid aggregate creation.
- Specification — named/composable rule.

## GRASP reminders

Information Expert, Creator, Controller, Low Coupling, High Cohesion, Polymorphism, Pure Fabrication, Indirection, Protected Variations.

## Selection warning

Patterns add vocabulary and constraints. If removing a pattern makes the code easier without losing a required quality attribute, remove it.
