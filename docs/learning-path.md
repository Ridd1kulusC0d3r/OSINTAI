# OSINT + AI Learning Path

A practical progression from AI-assisted analysis to defensible agentic OSINT.

## Stage 1 — Evidence before models
Learn:
- source evaluation;
- provenance;
- verification;
- collection notes;
- confidence and uncertainty.

Deliverable: manually produce one source-grounded OSINT report where every material claim maps to evidence.

## Stage 2 — AI as analyst copilot
Use AI for:
- summarization;
- entity extraction;
- translation;
- question generation;
- report drafting.

Deliverable: compare AI-assisted output with a manual baseline and document every unsupported claim.

## Stage 3 — Retrieval and local models
Learn:
- RAG;
- embeddings;
- local inference;
- case isolation;
- evidence indexing.

Deliverable: build a local searchable evidence corpus and require source citations for answers.

## Stage 4 — Tool calling and MCP
Learn:
- tool schemas;
- MCP;
- secrets handling;
- allowlists;
- audit logs.

Deliverable: expose a small read-only OSINT toolset to an agent with explicit tool permissions.

## Stage 5 — Graph and entity intelligence
Learn:
- entity resolution;
- knowledge graphs;
- temporal relationships;
- evidence-backed edges;
- graph retrieval.

Deliverable: build a graph where every relationship can be traced to evidence or marked as inference.

## Stage 6 — Agentic investigation
Learn:
- planning;
- bounded autonomy;
- human gates;
- adversarial prompt injection;
- cost controls;
- rollback and replay.

Deliverable: run a benchmark case where an agent can plan and call tools but cannot silently expand scope.

## Stage 7 — Evaluation engineering
Learn:
- golden datasets;
- precision and recall;
- factuality;
- provenance scoring;
- adversarial test corpora;
- regression testing.

Deliverable: evaluate two OSINT AI workflows on the same test set without using subjective “looks better” scoring.

## Stage 8 — Research contribution
Contribute:
- verified catalog entries;
- benchmark cases;
- reproducible experiments;
- failure analyses;
- security tests;
- governance patterns.

The strongest contribution is often a documented failure mode, because the ecosystem currently has more demos than rigorous operational evidence.
