# Defense-Style Exemplars

## Exemplar 1: Contribution Boundary

**Scenario:** Thesis defense  
**Domain:** Computer Science  
**Audience:** Thesis committee (systems, theory, and ML experts)  
**Overlay:** `defense-heavy-talk`  
**Input material type:** Contribution slide

### Slide content summary
- Title: "Contributions of this thesis"
- Bullets:
  - A new distributed training algorithm
  - Strong scaling to 10,000 GPUs
  - Open-source implementation

### Weak script
"The contributions of this thesis are: a new distributed training algorithm, strong scaling to 10,000 GPUs, and an open-source implementation."

### Critique
- Reads bullets without distinguishing the speaker's own work from collaborative work.
- A committee member will ask: "What did *you* do versus what your advisors or coauthors did?"
- "Strong scaling" is vague — strong compared to what baseline?
- No scope boundary.

### Improved script
"The core contribution of this thesis is a distributed training algorithm that maintains convergence guarantees while scaling to 10,000 GPUs. I developed the algorithm and the convergence proof. The large-scale experiments were run in collaboration with [Coauthor], who handled the cluster infrastructure, and [Advisor], who advised on the theoretical framework. The open-source implementation was led by [Coauthor], with my contribution focused on the core training loop and the API design. What is mine is the algorithm, the proof, and the benchmarking methodology. What is collaborative is the systems engineering and the release packaging."

### Why the revision works
- Uses first-person singular for the speaker's own contributions.
- Explicitly attributes collaborative work.
- Prepares the committee for the inevitable attribution question.
- Sets a clear boundary that the speaker can defend.

---

## Exemplar 2: Methodological Justification

**Scenario:** Thesis defense  
**Domain:** Economics  
**Audience:** Thesis committee (econometrician, theorist, and applied economist)  
**Overlay:** `defense-heavy-talk`  
**Input material type:** Methods slide

### Slide content summary
- Title: "Why diff-in-diff and not IV?"
- Bullets:
  - IV requires a valid instrument
  - No credible instrument available
  - DiD relies on parallel trends

### Weak script
"We use diff-in-diff instead of IV because we do not have a valid instrument. DiD relies on parallel trends, which we verify in the data."

### Critique
- Too brief for a defense. The committee expects a thorough justification.
- "Verify in the data" is weak — how exactly?
- No discussion of why other methods (synthetic control, RDD) were ruled out.

### Improved script
"A natural question is why we use diff-in-diff rather than instrumental variables or synthetic control. IV was our first choice, but we could not find a credible instrument that affects adoption without directly affecting the outcome through other channels. Every candidate we considered — local tech infrastructure, regional internet speed, manager turnover — failed the exclusion restriction. Synthetic control was also attractive, but our treatment is staggered across firms and time, which violates the standard synthetic-control assumptions. Diff-in-diff with staggered treatment timing and firm fixed effects is the most credible design available given the data. The key assumption is parallel trends, which we verify with an event-study plot and a placebo test using pre-period leads. Both support the design."

### Why the revision works
- Explains why the obvious alternatives were ruled out.
- Names specific instruments and why they failed.
- Shows the committee that the speaker thought through the choice systematically.
- Connects the method to the data structure (staggered treatment).
