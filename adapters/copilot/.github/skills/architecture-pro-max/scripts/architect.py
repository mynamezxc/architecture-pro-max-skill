#!/usr/bin/env python3
"""Deterministic first-pass architecture planner. Standard library only."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from typing import Dict, List

BASE = Path(__file__).resolve().parents[1]


def load(name: str):
    return json.loads((BASE / 'data' / name).read_text(encoding='utf-8'))


def level(v: str) -> int:
    return {'low': 1, 'medium': 3, 'high': 5}[v]


def score_candidates(args) -> List[Dict]:
    arch = load('architectures.json')
    domain = level(args.domain_complexity)
    scale = level(args.scale)
    team = min(5, max(1, round(args.team_size / 3)))
    deploy_pressure = 1 if args.team_size < 8 else 3 if args.team_size < 20 else 5
    ops_maturity = 1 if args.team_size < 5 else 2 if args.team_size < 10 else 3 if args.team_size < 25 else 4
    integration = min(5, 1 + args.integrations // 2)
    offline = 1 if args.offline == 'none' else 4 if args.offline == 'mobile' else 5
    realtime = 4 if args.realtime else 1
    longevity = 5 if args.lifecycle == 'long-lived' else 3 if args.lifecycle == 'normal' else 1

    pressures = {
        'domain': domain, 'scale': scale, 'team': team, 'deploy': deploy_pressure,
        'ops': ops_maturity, 'integration': integration, 'offline': offline,
        'realtime': realtime, 'longevity': longevity,
    }

    results = []
    for a in arch:
        s = 0.0
        # reward fit to domain/scale/deploy/offline; penalize operational complexity beyond maturity
        s += 4 * (5 - abs(a['domain'] - domain))
        s += 2 * (5 - abs(a['scale'] - scale))
        s += 2 * (5 - abs(a['deploy'] - deploy_pressure))
        s += 2 * (5 - abs(a['offline'] - offline))
        s -= 3 * max(0, a['ops'] - ops_maturity)
        s -= 2 * max(0, a['complexity'] - max(2, domain))
        if args.product in a.get('best_for', []):
            s += 6
        if args.integrations >= 4 and a['id'] == 'hexagonal-modular-monolith':
            s += 7
        if longevity >= 4 and a['id'] in {'modular-monolith','hexagonal-modular-monolith'}:
            s += 5
        if args.team_size < 12 and a['id'] == 'microservices':
            s -= 12
        if offline >= 4 and a['id'] == 'local-first':
            s += 9
        if args.offline == 'mobile' and a['id'] == 'local-first':
            s -= 3  # local-first entire system may be excessive for mobile-only offline
        results.append({'id': a['id'], 'name': a['name'], 'score': round(s, 1), 'meta': a})
    results.sort(key=lambda x: x['score'], reverse=True)
    return pressures, results


def recommendation_notes(args, winner):
    notes = []
    if winner['id'] in {'modular-monolith','hexagonal-modular-monolith'}:
        notes.append('Keep one deployable backend initially; enforce business-module APIs and data ownership.')
        notes.append('Define extraction thresholds instead of scheduling a premature microservice migration.')
    if args.integrations >= 4:
        notes.append('Place volatile third-party systems behind explicit adapters and contract tests.')
    if args.realtime:
        notes.append('Use synchronous APIs for commands that need immediate result; realtime channels/events for notifications and asynchronous side effects.')
    if args.offline != 'none':
        notes.append('Define a local store, sync states, idempotent mutation IDs and per-entity conflict policy.')
    if len(args.platform) > 1:
        notes.append('Share schemas/contracts/generated clients first; keep platform lifecycle and UX code local unless evidence supports sharing.')
    if args.multi_tenant:
        notes.append('Make tenant isolation an invariant tested at repository/query and authorization boundaries.')
    return notes


def render(args) -> str:
    pressures, ranked = score_candidates(args)
    winner = ranked[0]
    alt = ranked[1:4]
    platforms = ', '.join(args.platform)
    notes = recommendation_notes(args, winner)
    profile = load('product-profiles.json').get(args.product, {})
    modules = profile.get('modules', ['identity','core','reporting'])

    rows = '\n'.join(f"| {i+1} | {r['name']} | {r['score']:.1f} |" for i, r in enumerate(ranked[:5]))
    pressure_rows = '\n'.join(f"| {k} | {v}/5 |" for k, v in pressures.items())
    notes_md = '\n'.join(f'- {n}' for n in notes)
    mod_tree = '\n'.join(f'│   ├── {m}/' for m in modules)

    simpler = 'Feature-based monolith' if winner['id'] not in {'layered-monolith','feature-monolith'} else 'Layered monolith'
    strongest_against = (
        'The recommended boundaries add up-front structure and can slow an early team if the domain remains mostly CRUD.'
        if winner['id'] in {'modular-monolith','hexagonal-modular-monolith'} else
        'The simple structure may accumulate coupling quickly if workflows and integration count grow.'
    )

    return f"""# Architecture Plan — {args.product.upper()}

