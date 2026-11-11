---
name: executive-decision-memo
description: Draft, review, and format official executive memorandums, decision records, policy directives, and formal letters using strict Bottom Line Up Front (BLUF) and structured hierarchy rules. Use whenever the user asks to write an executive memo, decision record, policy directive, or formal business letter.
---

# Executive Decision Memo & Correspondence Standard

Follow these standards whenever drafting or reviewing formal organizational correspondence, policy directives, and decision records.

## 1. Data Privacy & Security Guardrails
- **Never process confidential, restricted, or Personally Identifiable Information (PII)** unless operating inside an authorized internal environment.
- Replace real personal identifiers, account numbers, and sensitive internal endpoints with placeholders (e.g., `[FULL NAME]`, `[DEPT-CODE]`) when drafting in shared workspaces.

## 2. Core Writing Style
- **Bottom Line Up Front (BLUF):** State the main decision, recommendation, or purpose in the very first paragraph.
- **Active Voice:** Use active voice rather than passive voice (e.g., "The Engineering Director approved the budget," not "The budget was approved").
- **Conciseness:** Keep sentences short (aim for an average of 15 words or fewer) and paragraphs brief (under 5–6 lines).
- **Plain Language:** Use simple, everyday words and avoid unnecessary jargon. Spell out acronyms on first use (e.g., `Standard Operating Procedure (SOP)`), except for universally known terms like `API` or `SLA`.

## 3. Formatting Rules
- **Spacing:** Single-space within paragraphs; double-space between paragraphs.
- **Dates:** Format dates unambiguously as `DD Month YYYY` (e.g., `11 November 2026`) for internal memorandums, or standard format (`November 11, 2026`) for external letters.
- **Paragraph Numbering:**
  - `1.` (flush left)
  - `a.` (indented 0.25 in / 4 spaces)
  - `(1)` (indented 0.50 in / 8 spaces)
  - `(a)` (indented 0.75 in / 12 spaces)
  - *Rule:* Never have a `1.` without a `2.`, or an `a.` without a `b.` (if there is only one sub-point, integrate it into the parent paragraph).

## 4. Authorized Document Types
1. **Memorandum (`MEMORANDUM TO:`):** Used for internal organizational directives and decisions. Requires a `DEPARTMENT CODE` (e.g., `ENG-INF-01`), `SUBJECT:` in ALL CAPS, and a reference ID if applicable.
2. **Decision Record (`DECISION RECORD`):** Used to document internal meetings, architecture reviews, phone calls, or leadership approvals.
3. **External Letter:** Used for formal correspondence outside the organization (vendors, regulators, partners). Includes a salutation (`Dear Mr./Ms. [Name]:`) and complimentary close (`Sincerely,`). Do **not** include internal department codes on external letters.

## 5. Sign-Off Blocks
- Align the sign-off block to the right half of the page, 4–5 lines below the last line of text.
- Format:
  ```text
  FIRST M. LAST
  Title / Role
  Department / Division
  ```
- List `Attachments` flush left on the same line as the first line of the sign-off block if supporting documents exist.

## Workflow
1. Identify the document type (Memorandum, Decision Record, or External Letter).
2. Read `references/memo-template.md` if generating a standard memorandum layout.
3. Draft the content strictly adhering to BLUF, active voice, and paragraph-numbering rules.
4. Verify that no single subdivisions exist (e.g., `1.a.` without `1.b.`).
