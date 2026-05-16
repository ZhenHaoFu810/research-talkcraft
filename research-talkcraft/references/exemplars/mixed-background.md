# Mixed-Background Exemplars

## Exemplar 1: Dual-Level Explanation

**Scenario:** Stakeholder briefing  
**Domain:** Environmental Science / Data Science  
**Audience:** Policymakers, environmental activists, and a few data scientists  
**Input material type:** Methods slide describing a model

### Slide content summary
- Title: "Predictive model"
- Bullets:
  - Gradient-boosted trees with 50 features
  - 87% accuracy on held-out test set
  - SHAP values for interpretability

### Weak script
"We use gradient-boosted trees with 50 features. The accuracy on the held-out test set is 87 percent. We use SHAP values for interpretability."

### Critique
- Uses jargon (gradient-boosted trees, SHAP values) without explanation.
- A policymaker will not know what SHAP is.
- No explanation of what the 50 features are or why they matter.
- The data scientists in the room will want more technical depth.

### Improved script
"The prediction model is a gradient-boosted tree — think of it as a decision-making process that learns from thousands of past examples to predict future wildfire risk. It uses 50 input variables, ranging from temperature and humidity to vegetation density and historical fire patterns. On data it has never seen before, it is correct 87 percent of the time. For the technical audience: we use XGBoost with early stopping, and the feature set includes 30 meteorological variables, 10 land-cover variables, and 10 historical fire variables. For everyone else: the key point is that the model is interpretable. We use a technique called SHAP — it tells us which variables drove each individual prediction. So if the model flags a region as high risk, we can say exactly why: temperature was the top driver, followed by dry vegetation. That transparency matters for trust."

### Why the revision works
- Gives a high-level analogy first (decision-making process).
- Lists the feature categories in plain language.
- Provides technical detail in a dedicated clause for the expert subset.
- Explains SHAP with a concrete example relevant to the application.

---

## Exemplar 2: Jargon Bridging

**Scenario:** Industry-academia collaboration meeting  
**Domain:** Materials Science  
**Audience:** Materials scientists, mechanical engineers, and project managers  
**Input material type:** Results slide with technical term

### Slide content summary
- Title: "Grain boundary strengthening"
- Bullets:
  - Hall-Petch coefficient increased by 15%
  - Yield stress: 450 MPa
  - Ductility preserved

### Weak script
"The Hall-Petch coefficient increased by 15 percent. The yield stress is 450 megapascals. Ductility is preserved."

### Critique
- "Hall-Petch coefficient" and "yield stress" are meaningless to a project manager.
- No explanation of what the numbers mean for the product.
- The engineers may want the numbers but not the mechanism.

### Improved script
"For the non-specialists: the material got stronger without becoming brittle. Think of a metal as a mosaic of tiny crystals. The boundaries between those crystals act like walls that block cracks. By refining the crystal size, we increased the density of those walls, which makes the material harder to deform. The technical metric is the Hall-Petch coefficient, which went up 15 percent. The practical result is that the yield stress — the point where the material permanently bends — is now 450 megapascals. That is strong enough for the automotive application we are targeting. And crucially, the material still has enough ductility to absorb impact without shattering. So we have the strength without the brittleness."

### Why the revision works
- Opens with the practical takeaway for non-specialists.
- Uses a visual analogy (mosaic of crystals) to explain grain boundaries.
- Gives the technical numbers for the engineers.
- Connects the result to the application (automotive).
- Repeats the key tradeoff (strength without brittleness) for emphasis.
