# Reference Architecture for AI-Augmented OSINT

The reference architecture is intentionally **evidence-first**. AI is an analysis and orchestration layer, not the system of record.

## Design goals

1. preserve source provenance;
2. make every transformation traceable;
3. isolate model-generated claims from observed evidence;
4. support local and cloud models;
5. allow deterministic replay where possible;
6. enforce least privilege for tools;
7. insert human gates before high-impact actions;
8. make evaluation measurable.

## Logical architecture

~~~mermaid
flowchart TD
    R[Requirements / Case Scope] --> P[Planner]
    P --> TB[Tool Broker]
    TB --> C1[Web / API Collectors]
    TB --> C2[MCP Servers]
    TB --> C3[Local Tools]
    C1 --> CAP[Capture & Preservation]
    C2 --> CAP
    C3 --> CAP

    CAP --> EV[(Evidence Store)]
    CAP --> N[Normalize / OCR / Transcribe]
    N --> ER[Entity Resolution]
    ER --> KG[(Knowledge Graph)]
    N --> IX[(Search / Vector Index)]

    KG --> AG[Agent / LLM Sandbox]
    IX --> AG
    EV --> AG

    AG --> HY[Hypotheses / Findings]
    HY --> V[Verification Engine]
    V --> HR[Human Review]
    HR --> REP[Report / Dissemination]

    EV --> V
    LOG[(Audit Log)] --- P
    LOG --- TB
    LOG --- AG
    LOG --- HR
~~~

## Components

### Case scope
Store purpose, target classes, allowed source classes, time window, retention policy, analyst owner, legal/privacy notes and stop conditions.

### Planner
The planner converts requirements into tasks. It should never silently expand scope.

Recommended controls:
- maximum task depth;
- maximum tool calls;
- allowlisted tool families;
- explicit approval for new target entities.

### Tool broker
The tool broker is the security boundary between the agent and external capabilities.

It should enforce:
- least privilege;
- input validation;
- per-tool rate limits;
- secrets isolation;
- network boundaries;
- action logging;
- deterministic tool identifiers and versions.

### Capture and preservation
Store raw material before AI transforms it when appropriate.

Useful metadata:
- source URL or identifier;
- retrieval timestamp;
- MIME/type;
- collector/tool version;
- content hash;
- HTTP metadata when relevant;
- screenshot/archive reference;
- case identifier.

### Evidence store
The evidence store is append-oriented. Derived artifacts should point back to originals.

### Normalization
Possible tasks include OCR, transcription, language normalization, metadata parsing, HTML cleanup, document chunking and entity extraction.

Derived text must retain a pointer to its source artifact and transformation method.

### Entity resolution
Never store “same person” as a boolean without context. Prefer candidate match, score, features used, evidence, analyst decision and timestamp.

### Search and knowledge graph
Use the graph for explicit relationships and search/vector indexes for retrieval. Do not let embedding similarity masquerade as a proven relationship.

### Agent/LLM sandbox
The model should receive only the data required for the task.

Controls:
- retrieval filtering;
- prompt-injection defenses;
- tool allowlists;
- bounded context;
- no direct secret exposure;
- no direct write access to evidence originals.

### Verification engine
Verification should test source support, contradictions, freshness, temporal consistency, entity consistency, citation coverage and unsupported model claims.

### Human review gates
Recommended mandatory gates:
- scope expansion;
- sensitive identity resolution;
- high-impact accusations or conclusions;
- publication;
- destructive or irreversible actions;
- retention exceptions.

## Evidence object

~~~json
{
  "evidence_id": "ev_001",
  "case_id": "case_001",
  "source": {
    "uri": "https://example.org/item",
    "retrieved_at": "2026-10-01T18:00:00Z"
  },
  "capture": {
    "tool": "collector-name",
    "tool_version": "1.2.3",
    "sha256": "..."
  },
  "transformations": [
    {
      "type": "ocr",
      "tool": "model-or-engine",
      "version": "..."
    }
  ],
  "classification": "public",
  "analyst_notes": []
}
~~~

## Claim object

~~~json
{
  "claim_id": "cl_001",
  "text": "Example claim",
  "type": "observation",
  "evidence_ids": ["ev_001"],
  "generated_by": "analyst-or-model",
  "confidence": 0.82,
  "review_status": "pending"
}
~~~

## Architecture principle

**Models reason over evidence. They do not replace the evidence layer.**
