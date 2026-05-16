# Non-English Support Contract

This document defines the stable contract for non-English support in `research-talkcraft`. It specifies what the Skill promises, what it does not promise, and when Chinese-specific references should be consulted.

## What "Non-English Support" Means

Non-English support in `research-talkcraft` means:

1. **Language-matched output.** When the user's talk is in Chinese, the Skill produces Chinese-language scripts, critiques, and Q&A guidance.
2. **Culturally calibrated references.** Chinese academic presentations have distinct norms for contribution framing, transition style, directness of challenge, and pacing. The Skill consults Chinese-specific references to calibrate these dimensions.
3. **Technical accuracy preservation.** If the source material is in English but the talk is in Chinese, the Skill preserves technical accuracy while rewriting for natural spoken Chinese.

## What Is Promised (v5A)

- Chinese-language exemplars for common research presentation scenarios.
- Chinese-oriented critique calibration (e.g., unnatural translated transitions, overly formal wording).
- Chinese audience personas and scenario playbooks.
- Chinese-specific Q&A patterns for seminar and defense contexts.
- Clear fallback to English/general references when Chinese references are not applicable.

## What Is Not Promised

- **Full multilingual equivalence.** v5A starts with Chinese only. Support for other languages is not guaranteed.
- **Automatic translation.** The Skill does not translate an English deck into a polished Chinese script verbatim. It rewrites for spoken Chinese, which involves restructuring, not just word substitution.
- **Locale-specific etiquette for every institution.** The playbooks cover general Chinese academic norms, not the customs of every individual university or lab.
- **Bilingual code-switching.** The Skill does not optimize for talks that mix English and Chinese extensively. It assumes a primary talk language.

## When to Use Chinese References

The Skill should consult Chinese references when **all** of the following are true:

1. The user explicitly states the talk will be delivered in Chinese.
2. The audience is a Chinese academic setting (seminar, lab meeting, defense).
3. The user has not requested English-only output.

If the talk is in English — even if the speaker is Chinese or the institution is in China — the Skill uses the default English/general references. Chinese references are for Chinese-language talks, not for Chinese speakers giving English talks.

## Fallback Rules

- If a Chinese-specific reference does not exist for a given scenario, fall back to the general English reference.
- If the user requests a language that is not Chinese and not English, fall back to English/general references and note the limitation.
- If the source material is in English and the talk is in Chinese, the Skill must preserve technical terms accurately while making the surrounding prose natural in Chinese. Do not force-translate established technical terms that are commonly left in English.

## Integration Points

Chinese references are integrated at these points in the workflow:

1. **Presentation Brief** — Use Chinese playbook audience assumptions and tone guidance.
2. **Script drafting** — Consult Chinese exemplars for natural spoken Chinese structure.
3. **Critique** — Apply Chinese-specific critique rules (e.g., unnatural transitions, over-formality).
4. **Revision** — Apply Chinese revision patterns for contribution framing and signposting.
5. **Q&A** — Use Chinese seminar/defense Q&A patterns where relevant.

## Strict Non-Goals

1. **No machine translation pipeline.** Output is rewritten, not translated.
2. **No bilingual optimization.** The Skill assumes a single primary talk language.
3. **No cultural generalization beyond academic settings.** Playbooks cover seminars, lab meetings, and defenses, not business or public speaking contexts.
