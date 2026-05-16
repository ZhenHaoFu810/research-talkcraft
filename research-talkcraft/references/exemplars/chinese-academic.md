# Chinese Academic Presentation Exemplars

These exemplars illustrate common weak-to-strong transformations specifically for Chinese academic research presentations. They are not literal translations of English exemplars; they capture patterns that arise when speakers write scripts for Chinese-speaking academic audiences.

---

## Exemplar 1: Seminar Motivation — From Vague Background to Clear Stakes

**Scenario:** Chinese university department seminar  
**Domain:** Economics / Finance  
**Audience:** Mixed faculty and graduate students, some familiar with the sub-topic, others not  
**Input material type:** Opening motivation slide with three bullets

### Slide content summary
- Title: "研究背景"
- Bullets:
  - 宏观审慎政策受到广泛关注
  - 银行风险承担行为存在争议
  - 现有研究缺乏因果识别

### Weak script
"宏观审慎政策受到广泛关注。银行风险承担行为存在争议。现有研究缺乏因果识别。因此，我们研究了宏观审慎政策对银行风险承担的影响。"

### Critique
- Pure bullet reading with no spoken hook. The audience has already read the slide.
- No explanation of why the controversy matters or what is at stake.
- The phrase "存在争议" is overused in Chinese academic talks and sounds generic.
- No transition into the speaker's specific contribution.

### Improved script
"过去十几年，各国监管部门出台了一系列宏观审慎工具，目的是抑制信贷周期、降低系统性风险。但有一个问题一直没有得到很好回答：这些政策真的减少了银行的风险承担，还是只是把风险转移到了监管较少的影子银行？要回答这个问题很难，因为政策变化不是随机分配的——你不能随机决定哪些银行受监管、哪些不受。所以现有的研究大多只能描述相关性，缺乏干净的因果识别。我们这篇文章试图利用西班牙的一个自然实验，来给出因果证据。"

### Why the revision works
- Opens with a concrete policy context instead of abstract "广泛关注."
- Poses a tension (risk reduction vs. risk displacement) that creates narrative stakes.
- Explains why causal identification is hard, rather than just stating that it is lacking.
- Sets up the speaker's specific contribution (Spanish natural experiment) naturally.

---

## Exemplar 2: Lab Meeting Methods — From Jargon Dump to Audience-Oriented Intuition

**Scenario:** Chinese lab group meeting  
**Domain:** Computer Science / Machine Learning  
**Audience:** Lab members who know deep learning basics but not this specific method  
**Input material type:** Methods slide with technical details

### Slide content summary
- Title: "模型架构"
- Bullets:
  - 使用Transformer，12层，8头注意力
  - 隐藏层维度256，dropout 0.1
  - 训练100轮，Adam优化器，学习率1e-4

### Weak script
"我们使用Transformer，12层，8头注意力。隐藏层维度256，dropout 0.1。训练100轮，使用Adam优化器，学习率1e-4。"

### Critique
- Reads every hyperparameter without explaining why any of them matter.
- The listener knows what a Transformer is but not why these specific choices were made.
- Sounds like reading a configuration file, not explaining a design decision.
- No connection to the problem the method is solving.

### Improved script
"我们用的是标准Transformer，但有一个关键的设计选择：我们故意把模型压得比较小——12层、256维。为什么不放大？因为我们要在边缘设备上实时运行，比如手机端的语音识别。模型大了确实准确率会高一点，但推理 latency 受不了。所以我们用轻量级的架构，在准确率和速度之间找一个能部署的平衡点。训练方面就是常规设置，Adam、cosine decay，100轮收敛。"

### Why the revision works
- Leads with the design constraint (edge deployment) rather than the architecture name.
- Explains the tradeoff (accuracy vs. latency) in terms the lab cares about.
- Defers routine training details to a brief closing sentence.
- Uses "压得比较小" and "受不了" — spoken Chinese that sounds natural in a lab meeting, not written-formal.

---

## Exemplar 3: Defense-Style Contribution Framing — From Overclaiming to Defensible Boundaries

**Scenario:** Chinese doctoral thesis defense  
**Domain:** Neuroscience  
**Audience:** Committee members evaluating originality and scope  
**Input material type:** Contribution slide

