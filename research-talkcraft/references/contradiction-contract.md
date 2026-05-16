# Contradiction Contract

This document defines the stable contract for contradiction detection and reconciliation in `slides+context` mode. It specifies what counts as a contradiction, what inputs are inspected, what outputs are produced, and what the layer explicitly does not do.

## What Counts As A Contradiction

A contradiction is a **material discrepancy** between the slide deck and supporting materials that could mislead the speaker or the audience if unresolved. The discrepancy must be about a factual claim, not merely a difference in detail level or framing.

### Contradiction criteria (all three must hold)

1. **Both sources make an explicit or strongly implicit claim about the same entity.**
   - Example: Both the deck and the abstract state the sample period.
   - Non-example: The deck mentions GPTZero; the abstract never names the detector. This is a gap, not a contradiction.

2. **The claims cannot both be true simultaneously.**
   - Example: The deck says 2010–2023; the abstract says through 2024.
   - Non-example: The deck says "validated on five hundred firms"; the abstract says "validated on a large sample." These are compatible.

3. **The discrepancy matters for rehearsal quality.**
   - Example: A temporal mismatch changes what the speaker should say about sample coverage.
   - Non-example: The deck uses "ten-K" and the abstract uses "10-K." Typographic variants are not contradictions.

### What is NOT a contradiction

| Phenomenon | Why it is not a contradiction | How to handle |
|-----------|------------------------------|---------------|
| **Version drift** | The deck is an older version; the abstract is newer. Both were true at their time of writing. | Flag as version drift, note which source is newer, and let the user choose. |
| **Extra supporting detail** | The abstract contains information the deck omits but does not conflict with. | Surface as supplementary context, not a contradiction. |
| **Presentational compression** | The deck simplifies a complex claim for slide brevity. | Expected and acceptable unless the compression changes the factual meaning. |
| **Typographic or naming variation** | Different abbreviations, date formats, or citation styles. | Ignore. |
| **Scope narrowing** | The deck focuses on one analysis while the abstract mentions a broader project. | Acceptable unless the deck contradicts the broader claim. |

## Inputs Inspected

The contradiction layer may inspect:

1. **Slide text or extracted slide summaries** — the primary rehearsal anchor.
2. **Abstract** — highest-priority supporting material for framing and contribution claims.
3. **Paper draft or extended summary** — for method details, results, and limitations.
4. **Speaker notes or outline** — for intended emphasis.
5. **Previous rehearsal pack** — if one exists, to detect whether a prior contradiction was already resolved.

The layer does **not** inspect:
- External databases or search results.
- Invented or inferred facts not present in the materials.

## Required Outputs

For every detected contradiction, the layer must produce:

1. **Contradiction class** — from the taxonomy in `references/contradiction-taxonomy.md`.
2. **Severity** — High, Medium, or Low.
3. **Source locations** — Which slide and which supporting material contain the conflicting claims.
4. **Conflicting claims** — Quoted or paraphrased, with enough context to be understandable.
5. **Proposed reconciliation** — From `references/contradiction-reconciliation-rules.md`.
6. **User-facing warning** — Explicit, concise, and non-speculative.

## Strict Non-Goals

The contradiction layer **must not**:

1. **Silently blend sources.** Do not merge slide and abstract claims into a single sentence without flagging the merge.
2. **Invent facts to resolve gaps.** If the deck says X and the abstract says Y, do not invent Z that makes both true.
3. **Automatically correct slides.** The layer critiques and warns; it does not redesign or rewrite slide content.
4. **Run in `slides-only` mode.** Without supporting materials, there is nothing to contradict.
5. **Treat every difference as a contradiction.** Use the criteria above to filter benign differences.
6. **Override user resolution without permission.** If the user explicitly states which source to trust, follow that instruction.
