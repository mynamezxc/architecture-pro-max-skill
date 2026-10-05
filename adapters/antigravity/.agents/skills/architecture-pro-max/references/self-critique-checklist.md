# Architecture self-critique checklist

Use this before finalizing a recommendation.

## Complexity challenge

- Can one deployable process satisfy the current requirements?
- Can module boundaries solve the problem before network boundaries?
- Are CQRS/events introduced for a measurable read/write or integration need?
- Are interfaces wrapping volatile boundaries or merely every class?
- Is a second database/store justified by access patterns or just preference?

## Multi-platform challenge

- Can one requested app be replaced by responsive web/PWA?
- Is shared UI lowering accessibility/native UX?
- Are shared packages runtime-neutral?
- Is the chosen desktop technology justified by native capabilities?
- Does offline mode define actual write/sync/conflict semantics?

## Data challenge

- Who owns each table/entity?
- Which operations truly require strong transactions?
- Are async events being used for synchronous business dependencies?
- Are migration and backward compatibility addressed?
- Are seeds, fixtures and production bootstrap accidentally mixed?

## Operations challenge

- Can the team debug this system at 2 AM?
- Does every distributed component have logs/metrics/traces/health/ownership?
- Are retries bounded and idempotent?
- What happens when each external dependency is slow or unavailable?
- Is rollback feasible?

## Change-cost challenge

- What are the three most likely future changes?
- Which files/modules would each change touch?
- Does the architecture localize those changes?
- Is there a simpler design with nearly the same future flexibility?

## Evidence challenge

- Which requirement drove each major pattern?
- Which decision is based only on speculation?
- What measurable threshold triggers extraction or redesign?

## Final response requirement

Include:

1. strongest argument **against** the recommendation;
2. simpler fallback;
3. conditions where an alternative becomes better;
4. biggest operational risk;
5. biggest maintainability risk;
6. next architecture review trigger.
