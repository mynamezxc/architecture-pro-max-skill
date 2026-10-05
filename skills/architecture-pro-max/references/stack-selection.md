# Stack and language selection

Choose technologies only after product boundaries and quality attributes are clear. Prefer the team's proven ecosystem unless another stack has a material product advantage.

| Ecosystem | Strong fit | Multi-platform notes | Main cautions |
|---|---|---|---|
| TypeScript / JavaScript | web products, API/BFF, SaaS, realtime | React/Next + React Native + Tauri/Electron can share contracts/tooling | do not leak browser assumptions into native clients; runtime type safety needs schemas |
| C# / .NET | enterprise backend, Windows-heavy desktop, business systems | ASP.NET + WPF/WinUI/Avalonia/MAUI/Uno offers strong shared ecosystem | cross-platform UI choice needs careful maturity/UX evaluation |
| Java / Kotlin | enterprise backend, JVM ecosystems, Android | Spring/Ktor + Android/Compose; Compose Multiplatform can cover desktop and some shared UI | JVM desktop/web strategy may still require multiple UI stacks |
| Dart / Flutter | mobile-first and rich cross-platform clients | strong mobile + desktop sharing; web can work for app-like experiences | content-heavy/SEO/accessibility-sensitive web may favor web-native stack |
| Swift | iOS/macOS premium native experience | excellent Apple sharing via SwiftUI where suitable | not a general web/Windows strategy |
| Kotlin native/Compose | Android-centric and multiplatform client teams | shared logic and increasingly shared UI across mobile/desktop | ecosystem/platform gaps must be validated for target features |
| Go | services, gateways, CLI, networking, operational tools | pairs well with any client stack | not a mainstream rich-client UI choice |
| Rust | performance/safety-sensitive services, desktop core, systems | Tauri/native libraries can pair with web UI | learning curve and app-layer ecosystem smaller than TS/.NET/Java |
| Python | AI/data-heavy backends, automation, rapid service development | web API + native/web clients in other stacks; Qt for selected desktop tools | CPU-bound/high-concurrency paths may need different runtime strategy |
| C++ | low-latency/native/device/engine workloads | Qt and native UI possible across desktop | development complexity and memory-safety burden unless justified |

## Selection questions

1. Which ecosystem does the team already operate confidently?
2. Which client has the hardest native/platform requirements?
3. Is web a document/content surface or an app surface?
4. Does desktop require native filesystem, tray, background service, device or windowing integration?
5. Does mobile require deep background execution, Bluetooth, camera, push, secure storage or offline sync?
6. What must actually be shared: contracts, business rules, UI, or all three?
7. Which ecosystem gives the best debugging/testing/deployment path for the team?
8. What is the cost of hiring and long-term maintenance?

## Avoid stack monoculture by default

One language everywhere is useful only if it reduces total change cost. It is acceptable to use:

```text
web: TypeScript
mobile/desktop: Flutter
backend: Go or .NET
```

if boundaries and generated contracts keep integration reliable. Conversely, an all-TypeScript stack can be excellent when the product and team genuinely fit it.

## Stack decision output

When recommending technologies, include:
- primary recommendation;
- one credible alternative;
- strongest reason against the primary;
- what is shared vs platform-specific;
- dependency/runtime maturity risks;
- build/test/deploy implications;
- migration path if the choice proves wrong.
