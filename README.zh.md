# Research Talkcraft

一个以讲稿为核心的学术演讲排练 Skill。它读取现有幻灯片及配套材料，生成结构化的演讲排练包（Presentation Rehearsal Pack），包含有依据的逐页讲稿、critique、改进版讲稿、Q&A 预备以及时间控制建议。

Research Talkcraft 不生成、不修改、不重新设计幻灯片。它在固定材料的基础上优化口头叙事。

---

## 概述

学术演讲常常存在材料完成与口头表达效果之间的落差。幻灯片可能已制作完成，但口述内容却未针对听众、时间限制和可能的挑战进行校准。Research Talkcraft 通过将现有材料转化为可直接用于排练的标准化输出包，弥合这一落差。

该 Skill 提供两种运行模式：

- **`slides-only`**：适用于幻灯片内容自洽、足以支撑讲稿生成的场景。
- **`slides+context`**：适用于幻灯片内容较薄、需要额外材料（论文草稿、摘要、笔记、审稿意见）提供依据的场景。此模式同时支持幻灯片与配套材料之间的矛盾检测。

---

## 核心功能

- **逐页讲稿生成**：产出解释性口述内容，而非照读 bullet points。
- **听众感知的 critique**：针对三类听众画像（困惑的听众、领域专家、挑剔的审稿人）进行评估，采用稳定的评分维度（依据性、清晰度、听众适配、时间控制）。
- **改进版讲稿生成**：基于 critique 反馈生成优化后的讲稿。
- **可能遇到的 Q&A 预备**：预判听众问题并提供结构化回答思路。
- **时间控制**：估算每段口述时长，标记超时风险，识别可删减内容。附带确定性计时辅助脚本（`scripts/estimate_timing.py`），支持可配置的语速 profile 与复杂度修正系数。
- **矛盾检测**：识别幻灯片内容与配套材料之间的事实性不一致。

---

## 输出：演讲排练包

每次运行生成包含八个章节的标准化排练包：

1. **演讲简报** —— 演讲目的、听众画像、核心叙事弧线、沟通风险、建议语气、运行模式、不确定性标记。
2. **逐页讲稿** —— 每页幻灯片的口述内容，附过渡提示与估算时长。
3. **困惑与挑战点** —— 听众可能产生摩擦的结构化列表及应对策略。
4. **Critique 总结** —— 在依据性、清晰度、听众适配、时间控制等维度上的量化评估。
5. **改进版讲稿** —— 吸收 critique 建议后的优化版本。
6. **可能遇到的 Q&A** —— 预判问题及高质量回答思路。
7. **时间控制建议** —— 每段时长、超时风险及压缩策略。
8. **排练检查清单** —— 演讲前需核实的确认项。

---

## 安装

```bash
npx skills add <你的-github-用户名>/research-talkcraft
```

或手动安装，将 `research-talkcraft/` 复制到 agent 的 skills 目录：

```bash
# Claude Code
mkdir -p ~/.claude/skills/
cp -r research-talkcraft ~/.claude/skills/

# 项目本地
mkdir -p .claude/skills/
cp -r research-talkcraft .claude/skills/
```

---

## 使用示例

- "我有一个 20 分钟的研讨会幻灯片，帮我排练。"
- "帮我 critique 这份讲稿，听众是混 CS 和经济学背景的。"
- "我的幻灯片内容较薄，但我有论文草稿，生成一份排练包。"
- "我下周答辩，帮我准备可能的 Q&A 和时间风险点。"
- "把这些要点转成适合组会使用的中文口语表达。"

---

## 设计原则

- **先讲稿，后幻灯片**：在固定材料基础上优化口头叙事，不生成、不修改、不重新设计幻灯片。
- **用户可见的模式选择**：`slides-only` 与 `slides+context` 两种模式始终向用户明示，而非由 agent 静默选择。
- **单 agent 默认**：核心工作流是确定性的单 agent 流程。多 agent 强化为可选扩展，而非默认行为。
- **有依据的生成**：讲稿中的所有论断必须可追溯至提供的材料。当内容不足时，Skill 标记不确定性而非自行编造。
- **时间有界的现实性**：讲稿按实际口述时长校准，在时间压力下提供明确的压缩指导。

