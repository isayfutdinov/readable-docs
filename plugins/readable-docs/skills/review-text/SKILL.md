---
name: review-text
description: Use when a document — one file or a set of files — must be checked for how it reads before it goes to a team, a client or another agent, or re-checked after fixes, to see whether a reader can follow it in order and act on it without guessing. Triggers include "make this document readable", "polish this document", "clean up this document", "review from each reader role", "prepare this document for sharing", "readability review", "review this doc as PO / dev / QA", any AI-written BRD, architecture note, plan, guide or spec before sharing. Not for code review, writing a document from notes, translation, spelling-only checks, or short messages.
---

# Reviewing documents for sequential reading

## Overview

One round of form review of a document, from the roles of its readers, gives a report with findings, ready replacement text, the findings that block a reader marked, and a 0–10 score per role; the document itself is never changed.

## Hard constraints

- Never create, edit or delete the document or any of its files; read only the inputs the request names and this skill's files. The only deliverable is the report, written where the request says (the document's folder included), otherwise as the reply.
- Write the report in the language the request names, otherwise in the request's language. Document terms stay as written; text to paste into the document is in its language.
- The report holds no text on how to read it and no phrase of this skill ("without guessing").
- A finding is a proposal, never a verdict or a judgement of the author, written as the lines of `assets/review-report-template.md`.
- Every replacement obeys 3a–3c of `references/readability-rules.md`.
- Review the form, not whether business decisions are right.
- Every role run has its own 0–10 score.
- Findings have no quota. Report a finding as `references/readability-rules.md` defines it, not a change merely to fill the report; no optional improvement is required.

## Priorities when rules compete

Preserve the document's content, conditions, qualifications, attribution and author's position. Make the intended meaning explicit and follow the reader's task; then shorten and polish. Brevity or style never justifies losing meaning or leaving the reader to guess. Where the document does not establish the intended meaning, name the gap and use a placeholder instead of choosing a reading. This is an order for editorial choices, not a fact check.

## One round

Write the report from a copy of `assets/review-report-template.md`.

**0. Intake.** Read every file in reading order (a README, numbered prefixes, or the user's order) before the document pass. Set the document's purpose and readers: who reads it and what they must be able to decide or do after reading, from the request, otherwise from the document. Pick the reviewer set (`references/reviewer-personas.md`). Ask the user to confirm it only when the request names no readers, the answer would change the set, and an answer can reach this run; otherwise run the set, and About says why it was not asked or not confirmed.

**1. Document review.** Make the document pass of `references/readability-rules.md`.

**2. Reviewers.** Run one reviewer per role in the set, with its rule blocks, and the typo reviewer, as `references/reviewer-personas.md` says.

**3. Consolidate.** Merge reviewer findings with your own; a defect stated by several reviewers or at several places is one finding. Check each mark against the definition of a blocking finding (`references/readability-rules.md`). Check each replacement against the text it replaces by 3a–3c and 10a: restore losses and turn additions into placeholders. The report's length comes from the document's defects, never from the report's own words: one line per defect, as the template gives it. No finding is dropped for length.

**4. Rounds.** A round is one `review` run on the current version of the document. With a previous report it is the next round: number it from that report and move each unfixed repeat, a partial fix included, to "Still open". In rounds 1 and 2 the report recommends a next round only when the round has a blocking finding, to be run after it is fixed; wording findings never call for one. In round 3 and later it recommends stopping, even when blocking findings remain, and lists them as remaining. The skill never declares the document done; the user decides.

## Modes

- `review` (default): one round as above.
- `human-pass`: the request brings the user's remarks on a previous report (without one, run `review` first). No reviewer round: copy the previous report, keep its round number, and answer each remark under "Answers to remarks". A remark changes the answers in this report, never the rules or the score scale of later rounds.
- `second-opinion`: the request names a model. Run step 2 on that model, then step 3 with the document pass of the main report of the same round (without one, run `review` first). Write a separate report with that round's number and the second-opinion title of the template; the user copies what they approve into the main report.

## Red flags

| If you think | Do instead |
|---|---|
| "The likely reading is obvious; I'll use it." | A guess is a finding; without a reading the document establishes, the replacement carries both (8b). |
| "The author surely means this actor, reason or order." | Name the missing fact as the defect, with a placeholder (3c). |
| "I'll ask the author." | A missing fact is a finding with a placeholder, never a question (3c). |
| "The shorter replacement says the same." | Check it condition by condition against each original (3a, 10a). |
| "Unclear; this needs a rewrite." | Give the replacement text, or the placeholder for what is missing. |
| "The document is in another language, so the report is too." | The report is in the request's language (Hard constraints). |
| "The report is long; minor findings can go." | No finding is dropped for length (step 3). |
