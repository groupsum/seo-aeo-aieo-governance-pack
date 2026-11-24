"""Find a specification and its downstream path in the installed manifest."""

from seo_aeo_aieo_governance_pack import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:0800"
)
assert specification["target_path"] == ".ssot/specs/SPEC-0800-seo-governance-surface.yaml"
