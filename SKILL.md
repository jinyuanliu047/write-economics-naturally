---
name: write-economics-naturally
description: Write and revise English economics papers with clear motivation, natural flow, precise empirical interpretation, and a consistent author voice. Covers abstracts through appendices and exhibit notes; includes a source-based learning programme drawn from 150 articles. Preserve the research, follow the author's choices, and use the complete portable workflow rather than a journal template.
---

# Write Economics Naturally

Help an economist understand the question, the comparison, the evidence, and why each sentence follows the previous one. Apply the same standard to the abstract, introduction, data, design, results, mechanisms, robustness, conclusion, appendix, and exhibit notes. These instructions are self-contained and apply across papers, topics, datasets, and AI tools.

## 1. Learn the craft and understand the paper

For a new assistant's first study, read [the learning guide](references/first-use-study.md) and work through the [150-article source map](references/reading-ledger.json). Open the actual articles; a bibliography, inherited completion flag, abstract alone, or another assistant's summary does not establish that you read them. Save your own source locations and concrete observations, resume unfinished batches, and report the actual scope. A user can request an immediate edit while the longer study continues; do not claim that the study is complete before it is.

For the paper being edited, first read its current sources, exhibits, research choices, terminology, and relevant user-authored examples. Establish the question, contribution, identifying comparison, core outcomes, main magnitudes, and evidence that materially changes interpretation. Ask only for missing information that matters. Treat criticized assistant prose as a problem to fix, not as the author's desired voice.

Learn the clarity, economic motivation, and narrative patience of good published economics, including work by David Y. Yang, Nancy Qian, Justin Yifu Lin, and Claudia Goldin. Adapt the craft to the current argument; do not copy distinctive wording, borrow another paper's conclusions, or imitate one author's surface mannerisms.

## 2. Use the author's portable defaults

Unless the user explicitly requests a different style, apply all of these defaults throughout new prose:

- Do not use em dashes, including paired interruptions. In LaTeX prose, do not introduce `---` or `\textemdash`. Use a full stop or recast the sentence. Preserve mathematical minus signs, numerical ranges, exact source titles, and faithful quotations when needed.
- Use familiar words, precise verbs, and idiomatic economic language. Avoid inflated vocabulary such as “delve,” “pivotal,” “tapestry,” “testament,” “underscore,” and “it is worth noting.” Do not trade a stable technical term for an unfamiliar synonym merely to sound varied.
- Prefer short declarative sentences with one main idea. Let a necessary explanatory sentence be longer when it improves flow. Avoid long noun chains, stacked subordinate clauses, double-comma appositives, and repeated comma interruptions.
- Use active subjects. “We use” suits an author choice; people, institutions, outcomes, and estimates can carry the next sentence. Avoid consecutive mechanical “We” openings and forced passive substitutes. Sentences beginning with “The” are allowed when natural.
- Make each sentence motivated. Carry known information into the next sentence and add one useful point. Explain why a fact, method, control, or subsequent test matters before listing its mechanics. Remove repetition and filing announcements that do not advance the argument.
- Lead with the question or finding and then explain it. Use warranted significance and quantitative language. Avoid both blanket certainty and a ritual disclaimer after every result. Preserve specific qualifications and contrary evidence that change interpretation.

These defaults travel with the skill and do not depend on a particular project's `AGENTS.md`. Explicit user instructions take precedence. Preserve the current paper's voice and terminology rather than imposing the same opening, paragraph skeleton, or vocabulary on every project.

## 3. Build an argument at each scale

Before revising a paragraph, identify its job and what the reader already knows. A sentence should supply a necessary fact, explain a comparison, present evidence, interpret it, or motivate the next question. The connection must be substantive; adding “moreover” does not fix a missing connection.

Name the people, institution, event, place, and period before compressing them into technical labels. Explain who differs from whom and when before referring to DID, IV, a gradient, or a margin. Historical context earns its place by explaining behavior, measurement, timing, identification, or interpretation. Let the account unfold patiently without inventing scenes, anecdotes, facts, mechanisms, or citations.

