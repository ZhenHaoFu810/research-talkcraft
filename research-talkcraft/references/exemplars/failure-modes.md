# Failure-Mode Exemplars

These exemplars isolate common failure patterns and pair each with a clear revision. They map directly to the problems the system is designed to fix.

---

## Failure Mode 1: Bullet Reading

**Scenario:** Any research presentation  
**Domain:** Any  
**Audience:** Any  
**Input material type:** Slide with 3–4 bullets

### Slide content summary
- Title: "Key findings"
- Bullets:
  - Model A outperforms baseline
  - Robust to adversarial noise
  - Deployable on mobile devices

### Weak script
"Our key findings are: Model A outperforms the baseline. It is robust to adversarial noise. It is deployable on mobile devices."

### Critique
- Pure bullet reading. The audience can read faster than the speaker can speak.
- No interpretation, no pattern, no takeaway.
- Wastes rehearsal time.

### Improved script
"The short version is that Model A beats the baseline, survives adversarial attacks, and fits on a phone. Let me unpack that. First, on the standard benchmark, Model A improves accuracy by 8 points over the best prior method. Second, when we deliberately corrupt the input — adding noise that would fool most models — Model A drops only 3 points, while the baseline drops 15. That means it is not just accurate; it is reliable. Third, the whole model is under 10 megabytes, which is small enough to run on a mobile device in real time. So the pattern is: accuracy, robustness, and efficiency — together."

### Why the revision works
- Summarizes first, then expands.
- Adds specific numbers and comparisons.
- Connects the three bullets into a single pattern.

---

## Failure Mode 2: Overclaiming / Causal Overstatement

**Scenario:** Conference talk  
**Domain:** Economics / Policy  
**Audience:** Academic and policy researchers  
**Input material type:** Results slide with correlational finding

### Slide content summary
- Title: "Impact of early education"
- Bullets:
  - Early education increases earnings by 12%
  - Effects persist through age 30
  - Policy implication: expand preschool access

### Weak script
"Early education increases earnings by 12 percent. The effects persist through age 30. The policy implication is to expand preschool access."

### Critique
- "Increases earnings" implies causation, but the design is likely observational.
- Policy recommendation outruns the evidence.
- A skeptical reviewer will challenge the causal claim immediately.

### Improved script
"In our sample, children who attended early education programs have 12 percent higher earnings at age 30. That association is robust to controls for family income, parental education, and neighborhood quality, and it persists across multiple cohorts. The design is observational, so we cannot rule out all selection bias — for example, parents who enroll their children may differ in unobserved ways. Under the assumption that our controls capture the main sources of selection, the result is consistent with a causal effect. As for policy, the findings suggest that expanding preschool access could be beneficial, but the cost-effectiveness depends on program quality and targeting, which our data do not address."

### Why the revision works
- Replaces "increases" with "have higher earnings" and "association."
- States the identification assumption explicitly.
- Softens the policy claim to a conditional suggestion.

---

## Failure Mode 3: Missing Intuition

**Scenario:** Seminar  
**Domain:** Statistics / Machine Learning  
**Audience:** Mixed statisticians and domain scientists  
**Input material type:** Methods slide with dense technical content

### Slide content summary
- Title: "Variational inference"
- Bullets:
  - Approximate posterior with mean-field family
  - Optimize ELBO via stochastic gradient ascent
  - Convergence guaranteed under mild assumptions

### Weak script
"We approximate the posterior with a mean-field family. We optimize the ELBO via stochastic gradient ascent. Convergence is guaranteed under mild assumptions."

### Critique
- Three jargon terms in one sentence: mean-field, ELBO, stochastic gradient ascent.
- No intuition for what variational inference does or why it is needed.
- The domain scientists are lost immediately.

