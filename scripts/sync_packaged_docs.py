from __future__ import annotations

import hashlib
import json
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover
    import tomli as tomllib


ROOT = Path(__file__).resolve().parents[1]
ADR_TEMPLATES = ROOT / "src" / "seo_aeo_aieo_governance_pack" / "templates" / "adr"
SPEC_TEMPLATES = ROOT / "src" / "seo_aeo_aieo_governance_pack" / "templates" / "specs"
RESERVATION_OWNER = "extension-pack:seo-aeo-aieo-governance-pack"
MINIMUM_SCHEMA_VERSION = "0.4.0"


def _project_version() -> str:
    data = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    return data["project"]["version"]


def _sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _load_documents(folder: Path) -> list[tuple[Path, dict]]:
    rows: list[tuple[Path, dict]] = []
    for path in sorted(folder.glob("*.yaml")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        rows.append((path, payload))
    return rows


def _sync_kind(kind: str, templates: Path, version: str) -> list[dict]:
    manifest_rows: list[dict] = []
    templates.mkdir(parents=True, exist_ok=True)
    manifest_path = templates / "manifest.json"
    if manifest_path.exists():
        manifest_path.unlink()
    for path, payload in _load_documents(templates):
        raw_bytes = path.read_bytes()
        sha256 = _sha256_bytes(raw_bytes)

        entry = {
            "id": payload["id"],
            "number": payload["number"],
            "slug": payload["slug"],
            "title": payload["title"],
            "filename": path.name,
            "target_path": f".ssot/{'adr' if kind == 'adr' else 'specs'}/{path.name}",
            "sha256": sha256,
            "origin": "extension-pack",
            "reservation_owner": RESERVATION_OWNER,
            "immutable": True,
            "minimum_schema_version": MINIMUM_SCHEMA_VERSION,
            "introduced_in": version,
            "status": payload["status"],
            "supersedes": payload.get("supersedes", []),
            "superseded_by": payload.get("superseded_by", []),
            "status_notes": payload.get("status_notes", []),
        }
        if kind == "spec":
            entry["kind"] = payload["spec_kind"]
        manifest_rows.append(entry)

    manifest_path.write_text(json.dumps(manifest_rows, indent=2) + "\n", encoding="utf-8")
    return manifest_rows


def main() -> None:
    version = _project_version()
    _sync_kind("adr", ADR_TEMPLATES, version)
    _sync_kind("spec", SPEC_TEMPLATES, version)


if __name__ == "__main__":
    main()
