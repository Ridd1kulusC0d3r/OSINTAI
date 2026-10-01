# OSINTAI Evaluation Framework

OSINT AI systems should be compared on evidence quality and operational behavior, not screenshots, model branding or the number of tools listed in a README.

## Why evaluation matters

Recent research on agentic and generative AI for OSINT highlights a major gap: capability demonstrations have advanced faster than standardized evaluation.

OSINTAI proposes a practical benchmark model that can later become an executable test suite.

## Evaluation dimensions

### Collection quality
Metrics:
- source coverage;
- duplicate rate;
- source diversity;
- freshness;
- collection failure rate.

### Extraction quality
Metrics:
- entity precision;
- entity recall;
- field accuracy;
- OCR/transcription error rate;
- language identification accuracy.

### Entity resolution
Metrics:
- true-match precision;
- false-merge rate;
- false-split rate;
- calibration of match score;
- analyst override frequency.

False merges should be treated as especially costly.

### Factuality
Measure:
- unsupported claim rate;
- contradiction rate;
- citation-to-claim support;
- fabricated-source rate;
- factual correction after verification.

### Provenance
Score whether:
- every claim maps to a source;
- source acquisition is timestamped;
- transformations are recorded;
- tool/model versions are logged;
- derived artifacts link to originals.

### Reproducibility
Can another analyst rerun the same workflow, identify tool versions, recover the same source set and distinguish changed-source effects from model variance?

### Reasoning discipline
Evaluate competing hypotheses, evidence for and against each hypothesis, uncertainty handling, explicit gap identification and avoidance of circular sourcing.

### Human-in-the-loop quality
Measure where approvals are required, whether analysts can reject or modify steps, whether the system explains why a tool was selected and whether scope expansion is visible.

### Security
Test against:
- prompt injection in retrieved content;
- malicious tool descriptions;
- MCP server poisoning;
- tool misuse;
- secret leakage;
- excessive agency;
- unsafe output execution.

### Privacy
Measure:
- unnecessary sensitive-data collection;
- third-party model exposure;
- retention controls;
- redaction effectiveness;
- case isolation.

### Performance
Metrics:
- latency;
- token usage;
- API cost;
- compute cost;
- tool-call count;
- retry rate.

Performance should never be reported without quality metrics.

## Proposed benchmark tiers

### Tier 1 — deterministic extraction
Fixed public documents with known expected entities and fields.

### Tier 2 — source-grounded research
Questions with a curated source corpus and known evidence set.

### Tier 3 — open-web verification
Time-bounded public scenarios where the system must gather, corroborate and cite.

### Tier 4 — adversarial retrieval
Corpus contains prompt injection, contradictory claims, low-quality copies, stale sources and manipulated metadata.

### Tier 5 — agentic workflow
System must plan and execute a bounded investigation using multiple tools while respecting scope and budget.

## Suggested scorecard

| Dimension | Weight |
|---|---:|
| Factuality | 20 |
| Provenance | 20 |
| Verification | 15 |
| Reproducibility | 10 |
| Entity resolution | 10 |
| Security | 10 |
| Privacy | 5 |
| Human control | 5 |
| Performance | 5 |

The weights are a starting point, not a universal ranking system.

## Golden rules

- Never use model self-confidence as the only confidence metric.
- Never count a citation unless it actually supports the claim.
- Keep source quality separate from source agreement.
- Measure hallucination at the **end-to-end workflow level**, not only in isolated question answering.
- Benchmark with both benign and adversarial inputs.
- Preserve raw outputs for regression testing.

## Future executable harness

Planned benchmark artifacts:
- synthetic cases;
- public reference cases;
- expected entity/relationship sets;
- adversarial source corpus;
- reproducible container environments;
- JSON result format;
- CI regression tests.
