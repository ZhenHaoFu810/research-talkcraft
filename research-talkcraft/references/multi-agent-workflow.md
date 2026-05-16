# Multi-Agent Workflow

This document specifies the deterministic interaction pattern for the optional `v1A` multi-agent rehearsal mode. The workflow is bounded, sequential, and designed to prevent runaway loops.

## Overview

```
User Trigger -> Load Prerequisites -> Agent 1 Critique -> Agent 2 Critique -> Agent 3 Critique -> Synthesis -> Revision Pass 2 -> Output
```

There is **no feedback loop** from Revision Pass 2 back into the agents. `v1A` runs exactly one multi-agent round.

---

## Step 1: Validate Prerequisites

Before running any agent, confirm:

- [ ] A Presentation Rehearsal Pack exists (or at minimum a revised script + brief + timing target).
- [ ] Audience profile is available.
- [ ] The user has explicitly triggered multi-agent mode.

If any prerequisite is missing, decline and prompt the user to complete the default `v0` workflow first.

---

## Step 2: Agent 1 — Confused Listener Critique

**Input:** Revised script, Presentation Brief, slide/section mapping.
**Task:** Read the script once from the perspective of a non-expert listener. Mark clarity breakdowns, unexplained jargon, abrupt transitions, and missing motivation.
**Output:** A structured critique list with:
- Location (slide/section)
- Issue description
- Why it is confusing
- Suggested fix
- Severity estimate (High / Medium / Low)

**Constraint:** The Confused Listener must not critique technical precision or validity. Those belong to Agents 2 and 3.

---

## Step 3: Agent 2 — Domain Expert Critique

**Input:** Revised script, Presentation Brief, slide/section mapping, supporting materials (if any).
**Task:** Read the script from the perspective of a sub-field expert. Mark imprecise descriptions, unsupported novelty claims, missing related work, and under-explained method choices.
**Output:** Same structure as Agent 1.

**Constraint:** The Domain Expert must not critique clarity for non-experts or validity/identification concerns. Those belong to Agents 1 and 3.

---

## Step 4: Agent 3 — Skeptical Reviewer Critique

**Input:** Revised script, Presentation Brief, slide/section mapping, supporting materials, original `v0` Critique Summary and Likely Q&A.
**Task:** Read the script from the perspective of a rigorous reviewer. Mark overconfident claims, missing limitations, untested robustness concerns, and alternative explanations. Cross-check against the original `v0` Q&A to avoid duplication.
**Output:** Same structure as Agent 1, plus a note for each issue indicating whether it is new or already surfaced in the `v0` pack.

**Constraint:** The Skeptical Reviewer must not critique clarity or technical precision per se. Those belong to Agents 1 and 2.

---

## Step 5: Synthesis

**Input:** All three agent critique lists.
**Task:** Merge, deduplicate, rank, and resolve disagreements.

### 5.1 Deduplication Rules

- If two agents flag the same slide with the same core issue, merge them into one entry.
- Preserve the most severe severity rating.
- Combine the suggested fixes if they complement each other; keep the best one if they conflict.
- Attribute the merged entry to both agents (e.g., "Confused Listener + Domain Expert").

### 5.2 Disagreement Handling

- If Agent A rates an issue High and Agent B rates it Low, the synthesis step must decide based on the prioritization rules in `references/critique-priority-rules.md`.
- Groundedness and defense-readiness risks generally override clarity preferences.
- If agents disagree on the fix strategy, the synthesis step should present both options and recommend one with reasoning.

### 5.3 Low-Value Filtering

Drop critiques that meet any of these criteria:

- Pure stylistic preference with no grounding or clarity impact.
- Already fully addressed in the `v0` revised script.
- Contradicts the audience profile (e.g., complaining about missing basic definitions at an expert-only conference).
- Speculative with no connection to the actual materials.

### 5.4 Ranking

Produce a merged priority list sorted by:

1. **Severity:** High > Medium > Low.
2. **Category priority:** Groundedness / Defense Readiness > Clarity > Audience Fit > Timing.
3. **Consensus:** Issues flagged by multiple agents rank above single-agent issues at the same severity.
4. **Remediability:** Issues with clear fixes rank above vague concerns.

The merged list should contain no more than **12 items** for a 30-minute talk, **8 items** for a 15-minute talk, and **15 items** for a 45-minute talk. If the raw list is longer, the synthesis step must cut the lowest-priority items and note them as "deferred."

---

## Step 6: Revision Pass 2

**Input:** Original revised script + merged priority list.
**Task:** Produce a second-pass revised script that addresses only the ranked issues.

### Rules for Revision Pass 2

- Do not rewrite the entire script. Change only the segments tied to ranked issues.
- Mark each changed segment with a brief note: `[v1A: fixed clarity issue flagged by Confused Listener]`.
- If an issue cannot be fixed without destabilizing the script, mark it as a **residual risk** instead of forcing a bad fix.
- Preserve timing. If fixes would expand the script beyond budget, include `cut-for-time` alternatives for the changed segments.
- Do not invent new facts. All changes must be grounded in the original materials.

---

## Step 7: Output Assembly

Produce the `Rehearsal Intensification Output` containing:

1. **Persona Critiques** — Agent 1, Agent 2, Agent 3 critiques in full.
2. **Disagreement Map** — A short section listing the main disagreements and how they were resolved.
3. **Merged Priority List** — The ranked, deduplicated issues.
4. **Revision Pass 2** — The updated script with change annotations.
5. **Residual Risks** — Issues that remain unresolved or are accepted as tradeoffs.

Append this output to the existing Presentation Rehearsal Pack. Do not replace the original pack.

---

## Loop Boundaries

- **Maximum agent critique passes:** 3 (one per persona).
- **Maximum synthesis passes:** 1.
- **Maximum revision passes:** 1 (Revision Pass 2).
- **No recursion:** Revision Pass 2 is not fed back into the agents for another round.
- **No expansion:** The workflow cannot spawn additional agents or personas in `v1A`.

If the user wants another round after Revision Pass 2, they must trigger a new multi-agent rehearsal session explicitly. The Skill should warn that diminishing returns are likely.
