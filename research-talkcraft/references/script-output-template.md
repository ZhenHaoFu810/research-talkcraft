# Presentation Rehearsal Pack — Output Template

This template defines the standard structure of the `Presentation Rehearsal Pack`. The Skill must produce every section below in order. If a section cannot be filled meaningfully, the Skill should explicitly state why rather than omitting the section.

---

## 1. Presentation Brief

A concise framing summary produced before the script. Include:
- **Talk purpose:** One-sentence statement of what the talk is trying to achieve.
- **Audience profile:** Knowledge level, likely background mix, and what they care about.
- **Core narrative arc:** The story the talk tells (e.g., "problem → approach → result → implication").
- **Communication risks:** The top 2–4 things most likely to confuse or lose the audience.
- **Recommended tone and depth:** e.g., "conversational but precise," "defensive because of skeptical reviewers," "high-level intuition over equations."
- **Operating mode:** `slides-only` or `slides+context`.
- **Uncertainty flags:** Any missing context that may limit script quality.

---

## 2. Slide-by-Slide Script (First Pass)

For each slide or section:
- **Slide identifier:** Slide number or section title.
- **Key content summary:** What the slide actually shows (1–2 sentences).
- **Suggested script:** The spoken narrative for this slide. Must explain, not read bullets. Should feel like natural speech, not written prose.
- **Approximate time:** Estimated delivery time for this segment.
- **Transition cue:** How to move to the next slide/section.

**Constraints:**
- Do not read bullets verbatim.
- Do not invent facts not present in the materials.
- Flag any slide where the content is too sparse to script confidently.

---

## 3. Confusion and Challenge Points

A structured list of likely audience friction points. For each:
- **Location:** Which slide/section it relates to.
- **What might confuse or be challenged:** The specific concept, claim, or transition.
- **Why it is risky:** Brief explanation of the knowledge gap or skeptical pressure.
- **Suggested mitigation:** How the speaker might preempt or address it.

---

## 4. Critique Summary

A concise evaluation of the first-pass script using the rubric dimensions. For each dimension (Groundedness, Clarity, Audience Fit, Non-Redundancy, Technical Precision, Narrative Flow, Timing Fit, Defense Readiness):
- **Score indicator:** Strong / Adequate / Weak (or a 1–5 scale).
- **Key finding:** The most important observation for this dimension.
- **Actionable fix:** What to change in the revised script.

Highlight the top 2–3 priority fixes.

---

## 5. Revised Script

The rehearsal-ready script, incorporating the critique. Structure it the same way as the first pass (slide-by-slide or section-by-section), but with improvements in:
- Clarity and pacing
- Audience alignment
- Transition smoothness
- Defense resilience
- Time discipline

Mark any segments where `cut-for-time` alternatives are available.

---

## 6. Likely Q&A

For each anticipated question:
- **Category:** Clarification, Motivation, Method, Validity, Limitation, Implication, or Hostile/Skeptical Challenge.
- **Likely question:** The question itself, phrased naturally.
- **Linked to:** Specific slide/claim/uncertainty point.
- **Strong answer outline:** Key points the speaker should hit.
- **Risky answer to avoid:** Common weak response patterns.

Keep Q&A grounded in the actual content. Do not generate generic debating language.

---

## 7. Time-Control Guidance

- **Total estimated time:** Sum of per-segment estimates.
- **Budget comparison:** If a target duration was given, show whether the script is over, under, or on target.
- **Section-level timing table:** When the v4A timing helper is used, include a table with:
  - Section label
  - Word count
  - Effective WPM (after complexity adjustment)
  - Estimated duration
  - Complexity flag (e.g., `DENSE` for sections with equations or heavy jargon)
- **Overrun segments:** Sections most likely to exceed their time budget.
- **Cut-for-time suggestions:** Concise alternatives for high-risk sections (e.g., "Cut the detailed derivation on slide 7; keep only the intuition and final formula").
- **Pacing tips:** Where to slow down (critical claims) and where to speed up (transitions, background).

If the timing helper is unavailable, produce the same sections using the 120–150 WPM heuristic. Do not omit Section 7.

---

## 8. Rehearsal Checklist

A short, actionable checklist the speaker can use when practicing:
- [ ] I can explain the core narrative in one sentence.
- [ ] I do not read any slide bullets verbatim.
- [ ] I have a clean transition between every pair of slides.
- [ ] I can answer the top 3 likely Q&A questions in under 60 seconds each.
- [ ] I know which sections to cut if I am running over time.
- [ ] I have a plan for the most likely confusion point.
- [ ] I have a plan for the most likely skeptical challenge.
- [ ] I have practiced the opening 60 seconds until it feels natural.
- [ ] I have flagged any claims I cannot fully defend and prepared a response.
- [ ] I have rehearsed with a timer at least once.

Add scenario-specific items from `references/scenario-playbooks.md` if relevant.

---

## Uncertainty and Missing-Context Warnings

Throughout the pack, the Skill should:
- Flag when a slide is too sparse for confident scripting.
- Flag when supporting materials contradict the deck.
- Flag when a critical piece of context (audience, duration, goal) was not provided.
- Avoid filling gaps with generic eloquence. State the gap and move on.

### Contradiction Report (slides+context mode)

When operating in `slides+context` mode, produce a structured Contradiction Report as part of the pack. This report is **omitted** if no contradictions are detected.

**For each detected contradiction, report:**

- **Contradiction ID:** A short identifier (e.g., C1, C2).
- **Class:** From `references/contradiction-taxonomy.md` (e.g., Temporal Mismatch, Claim-Strength Mismatch).
- **Severity:** High / Medium / Low.
- **Source locations:** Which slide(s) and which supporting material(s) contain the conflicting claims.
- **Conflicting claims:** Quoted or paraphrased, with enough context to be understandable.
- **Proposed reconciliation:** From `references/contradiction-reconciliation-rules.md`.
- **User warning:** A concise, explicit statement of what the speaker should do.

**Escalation for High-severity contradictions:**
- If severity is High, the script must **refuse to state the disputed claim** until the user resolves it.
- Replace the claim with an explicit uncertainty flag: "The deck and supporting material differ on [point]. Verify before presenting."

**Integration into other pack sections:**
- **Presentation Brief:** Summarize the number and highest severity of contradictions found.
- **Critique Summary:** Elevate Groundedness and Defense Readiness severity if contradictions remain unresolved.
- **Likely Q&A:** Generate questions that a skeptical audience might ask about the discrepancy.
- **Rehearsal Checklist:** Add "I have resolved or prepared for every High- and Medium-severity contradiction."

---

## Adaptation for Imperfect Slide Boundaries

If the input material is partially structured (e.g., pasted text without clear slide breaks):
- Group content into logical sections.
- Label them "Section 1: ..." instead of "Slide 1."
- Apply the same script, critique, and Q&A logic at the section level.

---

## Optional Appendix: Rehearsal Intensification Output (v1A)

If the user explicitly requests multi-agent rehearsal (e.g., "stress test this talk"), append the `Rehearsal Intensification Output` after Section 8. Follow `references/rehearsal-pass-2-template.md`. The original `Presentation Rehearsal Pack` must remain unchanged.
