# Q&A Playbook

This playbook defines the categories of questions that commonly arise in research presentations. For each category, it describes what a strong answer should contain, what makes an answer risky or weak, and how to link the Q&A to specific slides, claims, and uncertainty points.

---

## 1. Clarification

### What it asks
The questioner wants to understand something better. They are not challenging the claim; they need a clearer explanation.

### What a strong answer contains
- A one-sentence restatement of the point in simpler language.
- A concrete example or analogy if helpful.
- A brief check: "Does that address your question?"

### What makes an answer risky or weak
- Repeating the exact same words from the slide.
- Diving into unnecessary technical depth that obscures the point.
- Apologizing excessively or sounding uncertain about the basic claim.

### How to generate likely questions
- For every slide with jargon, dense notation, or a complex figure, ask: "What would someone need explained here?"
- For every transition, ask: "Could a listener lose the thread here?"

---

## 2. Motivation

### What it asks
The questioner wants to know why this problem matters, why now, or why this approach over alternatives.

### What a strong answer contains
- A crisp statement of the gap or inefficiency the work addresses.
- One sentence on why existing solutions are insufficient.
- A brief link to a real or plausible application.

### What makes an answer risky or weak
- "Because it's interesting" or "Because no one has done it."
- Overstating practical impact if the work is theoretical.
- Failing to acknowledge reasonable alternative motivations.

### How to generate likely questions
- For the opening slides, ask: "Why should this audience care?"
- For the approach slide, ask: "Why not the standard method?"

---

## 3. Method

### What it asks
The questioner wants to understand how the analysis was done, why a specific choice was made, or how the method works.

### What a strong answer contains
- A high-level intuition first, then one layer of detail if pressed.
- A justification for the key choice (not every choice, but the salient one).
- An honest acknowledgment of limitations or trade-offs.

### What makes an answer risky or weak
- Reading the method bullet points verbatim.
- Claiming a method is "standard" when it is not, or vice versa.
- Hiding a known weakness in the design.

### How to generate likely questions
- For every non-standard methodological choice, ask: "Why this and not the alternative?"
- For every complex method, ask: "What is the simplest explanation of how this works?"

---

## 4. Validity

### What it asks
The questioner is probing whether the result is robust, whether the design supports the claim, or whether the analysis is sound.

### What a strong answer contains
- A clear statement of the key assumption or identification strategy.
- One piece of evidence that supports validity (e.g., a placebo test, a robustness check).
- An honest boundary: "This holds under the assumption that..."

### What makes an answer risky or weak
- Dismissing the concern without engaging.
- Making up a robustness check that was not performed.
- Claiming the result is "definitely causal" when the design is only suggestive.

### How to generate likely questions
- For every causal or general claim, ask: "What is the biggest threat to validity here?"
- For every sample or dataset, ask: "Could selection bias be a concern?"

---

## 5. Limitation

### What it asks
The questioner wants to know what the work does not cover, where it might fail, or what the boundaries are.

### What a strong answer contains
- An explicit limitation stated proactively.
- A brief explanation of why the limitation exists.
- A constructive framing: "This means our results apply best to..." or "Future work could address this by..."

### What makes an answer risky or weak
- Saying "we have no limitations."
- Only acknowledging trivial limitations while hiding serious ones.
- Letting the limitation undermine the entire contribution without qualification.

### How to generate likely questions
- For every scope boundary, ask: "What happens outside this boundary?"
- For every strong claim, ask: "Under what conditions does this not hold?"

---

## 6. Implication

### What it asks
The questioner wants to know what the result means for practice, policy, future research, or related areas.

### What a strong answer contains
- A clear distinction between what the result shows and what it suggests.
- One concrete implication that is directly supported.
- A boundary on over-interpretation.

### What makes an answer risky or weak
- Jumping from a lab result to a policy recommendation.
- Claiming implications that are not supported by the evidence.
- Being so cautious that the answer sounds like the work has no value.

### How to generate likely questions
- For every result slide, ask: "So what? Who should change what based on this?"
- For the conclusion, ask: "What is the most important next step, and why?"

---

## 7. Hostile or Skeptical Challenge

### What it asks
The questioner is openly skeptical, possibly aggressive. They may believe the work is wrong, overstated, or unoriginal.

### What a strong answer contains
- A calm acknowledgment of the concern.
- A precise response to the specific challenge, not a general defense.
- If the challenge has merit, a graceful concession: "That is a fair point; what we can say with confidence is..."
- If the challenge is based on a misunderstanding, a respectful correction with evidence.

### What makes an answer risky or weak
- Getting defensive or dismissive.
- Agreeing too quickly and undermining the whole contribution.
- Filibustering to run out the clock.

### How to generate likely questions
- For every strong claim, ask: "What would someone who disagrees say here?"
- For every methodological novelty, ask: "Isn't this just a minor tweak on [known approach]?"

---

## 8. Contradiction-Triggered Challenge

### What it asks
The questioner has noticed (or suspects) a discrepancy between what the speaker says and what the paper or supporting material says. This is especially common in `slides+context` presentations where some audience members have read the paper.

### What a strong answer contains
- A calm acknowledgment of the discrepancy.
- A clear statement of which version the speaker is presenting and why.
- If the discrepancy is unresolved: "That is a good catch. The deck and the paper differ on this point because [reason]. I am presenting the deck version today, but the updated paper uses [other version]."

