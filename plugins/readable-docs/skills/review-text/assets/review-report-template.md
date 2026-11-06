<!--
Copy this template, replace every <slot>, follow the comments, then delete every comment, this one included.
Finding line, in Sections and order, Contradictions, Line by line and Still open: <file>:<place> — <blocking | wording> — <what is wrong, one sentence> → «<replacement>» (rule <id>; also at: <places>)
- <place> is a line number, or a section and item id where line numbers do not hold.
- The mark is blocking or wording by the definition in readability-rules.md, written in the report language.
- What is wrong is a defect of the document; a missing fact is stated as one and marked ‹…› in the replacement (3c).
- A replacement longer than two lines goes in a fenced block under the line.
- A defect at several places is one finding: "also at" names the other places, up to five, and is left out when a search of the whole document found none.
- Each finding stands alone: no finding numbers, no "see above", no references between findings.
Terms, Growth areas, Facts changed and Typos have their own lines, given in their sections.
Keep the sections in this order. A section or line whose comment starts with "Only" is left out when its condition is false; any other section stays, with "none found" when empty. No section of your own.
-->

# Readability review — <document name> — round <N>

<!-- In second-opinion mode the title is "Readability review — <document name> — round <N> — second opinion — <model>". -->

## Summary

| Role | Score 0–10 | Blocking findings | Where the reader first gets stuck |
|---|---|---|---|
| <role> | <score> | <number> | <place and a few words> |

<verdict on the document as a whole>

<!-- One row per role run, scored by its own reviewer, with one decimal; the number of blocking findings that block this role's reader, 0 included; "—" in the last column when nothing blocks the role. Then the verdict, a few plain sentences: whether the readers can act on the document, and which kinds of problems dominate. The verdict holds no finding, place, replacement or rule id: every finding lives in its own section below. -->

## Answers to remarks

| Remark | Agree or not, and why | Rule that covers it | Same defect elsewhere |
|---|---|---|---|
| <remark> | <answer> | <rule id | none> | <places, or none after checking> |

<!-- Only in human-pass mode: one row per remark the user brought. "Rule that covers it" names the rule of readability-rules.md under which the defect falls, or "none". -->

## Structure

### TL;DR for the top of the document

> <two or three lines, ready to paste>

<!-- Only when the opening of the document does not give the main point (document pass, item 2). -->

### Proposed order of the document

1. <part> — <what it holds>

<!-- The order the document's parts should take after the edits: the TL;DR when there is one, then context (what and why), then details. Say where each moved part comes from. Write the list even when nothing moves; for a document of one part (a single table or list), one line saying so instead of the list. -->

### Sections and order

- <finding line>

<!-- Findings on sections and order, in reading order: every section whose purpose cannot be stated, with a proposed opening sentence (7a); text that belongs elsewhere, a duplicate, an item of another kind (7b–7f); file names out of reading order (4i); a term or reference used before it is explained (4c, 4d), with the place where it is defined or the gloss at first use. After → comes the text to paste in «» (an opening sentence, a gloss), or "move to <place>". -->

## The document as a whole

### Terms

- <thing or term> — <blocking | wording> — <names or meanings found, with places> → «<one name, or a definition built from the document's own uses, else ‹…›>» (rule <id>)

<!-- One item per term with two meanings or thing with several names (1a–1c), and each definition to add (1g, 1i), built from the document's own uses, else ‹…›. Line by line does not repeat them. -->

### Contradictions

- <finding line naming both places>

<!-- Rule 8a: two places that cannot both be true. The replacement carries both versions in a placeholder, never a choice between them. -->

### Growth areas

- <pattern, and why it matters to the reader> → <what to change>; places: <places>

<!-- Each item is a pattern — one writing habit behind several different findings, with their places — or a change to the whole document, with a proposal. A defect repeated at several places is one finding with "also at", not a growth area, and a growth area never restates a finding's defect or replacement. A fix order or a list of the top findings is not a growth area. -->

### Facts changed since the previous version

- <id, number, date, condition, limit or obligation> — was «<old>», now «<new>» | gone

<!-- Only with a previous version: the facts compared in the document pass. -->

## Line by line

- <finding line>

<!-- Every other finding, one line each, in the reading order of the document. -->

## Still open

- <finding line> — raised in round <K>; <not fixed | partly fixed: what remains>

<!-- Only with a previous report: every unfixed repeat from an earlier round, a partial fix included, listed here instead of under Line by line. -->

## Typos

- <file>:<place> — «<was>» → «<should be>» (also at: <places>)

<!-- From the typo reviewer, plus typos the role reviewers noticed: typos, spelling, grammar, punctuation, semicolons. A slip repeated at many places is one item with its places. Kept in this section only (9a). -->

## About this review

- Document: <what it is>; files in reading order: <files>
- Readers: <who>; after reading they must be able to: <what>
- Reviewers: <role (blocks) — why it was chosen>; optional, not run: <role — why | none>; <confirmed by the user | not asked: the request names the readers | not asked: the answer would not change the set | not confirmed: the user could not be asked during this run>; <worked independently | worked one at a time in one shared context>
- Round <N>; blocking findings in this round: <number>; next round: <recommended after the blocking findings are fixed | not needed: no blocking findings (rounds 1 and 2) | stop: round 3 reached, blocking findings remaining: <places | none>>
- Previous report: <path | none>; previous version: <path | none> <!-- Only with a previous report or version. -->
- Previous scores: <scores>; fixed since the last round: <places | none>; still open: <count> <!-- Only with a previous report. -->
- Checked with no findings: <role or rule block — what was checked>

<!-- A named reader with no matching role: name the row used for it, or the row written for it. Blocking findings in this round is the number of distinct blocking findings: a finding that blocks two roles counts once here and in each role's row of the Summary. -->
