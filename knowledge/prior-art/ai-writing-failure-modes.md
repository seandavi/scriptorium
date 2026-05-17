# AI writing failure modes

*Last updated: 2026-05-17*

## Synthesis

The failure modes of AI-assisted scholarly writing fall into four
well-characterised categories: **hallucinated references**,
**authorial-voice loss / lexical homogenisation**, **automation
complacency**, and (more speculatively) **skill degradation over
time**. Three of the four are well-documented in the empirical
literature; the fourth is mostly hype with thin evidence. Scriptorium
should be honest about which it defends against and which it does
not.

The single most important framing point: scriptorium's design
choices — *conservative edits*, *structured outputs*, *explicit
invocation*, and *one skill = one responsibility* — are not
generically virtuous. They are specific defences against specific
failure modes. The conservative-edit posture defends against
voice loss and unintended semantic drift. Structured outputs make
hallucination auditable. Explicit invocation defends against
automation complacency. *They do not defend against everything*,
and pretending otherwise is a worse posture than naming the gaps.
This document exists so that `DESIGN.md` can ground its design
language in evidence rather than slogan.

## Evidence and frameworks

### 1. Hallucinated references

The best-characterised failure mode. Two foundational studies:

- **Walters & Wilder 2023** [1] tested ChatGPT-3.5 and GPT-4 on 42
  multidisciplinary topics, examining 636 citations. **55% of
  GPT-3.5 citations were fabricated outright**; **18% of GPT-4
  citations were fabricated**. Of the remaining (non-fabricated)
  citations, 43% (GPT-3.5) and 24% (GPT-4) contained substantive
  errors (wrong year, wrong page, misspelled author, wrong
  journal). GPT-4 was better, but the fabrication rate is still
  catastrophic for scholarly use without verification.

- **Bhattacharyya et al. 2023** [2] tested ChatGPT on medical
  content: 47% of citations fabricated, 46% authentic-but-
  inaccurate, only 7% correct. PMID 37337480.

The pattern is consistent across replications: LLMs hallucinate
plausible-looking citations at high rates, and the hallucinations
are often hard to detect by surface inspection because the cited
authors are real, the journals are plausible, and the topic
matches. See [[hallucination-in-llm-citations]] for the deeper
review and [[citation-accuracy-evidence]] for downstream
consequences.