Read [prose-craft.md](references/prose-craft.md) for diction, reference, and rhythm, and [editing-examples.md](references/editing-examples.md) for concrete decisions. The examples are synthetic illustrations, not sentences to reuse mechanically.

## 4. Carry the standard through every section

**Abstract.** Begin with a question or problem of wider economic relevance, then connect it naturally to the setting and evidence. Give an intelligible comparison, the principal finding, the contribution, and a few informative numbers when supported. Preserve the declared core outcome set and useful data scale. Omit the full transformation formula, FE list, coefficient catalogue, and robustness inventory unless essential to the point. Do not introduce a vague global claim merely to sound broad.

**Introduction and contribution.** Explain the economic problem, why this setting helps answer it, what the study adds, and how the evidence bears on the question. Distinguish what existing literature establishes from the precise additional question answered here. Develop the relevant literature streams rather than listing citations or renaming contributions. Summarize results substantively; put detailed table interpretation and appendix references where readers need the supporting evidence.

**Background and data.** Give context before labels. Define the central concept, its proxy, the population, source coverage, timing, geographic level, denominator, and missing-value treatment as needed for interpretation. Keep a concept distinct from its administrative record or survey proxy. Separate events from later remembrance, exposure from outcomes, and measured attitudes from behavior when those distinctions matter to the paper.

**Design.** Explain the economic comparison and source of variation before the regression notation. State the actual comparison groups and relevant timing in ordinary language. Motivate each important control or alternative specification by the competing explanation it addresses. Preserve the sample, estimator, transformation, FE, weights, and clustering. First-stage strength establishes relevance; give exclusion assumptions with the substantive IV interpretation.

**Results and robustness.** Give the finding, its units, comparison, magnitude, and implication. Refer to an exhibit as part of the argument: “Table 4 shows ...” or “Panel B of Table 4 ...”. Identify the parent table when introducing or switching panels. Use a verified benchmark only on the correct sample and scale. Compare controlled and baseline estimates on identical observations before attributing a change to the control. Distinguish a precise small estimate, an imprecise estimate, and a materially unstable result. Keep an economic explanation constructive while distinguishing demonstrated evidence from possible mechanisms.

**Mechanisms and further analysis.** Organize evidence around meaningful channels and explain why each measure informs the proposed channel. A proxy, a reported belief, an observed action, and a causal mediator are different objects. Interpret survey questions according to their actual wording. State the sample and geographic match where they change the comparison. Keep later outcomes and intergenerational comparisons connected to the paper's question without silently treating them as the original identification design.

**Conclusion, appendix, and notes.** Return to the economic question and warranted contribution. Keep needed definitions and source attribution available without repeating the whole methods section. Notes should define the dependent variable and unit, exposure, comparison or sample, essential specification, inference, and any feature needed to read the exhibit. Preserve the author's established formatting; learning from AER does not require its document class or template. With no established table style, use clear outcome headings above estimates, sequential column numbers, readable rules, and consistent notes.

Read [empirical-sections.md](references/empirical-sections.md) for detailed empirical interpretation. Do not change research choices to improve the story or significance.

## 5. Review meaning, flow, and delivery together

Compare every substantive claim with the current exhibits, code, and sources. Preserve values, uncertainty, sample definitions, missing-value rules, estimators, outcomes, exposure measures, LaTeX commands, citation keys, labels, and references unless their modification is separately authorized. Do not invent a benchmark, IQR interpretation, causal channel, or statistical claim.

Read adjacent paragraphs together and read the passage aloud internally. Check that each sentence earns its place, references have clear antecedents, comparisons are intelligible, terms remain stable, and the next paragraph has a reason to follow. Check repeated openings, repeated conclusions, awkward noun chains, unsupported causal verbs, and em dashes in all newly written prose. Revise the argument before merely swapping words.

For LaTeX, edit the intended existing sources, compile the project, and inspect affected output. Distinguish a saved draft, a successful build, and verified scientific interpretation. Return a complete usable revision with a short account of material changes and remaining questions. Reuse the learned craft across projects while rebuilding the factual argument from the current paper's evidence.
