# Neuroscience / Biology Exemplars

## Exemplar 1: Methods-Intuition Content

**Scenario:** Lab meeting  
**Domain:** Neuroscience  
**Audience:** Lab members with mixed expertise (some electrophysiologists, some computational)  
**Input material type:** Methods slide describing recording technique

### Slide content summary
- Title: "Electrophysiology setup"
- Bullets:
  - 64-channel silicon probe in hippocampus CA1
  - Spike sorting with Kilosort 2.0
  - LFP filtered 1–200 Hz

### Weak script
"We use a 64-channel silicon probe implanted in hippocampus CA1. Spikes are sorted with Kilosort 2.0. The local field potential is filtered between 1 and 200 Hertz."

### Critique
- Reads method specs without explaining why this setup is appropriate.
- A mixed lab will lose the non-electrophysiologists immediately.
- No intuition for what CA1 means or why spike sorting matters.
- "Kilosort 2.0" is jargon without context.

### Improved script
"To record neural activity, we implant a 64-channel silicon probe in the hippocampus — specifically area CA1, which is the brain region that forms episodic memories. Think of the probe as a tiny microphone array: each channel listens to the electrical chatter of nearby neurons. We then run the raw signal through Kilosort, which is an open-source algorithm that separates the mixed electrical activity into individual neurons' spike trains. The local field potential — the slower rhythm that reflects the summed activity of thousands of neurons — is filtered to capture frequencies from 1 to 200 Hertz. That range covers the theta and gamma rhythms we care about."

### Why the revision works
- Maps each technical term to an intuitive analogy (microphone array).
- Explains *why* CA1 matters (episodic memory) before stating the fact.
- Gives Kilosort a one-sentence purpose: "separates mixed activity into individual neurons."
- Connects the LFP filter range to the biological phenomena of interest.

---

## Exemplar 2: Mechanism-Explanation Content

**Scenario:** Seminar presentation  
**Domain:** Neuroscience  
**Audience:** Mixed neuroscientists and cognitive psychologists  
**Input material type:** Results slide about a mechanism

### Slide content summary
- Title: "Theta-gamma coupling predicts memory performance"
- Figure: scatter plot showing correlation between coupling strength and recall accuracy
- Statistic: r = 0.48, p < 0.001

### Weak script
"Theta-gamma coupling predicts memory performance. The correlation is 0.48, p less than 0.001. This suggests that cross-frequency coupling is important for memory."

### Critique
- States the correlation without explaining the mechanism.
- "Important for memory" is vague.
- No explanation of what theta-gamma coupling actually is or why it might matter.
- The audience could read the p-value on the slide.

### Improved script
"Here is the key finding: the stronger the coupling between theta and gamma rhythms, the better the animal remembers the location. Let me unpack that. Theta is the slow brain wave — about 8 cycles per second — that organizes when neurons fire. Gamma is the fast wave — about 40 cycles per second — that reflects active computation. Theta-gamma coupling means that the fast gamma bursts are locked to specific phases of the slow theta cycle. Our result shows that when this locking is stronger, the animal's spatial memory is more accurate. The correlation is 0.48, which is moderate but robust. The interpretation is that theta acts like a temporal organizer, and gamma acts like the actual information carrier. When they are well-coordinated, memory works better."

### Why the revision works
- Explains the mechanism before stating the statistic.
- Uses concrete frequencies and analogies (organizer and carrier).
- Connects the neural phenomenon to the behavioral outcome.
- Gives the audience a mental model, not just a correlation.
