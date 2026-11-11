import re
import sys
from pathlib import Path

VAGUE_WORDS = {
    "fast", "quick", "quickly", "robust", "seamless", "seamlessly",
    "user-friendly", "easy", "easily", "flexible", "scalable", "efficient",
    "optimal", "adequate", "appropriate", "etc", "tbd"
}

PASSIVE_PATTERN = re.compile(
    r"\b(is|are|was|were|be|been|being)\s+([a-z]+ed|done|made|built|sent|run|set|put)\b",
    re.IGNORECASE
)

STEP_PATTERN = re.compile(r"^\s*\d+\.\s+(.+)$")
WARNING_PATTERN = re.compile(r"^\s*(CRITICAL|DANGER|WARNING|CAUTION|NOTE):", re.IGNORECASE)


def audit_document(file_path: str) -> int:
    path = Path(file_path)
    if not path.exists():
        print(f"Error: File not found -> {file_path}")
        return 1

    lines = path.read_text(encoding="utf-8").splitlines()
    issues = []

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        step_match = STEP_PATTERN.match(stripped)
        if step_match:
            step_text = step_match.group(1)
            words = re.findall(r"\b\w+\b", step_text)
            if len(words) > 20:
                issues.append(
                    f"[Line {idx}] Procedural Length Violation ({len(words)} words > 20 max): '{stripped[:60]}...'"
                )

        passive_match = PASSIVE_PATTERN.search(stripped)
        if passive_match:
            issues.append(
                f"[Line {idx}] Passive Voice Detected ('{passive_match.group(0)}'): '{stripped[:60]}...'"
            )

        tokens = set(re.findall(r"\b[a-z-]+\b", stripped.lower()))
        found_vague = tokens.intersection(VAGUE_WORDS)
        if found_vague:
            issues.append(
                f"[Line {idx}] Vague Term(s) {sorted(found_vague)} - Replace with measurable metrics."
            )

        if WARNING_PATTERN.match(stripped) and idx > 1:
            prev_line = lines[idx - 2].strip()
            if STEP_PATTERN.match(prev_line):
                issues.append(
                    f"[Line {idx}] Hazard Placement Violation: '{stripped[:30]}' appears AFTER a step. Move it BEFORE."
                )

    print(f"=== High-Reliability Doc Audit: {path.name} ===")
    if not issues:
        print("PASS: 0 violations found.")
        return 0

    for issue in issues:
        print(f"FAIL: {issue}")
    print(f"\nTotal Violations: {len(issues)}")
    return 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_docs.py <path-to-draft.md>")
        sys.exit(1)
    sys.exit(audit_document(sys.argv[1]))
