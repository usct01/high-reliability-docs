---
name: clear-spec-writer
description: Draft and audit engineering specifications, Product Requirement Documents (PRDs), SLAs, and compliance policies using strict systems engineering and RFC-2119 requirement standards. Use whenever the user asks to write system requirements, PRDs, technical specs, or audit ambiguous specifications.
---

# Clear Spec Writer (RFC-2119 & Systems Engineering Standard)

Write verifiable, atomic, and unambiguous system requirements modeled on rigorous systems engineering practices and IETF RFC-2119 modal verbs.

## 1. Binding Modal Verbs (Strict Definitions)
- **SHALL / MUST:** Indicates a mandatory, legally or contractually binding requirement that must be verified through automated testing, inspection, or telemetry analysis.
- **SHOULD:** Indicates a strongly recommended goal or best practice. Deviation is permitted only with documented architectural justification.
- **MAY:** Indicates a truly optional feature or behavior.
- **WILL:** Expresses a statement of fact, future event, or declaration of purpose—**never** use `WILL` to state a mandatory requirement.

## 2. Rules for Well-Formed Requirements
Every requirement statement must satisfy five criteria:
1. **Atomic (One Requirement Per Sentence):** Never combine two requirements with `and` or `or`. Split them into separate numbered IDs.
2. **Verifiable:** State measurable thresholds (latency, uptime, throughput, tolerance). Ban subjective adjectives like *fast*, *user-friendly*, *robust*, *scalable*, or *seamless*.
   - *Bad:* "The API shall be fast and reliable."
   - *Good:* "The API **SHALL** respond to 99% of `GET` requests within 150 milliseconds (`REQ-001`)."
3. **Implementation-Free:** State **what** the system must achieve, not **how** to code or build it (unless specifying an external interface constraint).
4. **Unique Identifier:** Assign every requirement a traceable ID (e.g., `REQ-SYS-001`).
5. **Active Subject:** Name the specific system, subsystem, or role responsible (`The Authentication Service SHALL...`, not `Users should be authenticated...`).

## 3. Specification Output Template

```markdown
# SYSTEM REQUIREMENTS SPECIFICATION: [SYSTEM / FEATURE NAME]
**Document ID:** [SPEC-001] | **Status:** Draft | **Date:** [YYYY-MM-DD]

## 1. Scope & Conformance
Interpret the key words **SHALL**, **MUST**, **SHOULD**, and **MAY** in this document as defined in RFC-2119.

## 2. Functional Requirements

| ID | Requirement Statement | Verification Method | Priority |
| :--- | :--- | :--- | :--- |
| `REQ-001` | The [System] **SHALL** [measurable action] within [X] seconds. | Automated Test | Mandatory |
| `REQ-002` | The [System] **SHALL** record all failed access attempts to [Destination]. | Code Review | Mandatory |

## 3. Non-Functional & Interface Requirements

| ID | Requirement Statement | Verification Method | Priority |
| :--- | :--- | :--- | :--- |
| `REQ-101` | The [System] **SHALL** maintain 99.95% availability over any rolling 30-day window. | Telemetry Audit | Mandatory |
| `REQ-102` | The [System] **SHOULD** support horizontal scaling without service interruption. | Demonstration | Recommended |

## 4. Verification Methods Legend
- **Automated Test:** Verified under controlled conditions using automated test suites or load instrumentation.
- **Demonstration:** Qualitative exhibition of functional operation in a simulated exchange environment.
- **Telemetry Audit:** Verified via production metrics, mathematical calculations, or log analysis.
- **Code Review:** Direct inspection of source code, schemas, or configuration files against design rules.
```

## 4. Audit Mode Workflow
When asked to review an existing PRD or specification:
1. Flag every instance of vague words (*fast*, *easy*, *flexible*, *etc.*, *TBD*).
2. Highlight compound sentences containing multiple `shall` statements and split them into atomic IDs.
3. Rewrite passive requirements into active `[Subject] SHALL [Measurable Action]` statements.
