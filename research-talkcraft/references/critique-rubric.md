# Critique Rubric

Use these eight dimensions to evaluate every draft script. For each dimension, identify the strongest observation and the most important actionable fix. Translate findings into concrete revision guidance.

---

## 1. Groundedness

**What it means:** Every claim in the script is traceable to the provided materials. The script does not hallucinate, invent data, or overstate what the slides or context support.

**Strong performance:**
- All numbers, citations, and findings match the input materials.
- Uncertainty is flagged rather than masked with confident language.
- The script acknowledges when a slide under-specifies a claim.

**Common failure:**
- The script states a result more strongly than the materials allow.
- A method is described with details that only appear in the paper, not the deck, without flagging the gap.
- The script invents a "future work" direction not mentioned anywhere.

**Revision guidance:**
- Replace unsupported claims with softer framing or explicit flags.
- Add grounding notes where the script goes beyond the deck in `slides-only` mode.
- In `slides+context` mode, if the script resolves a contradiction by preferring one source, annotate which source was chosen and why.

---

## 2. Clarity

**What it means:** The audience can follow the spoken narrative without re-reading the slide. Jargon is either avoided or explained. Sentence structure is suited to listening, not reading.

**Strong performance:**
- Complex ideas are introduced with intuition before detail.
- Technical terms are defined on first use.
- Sentences are short enough to be spoken in one breath.

**Common failure:**
- Dense, abstract sentences that would work in a paper but not in speech.
- Unexplained acronyms or field-specific shorthand.
- Bullet reading disguised as explanation.

**Revision guidance:**
- Break long sentences into spoken fragments.
- Add signposting language ("What this means is...", "The key idea here is...").
- Replace jargon with paraphrase or add a brief definition.

---

## 3. Audience Fit

**What it means:** The depth, tone, and framing match the target audience's knowledge level and interests. A seminar script differs from a lab-meeting script.

**Strong performance:**
- Background depth scales to the audience (more for mixed, less for experts).
- Motivation is framed in terms the audience cares about.
- Technical detail is present but not overwhelming.

**Common failure:**
- A seminar script assumes everyone knows the subfield's standard methods.
- A lab-meeting script over-explains basics the group already shares.
- A mixed-audience talk uses uncalibrated jargon without bridges.

**Revision guidance:**
- Add or remove background scaffolding based on the audience profile.
- Reframe motivation in audience-relevant terms.
- Use the scenario playbook to recalibrate depth.

---

## 4. Non-Redundancy

**What it means:** The script adds value beyond what is already visible on the slide. The speaker is not a human voice synthesizer for the deck.

**Strong performance:**
- The script explains the *why* and *so what* behind slide content.
- The script interprets figures and tables rather than describing them.
- Each slide's script has a distinct informational role.

**Common failure:**
- The script reads every bullet aloud with minor rewording.
- The script describes a figure that is already self-explanatory.
- The same point is repeated across consecutive slides without progression.

**Revision guidance:**
- Replace bullet reading with explanation, interpretation, or narrative bridge.
- Delete descriptions that add no information beyond the visual.
- Ensure each slide's script moves the story forward.

---

## 5. Technical Precision

**What it means:** The script is technically accurate where it needs to be, and does not oversimplify to the point of being misleading. It respects the audience's ability to handle precise claims.

**Strong performance:**
- Key assumptions and limitations are stated precisely.
- Causal language is used only where justified.
- Method descriptions are accurate to the actual approach.

**Common failure:**
- A method is described with a standard template that does not match what was actually done.
- A correlational result is framed causally.
- A limitation is omitted or glossed over.

**Revision guidance:**
- Audit causal language against the actual analysis.
- Add precise qualifiers where the script is too loose.
- Surface limitations that the speaker should acknowledge.

---

## 6. Narrative Flow

**What it means:** The talk feels like a coherent story, not a sequence of disconnected slides. Transitions are smooth and purposeful.

**Strong performance:**
- Each slide connects logically to the next.
- Transitions preview what is coming or summarize what was learned.
- The opening sets up the payoff; the closing ties back to the opening.

**Common failure:**
- Abrupt jumps between topics with no bridge.
- The opening states a problem but the closing never returns to it.
- Transitions are just "Next slide" or "Moving on."

**Revision guidance:**
- Add explicit transition sentences between sections.
- Recap the narrative arc at key milestones.
- Ensure the conclusion answers the question posed in the opening.

---

## 7. Timing Fit

**What it means:** The script respects the time budget. No section is disproportionately long, and there are clear cut points if time runs short.

**Strong performance:**
- Per-slide estimates sum to a plausible total.
- Complex sections are allocated more time; simple transitions, less.
- Cut-for-time alternatives are identified for high-risk sections.

**Common failure:**
- The script is clearly too long for the stated duration.
- A minor background slide gets as much time as the main result.
- No guidance is given for what to drop if the speaker runs over.

**Revision guidance:**
- Trim overlong explanations and redundant examples.
- Reallocate time toward high-priority claims.
- Add explicit "if short on time, cut X" notes.
- When the script is over budget, apply `references/revision-patterns.md` Pattern 8 (Timing Compression Under Pressure): compress background, collapse redundant transitions, keep the strongest example only, and move derivations to backup slides.
- Ensure cuts preserve the core claim and narrative arc; do not cut audience bridges or critical intuitions.

