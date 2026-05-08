from __future__ import annotations

import json
import unittest

from seo_aeo_aieo_governance_pack import load_document_manifest, read_packaged_document_text


class TemplateManifestTests(unittest.TestCase):
    def test_adr_manifest_has_expected_rows(self) -> None:
        manifest = load_document_manifest("adr")
        self.assertEqual(10, len(manifest))
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
            ],
            [row["id"] for row in manifest],
        )

    def test_spec_manifest_has_expected_rows(self) -> None:
        manifest = load_document_manifest("spec")
        self.assertEqual(17, len(manifest))
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