The defence: **never let a generation step add citations**. Audit
existing citations against retrievable sources
([[citation-claim-alignment]]). Scriptorium's no-citation-invention
rule (DESIGN.md line: "Critique skills don't invent citations;
transformation skills don't add them") is a direct response.

### 2. Authorial-voice loss and lexical homogenisation

The "ChatGPT smell" has become measurable. Kobak et al. [3]
analysed ~15 million PubMed abstracts from 2010–2024, examining
*excess vocabulary* — words whose 2024 frequency substantially
exceeded the pre-ChatGPT (2021–2022) baseline. Terms with the
highest excess included **"delve", "underscore", "primarily",
"meticulous", "boast", "intricate", "realm", "commendable"**.
Over 100 terms showed meaningful surges. The authors estimate
that **at least 10% of 2024 PubMed abstracts were processed with
LLMs** — implying ~150,000 papers per year.

Detection studies (Sadasivan et al. 2023, "Can AI-Generated Text
Be Reliably Detected?" [4]) show the reverse problem: as LLM
distributions and human distributions converge, *any* detector
must trade Type I and Type II error. Watermarking helps but is
removable by paraphrasing. The practical implication is that
**stylistic detection of AI text is fundamentally limited**;
relying on detectors to police authorship is a losing strategy.

A separate strand of evidence is the **homogenisation effect**:
Agarwal et al. [5] found that AI writing suggestions push prose
toward Western, English-native, and majority-culture norms,
diminishing the cultural and stylistic nuances of writers from
underrepresented backgrounds. This is the inverse of the
ESL-helpful framing in [[esl-writers-swales-hyland]] — the same
tool that helps a hedging-uncertain ESL writer get reviewable
prose can also flatten a writer's distinctive voice.

The defence: **conservative-edit posture**. A transformation skill
that preserves terminology declared in `MANUSCRIPT_STATE.yaml`,
preserves citations and statistics, and reports its changes in
structured form gives the author the choice of which edits to
accept. The defence is *not* that scriptorium prose sounds less
AI-y than ChatGPT's; it's that the author retains the choice.

### 3. Automation complacency

The classic human-factors literature: **Parasuraman & Manzey 2010**
[6] reviewed empirical studies of automation use and integrated
them into a theoretical model. Key findings:

- **Automation complacency** — failure to monitor automated
  systems adequately — occurs under multitask load even in
  experts and cannot be trained away.
- **Automation bias** — over-acceptance of automation
  recommendations even against contrary evidence — occurs in
  both novices and experts, and persists across teams as well as
  individuals.
- Both are dynamic interactions of personal, situational, and
  automation-related characteristics; they are not character
  flaws.

Applied to writing assistance: studies on co-writing with
opinionated LLMs (Jakesch et al. 2023, the Buschek/Bhat line of
CHI work [7]) show that **users who accept more AI suggestions
exhibit measurable attitude shifts toward the AI's bias**, and
**most users do not notice they are being influenced**. The 2023
Cornell study found that a biased AI writing assistant doubled
the probability of users writing the assistant's position on a
contested social question.

The implication for scriptorium: every accepted edit is a small
attitude shift. A tool that emits voluminous suggestions and
expects the user to accept or reject each one is a complacency
machine. Scriptorium's design responses:

- **One skill = one responsibility**: smaller, more legible
  outputs are easier to evaluate carefully.
- **Explicit invocation**: users have to ask for help, which
  forces a moment of intentionality.
- **Structured outputs**: easier to scan and selectively act on
  than free-form prose.
- **Critique skills don't transform**: separating critique from
  transformation forces a second conscious step.

These help. They don't eliminate the problem.

### 4. Skill degradation over time

This is the most-discussed and least-measured of the failure
modes. The hypothesis: extended use of AI writing assistance
erodes the user's ability to write without it, with downstream
costs for thinking, learning, and disciplinary fluency.

Evidence is thin. The genre is mostly speculative essays (Marc
Watkins on writing pedagogy; press coverage of student writing
samples) and short-horizon experimental studies (Bhat et al.,
some 2024 CHI work) that cannot answer the long-horizon question.
There is *some* analogous evidence from GPS-and-navigation
literature (reduced spatial cognition with prolonged GPS use) and
from calculator-and-mental-arithmetic literature, but transfer to
writing is speculative.

The honest position: **flag this as a real concern but mark the
evidence as weak**. Scriptorium's design language should not
overclaim that conservative-edit posture defends against
skill degradation. It probably does not — what it defends against
is unintended *manuscript* degradation, not unintended *author*
degradation.

## How this informs scriptorium

This document is a **DESIGN.md defensive section**, not a skill.
The concrete uses are:

1. **Frame the conservative-edit posture as a defence, not a
   slogan.** When `DESIGN.md` says "transformative skills
   preserve citations, statistics, and terminology by default",
   point to Kobak et al. [3] and Walters & Wilder [1] as the
   reasons.

2. **Frame explicit invocation as automation-complacency
   defence.** Parasuraman & Manzey [6] is the citation. Auto-
   invoking transformative skills on file save would directly
   contradict this design choice.

3. **Acknowledge what scriptorium does *not* defend against:**
   - **Stylistic homogenisation by the author's own
     LLM-influenced prose style.** If the author already writes
     in the "delve / underscore / intricate" register before
     scriptorium runs, scriptorium does not fix that.
   - **Author skill degradation over long-horizon use.** No
     editing tool defends against this.
   - **Sophisticated user circumvention** (e.g., asking an LLM
     to draft an entire section and then running scriptorium on
     the result as a fig-leaf). The structured-output design
     surfaces the drafted content faithfully; it does not detect
     that the content was AI-drafted in the first place.

4. **Scope the project's claims honestly.** Scriptorium is a tool
   for *manuscript* improvement under human oversight. It is not
   a defence of the *author's writing skill*, the field's
   *epistemic norms*, or the long-term *health of the literature*.
   Conflating these is the trap.

## Implementation priority for scriptorium

**Verdict:** No new skill. **DESIGN.md defensive section**: yes,
high priority.

**Why useful context anyway:**
1. **Defends design choices already in `DESIGN.md`.** The four
   anti-patterns listed there ("giant prompts", "unconstrained
   rewriting", "hidden state", "citation hallucination") map
   directly onto failure modes documented in this evidence base.
   Pointing the prose at primary literature turns the
   anti-patterns from preferences into defensible engineering
   responses.
2. **Scopes the project's claims.** External readers (reviewers,
   adopters, critics) will probe whether scriptorium is "just
   another LLM writing tool with prettier marketing". This
   document gives Sean the language to answer: *here are the
   four documented failure modes; here are the specific design
   choices that respond to each; here is what we explicitly do
   not claim to fix.*
3. **Informs the skill descriptions.** Each skill's description
   should state which failure mode(s) it is calibrated against.
   `citation-audit` defends against (1); `argumentative-flow`'s
   conservative-edit posture defends against (2); explicit
   invocation defends against (3); none defend against (4).

**Concrete action:** add a "Defensive design" section to
`DESIGN.md` that summarises the four failure modes and links each
to a specific design choice. This document is the source material.

**Condition that would flip to a skill:** if a "voice
preservation" check becomes load-bearing (e.g., users complain
that their prose comes out flattened after a critique-and-revise
cycle), a `voice-fidelity-audit` skill could become justified in
v0.3+. The data it would need: a sample of the author's prior
prose to fingerprint against. Operationally non-trivial.

## Open questions / weak evidence

- **Skill degradation** is poorly evidenced. Treat as a real
  concern but do not overclaim defences.
- **Voice-loss measurement** is open. The Kobak et al. excess-
  vocabulary method [3] works at population scale (millions of
  abstracts) but is noisy for single manuscripts.
- **Author identity and AI use** are increasingly fluid: many
  writers now have their own LLM workflow before they ever touch
  scriptorium. The failure modes of "AI-then-scriptorium" prose
  are distinct from "human-then-scriptorium" prose and are not
  well characterised.
- **Detection literature** is a moving target. Sadasivan et al.
  [4] is the right framing (any detector trades Type I/II
  error), but specific detector benchmarks date quickly.

## References

[1] Walters, W. H., & Wilder, E. I. (2023). Fabrication and
errors in the bibliographic citations generated by ChatGPT.
*Scientific Reports*, 13, 14045. DOI:
10.1038/s41598-023-41032-5. PMID: 37679503.

[2] Bhattacharyya, M., Miller, V. M., Bhattacharyya, D., & Miller,
L. E. (2023). High rates of fabricated and inaccurate references
in ChatGPT-generated medical content. *Cureus*, 15(5), e39238.
DOI: 10.7759/cureus.39238. PMID: 37337480.

[3] Kobak, D., González-Márquez, R., Horvát, E.-Á., & Lause, J.
(2024). Delving into ChatGPT usage in academic writing through
excess vocabulary. arXiv:2406.07016. (See also subsequent extended
analysis "Delving into LLM-assisted writing in biomedical
publications through excess vocabulary".)

[4] Sadasivan, V. S., Kumar, A., Balasubramanian, S., Wang, W., &
Feizi, S. (2023). Can AI-Generated Text be Reliably Detected?
arXiv:2303.11156. (Originally posted 2023; subsequent NeurIPS /
ICLR follow-up work in 2024 builds on this framing.)

[5] Agarwal, D., Naaman, M., & Vashistha, A. (2024). AI Suggestions
Homogenize Writing Toward Western Styles and Diminish Cultural
Nuances. arXiv:2409.11360. See also Jakesch, M., Bhat, A.,
Buschek, D., Zalmanson, L., & Naaman, M. (2023). Co-Writing with
Opinionated Language Models Affects Users' Views. *Proceedings of
the 2023 CHI Conference on Human Factors in Computing Systems*.
DOI: 10.1145/3544548.3581196.

[6] Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias
in human use of automation: An attentional integration. *Human
Factors*, 52(3), 381–410. DOI: 10.1177/0018720810376055. PMID:
21077562.

[7] Jakesch et al. 2023, as above [5]; the broader Bhat/Buschek
line at CHI 2023–2025 on writing-assistant suggestion-acceptance
bias. For the homogenisation pull specifically, see also Reizinger,
P., Bonastre, J.-F., et al. work on AI text fingerprinting (2024)
[TODO verify exact citation; the originally referenced "Reizinger
2024" did not resolve cleanly in search].
