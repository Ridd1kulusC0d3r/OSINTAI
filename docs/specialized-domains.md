# Specialized OSINT + AI Domains

AI-assisted OSINT is splitting into specialized domains. Treating all of them as one generic 'AI tool' category hides the actual investigative tradeoffs.

## Dark-web research

**Robin** is included as a verified AI-assisted dark-web OSINT research platform. OSINTAI catalogs its architecture, model support, MCP integration and reporting role, but intentionally does not reproduce operational access instructions.

Key evaluation questions:
- source legality and institutional policy;
- analyst safety and isolation;
- provenance of retrieved material;
- separation between indexed claims and verified facts;
- third-party model exposure of sensitive queries.

## SOCMINT

**OWASP Social OSINT Agent** represents the agentic SOCMINT category: multi-platform public-data collection, text/vision analysis, relationship discovery and structured reporting.

Key evaluation questions:
- identity resolution false positives;
- rate limits and platform terms;
- prompt injection hidden in user-generated content;
- image-analysis provenance;
- privacy and proportionality.

## GEOINT and tactical intelligence

**WorldView** combines live public feeds, a CesiumJS globe, local inference, LangGraph, Qdrant and Neo4j.

Key evaluation questions:
- temporal freshness;
- feed reliability;
- geospatial uncertainty;
- duplicated or conflicting event sources;
- model inference versus sensor/feed observation.

## Search-based OSINT

**Banshee-AI** represents AI-assisted search-query generation and repeatable discovery workflows.

Key evaluation questions:
- query quality versus noise;
- scope enforcement;
- search-engine bias;
- archival reproducibility;
- whether an apparent finding is still current.

## Local-first crawling

**OSINTai** combines asynchronous crawling, local Ollama analysis, evidence-labelled findings, correlations, timelines and graph-oriented exports.

Key evaluation questions:
- crawler scope controls;
- redirect handling;
- evidence preservation;
- deterministic versus model-derived findings;
- correlation false positives.

## Military OSINT

**Theosight** is cataloged as a commercial, sovereign-deployment-oriented military OSINT platform with per-field provenance and structured reporting.

Key evaluation questions:
- source provenance;
- doctrine/schema transparency;
- offline deployment controls;
- model traceability;
- human review for consequential intelligence judgments.