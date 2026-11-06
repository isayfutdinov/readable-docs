# Readability rules

The orchestrator reads it before its document pass and sends it whole to every reviewer, whose brief names the blocks that reviewer applies. Every rule has an id (1a, 4c …), and a finding cites it; 10a, at the end, governs every proposal to cut or shorten, in every role. An example illustrates its rule; it is not the only case the rule covers. Examples are in English; apply each rule in the language of the document's body text.

**Finding.** A finding is a concrete defect for the reader: something they could misunderstand, have to reconstruct, miss, or spend effort finding or reading. A stylistic preference alone is not one. A place where the reader must guess is a finding even when the likely reading is correct.

**Blocking.** A finding is blocking when, without the fix, the reader cannot make a decision or perform an action: a fact the reader needs is missing, two readings lead to different decisions or actions, or two places contradict each other on what to do. Every other finding is wording.

## How to check: the document pass and three reviewer passes

The orchestrator makes the document pass; each reviewer makes the three passes over the blocks its brief names. Every pass reads diagrams as text (4l).

**Document pass** (orchestrator: block 7, and 1a across the document). Made for the purpose and readers set at Intake.
1. Check whether the document answers the question its readers bring. The answer goes into the verdict of the Summary; a question the document leaves unanswered is named there, without a place.
2. Check the order of parts (context before details) and whether the opening gives the main point (4a); a heading is the opening when it names what the reader must decide or do. Only when the opening does not give the main point, write a TL;DR to paste at the top: two or three lines in the document's own words and facts that give the main point by 4a, never a description of the document, a list of its parts or a summary of the review.
3. Go through the sections in reading order and write one line for each: "This section answers: …". If you cannot write it, that is a 7a finding; it goes into the report whether or not a reviewer raises it. Then check that the title names that question, the first sentence answers it, no text answers another question and nothing repeats another section (7b–7f).
4. Note every term the document uses in more than one sense across its sections (1a).
5. With a previous version, compare the facts of the two versions: requirement ids, numbers, dates, conditions, limits and obligations.

**Reviewer passes.** Each pass finds what the others miss, so make every pass that holds one of your blocks.
1. **Section pass** (block 4). Go through the sections in reading order: no term comes before its definition, no reference points forward, a paragraph's first sentence carries its point, a flow told as a story is numbered steps (4h).
2. **Sentence pass** (blocks 1–6, 8). Read each sentence as the reader who must act on it: who does what, when, under which condition, with what result; what is missing; what reads two ways; what adds nothing. A sentence that word swaps cannot fix is rewritten whole (4k).
3. **Inventory pass** (blocks 1 and 5). List every term and name with the places it appears, glossary entries, headings, table rows, diagram labels, legends and letter codes included, and every limit, retry count, prohibition and known constraint. A thing with two names and a limit with no consequence are findings; a term with two meanings is the document pass's (1a) — note it for the orchestrator, do not score it.

## 1. Terms — the reader must not wonder "is this the same thing?"
- **1a** One term, one meaning in the whole document or set. Two meanings for one word make the reader re-read.
- **1b** One thing, one name: no synonyms for variety, no ornate turns of phrase, and no company or system name standing in for the role it plays. A technical document is not a novel; a new word signals a new thing.
- **1c** Before merging two "synonyms", check every use: if they name two different things, the defect is the reverse, one name for two things, and each thing needs a name of its own. Merging them would hide the difference the reader needs.
- **1d** When the document or its glossary gives an established term for a thing, the text uses it, not a term invented for the same thing.
- **1e** When the text names a person who acts, decides or is to be contacted, the reader must be able to match the name to the person: at first mention give the name and the role ("Omar Haddad, release manager"), then keep one designation (1b). A first name alone, or a role that several people hold, leaves the reader not knowing whom to go to; where the document lacks the name or the role, the replacement has a placeholder.
- **1f** A long name appears once in full, then gets a short form used everywhere after.
- **1g** A term is defined in the document or is obvious to the stated audience; its place in the text is 4c's rule. A glossary, if given, is the source of definitions; propose additions in the report, never edit the glossary.
- **1h** Check every glossary entry, heading, table row and diagram label, not only the terms used most: readers navigate by them, and a defect there survives every re-read of the body.
- **1i** A glossary entry defines one thing and states its boundary: what counts and what does not.
- **1j** A glossary entry and the rules that use its term say the same thing.
- **1k** A heading names its subject: "Settings" → "Administrator notification settings".
- **1l** Letters, colours and short labels on a diagram are explained on the diagram, with as few keys as possible, and match the names in the text: the reader looks at the picture before the text.
- **1m** System terms are ones the stated reader can recognize; unexplained slang or jargon gets a gloss at first use, taken from the document, else a placeholder ‹…›.
Example: "The operator checks the application; then the specialist reviews the documents; then the employee makes a decision." → if the document means one role, one name: "The operator checks the application, reviews the documents and makes a decision." If it means three roles, each keeps its own name everywhere. If the document does not say which, that is the defect, and a placeholder ‹role› stands where the name goes.

