# Readability rules

The orchestrator reads it before its document pass and sends it whole to every reviewer, whose brief names the blocks that reviewer applies. Every rule has an id (1a, 4c …), and a finding cites it; Volume, at the end, governs every proposal to cut or shorten. Numbers in brackets are ASD-STE100 Issue 9 rules; A-numbers are this skill's own additions. Examples mix Russian and English; apply each rule in the language of the document's body text. Every rule says why: a reviewer that knows the reason finds the cases the examples do not show.

## How to check: the document pass and three reviewer passes

The orchestrator makes the document pass; each reviewer makes the three passes over the blocks its brief names. Diagrams and schemes are text: every pass reads their labels, legends, step names and codes with the prose around them (4l).

**Document pass** (orchestrator: block 7, and 1a across the document). Made with what the user asked: who the readers are and what they must be able to do after reading.
1. State the document's purpose and readers, and whether it answers the question those readers bring.
2. Check the order of parts (TL;DR, context, details) and write the TL;DR.
3. Go through the sections in reading order and write one line for each: "This section answers: …". If you cannot write it, that is a 7a finding with a proposed opening sentence, and it goes into the report even when no reviewer raises it. Then check that the title names that question, the first sentence answers it, no text answers another question and nothing repeats another section (7b–7f).
4. Note every term the document uses in more than one sense across its sections (1a).

No sentence pass and no inventory of every term here: those are the reviewers' passes, and consolidation merges their findings with the document pass's.

**Reviewer passes.** Each pass finds what the others miss, so make every pass that holds one of your blocks.
1. **Section pass** (block 4). Go through the sections in reading order: no term comes before its definition, no reference points forward, a paragraph's first sentence carries its point, a flow told as a story is numbered steps.
2. **Sentence pass** (blocks 1–6, 8). Read each sentence as the reader who must act on it: who does what, when, under which condition, with what result; what is missing; what reads two ways; what adds nothing. A sentence that word swaps cannot fix is rewritten whole (4k); a scenario told as a story becomes numbered steps (4h) — where you hold block 4.
3. **Inventory pass** (blocks 1 and 5). List every term and name with the places it appears, glossary entries, headings, table rows, diagram labels, legends and letter codes included, and every limit, retry count, prohibition and known constraint. A thing with two names and a limit with no consequence are findings; a term with two meanings is the document pass's (1a) — note it for the orchestrator, do not score it.

## 1. Terms — the reader must not wonder "is this the same thing?"
- **1a** One term, one meaning in the whole document or set [1.3]. Two meanings for one word make the reader re-read.
- **1b** One thing, one name: no synonyms for variety, no ornate turns of phrase, and no company or system name standing in for the role it plays. A technical document is not a novel; a new word signals a new thing [1.11, 1.14, 9.4].
- **1c** Before merging two "synonyms", check every use: if they name two different things, the defect is the reverse, one name for two things, and each thing needs a name of its own. Merging them would hide the difference the reader needs.
- **1d** Terms are the ones the company, product or industry already uses, not invented for this text [1.8].
- **1e** No slang, nicknames or jargon as terms: name systems and people by name and role [1.10], even when the whole team knows the nickname, because the next reader is not on the team.
- **1f** A long name appears once in full, then gets a short form used everywhere after [2.2].
- **1g** A term is defined before its first use or is obvious to the stated audience. A glossary, if given, is the source of definitions; propose additions in the report, never edit the glossary.
- **1h** Check every glossary entry, heading, table row and diagram label, not only the terms used most: readers navigate by them, and a defect there survives every re-read of the body.
- **1i** A glossary entry defines one thing and states its boundary: what counts and what does not. History and migration notes go elsewhere. An "also called" line adds a second name.
- **1j** A glossary entry and the rules that use its term say the same thing.
- **1k** A heading names its subject: "Настройки" → "Настройки уведомлений для администратора".
- **1l** Letters, colours and short labels on a diagram are explained on the diagram, with as few keys as possible, and match the names in the text: the reader looks at the picture before the text.
Example: "Оператор проверяет заявку; затем специалист смотрит документы; потом сотрудник принимает решение." → if the document means one role, one name: "Оператор проверяет заявку, смотрит документы и принимает решение." If it means three roles, each keeps its own name everywhere. If the document does not say which, that is the defect, and a placeholder ‹роль› stands where the name goes.

