#!/usr/bin/env python3
"""Validate SKILL.md frontmatter and hospital data files.

Usage: python scripts/validate.py
Requires: pyyaml, jsonschema
"""
import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
STAGES = {"learn", "assess", "match", "travel", "recover", "cross-cutting"}
REQUIRED_SECTIONS = ["用途", "何时使用", "输入", "步骤", "输出格式", "边界", "医学声明"]
errors = []


def err(path, msg):
    errors.append(f"{path.relative_to(ROOT)}: {msg}")


def check_skill(skill_dir: Path):
    md = skill_dir / "SKILL.md"
    if not md.exists():
        err(skill_dir, "missing SKILL.md")
        return
    text = md.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        err(md, "missing YAML frontmatter")
        return
    fm = yaml.safe_load(m.group(1)) or {}
    if fm.get("name") != skill_dir.name:
        err(md, f"name '{fm.get('name')}' must equal directory name '{skill_dir.name}'")
    desc = fm.get("description") or ""
    if not desc or len(desc) > 300:
        err(md, "description missing or longer than 300 chars")
    meta = fm.get("metadata") or {}
    if meta.get("stage") not in STAGES:
        err(md, f"metadata.stage must be one of {sorted(STAGES)}")
    for key in ("version", "license", "author"):
        if not meta.get(key):
            err(md, f"metadata.{key} missing")
    for section in REQUIRED_SECTIONS:
        if not re.search(rf"^##\s+.*{section}", text, re.M):
            err(md, f"missing section '{section}'")
    examples = skill_dir / "examples"
    if not examples.is_dir() or len([p for p in examples.iterdir() if p.is_file()]) < 2:
        err(skill_dir, "needs at least 2 files in examples/")


def check_data():
    schema = json.loads((ROOT / "data/schema/hospital.schema.json").read_text())
    validator = Draft202012Validator(schema)
    seen = {}
    for f in sorted((ROOT / "data/hospitals").glob("*.yaml")):
        records = yaml.safe_load(f.read_text(encoding="utf-8")) or []
        if not isinstance(records, list):
            err(f, "top level must be a list")
            continue
        for i, rec in enumerate(records):
            for e in validator.iter_errors(rec):
                err(f, f"[{i}] {rec.get('id', '?')}: {e.message}")
            rid = rec.get("id")
            if rid in seen and seen[rid] != f:
                pass  # same hospital may appear under several directions
            seen.setdefault(rid, f)


def main():
    skills = ROOT / "skills"
    for d in sorted(p for p in skills.iterdir() if p.is_dir() and not p.name.startswith("_")):
        check_skill(d)
    check_data()
    if errors:
        print("\n".join(errors))
        print(f"\n{len(errors)} problem(s) found.")
        sys.exit(1)
    print("All checks passed.")


if __name__ == "__main__":
    main()
