# Overlay: Finance Academic Talk

## Audience Profile

- **Primary:** Finance PhD students and faculty, plus economists from adjacent fields (accounting, economics, marketing-quant).
- **Mixedness:** Usually homogeneous in methodological training, but may span corporate finance, asset pricing, and fintech subfields.
- **Motivation:** Evaluating whether the work is publishable, whether the identification is credible, and whether the magnitudes matter.

## Assumed Knowledge

The speaker can safely assume the audience knows:
- Standard econometric methods: OLS, fixed effects, IV, diff-in-diff, regression discontinuity.
- Core finance concepts: CAPM, EMH, agency theory, information asymmetry.
- Standard databases: CRSP, Compustat, WRDS.
- The difference between correlation and causation.

**Do not over-explain:** OLS, fixed effects, or what CRSP is.
**Do explain:** Novel measures, custom pipelines, or non-standard identification strategies.

## Likely Challenges

| Challenge | Why It Happens | How To Prepare |
|-----------|---------------|----------------|
| Identification | Finance seminars treat credible identification as a first-class requirement. | State the identification strategy in one sentence before showing results. |
| External validity | Results from one market or one regulatory setting may not generalize. | Proactively state the setting boundaries: "This holds in the U.S. public-firm context where..." |
| Economic magnitude | A statistically significant result may be economically trivial. | Report economic magnitudes alongside statistical ones: "A one-standard-deviation increase in X corresponds to a Y percent change in Z." |
| Causal language discipline | Descriptive results framed as causal will be attacked immediately. | Audit every "leads to," "causes," or "increases" in the script. Replace with "is associated with" or add explicit caveats. |
| Mechanism vs. reduced form | The audience wants to know if you have evidence for the mechanism, not just the correlation. | Separate reduced-form evidence from mechanism evidence. Do not claim mechanism if you only have correlation. |

## Overclaiming Definitions

In finance seminars, the following are common overclaiming patterns:

1. **Causal inference from cross-sectional correlations.**
   - Weak: "Firms with higher X have lower Y."
   - Strong: "We find that firms with higher X have lower Y. While we cannot rule out all endogeneity concerns, our [design/IV/RD] addresses the most plausible alternative explanations."

2. **Generalization beyond the sample.**
   - Weak: "This shows that GAI affects financial reporting."
   - Strong: "In our sample of U.S. public firms from 2010–2023, we document measurable GAI adoption in MD&A and S-1 filings. Whether this extends to private firms or international settings is an open question."

3. **Policy implications without causal evidence.**
   - Weak: "Regulators should require disclosure of GAI use."
   - Strong: "Our findings suggest that GAI adoption is already occurring at measurable rates. If regulators wish to monitor this, validated detection tools like the one we propose could be useful."

## Pacing and Tone

- **Pacing:** Slightly slower in the identification and results sections; faster through motivation and lit review.
- **Tone:** Confident but precise. Avoid hype words like "revolutionary" or "unprecedented." Use "we document," "we find," and "our estimates suggest."
- **Formality:** High. Use full names on first citation, precise terminology, and numbered equations if needed.

## Common Failure Modes

1. **Hiding the identification strategy in an appendix slide.** The audience will ask about it in the first question. Put it in the main narrative.
2. **Reporting t-statistics without economic magnitudes.** A t-stat of 4.2 means nothing if the economic effect is a 0.1 basis-point change.
3. **Using causal language in a reduced-form design.** This is the fastest way to lose credibility.
4. **Overselling policy implications.** Finance audiences are skeptical of "so what" claims that outrun the evidence.
5. **Ignoring the null result.** If a predicted effect is absent, say so. Silence invites skepticism.

## Proactive Defense Requirements

Before the audience asks, the script should already address:

1. **What is the identification strategy?** One sentence, early in the talk.
2. **What is the economic magnitude?** In interpretable units, not just coefficients.
3. **What are the main threats to validity?** Name them proactively.
4. **What is outside the scope?** Clear boundaries prevent "why didn't you..." questions.
5. **How does this relate to [well-known paper]?** The audience will compare. Get ahead of it.
