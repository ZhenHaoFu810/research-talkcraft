# Audience Personas

These personas represent typical audience members at research presentations. In `v0`, they are used within a single-agent critique loop to simulate likely confusion, challenge, and Q&A. They do not require a multi-agent system.

Use them during:
- Critique ("Would the Confused Listener understand this transition?")
- Q&A generation ("What would the Skeptical Reviewer ask here?")
- Revision prioritization ("Which persona is most likely to be lost on this slide?")

---

## 1. Confused Listener

### What they know
- They understand the broad field but are not deep in this sub-topic.
- They may have heard of the general problem but not the specific approach.
- They are trying to follow the talk in real time without re-reading slides later.

### What they typically do not understand
- Why this problem matters right now.
- How the method works at an intuitive level.
- The meaning of a result without explicit interpretation.
- How one slide connects to the next.

### What kinds of questions they ask
- "Can you explain why you chose this approach over the standard one?"
- "What does this result actually mean in practice?"
- "Could you walk through the intuition one more time?"
- "How does this connect to what you showed two slides ago?"

### What weak script they will expose
- Bullet reading with no explanation.
- Jargon that is never defined.
- Abrupt jumps between topics.
- Results presented without interpretation.
- Method slides that list steps but give no intuition.

### How to use in `v0`
- During critique, ask: "If I knew only the broad field, would I understand why this slide matters?"
- During Q&A, generate 1–2 clarification questions per major section.
- During revision, add intuition bridges and explicit motivation language.

---

## 2. Domain Expert

### What they know
- They work in the same sub-field and understand the standard methods.
- They know the relevant literature and can spot subtle technical choices.
- They expect precision and respect for established conventions.

### What they typically do not understand
- Why the author made a specific modeling or methodological choice that deviates from the norm.
- Whether the result is actually new or just a minor extension.
- Whether the claimed contribution is large enough to justify the method.

### What kinds of questions they ask
- "Why did you use Method X instead of the more common Method Y?"
- "How does this compare to the result in [Known Paper Z]?"
- "Can you be more precise about the identifying assumption?"
- "Is this a robustness check or the main specification?"

### What weak script they will expose
- Over-explaining basics the audience already knows.
- Vague or imprecise technical descriptions.
- Claims of novelty that are not well supported.
- Missing acknowledgment of related work.

### How to use in `v0`
- During critique, ask: "Would an expert find this precise enough? Would they ask for more detail?"
- During Q&A, generate 1–2 method or comparison questions per technical section.
- During revision, calibrate depth: add precision for experts, but keep intuition for mixed audiences.

---

## 3. Skeptical Reviewer

### What they know
- They are trained to find weaknesses, alternative explanations, and unsupported claims.
- They may not be hostile, but they are rigorous and will push on boundaries.
- They care about validity, robustness, and honest limitation disclosure.

### What they typically do not understand
- Why the author is confident in a causal or general claim given the evidence shown.
- Why a limitation was omitted or downplayed.
- How the result survives obvious robustness concerns.

### What kinds of questions they ask
- "What is the most important threat to your identification strategy?"
- "How do you know this isn't driven by [alternative mechanism]?"
- "Why didn't you report [standard robustness check]?"
- "Isn't your sample selection a concern given [obvious bias]?"

### What weak script they will expose
- Overconfident claims without acknowledged boundary conditions.
- Missing limitations.
- Causal language where only correlation is shown.
- Method descriptions that hide rather than clarify assumptions.

### How to use in `v0`
- During critique, ask: "What would a skeptical reviewer pounce on here?"
- During Q&A, generate 1–2 challenge questions per claim slide.
- During revision, add proactive qualifiers, surface limitations honestly, and replace overconfident framing with defensible language.

---

## Single-Agent Simulation Guidance

In `v0`, a single agent can simulate all three personas sequentially:

1. **First pass:** Read the script as the Confused Listener. Mark anything that feels unexplained or unmotivated.
2. **Second pass:** Read the script as the Domain Expert. Mark anything that feels imprecise or under-explained.
3. **Third pass:** Read the script as the Skeptical Reviewer. Mark any claim that feels too strong or any limitation that is hidden.

---

## Chinese Research Settings: Persona Variations

In Chinese academic settings, the three core personas behave somewhat differently from their Western counterparts. The Skill should calibrate critique and Q&A generation accordingly.

### Confused Listener in Chinese Seminars

**What changes:**
- May be less likely to interrupt or ask clarifying questions during the talk, but confusion will show in post-talk Q&A or private feedback.
- Often loses the thread when the speaker uses written-formal transitions ("基于以上分析"、"综上所述") instead of spoken bridges.
- May not be familiar with English technical terms that the speaker leaves untranslated.

**What weak script they will expose:**
- Overly literal bullet reading, especially parallel 动宾短语 lists.
- Transitions that announce sections rather than connect ideas.
- Jargon dumped without either a Chinese paraphrase or a clear English anchor.

**How to use:**
- During critique, ask: "Would a listener who is not deep in this sub-field understand why this matters in the first two minutes?"
- During revision, add explicit motivation and replace written-formal phrases with spoken Chinese.

### Domain Expert in Chinese Settings

**What changes:**
- Expects precision but also values humility. Overclaiming ("首次"、"颠覆性") is viewed more negatively than in some Western contexts.
- May ask comparative questions referencing well-known domestic or international work.
- Often evaluates whether the method choice is justified given local data constraints.

**What weak script they will expose:**
- Vague novelty claims without precise boundaries.
- Missing acknowledgment of related domestic literature.
- Method descriptions that ignore practical constraints (e.g., data availability in China).

**How to use:**
- During critique, ask: "Would an expert find this claim defensible? Is the scope clearly bounded?"
- During Q&A, generate questions that reference known papers or domestic data constraints.

### Skeptical Reviewer in Chinese Defenses

**What changes:**
- In defense settings, committee members often have an explicit evaluative role. Their questions may be direct and probing.
- They are particularly sensitive to scope overreach and to claims that sound like they belong in a press release rather than a thesis.
- They may challenge external validity specifically in the Chinese context.

**What weak script they will expose:**
- "填补了研究空白" without specifying the空白.
- Overconfident causal language given the identification strategy.
- Missing robustness checks that are standard in the field.

**How to use:**
- During critique, ask: "What would a committee member pounce on here? Is every strong claim properly qualified?"
- During Q&A, generate direct challenges about scope, robustness, and external validity in the Chinese context.

---

## Single-Agent Simulation Guidance

In `v0`, a single agent can simulate all three personas sequentially:

1. **First pass:** Read the script as the Confused Listener. Mark anything that feels unexplained or unmotivated.
2. **Second pass:** Read the script as the Domain Expert. Mark anything that feels imprecise or under-explained.
3. **Third pass:** Read the script as the Skeptical Reviewer. Mark any claim that feels too strong or any limitation that is hidden.

Consolidate the three passes into one critique summary and one set of Q&A questions.
