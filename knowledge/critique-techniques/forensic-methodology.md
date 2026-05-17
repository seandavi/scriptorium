# Forensic methodology: the science-of-science sleuthing toolkit

*Last updated: 2026-05-17*

## Synthesis

The past fifteen years have produced an organised, increasingly
professionalised forensic-science-of-science movement: image-
duplication detectors (Elisabeth Bik and successors), tortured-phrase
detectors (Guillaume Cabanac and the Problematic Paper Screener),
statistical-inconsistency detectors (Nick Brown, James Heathers — see
[[statistical-inconsistency]]), citation-network and retraction
analysis (Retraction Watch and Crossref's retracted indicator), and
author-network forensics for paper-mill detection. The movement's
operating model is broadly post-publication: sleuths find problems
*after* a paper is in the literature, often resulting in corrections,
expressions of concern, or retractions. The tools work; the human
follow-through is the bottleneck.

Three claims about the evidence base are robust. First, the failure
modes these tools detect are common enough to matter. Bik et al. (2016)
found that **~3.8% of 20,621 papers across 40 journals (1995–2014)
contained inappropriately duplicated images** [^1] — many features
suggestive of deliberate manipulation. Second, the tools generalise:
Bik's methodology has been re-implemented as Proofig and ImageTwin,
both now used by major publishers (Science, the ASM journals
respectively). Third, the same forensic frame applies across modalities
— image, text (tortured phrases), statistical (Statcheck-class),
author-network (paper-mill signatures) — and a comprehensive
post-publication audit is now imaginable as a pipeline rather than as
heroic individual work.

For scriptorium the relevant question is *where the per-manuscript
critique skill should sit relative to this ecosystem*. The honest
positioning: scriptorium is a **pre-submission, first-pass tool** that
catches cheap and common errors before they reach the literature. It
is not a replacement for forensic experts, and most of these tools'
operations require numerical computation, image processing, or
corpus-level network analysis that an LLM-only skill cannot perform
reliably. See [[statistical-inconsistency]] for the statistics-
forensics layer, [[internal-consistency]] for the within-manuscript
bookkeeping layer, and [[citation-claim-alignment]] for the citation-
support layer.

## Techniques and tools

### Image forensics

**Bik, Casadevall & Fang (2016)** [^1] is the foundational empirical
study. Bik visually screened images from 20,621 papers across 40
biomedical journals (1995–2014), classifying duplications into three
categories: simple duplication (same image used twice), repositioning
(rotation/flip/crop), and alteration (cutting/pasting, contrast
changes). 3.8% of papers contained problematic figures; at least half
showed features suggestive of deliberate manipulation. The prevalence
rose substantially across the time series. Bik's protocol — visual
inspection augmented by suspicion-based pattern recognition — has been
the methodological model for every subsequent image-integrity tool.

**Automated image forensics tools**:

- **ImageTwin** (https://imagetwin.ai/) — deep-learning-based detection
  of duplications, splicing, and rotation/flip/crop variants.
  Compares figures against a database of ~120 million published
  figures. Integrated into the American Society for Microbiology
  journal workflow as of a 2023+ pilot [^2].
- **Proofig** (https://www.proofig.com/) — adopted by Science (AAAS)
  in early 2025 (announced 2025). Targets duplication and partial-
  duplication in Western blots and microscopy, robust to rotation,
  flipping, resizing, and colour change.

Both tools augment but do not replace human inspection — the
sleuthing literature is consistent that the most informative
duplications are the ones that look intentional, which requires
contextual judgement the tools support but cannot fully replace.

### Tortured-phrase detection

**Cabanac, Labbé & Magazinov (2021)** [^3] introduced the concept of
"tortured phrases" — unusual substitutes for established terminology
that betray translation- or paraphrase-tool manipulation. Their
2021 *arXiv* preprint (later in *Scientometrics*) gave examples that
have become canonical:

- *counterfeit consciousness* → artificial intelligence
- *cruel temperature* → mean temperature
- *flag to clamor* → signal to noise
- *bosom peril* → breast cancer

Their analysis of the journal *Microprocessors and Microsystems*
found pervasive tortured-phrase use suggestive of large-scale
paraphrasing-tool laundering of plagiarised text. The follow-on
**Problematic Paper Screener** (Cabanac et al., 2022–present)
operationalises tortured-phrase detection plus eight additional
detectors (including ChatGPT-fingerprint patterns) and scans ~130
million publications weekly [^4]. As of recent counts it has been
instrumental in over 1,000 retractions.

The detection logic is simple: a curated dictionary of tortured-phrase
candidates flags any paper containing a hit, which is then triaged
manually. The list grows from sleuth contributions.

### Citation-pattern forensics

Citation-network analysis can detect:

- **Citation rings** — clusters of authors who cite each other
  disproportionately, indicating coordinated citation manipulation.
- **Self-citation patterns** — outlier authors whose self-citation
  rate exceeds field norms.
- **Retraction propagation** — citations to retracted papers that
  continue to appear after retraction. Documented extensively in
  Retraction Watch coverage.
- **Greenberg-style citation distortion** — bias / amplification /
  invention patterns at the literature level (see
  [[citation-claim-alignment]] and Greenberg 2009 [^5]).

The Retraction Watch + Crossref integration (2023) [^6] is the
institutional infrastructure for the retraction-propagation work. As
of late 2023 the Retraction Watch database contained ~43,000
retractions vs. ~14,000 in Crossref's prior internal data; after
Crossref's acquisition the data became openly available via the
Crossref API, enabling integration into reference managers and
citation auditors.

### Author-network and paper-mill forensics

Paper mills produce manuscripts at scale and sell authorship; the
*co-authorship network* of paper-mill products leaves detectable
fingerprints. A 2024 *Scientific Reports* paper [^7] developed an
explicit statistical method: paper-mill networks tend to show
**low clustering coefficients** (co-authors not connected to each
other, suggesting transactional rather than organic collaboration),
**young publication ages** (authors early in their careers, hired by
the mill), and **high single-collaboration rates** (one paper with a
given co-author and no further work).

The COPE/STM 2022 paper-mill research report [^8] is the
publisher-side governance synthesis. It describes shared screening
platforms, ORCID-based identity verification, and the integration of
image, statistical, and text forensics into editorial workflows.

### Whistleblower / sleuth methodology

The day-to-day practice of post-publication sleuthing — what
Elisabeth Bik, James Heathers, Nick Brown, Adam Marcus, Ivan Oransky,
Leonid Schneider, and others actually do — combines:

1. **Tip-driven and targeted inspection**: examining papers flagged
   by colleagues, by anomaly in citation patterns, or by author's
   prior record.
2. **Image inspection** for duplication / manipulation (Bik's
   visual-inspection protocol).
3. **Statistical recomputation** using Statcheck, GRIM, GRIMMER,
   SPRITE (see [[statistical-inconsistency]]).
4. **Posting to PubPeer** [^9] — the anonymous post-publication
   peer-review platform that has been involved in roughly 19% of
   all paper retractions since its 2012 founding.
5. **Contacting journals / institutions** with structured concerns;
   following the (often slow) institutional response.

PubPeer's anonymous-comment policy, controversial since inception,
became the dominant comment mode by March 2013 because researchers
reported they were "afraid to comment in the open view of their
senior peers." The platform requires that critical comments cite
publicly verifiable facts.

### Stuart Ritchie's *Science Fictions*

Ritchie's *Science Fictions* (2020) [^10] (see also
[[statistical-inconsistency]]) is the lay synthesis that frames the
whole forensic-methodology ecosystem as part of a broader reform
agenda — pre-registration, registered reports, replication, open
data, open peer review — rather than as ad hoc fraud-hunting. The
reform framing matters because forensic methodology in isolation can
look adversarial; in context it is part of a quality-assurance
infrastructure the literature has lacked for most of its history.

## How this informs scriptorium

Scriptorium's relationship to forensic methodology is *first-pass*,
*pre-submission*, *cheap-errors-only*. The contributions it can
realistically make:

- **`citation-audit`** can flag references to retracted papers
  using the Crossref retracted indicator. This is a deterministic
  check requiring no LLM judgement.
- **A future tortured-phrase / AI-fingerprint check** is a
  reasonable Phase 3 candidate — the Cabanac dictionary is open and
  the regex matching is cheap. Output: "flagged phrase 'counterfeit
  consciousness' at [passage] — possible paraphrasing-tool
  artifact; please verify."
- **`statistics-consistency`** (covered at
  [[statistical-inconsistency]]) implements Statcheck-class logic.
- **Image-integrity** is out of scope for a text-focused tool;
  point authors to Proofig / ImageTwin and to journal submission
  workflows that increasingly include them.
- **Author-network / paper-mill detection** is out of scope and
  inappropriate for a per-manuscript pre-submission tool; the
  network signature requires corpus-level analysis.

The honest framing: scriptorium catches the cheap errors *before*
submission. The forensic tools — and the sleuths who operate them —
catch the rest *after*. The two layers compose; neither replaces the
other.

LLM limits — be honest:

- Image forensics requires image processing; not LLM-tractable
  in-band.
- Citation-network analysis requires corpus-level data; out of scope
  for per-manuscript skills.
- Paper-mill fingerprint detection requires author-network data
  scriptorium does not have.
- Tortured-phrase / AI-fingerprint detection is tractable but
  carries a real false-positive risk on legitimate non-native-
  English writing; the skill must avoid stigmatising language
  variation and reserve flagging for unambiguous cases (e.g. the
  canonical "counterfeit consciousness" examples).

## Limits and caveats

- The forensic-methodology movement is contested in places. Some
  sleuths have been accused of overreach, of inadequate
  due process before public flagging, or of inadequate
  acknowledgement of legitimate variability in research practice.
  PubPeer's anonymity is repeatedly criticised on these grounds
  (see e.g. *DARU Journal of Pharmaceutical Sciences*, Tsatsakis et
  al. 2025, expert criticism of PubPeer). The reform-vs-overreach
  tension is genuine.
- Image-duplication detection is high-recall, modest-precision:
  many flagged duplications are legitimate reuse of stock images,
  schematic templates, or scale bars across panels. The tools
  surface candidates; humans adjudicate.
- Tortured-phrase detection penalises non-native English writers
  using legitimate but unusual phrasing. False-positive risk is
  real and asymmetric.
- Carlisle-method baseline analysis (see
  [[statistical-inconsistency]]) is corpus-level and has been
  reanalysed by Bolland et al. and others with caveats about
  assumption sensitivity.
- The Retraction Watch database is comprehensive but not exhaustive;
  estimated retraction undercounts in the broader literature remain
  substantial (multiple analyses suggest true retraction rates are
  ~2–3× the captured rate, depending on field).
- The right scriptorium posture: surface candidates with hedging
  language, name the technique that flagged them, and route to
  human (or to dedicated forensic tools) for adjudication. Never
  produce a verdict.

## References

[^1]: Bik EM, Casadevall A, Fang FC. The Prevalence of Inappropriate
    Image Duplication in Biomedical Research Publications. *mBio*.
    2016; 7(3):e00809-16. DOI: 10.1128/mBio.00809-16. PMID: 27273827.

[^2]: ASM Editors. ASM incorporates Imagetwin to address image
    duplication and preserve scientific accuracy. *mBio*. 2025;
    DOI: 10.1128/mbio.01990-25.

[^3]: Cabanac G, Labbé C, Magazinov A. Tortured phrases: A dubious
    writing style emerging in science. Evidence of critical issues
    affecting established journals. *arXiv*. 2021; arXiv:2107.06751.
    Subsequently in *Scientometrics* / HAL: hal-03596867.

[^4]: Cabanac G, Labbé C, Magazinov A. The 'Problematic Paper
    Screener' automatically selects suspect publications for
    post-publication (re)assessment. *arXiv*. 2022; arXiv:2210.04895.
    Live tool: https://www.irit.fr/~Guillaume.Cabanac/problematic-paper-screener/.

[^5]: Greenberg SA. How citation distortions create unfounded
    authority: analysis of a citation network. *BMJ*. 2009;
    339:b2680. DOI: 10.1136/bmj.b2680.

[^6]: Crossref. Retraction Watch acquisition announcement, September
    2023. https://www.crossref.org/blog/news-crossref-and-retraction-watch/.
    Retracted-paper indicator documentation:
    https://crossref.org/documentation/retrieve-metadata/retraction-watch/.

[^7]: Identifying fabricated networks within authorship-for-sale
    enterprises. *Scientific Reports*. 2024; 14:art. 71230.
    DOI: 10.1038/s41598-024-71230-8. arXiv preprint: 2401.04022.

[^8]: COPE & STM. Paper Mills: Research Report. 2022.
    https://members.publicationethics.org/sites/default/files/paper-mills-cope-stm-research-report.pdf.

[^9]: PubPeer Foundation. Post-publication peer-review platform.
    https://pubpeer.com/. Founded 2012; anonymous commenting since
    March 2013. Estimated involvement in ~19% of paper retractions
    since founding (per PubPeer Foundation reporting).

[^10]: Ritchie SJ. *Science Fictions: How Fraud, Bias, Negligence,
    and Hype Undermine the Search for Truth*. Metropolitan Books,
    2020. ISBN 9781250222695 (US hardcover); 9781847925657 (UK
    Bodley Head hardcover); 9781847925664 (UK paperback).
