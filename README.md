<div align="center">

<h1>seo-aeo-aieo-governance-pack</h1>

<p>
  <a href="https://pypi.org/project/seo-aeo-aieo-governance-pack/"><img alt="PyPI version" src="https://img.shields.io/pypi/v/seo-aeo-aieo-governance-pack.svg"></a>
  <a href="https://pepy.tech/projects/seo-aeo-aieo-governance-pack"><img alt="Downloads" src="https://static.pepy.tech/badge/seo-aeo-aieo-governance-pack"></a>
  <a href="https://hits.sh/github.com/groupsum/seo-aeo-aieo-governance-pack/"><img alt="Hits" src="https://hits.sh/github.com/groupsum/seo-aeo-aieo-governance-pack.svg"></a>
  <a href="https://pypi.org/project/seo-aeo-aieo-governance-pack/"><img alt="Python versions" src="https://img.shields.io/pypi/pyversions/seo-aeo-aieo-governance-pack.svg"></a>
  <a href="https://github.com/groupsum/seo-aeo-aieo-governance-pack/blob/master/LICENSE"><img alt="License" src="https://img.shields.io/pypi/l/seo-aeo-aieo-governance-pack.svg"></a>
  <a href="https://github.com/groupsum/seo-aeo-aieo-governance-pack/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/groupsum/seo-aeo-aieo-governance-pack/actions/workflows/ci.yml/badge.svg?branch=master"></a>
</p>

<p>
  <a href="https://github.com/groupsum/seo-aeo-aieo-governance-pack"><img alt="GitHub repo" src="https://img.shields.io/badge/GitHub-groupsum%2Fseo--aeo--aieo--governance--pack-181717?logo=github"></a>
</p>

</div>

`seo-aeo-aieo-governance-pack` is an SSOT Registry pack for search visibility, answer visibility, AI citation readiness, web metadata quality, accessibility, and performance governance.

It gives product, platform, content, and compliance teams a shared set of Architecture Decision Records (ADRs) and Specifications (SPECs) that can be applied across many repositories. Centralizing these requirements turns discoverability work into reusable governance: one reviewed standard can be synchronized into project registries, linked to features and tests, and reused during release review instead of being rewritten from scratch in every product.

## What Is An SSOT Registry Pack?

An SSOT Registry pack is an installable package of governed ADRs and SPECs for [`ssot-registry`](https://pypi.org/project/ssot-registry/). The pack supplies reusable decision and requirement documents. `ssot-registry` applies those documents to a project registry so teams can trace product requirements from decision, to specification, to implementation, to tests and release evidence.

This makes governance portable. A project can adopt the pack, synchronize the documents, list the active requirements, and connect local features or tests to the shared IDs.

## Why This Pack Exists

Search, answer, and AI discovery requirements now span many surfaces: HTML metadata, structured data, robots policy, sitemaps, crawler controls, accessibility baselines, social graph previews, and performance signals. Teams need one durable source for these requirements so product changes, content operations, and technical implementation stay aligned.

This pack helps teams:

- apply reviewed SEO, AEO, and AiEO requirements quickly across projects
- keep search metadata, answer extraction, and AI citation requirements consistent
- give engineering and content teams the same IDs for planning, implementation, and review
- connect accessibility and performance quality to discoverability governance
- make release reviews easier by tracing project work back to shared ADRs and SPECs

## Domain Focus

The pack focuses on product domains where discoverability, answer quality, and machine-readable metadata directly affect user acquisition, trust, and citation quality:

- SEO and organic search governance
- AEO answer surface governance
- AiEO citation and provenance governance
- robots and crawler control policy
- sitemap and discovery artifact policy
- HTML head metadata and canonical URL policy
- structured data vocabulary and encoding quality
- social preview metadata for Open Graph and X / Twitter Cards
- accessibility baseline governance through WCAG 2.1 AA
- web performance quality using Core Web Vitals and supporting metrics
- AI crawler controls and experimental `llms.txt` handling

## Included ADRs

- `adr:0800` SEO, AEO, and AiEO documents ship as an installable extension pack
- `adr:0801` crawl control is distinct from indexing control
- `adr:0802` discovery artifacts are separate from metadata artifacts
- `adr:0803` canonical HTML metadata remains the source page contract
- `adr:0804` structured data uses layered authority
- `adr:0805` Google AI features do not justify AI-specific schema or AI-only files
- `adr:0806` accessibility conformance is a governed discovery-quality prerequisite
- `adr:0807` social graph metadata is separate from search structured data
- `adr:0808` AI crawler controls must distinguish search, training, and user-triggered fetch
- `adr:0809` `llms.txt` is experimental and must not outrank canonical surfaces
- `adr:0810` performance metrics use standards-backed authority where available
- `adr:0811` derived tooling metrics remain separate from web-platform normative metrics

## Included SPECs

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
- `spc:0810` WCAG 2.1 AA accessibility contract
- `spc:0811` Core Web Vitals performance contract
- `spc:0812` Open Graph contract
- `spc:0813` X / Twitter Cards contract
- `spc:0814` DCMI interoperable metadata contract
- `spc:0815` OpenAI crawler controls contract
- `spc:0816` `llms.txt` experimental contract
- `spc:0817` First Contentful Paint contract
- `spc:0818` Largest Contentful Paint contract
- `spc:0819` Long Tasks responsiveness contract
- `spc:0820` Total Blocking Time operator contract

## Install With uv

Install the pack into a project environment:

```bash
uv add seo-aeo-aieo-governance-pack
```

Install it alongside the SSOT Registry CLI:

```bash
uv add ssot-registry seo-aeo-aieo-governance-pack
```

Run without adding dependencies to a project:

```bash
uvx --from ssot-registry --with seo-aeo-aieo-governance-pack ssot --help
```

## Install With The SSOT Registry Pack CLI

Pack-enabled SSOT Registry environments can install and synchronize packs through the pack command surface:

```bash
uvx --from ssot-registry ssot pack install seo-aeo-aieo-governance-pack
uvx --from ssot-registry ssot pack sync . seo-aeo-aieo-governance-pack
```

## Use With The SSOT Registry CLI

After the pack is installed in the same environment as `ssot-registry`, synchronize ADRs and SPECs into a target repository:

```bash
uv run ssot adr sync .
uv run ssot spec sync .
```

Review the synchronized governance surface:

```bash
uv run ssot adr list .
uv run ssot spec list .
uv run ssot spec get . --id spc:0805
```

Use the IDs from this pack when linking project features, tests, claims, and release evidence in your local `.ssot` registry.

## Programmatic Usage

```python
from seo_aeo_aieo_governance_pack import load_document_manifest, read_packaged_document_text

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")

print(adr_manifest[0]["id"])
print(spec_manifest[0]["id"])

text = read_packaged_document_text("spec", "SPEC-0801-aeo-answer-surface-contract.yaml")
print(text[:120])
```

## Resources

- GitHub repository: [groupsum/seo-aeo-aieo-governance-pack](https://github.com/groupsum/seo-aeo-aieo-governance-pack)
- PyPI package: [seo-aeo-aieo-governance-pack](https://pypi.org/project/seo-aeo-aieo-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)

## Normative ownership boundary

Removed duplicate performance metric definitions and added a search-performance evidence profile.
