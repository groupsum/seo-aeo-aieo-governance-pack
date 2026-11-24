# seo-aeo-aieo-governance-pack

<!-- readme-standards:begin branding -->
<p align="center"><a href="https://github.com/groupsum/readme-standards"><img src="https://raw.githubusercontent.com/groupsum/readme-standards/master/docs/assets/readme-standards.svg" alt="Groupsum README Standards" width="300"></a></p>
<p align="center"><strong>seo-aeo-aieo-governance-pack</strong></p>
<p align="center">Installable ADR and SPEC extension pack for SEO, AEO, and AiEO governance.</p>
<p align="center">
<a href="https://pypi.org/project/seo-aeo-aieo-governance-pack/"><img alt="pypi: seo-aeo-aieo-governance-pack" src="https://img.shields.io/pypi/v/seo-aeo-aieo-governance-pack?labelColor=1E293B&amp;color=1D4ED8"></a>
<a href="https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/pyproject.toml"><img alt="Source version: 0.2.0.dev2" src="https://img.shields.io/static/v1?label=Source%20version&amp;message=0.2.0.dev2&amp;labelColor=1E293B&amp;color=4338CA"></a>
<a href="https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/pyproject.toml"><img alt="Python: &gt;=3.10,&lt;3.15" src="https://img.shields.io/static/v1?label=Python&amp;message=%3E%3D3.10%2C%3C3.15&amp;labelColor=1E293B&amp;color=0F766E"></a>
<a href="https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/pyproject.toml"><img alt="Layer: governance" src="https://img.shields.io/static/v1?label=Layer&amp;message=governance&amp;labelColor=1E293B&amp;color=6D28D9"></a>
<a href="https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/README.md#lifecycle-and-migration"><img alt="Lifecycle: active" src="https://img.shields.io/static/v1?label=Lifecycle&amp;message=active&amp;labelColor=1E293B&amp;color=166534"></a>
<a href="https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/static/v1?label=License&amp;message=Apache-2.0&amp;labelColor=1E293B&amp;color=86198F"></a>
<a href="https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/README.md#notices"><img alt="Notice: not required" src="https://img.shields.io/static/v1?label=Notice&amp;message=not%20required&amp;labelColor=1E293B&amp;color=475569"></a>
</p>
<p align="center">
<a href="https://pypi.org/project/seo-aeo-aieo-governance-pack/"><img alt="Monthly PyPI downloads: seo-aeo-aieo-governance-pack" src="https://img.shields.io/pypi/dm/seo-aeo-aieo-governance-pack?labelColor=1E293B&amp;color=0E7490"></a>
<a href="https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/README.md"><img alt="README hits: seo-aeo-aieo-governance-pack" src="https://hits.sh/github.com/groupsum/seo-aeo-aieo-governance-pack/README.md.svg?label=README%20hits&amp;labelColor=1E293B&amp;color=0E7490"></a>
</p>
<p align="center">
<a href="https://github.com/groupsum/seo-aeo-aieo-governance-pack/actions/workflows/readme-standards.yml"><img alt="README standards: CI gate" src="https://img.shields.io/static/v1?label=README%20standards&amp;message=CI%20gate&amp;labelColor=1E293B&amp;color=1D4ED8"></a>
<a href="https://github.com/groupsum/seo-aeo-aieo-governance-pack/actions/workflows/readme-standards.yml"><img alt="Tests: package and example checks" src="https://img.shields.io/static/v1?label=Tests&amp;message=package%20and%20example%20checks&amp;labelColor=1E293B&amp;color=0F766E"></a>
<a href="https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/README.md#certification-status"><img alt="Certification: not certified" src="https://img.shields.io/static/v1?label=Certification&amp;message=not%20certified&amp;labelColor=1E293B&amp;color=92400E"></a>
<a href="https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/docs/pack-guide.md"><img alt="Governance: pack governance" src="https://img.shields.io/static/v1?label=Governance&amp;message=pack%20governance&amp;labelColor=1E293B&amp;color=4338CA"></a>
<a href="https://github.com/groupsum/seo-aeo-aieo-governance-pack/actions/workflows/readme-standards.yml"><img alt="Evidence: README and wheel checks" src="https://img.shields.io/static/v1?label=Evidence&amp;message=README%20and%20wheel%20checks&amp;labelColor=1E293B&amp;color=6D28D9"></a>
</p>
<p align="center"><a href="#overview">Overview</a> · <a href="#installation">Installation</a> · <a href="#quick-start">Quick Start</a> · <a href="#usage">Usage</a> · <a href="#public-api-and-import-surfaces">API</a> · <a href="#contributing">Contributing</a> · <a href="#governance">Governance</a> · <a href="#license">License</a></p>
<!-- readme-standards:end branding -->

