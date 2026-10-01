# Governance, Privacy and Evidence Integrity

This document is operational guidance, not legal advice.

## Core principles

### Purpose limitation
Define why the investigation exists before collection begins.

### Data minimization
Collect what is necessary for the intelligence requirement, not everything technically obtainable.

### Proportionality
The intrusiveness of collection and analysis should be proportionate to the investigative need.

### Provenance
Maintain traceability from report claims back to captured source material.

### Human accountability
AI can assist analysis, but responsibility for consequential conclusions remains human.

### Separation of fact and inference
Reports should distinguish:
- source statement;
- direct observation;
- analyst inference;
- model suggestion;
- unresolved uncertainty.

### Retention discipline
Case data should have a documented retention policy.

## Useful governance references

### OSINT Privacy Impact Framework (OPIF)
New America's framework is specifically focused on privacy risks in AI-integrated OSINT and emphasizes privacy baselines, process-flow impact assessment and risk mitigation.

### Berkeley Protocol
The Berkeley Protocol provides professional standards for identification, collection, preservation, verification and analysis of digital open-source information, especially for investigations with evidentiary consequences.

### NIST AI RMF
NIST's AI Risk Management Framework and Generative AI Profile are useful for structuring AI risk identification, measurement and governance.

### OWASP Agentic guidance
Agentic systems introduce specific risks around goals, tools, privileges, supply chains and execution.

### EU AI Act
For systems and deployments that fall within its scope, the EU AI Act introduces requirements that may include transparency, risk management, logging, documentation, human oversight, robustness and cybersecurity depending on system classification and role.

## Privacy review checklist

Before using AI on case data:

- Is the data required for the stated purpose?
- Can identifiers be redacted before model use?
- Will data leave the analyst-controlled environment?
- Is the model provider allowed to retain inputs?
- Are prompts and outputs stored?
- Are third-party subprocessors involved?
- Can local inference reduce exposure?
- Is retention documented?
- Is the output consequential for an identifiable person?
- Is human review mandatory before dissemination?

## Evidence integrity checklist

- raw source captured where appropriate;
- timestamp recorded;
- original URL or identifier recorded;
- hash recorded for preserved artifacts where appropriate;
- transformations logged;
- model and tool versions recorded;
- claims linked to evidence;
- contradictions preserved;
- analyst decisions recorded.

## Publication checklist

Before publishing an intelligence product:
- verify source support for each material claim;
- remove unnecessary personal data;
- separate fact from inference;
- disclose significant uncertainty;
- record review and approval;
- preserve the source package needed for later audit.

## Principle

**Public availability does not eliminate privacy, proportionality or accuracy obligations.**
