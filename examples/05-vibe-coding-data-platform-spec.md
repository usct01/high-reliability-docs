# SYSTEM REQUIREMENTS SPECIFICATION: VIBE-CODED INVESTMENT DATA PLATFORM
**Document ID:** `SPEC-DAT-005` | **Status:** Draft | **Date:** 2026-11-11

## 1. Scope & Conformance
Interpret the key words **SHALL**, **MUST**, **SHOULD**, and **MAY** in this document as defined in RFC-2119. This specification constrains AI-assisted code generation ("vibe coding") for the Investment Management Data Platform so generated pipelines preserve financial auditability and point-in-time accuracy.

## 2. Functional & Data Integrity Requirements

| ID | Requirement Statement | Verification Method | Priority |
| :--- | :--- | :--- | :--- |
| `REQ-DAT-001` | The Data Platform **SHALL** store all market prices, fundamentals, and holdings using bi-temporal schemas with separate `as_of_date` and `system_recorded_timestamp` columns. | Code Review | Mandatory |
| `REQ-DAT-002` | The Ingestion Engine **SHALL** reject any custodian position file whose aggregate Net Asset Value (NAV) deviates more than 0.01 percent from internal accounting ledgers. | Automated Test | Mandatory |
| `REQ-DAT-003` | The Data Platform **SHALL** enforce idempotent pipeline execution so re-running any ingestion job for a historical date produces zero duplicate records. | Automated Test | Mandatory |
| `REQ-DAT-004` | The Security Master Service **SHALL** map every tradable instrument to a unique internal identifier alongside ISIN, CUSIP, and FIGI codes before downstream publication. | Automated Test | Mandatory |
| `REQ-DAT-005` | The Data Platform **SHOULD** expose point-in-time SQL views that prevent look-ahead bias during quantitative factor backtesting. | Demonstration | Recommended |

## 3. AI-Assisted ("Vibe Coding") Guardrails & Governance

| ID | Requirement Statement | Verification Method | Priority |
| :--- | :--- | :--- | :--- |
| `REQ-DAT-101` | Developers using AI coding agents **SHALL** generate accompanying unit tests achieving at least 90 percent branch coverage for every data transformation module. | Automated Test | Mandatory |
| `REQ-DAT-102` | The Data Platform **SHALL** prohibit AI-generated code from writing directly to production schemas without passing automated schema-drift and null-value gates in CI. | Code Review | Mandatory |
| `REQ-DAT-103` | All data pipelines **SHALL** store monetary amounts using fixed-point `DECIMAL(18,6)` data types rather than floating-point types. | Code Review | Mandatory |
| `REQ-DAT-104` | The Data Catalog **MAY** use Large Language Models (LLMs) to draft column descriptions, provided a data steward approves every description before publication. | Inspection | Optional |

## 4. Verification Methods Legend
- **Automated Test:** Verified under controlled conditions using automated unit, integration, and replay test suites.
- **Demonstration:** Qualitative exhibition of functional operation in a staging environment.
- **Code Review:** Direct inspection of AI-generated SQL, Python transforms, and CI/CD pipeline definitions.
- **Inspection:** Manual review of governance workflows and stewardship sign-offs.
