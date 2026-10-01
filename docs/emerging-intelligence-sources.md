# Emerging Intelligence Sources

OSINTAI tracks not only new tools, but also **new source classes**. A source class matters when it creates investigative value that did not previously exist, or makes previously inaccessible information systematically searchable.

## PromptINT

PromptINT was presented at the SANS OSINT Summit 2026 as a methodology for analyzing exposed LLM conversations and leaked system prompts.

### Why it matters

LLM artifacts can reveal:
- workflow logic;
- organizational language;
- decision rules;
- escalation paths;
- integration assumptions;
- security and authentication assumptions;
- model usage patterns.

### Evidence model

A leaked prompt should be treated as an artifact with provenance, not as proof that the described workflow is current or universally deployed.

Recommended states:
- discovered;
- source-validated;
- organization-linked;
- temporally validated;
- corroborated;
- analyst-reviewed.

### Privacy boundary

PromptINT carries unusually high privacy risk because exposed conversations may include information that was never intentionally published for broad discovery.

OSINTAI therefore treats:
- public indexability;
- lawful accessibility;
- appropriate collection;
- appropriate retention;
- appropriate dissemination

as separate questions.

## Torrent Metadata Intelligence

The 2026 preprint *Breadcrumbs in the Digital Forest* explores public torrent metadata as a scalable OSINT signal.

Potential analytical value:
- temporal patterns;
- peer clustering;
- co-occurrence;
- infrastructure patterns;
- anonymization indicators;
- network-level behavioral signals.

### Attribution warning

An IP address or torrent peer observation is not a person.

Analysts must account for:
- NAT;
- shared networks;
- VPNs;
- proxies;
- dynamic addressing;
- compromised hosts;
- measurement error.

The source is best treated as a **lead-generation and behavioral signal**, not a standalone identity claim.

## Public AI-System Metadata

AI systems now generate a large public metadata surface:

- model cards;
- package metadata;
- public repositories;
- API documentation;
- deployment fingerprints;
- MCP metadata;
- SBOMs;
- release notes;
- vulnerability advisories;
- public incident reports.

This creates a new defensive OSINT domain: mapping the **AI software supply chain and observable deployment ecosystem**.

## Live Multimedia Streams

AVH-like systems demonstrate that live video can be treated as a continuous source rather than a manually reviewed artifact.

Relevant derived signals can include:
- objects;
- logos;
- visible text;
- speech transcripts;
- time;
- scene changes;
- geospatial clues.

Derived signals remain hypotheses until validated against captured frames/audio and independent sources.

## Unstructured Leak and Hidden-Service Content

AIL Framework illustrates how heterogeneous content can be normalized into searchable intelligence:
- screenshots;
- chat messages;
- PDFs;
- encoded files;
- QR/barcodes;
- crawled pages;
- Tor/I2P content;
- image descriptions.

The key architectural requirement is that every derived representation remains linked to the original artifact.

## Source maturity model

| Level | Description |
|---|---|
| **S0 Experimental** | interesting signal with little validation |
| **S1 Observable** | source can be consistently collected |
| **S2 Structurable** | artifacts can be normalized and indexed |
| **S3 Correlatable** | source can be linked to independent evidence |
| **S4 Validated** | methodology has documented evaluation |
| **S5 Operationally defensible** | provenance, legal/privacy controls and reproducibility are mature |

A new source is not valuable merely because it is novel. Novel garbage is still garbage, only with a conference slide.
