# Multi-Agent Rehearsal Contract

This document defines the stable contract for the optional `v1A` multi-agent rehearsal mode. It specifies when the mode is invoked, what it requires, what it produces, and what it explicitly does not do.

## Invocation

Multi-agent rehearsal is **never the default**. It runs only when:

1. A Presentation Rehearsal Pack (or at minimum a first-pass/revised script) already exists.
2. The user explicitly requests a deeper rehearsal pass.

### User trigger phrases

Any of the following should activate multi-agent rehearsal mode:

- "Stress test this talk"
- "Run a skeptical review"
- "Simulate audience disagreement"
- "Give me a second-pass rehearsal round"
- "Intensify the critique"
- "What would a hostile audience ask?"
- "Deep rehearsal pass"

The Skill should recognize these as opt-in signals, not as requests to rewrite the core workflow.

## Input Prerequisites

The multi-agent mode requires all of the following:

1. **Existing Presentation Rehearsal Pack** or at minimum:
   - First-pass or revised script
   - Slide-by-slide mapping (or section mapping)
   - Presentation Brief (audience, duration, goals)
2. **Audience profile** — who will be in the room.
3. **Timing target** — the budget the speaker must hit.
4. **Optional but recommended:**
   - Original slide content or deck text;
   - Supporting materials (paper draft, notes);
   - Speaker's self-identified worries ("I am nervous about the methods section").

If the prerequisites are missing, the Skill must decline to run multi-agent rehearsal and instead prompt the user to complete the default `v0` pack first.

## Preflight Check (Warn, Do Not Block)

Before launching the three persona critiques, the Skill must evaluate the quality of the existing `v0` pack against the criteria in `references/critique-priority-rules.md`.

- **If the pack is already strong** (Strong on Groundedness, Defense Readiness, and Technical Precision; or 0 High + ≤2 Medium findings), the Skill must warn the user that v1A may add only minor polish.
- **The warning must be a suggestion, not a gate.** The user can override and proceed.
- **If the user overrides,** the Skill runs the full workflow and reports the result honestly, including an empty Revision Pass 2 if all critiques are dropped.

This preflight converts the diminishing-returns heuristic into an operational invocation boundary.

## Required Outputs

The multi-agent mode produces a `Rehearsal Intensification Output` that is **appended** to the existing pack. It contains:

1. **Persona-by-persona critique** — What each agent found, labeled by role.
2. **Disagreement map** — Where personas disagree on severity, importance, or fix strategy.
3. **Merged priority list** — Ranked issues after synthesis and deduplication.
4. **Revision Pass 2** — A revised script addressing only the ranked issues.
5. **Residual risks** — Issues that remain unresolved or are explicitly accepted as tradeoffs.

The original `Presentation Rehearsal Pack` must remain intact and referenceable.

## Strict Non-Goals

The multi-agent mode **must not**:

1. Run autonomously without a user trigger.
2. Run open-ended loops ("keep critiquing until no issues remain").
3. Rewrite slides, redesign visuals, or suggest new slide layouts.
4. Invent new facts or claims not present in the original materials.
5. Produce output if the prerequisites are missing.
6. Become the default path for new users.
7. Simulate more than three personas in `v1A`.

## Cost and Latency Warning

The Skill must warn the user that multi-agent rehearsal is:

- **More expensive** — it consumes significantly more tokens than the default single-agent pack.
- **Slower** — it requires multiple sequential critique passes plus a synthesis step.
- **Optional** — the default `v0` pack is often sufficient; this mode is for high-stakes talks or speakers who want extra confidence.

## Success Criterion

A successful multi-agent rehearsal is one where:

- The persona critiques are meaningfully different from each other (not three copies of the same critique).
- The synthesis step removes duplication without losing important nuance.
- Revision Pass 2 improves the script in at least one clearly observable way over the original revised script.
- The output remains fully grounded in the original materials.