---

## 包内容

### 核心

| 文件 | 作用 |
|------|------|
| `SKILL.md` | 主工作流定义。规定运行模式（`slides-only` / `slides+context`）、七步核心工作流、输入处理规则与护栏。 |
| `references/script-output-template.md` | 八章节演讲排练包输出模板，规定每章节的必需内容。 |

### 场景剧本与听众画像

| 文件 | 作用 |
|------|------|
| `references/scenario-playbooks.md` | 常见演讲场景（研讨会、学术会议、组会、答辩、跨背景汇报）的校准参数。 |
| `references/audience-personas.md` | 三类听众画像（困惑的听众、领域专家、挑剔的审稿人），用于 critique 与 Q&A 生成。 |
| `references/qna-playbook.md` | 学术演讲常见提问类别及高质量回答的结构化指导。 |

### Critique 与修订

| 文件 | 作用 |
|------|------|
| `references/critique-rubric.md` | 八维度评分量表，用于评估讲稿草稿（依据性、清晰度、听众适配、时间控制等）。 |
| `references/revision-patterns.md` | 常见弱讲稿 → 强讲稿转换模式目录，附前后对比指导。 |

### 范例

| 文件 | 作用 |
|------|------|
| `references/exemplars.md` | 指向各学科与场景范例文件的索引。 |
| `references/exemplars/*.md` | 跨学科（CS/ML、金融/经济、神经科学、社会科学）与跨场景（研讨会、答辩、组会、跨背景汇报）的弱版与改进版讲稿示例。 |

### 可选扩展

| 文件 | 作用 |
|------|------|
| `references/multi-agent-rehearsal-contract.md` | 可选 `v1A` 多 agent 强化排练模式的契约。 |
| `references/multi-agent-workflow.md` | 多 agent 排练的分步工作流。 |
| `references/multi-agent-personas.md` | 多 agent 模拟中的角色定义。 |
| `references/overlay-contract.md` | 学科专属叠加层（`v1B`）的契约。 |
| `references/overlays/*.md` | 学科专属校准（金融、CS 组会、重答辩场景）。 |
| `references/contradiction-contract.md` | 幻灯片与配套材料间矛盾检测（`v2A`）的契约。 |
| `references/contradiction-taxonomy.md` | 矛盾类型分类学。 |
| `references/contradiction-reconciliation-rules.md` | 检测到的矛盾的消解规则。 |
| `references/exemplar-contract.md` | 范例层（`v3A`）的治理契约。 |
| `references/timing-tool-contract.md` | 确定性计时辅助工具（`v4A`）的契约。 |
| `references/timing-model.md` | 语速 profile 与复杂度修正系数。 |
| `references/non-english-support-contract.md` | 中文学术演讲支持（`v5A`）的范围契约。 |

### 脚本与验证

| 文件 | 作用 |
|------|------|
| `scripts/estimate_timing.py` | 确定性计时估算器，支持可配置语速 profile 与复杂度修正。 |
| `references/capability-matrix.md` | 8 模块共 29 项能力的统一清单。 |
| `references/benchmark-set.md` | 25 个基准案例及场景映射与价值评级。 |
| `references/distilled-assets-index.md` | 全部 29 份参考文件的索引清单。 |
| `STOP_LINE.md` | 明确的范围边界与非目标。 |

---

## 验证

- **25 个基准案例**：覆盖真实与合成场景，包含高价值与低价值案例、学科叠加、矛盾检测、时间压力及中文语言支持。
- **能力矩阵**：记录 8 个模块共 29 项能力，标注来源版本、默认状态、适用场景及已知边界。
- **停止线**：记录明确的非目标，防止范围蔓延。

关键文档：[能力矩阵](research-talkcraft/references/capability-matrix.md) | [基准集](research-talkcraft/references/benchmark-set.md) | [停止线](research-talkcraft/STOP_LINE.md)

---

## 许可证

MIT