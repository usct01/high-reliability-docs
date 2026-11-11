# Financial Investment Domain Examples

These examples demonstrate how each skill—and the `high-reliability-docs` orchestrator—produces clear, auditable documentation for investment management, quantitative trading, data engineering, and enterprise AI operations.

| Example File | Skill(s) Demonstrated | Financial Use Case |
| :--- | :--- | :--- |
| `01-combined-risk-directive-memo.md` | `high-reliability-docs` (`executive-decision-memo` + `clear-spec-writer`) | Investment Committee mandate enforcing concentration limits and automated drawdown circuit breakers. |
| `02-flash-crash-action-plan.md` | `high-reliability-docs` (`goal-action-plan` + `zero-ambiguity-sop`) | Multi-desk response plan and emergency hedging steps during a severe liquidity drop. |
| `03-rebalancing-execution-sop.md` | `zero-ambiguity-sop` | Step-by-step institutional portfolio rebalancing runbook with pre-trade risk checks. |
| `04-order-routing-engine-spec.md` | `clear-spec-writer` | Verifiable engineering requirements (`SHALL` / `SHOULD`) for a Smart Order Router (SOR). |
| `05-vibe-coding-data-platform-spec.md` | `clear-spec-writer` | Guardrails and bi-temporal data integrity requirements for AI-assisted ("vibe-coded") investment data pipelines. |
| `06-investment-ai-platform-spec.md` | `clear-spec-writer` | Citation, ethical-wall RBAC, MNPI redaction, and 7-year audit requirements for an Investment AI Platform. |

## Validate Examples with the Linter

Run the document linter against any example file to verify zero violations:

```bash
python3 skills/high-reliability-docs/scripts/validate_docs.py examples/05-vibe-coding-data-platform-spec.md
```
