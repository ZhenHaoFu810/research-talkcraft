# Timing Model

This document specifies the deterministic timing model used by `scripts/estimate_timing.py`.

## Base Assumption

**Default pace:** 130 words per minute (WPM).

This is the midpoint of the 120–150 WPM heuristic used in the base SKILL.md. It assumes a native speaker presenting technical content at a measured pace.

## Pace Profiles

| Profile | WPM | When to Use |
|---------|-----|-------------|
| `default` | 130 | Standard technical presentation. |
| `dense` | 110 | Heavy notation, equations, or non-native speaker. |
| `fast` | 150 | High-level overview, familiar audience, or urgent delivery. |

## Complexity Modifiers

Certain text features slow delivery. The model applies a complexity penalty per section.

| Feature | Penalty | Detection Rule |
|---------|---------|----------------|
| Equations / notation | +20% duration | Contains `=`, `\sum`, `\int`, Greek letters, or superscripts. |
| Dense jargon | +10% duration | More than 3 uncommon technical terms per 50 words. |
| Numbers / statistics | +10% duration | More than 3 numbers or percentages per 50 words. |
| Transitions / summaries | −10% duration | Section is labeled as transition, TOC, or summary. |
| Q&A prompt | −20% duration | Section is labeled as Q&A or closing. |

Penalties are additive but capped at +50% per section.

## Section Complexity Estimation

The model estimates complexity from text alone:

1. **Word count** — Simple tokenization on whitespace.
2. **Sentence length** — Longer sentences (>25 words) slow pacing.
3. **Character density** — High ratio of symbols to letters suggests equations or notation.
4. **Keyword triggers** — Words like "formally," "theorem," "proof," "derivation" signal density.

## What the Model Does Not Pretend to Know

- The speaker's actual speaking speed.
- Whether the speaker will pause for questions or audience reaction.
- Whether a slide contains a long animation or video.
- Whether the speaker will ad-lib.

These factors are acknowledged in the output as known uncertainties.

## Output Format

The model produces timing data in this structure:

```
Section                          Words  WPM   Duration  Flag
─────────────────────────────────────────────────────────────
Slide 1 — Title                     25  130     12 sec  
Slide 2 — Background               120  130     55 sec  
Slide 3 — Methods (dense)          180  110     98 sec  DENSE
Slide 4 — Results                  150  130     69 sec  
Slide 5 — Conclusion                80  130     37 sec  
─────────────────────────────────────────────────────────────
TOTAL                              555  127    271 sec  ~4.5 min

Target: 5.0 min
Status: UNDER BUDGET by 29 sec

Overrun risk ranking:
1. Slide 3 — Methods (dense)  98 sec  36% of total

Cut-for-time candidates:
1. Slide 2 — Background  55 sec  (compress to 30 sec)
```

## Known Limitations

- Word count is a proxy, not ground truth. Some speakers talk faster; some slower.
- Complexity detection is heuristic. A section flagged as "dense" may not actually slow the speaker.
- The model does not account for rehearsal time or Q&A duration.