### Improved script
"The challenge is that the true posterior distribution — the full picture of what we know about the parameters — is too complex to compute exactly. Variational inference is a trick: instead of computing the true posterior, we approximate it with a simpler distribution — in our case, one where each parameter is independent. Think of it as sketching a detailed portrait with a simpler cartoon: it captures the main features without every brushstroke. We find the best cartoon by maximizing a quantity called the ELBO, which measures how close the cartoon is to the real thing. We do this with stochastic gradient ascent, which is just a fancy name for 'try a direction, check if it helps, repeat.' Under standard conditions, this process converges to the best approximation."

### Why the revision works
- Explains the problem first (posterior is too complex).
- Uses a visual analogy (cartoon vs. portrait).
- Explains ELBO in plain language.
- Defines stochastic gradient ascent intuitively.

---

## Failure Mode 4: Timing Overrun

**Scenario:** Conference talk (15-minute slot)  
**Domain:** Any  
**Audience:** Any  
**Input material type:** Background slide that consumes 90 seconds

### Slide content summary
- Title: "Literature review"
- Bullets:
  - Seminal work by Smith (2010)
  - Extension by Jones (2012)
  - Critique by Lee (2015)
  - Recent advances by Patel (2020)
  - Our work builds on Chen (2023)

### Weak script
"The literature begins with Smith in 2010, who introduced the foundational framework. Jones extended it in 2012 by adding a modular component. Lee critiqued the framework in 2015, arguing that it underestimated variance. Patel made recent advances in 2020 by applying the framework to a new domain. Our work builds on Chen in 2023, who provided the most recent implementation."

### Critique
- 90 seconds of background that most of the audience already knows.
- No clear link to the speaker's specific contribution.
- Risks overrunning before the main result is presented.

### Improved script
"The background here is well-known, so I'll just highlight the one paper that directly enables our work. Chen in 2023 provided an open-source implementation of the core framework, which we extend in two ways. If anyone wants the full literature trail, see the backup slide."

### Why the revision works
- Compresses 90 seconds into 20.
- Identifies the one paper that matters for this talk.
- Offers backup detail for those who want it.
- Respects the time budget.

---

## Failure Mode 5: Contradiction Mishandling

**Scenario:** Conference talk  
**Domain:** Any  
**Audience:** Any  
**Input material type:** Results slide that conflicts with supporting abstract

### Slide content summary
- Title: "Sample"
- Deck bullet: "Sample: 2015–2019"
- Supporting abstract: "Sample: 2015–2021"

### Weak script
"Our sample covers 2015 to 2021."

### Critique
- Silently prefers the abstract over the deck.
- Does not flag the discrepancy.
- A skeptical audience member who has the deck will notice the mismatch.

### Improved script
"The deck shows our original sample through 2019. The updated paper extends through 2021. I will present the full 2015-to-2021 results today, but note that the deck may be an earlier version."

### Why the revision works
- Acknowledges the discrepancy explicitly.
- States which version the speaker is presenting.
- Gives the audience a reason for the mismatch (version update).

---

## Failure Mode 6: Weak Contribution Framing

**Scenario:** Conference talk  
**Domain:** Any  
**Audience:** Any  
**Input material type:** Contribution slide

### Slide content summary
- Title: "Contributions"
- Bullets:
  - We improve the state of the art
  - Our method is more efficient
  - We provide new insights

### Weak script
"Our contributions are: we improve the state of the art, our method is more efficient, and we provide new insights."

### Critique
- Every claim is vague.
- "Improve the state of the art" — by how much, on what benchmark?
- "More efficient" — in time, memory, energy?
- "New insights" — what exactly?

### Improved script
"Our first contribution is a training algorithm that scales to 10,000 GPUs without losing convergence guarantees — the largest prior system we are aware of topped out at 2,000. Second, the algorithm uses 30 percent less memory per GPU than the standard data-parallel baseline, which means you can train larger models on the same hardware. Third, we show that the convergence rate depends on the communication topology in a way that was not previously understood: ring topologies work better than tree topologies for large batches. So the contribution is not just scale, but a new understanding of why scale works."

### Why the revision works
- Every claim has a concrete number or comparison.
- Efficiency is defined (memory, 30 percent).
- The "insight" is specific (ring vs. tree topology).
- The speaker can defend every bullet under challenge.