## 2. Actions — the reader must know who does what, and when
- **2a** Every action names the actor, the action and the moment or condition; add why and the result where the reader would otherwise guess. If the document does not say why, the finding says so and a placeholder ‹reason› marks the missing fact; it does not supply a reason.
- **2b** An action is a verb, not a noun made from one: "check", not "perform a check"; "approve", not "perform an approval".
- **2c** Instruction steps are imperative or name the actor; in requirements "the system shall" stays.
- **2d** No stacks of modal and auxiliary verbs: "might have had to" → one tense, one modality.
- **2e** "may" or "can" in a rule says whether the step is required, optional or a permission: "The user can confirm their email" leaves the reader unsure whether anything waits for it.
- **2f** A rule that allows something under a condition says what happens when the condition is not met: what the user sees, what the system does. Otherwise every reader invents the other branch, and each invents a different one.
Example: "Rejection results in the application being transferred." → "After rejection, the operator manually transfers the application to the supervisor." only if the document says who, to whom and how; otherwise "After rejection, ‹who› transfers the application to ‹whom›.", and the finding states the gap: "the text does not say who transfers the application to whom after rejection".

## 3. Completeness — shortening must not remove meaning
- **3a** Keep every word that carries meaning: subject, verb, object, condition, number, qualifier ("only", "automatically", "internal", "if …", "after …"). A number or a date keeps its scope: a deadline given for one step is not the deadline of the whole. A sentence cut to a label makes the reader reconstruct it, and reconstructions differ. This holds for replacement text too: one wording for several places keeps the conditions of each place.
- **3b** A hedge stays a hedge: "possibly" never becomes a fact.
- **3c** Replacement text adds no fact absent from the document: no number, date, cause or frequency, and no actor, step, order, destination, permission, state change, alternate flow or failure path. A cause also hides in a linking word ("therefore", "so", "because") or in a colon that joins two facts, and an actor in a generic subject ("the platform", "the system") where the document names none. Where information is missing, the finding names the missing fact as the defect, and a placeholder ‹…› marks the missing fact: a word or two (‹who›, ‹duration›), or the versions the document gives (‹5|10›), never a guess or a question. A pasted replacement becomes the document, so whatever it adds becomes a rule nobody decided.
- **3d** A word that points outside the text or to an unnamed set ("the usual process", "elsewhere", "today") names what it points to: the reader does not share the author's context.
- **3e** A list that presents itself as complete ("all", "the following", "supported") holds everything the document names elsewhere, or says that it is partial: the reader takes it as complete.
- **3f** A step "before X" says whether X waits for it (a condition) or only comes later (a time): the two lead the reader to different actions.
- **3g** A transfer, a payment or a handover names what moves, from where, to whom, and who starts it: each missing part is a question the reader has to take to someone.
Example: "Limit of 5 per day, otherwise blocked." → "If the user issues more than five cards in a day, the system blocks issuance until the next day." Only when the document states both halves; a part it does not state stays a placeholder: "…the system blocks issuance for ‹duration›".

## 4. Order and cohesion — the reader must never need what comes later
- **4a** The opening of a document, a section or a paragraph gives its reader the main point first: the answer, the result, or what the reader must decide or do; details follow. In a text that asks the reader for a yes, the opening gives what meets the reader's criteria; what is missing comes after.
- **4b** One paragraph, one topic; one list item, one rule. A paragraph that mixes how something works with its known problems, or an item that mixes two rules, leaves the reader to sort them.
- **4c** Define before use. No forward references ("see below", "as described later"): move the definition up or restate the needed part here. A glossary later in the reading order is not a definition before first use: the reader meets the term first and has to guess, so give a one-clause gloss at first use; the full definition stays in the glossary.
- **4d** Spell out references: "BR-12 (document no older than 90 days)", not "BR-12"; a ticket number, a commit or a version says what it is; a link gets a label that says what is behind it.
- **4e** Where the reader has to infer how two sentences relate, a linking word ("then", "in addition", "but") names the relation the document establishes; a relation it does not establish stays a placeholder ‹…› (3c).
- **4f** Condition before action: "If X, do Y", not "Do Y if X". The reader acts as they read.
- **4g** Three or more items, steps or conditions go in a list.
- **4h** A scenario told in prose becomes numbered steps, each naming its actor; a precondition comes before the steps. In a story the reader has to find the steps, their order and who takes each, and every reader splits it differently.
- **4i** File names of a set sort in reading order: file trees and menus sort them as text, so step-10 lands before step-2; number with leading zeros (step-02).
- **4j** A note informs; it never hides an instruction.
- **4k** A sentence the reader has to read twice to understand, and that swapping single words does not fix, gets a whole new sentence as its replacement: a sentence patched word by word still has to be read twice.
- **4l** A diagram is text, read with the prose around it: its step names are the names the text gives those steps, its legend matches the colours and shapes actually drawn, its letters and codes follow 1l, and a note in the diagram's source that the rendered picture does not show moves into visible text. The reader looks at the picture first, so where picture and prose disagree, report the disagreement under 8a.
Example: "The application moves to Review status (see section 5)." The status is used in section 2 and defined only in section 5 → "The application moves to Review status — awaiting an operator check; all statuses are in section 5." The gloss is taken from the definition in section 5, not invented.

