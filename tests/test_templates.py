from __future__ import annotations

import json
import unittest

from seo_aeo_aieo_governance_pack import (
    __pypi_package_name__,
    __ssot_package_name__,
    __version__,
    get_packaged_document_entry,
    list_packaged_document_ids,
    load_document_manifest,
    load_pack_manifest,
    load_pack_metadata,
    load_pack_schema_version,
    read_packaged_document_text,
)


class TemplateManifestTests(unittest.TestCase):

    def test_pack_metadata_contract_is_exposed(self) -> None:
        metadata = load_pack_metadata()
        self.assertEqual("seo-aeo-aieo-governance-pack", __ssot_package_name__)
        self.assertEqual("seo-aeo-aieo-governance-pack", __pypi_package_name__)
        self.assertEqual("0.1.4", __version__)
        self.assertEqual("1.0.0", metadata["schema_version"])
        self.assertEqual("seo-aeo-aieo-governance-pack", metadata["ssot_package_name"])
        self.assertEqual("seo-aeo-aieo-governance-pack", metadata["pypi_package_name"])
        self.assertEqual("seo-aeo-aieo-governance-pack", metadata["origin"]["package_name"])
        self.assertEqual("seo_aeo_aieo_governance_pack", metadata["origin"]["import_name"])
        self.assertEqual("extension-pack", metadata["trust"]["origin"])
        self.assertEqual("extension-pack:seo-aeo-aieo-governance-pack", metadata["trust"]["reservation_owner"])
        self.assertEqual("1.0.0", load_pack_schema_version())
        self.assertEqual("0.1.4", metadata["version"])

    def test_pack_manifest_contract_is_exposed(self) -> None:
        manifest = load_pack_manifest()
        self.assertEqual("seo-aeo-aieo-governance-pack", manifest["metadata"]["origin"]["package_name"])
        self.assertIn("adr", manifest["documents"])
        self.assertIn("spec", manifest["documents"])
        self.assertEqual("adr:0800", get_packaged_document_entry("adr:0800")["id"])
        self.assertEqual(33, len(list_packaged_document_ids()))
    def test_adr_manifest_has_expected_rows(self) -> None:
        manifest = load_document_manifest("adr")
        self.assertEqual(12, len(manifest))
        self.assertEqual(
            [
                "adr:0800",
                "adr:0801",
                "adr:0802",
                "adr:0803",
                "adr:0804",
                "adr:0805",
                "adr:0806",
                "adr:0807",
                "adr:0808",
                "adr:0809",
                "adr:0810",
                "adr:0811",
            ],
            [row["id"] for row in manifest],
        )

    def test_spec_manifest_has_expected_rows(self) -> None:
        manifest = load_document_manifest("spec")
        self.assertEqual(21, len(manifest))
        self.assertEqual(
            [
                "spc:0800",
                "spc:0801",
                "spc:0802",
                "spc:0803",
                "spc:0804",
                "spc:0805",
                "spc:0806",
                "spc:0807",
                "spc:0808",
                "spc:0809",
                "spc:0810",
                "spc:0811",
                "spc:0812",
                "spc:0813",
                "spc:0814",
                "spc:0815",
                "spc:0816",
                "spc:0817",
                "spc:0818",
                "spc:0819",
                "spc:0820",
            ],
            [row["id"] for row in manifest],
        )

    def test_packaged_document_can_be_loaded(self) -> None:
        text = read_packaged_document_text("spec", "SPEC-0801-aeo-answer-surface-contract.yaml")
        payload = json.loads(text)
        self.assertEqual("spc:0801", payload["id"])
        self.assertEqual("normative", payload["spec_kind"])

    def test_packaged_adr_can_be_loaded(self) -> None:
        text = read_packaged_document_text("adr", "ADR-0805-google-ai-features-do-not-justify-ai-specific-schema-or-ai-only-files.yaml")
        payload = json.loads(text)
        self.assertEqual("adr:0805", payload["id"])
        self.assertEqual(
            "Google AI features do not justify AI-specific schema or AI-only files",
            payload["title"],
        )

    def test_packaged_spec_can_be_loaded(self) -> None:
        text = read_packaged_document_text("spec", "SPEC-0803-robots-exclusion-protocol-contract.yaml")
        payload = json.loads(text)
        self.assertEqual("spc:0803", payload["id"])
        self.assertEqual("normative", payload["spec_kind"])

    def test_second_half_packaged_spec_can_be_loaded(self) -> None:
        text = read_packaged_document_text("spec", "SPEC-0815-openai-crawler-controls-contract.yaml")
        payload = json.loads(text)
        self.assertEqual("spc:0815", payload["id"])
        self.assertEqual("normative", payload["spec_kind"])


if __name__ == "__main__":
    unittest.main()

