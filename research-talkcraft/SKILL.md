# SKILL: Research Talkcraft

## Metadata

- **Name:** Research Talkcraft
- **Description:** A rehearsal and script optimization Skill for research presentations. Accepts existing slides and optional supporting materials, then produces a structured Presentation Rehearsal Pack: a grounded, audience-aware speaker script with critique, revision, likely Q&A, and rehearsal guidance. The Skill does not generate, rewrite, or redesign slides.
- **Default target:** General research presentations (seminars, conferences, thesis defenses, lab meetings, mixed-background updates).
- **Modes:** `slides-only` and `slides+context`.
- **Output:** Presentation Rehearsal Pack.

---

## What This Skill Does

1. Reads your existing presentation materials.
2. Infers or confirms talk context (audience, duration, goals).
3. Builds a concise Presentation Brief.
4. Drafts a first-pass spoken script slide-by-slide or section-by-section.
5. Critiques the draft against a stable rubric.
6. Revises the script into a rehearsal-ready version.
7. Produces a full Presentation Rehearsal Pack.

---

## What This Skill Does Not Do

- It does **not** generate, rewrite, or redesign slides.
- It does **not** coach voice, pace, filler words, or body language.
- It does **not** run mandatory multi-agent loops.
- It does **not** invent unsupported facts or claims.
- It does **not** turn into a paper-summary engine.

---

## Accepted Inputs

- Slides (PPTX, PDF, images, OCR text, or pasted text)
- Paper drafts, abstracts, extended summaries
- Speaker notes or outlines
- Reviewer comments
- Talk goals and intended takeaways

---

## Operating Modes

The Skill runs in one of two modes. The mode must be visible in reasoning and output.

### `slides-only`
- **When to use:** The deck contains enough content; you want a fast first-pass rehearsal pack; you do not want the Skill to read a large supporting corpus.
- **Behavior:** The Skill reads only the slide content and the explicit user context. It builds the script and critique from the deck alone.
- **Limitation flag:** If the deck is too sparse to generate a confident script, the Skill must surface an uncertainty warning and recommend switching to `slides+context`.

### `slides+context`
- **When to use:** You want stronger grounding, richer explanations, or better defense readiness; you have a paper, draft, notes, or other supporting text.
- **Behavior:** The Skill actively reads supporting materials alongside the deck. It uses them to recover the research question, contribution framing, method intuition, result interpretation, and likely limitations.
- **Priority order when multiple supports are provided:**
  1. Abstract or intended takeaways (highest priority — gives framing)
  2. Paper draft or extended summary (recovers logic and detail)
  3. Speaker notes or outline (recovers intended emphasis)
  4. Reviewer comments (surfaces likely challenges)
- **Guardrail:** Do not over-import irrelevant details. Stay centered on the spoken presentation, not a paper summary.

---

## Core Workflow (Single-Agent Default)

### Step 1: Parse Presentation Context
Before reading materials, infer or request:
- Presentation type (seminar, conference, lab meeting, thesis defense, mixed-background update)
- Audience profile (knowledge level, mixed backgrounds, domain experts, reviewers)
- Target duration and language
- Speaker goal (inform, persuade, defend, recruit feedback)
- Whether slides are fixed
- Whether Q&A preparation is needed
- Operating mode: `slides-only` or `slides+context`

### Step 2: Read Available Materials
- In `slides-only`: read the deck only.
- In `slides+context`: read the deck plus supporting materials in the priority order above.
- Identify the central claim or question, the logic of the talk, and the role of each slide/section.
- Flag missing information that may limit script quality.

**Contradiction scan (slides+context only):**
After reading both deck and supporting materials, run a structured contradiction scan:
1. Compare explicit claims across sources using `references/contradiction-taxonomy.md`.
2. Classify each discrepancy by type and severity using `references/contradiction-reconciliation-rules.md`.
3. Distinguish true contradictions from benign differences (version drift, extra detail, presentational compression).
4. Produce a Contradiction Report if any true contradictions are found.
5. For High-severity contradictions, escalate to the user and refuse to state the disputed claim until resolved.
6. For Medium and Low contradictions, surface them in the pack and propose reconciliation.

The scan runs automatically in `slides+context` mode. It does not run in `slides-only` mode.

**Missing-context behavior:**
- If information is absent, state the gap explicitly rather than hallucinating.
- If slides conflict with supporting text, note the conflict and prefer the deck as the rehearsal anchor unless the user specifies otherwise.
- If the deck appears too sparse for confident script generation, emit an uncertainty warning.

