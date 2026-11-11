---
name: goal-action-plan
description: Structure operational plans, incident response playbooks, outage management, and complex project execution using a standardized 5-section Goal Action Plan framework. Use whenever the user asks for an action plan, incident response structure, launch plan, or multi-team execution playbook.
---

# 5-Section Goal Action Plan Skill

Organize complex operations, incident responses, and multi-team projects into a fixed 5-section execution framework so every stakeholder knows the objective, their exact task, and the escalation path.

## 1. Core Principles
- **Leadership Intent & End State:** Clearly define what success looks like when the operation is complete.
- **Single-Sentence Objective:** Section 2 must contain a single sentence answering **Who, What, When, Where, and Why (In order to...)**.
- **Task and Purpose:** Every assigned team or owner must receive both a **Task** (what to do) and a **Purpose** (why they are doing it) so they can adapt if conditions change.
- **Time Format:** Use 24-hour time with an explicit time zone (e.g., `08:00 UTC` or `13:30 IST`).

## 2. Mandatory 5-Section Structure

Format every plan using these exact five top-level sections:

```text
# GOAL ACTION PLAN: [INITIATIVE / INCIDENT NAME]
**Timestamp:** [DD Month YYYY, HH:MM TZ]
**Primary Time Zone:** [e.g., UTC / IST / EST]

## 1. CONTEXT & IMPACT
- **Current Situation / Root Cause:** [What is happening right now? Include root cause, customer/system impact, and constraints.]
- **Available Teams & Dependencies:** [Participating teams, external vendors, or upstream services.]
- **Assumptions:** [Key assumptions required for this plan to succeed.]

## 2. OBJECTIVE
[WHO] will [WHAT - core action] no later than [WHEN] at [WHERE] in order to [WHY - overarching goal].

## 3. EXECUTION
- **Leadership Intent / Desired End State:** [2–3 sentences describing the final verified state once all tasks are complete.]
- **Phased Rollout:** [High-level phased summary: Phase I (Containment), Phase II (Resolution), Phase III (Verification).]
- **Team Assignments:**
  - **[Team / Lead A]:**
    - *Task:* [Specific deliverable or action.]
    - *Purpose:* [Why this task matters to the main objective.]
  - **[Team / Lead B]:**
    - *Task:* [Specific deliverable or action.]
    - *Purpose:* [Why this task matters to the main objective.]
- **Coordinating Instructions:** [Deadlines, escalation triggers, release gates, and operational boundaries.]

## 4. RESOURCES & HANDOFFS
- **Tooling & Infrastructure:** [Tools, compute capacity, budget, credentials, or environments needed.]
- **Staffing & Shift Rotation:** [On-call handoffs, backup leads, and coverage windows.]

## 5. ESCALATION & COMMS
- **Decision Chain:** [Primary Incident/Project Lead, followed by backup decision makers.]
- **Communication Channels:**
  - *Primary Channel:* [e.g., #incident-war-room]
  - *Backup Channel:* [e.g., Video Bridge Link]
  - *Status Cadence:* [e.g., Written status update every 30 minutes on the hour and half-hour.]
```

## 3. Execution Rules
- Never leave Section 2 (Objective) as a bulleted list; enforce a single, crisp sentence.
- Ensure every assignment in Section 3 pairs an explicit **Task** with an explicit **Purpose**.
- If information is missing from the user's prompt, insert `[TBD - Assign Owner]` rather than inventing operational details.