### Slide content summary
- Title: "本文贡献"
- Bullets:
  - 首次揭示了某神经通路与决策行为的因果关系
  - 提出了全新的理论框架
  - 方法具有普适性

### Weak script
"本文首次揭示了某神经通路与决策行为的因果关系。我们提出了全新的理论框架。该方法具有普适性，可以应用到其他领域。"

### Critique
- "首次揭示" is a strong claim that may not be defensible. Defenses in Chinese settings often use "首次" too liberally.
- "全新的理论框架" overstates contribution size. Committees are sensitive to this.
- "普适性" is vague and invites challenge. Which other domains? Under what conditions?
- No acknowledgment of boundary conditions or limitations.

### Improved script
"在这项工作中，我们聚焦一个具体的问题：在风险决策任务中，前额叶皮层到纹状体的神经通路如何调控选择行为。利用光遗传学和纤维光度记录，我们发现激活这条通路会系统性改变动物对高风险选项的偏好。需要强调的是，这个结论目前仅限于我们使用的任务范式和小鼠模型，是否能推广到灵长类或者其他决策场景，还需要后续研究。至于方法层面，我们建立的光遗传-行为整合流程，理论上可以迁移到其他神经环路的研究中，但具体的可行性取决于目标脑区的解剖可达性。"

### Why the revision works
- Replaces "首次揭示" with a concrete, bounded finding ("激活这条通路会改变偏好").
- Explicitly states scope boundaries (mouse model, specific task) before the committee asks.
- Replaces "普适性" with a qualified, operational statement about method transferability.
- Sounds confident but not overconfident — exactly the tone a defense committee expects.

---

## Exemplar 4: Transition and Signposting — From Abrupt Jumps to Narrative Bridges

**Scenario:** Chinese academic seminar  
**Domain:** Social Science / Public Policy  
**Audience:** Mixed faculty and graduate students  
**Input material type:** Transition between background and methods

### Weak script
"以上就是文献综述的内容。下面介绍研究方法。"

### Critique
- Extremely abrupt. Sounds like a slide-change announcement, not a narrative bridge.
- Common in Chinese talks because speakers mimic written-section headers in speech.
- Gives the audience no reason to care about the upcoming methods section.

### Improved script
"前面我们看了，现有文献主要用相关性方法来估计政策效果，但因果识别一直是个难题。那要解决这个问题，我们得换一个思路——利用政策实施中的断点来构造一个准自然实验。接下来我就介绍一下这个识别策略是怎么设计的，以及为什么它能帮我们回答前面提出的那个问题。"

### Why the revision works
- Recaps the problem from the previous section (causal identification is hard).
- Previews the solution approach (regression discontinuity / quasi-experiment).
- Connects the methods section back to the motivating question.
- Uses spoken Chinese节奏 ("那要解决这个问题，我们得换一个思路") rather than written-section headers.

---

## Common Patterns Across Chinese Academic Talks

### Pattern: Over-formality from written prose
Chinese academic speakers often write scripts that sound like paper abstracts — full of "本文"、"研究表明"、"具有重要的理论和实践意义." These phrases feel natural in writing but stiff in speech.

**Fix:** Replace with spoken equivalents. "本文发现" → "我们发现"; "具有重要的意义" → "这意味着什么？"; "基于以上分析" → "所以回过头来看."

### Pattern: Literal bullet reading
Because Chinese slides often use parallel grammatical structures (动宾短语 lists), speakers read them verbatim, creating a mechanical rhythm.

**Fix:** Break the parallel structure. Turn the bullet list into a spoken argument with cause-and-effect logic.

### Pattern: Weak contribution framing with "填补空白"
Chinese talks often frame contributions as "填补了研究空白" without specifying what空白, why it matters, or who cares.

**Fix:** Replace with a concrete tension or puzzle. "Previous work assumed X; we relax X and show Y changes."

### Pattern: Transitions that announce rather than bridge
"下面进入第二部分" is common but adds no narrative value.

**Fix:** Use recap-and-preview bridges. "So the core problem is X. The natural next question is Y."
