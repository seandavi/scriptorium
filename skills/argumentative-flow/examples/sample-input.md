# Sample input — argumentative-flow

An intentionally meandering discussion paragraph, with citations and
statistics that must be preserved verbatim through the revision.

---

## Section to revise: Discussion (first paragraph)

A growing literature suggests that gut-microbiome composition is
relevant to cardiovascular disease, although the mechanisms remain
incompletely understood [@chen2023; @kumar2022review]. We found that
*Bacteroides fragilis* abundance was inversely correlated with
carotid intima-media thickness in our cohort of 312 adults
(Spearman r = −0.38, p = 0.002). This is broadly consistent with
prior murine work, though the translation from mouse models to
human cohorts is rarely as clean as one would hope. Mediterranean-
diet adherence also correlated with both microbiome composition and
intima-media thickness in our cohort. The directionality of the
microbiome–vascular relationship cannot be established from
cross-sectional data. Our findings should be interpreted with the
limitations of cross-sectional design in mind. There is, however,
sufficient prior evidence (including the present association) to
motivate prospective work on whether microbiome-targeted dietary
interventions slow subclinical atherosclerosis.

---

## MANUSCRIPT_STATE.yaml (excerpt)

```yaml
project:
  title: "Gut microbiome composition and subclinical atherosclerosis: a cross-sectional cohort study"
  target_type: manuscript
  target_venue: "Atherosclerosis"

document_phase:
  current: revision

core_claims:
  - "Bacteroides fragilis abundance is inversely correlated with carotid intima-media thickness in our human cohort."
  - "Mediterranean-diet adherence correlates with both microbiome composition and intima-media thickness."
  - "Cross-sectional design precludes causal inference; prospective microbiome-targeted dietary intervention work is motivated."

known_weaknesses:
  - "Cross-sectional design precludes causal inference."

terminology:
  preferred:
    - "Bacteroides fragilis"
    - "carotid intima-media thickness"
  forbidden:
    - "groundbreaking"
    - "novel"
    - "very"

style:
  tone: ["quantitative", "restrained"]
  voice: active
  audience: "vascular biology + clinical cardiology"

constraints:
  preserve_citations: true
  preserve_statistics: true
  avoid_hype: true
```

---

## What this paragraph needs

The paragraph's content is fine; the **order** isn't. The
load-bearing claim (the microbiome–intima-media-thickness association
in this cohort) is buried in the middle. The limitation of cross-
sectional design appears twice in slightly different wording. The
Mediterranean-diet finding is introduced without a connecting
sentence, then dropped. The bridge to the "motivate prospective work"
conclusion arrives too abruptly.

A well-executed argumentative-flow pass should:

- **Move the cohort finding to the topic position** of the
  paragraph (Gopen & Swan).
- **Consolidate the two limitation statements** into one explicit
  acknowledgment.
- **Connect the Mediterranean-diet finding** to the microbiome
  finding it accompanies.
- **Preserve every cite key** (`@chen2023`, `@kumar2022review`) in
  the output.
- **Preserve every number verbatim**: 312 adults, Spearman r =
  −0.38, p = 0.002.
- **Preserve declared terminology** ("Bacteroides fragilis," "carotid
  intima-media thickness" — never "IMT" or "CIMT" unless declared).
- **Preserve the active voice and quantitative, restrained tone.**
- **Not add new claims** (e.g., must not invent a mechanism not in
  the source).
- **Surface a recommendation** if it thinks the Mediterranean-diet
  finding should be its own paragraph — but **not split** the
  paragraph itself, since that's a content-level call for the author.
