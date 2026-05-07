<div align="center">

<h1>seo-aeo-aieo-governance-pack</h1>

<p>
  <a href="https://pypi.org/project/seo-aeo-aieo-governance-pack/"><img alt="PyPI version" src="https://img.shields.io/pypi/v/seo-aeo-aieo-governance-pack.svg"></a>
  <a href="https://pepy.tech/projects/seo-aeo-aieo-governance-pack"><img alt="Downloads" src="https://static.pepy.tech/badge/seo-aeo-aieo-governance-pack"></a>
  <a href="https://pypi.org/project/seo-aeo-aieo-governance-pack/"><img alt="Python versions" src="https://img.shields.io/pypi/pyversions/seo-aeo-aieo-governance-pack.svg"></a>
  <a href="https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/pypi/l/seo-aeo-aieo-governance-pack.svg"></a>
  <a href="https://github.com/groupsum/seo-aeo-aieo-governance-pack/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/groupsum/seo-aeo-aieo-governance-pack/actions/workflows/ci.yml/badge.svg?branch=master"></a>
</p>

<p>
  <a href="https://github.com/groupsum/seo-aeo-aieo-governance-pack"><img alt="GitHub repo" src="https://img.shields.io/badge/GitHub-groupsum%2Fseo--aeo--aieo--governance--pack-181717?logo=github"></a>
</p>

</div>

`seo-aeo-aieo-governance-pack` is a small SSOT-compatible document pack for SEO, AEO, and AiEO governance.

It is designed to be published to PyPI and consumed by [`ssot-registry`](https://pypi.org/project/ssot-registry/) as an installable `extension-pack` document source. This repository does not perform downstream mutation itself. Its job is to ship immutable ADR and SPEC artifacts plus manifests that a downstream [`ssot-registry`](https://pypi.org/project/ssot-registry/) runtime can sync into the downstream `.ssot` registry.

The packaged distribution has one document artifact surface: `src/seo_aeo_aieo_governance_pack/templates/`. This repository does not package or maintain a parallel `.ssot/registry.json`.

## What is in scope

- upstream ADRs for SEO, AEO, and AiEO governance
- upstream SPECs for SEO, AEO, and AiEO operator requirements
- packaged manifests for ADR and SPEC discovery
- a minimal Python loader module for runtime consumption

## What is intentionally out of scope

- downstream feature, claim, test, evidence, boundary, or release mutation
- repo-specific scoring logic
- crawler, answer-engine, or model-runtime implementations

## Canonical layout

- repo-local source ADRs: `.ssot/adr/`
- repo-local source SPECs: `.ssot/specs/`
- packaged ADR templates: `src/seo_aeo_aieo_governance_pack/templates/adr/`
- packaged SPEC templates: `src/seo_aeo_aieo_governance_pack/templates/specs/`

The repo-local `.ssot` documents are the authored source files in this repository. The packaged templates and manifests are the only shipped distribution artifact and are derived with:

```bash
python scripts/sync_packaged_docs.py
```

## Install

```bash
python -m pip install seo-aeo-aieo-governance-pack
```

## Programmatic usage

```python
from seo_aeo_aieo_governance_pack import load_document_manifest, read_packaged_document_text

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")
print(adr_manifest[0]["id"])
print(spec_manifest[0]["id"])

text = read_packaged_document_text("spec", "SPEC-0801-aeo-answer-surface-contract.yaml")
print(text[:120])
```

## Initial upstream documents

- `adr:0800` SEO, AEO, and AiEO documents ship as an installable extension pack
- `adr:0801` crawl control is distinct from indexing control
- `adr:0802` discovery artifacts are separate from metadata artifacts
- `adr:0803` canonical HTML metadata remains the source page contract
- `adr:0804` structured data uses layered authority
- `adr:0805` Google AI features do not justify AI-specific schema or AI-only files
- `adr:0807` social graph metadata is separate from search structured data
- `adr:0808` AI crawler controls must distinguish search, training, and user-triggered fetch
- `adr:0809` `llms.txt` is experimental and must not outrank canonical surfaces
- `spc:0800` SEO governance surface
- `spc:0801` AEO answer surface contract
- `spc:0802` AiEO citation and provenance contract
- `spc:0803` robots exclusion protocol contract
- `spc:0804` sitemap and sitemap-index contract
- `spc:0805` HTML head metadata and canonical link contract
- `spc:0806` structured data vocabulary and encoding contract
- `spc:0807` Google Search eligibility and structured data quality contract
- `spc:0808` Google AI features eligibility contract
- `spc:0809` helpful, reliable, people-first content contract
- `spc:0811` Core Web Vitals performance contract
- `spc:0812` Open Graph contract
- `spc:0813` X / Twitter Cards contract
- `spc:0814` DCMI interoperable metadata contract
- `spc:0815` OpenAI crawler controls contract
- `spc:0816` `llms.txt` experimental contract

## Release notes

This repository includes reusable [`cobycloud/actions`](https://github.com/cobycloud/actions) workflows for:

- CI
- GitHub release creation
- PyPI publishing
