# CS / ML Exemplars

## Exemplar 1: Motivation-Style Content

**Scenario:** Conference talk  
**Domain:** Computer Science / Machine Learning  
**Audience:** Mixed CS researchers, some ML experts, some systems builders  
**Input material type:** Motivation slide with three bullets

### Slide content summary
- Title: "Why this matters"
- Bullets:
  - Existing methods fail under distribution shift
  - Real-world systems face noisy inputs
  - Need for robustness is growing

### Weak script
"Why this matters. Existing methods fail under distribution shift. Real-world systems face noisy inputs. The need for robustness is growing."

### Critique
- Pure bullet reading. Adds no explanation, no stakes, no audience hook.
- The listener already read the slide and learned nothing new.
- No transition into what the speaker actually does.

### Improved script
"Let me start with the problem that motivated this work. Most machine learning models work well in the lab, where the test data looks almost exactly like the training data. But in the real world — whether you're running a medical diagnosis system or a self-driving car — the inputs are noisy, corrupted, or just different from what the model saw during training. When that happens, standard methods drop in accuracy, sometimes catastrophically. That gap between lab performance and real-world reliability is what we target."

### Why the revision works
- Opens with a spoken hook, not a title read-aloud.
- Explains the problem in intuitive terms with concrete examples.
- Connects the abstract "distribution shift" to something the audience cares about.
- Sets up the speaker's specific angle without overstating it.

---

## Exemplar 2: Methods-Style Content

**Scenario:** Conference talk  
**Domain:** Computer Science / Machine Learning  
**Audience:** ML researchers and systems engineers  
**Input material type:** Methods slide with three bullets

### Slide content summary
- Title: "Our approach"
- Bullets:
  - Two-stage pipeline: filter, then classify
  - Filtering uses a learned threshold on uncertainty
  - Classification uses a lightweight ensemble

### Weak script
"Our approach is a two-stage pipeline: filter, then classify. The filtering stage uses a learned threshold on uncertainty. The classification stage uses a lightweight ensemble."

### Critique
- Reads bullets with minor rewording.
- No intuition for why two stages are needed.
- "Learned threshold" and "lightweight ensemble" are jargon without explanation.
- The listener knows what was done but not why it makes sense.

### Improved script
"We split the problem into two stages: filter, then classify. The reason is simple — if the input is too noisy, asking the classifier to make a decision is unfair. It will guess. So the first stage is a filter that asks, 'How confident am I about this input?' If the confidence is below a learned threshold, we flag the input for human review instead of forcing a prediction. The second stage is the actual classifier, and we use a lightweight ensemble — three small models instead of one large one — because we need the system to run in real time on a phone."

### Why the revision works
- Leads with the *why* before the *what*.
- Explains the filter in intuitive terms: "How confident am I?"
- Anchors the ensemble choice in a real constraint: running on a phone.
- Keeps technical terms but gives them spoken context.

---

## Exemplar 3: Results-Style Content

**Scenario:** Conference talk  
**Domain:** Computer Science / Machine Learning  
**Audience:** ML researchers  
**Input material type:** Results slide with bar chart

### Slide content summary
- Title: "Performance gains"
- Figure: bar chart comparing baseline vs. proposed method across 4 datasets
- Baseline: 72%, 68%, 81%, 75%
- Proposed: 79%, 76%, 85%, 80%

### Weak script
"Our method outperforms the baseline. On dataset A, we get 79% versus 72%. On dataset B, 76% versus 68%. On dataset C, 85% versus 81%. On dataset D, 80% versus 75%."

### Critique
- Reads numbers without interpretation.
- No sense of whether these gains are meaningful or incremental.
- No connection back to the motivating problem.
- The audience could read the chart faster.

### Improved script
"Across all four datasets, the proposed method improves over the baseline. The pattern is consistent: the biggest gains are on the noisier datasets — A and B — where we see roughly a 7- and 8-point jump. On the cleaner datasets — C and D — the improvement is smaller, about 4 and 5 points. That aligns with what we expected: the filter stage helps most when the input quality is poor. So the result supports the core idea that separating filtering from classification buys robustness where it is needed most."

### Why the revision works
- Groups results into a pattern rather than listing them.
- Interprets the pattern: gains are larger on noisy data.
- Connects the numbers back to the method's motivation.
- Gives the audience a takeaway they can remember.

---

## Exemplar 4: Conclusion / Contribution-Style Content

**Scenario:** Conference talk  
**Domain:** Computer Science / Machine Learning  
**Audience:** ML researchers  
**Input material type:** Contribution slide with three bullets

### Slide content summary
- Title: "Contributions"
- Bullets:
  - A robust two-stage pipeline
  - Strong empirical gains on noisy data
  - Lightweight enough for edge deployment

### Weak script
"To summarize, our contributions are: a robust two-stage pipeline, strong empirical gains on noisy data, and a system lightweight enough for edge deployment. Thank you."

### Critique
- Reads bullets and stops.
- "Strong empirical gains" is vague — strong compared to what?
- No restatement of the core problem.
- "Thank you" is not a closing; it is an abdication.

### Improved script
"Let me close by coming back to the problem we started with. We wanted a system that stays reliable when the real world throws noisy data at it. Our answer is a two-stage pipeline that separates uncertainty filtering from classification. On four standard benchmarks, that design gives consistent gains, especially on the noisiest datasets. And because the classifier is a lightweight ensemble, the whole system runs on a phone in real time. The main takeaway is simple: if you separate 'should I predict?' from 'what should I predict?' you get both robustness and speed. Thank you — I'll take questions."

### Why the revision works
- Restates the opening problem, creating narrative closure.
- Turns vague "strong gains" into a specific, defensible claim.
- Repeats the core insight in a memorable sentence.
- Ends with an explicit transition to Q&A.
