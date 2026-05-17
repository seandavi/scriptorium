# Citation accuracy: evidence base

*Last updated: 2026-05-17*

## Synthesis

The empirical literature on citation accuracy converges on an
uncomfortable finding: roughly one in four to one in five citations in
biomedical and adjacent literatures contains some form of inaccuracy,
and roughly one in ten contains an inaccuracy serious enough to
mislead a careful reader about what the cited paper says. This is not
a "new" problem traceable to LLMs; it predates them by four decades.
The earliest systematic accounting was published in *BMJ* in 1985
(de Lacey, Record & Wade), and every replication since — across
specialties, decades, and review methodologies — has landed in the
same neighborhood.

Two patterns matter most for any system that audits citations. First,
errors are not evenly distributed: review articles and frequently
cited "canonical" papers attract disproportionate inaccuracy, and a
substantial minority of errors propagate as *citation chains* in
which authors copy a wrong claim from a previous author who copied it
from theirs. Second, errors split between **quotation errors** (the
cited paper does not support the statement, or supports it only
partially) and **citation errors** (bibliographic data is incomplete
or wrong). Quotation errors are the load-bearing problem; bibliographic
errors are mostly cosmetic.

Implication for `citation-audit`: the skill should be designed around
the *quotation-support* question — does the cited work actually
substantiate the in-text claim? — rather than around bibliographic
metadata, where the marginal value of an automated check is small and
existing tools (CrossRef, reference managers) are already strong.

## Evidence

**de Lacey, Record & Wade (1985), *BMJ* 291(6499):884–886** — examined
references in six medical journals published in January 1984.
Quotation accuracy: the original author was misquoted in **15%** of
all references, and "most of the errors would have misled readers."
Citation accuracy: errors occurred in **24%** of references, of which
**8%** were major (preventing identification of the source). This is
the foundational study; subsequent work largely confirms its
numbers.[^1]

**Wager & Middleton (2007/2008 Cochrane methodology review,
*MR000002*)** — a systematic review of 66 studies analyzing 3,836
references across 74 biomedical journals. Median citation-error rate:
**38%** (range 4–67%) across more than 27,000 references. Median rate
of "major and minor quotation errors": **20%** (range 0–50%). Technical
editing was associated with lower error rates.[^2]

**Jergas & Baethge (2015), *PeerJ* 3:e1364** — systematic review and
meta-analysis of 28 studies (1985–2013) covering 7,321 references.
Pooled prevalence: **major** quotation errors 11.9% (95% CI 8.4–16.6);
**minor** errors 11.5% (95% CI 8.3–15.7); **total** quotation errors
25.4% (95% CI 19.5–32.4). Their conclusion: "quotation errors are
common in medical journal articles," and "even the lowest estimate of
total quotation errors was considerable (6.7%)."[^3]

**Pavlovic et al. (2021), *Clinical Science* 135(5):671–681** —
re-examined frequently cited biomedical papers by going back to the
original first authors to verify what their own papers actually said.
Feasibility study (1,540 articles, 2,526 citations of 14 papers):
**7.2%** of individual citations inaccurate; **11.1%** of articles
contained at least one inaccuracy. Verification study (2,995 articles,
4,912 citations of 13 papers): **10.3%** citations inaccurate; **15.0%**
of articles affected.

Critical sub-findings:

- **Citation of nonexistent findings** was the largest single error
  category (38.4% of inaccuracies) — the cited paper did not contain
  the claim attributed to it at all.
- **Inaccurately cited numerical data** (16.6%) and **inaccurate
  interpretation** (15.4%) were the next two categories.
- **Citation chains** accounted for ~20–24% of inaccuracies — errors
  copied from previous citing articles rather than introduced fresh.
- **Review articles** were more likely than primary research articles
  to contain inaccuracies, and inaccuracy rose with time since the
  cited paper's publication.[^4]

**Specialty-specific evidence** — Sauder et al. (2022) on surgical
literature found inaccuracy rates broadly consistent with the general
biomedical figures, with higher rates in lower-evidence study designs.
This pattern (higher inaccuracy where the claim is fuzzier) recurs
across specialties.[^5]

## How this informs scriptorium

The evidence base shapes `citation-audit` in three concrete ways.

1. **Audit the quotation, not just the citation.** Bibliographic
   errors are a long-solved problem in modern reference-manager
   workflows; quotation errors are not. The skill's primary
   responsibility is to ask, for each in-text citation, whether the
   referenced work supports the specific claim being made. Output
   sections should make this question explicit ("Claim supported?"
   "Claim partially supported?" "Claim not located in source?").

2. **Treat review citations differently from primary citations.** The
   Pavlovic finding that review articles carry higher inaccuracy
   rates, combined with the "review-citing-review" cascade documented
   in [[citation-overreach-research]], means the auditor should flag
   when a mechanistic or quantitative claim is supported only by a
   review citation. The flag is not "wrong" — it is "verify with
   primary source." This recommendation should *never* invent the
   primary source; see [[hallucination-in-llm-citations]].

3. **Surface citation chains.** When two or more papers cite the same
   source for the same claim using nearly identical phrasing, this is
   a hallmark of an unverified citation chain. The skill can detect
   such patterns when multiple papers in a corpus are audited
   together, and warn — without claiming to have verified the
   underlying source.

In `MANUSCRIPT_STATE.yaml`, the `preserve_citations: true` constraint
prevents transformation skills (compression, argumentative-flow) from
silently dropping or replacing references — which would otherwise
*introduce* the citation errors documented above as a side effect of
helpful-looking edits.

## Open questions / weak evidence

- Most accuracy studies are biomedical. Engineering, physics, and the
  humanities are less well-characterized. The numbers above should
  not be extrapolated to those literatures without caveat.
- "Major" vs "minor" error categorization is judgment-dependent. The
  Jergas meta-analysis acknowledges heterogeneity; pooled estimates
  carry wide confidence intervals.
- The fraction of errors that *change scientific conclusions*
  (vs. merely misattribute who said what) is not well quantified.
  Greenberg's distortion analysis in [[citation-overreach-research]]
  is the closest existing work and is qualitative.

## References

[^1]: de Lacey G, Record C, Wade J. How accurate are quotations and
    references in medical journals? *BMJ (Clinical Research Edition)*.
    1985;291(6499):884–886. doi:10.1136/bmj.291.6499.884.
    PMID: 3931753.

[^2]: Wager E, Middleton P. Technical editing of research reports in
    biomedical journals. *Cochrane Database of Systematic Reviews*.
    2008. doi:10.1002/14651858.MR000002.pub3.

[^3]: Jergas H, Baethge C. Quotation accuracy in medical journal
    articles — a systematic review and meta-analysis. *PeerJ*.
    2015;3:e1364. doi:10.7717/peerj.1364. PMID: 26528420.

[^4]: Pavlovic V, Weissgerber T, Stanisavljevic D, et al. How accurate
    are citations of frequently cited papers in biomedical literature?
    *Clinical Science (London)*. 2021;135(5):671–681.
    doi:10.1042/CS20201573. PMID: 33599711.

[^5]: Sauder M, Newsome K, Zagales I, et al. Evaluation of citation
    inaccuracies in surgical literature by journal type, study design,
    and level of evidence. *The American Surgeon*. 2022.
    doi:10.1177/00031348211067993.
