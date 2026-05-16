# Overlay: CS Group Meeting

## Audience Profile

- **Primary:** Lab members, advisor, and occasional visitors from the same department or adjacent groups.
- **Mixedness:** Highly variable. Theory groups are mostly theorists; systems groups include systems builders, ML engineers, and applied scientists.
- **Motivation:** Giving feedback, catching flaws early, understanding enough to collaborate or cite.

## Assumed Knowledge

The speaker can assume the audience knows:
- Standard algorithms and data structures.
- The group's shared tooling, frameworks, and baselines.
- Recent papers in the group's direct research area.
- Basic ML concepts if in an ML group; basic proof techniques if in a theory group.

**Do not over-explain:** What a neural network is (in an ML group), what Big-O is (in a theory group), or what the group's own prior work does.
**Do explain:** New architecture choices, why a non-obvious baseline was selected, and failure cases.

## Likely Challenges

| Challenge | Why It Happens | How To Prepare |
|-----------|---------------|----------------|
| Novelty vs. baseline | CS meetings ruthlessly compare to prior work. | State the exact baseline, the metric, and the improvement clearly. Do not claim "state of the art" without naming the prior SOTA. |
| Ablations | The audience wants to know which design choice matters. | Prepare a one-sentence answer for every major architectural or hyperparameter choice. |
| Compute tradeoffs | Systems and ML audiences care about cost. | Report training time, inference latency, memory footprint, or energy cost if relevant. |
| Reproducibility | Can someone else run this? | Mention code availability, dataset access, and random seeds if applicable. |
| Theory-practice gap | Theory groups ask "does this assumption hold in practice?" Applied groups ask "what is the worst-case guarantee?" | Know which side of the gap your work sits on and defend the boundary. |

## Overclaiming Definitions

In CS group meetings, the following are common overclaiming patterns:

1. **"State of the art" without a named baseline.**
   - Weak: "Our model achieves state-of-the-art performance."
   - Strong: "On [dataset], our model achieves X% accuracy, improving over the previous best of Y% reported by [Author et al., Year]."

2. **Claiming novelty for a standard technique.**
   - Weak: "We propose a novel attention mechanism."
   - Strong: "We adapt the standard attention mechanism by [specific change], which addresses [specific problem] in our setting."

3. **Ignoring negative results.**
   - Weak: Only showing the successful experiments.
   - Strong: "We also tried [alternative]. It underperformed because [reason]. This is in the appendix."

## Pacing and Tone

- **Pacing:** Fast. Group meetings are short (20–30 minutes). Spend minimal time on background.
- **Tone:** Collaborative and direct. It is okay to say "this is a dumb bug but it cost us two weeks" or "we don't know why this works yet."
- **Formality:** Low to medium. Use first person, contractions, and conversational transitions.

## Common Failure Modes

1. **Over-explaining background the group already knows.** Waste of time; signals the speaker does not know the audience.
2. **Hiding negative results.** The group will find out eventually. Early honesty builds trust.
3. **No clear ask.** Group meetings are for feedback. End with: "The place where I need input is..."
4. **Vague baseline comparisons.** "We did better than the baseline" is insufficient. By how much, on what metric, with what variance?
5. **Ignoring reproducibility.** If the code is not runnable, say why and when it will be.

## Proactive Defense Requirements

Before the audience asks, the script should already address:

1. **What is the exact baseline and the exact improvement?** Numbers, metrics, datasets.
2. **What ablations did you run?** At minimum, know which components matter.
3. **What is the compute cost?** Time, hardware, memory.
4. **What is reproducible right now?** Code, data, seeds, environment.
5. **What do you need feedback on?** End with a specific question, not a generic "any questions?"