---

## Overview

### Summary

Installable SSOT governance pack for SEO, AEO, and AiEO documents.

### Why This Package

The pack supplies versioned, source-linked ADR and SPEC templates for SEO, AEO, and AiEO Governance Pack.

### When to Use

Use this pack when a downstream SSOT Registry needs reusable decisions and requirements for SEO, AEO, and AiEO Governance Pack.

### Features

**Included ADRs**

- [`adr:0800`](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/src/seo_aeo_aieo_governance_pack/templates/adr/ADR-0800-seo-aeo-aieo-origin-packaging.yaml) — SEO, AEO, and AiEO governance documents ship as an installable extension pack
- [`adr:0801`](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/src/seo_aeo_aieo_governance_pack/templates/adr/ADR-0801-crawl-control-is-distinct-from-indexing-control.yaml) — Crawl control is distinct from indexing control
- [`adr:0802`](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/src/seo_aeo_aieo_governance_pack/templates/adr/ADR-0802-discovery-artifacts-are-separate-from-metadata-artifacts.yaml) — Discovery artifacts are separate from metadata artifacts
- [`adr:0803`](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/src/seo_aeo_aieo_governance_pack/templates/adr/ADR-0803-canonical-html-metadata-remains-the-source-page-contract.yaml) — Canonical HTML metadata remains the source page contract
- [`adr:0804`](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/src/seo_aeo_aieo_governance_pack/templates/adr/ADR-0804-structured-data-uses-layered-authority.yaml) — Structured data uses layered authority
- [`adr:0805`](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/src/seo_aeo_aieo_governance_pack/templates/adr/ADR-0805-google-ai-features-do-not-justify-ai-specific-schema-or-ai-only-files.yaml) — Google AI features do not justify AI-specific schema or AI-only files
- [`adr:0806`](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/src/seo_aeo_aieo_governance_pack/templates/adr/ADR-0806-accessibility-conformance-is-a-governed-discovery-quality-prerequisite.yaml) — Accessibility conformance is a governed discovery-quality prerequisite
- [`adr:0807`](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/src/seo_aeo_aieo_governance_pack/templates/adr/ADR-0807-social-graph-metadata-is-separate-from-search-structured-data.yaml) — Social graph metadata is separate from search structured data
- [`adr:0808`](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/src/seo_aeo_aieo_governance_pack/templates/adr/ADR-0808-ai-crawler-controls-must-distinguish-search-training-and-user-triggered-fetch.yaml) — AI crawler controls must distinguish search, training, and user-triggered fetch
- [`adr:0809`](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/src/seo_aeo_aieo_governance_pack/templates/adr/ADR-0809-llmstxt-is-experimental-and-must-not-outrank-canonical-surfaces.yaml) — llms.txt is experimental and must not outrank canonical surfaces
- [`adr:search-governance-consumes-canonical-performance-evidence`](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/src/seo_aeo_aieo_governance_pack/templates/adr/ADR-812-search-governance-consumes-canonical-performance-evidence.yaml) — Search Governance Consumes Canonical Performance Evidence

**Included SPECs**

