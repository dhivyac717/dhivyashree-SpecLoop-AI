# SpecLoop-AI Hackathon Requirements

Status: prototype requirements for the Shopizer case study. Business outcomes and AI-provider policy require stakeholder approval.

## Goal

Demonstrate a source-to-specification loop that recovers Shopizer behavior from source and tests, drafts reviewable business/technical artifacts, and makes those specifications a traceable starting point for future engineering work.

## Functional Requirements

- FR-01: Discover Maven modules, Java API mappings, relevant source files, test files, and source revision for Shopizer.
- FR-02: Cite source evidence for observed behavior and label inferred business intent separately.
- FR-03: Draft BRD, functional/technical specifications, user stories, candidate tests, traceability, and modernization observations.
- FR-04: Report ignored/disabled tests separately and never imply tests were run when they were only discovered.
- FR-05: Let reviewers preview and export artifacts while preserving draft/approval status.
- FR-06: Guide future changes from approved specifications to implementation tasks and acceptance tests.
- FR-07: Detect mismatches among approved specifications, source changes, and test results and route them for human decision.
- FR-08: Keep repository analysis read-only and external AI processing disabled unless explicitly configured and approved.
- FR-09: Keep customer PII, credentials, tokens, payment data, and secrets out of reports and samples.

## Quality Requirements

- Q-01: Every source-derived claim is traceable or explicitly marked as inference.
- Q-02: Analysis is reproducible against a recorded source revision.
- Q-03: Generated requirements/design remain drafts until a human reviewer approves them.
- Q-04: Actual test outcomes and proposed tests are represented as different states.
- Q-05: Unsupported analysis and missing evidence are surfaced, not fabricated.

## Prototype Boundary

Implemented: deterministic local discovery, artifact drafting, traceability generation, Streamlit preview/download, and Spec Kit feature workflow.

Not implemented: model-backed analysis, automatic code changes, actual Shopizer test execution, historical drift detection, shared persistence, production deployment, and measured productivity benefits.

## Open Decisions

- Select approved model provider and source-data retention policy before external processing.
- Define enterprise identity/access, artifact review roles, and deployment requirements.
- Define a measured productivity/quality baseline before making benefit claims.