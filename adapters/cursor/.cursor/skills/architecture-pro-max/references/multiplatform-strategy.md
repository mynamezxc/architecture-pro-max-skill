# Multi-platform strategy

## Goal

Minimize **total change cost** across web, mobile and desktop while preserving platform UX, accessibility, performance and native integration.

## First question: do all clients need to exist?

Challenge the requirement before designing three applications.

- Can responsive web/PWA satisfy desktop?
- Is a mobile wrapper enough or is offline/native integration real?
- Does desktop need filesystem, tray, global shortcuts, local DB, background services or device access?
- Are users internal or public? App-store distribution may add cost.

## Sharing layers

### Usually safe to share

- API schemas and generated clients;
- protocol/event definitions;
- domain value types and pure business formulas;
- validation rules with identical semantics;
- localization resources where platform format permits;
- design tokens (color/spacing/type scales), not necessarily widgets;
- test fixtures and scenario definitions;
- feature flags and capability IDs.

### Share only with evidence

- state management libraries;
- storage abstractions;
- auth/session helpers;
- telemetry wrappers;
- navigation abstractions;
- form engines.

### Usually platform-specific

- app lifecycle/navigation shell;
- accessibility semantics;
- keyboard/mouse/window behavior;
- push notifications and background execution;
- platform permissions;
- platform-native widgets where UX differs.

## Common implementation strategies

### Web + React Native + Tauri/Electron

Best when:
- TypeScript/React team is strong;
- web product is important;
- mobile can use React Native UX;
- desktop mostly needs a web UI with selected native capabilities.

Strength: shared contracts/tooling and some UI logic.
Risk: forcing DOM assumptions into native apps; Electron memory footprint if desktop is heavy.

### Web + Flutter mobile/desktop

Best when:
- mobile and desktop need a consistent rich client;
- Dart/Flutter team capability exists;
- web remains content/admin heavy and can use a web-native stack.

Strength: strong mobile/desktop sharing.
Risk: two major frontend ecosystems.

### Flutter everywhere

Best when:
- app-like UI dominates all clients;
- SEO/document semantics are unimportant;
- one rendering model is valued.

Risk: web accessibility/content integration and bundle/runtime characteristics may be inferior for web-heavy products.

### Native per platform

Best when:
- deep OS integrations, performance or accessibility dominate;
- teams can own multiple stacks.

Risk: duplicated implementation and coordination cost.

### PWA first

Best when:
- native requirements are weak;
- fastest distribution and shared UI matter.

Risk: background tasks, device APIs and platform integration may be constrained.

## Contract strategy

Prefer one canonical schema:

```text
API schema / event schema
        ↓
Generated clients / codecs
   ┌────┼─────┐
 Web Mobile Desktop
```

Avoid hand-maintaining three incompatible API models.

## Offline model

If offline is required, define states explicitly:

```text
local-only
pending-sync
synced
conflict
failed
```

Decide conflict policy per entity:
- server wins;
- client wins;
- last-write-wins with clock rules;
- field-level merge;
- domain-specific manual resolution.

Do not call a client “offline-first” if it only caches GET responses.

## Cross-platform testing

Define business scenarios once, then bind platform drivers:

```text
Scenario: create lead → qualify → convert to opportunity
  web driver
  mobile driver
  desktop driver
```

Contract and fixture data should be shared; interaction tests remain platform-aware.