## 5. Warnings and prohibitions — the reader must know what happens if they ignore one
- **5a** A warning starts with the command or the condition and states the consequence: "Do not change X, otherwise Y", never a bare "Do not change X". A prohibition without a consequence is ignored or over-applied.
- **5b** A limit, a retry count, a missing guarantee or a known constraint is a warning too: say what goes wrong because of it, what happens when it is reached, and what the reader does then. "The system retries sending three times" also needs what happens after the third failure and who acts then. Most of these are not worded as warnings: find them in the inventory pass.
- **5c** A prohibition the reader can break by mistake says what to do once it is broken: whom to tell, what to change.

## 6. Filler and decoration — "sounds reasonable" is not the same as "says something"
- **6a** Filler is text with no fact, decision, condition or instruction: greetings, restated questions, "in conclusion", "it is worth noting". Context that explains what and why is not filler.
- **6b** Test every paragraph and table: what does it add that its neighbour does not? Nothing means filler: a paragraph that retells the table under it, a table whose point the text never states.
- **6c** A sentence that repeats its subject as its news is filler: "The reporting module generates reports" tells the reader nothing new. Keep what the document says about which reports, for whom and when; what it does not say is a placeholder.
- **6d** A marketing adjective ("robust", "seamless") is removed or replaced by a measurable fact the document itself gives; where the document gives none and the claim matters, a placeholder ‹…› names the missing measure.
- **6e** A chain of hedges and qualifiers collapses into one hedge of the same strength: "it might possibly be expected to" → "it may". It never becomes a statement of fact (3b).
- **6f** A claim attributed to an unnamed source ("experts believe", "it is known") names the source the document gives, or a placeholder ‹source› stands for it.

## 7. Structure — every section answers one question, and its title names it
- **7a** If the reader cannot say what a section is for, that is a finding: propose the opening sentence that says it, or the place where its content belongs.
- **7b** A section that selects (the main cases, key examples, a short list) says what it selected and why, so the reader knows what is left out.
- **7c** Text that another reader or another document needs, and the reader of this section does not, moves there or becomes a link (release notes of an old version inside a user guide): the reader who needs it will not look here.
- **7d** The same fact twice (a paragraph and a table, two sections, this document and the one it summarises) stays in one place, and the other place links to it: copies drift apart, and the reader cannot tell which one is current.
- **7e** An item of another kind in a list or table (a deadline among the requirements) moves to a list of its own kind.
- **7f** Two sections or categories whose difference the reader cannot state ("Notes" and "Remarks") get the difference written down or are merged.
Example: for a section titled "Notifications", the line "This section answers: …" cannot be written, because its paragraphs alternate between the events that notify the user and the support team's on-call rota. Proposal: the opening sentence "This section lists the events that send the user a notification.", and the rota moved to the operations section.

## 8. Consistency — the reader must not have to choose which place to believe
- **8a** Two statements that cannot both be true (a status and the requirements, a diagram and its table, a rule and its comment, a summary and its details) are one finding with both places. Report it because the reader stumbles on it; which version is right is the author's call, so the replacement carries both versions in a placeholder, not a choice.
- **8b** A word or phrase that gives a sentence a second reading is a finding: quote both readings. The replacement keeps one reading only when the document establishes it elsewhere; otherwise it carries both in a placeholder ‹A|B›.
Example: section 1 says "a limit of 5 cards per day", the table in section 4 says "10 cards per day". One finding with both places: the defect is "section 1 and the table in section 4 state different limits", and the replacement in both is "‹5|10› cards per day".

## 9. Typos, spelling, grammar, punctuation
- **9a** Typos, spelling, grammar and punctuation are checked by the typo reviewer, reported in their own block and never counted in role scores.
- **9b** Semicolons count: a semicolon usually hides two sentences.
- **9c** A role reviewer that notices a typo passes it to this block.

## 10. Volume — shorter must not mean less
- **10a** Remove filler, keep every word the reader needs; telegraphic style is a defect, not a fix. Propose a cut only for text that carries nothing the reader needs (block 6); where the document has none, propose no cut. A replacement for a whole paragraph, a table or several places that comes out shorter is checked against the original condition by condition: losses hide in large replacements.
