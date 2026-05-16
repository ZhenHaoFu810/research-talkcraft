# Group-Meeting Exemplars

## Exemplar 1: Honest Status Update

**Scenario:** CS group meeting  
**Domain:** Computer Science / NLP  
**Audience:** Lab members (advisor, senior PhDs, first-year students)  
**Overlay:** `cs-group-meeting`  
**Input material type:** Status update slide

### Slide content summary
- Title: "This week's progress"
- Bullets:
  - Tried 3 fine-tuning strategies
  - Best result: 74.2 F1 on dev set
  - Still 5 points behind SOTA

### Weak script
"This week I tried three fine-tuning strategies. The best result is 74.2 F1 on the dev set. We are still 5 points behind SOTA."

### Critique
- Reports results without explaining what was tried or why.
- No analysis of why the gap persists.
- No clear ask for feedback.
- Sounds like a status report, not a collaborative discussion.

### Improved script
"This week I tested three fine-tuning strategies: full fine-tuning, LoRA with rank 16, and prefix tuning. Full fine-tuning overfit after epoch 3 — the dev F1 peaked at 74.2 and then dropped to 71. LoRA was more stable but plateaued at 72. Prefix tuning was worse, around 69. The problem seems to be that the pre-training distribution is far from our target domain, so lightweight adapters don't have enough capacity. The 5-point gap to SOTA is probably because SOTA uses task-specific pre-training on 10 million additional examples, which we don't have. The place where I need input is: should I invest in data augmentation, or should I try a larger base model even though it is slower?"

### Why the revision works
- Names the specific strategies and their outcomes.
- Diagnoses the failure (distribution mismatch, adapter capacity).
- Explains the gap to SOTA with a concrete hypothesis.
- Ends with a clear, specific ask.

---

## Exemplar 2: Negative Results

**Scenario:** Biology lab meeting  
**Domain:** Molecular Biology  
**Audience:** Lab members with shared methods expertise  
**Input material type:** Results slide showing null effect

### Slide content summary
- Title: "Knockdown results"
- Figure: Western blot showing no change in target protein after siRNA treatment
- Statistic: p = 0.42

### Weak script
"The knockdown experiment did not work. There was no change in the target protein. The p-value is 0.42. We are troubleshooting."

### Critique
- "Did not work" is vague and sounds like an excuse.
- No hypothesis for why the knockdown failed.
- No next steps.
- Hides the negative result behind vague language.

### Improved script
"The siRNA knockdown did not reduce target protein levels — the Western blot shows no visible band reduction, and the quantification is not significant, p equals 0.42. My hypothesis is that the protein turnover is too slow for the 48-hour treatment window. The half-life is estimated at 72 hours, so we may need a longer knockdown or a CRISPR approach instead. I also checked the transfection efficiency, and it was 85 percent, so delivery is not the issue. The next step I am considering is extending the treatment to 96 hours or switching to a CRISPRi line. Does anyone have experience with slow-turnover proteins?"

### Why the revision works
- States the null result clearly without apologizing.
- Proposes a mechanistic explanation (slow turnover).
- Rules out an alternative explanation (transfection efficiency).
- Ends with a specific next-step proposal and a request for expertise.
