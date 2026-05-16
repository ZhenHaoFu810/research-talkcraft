# Contradiction Taxonomy

This document defines the classes of contradictions that can arise between a slide deck and supporting materials in `slides+context` mode. Each class includes what it looks like, why it matters, common causes, and its default risk level.

---

## 1. Temporal Mismatch

**What it looks like:**
- The deck states a sample period, event date, or version date that differs from the supporting material.
- Example: Deck says "2010–2023"; abstract says "through 2024."

**Why it matters:**
- The speaker may present outdated or incomplete temporal scope.
- Audience members who have read the newer material will notice the discrepancy immediately.

**Common causes:**
- The deck was created before the paper was updated.
- The speaker is presenting an older version of the work.
- The abstract reflects a post-submission extension.

**Default risk level:** Medium. Usually manageable if the speaker acknowledges the discrepancy, but can become High if the temporal difference changes the main result.

---

## 2. Sample / Dataset Mismatch

**What it looks like:**
- The deck and supporting material describe different samples, populations, or data sources.
- Example: Deck says "S&P 500 firms"; abstract says "all U.S. public firms."

**Why it matters:**
- External validity claims depend on the correct sample description.
- A skeptical audience member may challenge generalizability based on the discrepancy.

**Common causes:**
- Presentational compression (deck simplifies for brevity).
- The deck reflects an earlier sample decision later expanded in the paper.

**Default risk level:** Medium. Often presentational compression, but can be High if the sample change is material to the identification strategy.

---

## 3. Claim-Strength Mismatch

**What it looks like:**
- The supporting material frames a result more strongly or more weakly than the deck.
- Example: Abstract says "reliably identifies even very small amounts"; deck says "power is modest at low usage rates."

**Why it matters:**
- This is a credibility risk. The speaker may accidentally oversell or undersell a result.
- Marketing-friendly language in supporting materials can create defense-readiness gaps.

**Common causes:**
- Abstracts and press releases use stronger language than the body of the paper.
- Decks are written by authors who want to be cautious; abstracts are written for broader appeal.

**Default risk level:** High. Claim-strength mismatches are among the most dangerous contradictions because they directly affect what the speaker can defend.

---

## 4. Method-Description Mismatch

**What it looks like:**
- The deck describes a method differently from the supporting material.
- Example: Deck says "we use GPTZero"; abstract says "we use a proprietary commercial classifier."

**Why it matters:**
- A detail-oriented audience member may ask for clarification.
- If the deck oversimplifies to the point of inaccuracy, the speaker cannot defend the method under challenge.

**Common causes:**
- Presentational compression.
- The deck was created before the final method was locked.

**Default risk level:** Low to Medium. Usually benign unless the simplification changes the methodological claim (e.g., "randomized experiment" vs. "observational design").

---

## 5. Result-Magnitude Mismatch

**What it looks like:**
- The deck and supporting material report different numerical results for the same analysis.
- Example: Deck says "40% reduction"; abstract says "35% reduction."

**Why it matters:**
- Direct numerical conflicts are easy for the audience to spot and hard to explain away.
- They suggest the speaker does not know their own numbers.

**Common causes:**
- The deck reflects an earlier analysis; the paper was updated.
- Rounding or unit conversion differences.
- The deck and paper report results from different specifications.

**Default risk level:** High. Any numerical discrepancy undermines credibility.

---

## 6. Contribution-Framing Mismatch

**What it looks like:**
- The deck and supporting material describe the contribution differently.
- Example: Deck says "we validate a detector"; abstract says "we provide the first large-sample evidence of GAI adoption."

**Why it matters:**
- Contribution framing determines how the audience evaluates the talk.
- A mismatch can make the talk feel incoherent or overstated.

**Common causes:**
- The abstract frames for a broad audience; the deck frames for a specialist audience.
- The deck focuses on one paper; the abstract reflects a broader research agenda.

**Default risk level:** Medium. Usually manageable if the speaker is aware of both framings, but can confuse the audience if the opening and closing use different contribution claims.

---

## 7. Availability / Reproducibility Mismatch

**What it looks like:**
- The deck and supporting material make different claims about data availability, code release, or reproducibility.
- Example: Deck says "data will be public"; abstract says "data are available upon request."

**Why it matters:**
- Reproducibility claims are scrutinized heavily.
- A mismatch can lead to accusations of misleading promises.

**Common causes:**
- Plans changed between deck creation and paper submission.
- The deck was aspirational; the paper reflects actual availability.

**Default risk level:** Medium to High. Depends on whether the audience cares about replication (very high in some fields).

---

## Distinguishing True Contradictions From Benign Differences

### Version Drift

**What it is:** The deck and supporting material describe different versions of the same project, both of which were accurate at the time they were written.

**How to tell:** Check whether the discrepancy can be explained by a timeline. If the abstract is newer and the deck is older, this is version drift, not a factual error.

**Handling:** Flag as version drift. Note which source is newer. Let the user decide which version to present.

### Extra Supporting Detail

**What it is:** The supporting material contains information the deck omits, but the omission does not conflict with anything in the deck.

**How to tell:** Ask whether the deck explicitly says the opposite. If not, it is extra detail, not a contradiction.

**Handling:** Surface as supplementary context. Do not flag as a contradiction.

### Presentational Compression

**What it is:** The deck simplifies a claim for brevity or clarity without changing its factual meaning.

**How to tell:** Ask whether a reasonable audience member would interpret the simplified claim differently from the full claim. If not, it is compression.

**Handling:** Accept as normal. Only flag if the compression changes the factual meaning.