- [`spc:0800`](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/src/seo_aeo_aieo_governance_pack/templates/specs/SPEC-0800-seo-governance-surface.yaml) — SEO governance surface
- [`spc:0801`](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/src/seo_aeo_aieo_governance_pack/templates/specs/SPEC-0801-aeo-answer-surface-contract.yaml) — AEO answer surface contract
- [`spc:0802`](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/src/seo_aeo_aieo_governance_pack/templates/specs/SPEC-0802-aieo-citation-and-provenance-contract.yaml) — AiEO citation and provenance contract
- [`spc:0803`](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/src/seo_aeo_aieo_governance_pack/templates/specs/SPEC-0803-robots-exclusion-protocol-contract.yaml) — Robots exclusion protocol contract
- [`spc:0804`](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/src/seo_aeo_aieo_governance_pack/templates/specs/SPEC-0804-sitemap-and-sitemap-index-contract.yaml) — Sitemap and sitemap-index contract
- [`spc:0805`](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/src/seo_aeo_aieo_governance_pack/templates/specs/SPEC-0805-html-head-metadata-and-canonical-link-contract.yaml) — HTML head metadata and canonical link contract
- [`spc:0806`](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/src/seo_aeo_aieo_governance_pack/templates/specs/SPEC-0806-structured-data-vocabulary-and-encoding-contract.yaml) — Structured data vocabulary and encoding contract
- [`spc:0807`](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/src/seo_aeo_aieo_governance_pack/templates/specs/SPEC-0807-google-search-eligibility-and-structured-data-quality-contract.yaml) — Google Search eligibility and structured data quality contract
- [`spc:0808`](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/src/seo_aeo_aieo_governance_pack/templates/specs/SPEC-0808-google-ai-features-eligibility-contract.yaml) — Google AI features eligibility contract
- [`spc:0809`](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/src/seo_aeo_aieo_governance_pack/templates/specs/SPEC-0809-helpful-reliable-people-first-content-contract.yaml) — Helpful, reliable, people-first content contract
- [`spc:0810`](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/src/seo_aeo_aieo_governance_pack/templates/specs/SPEC-0810-wcag-2-1-aa-accessibility-contract.yaml) — WCAG 2.1 AA accessibility contract
- [`spc:0812`](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/src/seo_aeo_aieo_governance_pack/templates/specs/SPEC-0812-open-graph-contract.yaml) — Open Graph contract
- [`spc:0813`](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/src/seo_aeo_aieo_governance_pack/templates/specs/SPEC-0813-x-twitter-cards-contract.yaml) — X / Twitter Cards contract
- [`spc:0814`](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/src/seo_aeo_aieo_governance_pack/templates/specs/SPEC-0814-dcmi-interoperable-metadata-contract.yaml) — DCMI interoperable metadata contract
- [`spc:0815`](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/src/seo_aeo_aieo_governance_pack/templates/specs/SPEC-0815-openai-crawler-controls-contract.yaml) — OpenAI crawler controls contract
- [`spc:0816`](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/src/seo_aeo_aieo_governance_pack/templates/specs/SPEC-0816-llmstxt-experimental-contract.yaml) — `llms.txt` experimental contract
- [`spc:search-performance-evidence-profile`](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/src/seo_aeo_aieo_governance_pack/templates/specs/SPEC-821-search-performance-evidence-profile.yaml) — Search Performance Evidence Profile

### Non-Goals

The pack supplies governance records. A downstream application implements the controls and collects its own conformance evidence.

---

## Getting Started

### Prerequisites

Use Python `>=3.10,<3.15`. Downstream synchronization also requires SSOT Registry and permission to write the target registry.

### Installation

#### uv

<!-- readme-standards:begin installation.uv -->
```bash
uv add seo-aeo-aieo-governance-pack
```
<!-- readme-standards:end installation.uv -->

#### pip

<!-- readme-standards:begin installation.pip -->
```bash
python -m pip install seo-aeo-aieo-governance-pack
```
<!-- readme-standards:end installation.pip -->

#### Poetry

<!-- readme-standards:begin installation.poetry -->
```bash
poetry add seo-aeo-aieo-governance-pack
```
<!-- readme-standards:end installation.poetry -->

### Quick Start

#### Example

<!-- readme-standards:begin example.quick-start -->
Source: [examples/quick_start.py](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/examples/quick_start.py).

```python
"""Inspect the installed pack identity."""

from seo_aeo_aieo_governance_pack import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:seo-aeo-aieo-governance"
print(metadata["origin"]["id"])
```
<!-- readme-standards:end example.quick-start -->

#### Expected Result

The script prints `pack:seo-aeo-aieo-governance` from the installed pack metadata.

---

## Usage

### Common Workflows

<!-- readme-standards:begin example.usage -->
Source: [examples/usage.py](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/examples/usage.py).

```python
"""Find a specification and its downstream path in the installed manifest."""

from seo_aeo_aieo_governance_pack import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:0800"
)
assert specification["target_path"] == ".ssot/specs/SPEC-0800-seo-governance-surface.yaml"
```
<!-- readme-standards:end example.usage -->

Use the downstream environment that has both SSOT Registry and `seo-aeo-aieo-governance-pack` installed. Inspect the pack and preflight the target registry before approving synchronization.

```bash
uv run ssot pack inspect seo_aeo_aieo_governance_pack
uv run ssot pack preflight . seo_aeo_aieo_governance_pack --all
uv run ssot pack sync . seo_aeo_aieo_governance_pack --all --trust --yes
uv run ssot validate .
```

### Configuration

Select the installed import package `seo_aeo_aieo_governance_pack` in SSOT Registry. Review reservation owner `extension-pack:seo-aeo-aieo-governance-pack` and the target's trust policy before syncing.

### Error Handling

If preflight reports a schema, trust, or document-number conflict, resolve it in the target registry and repeat preflight before synchronization.

### Best Practices

Pin the pack version in downstream projects. Reference document IDs in local governance and inspect the change set before granting trust.

---

## Package Boundary

### What It Owns

Removed duplicate performance metric definitions and added a search-performance evidence profile.

### Public API and Import Surfaces

