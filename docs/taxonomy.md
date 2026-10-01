# OSINTAI Taxonomy

This taxonomy classifies the OSINT + AI ecosystem by **investigative function**, **architecture**, **autonomy**, **deployment**, **evidence behavior** and **security boundary**.

## Intelligence-cycle functions

### Requirements and planning
AI may help decompose an intelligence requirement into questions, entities, collection plans and source classes.

Expected outputs:
- explicit intelligence questions;
- collection boundaries;
- assumptions;
- stop conditions;
- legal/privacy constraints.

### Collection
Systems acquire material from public sources, feeds, APIs, archives or approved datasets.

AI roles:
- query generation;
- source prioritization;
- tool selection;
- monitoring;
- deduplication suggestions.

### Preservation and provenance
Evidence should retain:
- original source;
- acquisition time;
- acquisition method;
- cryptographic hash where appropriate;
- collector identity/version;
- transformations;
- chain of derived artifacts.

### Extraction and normalization
Typical functions:
- OCR;
- transcription;
- language detection and translation;
- metadata parsing;
- structured field extraction;
- format normalization.

### Entity extraction and resolution
AI may identify and correlate people, organizations, domains, accounts, locations, events, infrastructure and aliases.

Entity resolution must distinguish:
- exact identity;
- candidate identity;
- similarity;
- analyst-confirmed equivalence.

### Enrichment
Examples:
- DNS/RDAP enrichment;
- public company records;
- public government data;
- threat-intelligence context;
- archive retrieval;
- geospatial or temporal context.

### Correlation and knowledge graphs
Graph systems can represent entities, claims, observations, sources, relationships, confidence and time.

The graph should not collapse “model-inferred relation” into “observed relation”.

### Verification
Verification includes source triangulation, temporal validation, geolocation validation, metadata consistency, contradiction search, media authenticity checks and provenance completeness.

### Analysis and hypothesis management
AI is useful for generating competing hypotheses, identifying gaps, clustering evidence and summarizing supporting and contradicting evidence.

Human analysts should retain responsibility for high-impact conclusions.

### Reporting
A strong report separates observed facts, sourced claims, analyst inference, model-generated suggestions and unresolved uncertainty.

### Monitoring and dissemination
AI can assist recurring collection, change detection, prioritization and alerting.

### OSINT on AI infrastructure
A distinct domain studies publicly observable AI systems and ecosystems, including:
- public model/service metadata;
- documented endpoints;
- model registries;
- public vector/database technology footprints;
- package and dependency ecosystems;
- model cards and safety documentation;
- AI supply-chain relationships.

This category is for defensive, research and intelligence purposes. Collection must remain lawful and proportionate.


## Paradigm layer

OSINTAI also classifies systems by the **paradigm they represent**, because two tools can perform similar tasks while embodying very different operational assumptions.

| Paradigm | Core idea |
|---|---|
| **Autonomous & Agentic OSINT** | models plan, select bounded tools and iterate over evidence |
| **Local-First & Zero-API OSINT** | sensitive inference and data remain under analyst control while external dependencies are minimized |
| **Emerging-Source Intelligence** | new value is extracted from overlooked source classes such as prompt leaks, AI-system metadata or torrent metadata |
| **Continuous Multimodal Intelligence** | systems reason across live or changing video, imagery, speech, geospatial and text streams |
| **Decentralized Intelligence Networks** | intelligence exchange or validation is distributed through mesh, peer-to-peer or decentralized infrastructure |

These paradigms are **not maturity rankings**. A decentralized or autonomous system is not automatically superior to a bounded analyst-copilot workflow.

See [paradigms.md](paradigms.md) and the machine-readable `catalog/paradigms.json`.

## Architecture classes

| Class | Description |
|---|---|
| **Copilot** | analyst directs each meaningful step |
| **Tool-calling assistant** | model can invoke bounded tools |
| **Planner-agent** | model decomposes objectives and selects tools |
| **Multi-agent** | specialized agents coordinate tasks |
| **Swarm** | multiple agents collaborate or compete with decentralized coordination |
| **Pipeline** | deterministic workflow with AI inserted into selected stages |
| **RAG** | model retrieves from a curated evidence corpus |
| **Graph-RAG** | graph structure participates in retrieval and reasoning |
| **MCP tool fabric** | tools are exposed through Model Context Protocol |
| **Local-first** | inference and data remain primarily on analyst-controlled infrastructure |

## Autonomy scale

- **A0 — manual:** AI is not in the investigative loop.
- **A1 — assistive:** summarization, extraction or drafting only.
- **A2 — bounded tool use:** AI calls pre-approved tools.
- **A3 — adaptive planning:** AI chooses sequences inside defined scope.
- **A4 — multi-agent orchestration:** agents coordinate with human checkpoints.
- **A5 — unattended autonomy:** system can continue without review.

OSINTAI does not assume higher autonomy is better. In sensitive investigations, A1–A3 may be operationally superior because provenance, privacy and analyst control are easier to maintain.

## Evidence maturity

| Level | Behavior |
|---|---|
| **E0** | output has no source traceability |
| **E1** | links or citations are present |
| **E2** | claims map to captured source artifacts |
| **E3** | transformations and provenance are recorded |
| **E4** | claims are reproducible and machine-auditable |
| **E5** | evidence integrity, analyst decisions and model/tool actions are fully auditable |

## Deployment sensitivity

- public cloud;
- private cloud;
- self-hosted;
- local workstation;
- isolated environment.

Sensitive cases should prefer architectures that minimize unnecessary disclosure to third-party models and services.

## Model modalities

Catalog entries may support text, image, video, audio, document, geospatial, code/infrastructure and graph modalities.

## Security dimensions

Every agentic platform should be considered against:
- prompt injection;
- agent goal hijacking;
- tool misuse;
- excessive permissions;
- secret leakage;
- poisoned MCP/tool dependencies;
- malicious retrieved content;
- insecure output execution;
- memory poisoning;
- audit gaps.

See mcp-security.md and evaluation-framework.md.
