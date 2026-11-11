import re
import subprocess
import sys
import tempfile
from pathlib import Path

SKILLS_DIR = Path("skills")
VALIDATOR_SCRIPT = SKILLS_DIR / "high-reliability-docs" / "scripts" / "validate_docs.py"
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def validate_skill_schemas() -> list[str]:
    errors = []
    if not SKILLS_DIR.is_dir():
        return ["Missing 'skills/' directory at repository root."]

    skill_folders = [p for p in SKILLS_DIR.iterdir() if p.is_dir()]
    if not skill_folders:
        return ["No skill folders found inside 'skills/'."]

    for folder in sorted(skill_folders):
        skill_md = folder / "SKILL.md"
        if not skill_md.exists():
            errors.append(f"[{folder.name}] Missing required SKILL.md file.")
            continue

        content = skill_md.read_text(encoding="utf-8")
        match = FRONTMATTER_RE.match(content)
        if not match:
            errors.append(f"[{folder.name}] Missing or malformed YAML frontmatter block.")
            continue

        frontmatter = match.group(1)
        name_match = re.search(r"^name:\s*(.+)$", frontmatter, re.MULTILINE)
        desc_match = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)

        if not name_match:
            errors.append(f"[{folder.name}] Frontmatter missing 'name' field.")
        else:
            declared_name = name_match.group(1).strip().strip("'\"")
            if declared_name != folder.name:
                errors.append(
                    f"[{folder.name}] Frontmatter name '{declared_name}' does not match directory name '{folder.name}'."
                )

        if not desc_match or len(desc_match.group(1).strip()) < 20:
            errors.append(f"[{folder.name}] Frontmatter missing a valid 'description' (min 20 chars).")

        for ref in re.findall(r"`((?:references|scripts)/[^`]+)`", content):
            ref_path = folder / ref
            if not ref_path.exists():
                errors.append(f"[{folder.name}] Broken internal reference: '{ref}' not found.")

    return errors


def test_document_validator() -> list[str]:
    errors = []
    if not VALIDATOR_SCRIPT.exists():
        return [f"Missing document linter script at {VALIDATOR_SCRIPT}"]

    good_doc = (
        "# SAMPLE SOP\n\n"
        "CRITICAL: Stop all active write traffic before you promote the standby database.\n\n"
        "1. Verify that primary health checks fail for three consecutive minutes.\n"
        "2. Execute the promotion command in the primary terminal.\n"
    )

    bad_doc = (
        "# BAD SAMPLE SOP\n\n"
        "1. Ensure the system is fast and seamless while all database nodes are restarted by the operator immediately.\n"
        "CAUTION: This step causes downtime.\n"
    )

    with tempfile.TemporaryDirectory() as tmpdir:
        good_path = Path(tmpdir) / "good.md"
        bad_path = Path(tmpdir) / "bad.md"
        good_path.write_text(good_doc, encoding="utf-8")
        bad_path.write_text(bad_doc, encoding="utf-8")

        res_good = subprocess.run(
            [sys.executable, str(VALIDATOR_SCRIPT), str(good_path)],
            capture_output=True,
            text=True,
        )
        if res_good.returncode != 0:
            errors.append(f"Linter failed on valid document:\n{res_good.stdout}")

        res_bad = subprocess.run(
            [sys.executable, str(VALIDATOR_SCRIPT), str(bad_path)],
            capture_output=True,
            text=True,
        )
        if res_bad.returncode == 0:
            errors.append("Linter unexpectedly passed an invalid document containing violations.")

    return errors


def validate_examples() -> list[str]:
    errors = []
    examples_dir = Path("examples")
    if not examples_dir.is_dir():
        return []

    for md_file in sorted(examples_dir.glob("*.md")):
        if md_file.name.lower() == "readme.md":
            continue
        res = subprocess.run(
            [sys.executable, str(VALIDATOR_SCRIPT), str(md_file)],
            capture_output=True,
            text=True,
        )
        if res.returncode != 0:
            errors.append(f"Example failed linter ({md_file.name}):\n{res.stdout}")
    return errors


def main() -> int:
    print("Running repository skill schema checks...")
    schema_errors = validate_skill_schemas()

    print("Running validate_docs.py self-tests...")
    linter_errors = test_document_validator()

    print("Validating financial examples...")
    example_errors = validate_examples()

    all_errors = schema_errors + linter_errors + example_errors
    if all_errors:
        print("\nCI VALIDATION FAILED:")
        for err in all_errors:
            print(f" - {err}")
        return 1

    print("\nALL CHECKS PASSED: Schemas, references, examples, and linter tests succeeded.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
