# Overlay Contract

This document defines what an overlay is, when it is selected, what it may change, and what it must preserve.

## What An Overlay Is

An overlay is a **calibration layer** that sits on top of the base `v0` general-research workflow. It does not replace the workflow; it sharpens audience assumptions, tone, likely challenges, and revision priorities for a specific discipline or presentation setting.

Overlays are **optional**. The base general-research mode works correctly without any overlay.

## When An Overlay Is Selected

An overlay is activated when either:

1. **The user explicitly requests it** using trigger language such as:
   - "This is a finance seminar"
   - "Treat this like a CS group meeting"
   - "Prepare me for a defense-style audience"
   - "Apply the finance overlay"
   - "Job-market talk format"

2. **The Skill infers it with high confidence** from the materials or user context, **and proposes it for confirmation.** The user must explicitly accept the proposed overlay before it is applied.

### High-confidence inference signals

- The user mentions a specific field or venue ("presenting at the AFA", "MIT theory reading group", "dissertation defense").
- The deck content contains strong field-specific cues (econometric notation, algorithm pseudocode, committee slide).
- The audience profile specifies a homogeneous expert group from a single discipline.

If inference is uncertain, the Skill **must not** silently apply an overlay. It should either:
- Ask the user directly: "This looks like a finance seminar. Should I apply the finance-academic overlay?"
- Or default to the base general-research mode.

## What Overlays Are Allowed To Change

Overlays may adjust the following dimensions:

1. **Audience assumptions** — What the audience already knows, what jargon is safe, what background is unnecessary.
2. **Tone guidance** — How formal, how aggressive, how collaborative the script should feel.
3. **Depth calibration** — Which sections deserve more technical depth and which should stay high-level.
4. **Likely challenge patterns** — What kinds of pushback are common in this setting.
5. **Q&A emphasis** — Which Q&A categories are most important and what strong answers look like in this context.
6. **Revision priorities** — Which critique dimensions get extra weight during revision.

## What Overlays Are NOT Allowed To Change

Overlays **must not**:

1. Change the core pack structure or required sections.
2. Relax grounding rules or permit hallucination.
3. Replace the single-agent default path with a mandatory multi-agent path.
4. Override the v1A contract or preflight check.
5. Introduce slide editing or redesign.
6. Demand field-specific facts or citations that are not in the provided materials.

## Fallback Behavior

If an overlay is requested but the inference is uncertain, or if the user declines a proposed overlay:

- **Fall back to the base general-research mode.**
- Use the scenario playbooks in `references/scenario-playbooks.md` for tone and depth.
- Do not apologize or over-explain the fallback. Simply proceed with the standard workflow.

If the user requests an overlay that does not exist:
- State that the overlay is not yet available.
- Offer the closest available overlay or the base general-research mode.
- Do not invent an overlay on the fly.

## Overlay File Structure

Every overlay file must contain these sections:

1. **Audience profile** — Who is in the room and what they know.
2. **Assumed knowledge** — What the speaker can take for granted.
3. **Likely challenges** — Typical pushback patterns for this setting.
4. **Overclaiming definitions** — What counts as overstated in this field.
5. **Pacing and tone** — Speed, formality, and emotional register.
6. **Common failure modes** — Mistakes speakers make in this setting.
7. **Proactive defense requirements** — What the speaker must address before being asked.

Overlay files should be short (under 300 lines) and operational. They should not duplicate the full base playbook.