### Step 3: Build a Presentation Brief
Before drafting the script, produce a brief summary:
- Likely purpose of the talk
- Target audience knowledge level
- Core narrative arc
- Likely communication risks
- Recommended tone and depth
- Chosen operating mode

This brief gives the user an inspectable framing layer before the full script.

### Step 4: Draft the Initial Script
- Draft slide-by-slide or section-by-section.
- Use spoken language, not written-paper prose.
- **Do not read bullets verbatim.** Explain the idea behind the bullet.
- Preserve factual discipline: do not hallucinate unsupported claims.
- Do not assume audience knowledge that was never specified.
- Keep the script grounded in the actual materials.

### Step 5: Critique the Draft
Critique the initial script using the dimensions in `references/critique-rubric.md`:
- Groundedness
- Clarity
- Audience fit
- Non-redundancy
- Technical precision
- Narrative flow
- Timing fit
- Defense readiness

Turn findings into actionable revision guidance.

### Step 6: Revise Into a Rehearsal-Ready Script
Produce a revised script that is:
- Clearer and better paced
- More audience-aligned
- More resilient to confusion and challenge
- More usable in real rehearsal

Apply patterns from `references/revision-patterns.md`.

### Step 7: Produce the Presentation Rehearsal Pack
Assemble the final output following `references/script-output-template.md`.

---

## Lightweight Timing Helper (v4A)

The Skill may use `scripts/estimate_timing.py` to sharpen timing estimates when a structured script exists and a target duration is known. This is a **deterministic, zero-dependency helper**, not a mandatory step.

### When to invoke the timing helper

- A sectioned script exists (slide-by-slide or section-by-section).
- The user has provided a target duration.
- The script can be run (Python is available).

### When to fall back to the heuristic

- The script is not yet sectioned.
- The target duration is unknown.
- Python is unavailable or the script fails.
- The input is sparse or unscripted (e.g., bullet lists only).

In fallback mode, use the coarse heuristic: **120–150 spoken words per minute** for technical content, adjusted downward for dense notation or non-native speakers.

### What the helper produces

- Per-section word count and estimated duration.
- Effective WPM per section, adjusted for complexity (equations, jargon, numbers, transitions, Q&A).
- Budget comparison against the target duration.
- Overrun risk ranking — sections most likely to exceed their fair-share time.
- Cut-for-time candidates — compressible non-critical sections.

The output is **advisory**. The user decides what to cut.

### Integration into the pack

When the timing helper runs, include its output in **Section 7 (Time-Control Guidance)** of the Presentation Rehearsal Pack. When it does not run, Section 7 falls back to the heuristic estimates and still provides budget comparison, overrun flags, and cut suggestions.

---

## Timing and Compression Guidance

- Estimate per-slide or per-section speaking time based on word count and complexity.
- Flag sections likely to exceed their time budget.
- Provide concise `cut-for-time` suggestions when timing pressure is detected.
- If the user provides a total duration, allocate time proportionally across sections and highlight overruns.
- Prefer the v4A timing helper when available; fall back to the 120–150 WPM heuristic otherwise.

---

## Optional Post-Draft Intensification Hook

After the initial Presentation Rehearsal Pack is delivered, the user may optionally request a deeper rehearsal pass. This is **not** the default.

Optional intensification paths:
- **Audience stress test:** Simulate the Confused Listener persona to find unclear explanations.
- **Expert challenge round:** Simulate the Domain Expert persona to find under-explained technical depth.
- **Skeptical reviewer round:** Simulate the Skeptical Reviewer persona to find weak claims and unsupported framing.
- **Revision pass 2:** Produce a second revised script addressing the new critique.

These paths use the personas in `references/audience-personas.md` within a single-agent critique loop. They do not require a full multi-agent implementation in `v0`.

---

## Optional Multi-Agent Rehearsal Mode (v1A)

This is an **optional, user-invoked** intensification layer that runs after the default `v0` Presentation Rehearsal Pack exists. It is **not** the default path.

### When to use

Activate multi-agent rehearsal only when:

- A complete Presentation Rehearsal Pack (or at minimum a revised script + brief + timing target) already exists.
- The user explicitly requests a deeper pass using trigger language such as:
  - "Stress test this talk"
  - "Run a skeptical review"
  - "Simulate audience disagreement"
  - "Give me a second-pass rehearsal round"
  - "Intensify the critique"

If prerequisites are missing, decline and guide the user through the default `v0` workflow first.

### Preflight check (warn, do not block)

