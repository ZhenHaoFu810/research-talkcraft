# Rehearsal Intensification Output — Template

This template defines the optional output produced by the `v1A` multi-agent rehearsal mode. It is **appended** to the existing `Presentation Rehearsal Pack`, not a replacement.

---

## 1. Persona Critiques

For each agent role, produce a structured critique list.

### 1.1 Confused Listener Critique

For each finding:
- **Location:** Slide/section number.
- **Issue:** What is confusing or unexplained.
- **Why it matters:** Brief explanation of the knowledge gap.
- **Suggested fix:** Concrete change to the script.
- **Severity:** High / Medium / Low.

**Example:**
- Location: Slide 7
- Issue: The term "entropy balancing" is used without definition.
- Why it matters: Most accounting researchers have not encountered this method.
- Suggested fix: Add a one-sentence intuition before using the term: "Entropy balancing reweights the control group to match the treatment group on observed characteristics, similar to propensity score matching but without requiring a propensity model."
- Severity: Medium

### 1.2 Domain Expert Critique

Same structure as above.

**Example:**
- Location: Slide 12
- Issue: The detector is described as "based on perplexity and burstiness" but the script does not explain how these features are combined into the GenScore.
- Why it matters: An NLP expert will want to know whether this is a simple logistic regression or a more complex ensemble.
- Suggested fix: Add a brief clause: "GPTZero combines perplexity and burstiness into a single probability using a proprietary classifier."
- Severity: Low

### 1.3 Skeptical Reviewer Critique

Same structure as above, plus:
- **Already in v0 Q&A?** Yes / No. If Yes, reference the original Q&A entry.

**Example:**
- Location: Slide 29
- Issue: The script says "significant post-ChatGPT increase" but does not acknowledge that the break could reflect a secular trend in writing style rather than GAI adoption.
- Why it matters: A reviewer will immediately raise this alternative explanation.
- Suggested fix: Add a proactive sentence: "We address the secular-trend concern with firm fixed effects, linear trend controls, and cross-sectional heterogeneity."
- Severity: High
- Already in v0 Q&A? No

---

## 2. Disagreement Map

List the main disagreements between agents and how the synthesis step resolved them.

For each disagreement:
- **Topic:** What the agents disagreed about.
- **Agent positions:** What each agent argued.
- **Resolution:** How the synthesis step decided, with reasoning.
- **Impact on Revision Pass 2:** Whether the disagreement led to a change, a compromise, or a deferred decision.

**Example:**
- Topic: Whether the opening 60 seconds spend too long on the Goldman Sachs quote.
- Agent positions:
  - Confused Listener: High severity — the quote is attention-grabbing but does not explain what the paper does.
  - Domain Expert: Low severity — the quote is fine for a general audience; experts can wait 20 seconds.
- Resolution: Compromise. Keep the quote but trim it from 25 seconds to 15 seconds, and add a one-sentence bridge to the research question.
- Impact: Script trimmed; no structural change.

---

## 3. Merged Priority List

A single ranked list of all deduplicated issues.

For each issue:
- **Rank:** 1, 2, 3, ...
- **Location:** Slide/section.
- **Issue summary:** One-sentence description.
- **Source agents:** Which agents flagged it.
- **Severity:** High / Medium / Low.
- **Category:** Groundedness / Defense Readiness / Clarity / Audience Fit / Timing.
- **Action for Revision Pass 2:** Fix / Partial fix / Defer / Accept as residual risk.

The list should be ordered by severity and category priority (Groundedness / Defense Readiness > Clarity > Audience Fit > Timing).

**Example:**
| Rank | Location | Issue Summary | Source Agents | Severity | Category | Action |
|------|----------|---------------|---------------|----------|----------|--------|
| 1 | Slide 29 | Missing secular-trend acknowledgment | Skeptical Reviewer | High | Defense Readiness | Fix |
| 2 | Slide 11 | Temporal discrepancy (2023 vs 2024) | Skeptical Reviewer | High | Groundedness | Fix |
| 3 | Slide 7 | "Entropy balancing" undefined | Confused Listener | Medium | Clarity | Fix |
| 4 | Slide 12 | GenScore combination unexplained | Domain Expert | Low | Audience Fit | Defer |

---

## 4. Revision Pass 2

The updated script, with changes annotated.

### Annotation Format

For each changed segment, add a brief inline note:

```
[v1A: fixed <issue> flagged by <agent>]
```

Or, if the change is subtle, append a short endnote:

```
Segment: Slide 29, second paragraph
Change: Added proactive acknowledgment of secular-trend concern.
Reason: Skeptical Reviewer flagged missing defense (Rank 1).
```

### Scope Rules

- Change only the segments tied to the Merged Priority List.
- Do not rewrite unaffected sections.
- Preserve the original script's structure and flow.
- If a fix would cause timing overrun, provide a `cut-for-time` alternative.

---

## 5. Residual Risks

Issues that were not fixed in Revision Pass 2, with explanation.

For each residual risk:
- **Location:** Slide/section.
- **Issue:** What remains unresolved.
- **Why it was not fixed:** Honest explanation (e.g., "fix would require adding a new slide," "fix would exceed time budget," "issue is acknowledged but accepted as a limitation").
- **Speaker guidance:** What to say if the issue comes up in Q&A.

**Example:**
- Location: Slide 12
- Issue: GenScore combination details remain unexplained.
- Why it was not fixed: The fix would add technical detail that most of the audience does not need. The Domain Expert's concern is valid but niche.
- Speaker guidance: If asked, say: "GPTZero uses a proprietary classifier. We validated its performance for financial text, which is what matters for our application."

---

## Appending to the Original Pack

The `Rehearsal Intensification Output` should be appended after the original `Rehearsal Checklist` (Section 8 of the `Presentation Rehearsal Pack`). Include a clear header:

```
---

# Optional Appendix: Rehearsal Intensification Output (v1A)

This section was produced by multi-agent rehearsal mode. It is optional and can be ignored if the default rehearsal pack is sufficient.
```

This ensures the original pack remains intact and the intensification output is clearly demarcated.
