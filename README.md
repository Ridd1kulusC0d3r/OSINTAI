# OSINTAI

> **Open Source Intelligence × Artificial Intelligence**
>
> A verification-first knowledge base for AI-augmented OSINT, agentic investigation, MCP ecosystems, local-first workflows, evaluation, governance, and OSINT focused on AI infrastructure.

[![Catalog Validation](https://github.com/Ridd1kulusC0d3r/OSINTAI/actions/workflows/validate-catalog.yml/badge.svg)](https://github.com/Ridd1kulusC0d3r/OSINTAI/actions/workflows/validate-catalog.yml)
![Status](https://img.shields.io/badge/status-v0.1%20foundation-blue)
![Focus](https://img.shields.io/badge/focus-OSINT%20%2B%20AI-purple)

## Why this repository exists

OSINT is rapidly absorbing LLMs, agents, multimodal models, graph reasoning, local inference and MCP tool ecosystems. The useful part is real. The hype is also very real.

**OSINTAI separates:**

- tools that actually exist from claims that merely circulate;
- collection from analysis;
- model output from evidence;
- automation from autonomy;
- AI-assisted investigation from OSINT against AI infrastructure;
- “interesting demo” from “operationally defensible workflow”.

The repository is designed for analysts, investigators, CTI teams, researchers and builders who need an **auditable map of the OSINT + AI ecosystem**.

## The OSINTAI model

~~~mermaid
flowchart LR
    A[Requirements] --> B[Collection]
    B --> C[Preservation & Provenance]
    C --> D[Extraction & Normalization]
    D --> E[Entity Resolution]
    E --> F[Enrichment]
    F --> G[Correlation / Graph]
    G --> H[Verification]
    H --> I[Analysis & Hypotheses]
    I --> J[Human Review]
    J --> K[Reporting / Dissemination]

    L[LLM / Agent Layer] -. assists .-> A
    L -. tool use .-> B
    L -. transforms .-> D
    L -. reasons over .-> G
    L -. proposes .-> I

    M[Evidence Ledger] --- C
    M --- H
    M --- K
~~~

**Rule zero:** an LLM response is not evidence. Evidence must remain traceable to a source, acquisition event and analyst decision.

## Core areas

| Area | What OSINTAI maps |
|---|---|
| **Agentic OSINT** | planning, tool orchestration, multi-step investigations, human-in-the-loop |
| **MCP for OSINT** | MCP servers, tool exposure, trust boundaries, least privilege |
| **Local-first AI** | Ollama/local models, private inference, sensitive-case isolation |
| **Multimodal OSINT** | image, video, OCR, audio, document and geospatial analysis |
| **Graph & entity intelligence** | entity extraction, resolution, knowledge graphs, relationship reasoning |
| **Verification** | source triangulation, provenance, factuality, media verification |
| **Automation** | monitoring, ingestion, enrichment, reporting and alerting |
| **OSINT for AI systems** | exposed AI services, public model/service metadata, AI supply-chain intelligence |
| **Evaluation** | reproducibility, hallucination measurement, provenance, security and cost |
| **Governance** | privacy, proportionality, human oversight, evidence handling, AI risk |

## Verified ecosystem snapshot

The table below contains projects whose repository identity and current description were manually checked for this foundation release.

| Project | Primary role | AI / agent pattern | MCP | Local-first | Verification |
|---|---|---|---|---|---|
| [OpenOSINT](https://github.com/OpenOSINT/OpenOSINT) | AI-assisted investigation toolkit | tool-calling agent | Yes | Optional | README checked |
| [Taranis AI](https://github.com/taranis-ai/taranis-ai) | OSINT collection + situational analysis | NLP/AI enrichment + analyst workflow | No | Self-hosted | README checked |
| [PANO](https://github.com/ALW1EZ/PANO) | graph/timeline investigation platform | PANAI assistant | No | Desktop/self-hosted | README checked |
| [Argus](https://github.com/AXRoux/argus-os) | agentic OSINT orchestration | autonomous tool orchestration | No | Optional | README checked |
| [osint-mcp-server](https://github.com/badchars/osint-mcp-server) | OSINT tools exposed to agents | MCP tool layer | Yes | Client-dependent | README checked |
| [MCP DadosBR](https://github.com/cristianoaredes/mcp-dadosbr) | Brazilian public-data OSINT | MCP tool layer | Yes | Client-dependent | README checked |
| [Focal Harvest](https://github.com/techno-neighbour/focal-harvest) | research + monitoring pipeline | LLM synthesis / collection automation | No | Has offline fallback | README checked |

Machine-readable records live in catalog/tools.json.

## Verification levels

OSINTAI does **not** treat every discovered project as equally trustworthy.

| Level | Meaning |
|---|---|
| **verified** | canonical repository/source inspected; description is grounded in that source |
| **candidate** | project appears to exist, but claims still need deeper validation |
| **archival** | useful historical reference; inactive or superseded |
| **rejected** | claim could not be substantiated or was materially misleading |

See docs/verification-notes.md for claims intentionally kept out of the verified catalog.

## Reference architecture

A defensible OSINT+AI stack should separate the evidence plane from the model plane.

~~~text
Sources
  ↓
Collectors / MCP / APIs
  ↓
Capture + hashing + timestamps + source metadata
  ↓
Normalization / parsing / OCR / transcription
  ↓
Evidence store ────────────────┐
  ↓                            │
Entity resolution              │
  ↓                            │
Graph / search / retrieval     │
  ↓                            │
LLM / agent sandbox            │
  ↓                            │
Hypotheses + confidence        │
  ↓                            │
Verification against evidence ←┘
  ↓
Human review
  ↓
Report with citations + provenance
~~~

Full design: docs/reference-architecture.md

## What makes OSINTAI different

1. **Verification-first curation** — ambiguous or unsupported claims are quarantined instead of promoted.
2. **Human + machine readable** — Markdown for analysts, JSON + schema for automation and LLM retrieval.
3. **Evidence-centric architecture** — provenance is a first-class component, not a reporting afterthought.
4. **Benchmark mindset** — projects can be evaluated on reproducibility, factuality, provenance and agent safety.
5. **Security-aware agent design** — prompt injection, tool misuse and MCP supply-chain risks are part of the model.
6. **Privacy-aware workflows** — data minimization and case sensitivity influence architecture and model placement.
7. **Dual perspective** — AI can assist OSINT, and AI infrastructure itself can become an OSINT subject.

## Repository map

~~~text
OSINTAI/
├── README.md
├── CONTRIBUTING.md
├── ROADMAP.md
├── catalog/
│   ├── tools.json
│   └── research.json
├── docs/
│   ├── taxonomy.md
│   ├── reference-architecture.md
│   ├── evaluation-framework.md
│   ├── mcp-security.md
│   ├── governance.md
│   ├── learning-path.md
│   └── verification-notes.md
├── schemas/
│   └── tool.schema.json
├── scripts/
│   └── validate_catalog.py
└── .github/
    └── workflows/
        └── validate-catalog.yml
~~~

## Research anchors

The project prioritizes primary sources and high-quality research, including:

- *Agentic and Generative AI for Open-Source Intelligence and Cyber Investigations: Taxonomy, Evaluation, Challenges, and Future Directions* (2026)
- *A Framework for Embedding Generative and Agentic AI in Open Source Intelligence* (2025)
- NIST AI RMF + Generative AI Profile
- OSINT Privacy Impact Framework (OPIF), New America
- Berkeley Protocol on Digital Open Source Investigations
- OWASP Top 10 for Agentic Applications 2026

Structured citations and canonical links live in catalog/research.json.

## Start here

- Understand the field: docs/taxonomy.md
- Design a platform: docs/reference-architecture.md
- Evaluate tools and agents: docs/evaluation-framework.md
- Use MCP safely: docs/mcp-security.md
- Build responsible workflows: docs/governance.md
- Learn progressively: docs/learning-path.md
- See what was excluded and why: docs/verification-notes.md

## Scope and ethics

OSINTAI is for lawful, ethical and authorized research using public or legitimately accessible information. The project emphasizes proportionality, privacy, provenance, analyst accountability and human review.

It does not treat “publicly reachable” as equivalent to “appropriate to collect”, and it does not treat model confidence as factual confidence.

## Contributing

New resources are welcome, but every contribution should include a canonical source and enough evidence to classify the resource.

Read CONTRIBUTING.md before submitting additions.

---

**OSINTAI is not trying to make OSINT autonomous at any cost. It is trying to make AI-assisted OSINT more useful, reproducible, defensible and difficult to fool.**