### What makes an answer risky or weak
- Pretending there is no discrepancy when one exists.
- Blaming the discrepancy on "a typo" without explaining which version is correct.
- Getting defensive about the mismatch.

### How to generate likely questions
- For every detected contradiction in the Contradiction Report, ask: "What would an audience member who has read the paper ask about this discrepancy?"
- For High-severity contradictions, assume the question will be aggressive and prepare a graceful response.

---

## Linking Q&A to Slides, Claims, and Uncertainty Points

For every likely Q&A item, the Skill must record:
- **Source slide/section:** Where in the talk the question is most likely to arise.
- **Linked claim:** The specific statement that triggers the question.
- **Known uncertainty:** Whether the materials already flag this as a weakness or gap.

This grounding ensures the Q&A section is rehearsal-relevant, not generic.

---

---

## Overlay-Specific Q&A Emphasis

When an overlay is active, the Skill should generate additional likely questions from the overlay's challenge patterns and weight them higher in the Q&A section.

### Finance Academic Talk Overlay

Generate at least one question from each of the following:
- **Identification:** "What is your identification strategy, and why should we believe it?"
- **Economic magnitude:** "That coefficient is statistically significant, but is it economically meaningful?"
- **External validity:** "Your sample is [setting]. Would this hold in [other setting]?"
- **Causal language:** "You say X causes Y. But your design is [design]. How do you rule out [alternative]?"
- **Mechanism:** "Do you have direct evidence for the mechanism, or is this just a correlation?"

### CS Group Meeting Overlay

Generate at least one question from each of the following:
- **Baseline specificity:** "What is the exact baseline, and what is the improvement in absolute terms?"
- **Ablations:** "Which component of your model actually drives the gain?"
- **Compute tradeoffs:** "What is the training cost and inference latency compared to the baseline?"
- **Reproducibility:** "Is the code publicly available? What are the random seeds and environment?"
- **Theory-practice gap:** "Does your theoretical assumption hold on real data?"

### Defense-Heavy Talk Overlay

Generate at least one question from each of the following:
- **Contribution boundary:** "What is your specific contribution versus what your coauthors did?"
- **Methodological justification:** "Why did you choose X over the standard Y approach?"
- **Scope discipline:** "Why didn't you address [obvious extension]?"
- **Cross-chapter consistency:** "Chapter 2 assumes X, but Chapter 3 assumes not-X. How do you reconcile this?"
- **Limitation ownership:** "What is the biggest limitation of this thesis, and why doesn't it invalidate your main result?"

When no overlay is active, these extra questions are optional. The base Q&A categories (Clarification, Motivation, Method, Validity, Limitation, Implication, Hostile Challenge) remain the primary framework.

## Q&A Generation Checklist

After drafting the script, run through:
- [ ] At least one clarification question per dense slide.
- [ ] At least one motivation question for the opening.
- [ ] At least one method question per non-trivial methodological choice.
- [ ] At least one validity question per causal or general claim.
- [ ] At least one limitation question per scope boundary.
- [ ] At least one implication question per major result.
- [ ] At least one skeptical challenge per bold claim.

If a category has no natural question for a given talk, explicitly state: "No natural [category] questions identified for this deck."

---

## Chinese-Specific Q&A Patterns

When the talk is in Chinese and the audience is a Chinese academic setting, generate additional likely questions that reflect common concerns in these contexts. These supplement, not replace, the base Q&A categories.

### Chinese Academic Seminar

Generate at least one question from each of the following:
- **Contribution clarity:** "你这项工作的核心贡献到底是什么？和已有文献相比，边界在哪里？"
- **Chinese context relevance:** "这个结论在中文情境下是否适用？中国的数据或制度环境会不会有不同的表现？"
- **Methodological transparency:** "你的识别策略在中文数据上会不会有特殊的挑战？"
- **Policy implication:** "你的发现对中国的监管政策或行业实践有什么具体启示？"

### Chinese Lab or Group Meeting

Generate at least one question from each of the following:
- **Honest assessment:** "这个 negative result 你打算怎么解释？是方法问题还是数据问题？"
- **Next step:** "下一步你打算验证什么？有没有备选方案？"
- **Resource constraint:** "这个实验的计算成本或者数据获取成本会不会太高？"
- **Reproducibility:** "如果让组里另一个人复现这个结果，你觉得最容易出问题的环节是什么？"

### Chinese Defense-Style Presentation

Generate at least one question from each of the following:
- **Contribution boundary:** "你最重要的贡献是什么？为什么它不是显而易见的？"
- **Scope discipline:** "这部分工作是你独立完成的，还是和合作者一起做的？你的具体贡献在哪里？"
- **Robustness:** "为什么你没有做某某稳健性检验？是不是因为结果会不显著？"
- **External validity in China:** "你的样本来自[某地区/某数据库]，这个结论能推广到中国其他地区吗？"
- **Methodological justification:** "同样的研究问题，为什么不用[更常见的方法]而用[你的方法]？"

### Chinese Q&A tone guidance

In Chinese academic Q&A, questions may be more direct than in some Western settings, but directness does not necessarily mean hostility. The speaker should:
- Answer with calm confidence, not excessive humility or defensiveness.
- Use "这是一个很好的问题" to acknowledge the question, but do not overuse it.
- If the question exposes a real weakness, concede gracefully: "您说得对，这确实是一个限制，我们的回应是..."
- Avoid filibustering. Chinese committee members and senior researchers value concise, precise answers.

When no Chinese scenario is active, these extra questions are optional. The base Q&A categories remain the primary framework.
