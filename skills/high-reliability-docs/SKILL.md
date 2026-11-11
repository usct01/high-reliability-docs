---
name: high-reliability-docs
description: Orchestrate and combine high-reliability documentation standards across executive correspondence, operational action plans, zero-ambiguity SOPs, and verifiable engineering specifications. Use whenever drafting complex operational documents, technical directives, runbooks, incident playbooks, or policy memos that require strict structure and zero ambiguity.
---

# High-Reliability Documentation Orchestrator

Use this meta-skill to select, route, and combine specialized documentation standards into a single cohesive document.

## 1. The Container + Content Architecture
Never apply two outer document layouts at once. Instead, pair one **Container Standard** (outer structure) with one or more **Content Standards** (inner writing rules):

- **Container Standards (Choose ONE for outer layout):**
  1. `executive-decision-memo`: Formal leadership decisions, policy directives, approvals, and official records.
  2. `goal-action-plan`: Multi-team execution plans, incident response, product launches, and crisis management.
  3. `clear-spec-writer`: Standalone engineering specifications, PRDs, and SLAs.
  4. `zero-ambiguity-sop`: Standalone operator manuals, runbooks, and maintenance SOPs.

- **Content Standards (Stack as needed inside sections):**
  - Use **`zero-ambiguity-sop` rules** inside any *How-To*, *Execution Step*, or *Runbook* section (20-word limit, active voice, imperative mood, `CRITICAL`/`CAUTION` callouts before steps).
  - Use **`clear-spec-writer` rules** inside any *Policy*, *Criteria*, *SLA*, or *Constraint* section (`SHALL`, `SHOULD`, `MAY`, measurable thresholds, unique IDs).
  - Use **`executive-decision-memo` BLUF rules** for all *Executive Summaries*, *Purpose* paragraphs, and *Leadership Intent* blocks.

## 2. Routing & Combination Matrix

| User Request Type | Container Skill (Layout) | Content Skill(s) to Inject | How to Merge |
| :--- | :--- | :--- | :--- |
| **Technical Policy / Approval Memo** | `executive-decision-memo` | `clear-spec-writer` | Use memo header, BLUF, and `1. / a. / (1)` numbering. Write policy rules using `SHALL`/`SHOULD` and verifiable metrics. |
| **Incident Playbook / Outage Plan** | `goal-action-plan` | `zero-ambiguity-sop` | Use the 5-section action plan structure. Format Section 3 (*Execution*) recovery steps using imperative rules and `CRITICAL`/`CAUTION` callouts. |
| **Engineering SOP with Compliance Rules** | `zero-ambiguity-sop` | `clear-spec-writer` | Use procedural steps and hazard headers. Add a *Conformance & Verification* section using requirement IDs (`REQ-001`). |
| **Launch Readiness / Release Plan** | `goal-action-plan` | `clear-spec-writer` + `zero-ambiguity-sop` | Use the 5-section action plan. Put Release Gate criteria (`SHALL`) in *Coordinating Instructions*, and SOP checklists in *Execution*. |
| **Audit / Rewrite Existing Document** | *Match source format* | All applicable standards | Run a 3-pass audit: (1) Fix structure/BLUF, (2) Replace vague words with `SHALL` + metrics, (3) Convert passive steps to active imperative. |

## 3. Conflict Resolution Rules
1. **Hazard Callouts Always Win:** Regardless of the container format, `CRITICAL` and `CAUTION` blocks **must** always appear immediately *before* the step or paragraph they protect.
2. **Outer Numbering Wins:** If using `executive-decision-memo` as the container, follow its paragraph numbering (`1.`, `a.`, `(1)`) and spacing rules, even when embedding `SHALL` statements.
3. **Sentence Length Scope:** Apply the **20-word sentence cap** strictly to *procedural action steps* and *BLUF opening sentences*. Requirement statements (`SHALL`) may exceed 20 words if needed to state exact measurable conditions and verification criteria.
4. **Acronym Consistency:** Always spell out acronyms on first use (`Standard Operating Procedure (SOP)`), except for standard terms authorized by the container (`BLUF`, `SHALL`, `RFC`).

## 4. Execution & Validation Workflow
1. **Classify Intent:** Identify the primary goal and select **one** Container Skill from Section 1.
2. **Select Content Overlays:** Determine if the document contains step-by-step actions (load `zero-ambiguity-sop`) or binding rules/metrics (load `clear-spec-writer`).
3. **Load Sub-Skills:** Read the `SKILL.md` files for the selected container and content skills before drafting.
4. **Validate Draft:** If shell execution is available, run `python3 scripts/validate_docs.py <draft-file>` to verify zero passive voice, vague adjectives, or length violations.