## 1. Scope

Platforms: **{platforms}**  
Team size: **{args.team_size}**  
Domain complexity: **{args.domain_complexity}**  
Scale pressure: **{args.scale}**  
Realtime: **{'yes' if args.realtime else 'no'}**  
Offline: **{args.offline}**  
External integrations: **{args.integrations}**  
Multi-tenant: **{'yes' if args.multi_tenant else 'no'}**

## 2. Architecture pressure profile

| Axis | Pressure |
|---|---:|
{pressure_rows}

## 3. Capability map (starter)

{', '.join(modules)}

## 4. Candidate ranking

Heuristic scores are a starting point, not a substitute for repository/user evidence.

| Rank | Candidate | Score |
|---:|---|---:|
{rows}

## 5. Recommendation

**{winner['name']}**

{notes_md}

## 6. Backend/module structure

```text
services/api/
└── src/modules/
{mod_tree}
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

Strongest argument against this recommendation: **{strongest_against}**

Simpler fallback: **{simpler}**.

Do not extract microservices until real independent deployment/scale/ownership/compliance pressure exists and the candidate module has stable contracts plus owned data.

## 11. Alternatives that remain credible

""" + '\n'.join(f"- **{x['name']}** — score {x['score']:.1f}; reconsider if its matching pressure increases." for x in alt) + """

## 12. Required project documentation

Create `docs/ai/INDEX.md`, `CODE-MAP.md`, `CHANGE-PROTOCOL.md`, architecture source-of-truth, ADRs and per-platform test-result indices before the system becomes large enough that ownership is ambiguous.
"""


def main():
    p = argparse.ArgumentParser(description='Generate a deterministic first-pass architecture plan.')
    p.add_argument('--product', default='saas', choices=['crm','cms','erp','marketplace','saas','internal-tool','developer-tool'])
    p.add_argument('--platform', nargs='+', default=['web'])
    p.add_argument('--team-size', type=int, default=5)
    p.add_argument('--domain-complexity', choices=['low','medium','high'], default='medium')
    p.add_argument('--scale', choices=['low','medium','high'], default='medium')
    p.add_argument('--realtime', action='store_true')
    p.add_argument('--offline', choices=['none','mobile','all'], default='none')
    p.add_argument('--integrations', type=int, default=2)
    p.add_argument('--multi-tenant', action='store_true')
    p.add_argument('--lifecycle', choices=['prototype','normal','long-lived'], default='long-lived')
    p.add_argument('--output')
    p.add_argument('--json', action='store_true', dest='as_json')
    args = p.parse_args()
    pressures, ranked = score_candidates(args)
    if args.as_json:
        result = json.dumps({'pressures': pressures, 'candidates': ranked}, indent=2)
    else:
        result = render(args)
    if args.output:
        Path(args.output).write_text(result + ('\n' if not result.endswith('\n') else ''), encoding='utf-8')
    else:
        print(result)

if __name__ == '__main__':
    main()
