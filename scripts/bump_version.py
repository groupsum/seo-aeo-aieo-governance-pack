from __future__ import annotations

import argparse
import re
from pathlib import Path


VERSION_RE = re.compile(
    r"^(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)(?:\.dev(?P<dev>\d+))?$"
)


def parse_version(version: str) -> tuple[int, int, int, int | None]:
    match = VERSION_RE.fullmatch(version.strip())
    if not match:
        raise ValueError(f"Unsupported version format: {version!r}")
    major, minor, patch = (int(match.group(part)) for part in ("major", "minor", "patch"))
    dev = match.group("dev")
    return major, minor, patch, int(dev) if dev is not None else None


def bump_version(version: str, bump: str) -> str:
    major, minor, patch, dev = parse_version(version)
    if bump == "minor":
        return f"{major}.{minor + 1}.{patch}.dev1"
    if bump == "patch":
        if dev is None:
            return f"{major}.{minor}.{patch + 1}.dev1"
        return f"{major}.{minor}.{patch}.dev{dev + 1}"
    if bump == "finalize":
        if dev is None:
            raise ValueError(f"Cannot finalize non-dev release: {version!r}")
        if dev > 1:
            return f"{major}.{minor}.{patch + 1}"
        return f"{major}.{minor}.{patch}"
    raise ValueError(f"Unsupported bump type: {bump}")


def read_project_version(pyproject_path: Path) -> str:
    text = pyproject_path.read_text(encoding="utf-8")
    in_project = False
    for line in text.splitlines():
        section_match = re.match(r"\s*\[([^\]]+)\]\s*$", line)
        if section_match:
            in_project = section_match.group(1).strip() == "project"
            continue
        if in_project:
            version_match = re.match(r'\s*version\s*=\s*"([^"]+)"\s*$', line)
            if version_match:
                return version_match.group(1)
    raise ValueError(f"Could not find [project].version in {pyproject_path}")


def replace_pyproject_version(pyproject_path: Path, version: str) -> None:
    text = pyproject_path.read_text(encoding="utf-8")
    in_project = False
    replaced = False
    lines: list[str] = []
    for line in text.splitlines(keepends=True):
        section_match = re.match(r"\s*\[([^\]]+)\]\s*$", line.rstrip("\n"))
        if section_match:
            in_project = section_match.group(1).strip() == "project"
            lines.append(line)
            continue
        if in_project and re.match(r'\s*version\s*=\s*"[^"]+"\s*$', line.rstrip("\n")):
            newline = "\n" if line.endswith("\n") else ""
            lines.append(f'version = "{version}"{newline}')
            replaced = True
        else:
            lines.append(line)
    if not replaced:
        raise ValueError(f"Could not replace [project].version in {pyproject_path}")
    pyproject_path.write_text("".join(lines), encoding="utf-8")


def replace_dunder_version(version_file: Path, version: str) -> None:
    text = version_file.read_text(encoding="utf-8")
    updated, count = re.subn(
        r'^__version__\s*=\s*"[^"]+"$',
        f'__version__ = "{version}"',
        text,
        count=1,
        flags=re.MULTILINE,
    )
    if count != 1:
        raise ValueError(f"Could not replace __version__ in {version_file}")
    version_file.write_text(updated, encoding="utf-8")


def update_changelog(changelog_path: Path, version: str) -> None:
    text = changelog_path.read_text(encoding="utf-8") if changelog_path.exists() else "# Changelog\n"
    normalized = text.rstrip() + "\n"
    entry_header = f"## {version}"
    if entry_header in normalized:
        return
    if "## " in normalized:
        updated = normalized.replace("## ", f"{entry_header}\n\n- Pending release notes.\n\n## ", 1)
    else:
        updated = normalized + f"\n{entry_header}\n\n- Pending release notes.\n"
    changelog_path.write_text(updated, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Bump package version metadata.")
    parser.add_argument("--bump", choices=("patch", "minor", "finalize"), required=True)
    parser.add_argument("--pyproject", default="pyproject.toml")
    parser.add_argument(
        "--version-file",
        default="src/seo_aeo_aieo_governance_pack/__init__.py",
    )
    parser.add_argument("--changelog", default="CHANGELOG.md")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    pyproject_path = Path(args.pyproject)
    version_file = Path(args.version_file)
    changelog_path = Path(args.changelog)

    current = read_project_version(pyproject_path)
    bumped = bump_version(current, args.bump)
    if args.write:
        replace_pyproject_version(pyproject_path, bumped)
        replace_dunder_version(version_file, bumped)
        update_changelog(changelog_path, bumped)
    print(bumped)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
