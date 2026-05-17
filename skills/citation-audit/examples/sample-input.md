# Sample input — citation-audit

A synthetic two-paragraph discussion section designed to exercise
every pattern the skill flags. Real manuscripts are messier; this is
a teaching example.

---

## Discussion (excerpt)

Our findings extend a growing literature on the role of gut-microbiome
composition in cardiovascular disease. *Bacteroides fragilis*
abundance correlates with reduced atherosclerotic plaque burden in
murine models [@chen2023], and our cohort replicates this association
in 312 human subjects. *B. fragilis* causes plaque regression through
trimethylamine-N-oxide (TMAO) suppression [@kumar2022review]. This is
consistent with the established role of TMAO as a primary driver of
atherogenesis. Mediterranean-diet adherence is a stronger predictor
of cardiovascular outcomes than statin use in elderly populations
[@martinez2024].

Several limitations should be noted. The murine model used by Chen
et al. employed a high-fat diet that exceeds typical human dietary
fat intake; whether the protective association translates to standard
human diets remains unclear. We also did not perform fecal microbiome
transplant experiments, which would be the gold standard for
establishing causation.

## Bibliography

```yaml
- id: chen2023
  type: article-journal
  title: "Gut microbiome diversity and atherosclerotic plaque
    burden in apoE-/- mice fed a high-fat diet"
  author:
    - family: Chen
    - family: Wang
    - family: Liu
  container-title: Circulation Research
  issued: { year: 2023 }
  abstract: >
    We characterized gut microbiome composition in 48 apoE-/- mice
    fed a high-fat diet for 16 weeks. Bacteroides fragilis abundance
    was inversely correlated with aortic plaque area (Spearman
    r = -0.42, p = 0.003). Causal inference requires further work;
    the present study establishes association only.

- id: kumar2022review
  type: article-journal
  title: "Trimethylamine-N-oxide and cardiovascular disease: a
    narrative review"
  author:
    - family: Kumar
  container-title: Frontiers in Cardiovascular Medicine
  issued: { year: 2022 }
  abstract: >
    This review surveys evidence linking TMAO to atherosclerotic
    cardiovascular disease across animal models, observational
    cohorts, and small interventional studies.

- id: martinez2024
  type: article-journal
  title: "Mediterranean diet vs statin therapy in elderly
    cardiovascular outcomes: a propensity-matched cohort"
  author:
    - family: Martinez
  container-title: JAMA Internal Medicine
  issued: { year: 2024 }
  abstract: >
    Among 1,847 propensity-matched elderly patients, Mediterranean-
    diet adherence and statin use were each associated with reduced
    composite cardiovascular events (HR 0.81 [95% CI 0.71-0.92] and
    HR 0.79 [95% CI 0.69-0.91] respectively); the two were not
    statistically distinguishable from each other.
```

## What this snippet is designed to exercise

| Issue | Where | Pattern |
|---|---|---|
| Cited paper explicitly disclaims causation; manuscript asserts causation | "*B. fragilis* causes plaque regression… [@kumar2022review]" combined with chen2023 disclaimer | Causal overreach + citation–claim mismatch |
| Mechanistic claim ("through TMAO suppression") supported only by a narrative review | kumar2022review | Review-only support for mechanistic claim |
| "Established role of TMAO as a primary driver of atherogenesis" | (in-text) | Unsupported assertion — no citation |
| "Stronger predictor than statin use" | martinez2024 | Citation overreach — the cited cohort found the two statistically indistinguishable, not one stronger |
| First sentence's reference to "growing literature" | (in-text) | Unsupported general claim |