Before launching the multi-agent workflow, assess the existing `v0` pack quality:

1. Check the Critique Summary. If it scores **Strong** on Groundedness, Defense Readiness, and Technical Precision, or contains **0 High-severity and ≤2 Medium-severity findings**, warn the user:
   > "Your default pack is already strong. Multi-agent rehearsal may add only minor polish. Do you still want to proceed?"

2. If the user says no, stop and return to the default pack.
3. If the user says yes (or any affirmative), proceed with the full workflow and report results honestly—including an empty Revision Pass 2 if that is what occurs.

This check is a **suggestion, not a gate.** The user may override it.

### Cost and latency warning

The Skill must warn the user that multi-agent rehearsal is:

- **More expensive** — it consumes significantly more tokens than the default single-agent pack.
- **Slower** — it requires three sequential critique passes plus synthesis.
- **Optional** — the default `v0` pack is sufficient for most talks. This mode is for high-stakes presentations or speakers who want extra confidence.

### Workflow sequence

1. **Validate prerequisites + run preflight** — confirm existing pack, audience profile, and timing target. Run the preflight quality check. Warn if the pack is already Strong; proceed only if the user confirms.
2. **Agent 1: Confused Listener critique** — clarity breakdowns, unexplained jargon, abrupt transitions, missing motivation.
3. **Agent 2: Domain Expert critique** — imprecision, unsupported novelty, missing related work, under-explained method choices.
4. **Agent 3: Skeptical Reviewer critique** — overconfident claims, missing limitations, untested robustness, alternative explanations.
5. **Synthesis** — merge, deduplicate, rank, and resolve disagreements using `references/critique-priority-rules.md`.
6. **Revision Pass 2** — update only the segments tied to ranked issues; mark changes with annotations.
7. **Output** — append the `Rehearsal Intensification Output` to the existing pack.

### Boundaries

- **Maximum agent passes:** 3 (one per persona).
- **Maximum synthesis passes:** 1.
- **Maximum revision passes:** 1 (Revision Pass 2).
- **No recursion:** Revision Pass 2 is not fed back into the agents.
- **No expansion:** Only the three defined personas are used in `v1A`.
- **No slide editing:** The mode critiques and revises the script only.

### Output format

Follow `references/rehearsal-pass-2-template.md`. The output includes:
1. Persona-by-persona critiques
2. Disagreement map
3. Merged priority list
4. Revision Pass 2 (annotated)
5. Residual risks

Append this output after Section 8 of the original `Presentation Rehearsal Pack`.

### Reference files for v1A

- `references/multi-agent-rehearsal-contract.md` — invocation rules and non-goals
- `references/multi-agent-personas.md` — agent role definitions
- `references/multi-agent-workflow.md` — interaction pattern and loop boundaries
- `references/critique-priority-rules.md` — ranking, filtering, and conflict resolution
- `references/rehearsal-pass-2-template.md` — output structure

---

## Optional Discipline-Specific Overlays (v1B)

Overlays are **optional calibration layers** that sharpen the base general-research workflow for specific disciplines or high-stakes settings. They do not change the core workflow, pack structure, or grounding rules.

### When to apply an overlay

Activate an overlay when:

- The user explicitly requests one using trigger language such as:
  - "This is a finance seminar"
  - "Treat this like a CS group meeting"
  - "Prepare me for a defense-style audience"
  - "Apply the finance overlay"

- Or the Skill infers one with **high confidence** from the materials or context and **proposes it for confirmation.** The user must explicitly accept before the overlay is applied.

If inference is uncertain, default to the base general-research mode. Do not silently apply an overlay.

### What overlays change

- **Audience assumptions** — what knowledge is safe to assume.
- **Tone and depth calibration** — formality, pacing, technical depth per section.
- **Likely challenge patterns** — what pushback is common in this setting.
- **Q&A emphasis** — which question categories are most important.
- **Revision priorities** — which critique dimensions get extra weight.

### What overlays do not change

- Core pack structure and required sections.
- Grounding rules and hallucination guardrails.
- Single-agent default path.
- v1A contract and preflight check.

### Available overlays in v1B

- `references/overlays/finance-academic-talk.md` — identification, economic magnitude, causal language discipline.
- `references/overlays/cs-group-meeting.md` — baseline specificity, ablations, compute tradeoffs, reproducibility.
- `references/overlays/defense-heavy-talk.md` — contribution boundaries, methodological justification, scope discipline.

### Fallback behavior