## 2. Actions — the reader must know who does what, and when
- **2a** Every action names the actor, the action and the moment or condition; add why and the result where the reader would otherwise guess [3.6, 3.7]. If the document does not say why, the finding says so and a placeholder ‹причина› marks the missing fact; it does not supply a reason.
- **2b** An action is a verb, not a noun made from one: "проверить", not "осуществить проверку"; "approve", not "perform an approval" [3.7].
- **2c** Instruction steps are imperative or name the actor; in requirements "the system shall" stays [5.3 inside 3.6].
- **2d** No stacks of modal and auxiliary verbs: "может быть должна была" → one tense, one modality [3.4].
- **2e** "может", "may" or "can" in a rule says whether the step is required, optional or a permission: "Пользователь может подтвердить email" leaves the reader unsure whether anything waits for it.
- **2f** A rule that allows something under a condition says what happens when the condition is not met: what the user sees, what the system does. Otherwise every reader invents the other branch, and each invents a different one.
Example: "Отказ приводит к передаче заявки." → "После отказа оператор передаёт заявку старшему вручную." only if the document says who, to whom and how; otherwise "После отказа ‹кто› передаёт заявку ‹кому›.", and the finding states the gap: "не сказано, кто и кому передаёт заявку после отказа".

## 3. Completeness — shortening must not remove meaning
- **3a** Keep every word that carries meaning: subject, verb, object, condition, number, qualifier ("только", "автоматически", "внутренних", "если …", "после …"; "only", "automatically", "internal") [4.2, A3]. A number or a date keeps its scope: a deadline given for one step is not the deadline of the whole. A sentence cut to a label makes the reader reconstruct it, and reconstructions differ. This holds for replacement text too: one wording for several places keeps the conditions of each place.
- **3b** A hedge stays a hedge: "возможно" never becomes a fact [A4].
- **3c** Replacement text adds no fact absent from the document: no number, date, cause or frequency, and no actor, step, order, destination, permission, state change, alternate flow or failure path [A5]. A cause also hides in a linking word ("поэтому", "потому что", "so", "because") or in a colon that joins two facts, and an actor in a generic subject ("платформа", "the system") where the document names none. Where information is missing, the finding names the missing fact as the defect, and a placeholder ‹…› marks the missing fact: a word or two (‹кто›, ‹срок›), or the versions the document gives (‹5|10›), never a guess or a question. A pasted replacement becomes the document, so whatever it adds becomes a rule nobody decided.
- **3d** A word that points outside the text or to an unnamed set ("текущая схема", "в другом регионе", "некоторые изменения", "today", "the old way") names what it points to: the reader does not share the author's context.
- **3e** A list that presents itself as complete ("all", "the following", "поддерживаются") holds everything the document names elsewhere, or says that it is partial: the reader takes it as complete.
- **3f** A step "before X" ("до X") says whether X waits for it (a condition) or only comes later (a time): the two lead the reader to different actions.
- **3g** A transfer, a payment or a handover names what moves, from where, to whom, and who starts it: each missing part is a question the reader has to take to someone.
Example: "Лимит 5 в день, иначе блокировка." → "Если пользователь выпускает больше пяти карт в день, система блокирует выпуск до следующего дня." Only when the document states both halves; a part it does not state stays a placeholder: "…система блокирует выпуск на ‹срок›".

## 4. Order and cohesion — the reader must never need what comes later
- **4a** The first sentence gives the answer or the result [A1]: what the subject is and does, before what it does not do. The first sentence of a paragraph carries its main point, details follow (STE section 6).
- **4b** One paragraph, one topic; one list item, one rule. A paragraph that mixes how something works with its known problems, or an item that mixes two rules, leaves the reader to sort them.
- **4c** Define before use. No forward references ("см. ниже", "as described later"): move the definition up or restate the needed part here. A glossary later in the reading order is not a definition before first use: the reader meets the term first and has to guess, so give a one-clause gloss at first use; the full definition stays in the glossary.
- **4d** Spell out references: "BR-12 (документ не старше 90 дней)", not "BR-12"; a ticket number, a commit or a version says what it is; a link gets a label that says what is behind it.
- **4e** Linking words show the logic between sentences: "поэтому", "тогда", "кроме того", "so", "but" [4.4].
- **4f** Condition before action: "Если X, сделайте Y", not "Сделайте Y, если X" [5.4]. The reader acts as they read.
- **4g** Three or more items, steps or conditions go in a list [4.3].
- **4h** A scenario told in prose becomes numbered steps, each naming its actor; a precondition comes before the steps. In a story the reader has to find the steps, their order and who takes each, and every reader splits it differently. Look for it in any long paragraph that describes a flow, not only in sections called scenarios.
- **4i** File names of a set sort in reading order: file trees and menus sort them as text, so step-10 lands before step-2; number with leading zeros (step-02).
- **4j** A note informs; it never hides an instruction [5.5].
- **4k** If swapping single words does not fix a sentence, restructure it [9.1]. A clumsy sentence (a heavy turn of phrase, a chain of nouns, a word that adds nothing) gets a whole new sentence as its replacement: a sentence patched word by word still has to be read twice.
- **4l** A diagram is text, read with the prose around it: its step names are the names the text gives those steps, its legend matches the colours and shapes actually drawn, its letters and codes follow 1l, and a note in the diagram's source that the rendered picture does not show moves into visible text. The reader looks at the picture first, so where picture and prose disagree, report the disagreement under 8a.
Example: "Заявка переходит в статус Review (см. раздел 5)." The status is used in section 2 and defined only in section 5 → "Заявка переходит в статус Review — ждёт проверки оператором; все статусы — в разделе 5." The gloss is taken from the definition in section 5, not invented.

