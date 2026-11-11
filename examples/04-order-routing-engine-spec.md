# SYSTEM REQUIREMENTS SPECIFICATION: SMART ORDER ROUTER (SOR)
**Document ID:** `SPEC-TRD-009` | **Status:** Approved | **Date:** 2026-11-11

## 1. Scope & Conformance
Interpret the key words **SHALL**, **MUST**, **SHOULD**, and **MAY** in this document as defined in RFC-2119.

## 2. Functional Requirements

| ID | Requirement Statement | Verification Method | Priority |
| :--- | :--- | :--- | :--- |
| `REQ-SOR-001` | The Smart Order Router **SHALL** evaluate top-of-book liquidity across all connected exchanges within 200 microseconds of order receipt. | Automated Test | Mandatory |
| `REQ-SOR-002` | The Smart Order Router **SHALL** reject any child order whose limit price deviates more than 2.0 percent from the National Best Bid and Offer (NBBO). | Automated Test | Mandatory |
| `REQ-SOR-003` | The Smart Order Router **SHALL** record nanosecond-precision timestamps for every routing decision to the immutable audit ledger. | Telemetry Audit | Mandatory |
| `REQ-SOR-004` | The Smart Order Router **SHOULD** prioritize lit venues offering maker fee rebates when displayed liquidity and latency metrics are equal. | Code Review | Recommended |

## 3. Non-Functional & Resilience Requirements

| ID | Requirement Statement | Verification Method | Priority |
| :--- | :--- | :--- | :--- |
| `REQ-SOR-101` | The Smart Order Router **SHALL** sustain a throughput of 50,000 orders per second with 99.9th-percentile internal latency under 500 microseconds. | Automated Test | Mandatory |
| `REQ-SOR-102` | The Smart Order Router **SHALL** fail over to the secondary matching node within 50 milliseconds of a primary heartbeat timeout. | Demonstration | Mandatory |
| `REQ-SOR-103` | The Smart Order Router **MAY** support dark-pool midpoint pegging for parent orders exceeding 10,000 shares. | Demonstration | Optional |

## 4. Verification Methods Legend
- **Automated Test:** Verified under controlled conditions using automated load generators and replay harnesses.
- **Demonstration:** Qualitative exhibition of functional operation in a simulated exchange environment.
- **Telemetry Audit:** Verified via production execution logs, latency histograms, and timestamp audit trails.
- **Code Review:** Direct inspection of routing logic and configuration schemas against design specifications.
