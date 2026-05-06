from __future__ import annotations

import json
from importlib import resources


def _package_name(kind: str) -> str:
    normalized = kind.lower()
    if normalized in {"adr", "adrs"}:
        return "seo_aeo_aieo_governance_pack.templates.adr"
    if normalized in {"spec", "specs"}:
        return "seo_aeo_aieo_governance_pack.templates.specs"
    raise ValueError(f"Unsupported document kind: {kind}")


def load_document_manifest(kind: str) -> list[dict]:
    package = _package_name(kind)
    text = resources.files(package).joinpath("manifest.json").read_text(encoding="utf-8")
    return json.loads(text)


def read_packaged_document_bytes(kind: str, filename: str) -> bytes:
    package = _package_name(kind)
    return resources.files(package).joinpath(filename).read_bytes()


def read_packaged_document_text(kind: str, filename: str) -> str:
    return read_packaged_document_bytes(kind, filename).decode("utf-8")