## 5. Warnings and prohibitions — the reader must know what happens if they ignore one
- **5a** A warning starts with the command or the condition [7.2] and states the consequence [7.3]: "Не меняйте X, иначе Y", never a bare "Не меняйте X". A prohibition without a consequence is ignored or over-applied.
- **5b** A limit, a retry count, a missing guarantee or a known constraint is a warning too: say what goes wrong because of it, what happens when it is reached, and what the reader does then. "Система повторяет отправку три раза" also needs what happens after the third failure and who acts then. Most of these are not worded as warnings: find them in the inventory pass.
- **5c** A prohibition the reader can break by mistake says what to do once it is broken: whom to tell, what to change.

## 6. Filler and decoration — "sounds reasonable" is not the same as "says something"
- **6a** Filler is text with no fact, decision, condition or instruction: greetings, restated questions, "в заключение", "it is worth noting". Context that explains what and why is not filler [A2].
- **6b** Test every paragraph and table: what does it add that its neighbour does not? Nothing means filler: a paragraph that retells the table under it, a table whose point the text never states.
- **6c** A sentence that repeats its subject as its news is filler: "Модуль отчётов формирует отчёты" tells the reader nothing new. Keep what the document says about which reports, for whom and when, or ask.
- **6d** Marketing adjectives ("бесшовный", "robust", "seamless") are removed or replaced by a measurable fact [A6].
- **6e** A chain of hedges and qualifiers collapses into one clear statement [A8].
- **6f** AI-writing patterns to flag: significance inflation ("критически важный" for an ordinary step), synonym cycling (see 1b), vague attributions ("эксперты считают"), filler (see 6a), generic conclusions ("в заключение").

## 7. Structure — every section answers one question, and its title names it
- **7a** If the reader cannot say what a section is for, that is a finding: propose the opening sentence that says it, or the place where its content belongs. Every section for which the document pass cannot write "This section answers: …" is such a finding; the orchestrator adds it even when no reviewer raises it, because no single role owns that question.
- **7b** A section that selects (the main cases, key examples, a short list) says what it selected and why, so the reader knows what is left out.
- **7c** Text that belongs elsewhere moves there or becomes a link: decision history inside a description of the current state, corrections or instructions for another document, internals of a neighbouring system. The reader of this section does not need it, and the reader who needs it will not look here.
- **7d** The same fact twice (a paragraph and a table, two sections, this document and the one it summarises) stays in one place, and the other place links to it: copies drift apart, and the reader cannot tell which one is current.
- **7e** An item of another kind in a list or table (a work ticket among documents, a person among systems, an advantage among limitations) moves to a list of its own kind.
- **7f** Two sections or categories whose difference the reader cannot state (risks and issues, constraints and assumptions) get the difference written down or are merged. A section that continues another sits next to it.
Example: for a section, the line "This section answers: …" cannot be written, because it describes the current process and, in the same paragraphs, how that process was chosen. Proposal: an opening sentence that states the section's question, and the paragraphs of decision history moved to a "Decisions" section.

## 8. Consistency — the reader must not have to choose which place to believe
- **8a** Two statements that cannot both be true (a status and the requirements, a diagram and its table, a rule and its comment, a summary and its details) are one finding with both places. Report it because the reader stumbles on it; which version is right is the author's call, so the replacement carries both versions in a placeholder, not a choice.
- **8b** A word that gives a sentence a second reading is a finding: a qualifier that changes the claim, a phrase that suggests another arrangement, a feature that reads as a failure. Quote both readings and propose wording with one.
Example: section 1 says "лимит 5 карт в день", the table in section 4 says "10 карт в день". One finding with both places: the defect is "раздел 1 и таблица раздела 4 называют разный лимит", and the replacement in both is "‹5|10› карт в день".

## 9. Typos, spelling, grammar, punctuation
- **9a** Typos, spelling, grammar and punctuation are checked by the cheap reviewer, reported in their own block and never counted in role scores.
- **9b** Semicolons count: a semicolon usually hides two sentences [8.1].
- **9c** A role reviewer that notices a typo passes it to this block; it never appears outside the typo section.

## Volume
Remove filler, keep every word the reader needs. Telegraphic style is a defect, not a fix. If the document does not shrink in substance, do not propose cutting. A replacement for a whole paragraph, a table or several places that comes out shorter is checked against the original condition by condition: losses hide in large replacements.
