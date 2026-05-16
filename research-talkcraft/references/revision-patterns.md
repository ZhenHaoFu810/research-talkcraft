# Revision Patterns

This file documents common `weak script -> stronger script` transformations. Use these as a checklist during the revision stage. Match the weakness to a pattern, apply the transformation, and verify the improvement.

---

## Pattern 1: Bullet Reading -> Explanation

### Failure mode
The script reads slide bullets almost verbatim, adding only minor rewording. The speaker is a human text-to-speech engine.

### Why it hurts rehearsal quality
- The audience can read the slide faster than the speaker can say it.
- The script adds no value.
- The speaker sounds unprepared.

### What the better version does instead
- States the bullet as context, then explains the *meaning*, *intuition*, or *implication* behind it.
- Uses the bullet as a prompt for a short story, example, or analogy.
- Adds a "so what" sentence that is not on the slide.

### Example transformation
- **Weak:** "Our approach has three steps. First, data collection. Second, feature extraction. Third, model training."
- **Better:** "We break the problem into three stages. The first is data collection — and here the key challenge was that the raw signal is extremely noisy, so we had to design a custom filtering step. That filtered data then feeds into feature extraction, where we prioritize interpretability over raw predictive power. Finally, the model training stage uses a lightweight architecture so the system can run in real time."

---

## Pattern 2: Method Detail Dump -> Audience-Oriented Intuition

### Failure mode
The script lists every hyperparameter, equation, or implementation detail from the method slide.

### Why it hurts rehearsal quality
- The audience cannot absorb technical detail at speaking speed.
- The narrative stalls.
- The speaker sounds like they are reading a manual.

### What the better version does instead
- Leads with the core idea in one sentence.
- Explains *why* the method is shaped the way it is.
- Defers excessive detail to a backup slide or a verbal "if you're interested in the details..."

### Example transformation
- **Weak:** "We use a transformer with 12 layers, 8 attention heads, a hidden dimension of 256, dropout of 0.1, and we train for 100 epochs with Adam and a learning rate of 1e-4."
- **Better:** "The model is a standard transformer, but the key design choice is that we keep it relatively small — 12 layers, 256 dimensions — because we need it to run on edge devices. The smaller footprint means we sacrifice a little raw accuracy, but we gain the ability to deploy in real time, which is the actual requirement for this application."

---

## Pattern 3: Result Statement -> Result Interpretation

### Failure mode
The script states a result but does not explain what it means or why it matters.

### Why it hurts rehearsal quality
- The audience sees a number but does not know if it is good, bad, surprising, or expected.
- The speaker misses the chance to sell the contribution.

### What the better version does instead
- Interprets the result in plain language.
- Compares it to a baseline, expectation, or prior work.
- Connects it back to the motivating question.

### Example transformation
- **Weak:** "Our model achieves 87.3% accuracy on the test set."
- **Better:** "On the test set, the model hits 87.3% accuracy. That may not sound dramatic, but the best prior method on this exact benchmark was 82%, and the human baseline is around 90%. So we've closed most of the gap to human performance, and we do it with a model that is ten times smaller."

---

## Pattern 4: Vague Contribution Claim -> Evidence-Backed Contribution Framing

### Failure mode
The script claims a contribution but provides no evidence or specificity. "We improve the state of the art" or "Our method is more efficient."

### Why it hurts rehearsal quality
- Skeptical listeners will immediately ask: "By how much? Compared to what? Under what conditions?"
- The speaker sounds like they are hyping rather than presenting.

### What the better version does instead
- States the contribution with a concrete metric and a comparison.
- Qualifies the scope: "on this dataset," "for this class of problems."
- Acknowledges boundary conditions.

### Example transformation
- **Weak:** "Our approach is more robust than existing methods."
- **Better:** "On the three standard robustness benchmarks, our approach improves average performance by 8 percentage points over the best prior method. The gain is largest on adversarial examples — 12 points — and smallest on natural corruption — 4 points. So the contribution is strongest in adversarial settings."

---

## Pattern 5: Long Explanation -> Time-Bounded Explanation

### Failure mode
The script allocates too much time to a secondary point, risking overrun.

### Why it hurts rehearsal quality
- The speaker runs out of time before the main results.
- The audience loses focus during a long digression.

### What the better version does instead
- Provides a primary version (30 seconds) and a backup version (2 minutes) for complex sections.
- Marks a clear "if short on time, stop here" point.
- Moves optional detail to a backup slide.

### Example transformation
- **Weak:** A 90-second script for a background slide that most of the audience already understands.
- **Better:** A 20-second version: "You probably know the standard framework, so I'll just highlight the one assumption we relax — the independence condition — and why that matters for our setting. If anyone wants the full derivation, see the backup slide."

---

