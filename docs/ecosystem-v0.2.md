# OSINTAI Ecosystem Map — v0.2

Reviewed: **2026-10-01**

This map expands OSINTAI beyond a simple tools list. Resources are grouped by investigative role, architecture and trust level. Quantitative claims are treated as time-sensitive maintainer claims unless independently benchmarked.

## Agentic and orchestration platforms

| Project | Role | Architecture | Local option | Status |
|---|---|---|---|---|
| [OpenOSINT](https://github.com/OpenOSINT/OpenOSINT) | general AI-assisted OSINT | tool-calling agent + MCP | Yes | verified |
| [Argus OS](https://github.com/AXRoux/argus-os) | adaptive OSINT orchestration | planner-agent + adapters | Yes | verified |
| [FETIH](https://github.com/MustafaKemal0146/fetih) | security/OSINT agent | autonomous + multi-agent + skills | Yes | verified |
| [Unburden](https://github.com/ghostvyle/Unburden) | local security orchestration | local LLM + MCP | Yes | verified |
| [Focal Harvest](https://github.com/techno-neighbour/focal-harvest) | research and monitoring | pipeline + LLM synthesis | Partial | verified |

## Local-first and evidence-oriented systems

| Project | Distinguishing capability | Evidence/graph posture |
|---|---|---|
| [OSINTai](https://github.com/gs-ai/OSINTai) | async crawler with Ollama | evidence-labelled findings, correlations, timelines and graph export |
| [WorldView](https://github.com/Hunter5Thompson/OSINT) | tactical GEOINT/situational awareness | Neo4j + Qdrant + local multi-agent RAG |
| [PANO](https://github.com/ALW1EZ/PANO) | graph/timeline/map investigation | graph-centric investigation with PANAI assistant |
| [Taranis AI](https://github.com/taranis-ai/taranis-ai) | OSINT collection and situational analysis | analyst workflow with structured reporting |

## Specialized investigation domains

| Domain | Resources |
|---|---|
| Dark-web OSINT | [Robin](https://github.com/apurvsinghgautam/robin) |
| SOCMINT | [OWASP Social OSINT Agent](https://github.com/bm-github/owasp-social-osint-agent) |
| GEOINT / tactical intelligence | [WorldView](https://github.com/Hunter5Thompson/OSINT) |
| Search-based discovery | [Banshee-AI](https://github.com/Vulnpire/Banshee-AI) |
| Military OSINT | [Theosight](https://www.eos-applications.com/) |

## MCP and tool fabrics

| Resource | Focus |
|---|---|
| [osint-mcp-server](https://github.com/badchars/osint-mcp-server) | infrastructure OSINT sources exposed through MCP |
| [MCP DadosBR](https://github.com/cristianoaredes/mcp-dadosbr) | Brazilian public-data intelligence |
| [GreyNoise MCP Server](https://github.com/GreyNoise-Intelligence/greynoise-mcp-server) | threat intelligence and infrastructure context |
| [Awesome OSINT MCP Servers](https://github.com/soxoj/awesome-osint-mcp-servers) | discovery index organized by intelligence domain |

## AI infrastructure as an OSINT subject

[7WaySecurity/ai_osint](https://github.com/7WaySecurity/ai_osint) establishes an important separate category: AI systems themselves can become the subject of defensive OSINT. Relevant public signals include service metadata, exposed management interfaces, model and package registries, vector-database technologies, AI agent/MCP ecosystems, MLOps components and public incident reporting.

OSINTAI deliberately documents this category as **defensive exposure intelligence**. It does not reproduce secret-harvesting queries or turn third-party exposure into an exploitation workflow.

See [ai-infrastructure-osint.md](ai-infrastructure-osint.md).

## Curated discovery sources

- [The OSINT Toolbox — AI Resources](https://github.com/The-Osint-Toolbox/AI-Resources)
- [Awesome AI OSINT](https://github.com/ubikron/Awesome-AI-OSINT)
- [Awesome OSINT MCP Servers](https://github.com/soxoj/awesome-osint-mcp-servers)
- [AI OSINT / 7WaySecurity](https://github.com/7WaySecurity/ai_osint)

These collections are excellent discovery feeds, but OSINTAI independently verifies high-value entries before promoting them into the primary catalog.

## Research layer

Notable additions in v0.2 include:

- **MOSAIV (ICMR 2026)** — multi-agent multimedia verification with Prime, Verification and Localization stages.
- **Automated MITRE ATT&CK Technique Classification Using OSINT and Advanced NLP (2026)**.
- **The Cognitive Fingerprint (2026 preprint)** — temporal/syntactic cross-domain attribution research; results remain preprint claims.
- **Open-Source Intelligence Analysis Method Based on Fine-Tuned Large Models and Knowledge Graphs (2025)**.
- **n8n + LLM + OSINT architecture (2026)** — modular workflow automation research.
- **Remote sensing + OSINT multimodal alignment (2026)** — retained as a candidate until canonical proceedings metadata is directly verified.

Structured metadata lives in `catalog/research.json`.

## Training layer

Verified training references are maintained separately in `catalog/training.json`, including JEIS, RRU/RISE, IAI, CyberSafe and the SCSP/Coursera Intelligence Edge course.

## Corrections applied during verification

- **OpenOSINT:** current project documentation advertises 20 modular investigation tools, so the older claim of 18 was not retained.
- **OSINTai:** the `gs-ai/OSINTai` repository is treated as the primary catalog record; `UberGuidoZ/osintai` is documented as a related public lineage rather than silently conflated.
- **MOSAIV:** verified as an ACM ICMR 2026 research paper, not promoted as a standalone production platform.
- **Theosight:** the official Eos Applications site currently presents it as an active commercial product; the unverified 'launch in 2027' claim was removed.
- **Fine-tuned LLM + knowledge graph paper:** publication year is 2025 even though IEEE Xplore indexed it in 2026.
- **AgentOSINT and VulnAI Pro:** remain outside the verified catalog because the specific claims supplied were not backed by a canonical source during review.

## Selection principle

OSINTAI prefers a smaller verified catalog over a larger hallucinated one. Discovery is cheap. Provenance is the work.