# Finance / Economics Exemplars

## Exemplar 1: Identification-Strategy Content

**Scenario:** Finance seminar  
**Domain:** Finance / Economics  
**Audience:** Finance PhD students and faculty  
**Overlay:** `finance-academic-talk`  
**Input material type:** Methods slide describing identification

### Slide content summary
- Title: "Identification"
- Bullets:
  - Difference-in-differences with firm fixed effects
  - Post-ChatGPT indicator interacted with treatment intensity
  - Parallel trends verified in pre-period

### Weak script
"We use a difference-in-differences design with firm fixed effects. The treatment is a post-ChatGPT indicator interacted with treatment intensity. We verify parallel trends in the pre-period."

### Critique
- Reads the method bullets without explaining why this design is credible.
- A finance audience will immediately ask: "Why should I believe your parallel trends assumption?"
- No mention of the comparison group or the economic mechanism.
- "Treatment intensity" is undefined.

### Improved script
"The core challenge is that firms didn't randomly adopt ChatGPT. So we use a difference-in-differences design: we compare firms that were already heavy users of disclosure-writing tools — our high-intensity group — to firms that were not, before and after ChatGPT launched in November 2022. The key identifying assumption is parallel trends: in the absence of ChatGPT, the high- and low-intensity groups would have followed similar trends. We test this by showing that the pre-period trends are statistically indistinguishable for five years before the launch. That gives us a credible counterfactual."

### Why the revision works
- States the identification strategy in one intuitive sentence.
- Names the comparison group explicitly.
- Explains the parallel trends assumption in plain language, not just "verified."
- Connects the method to the economic problem (non-random adoption).

---

## Exemplar 2: Economic-Magnitude Content

**Scenario:** Finance seminar  
**Domain:** Finance / Economics  
**Audience:** Finance PhD students and faculty  
**Overlay:** `finance-academic-talk`  
**Input material type:** Results slide with coefficient table

### Slide content summary
- Title: "Main results"
- Table: Coefficient on Post x Treatment = 0.042, t-stat = 3.87
- No economic interpretation provided

### Weak script
"The coefficient on the post-treatment interaction is 0.042 with a t-statistic of 3.87. It is statistically significant at the one percent level."

### Critique
- Reports a coefficient without interpreting it.
- A finance audience will ask: "0.042 of what? Is that large or small?"
- Statistical significance is not economic significance.
- No baseline for comparison.

### Improved script
"The point estimate is 0.042. That means that after ChatGPT launched, high-intensity firms increased their generative-AI usage score by 4.2 percentage points relative to low-intensity firms. To put that in context, the mean score in the pre-period was about 12 percent, so this is roughly a 35 percent increase over the baseline. That is not just statistically significant — it is economically meaningful. It suggests that the launch had a material effect on disclosure writing, not just a marginal blip."

### Why the revision works
- Translates the coefficient into an interpretable unit (percentage points).
- Provides a baseline comparison (35 percent increase).
- Distinguishes statistical from economic significance.
- Gives the audience a concrete takeaway.

---

## Exemplar 3: Causal-Language-Discipline Content

**Scenario:** Finance seminar  
**Domain:** Finance / Economics  
**Audience:** Finance PhD students and faculty  
**Overlay:** `finance-academic-talk`  
**Input material type:** Conclusion slide with causal claim

### Slide content summary
- Title: "Implications"
- Bullets:
  - ChatGPT adoption causes firms to write more positive MD&A
  - Regulators should require disclosure of AI use
  - Future research should study welfare effects

### Weak script
"Our results show that ChatGPT adoption causes firms to write more positive MD&A. Regulators should require disclosure of AI use. Future research should study welfare effects."

### Critique
- "Causes" is overstated. The design is DiD with firm fixed effects, not an RCT.
- Policy recommendation outruns the evidence.
- A skeptical reviewer will attack the causal language immediately.

### Improved script
"Our estimates are consistent with ChatGPT adoption leading to more positive language in MD&A. Under the parallel trends assumption, the DiD design supports a causal interpretation, though we cannot rule out all confounding from concurrent shocks. As for policy, our findings suggest that AI adoption in disclosures is already occurring at measurable rates. If regulators want to monitor this, validated detection tools could help — but we are not claiming that mandatory disclosure is costless or obviously welfare-improving. That is a question for future work."

### Why the revision works
- Replaces "causes" with "consistent with... leading to" and adds the assumption caveat.
- Softens the policy recommendation to a conditional suggestion.
- Frames the contribution precisely: descriptive evidence, not policy proof.
- Prepares the speaker for the inevitable causal-language challenge.
