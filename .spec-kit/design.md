# SpecLoop-AI Design for Shopizer

Status: deterministic local prototype implemented; GenAI, change implementation, and drift comparison remain proposed extensions.

## Context

Shopizer is a Java 11 Maven multi-module commerce application. This case study covers storefront order checkout, cart operations, and customer identity. The analyzer reads the repository and produces reviewable artifacts without modifying Shopizer.

## Current Flow

1. User selects a local repository root and starts analysis.
2. Scanner parses root Maven metadata, walks declared Java modules, extracts supported Spring route annotations, and inventories relevant test files/ignore annotations.
3. Deterministic agents create source-linked capability observations, requirement IDs, design inventory, proposed checks, traceability, and modernization caveats.
4. Streamlit previews the outputs and offers individual Markdown and ZIP downloads.
5. Spec Kit keeps the project feature spec, plan, and tasks in versioned project docs.

## Intended Full Loop

Source and tests -> evidence -> BRD -> functional/technical specifications -> human approval -> change request -> implementation and acceptance tests -> traceability/drift review. GenAI can assist drafting only after provider/data approval; it cannot replace evidence validation or human approval.

## Components

Current components are `demo-app/streamlit_app.py`, deterministic modules in `demo-app/agents/`, sample-data summaries, and `specs/`. No model provider, database, authentication service, or deployment service is connected.

## Alternatives and Trade-offs

Deterministic local analysis is the safe working baseline. Azure OpenAI, Semantic Kernel, and AI Foundry docs are optional future designs, not current deployment facts. A provider adapter may be added behind an explicit consent boundary when selected.

## Security and Data

Treat source as confidential. Use read-only access, no external transmission by default, synthetic examples, secret storage for future credentials, and redaction for output. Future implementation/test execution must use an isolated worktree or candidate branch with explicit user approval.