## Pattern 6: Abrupt Slide Shift -> Narrative Transition

### Failure mode
The script ends one slide with a closing sentence and starts the next with no bridge. The talk feels like a slideshow, not a story.

### Why it hurts rehearsal quality
- The audience has to mentally reboot between every slide.
- The speaker sounds like they are ticking through a list.

### What the better version does instead
- Adds a sentence that connects the outgoing slide to the incoming one.
- Uses preview language: "Now that we know X, we can ask Y."
- Uses recap language: "So the main takeaway is X. That leads directly to the next question."

### Example transformation
- **Weak:** "That concludes the motivation. Next, the methods."
- **Better:** "So the core problem is that existing methods fail when the data is adversarially corrupted. The natural question is: what structure in the data can we exploit to fix that? Our answer is a robust feature extractor, and here's how it works."

---

## Pattern 7: Jargon Dump -> Inline Definition

### Failure mode
The script uses technical terms without explanation, assuming the audience already knows them.

### Why it hurts rehearsal quality
- A subset of the audience is lost immediately.
- The speaker sounds exclusive rather than inclusive.

### What the better version does instead
- Defines the term on first use in one short phrase.
- Uses an analogy or example to anchor the term.
- Keeps the definition in spoken language, not dictionary language.

### Example transformation
- **Weak:** "We use causal forest estimation to compute heterogeneous treatment effects."
- **Better:** "We use causal forests — that's a machine-learning method that finds subgroups where the treatment effect is strongest — to figure out which patients benefit most from the intervention."

---

## Pattern 8: Timing Compression Under Pressure

### Failure mode
The script exceeds the target duration, or the timing helper flags multiple sections as overrun risks. The speaker has no clear plan for what to cut without damaging the narrative.

### Why it hurts rehearsal quality
- The speaker is forced to improvise cuts during the talk, which disrupts flow.
- Random cutting often removes transitions or examples that the audience needs.
- Overruns signal poor time discipline to reviewers and organizers.

### What the better version does instead
- Compresses background to the minimum needed for this audience.
- Collapses redundant transitions into a single bridging sentence.
- Replaces example-heavy explanations with one strongest example.
- Moves technical depth to a backup slide or Q&A buffer.
- Marks explicit "if short on time" stopping points.

### Example transformations

**Compress background:**
- **Weak:** A 60-second historical overview of a field the audience already knows.
- **Better:** "You know the standard setup, so I'll skip to the one assumption we relax."

**Collapse redundant transitions:**
- **Weak:** Three consecutive slides each open with a recap of the previous slide.
- **Better:** One recap at the section boundary, then direct entry into each slide.

**Replace example-heavy explanation:**
- **Weak:** Two detailed examples illustrating the same mechanism.
- **Better:** One detailed example plus a one-sentence note that the pattern generalizes.

**Move technical depth to backup/Q&A:**
- **Weak:** A full derivation on the main path of the talk.
- **Better:** "The intuition is X; the formal derivation is on the backup slide if anyone wants the details."

### Audience-aware constraint
Timing compression must not remove the core claim, the key intuition, or the audience bridge. Cut around the critical path, not through it.

---

## Revision Workflow

1. Scan the first-pass script for each pattern.
2. Tag the location of each weakness.
3. Apply the corresponding transformation.
4. Verify that the revised script sounds natural when read aloud.
5. Re-check timing after revision. If the script is still over budget, apply Pattern 8 (Timing Compression Under Pressure).

## Exemplar References

For concrete illustrations of each pattern, consult `references/exemplars/failure-modes.md`. For domain-specific examples, see:
- `references/exemplars/cs-ml.md` — machine learning scenarios
- `references/exemplars/finance-econ.md` — finance and economics scenarios
- `references/exemplars/neuroscience.md` — neuroscience and biology scenarios
- `references/exemplars/social-science.md` — social science and mixed-methods scenarios

For audience-specific calibration, see:
- `references/exemplars/seminar-style.md` — mixed-audience seminars
- `references/exemplars/defense-style.md` — thesis defenses
- `references/exemplars/group-meeting.md` — informal group meetings
- `references/exemplars/mixed-background.md` — stakeholder briefings
- `references/exemplars/chinese-academic.md` — Chinese academic presentations

---

## Chinese-Specific Revision Patterns

These patterns address weaknesses that appear specifically in Chinese academic research talks.

### Pattern C1: Written-Formality -> Spoken Naturalness

**Failure mode:** The script uses phrases common in written Chinese academic papers ("本文"、"研究表明"、"具有重要的理论和实践意义") that sound stiff when spoken.

**Why it hurts rehearsal quality:**
- The speaker sounds like they are reading an abstract, not giving a talk.
- Creates distance between speaker and audience.
- These phrases add no information.

