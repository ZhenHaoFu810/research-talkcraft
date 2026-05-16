# Critique Priority Rules

This document defines how the `v1A` synthesis step ranks, filters, and resolves conflicts between persona critiques.

## Severity Levels

Every critique finding must be assigned one of three severity levels:

| Level | Definition | Typical Impact |
|-------|-----------|----------------|
| **High** | Undermines the credibility of the talk or causes significant audience loss. | Must be fixed in Revision Pass 2. |
| **Medium** | Causes friction, confusion, or defensibility risk for a subset of the audience. | Should be fixed if time and script stability allow. |
| **Low** | A nit, preference, or minor improvement that does not materially affect rehearsal quality. | Fix only if easy; otherwise defer or accept as residual risk. |

---

## Category Priority Order

When two issues have the same severity, rank them by category:

1. **Groundedness** — Risk of hallucination, unsupported claims, or factual error.
2. **Defense Readiness** — Risk that the speaker cannot defend a claim under challenge.
3. **Clarity** — Risk that part of the audience will not understand.
4. **Audience Fit** — Risk that depth or tone is mismatched.
5. **Timing** — Risk that the script exceeds the budget.

**Rule:** A Medium-severity Groundedness issue outranks a High-severity Timing issue. Factual integrity comes before pacing.

---

## Preflight Check: When to Warn Against v1A

Before running multi-agent rehearsal, the Skill must assess whether the existing `v0` pack is already high-quality enough that v1A is likely to produce only low-value output.

### Warning criteria (any one triggers a warning)

1. The `v0` Critique Summary scores **Strong** on Groundedness, Defense Readiness, and Technical Precision.
2. The `v0` Critique Summary contains **0 High-severity findings** and **2 or fewer Medium-severity findings**.
3. The revised script already contains **proactive caveats** for every major claim, with no causal overstatement and no upward-biased marketing language.

### Warning language

If any criterion is met, present exactly:

> "Your default pack is already strong on groundedness, defense-readiness, and technical precision. Multi-agent rehearsal may add only minor polish or stylistic preferences. Do you still want to proceed?"

### User override

The warning must **not** block execution. The user can proceed anyway. If they do, the Skill runs the normal v1A workflow and documents the result honestly (including an empty Revision Pass 2 if that is what occurs).

---

## When to Drop a Critique as Low-Value

Drop a critique if it meets any of these criteria:

1. **Pure stylistic preference** with no clarity, precision, or defensibility impact.
   - Example: "I would have used 'demonstrate' instead of 'show.'"
2. **Already fully addressed** in the `v0` revised script.
   - Example: The Skeptical Reviewer flags a limitation that the `v0` script already acknowledges proactively.
3. **Contradicts the audience profile.**
   - Example: The Confused Listener demands a definition of "OLS" at a methods workshop where everyone knows OLS.
4. **Speculative with no material connection.**
   - Example: "What if the results are completely driven by unobserved macro shocks?" when the paper already uses firm fixed effects and time trends.
5. **Demands scope expansion.**
   - Example: "The speaker should also discuss the macro implications" when the talk is explicitly a micro study.

---

## When One Persona's Concern Overrides Another

### Confused Listener vs. Domain Expert

- If the Confused Listener wants more intuition and the Domain Expert wants more precision, **the synthesis step should favor intuition for mixed-audience talks and precision for expert-only talks.**
- If the talk audience is mixed, the default resolution is: add a brief intuition clause and defer deep precision to a backup slide or Q&A.

### Skeptical Reviewer vs. Confused Listener

- The Skeptical Reviewer's groundedness and defense-readiness concerns generally override the Confused Listener's clarity preferences.
- Exception: If the Skeptical Reviewer's fix would make the script incomprehensible to 80% of the audience, the synthesis step should find a compromise (e.g., simplify the defense language without omitting the defense).

### Domain Expert vs. Skeptical Reviewer

- If the Domain Expert wants more technical detail and the Skeptical Reviewer wants a limitation acknowledged, **the Skeptical Reviewer's concern usually wins** because missing limitations are more dangerous to the speaker than missing detail.
- Exception: If the technical detail is necessary to understand the limitation, the Domain Expert's concern takes precedence.

---

## Examples: Real Issue vs. Stylistic Preference vs. False Positive

### Real Issue

- **Confused Listener:** "The script jumps from the detection method to the results without explaining how the sample was constructed. I would not know what data I am looking at."
  - *Why real:* This is a clarity gap that breaks narrative flow and undermines result credibility.
  - *Action:* Fix in Revision Pass 2.

- **Domain Expert:** "The script calls the estimator 'novel' but it is a standard LASSO with a different loss function. This overstates contribution."
  - *Why real:* This is a groundedness and defense-readiness risk.
  - *Action:* Fix in Revision Pass 2.

- **Skeptical Reviewer:** "The script claims causal effects but the design is a simple pre-post comparison with no control group."
  - *Why real:* This is a severe defense-readiness risk.
  - *Action:* Fix immediately. Replace causal language with descriptive language or add a strong caveat.

### Stylistic Preference

- **Any agent:** "The opening would be stronger with a question rather than a statement."
  - *Why preference:* This may be true, but it is not grounded in any material deficiency. Either option can work.
  - *Action:* Drop or note as optional suggestion.

- **Domain Expert:** "I prefer tables to figures for this result."
  - *Why preference:* This is about slide design, not script quality.
  - *Action:* Drop. Out of scope for `research-talkcraft`.

### False Positive

- **Confused Listener:** "The script does not explain what a p-value is."
  - *Why false:* The audience profile specifies statistics PhD students. This is expected knowledge.
  - *Action:* Drop.

- **Skeptical Reviewer:** "The speaker does not discuss the Lucas critique."
  - *Why false:* The talk is about a micro panel-data design where the Lucas critique is irrelevant. The critique is not grounded in the actual materials.
  - *Action:* Drop.

- **Domain Expert:** "The script should cite Paper X."
  - *Why false:* Paper X was published after the talk was written. The agent invented a relevance that does not exist in the materials.
  - *Action:* Drop.

---

## Consensus Bonus

An issue flagged by **two or more agents** at severity Medium or higher receives a "consensus bonus" in ranking: it is treated as one severity level higher for prioritization purposes.

- Example: A Medium-severity issue flagged by both the Confused Listener and the Skeptical Reviewer is treated as High for ranking.
- This reflects the principle that cross-persona agreement indicates a robust problem, not just one perspective's bias.

## Maximum List Length

To prevent overwhelm, the merged priority list must respect these caps:

| Talk Duration | Max Items |
|---------------|-----------|
| 10 minutes | 5 |
| 15 minutes | 8 |
| 20 minutes | 10 |
| 30 minutes | 12 |
| 45 minutes | 15 |

If the raw list exceeds the cap, cut from the bottom (lowest severity, lowest category priority) and list the cut items as "deferred" in the Residual Risks section.
