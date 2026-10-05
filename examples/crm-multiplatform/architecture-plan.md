# Architecture Plan — CRM

## 1. Scope

Platforms: **web, mobile, desktop**  
Team size: **7**  
Domain complexity: **high**  
Scale pressure: **medium**  
Realtime: **yes**  
Offline: **mobile**  
External integrations: **6**  
Multi-tenant: **yes**

## 2. Architecture pressure profile

| Axis | Pressure |
|---|---:|
| domain | 5/5 |
| scale | 3/5 |
| team | 2/5 |
| deploy | 1/5 |
| ops | 2/5 |
| integration | 4/5 |
| offline | 4/5 |
| realtime | 4/5 |
| longevity | 5/5 |

## 3. Capability map (starter)

identity, customers, sales, activity, workflow, reporting, admin

## 4. Candidate ranking

Heuristic scores are a starting point, not a substitute for repository/user evidence.

| Rank | Candidate | Score |
|---:|---|---:|
| 1 | Modular Monolith + Hexagonal Boundaries | 60.0 |
| 2 | Modular Monolith | 57.0 |
| 3 | Local-first + Sync Backend | 45.0 |
| 4 | Vertical Slice Architecture | 40.0 |
| 5 | Microkernel / Plugin | 40.0 |

## 5. Recommendation

**Modular Monolith + Hexagonal Boundaries**

- Keep one deployable backend initially; enforce business-module APIs and data ownership.
- Define extraction thresholds instead of scheduling a premature microservice migration.
- Place volatile third-party systems behind explicit adapters and contract tests.
- Use synchronous APIs for commands that need immediate result; realtime channels/events for notifications and asynchronous side effects.
- Define a local store, sync states, idempotent mutation IDs and per-entity conflict policy.
- Share schemas/contracts/generated clients first; keep platform lifecycle and UX code local unless evidence supports sharing.
- Make tenant isolation an invariant tested at repository/query and authorization boundaries.

## 6. Backend/module structure

```text
services/api/
└── src/modules/
│   ├── identity/
│   ├── customers/
│   ├── sales/
│   ├── activity/
│   ├── workflow/
│   ├── reporting/
│   ├── admin/
```

Each module owns its internal model and persistence mappings. Cross-module access goes through public application interfaces/contracts, not internal repositories.

## 7. Multi-platform structure

```text
apps/
├── web/
├── mobile/
└── desktop/
packages/
├── contracts/
├── api-client/
├── domain/          # pure runtime-neutral rules only
├── validation/
├── design-tokens/
└── test-utils/
```

Do not force platform-specific UI/navigation into shared packages solely to maximize reuse.

## 8. Data and communication

- Start with a relational source of truth for business data unless workload evidence says otherwise.
- Clients communicate through versioned API contracts; do not share production DB access.
- Keep synchronous transactions inside the backend/module boundary.
- Add an outbox only for DB changes whose event publication must be reliable.
- Separate migrations, seeds, fixtures and factories.
- Make setup/onboarding wizard steps resumable and idempotent when external side effects exist.

## 9. Tests

```text
module tests            → domain + use cases
integration tests       → DB + external adapters
contract tests          → API/events
database tests          → migrations + seeds
apps/*/e2e              → platform journeys
tests/cross-platform    → shared business scenarios
docs/testing/results    → compact evidence + CI links
```

## 10. Self-critique

Strongest argument against this recommendation: **The recommended boundaries add up-front structure and can slow an early team if the domain remains mostly CRUD.**

Simpler fallback: **Feature-based monolith**.

Do not extract microservices until real independent deployment/scale/ownership/compliance pressure exists and the candidate module has stable contracts plus owned data.

## 11. Alternatives that remain credible

- **Modular Monolith** — score 57.0; reconsider if its matching pressure increases.
- **Local-first + Sync Backend** — score 45.0; reconsider if its matching pressure increases.
- **Vertical Slice Architecture** — score 40.0; reconsider if its matching pressure increases.

## 12. Required project documentation

Create `docs/ai/INDEX.md`, `CODE-MAP.md`, `CHANGE-PROTOCOL.md`, architecture source-of-truth, ADRs and per-platform test-result indices before the system becomes large enough that ownership is ambiguous.
