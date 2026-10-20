# Forensic methodology: the science-of-science sleuthing toolkit

*Last updated: 2026-10-20*

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

The 2025–2026 evidence adds two pressures. First, organised fraud is
scaling. Case studies in *PNAS* argue that paper mills, brokers and
predatory outlets evade interventions, and that this lets fraudulent
publications grow "at a rate far outpacing that of legitimate science"
[^13]. Second, generative AI is weakening image forensics. In a 2026
diagnostic study, 24 PhD-level reviewers distinguished AI-forged western
blots and tumour images from authentic ones at chance (mean accuracy
50.5%). The best commercial detector reached only AUC 0.79 [^14]. ASM's
2023–24 pilot of ImageTwin also found that, at the time, the tool
flagged problems only in halftone images (blots, micrographs,
photographs) and "could not detect issues with line art, sketches, or
graphs" [^2].

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

- **ImageTwin** (https://imagetwin.ai/): automated detection of
  duplications, splicing, and rotation/flip/crop variants. It compares
  figures against "a growing database of published content" [^2]. (The
  earlier "~120 million figures" figure was not found in the cited
  source and has been removed.) ASM integrated ImageTwin into its
  journal workflow in 2023 and ran a 12-month pilot across all 15 ASM
  journals from March 2023 to March 2024 [^2]. Of 2,627 accepted
  manuscripts screened, 410 raised image-related concerns; about 60% of
  these (248) were duplications. Acceptance was revoked for six (0.23%).
  ASM reports that about 3.9% of accepted manuscripts had duplication
  problems, "aligning with" Bik's 3.8% [^2]. Treat that comparison with
  caution. The 3.9% is given as "248 out of 6416", a denominator the
  paper does not reconcile with the 2,627 manuscripts it says were
  screened (248 of 2,627 would be about 9.4%). The paper's figure legend
  also puts duplications at "two-thirds" of concerns, against "nearly
  60%" in the text. The authors stress that "human
  training, review, and oversight are essential to validate output and
  filter out false positives".
- **Proofig** (https://www.proofig.com/): adopted across all six
  *Science* family journals. The adoption was announced in the January
  2024 editorial "Genuine images in 2024" [^11]; this corrects the
  earlier "early 2025" dating. Proofig targets duplication and
  partial duplication in western blots and microscopy, robust to
  rotation, flipping, resizing, and colour change.

Both tools augment but do not replace human inspection — the
sleuthing literature is consistent that the most informative
duplications are the ones that look intentional, which requires
contextual judgement the tools support but cannot fully replace.

**Generative-AI image forgery (2025–2026).** Duplication detectors look
for reuse. Synthetic images are not reused, so they need different
methods, and current evidence is discouraging:

- Luo et al. 2026 [^14]: expert reviewers performed at chance (50.5%)
  on 104 western-blot and xenograft images, some forged with a
  high-fidelity generative model. The best commercial AI detector
  reached AUC 0.790 (95% CI 0.695–0.885).
- Gosselin 2025 [^15]: three free web-based AI-image detectors tested
  on 48 ChatGPT-generated and 48 authentic western blots gave widely
  divergent sensitivity (0.19–0.96) and specificity (0.42–0.88), with
  low positive predictive values.

*Interpretation.* Image integrity is becoming harder, not easier, and
nothing in this evidence makes it tractable for a text-focused tool.

### Tortured-phrase detection

**Cabanac, Labbé & Magazinov (2021)** [^3] introduced the concept of
"tortured phrases" — unusual substitutes for established terminology
that betray translation- or paraphrase-tool manipulation. Their
2021 *arXiv* preprint (also deposited in HAL) gave examples that
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
million publications weekly [^4] [^12]. Its developers report that it
"has been instrumental in more than 1,000 retractions" [^12].

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
institutional infrastructure for the retraction-propagation work. At
the September 2023 announcement, Crossref's own retraction records
numbered about 14,000 and the Retraction Watch database about 43,000,
around 50,000 combined after overlap [^6]. After Crossref's
acquisition the data became openly available. Crossref's REST API
records retractions in the `update-to` field, with a `source` value of
`publisher` or `retraction-watch`, and the full dataset is a CSV in a
public git repository, updated once per working day [^6]. This enables
integration into
reference managers and citation auditors. By October 2026 Retraction
Watch reported "over 67,000 retractions" in its database [^18].

### Author-network and paper-mill forensics

Paper mills produce manuscripts at scale and sell authorship; the
*co-authorship network* of paper-mill products leaves detectable
fingerprints. Porter & McIntosh (*Scientific Reports*, 2024) [^7]
model this "authorship-for-sale" activity. Most authors on a fabricated
paper are added through a transaction, so co-authors are unlikely ever
to appear together on more than one paper. The resulting network
fingerprint gives a statistical detection method. Researchers in the
networks it flagged were connected to 37% of the papers identified by
the Problematic Paper Screener's tortured-phrase and "clay-feet"
methods [^7]. (The earlier description of three specific network
features, namely clustering coefficients, publication age and
single-collaboration rates, was not found in the abstract and has been
reduced to what the source states.)

Richardson et al. (*PNAS*, 2025) [^13] extend this from individual
networks to the enabling *entities*: paper mills, brokers that place
fraudulent work in targeted journals at scale, and predatory journals.
Their case studies show coordinated publishing across journals and
uneven targeting of subfields. They conclude that the entities' ability
to evade interventions is letting fraudulent output outgrow legitimate
science.

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
4. **Posting to PubPeer** [^9]: the post-publication peer-review
   platform, founded in 2012, where many detected flaws are posted
   [^11]. (The earlier "roughly 19% of all paper retractions" figure
   had no traceable source and has been removed.)
5. **Contacting journals / institutions** with structured concerns;
   following the (often slow) institutional response.

PubPeer allows anonymous comments, and its anonymity has been
controversial since its early years. (The earlier dating of anonymity
to March 2013, and the quotation about researchers being "afraid to
comment", had no traceable source and have been removed pending
verification.) The platform requires that critical comments cite
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
  check requiring no LLM judgement. The implementation hook is
  Crossref's `update-to` field and the Retraction Watch CSV [^6].
- **A future tortured-phrase / AI-fingerprint check** is a
  reasonable Phase 3 candidate — the Cabanac dictionary is open and
  the regex matching is cheap. Output: "flagged phrase 'counterfeit
  consciousness' at [passage] — possible paraphrasing-tool
  artifact; please verify."
- **`statistics-consistency`** (covered at
  [[statistical-inconsistency]]) implements Statcheck-class logic.
- **Image-integrity** is out of scope for a text-focused tool;
  point authors to Proofig / ImageTwin and to journal submission
  workflows that increasingly include them. `figure-text-alignment`
  draws this boundary, and the 2025–2026 evidence reinforces it. In
  ASM's 2023–24 pilot, ImageTwin flagged problems only in halftone
  images, not line art or graphs [^2]. We found no source stating
  Proofig's image-type coverage, so that limit should not be attributed
  to Proofig. Neither experts nor current detectors reliably catch
  generative-AI forgeries [^14] [^15]. Even a future multimodal
  sub-skill should not take on image-integrity claims.
- **Author-network / paper-mill detection** is out of scope and
  inappropriate for a per-manuscript pre-submission tool; the
  network signature requires corpus-level analysis.

The honest framing: scriptorium catches the cheap errors *before*
submission. The forensic tools — and the sleuths who operate them —
catch the rest *after*. The two layers compose; neither replaces the
other.

A cautionary 2025 case shows why the pre-submission layer matters. A
*DARU* article criticising PubPeer [^16] drew an editor's note within a
week. Retraction Watch reported that five of its 17 references did not
appear to exist, three more had incorrect DOIs or links, and one cited
a retracted paper. The editor-in-chief, a co-author, said two authors
had "checked CHATGPT" to verify the references [^17]. Unverified LLM
reference-checking let fabricated references reach print. That is the
failure mode `citation-audit` exists to catch (see
[[hallucination-in-llm-citations]]).

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

## Implementation priority for scriptorium

**Verdict:** No new skill. This is boundary-setting context, with one
deterministic hook in an existing skill.

- *Existing skill hook*: `citation-audit`'s retraction check, using
  Crossref's `update-to` field and the Retraction Watch data [^6].
  This is unchanged and remains the highest-yield item.
- *Boundary for `figure-text-alignment`*: the image-integrity exclusion
  stands and is now better supported [^2] [^14] [^15]. The skill's
  pointer to ImageTwin can note that, in ASM's 2023–24 pilot, it flagged
  problems only in halftone images (blots, micrographs, photographs),
  not graphs or line art [^2]. No source we found states Proofig's
  image-type coverage, so the pointer should not extend that limit to
  Proofig.
- *Maybe later*: a tortured-phrase / ChatGPT-fingerprint check. It
  would flip to Yes if the Problematic Paper Screener dictionary can be
  vendored under a compatible licence and a false-positive evaluation on
  non-native-English prose is done.
- *No*: image forensics, author-network and paper-mill detection, and
  corpus-level citation analysis.

## Limits and caveats

- The forensic-methodology movement is contested in places. Some
  sleuths have been accused of overreach, of inadequate
  due process before public flagging, or of inadequate
  acknowledgement of legitimate variability in research practice.
  PubPeer's anonymity is repeatedly criticised on these grounds,
  for example in an expert criticism in the *DARU Journal of
  Pharmaceutical Sciences* by Tsatsakis et al. (2025) [^16]. That
  article itself drew an editor's note over nonexistent references
  [^17], which illustrates both sides of the tension. The
  reform-vs-overreach tension is genuine.
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
- The Retraction Watch database is comprehensive but not exhaustive.
  Crossref notes that many retractions it holds "have not been reported
  by our members" [^6], and publishers do not always update Crossref
  metadata when they retract. (An earlier, unsourced estimate that true
  retraction rates are "~2–3×" the captured rate has been removed.)
- The right scriptorium posture: surface candidates with hedging
  language, name the technique that flagged them, and route to
  human (or to dedicated forensic tools) for adjudication. Never
  produce a verdict.

## References

[^1]: Bik EM, Casadevall A, Fang FC. The Prevalence of Inappropriate
    Image Duplication in Biomedical Research Publications. *mBio*.
    2016; 7(3):e00809-16. DOI: 10.1128/mBio.00809-16. PMID: 27273827.

[^2]: Chaturvedi AP, Hibbard A, Nelson C, Casadevall A, Kullas AL. ASM
    incorporates Imagetwin to address image duplication and preserve
    scientific accuracy. *mBio*. 2025;16(10):e0199025.
    DOI: 10.1128/mbio.01990-25. PMID: 40853133.

[^3]: Cabanac G, Labbé C, Magazinov A. Tortured phrases: A dubious
    writing style emerging in science. Evidence of critical issues
    affecting established journals. *arXiv*. 2021; arXiv:2107.06751.
    Also deposited as HAL preprint hal-03596867. (The earlier note
    that it appeared "subsequently in *Scientometrics*" was not
    supported by HAL, which lists it as a preprint, and has been
    removed.)

[^4]: Cabanac G, Labbé C, Magazinov A. The 'Problematic Paper
    Screener' automatically selects suspect publications for
    post-publication (re)assessment. *arXiv*. 2022; arXiv:2210.04895.
    Live tool: https://www.irit.fr/~Guillaume.Cabanac/problematic-paper-screener/.

[^5]: Greenberg SA. How citation distortions create unfounded
    authority: analysis of a citation network. *BMJ*. 2009;
    339:b2680. DOI: 10.1136/bmj.b2680. PMID: 19622839.

[^6]: Crossref. News: Crossref and Retraction Watch. 12 September
    2023. DOI: 10.13003/c23rw1d9.
    https://www.crossref.org/blog/news-crossref-and-retraction-watch/.
    Retracted-paper indicator documentation:
    https://crossref.org/documentation/retrieve-metadata/retraction-watch/
    (accessed 2026-10-20).

[^7]: Porter SJ, McIntosh LD. Identifying fabricated networks within
    authorship-for-sale enterprises. *Scientific Reports*. 2024;
    14:29569. DOI: 10.1038/s41598-024-71230-8. PMID: 39609477.
    arXiv preprint: 2401.04022. (The earlier article number "71230" was
    a fragment of the DOI.)

[^8]: COPE & STM. Paper Mills: Research Report. 2022.
    DOI: 10.24318/jtbG8IHL.
    https://members.publicationethics.org/sites/default/files/paper-mills-cope-stm-research-report.pdf.

[^9]: PubPeer Foundation. Post-publication peer-review platform.
    https://pubpeer.com/. Founded 2012.

[^10]: Ritchie SJ. *Science Fictions: How Fraud, Bias, Negligence,
    and Hype Undermine the Search for Truth*. Metropolitan Books,
    2020. ISBN 9781250222695 (US hardcover); 9781847925657 (UK
    Bodley Head hardcover); 9781847925664 (UK paperback).

[^11]: Thorp HH. Genuine images in 2024. *Science*. 2024;383(6678):7.
    DOI: 10.1126/science.adn7530. PMID: 38175900.

[^12]: Cabanac G, *et al.* Problematic Paper Screener: Trawling for
    fraud in the scientific literature. *The Conversation*.
    https://theconversation.com/problematic-paper-screener-trawling-for-fraud-in-the-scientific-literature-246317
    (accessed 2026-10-20).

[^13]: Richardson RAK, Hong SS, Byrne JA, Stoeger T, Amaral LAN. The
    entities enabling scientific fraud at scale are large, resilient,
    and growing rapidly. *Proc Natl Acad Sci U S A*.
    2025;122(32):e2420092122. DOI: 10.1073/pnas.2420092122.
    PMID: 40758886.

[^14]: Luo S, Tang R, Chen Z, *et al.* Biomedical Research Images
    Manipulated by Generative AI to Alter Scientific Outcomes:
    Diagnostic Study of Human and Automated Detection. *J Med Internet
    Res*. 2026;28:e100710. DOI: 10.2196/100710. PMID: 42826371.

[^15]: Gosselin RD. AI detectors are poor western blot classifiers: a
    study of accuracy and predictive values. *PeerJ*. 2025;13:e18988.
    DOI: 10.7717/peerj.18988. PMID: 39989748.

[^16]: Tsatsakis A, Aschner M, Sarigiannis D, Docea AO, Rezaee R,
    *et al.* An expert criticism on post-publication peer review
    platforms: the case of pubpeer. *DARU J Pharm Sci*. 2025;34(1):1.
    DOI: 10.1007/s40199-025-00580-z. PMID: 41233614.

[^17]: Retraction Watch. Springer Nature flags paper with fabricated
    reference to article (not) written by our cofounder. 21 November
    2025 (updated 24 November 2025).
    https://retractionwatch.com/2025/11/21/springer-nature-flags-paper-with-fabricated-reference-to-article-not-written-by-our-cofounder/.

[^18]: Retraction Watch. Weekend reads, 17 October 2026 (states "The
    Retraction Watch Database has over 67,000 retractions").
    https://retractionwatch.com/2026/10/17/weekend-reads-computer-science-conferences-impose-caps-lancet-strikes-continue-mathocalypse/
    (accessed 2026-10-20).
