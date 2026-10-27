<!--
Copy this template, replace every <slot>, follow the comments, then delete every comment, this one included.
Language: the report, headings included, is in the language the request names, otherwise in the language of the request. Document terms stay as written. Text to paste into the document (replacements, the TL;DR, opening sentences, glossary entries) is in the document's language.
Leave out anything on how to read the report, anything from these comments, and any phrase of the skill, such as "without guessing": the skill's wording is not the document's.
Finding line, in every section: <file>:<place> — <what is wrong, one sentence> → «<replacement>» (rule <id>; also at: <places>)
- <place> is a line number, or a section and item id where line numbers do not hold.
- What is wrong is a defect of the document; a missing fact is stated as one ("does not say who grants access"), never as a question to the author.
- A placeholder ‹…› marks a fact the document lacks: a word or two (‹who›, ‹deadline›), or the versions the document gives (‹5|10›).
- A replacement longer than two lines goes in a fenced block under the line.
- "also at" names up to five places and is left out when a search of the whole document found none; a defect at three or more places is also one growth area that lists its places.
- Each finding stands alone: no finding numbers, no "see above", no references between findings.
Keep the sections in this order. A section or line whose comment starts with "Only" is left out when its condition is false; any other section stays, with "none found" when empty. No severity scale and no section of your own.
-->

# Readability review — <document name> — round <N>

## Summary

| Role | Score 0–10 | Where the reader first gets stuck |
|---|---|---|
| <role> | <score> | <place and a few words> |

<verdict on the document as a whole>

<!-- One row per confirmed role, scored by its own reviewer, with one decimal; "—" in the last column when nothing blocks the role. Then the verdict, a few plain sentences: whether the readers can act on the document, and which kinds of problems dominate. The verdict holds no finding, place, replacement or rule id: every finding lives in its own section below. After round 5 without the threshold, the verdict recommends stopping. -->

## Answers to remarks

| Remark | Agree or not, and why | Why the reviewers missed it | Same defect elsewhere |
|---|---|---|---|
| <remark> | <answer> | <reason> | <places, or none after checking> |

<!-- Only in human-pass mode: one row per remark the user brought. -->

## Structure

### TL;DR for the top of the document

> <two or three lines, ready to paste>

<!-- In the document's language and in its own facts and words: what the document is, for whom, what they can do after reading it, its parts in reading order. A summary of this review is not a TL;DR. -->

### Proposed order of the document

1. <part> — <what it holds>

<!-- The order the document's parts should take after the edits: TL;DR, then context (what and why), then details. Say where each moved part comes from. Write the list even when nothing moves. -->

### Sections and order

- <finding line>

<!-- Findings on sections and order, in reading order: every section whose purpose cannot be stated, with a proposed opening sentence (7a), including those from the orchestrator's document pass that no reviewer raised; text that belongs elsewhere, a duplicate, an item of another kind (7b–7f); file names out of reading order (4i); a term or reference used before it is explained (4c, 4d), with the place where it is defined or the gloss at first use. After → comes the text to paste in «» (an opening sentence, a gloss), or "move to <place>". -->

## The document as a whole

### Terms

- <thing or term> — <names or meanings found, with places> → «<one name, or a definition built from the document's own uses, else ‹…›>» (rule <id>)

<!-- One item per term with two meanings or thing with several names (1a–1c), and each definition to add (1g, 1i), built from the document's own uses, else ‹…›. Line by line does not repeat them. -->

### Contradictions

- <finding line naming both places>

<!-- Rule 8a: two places that cannot both be true. The replacement carries both versions in a placeholder, never a choice between them. -->

### Growth areas

- <pattern, and why it matters to the reader> → <what to change>; places: <places>

<!-- A defect at three or more places, or a change to the whole document. The line findings of those places stay; the growth area lists the places. A fix order or a list of the top findings is not a growth area. -->

### Facts changed since the previous version

- <id, number, date, condition, limit or obligation> — was «<old>», now «<new>» | gone

<!-- Only with a previous version: compare the versions by requirement ids, numbers, dates, conditions, limits and obligations. -->

## Line by line

- <finding line>

<!-- Every other finding, one line each, in the reading order of the document. -->

## Still open

- <finding line> — raised in round <K>; <not fixed | partly fixed: what remains>

<!-- Only with a previous report: every unfixed repeat from an earlier round, a partial fix included, listed here instead of under Line by line. -->

## Typos

- <file>:<place> — «<was>» → «<should be>»

<!-- From the typo reviewer, plus typos the role reviewers noticed: typos, spelling, grammar, punctuation, semicolons. A slip repeated at many places is one item with its places. Never counted in scores and never cited in another section. -->

## About this review

- Document: <what it is>; files in reading order: <files>
- Readers: <who>; after reading they must be able to: <what>
- Reviewers: <role (blocks) — why it was chosen>; optional, not run: <role — why | none>; <confirmed by the user | not confirmed, the user could not be asked during this run>; <worked independently | worked one at a time in one shared context>
- Round <N>; threshold for the next round: <9.0 | 9.6>; status: <not met | met in rounds <N-1> and <N> | round 5 reached>
- Previous report: <path | none>; previous version: <path | none> <!-- Only with a previous report or version. -->
- Previous scores: <scores>; fixed since the last round: <places | none>; still open: <count> <!-- Only with a previous report. -->
- Checked with no findings: <role or rule block — what was checked>

<!-- A named reader with no matching role: name the row used for it, or the row written for it. -->
