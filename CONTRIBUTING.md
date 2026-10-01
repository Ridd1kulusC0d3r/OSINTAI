# Contributing to OSINTAI

OSINTAI values **verifiable additions over large additions**.

## Resource submission requirements

For a tool, framework, MCP server or platform, provide:

- canonical project URL;
- canonical documentation or repository;
- concise description;
- OSINT function;
- AI or agent architecture;
- deployment model;
- local or cloud behavior;
- protocol support such as MCP;
- evidence for quantitative claims;
- last verification date.

## Verification rules

Do not submit marketing claims as facts.

Examples that require evidence:
- “100% local”;
- exact tool counts;
- “production ready”;
- “zero hallucination”;
- fixed investigation times;
- benchmark accuracy figures;
- exact numbers of integrations, models or providers.

If a claim cannot be verified, mark it as a candidate or omit it.

## Preferred sources

Priority order:
1. canonical project repository or documentation;
2. academic paper or DOI;
3. official standard or government source;
4. maintainer release notes;
5. reputable secondary analysis.

## Catalog changes

When editing catalog/tools.json:
- keep IDs stable;
- use ISO date format;
- do not silently change verification status;
- update last_reviewed;
- run the validator locally with Python.

## Research contributions

Strong contributions include:
- reproducible benchmark cases;
- negative results;
- agent failure analyses;
- prompt-injection tests;
- evidence and provenance patterns;
- privacy-preserving designs;
- local-first architectures;
- entity-resolution evaluations.

## Safety and ethics

Contributions should support lawful, ethical and authorized OSINT. Do not include material whose primary purpose is abuse, covert harassment, doxxing, credential theft or unauthorized access.

## Style

Write for both:
- analysts who need operational clarity;
- machines and LLMs that need structured metadata.

Prefer explicit fields and evidence over adjectives.
