# Learning from the 150 articles

## Purpose and scope

Use the corpus to learn how economists motivate a question, choose concrete words, explain identification, present numbers, develop a paragraph, and sustain an argument. Study empirical sections as carefully as introductions. The source map contains 30 articles each from AER, QJE, JPE, Econometrica, and ReStud. It supplies public links, reference versions, and section locations. It is a reading plan, not proof of the installing assistant's work.

## Complete a source-based first study

1. Create a fresh reading record outside the installed skill directory. Start every article as unread. Use the standard-library helper if available:

   ```bash
   python3 scripts/reading_tracker.py init /path/to/reading-progress.json
   ```

   Otherwise maintain the same information in a local document. Do not inherit the curator's read status, another AI's claimed completion, or this repository's examples.

2. Open each article's actual text using the available browser, document reader, or local PDF tools. Confirm title, authors, year, and version. Prefer the journal or author's source. If the supplied link fails, locate the same article through its DOI, publisher, author, or institutional repository. Record any change of version. Search snippets and abstracts cannot substitute for the article. Do not bypass access controls. Mark unavailable articles blocked and continue the accessible corpus.

3. Read the complete main text. Then inspect the abstract if present, the complete introduction, the data/design explanation or corresponding theoretical setup, a substantive results or argument section, and the conclusion closely. Use the source map's locations as starting points. Read relevant appendix material when it is needed to understand the example; do not describe selected passages as a full-article reading.

4. For every completed article, record the actual source, version, locations, and your own observations. Include at least three concrete observations with a passage location: how a transition is motivated; how wording or sentence subjects maintain flow; and how a comparison, number, or qualification is explained. For theory papers, study the corresponding economic argument rather than inventing empirical results. Explain why the choices work and when they would transfer to another paper. Paraphrase; do not collect a library of copyrighted sentences or distribute article PDFs.

5. Work in resumable batches that fit the available context. Save progress after each batch. Delegation is optional and requires authorization in the host environment; inspect the returned passages and notes before accepting their completion. Do not mark the whole corpus read because a download succeeded or a source list was loaded.

6. Synthesize what you learned across journals and sections. Identify recurring practices, useful differences, and cases where the same device would be inappropriate. Test the synthesis on an unfamiliar paper: explain its own economic question, comparison and evidence before editing. Keep its terminology and research choices. Transfer the writing method, not another paper's narrative, sample, variables, findings, or claims.

### Record format

Keep the generated article IDs. For each article set `opened_source`, `source_access_reference` (a tool result, document reference, or local source hash), and `actual_version`. Set `full_main_text_read` to true only after reading that scope. `sections` contains objects with `section` and `location`. Each of at least three `observations` contains `location`, `choice`, `why_it_works`, and `transfer`, written in your own words. Set `status` to `read` after these steps, or to `blocked` with `blocked_reason` when access fails. Saved progress belongs to the reader's workspace, not this public repository.

## Completion and reuse

Check progress with:

```bash
python3 scripts/reading_tracker.py check /path/to/reading-progress.json
```

The checker verifies coverage and the presence of source locations and substantive notes. It cannot prove comprehension or replace opening and reading the sources. Report the actual number read and blocked, and distinguish full-main-text reading from a selected-section study. Claim a completed 150-article first study only when all 150 records meet the stated scope. Until then, describe it as partial and continue from the saved record.

Once complete, reuse the synthesis and saved notes rather than rereading 150 articles for every paragraph. A new assistant that has not performed or inspected an evidence-backed study should not claim to have done so. A user can request an urgent edit before the study finishes; apply the portable writing workflow and report the learning status accurately.

If the host has no tools for reading external or local documents, state that limitation. It can still use the written guidance, but cannot truthfully claim to have read the corpus. This skill stores a portable method and reading evidence, not hidden memory or permanent changes to a model's weights.
