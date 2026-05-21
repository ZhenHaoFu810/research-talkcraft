# Research Talkcraft

一个学术演讲排练 Skill。它读取幻灯片及配套材料，生成逐页讲稿、critique、改进版、Q&A 预备和时间建议。

它不生成、不修改、不重新设计幻灯片。它在现有材料的基础上优化口述内容。

---

## 功能

Research Talkcraft 将现有材料转化为可直接排练的输出。你提供幻灯片，可选择性附加论文草稿、摘要或笔记；它返回完整的 **演讲排练包**。

该 Skill 提供两种运行模式：

- **`slides-only`** —— 幻灯片内容自洽，足以支撑讲稿生成。
- **`slides+context`** —— 幻灯片内容较薄，需要额外材料（论文草稿、摘要、笔记、审稿意见）提供依据。此模式同时检测幻灯片与配套材料之间的矛盾。

### 核心能力

- **逐页讲稿生成** —— 生成解释性口述内容，而非照读 bullet points。
- **Critique** —— 从三类听众画像（困惑的听众、领域专家、挑剔的审稿人）评估讲稿。
- **改进版讲稿** —— 基于 critique 反馈生成优化版本。
- **Q&A 预备** —— 预判听众问题并提供回答思路。
- **时间控制** —— 估算每段口述时长，标记超时风险，识别可删减内容。附带确定性计时脚本（`scripts/estimate_timing.py`），支持配置语速参数。
- **矛盾检测** —— 识别幻灯片内容与配套材料之间的事实性不一致。

### 演讲排练包

输出包含八个部分：

1. **简报** —— 听众画像、核心叙事弧线、沟通风险、语气建议。
2. **讲稿** —— 每页幻灯片的口述内容，附过渡提示与估算时长。
3. **卡点** —— 听众可能困惑的位置及应对方式。
4. **Critique 总结** —— 依据性、清晰度、听众适配、时间控制四个维度的量化评估。
5. **改进版讲稿** —— 吸收 critique 后的优化版本。
6. **可能遇到的 Q&A** —— 预判问题及回答思路。
7. **时间建议** —— 每段时长、超时风险、压缩策略。
8. **检查清单** —— 演讲前需核实的确认项。

---

## 安装

```bash
npx skills add ZhenHaoFu810/research-talkcraft
```

或手动复制到 agent 的 skills 目录：

```bash
# Claude Code
mkdir -p ~/.claude/skills/
cp -r research-talkcraft ~/.claude/skills/

# 项目本地
mkdir -p .claude/skills/
cp -r research-talkcraft .claude/skills/
```

---

## 使用

Skill 在提及排练、讲稿或 critique 时自动触发。示例：

- "我有一个 20 分钟的研讨会幻灯片，帮我排练。"
- "帮我 critique 这份讲稿，听众是混 CS 和经济学背景的。"
- "我的幻灯片内容较薄，但我有论文草稿，生成一份排练包。"
- "我下周答辩，帮我准备可能的 Q&A 和时间陷阱。"
- "把这些要点转成适合组会使用的中文口语表达。"

---

## 设计原则

- **先讲稿，后幻灯片。** 在固定材料基础上优化口述内容，不动幻灯片设计。
- **模式由用户选择。** `slides-only` 与 `slides+context` 始终明示给用户，不由 agent 静默选择。
- **默认单 agent。** 核心流程是确定性的单 agent 流程。多 agent 强化为可选扩展。
- **有依据，不编造。** 讲稿中的所有论断必须可追溯至提供的材料。内容不足时，Skill 标记不确定性而非自行填补。
- **时间有界。** 20 分钟 slot 讲了 35 分钟，就是失败的讲稿。压缩策略内置。

---

## 包内容

### 核心

- **`SKILL.md`** —— 主工作流定义：运行模式、七步核心流程、输入处理规则、护栏。
- **`references/script-output-template.md`** —— 八部分演讲排练包的输出模板。

### 场景与听众

- **`references/scenario-playbooks.md`** —— 常见演讲场景（研讨会、学术会议、组会、答辩、跨背景汇报）的语气与深度校准。
- **`references/audience-personas.md`** —— 三类听众画像，用于 critique 和 Q&A：困惑的听众、领域专家、挑剔的审稿人。
- **`references/qna-playbook.md`** —— 常见问题类型及高质量回答的结构化指导。

### Critique 与修订

- **`references/critique-rubric.md`** —— 八维度评分量表（依据性、清晰度、听众适配、时间控制等）。
- **`references/revision-patterns.md`** —— 弱讲稿到强讲稿的转换模式，附前后对比。

### 范例

- **`references/exemplars.md`** —— 各学科与场景范例文件的索引。
- **`references/exemplars/*.md`** —— 具体示例，覆盖 CS/ML、金融/经济、神经科学、社会科学等学科，以及研讨会、答辩、组会、跨背景汇报等场景。

### 可选扩展

- **`references/multi-agent-rehearsal-contract.md`** —— 多 agent 强化排练模式定义。
- **`references/multi-agent-workflow.md`** —— 多 agent 排练的具体流程。
- **`references/multi-agent-personas.md`** —— 多 agent 模拟的角色定义。
- **`references/overlay-contract.md`** —— 学科专属叠加层定义。
- **`references/overlays/*.md`** —— 学科专属校准（金融、CS 组会、重答辩场景）。
- **`references/contradiction-contract.md`** —— 矛盾检测规则。
- **`references/contradiction-taxonomy.md`** —— 矛盾类型分类。
- **`references/contradiction-reconciliation-rules.md`** —— 矛盾消解规则。
- **`references/exemplar-contract.md`** —— 范例层治理说明。
- **`references/timing-tool-contract.md`** —— 计时辅助工具配置。
- **`references/timing-model.md`** —— 语速 profile 和复杂度修正。
- **`references/non-english-support-contract.md`** —— 中文学术演讲支持范围说明。

### 脚本与验证

- **`scripts/estimate_timing.py`** —— 确定性计时估算器，支持配置语速参数。
- **`references/capability-matrix.md`** —— 8 模块共 29 项能力的清单。
- **`references/benchmark-set.md`** —— 25 个基准案例及场景映射。
- **`references/distilled-assets-index.md`** —— 全部参考文件的索引。
- **`STOP_LINE.md`** —— 明确的范围边界和非目标。

---

## 验证

项目用 25 个基准案例做了验证，覆盖真实与合成场景，包括学科叠加、矛盾检测、时间压力和中文语言支持。能力矩阵记录了 8 个模块共 29 项能力，停止线则记下了明确的非目标，防止范围蔓延。

关键文档：[能力矩阵](research-talkcraft/references/capability-matrix.md) | [基准集](research-talkcraft/references/benchmark-set.md) | [停止线](research-talkcraft/STOP_LINE.md)

---

## 许可证

MIT