If the user requests an overlay that does not exist, state that it is unavailable and offer the closest available overlay or the base mode.

If the user declines a proposed overlay, proceed with the base general-research mode using `references/scenario-playbooks.md`.

---

## Exemplar Consultation (v3A)

Exemplars are **concrete reference illustrations** of weak and improved script segments across domains, audiences, and failure modes. They anchor quality judgments during critique and revision.

### When to consult exemplars

The Skill should consult exemplars during:
- **Critique:** When a script segment matches a known failure pattern (bullet reading, overclaiming, missing intuition, etc.).
- **Revision:** When applying a transformation from `references/revision-patterns.md`; match the weakness to the relevant exemplar category.
- **Q&A generation:** Use exemplar scenarios as inspiration for likely audience questions.

### How to consult exemplars (lightweight)

1. Identify the weakness type from the script.
2. Match it to the relevant exemplar category:
   - Domain: `references/exemplars/cs-ml.md`, `finance-econ.md`, `neuroscience.md`, `social-science.md`
   - Audience: `references/exemplars/seminar-style.md`, `defense-style.md`, `group-meeting.md`, `mixed-background.md`
   - Language: `references/exemplars/chinese-academic.md` — Chinese academic presentations
   - Failure mode: `references/exemplars/failure-modes.md`
3. Apply the transformation principle, not the domain-specific wording.
4. Do not load the full collection for every script. Consult only the categories relevant to the current talk.

### Quality check

After revising, ask: "Does the improved script follow the same principle as the exemplar's improved version?" If not, re-examine the transformation.

---

## Non-English Support (v5A)

The Skill supports Chinese-language research presentations through a bounded reference layer. It does not translate verbatim; it rewrites for spoken Chinese while preserving technical accuracy.

### When to use Chinese references

Consult Chinese references when **all** of the following are true:

1. The user explicitly states the talk will be delivered in Chinese.
2. The audience is a Chinese academic setting (seminar, lab meeting, defense).
3. The user has not requested English-only output.

If the talk is in English — even if the speaker is Chinese or the institution is in China — use the default English/general references. Chinese references are for Chinese-language talks, not for Chinese speakers giving English talks.

### Language choice rules

- **Talk language drives output language.** If the talk is in Chinese, the script, critique, Q&A, and rehearsal guidance should be in Chinese.
- **Source material language does not dictate talk language.** If the deck or paper is in English but the talk is in Chinese, preserve technical accuracy while rewriting for natural spoken Chinese.
- **Technical terms:** Do not force-translate established technical terms that are commonly left in English (e.g., "transformer"、"ablation"、"regression discontinuity"). Use the form that is standard in the speaker's field.

### What Chinese references provide

- **Scenario playbooks** — `references/scenario-playbooks.md` (Chinese Academic Seminar, Chinese Lab/Group Meeting, Chinese Defense-Style Presentation).
- **Audience personas** — `references/audience-personas.md` (Chinese research setting variations).
- **Exemplars** — `references/exemplars/chinese-academic.md` (weak and improved Chinese script segments).
- **Revision patterns** — `references/revision-patterns.md` (Chinese-specific patterns C1–C5).
- **Critique emphasis** — `references/critique-rubric.md` (Chinese-specific elevated critiques).
- **Q&A patterns** — `references/qna-playbook.md` (Chinese seminar, lab meeting, and defense questions).

### Fallback rules

- If a Chinese-specific reference does not exist for a given scenario, fall back to the general English reference.
- If the user requests a language that is not Chinese and not English, fall back to English/general references and note the limitation.
- The default English path must work without loading unnecessary Chinese references.

### Contract

See `references/non-english-support-contract.md` for the full contract, including strict non-goals (no machine translation pipeline, no bilingual optimization, no cultural generalization beyond academic settings).

---

## Out-of-Scope Rules (Strict)

- **No slide redesign by default.** Do not suggest new slide layouts, colors, or visual restructuring unless the user explicitly asks for slide-feedback mode.
- **No delivery coaching.** Do not evaluate voice, pace, filler words, or body language.
- **No mandatory multi-agent loop.** Multi-agent rehearsal is optional and user-invoked.
- **No unsupported factual invention.** Every claim in the script must be traceable to the provided materials. Flag uncertainty when grounding is weak.

---

## Quality Bar

A successful output is one the user can actually rehearse with. The script should:
- Explain the slide rather than read it
- Preserve factual discipline
- Adapt detail to the audience
- Provide clean transitions
- Surface vulnerable points
- Help the user rehearse under realistic time constraints
