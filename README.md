# High-Reliability Docs (Agent Skills)

A modular suite of [Agent Skills](https://github.com) designed to enforce zero-ambiguity writing, structured decision-making, verifiable system specifications, and safety-first operational runbooks across AI coding and writing agents (Claude Code, Cursor, GitHub Copilot, Gemini CLI, and Windsurf).

## Included Skills

| Skill | Primary Use Case | Core Mechanism |
| :--- | :--- | :--- |
| **`high-reliability-docs`** | Meta-Orchestrator | Automatically selects an outer document layout and layers strict inner writing rules. |
| **`executive-decision-memo`** | Leadership Memos & Records | Bottom Line Up Front (BLUF), active voice, strict hierarchy, and crisp sign-off blocks. |
| **`goal-action-plan`** | Incident Response & Project Plans | Fixed 5-section execution framework with a single-sentence objective and *Task + Purpose* assignments. |
| **`zero-ambiguity-sop`** | Runbooks & Technical Guides | Controlled vocabulary, 20-word step limits, imperative verbs, and front-loaded hazard callouts. |
| **`clear-spec-writer`** | PRDs, SLAs & System Specs | Binding modal verbs (`SHALL`, `SHOULD`, `MAY`), measurable thresholds, and unique requirement IDs. |

## Installation

```bash
# Install into the current workspace (.agents/skills/)
./install.sh local

# Install globally across all projects (~/.agents/skills/)
./install.sh global

# Install specifically for Claude Code (.claude/skills/)
./install.sh claude
```

## Automated Document Linter

```bash
python3 skills/high-reliability-docs/scripts/validate_docs.py examples/03-rebalancing-execution-sop.md
```