---

## 8. Defense Readiness

**What it means:** The script anticipates likely pushback and prepares the speaker to respond. It does not present weak claims with false confidence.

**Strong performance:**
- Key assumptions are acknowledged proactively.
- Limitations are framed as honest constraints, not hidden flaws.
- The script signals where the evidence is strong and where it is preliminary.

**Common failure:**
- A bold claim is made with no acknowledgment of its boundary conditions.
- A limitation is entirely absent from the narrative.
- The script sounds overconfident about results that are noisy or preliminary.

**Revision guidance:**
- Add proactive qualification language around risky claims.
- Surface the top 2–3 vulnerabilities in the Confusion and Challenge Points section.
- Adjust framing so the speaker can defend the claim without overstating it.
- In `slides+context` mode, unresolved contradictions between deck and supporting material are automatically treated as High-severity Defense Readiness risks.

---

---

## Overlay-Specific Critique Emphasis

When an overlay is active, the Skill should apply extra scrutiny to the dimensions most important in that setting. The base rubric still evaluates all eight dimensions, but the overlay elevates specific failure modes.

### Finance Academic Talk Overlay

Elevate these critiques:
- **Technical Precision:** Causal language audit. Every "leads to," "causes," or "increases" must be justified by the identification strategy.
- **Defense Readiness:** Economic magnitude reporting. A result without an interpretable magnitude is a Medium-severity issue.
- **Groundedness:** Generalization claims. Any claim that implies universal validity without sample boundaries is a High-severity issue.

### CS Group Meeting Overlay

Elevate these critiques:
- **Technical Precision:** Baseline specificity. "Better than baseline" without numbers or named baselines is a Medium-severity issue.
- **Audience Fit:** Background depth. Over-explaining standard concepts to an expert group is a Medium-severity issue.
- **Defense Readiness:** Reproducibility and ablation notes. Missing reproducibility information is a Medium-severity issue.

### Defense-Heavy Talk Overlay

Elevate these critiques:
- **Defense Readiness:** Scope discipline. Unclear contribution boundaries or missing methodological justifications are High-severity issues.
- **Groundedness:** Attribution accuracy. Misattributing coauthor work is a High-severity issue.
- **Clarity:** Cross-chapter consistency. Internal contradictions across chapters are High-severity issues.

When no overlay is active, the base rubric weights all dimensions equally, with the standard priority order: Groundedness > Defense Readiness > Clarity > Audience Fit > Timing.

## Turning Rubric Findings Into Actionable Revision Guidance

1. **Rank findings:** Not all weaknesses are equal. Prioritize failures in Groundedness, Defense Readiness, and Clarity over minor Timing Fit issues.
2. **Link to script locations:** Every critique point should reference a specific slide or section.
3. **Prescribe a revision pattern:** Match the weakness to a pattern in `references/revision-patterns.md` and apply it.
4. **Re-score after revision:** Briefly note whether the revised script resolves the finding or leaves residual risk.

## Chinese-Specific Critique Emphasis

When the talk is in Chinese, the Skill should apply extra scrutiny to dimensions that commonly fail in Chinese academic presentations. The base rubric still evaluates all eight dimensions, but Chinese-specific failure modes should be elevated.

### Elevated critiques for Chinese talks

- **Clarity:** Over-formality from written prose. Phrases like "本文"、"研究表明"、"具有重要的理论和实践意义" are standard in written papers but sound stiff in spoken Chinese. Treat excessive written-formal language as a Medium-severity issue.
- **Audience Fit:** Unnatural translated transitions. Transitions that literally translate English signposting ("Turning to the next point" → "转到下一点") without adapting to Chinese spoken rhythm are a Medium-severity issue.
- **Technical Precision:** Weak contribution framing with "填补了研究空白." Claims of filling a gap without specifying the gap, why it matters, or who cares are a Medium-severity issue. In defense settings, this is High-severity.
- **Defense Readiness:** Overclaiming with "首次" or "全新的理论框架." Claims that exceed what the evidence supports are treated as High-severity issues in Chinese defense contexts.
- **Narrative Flow:** Abrupt section-announcement transitions. "下面介绍研究方法" with no narrative bridge is a Low-to-Medium severity issue depending on frequency.

### Consult Chinese exemplars

For concrete illustrations of Chinese-specific weak and improved scripts, consult:
- `references/exemplars/chinese-academic.md`

---

## Exemplar References

For concrete illustrations of weak and improved scripts across domains and failure modes, consult the exemplar collection in `references/exemplars/`. Match rubric weaknesses to exemplar categories:
- Groundedness / Defense Readiness issues → `references/exemplars/failure-modes.md` (overclaiming, contradiction mishandling)
- Clarity / Audience Fit issues → `references/exemplars/mixed-background.md`, `seminar-style.md`, `chinese-academic.md`
- Technical Precision issues → `references/exemplars/finance-econ.md`, `neuroscience.md`
- Narrative Flow / Timing issues → `references/exemplars/failure-modes.md` (timing overrun, abrupt transitions)
