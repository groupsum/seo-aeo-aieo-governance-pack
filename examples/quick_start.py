"""Inspect the installed pack identity."""

from seo_aeo_aieo_governance_pack import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:seo-aeo-aieo-governance"
print(metadata["origin"]["id"])
