---
name: zero-ambiguity-sop
description: Write and edit technical procedures, Standard Operating Procedures (SOPs), runbooks, and user guides using Controlled Technical English standards. Use whenever the user asks to simplify technical instructions, write clear SOPs, eliminate ambiguity, or build safety-critical runbooks.
---

# Zero-Ambiguity SOP & Runbook Skill

Apply Controlled Technical English principles to produce clear, unambiguous, and globally readable operational procedures.

## 1. Core Writing Rules
- **One Word, One Meaning:** Never use the same word as both a noun and a verb, or with multiple meanings.
  - *Incorrect:* "Log the error in the error log."
  - *Correct:* "Record the error in the system log."
- **Active Voice Only:** Always state who or what performs the action. Passive voice is strictly forbidden.
  - *Incorrect:* "The service must be stopped before the database is migrated."
  - *Correct:* "Stop the service before you migrate the database."
- **Imperative Mood for Procedures:** Start every instructional step with a direct action verb (e.g., *Open*, *Connect*, *Measure*, *Verify*).
- **Sentence Length Caps:**
  - **Procedural steps:** Maximum **20 words** per sentence.
  - **Descriptive text:** Maximum **25 words** per sentence.
- **One Action Per Step:** Write one instruction per numbered step. Only combine two actions if they happen simultaneously (e.g., *"Press and hold the RESET button"*).
- **Avoid Noun Clusters:** Never stack more than three nouns together. Break them up with prepositions.
  - *Incorrect:* "Primary database connection pool timeout configuration"
  - *Correct:* "The timeout configuration for the primary database connection pool"

## 2. Hazard & Risk Callout Hierarchy
Always place callouts **immediately before** the step to which they apply—never after.
- **CRITICAL:** Indicates a procedure or condition that, if not strictly observed, can result in **personal injury, security breach, or irreversible production outage**.
- **CAUTION:** Indicates a procedure or condition that, if not strictly observed, can result in **equipment damage, data corruption, or service degradation**.
- **NOTE:** Highlights an essential operating condition, tip, or clarification that requires emphasis.

## 3. Document Structure Template

```text
# [PROCEDURE TITLE IN ALL CAPS]

## 1. Prerequisites & Access
- [Required tools, permissions, credentials, or system states]

## 2. Hazard & Risk Precautions
CRITICAL: [Critical hazard affecting safety or irreversible data loss, if applicable.]
CAUTION: [Hazard affecting equipment or service stability, if applicable.]

## 3. Procedure
1. [Action verb] [single clear task <= 20 words].
2. [Action verb] [single clear task <= 20 words].
   
   CAUTION: [Step-specific hazard placed BEFORE the risky action.]
   
3. [Action verb] [risky action <= 20 words].
4. Verify that [expected system state or measurement].
```

## 4. Review Checklist
Before finalizing any output, verify:
1. No passive voice (`was`, `were`, `been`, `is [verb]ed`) exists.
2. Every procedural sentence is 20 words or fewer.
3. No hazard callouts appear below the step they protect.
4. No contractions (`don't`, `can't`, `it's`) are used.
