# Planning rules

## From the reader's way to sections

Start from the reader, not from a template and not from the kinds of facts you hold. List the steps the reader goes through to the result, in the order they go (`form-rules.md`, The build). Each step is one section; its heading names the question the reader has at that step. A step the sources have nothing for is skipped, or becomes an open question if the reader cannot do without it.

Then place every fact at the step where the reader uses it, the facts the reader's questions brought up included (`reader-checklists.md`), as `form-rules.md`, The build, says. Each answer the reader takes away as one is one section; the plan names its closing line where Devices allows one, otherwise none. When the text asks for a yes, the first row holds the facts that meet the reader's criteria, and the obstacle is planned with the facts that answer it (`form-rules.md`, When the text asks for a yes).

When the user gives a template, its sections are a frame (`form-rules.md`, Devices); each still needs a step, a content type and sources.

In each plan row, name the known content the reader needs to take away and its sources, not just the source filenames. Before drafting, walk the materials and answers back to the rows: a fact the reader needs that is missing from every row is a plan defect, even when the planned sections look complete (SKILL.md, Nothing known is lost). Details unrelated to the reader's task stay out.

A section without a step is not written, whatever headings the template has. A step without a section is a gap: add the section or an open question. A section that would hold only open questions or restate others is not written (`form-rules.md`, Each figure once).

## The first screen

The first row of the plan is the first screen (`form-rules.md`, The first screen): the main thing in prose, and only the devices whose condition holds. When it has an overview or a comparison table, plan the figures it holds and their status words; the sentence after the table states differences and consequences, and the figures are derived in the appendix when the text has one, otherwise in the sentence that uses them.

## Several readers

When the text has readers on two sides, the plan names the reader of each section and puts what both need (purpose, shared facts, shared dates) in one short shared part before the parts for each. Each reader's part follows that reader's way. For the external reader, also plan what is asked of them and by when, where the sources give it; where they do not, an open question.

## Content type per section

Pick the content type by what the reader does with it:

- **list** — an enumeration, steps in order, a set of conditions;
- **table** — a comparison, a correspondence (field ↔ field, side ↔ duty), several items with the same attributes;
- **diagram** — a flow, states and transitions, who talks to whom;
- **text** — reasoning, context, the consequences of a choice.

The plan names the content type; what renders it is decided by the output format and the tools at hand: a plain-text file holds text and simple lists only; markdown, a wiki page or a shared document hold tables; a diagram is drawn where diagrams render (for example, a mermaid block in markdown), otherwise described as a numbered sequence or a transition table. Say in the picture which format you assume; the user corrects it.

## Order and names

Each section may rely only on what the reader has already read. Things and people are named as `form-rules.md` says (The reader's words; People); a term the reader has no word for is defined where it first appears or earlier, the overview table included. A forward reference to the appendix or a table is fine when the current sentence is understandable without following it; "see below" in place of a definition is not.

## The plan

For each section: the step of the reader's way, its reader when there are several, its content type, the known content and the sources that cover it (by file or answer), the figures it states in full, the open questions that will remain in it (`form-rules.md`, Open questions). By default the plan is the "Plan" table of the cycle report; a separate `plan.md` from `../assets/document-plan-template.md` only when the request asks for a plan and its check. Devices such as numbered clauses with cross-references, a metadata header, an "out of scope" table or a "who does what" table are used when the reader's task calls for them, never by default.

Walk the check of `form-rules.md` (The check) on the plan before the draft; an independent run walks it only when the request asks for a plan check.

## When the materials are thin

Say so in the picture, list what is missing, and still write the text: every missing fact the gate keeps is an open question with who decides it, merged with its neighbours (`form-rules.md`, Open questions, Count). A thin text with honest gaps beats a full text with invented facts.
