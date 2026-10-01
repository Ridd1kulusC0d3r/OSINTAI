# Verification Notes

OSINTAI intentionally separates **resource discovery** from **resource verification**.

Latest ecosystem review: **2026-10-01**

## Verified platform set

Canonical repositories or official product pages inspected directly now include:

- OpenOSINT/OpenOSINT
- taranis-ai/taranis-ai
- ALW1EZ/PANO
- AXRoux/argus-os
- badchars/osint-mcp-server
- cristianoaredes/mcp-dadosbr
- techno-neighbour/focal-harvest
- gs-ai/OSINTai
- apurvsinghgautam/robin
- Hunter5Thompson/OSINT
- MustafaKemal0146/fetih
- ghostvyle/Unburden
- Vulnpire/Banshee-AI
- bm-github/owasp-social-osint-agent
- GreyNoise-Intelligence/greynoise-mcp-server
- Eos Applications / Theosight

## Resolved ambiguities

### OSINTai

The project name appears in multiple public repositories. The v0.2 catalog uses **gs-ai/OSINTai** as the primary record because its current repository directly identifies the project as OSINTai v4.2.0 and documents the local-first architecture.

A related **UberGuidoZ/osintai** repository contains closely related v4 material and still references gs-ai/OSINTai in setup instructions.

**Decision:** catalog gs-ai/OSINTai as the primary verified entry and document the related lineage instead of conflating them.

### AI OSINT / 7WaySecurity

The canonical organization repository **7WaySecurity/ai_osint** was located and inspected.

**Decision:** promote it into the verified curated-collections catalog as a defensive AI-infrastructure OSINT reference.

### MOSAIV

MOSAIV was verified as an **ICMR 2026 ACM conference paper** with DOI 10.1145/3805622.3812607.

**Decision:** catalog it as research, not as a standalone production platform unless a canonical implementation is separately established.

### Theosight

The official Eos Applications site currently presents Theosight as an active commercial military-OSINT product with structured intelligence, per-field provenance and sovereign deployment options.

**Decision:** remove the unsupported “launch planned for 2027” wording.

### OpenOSINT tool count

Current OpenOSINT documentation describes **20 modular tools**.

**Decision:** do not retain the older “18 tools” figure.

### Fine-tuned LLM + knowledge graph paper

The IEEE conference publication is from **2025** and was added to IEEE Xplore in 2026.

**Decision:** record publication year as 2025.

## Claims still not promoted to verified status

### AgentOSINT

Repository search returns multiple projects with this name. The repository initially discovered during review had only a minimal Node.js README and did not support the repeated claim of a Python/FastAPI five-agent platform completing investigations in 30–60 seconds.

**Decision:** keep the detailed claim out of the verified catalog until a canonical project or paper is identified.

### VulnAI Pro

The claimed platform was not located confidently from a canonical source.

**Decision:** candidate/research queue only.

### MCP World

A canonical source matching the specific “MCP World OSINT Tools” description was not established during this review.

**Decision:** do not promote it. The verified [soxoj/awesome-osint-mcp-servers](https://github.com/soxoj/awesome-osint-mcp-servers) collection covers the same discovery need with clear provenance.

### Remote-sensing + OSINT multimodal paper

Secondary indexing confirms the title and 2026 conference context, but a canonical proceedings record or DOI was not directly established during this pass.

**Decision:** retain as a research candidate with explicit status.

### IAI 10th edition claim

The verified IAI source located during review was the 9th edition held 25–30 March 2026. The claimed 10th edition dates of 19–23 October 2026 were not independently confirmed.

**Decision:** catalog the verified 9th edition and leave the 10th-edition claim out until a canonical announcement appears.

## Verification policy

A tool can be marked **verified** when at least one canonical source is inspected and its key claims are directly supported.

Stronger claims require exact support, especially:

- number of tools or skills;
- provider counts;
- local-only or zero-cloud behavior;
- benchmark accuracy;
- throughput or investigation-time claims;
- security statistics;
- “production grade” wording;
- future release dates.

Maintainer-reported numbers are recorded as such and should be rechecked as projects evolve.

## Why this matters

OSINT practitioners work in an evidence discipline. A repository about AI should raise the standard for provenance, not lower it because the ecosystem moves quickly.