Import `load_pack_metadata`, `load_document_manifest`, and `read_packaged_document_text` from `seo_aeo_aieo_governance_pack` to inspect packaged records.

### Entry Points

<!-- readme-standards:begin entry-points -->
This package declares no command-line, GUI, or plugin entry points in its manifest.
<!-- readme-standards:end entry-points -->

### Injected Dependencies

The package binds its metadata and document loaders through `ssot-pack-contracts`. The caller supplies the target registry to SSOT Registry when synchronizing.

### Protocol Consumers

SSOT Registry uses the pack metadata, document manifests, and bundled templates during inspect, preflight, and sync.

### Extensions

Define downstream policies as local records and reference the pack's document IDs. Send proposed changes to the canonical pack through repository review.

---

## Operations and Readiness

### Operational Requirements

Local inspection reads installed package resources. Synchronization requires an initialized downstream registry and explicit operator approval.

### Health and Observability

Review the preflight and sync output, then use `ssot validate` to check the resulting registry.

### Security and Resource Limits

Implicit trust is disabled. Review the exact distribution, version, records, and reserved IDs before enabling trust in a target registry.

### Compatibility

- Python `>=3.10,<3.15`
- SSOT Registry schema `>=0.4.0`
- SSOT pack contracts `>=0.2.17,<0.3.0`

---

## Verification

### Tests

Run `python -m unittest discover -s tests -v` with the pack installed. The [README workflow](https://github.com/groupsum/seo-aeo-aieo-governance-pack/actions/workflows/readme-standards.yml) checks the source README and runs both examples against an installed wheel.

### Certification Status

The pack has no external certification. Downstream adoption requires evidence for the controls an application implements.

### Evidence

See the [README workflow](https://github.com/groupsum/seo-aeo-aieo-governance-pack/actions/workflows/readme-standards.yml) for package and documentation verification and the [packaged records](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/src/seo_aeo_aieo_governance_pack/templates) for document-level sources.

---

## FAQ

### Why

**Why do document IDs matter?** Downstream records use them to trace an adopted decision or requirement to the pack that owns it.

### How

**How do I preview changes?** Use the registry's pack preflight before approving a sync.

### When

**When should I upgrade?** Read the changelog and preflight the new version against the target registry before applying it.

---

## Documentation and Related Packages

### More Documentation

See the [Pack guide](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/docs/pack-guide.md), [changelog](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/CHANGELOG.md), and [pack metadata](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/src/seo_aeo_aieo_governance_pack/metadata.json).

### Related Packages

[SSOT Registry](https://pypi.org/project/ssot-registry/) manages downstream registries. [SSOT Pack Contracts](https://pypi.org/project/ssot-pack-contracts/) provides the shared pack interface.

### Project Links

<!-- readme-standards:begin project-links -->
- [Homepage](https://github.com/groupsum/seo-aeo-aieo-governance-pack)
- [Issues](https://github.com/groupsum/seo-aeo-aieo-governance-pack/issues)
- [Repository](https://github.com/groupsum/seo-aeo-aieo-governance-pack)
- [pypi: seo-aeo-aieo-governance-pack](https://pypi.org/project/seo-aeo-aieo-governance-pack/)
<!-- readme-standards:end project-links -->

---

## Contributing

### How to Contribute

Open an [issue](https://github.com/groupsum/seo-aeo-aieo-governance-pack/issues) or pull request describing the affected records, their authority, and the expected downstream effect.

### Development Setup

Install the checkout with `python -m pip install -e .`, then run `python -m unittest discover -s tests -v`. On Python 3.11 or newer, run `uvx --from readme-standards==0.1.3 readme-standards check`.

### Notes for Maintainers

Keep source links, document identifiers, and committed manifest hashes aligned. Run `uvx --from readme-standards==0.1.3 readme-standards render --write` after changing generated README inputs.

---

## Governance

### Ownership and Decision Making

Groupsum maintains `pack:seo-aeo-aieo-governance`. The pack's reservation owner is `extension-pack:seo-aeo-aieo-governance-pack`. Downstream registry operators approve synchronization.

### Standards and Policies

Review the [governance documentation](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/docs/pack-guide.md) and the primary references carried by the individual records.

### Lifecycle and Migration

Review [release changes](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/CHANGELOG.md) and preflight the chosen version against each downstream registry.

---

## License and Attribution

### License

<!-- readme-standards:begin license -->
Licensed under `Apache-2.0`. See [LICENSE](https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/LICENSE).
<!-- readme-standards:end license -->

### Notices

<!-- readme-standards:begin notices -->
No separate NOTICE file is declared. Review the license and bundled third-party attributions.
<!-- readme-standards:end notices -->