**What the better version does instead:**
- Replaces "本文" with "我们" or omits the subject entirely.
- Replaces "研究表明" with "我们发现" or "数据显示".
- Replaces generic significance claims with concrete implications.

**Example transformation:**
- **Weak:** "本文发现宏观审慎政策对银行风险承担具有显著的抑制作用，这一发现具有重要的理论和实践意义。"
- **Better:** "我们发现宏观审慎政策确实降低了银行的风险承担。这意味着监管部门手里多了一个可用的工具，但也提醒我们注意政策的边界——它并不是万能的。"

---

### Pattern C2: Translated Signposting -> Native Spoken Bridges

**Failure mode:** Transitions are literal translations of English signposting ("接下来"、"下面进入第二部分") with no narrative connection.

**Why it hurts rehearsal quality:**
- The audience has to mentally reboot between every section.
- Sounds mechanical, like a slide-change announcement.

**What the better version does instead:**
- Recaps the previous section's takeaway.
- Previews the next section's purpose using cause-and-effect logic.
- Uses natural spoken connectors ("那么问题来了"、"基于这个观察"、"反过来想").

**Example transformation:**
- **Weak:** "以上就是文献综述的内容。下面介绍研究方法。"
- **Better:** "前面我们看了，现有文献主要用相关性方法来估计政策效果，但因果识别一直是个难题。那要解决这个问题，我们得换一个思路——利用政策实施中的断点来构造一个准自然实验。"

---

### Pattern C3: Vague Gap-Filling -> Concrete Contribution Framing

**Failure mode:** The script frames the contribution as "填补了研究空白" without specifying what空白, why it matters, or who cares.

**Why it hurts rehearsal quality:**
- Skeptical listeners immediately ask: "什么空白？为什么这个空白重要？"
- The speaker sounds like they are using a template rather than making a real argument.
- In Chinese defenses, this is a common target for committee pushback.

**What the better version does instead:**
- Replaces "填补空白" with a concrete tension or puzzle.
- Specifies the prior assumption that is relaxed or the prior result that is challenged.
- Connects the contribution to a question the audience already cares about.

**Example transformation:**
- **Weak:** "本文填补了宏观审慎政策效果评估领域的研究空白。"
- **Better:** "之前的研究大多把宏观审慎政策当成一个整体来评估，但没有区分政策工具之间的差异。我们想知道：同样是资本缓冲，对大型银行和小型银行的影响是一样的吗？答案是否定的——我们发现存在明显的异质性。"

---

### Pattern C4: Overclaiming -> Defensible Boundaries

**Failure mode:** The script uses strong claims like "首次发现" or "全新的理论框架" when the evidence supports a more modest conclusion.

**Why it hurts rehearsal quality:**
- In Chinese academic settings, especially defenses, overclaiming damages credibility.
- Committee members and skeptical reviewers pounce on exaggerated claims.
- The speaker may not be able to defend the claim under follow-up questioning.

**What the better version does instead:**
- Replaces "首次" with a specific, bounded finding.
- Replaces "全新的理论框架" with "我们提出了一种新的分析视角" or "我们放松了某某假设".
- Explicitly states scope boundaries before the audience asks.

**Example transformation:**
- **Weak:** "本文首次揭示了神经通路与决策行为的因果关系，提出了全新的理论框架。"
- **Better:** "在这个特定的决策任务中，我们发现激活这条通路会改变动物的风险偏好。需要强调的是，这个结论目前仅限于小鼠模型和我们的任务范式，是否能推广还需要进一步验证。"

---

### Pattern C5: Parallel Bullet Reading -> Spoken Argument

**Failure mode:** Chinese slides often use parallel grammatical structures (动宾短语 lists), and speakers read them verbatim, creating a mechanical rhythm.

**Why it hurts rehearsal quality:**
- Sounds like reading a table of contents.
- The audience sees the bullets and hears the same words simultaneously.
- No causal logic or narrative progression.

**What the better version does instead:**
- Breaks the parallel structure.
- Turns the list into a spoken argument with cause-and-effect logic.
- Adds "所以"、"这意味着"、"问题是" to create narrative flow.

**Example transformation:**
- **Weak:** "现有方法存在三个问题：计算复杂度高、对噪声敏感、难以扩展到大规模数据。"
- **Better:** "现有方法有两个根本性的限制。第一，计算复杂度太高，导致我们无法在合理时间内处理大规模数据。第二，这些方法对噪声非常敏感——数据稍有偏差，结果就会大幅波动。所以我们需要一个新的思路，既能保持准确性，又能控制计算成本。"

---

## Exemplar References for Chinese Patterns

For concrete illustrations of Chinese-specific weak and improved scripts, consult:
- `references/exemplars/chinese-academic.md` — Chinese academic seminar, lab meeting, and defense examples
