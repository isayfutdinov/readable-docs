---
name: review-text
description: Use when a document — one file or a set of files — must be checked for how it reads before it goes to a team, a client or another agent, or re-checked after fixes, to see whether a reader can follow it in order and act on it without guessing. Triggers include "сделай доку читаемой", "заполишь", "причеши", "ревью по ролям", "подготовь к шарингу", "readability review", "review this doc as PO / dev / QA", any AI-written BRD, architecture note, plan, guide or spec before sharing. Not for code review, writing a document from notes, translation, spelling-only checks, or short messages.
license: MIT
metadata:
  author: Ildar Sayfutdinov
---

# Reviewing documents for sequential reading

## Overview

A human reads in order, and reads once. A document fails the moment the reader must guess; so does the report. Edits happen outside the report, and the next run is the next round.

## Hard constraints

- Never create, edit or delete the document or any file in its folder; read only the inputs the request names and this skill's files. The only deliverable is the report.
- Write the report in the language the request names, otherwise in the request's language. Document terms stay as written; text to paste into the document is in its language.
- The report holds no text on how to read it, no template comment and no phrase of this skill ("without guessing").
- A finding is a proposal, never a verdict or a judgement of the author, on one line: what is wrong, the replacement, the rule id, other places with the same defect.
- Replacement text adds no fact the document lacks: no number, date, cause or frequency, and no actor, step, order, destination, permission, state change, alternate flow or failure path. A missing fact is the defect ("does not say who grants access"), marked ‹…› in the replacement, never a question. A hedge stays a hedge.
- A replacement keeps every condition, number, qualifier and actor of the text it replaces; one wording for several places keeps each place's conditions.
- Review the form, not whether business decisions are right. A contradiction names both places; which version is right is the author's call.
- The TL;DR is 2–3 lines in the document's own words, ready to paste at its top; a review summary is not one.
- Every confirmed role has its own 0–10 score; a severity scale never replaces it.
- "No issues found" is not a pass; say what was checked.

## One round

Write the report from a copy of `assets/review-report-template.md`, comments deleted, where the request says or as the reply.

**0. Intake.** Read every file in reading order (a README, numbered prefixes, or the user's order) before any score. Pick the smallest reviewer set that covers the named readers (`references/reviewer-personas.md`), list other candidates as optional with one line why, and ask the user to confirm; if no answer can reach this run, proceed with the minimal set marked unconfirmed.

**1. Document review.** Make the document pass of `references/readability-rules.md` with what the user asked in mind: purpose and readers, whether the document answers their question, order of parts and the TL;DR, section purposes (7a, even if no reviewer raises it), terms used in more than one sense. With a previous version, compare their facts. The reviewer passes (section, sentence, inventory) are the reviewers'.

**2. Reviewers.** Run one reviewer per confirmed role, with its rule blocks, and the typo reviewer, as the personas file says, on a cheaper model than yours with a medium reasoning budget; the typo reviewer on the cheapest available with a small budget.

**3. Consolidate.** Merge reviewer findings with your own. A pasted replacement becomes the document, so check each against the text it replaces for a lost qualifier (only, automatically, if, after, internal), a causal link the document does not state (so, because, a colon joining two facts), a date or number beyond its scope and an actor the document does not name, even a generic one (the platform). Restore losses, turn additions into placeholders, and never claim nothing was invented without this check.

Keep proportion: every sentence that is not a finding hides the ones that matter. Volume comes from the document's defects, never from the report's own words: one line per defect, duplicates merged, "also at" short. The Summary holds scores and a verdict, never a finding. No finding is dropped for length.

**4. Rounds.** With a previous report, count the round and move each unfixed repeat, a partial fix included, to "Still open". Threshold: every role ≥ 9.0 in two consecutive rounds (≥ 9.6 after a human pass); after round 5 without it, the Summary recommends stopping. The skill never declares the document done; the user decides.

## Modes

- `review` (default): one round as above.
- `human-pass`: the request brings the user's remarks. No reviewer round (without a previous report, run `review` first): copy the previous report, answer each remark under "Answers to remarks" and keep the round number; later rounds use 9.6. Rules never change between runs.
- `second-opinion`: run the reviewer round on the model the request names and write a separate report titled "second opinion — <model>"; the user copies what they approve into the main report.

## Red flags: stop and re-read Hard constraints

- "Unclear" or "rewrite this" with no replacement text.
- A smoother or shorter replacement not checked condition by condition against each original.
- A replacement adds who acts, when, why or in which order.
- A replacement keeps the defect its finding names, or picks one side of a contradiction.
- A question to the author, or a guess inside a placeholder.
- Report text in the document's language only because the document is in it.
- A template comment, or its content in your own words, left in the report.
- A sentence the author does not need, or a finding dropped to make the report shorter.
