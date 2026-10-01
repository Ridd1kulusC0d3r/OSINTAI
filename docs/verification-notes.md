# Verification Notes

OSINTAI intentionally separates **resource discovery** from **resource verification**.

Date of foundation review: **2026-10-01**

## Verified in v0.1

The following canonical repositories were inspected directly:

- OpenOSINT/OpenOSINT
- taranis-ai/taranis-ai
- ALW1EZ/PANO
- AXRoux/argus-os
- badchars/osint-mcp-server
- cristianoaredes/mcp-dadosbr
- techno-neighbour/focal-harvest

## Claims not promoted to verified status

### AgentOSINT
A repository search returns multiple projects with this name. One discovered repository has only a minimal Node.js README and does not substantiate the commonly repeated claim of a Python/FastAPI five-agent platform.

**Decision:** exclude the detailed claim until a canonical repository, paper or project site is identified.

### Argus
The name is highly ambiguous across GitHub.

**Decision:** use the canonical name **AXRoux/argus-os** when referring to the agentic OSINT orchestration project. Do not use “Argus” without a URL in catalog contributions.

### VulnAI Pro
The claimed OSINT platform was not located confidently during the foundation review.

**Decision:** candidate or research queue only.

### MOSAIV
The research concept may be valid as an academic reference, but no canonical GitHub implementation was established during the initial repository search.

**Decision:** treat paper and code as separate verification targets.

### OSINTai
Multiple repositories or forks use the same name.

**Decision:** do not present a single implementation as canonical until ownership and provenance are established.

### AI OSINT / 7WaySecurity
Search surfaced a repository whose ownership and naming did not provide enough confidence to treat it as the canonical original.

**Decision:** hold for provenance verification.

## Verification policy

A tool can be marked **verified** when at least one canonical source is inspected and its key claims are directly supported.

For stronger claims such as:
- number of tools;
- supported providers;
- local-only behavior;
- benchmark accuracy;
- “zero cloud”;
- “production grade”;
- performance figures;

contributors should provide the exact source supporting the claim.

## Why this matters

OSINT practitioners routinely work in environments where confidence, provenance and attribution matter. A repository about AI should not lower that standard simply because the subject itself is moving quickly.
