# Implementation Plan: Source-to-Specification Development Loop

**Branch**: `001-shopizer-analysis` (feature identifier only; no Git branch) | **Date**: 2026-10-07 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification for a local read-only Shopizer analyzer and downloadable evidence-linked artifacts.

## Summary

This feature defines SpecLoop-AI's full Shopizer source-to-specification loop. The current MVP discovers Maven metadata, Java API mappings, source/test evidence, generates eight traceable draft artifacts, and previews/downloads them in Streamlit. The roadmap adds reviewed specification baselines, optional GenAI drafting, change implementation against approved requirements, actual test results, and revision drift. Source analysis remains read-only; external model calls and code changes require explicit approval.

## Technical Context

**Language/Version**: Python 3.11+ (syntax and tooling baseline)

**Primary Dependencies**: Streamlit; Python standard library for XML, Git revision metadata, archive packaging, and unit tests. No model provider is configured.

**Storage**: In-memory analysis result; Markdown downloads and ZIP archive; no persistent database

**Testing**: `python -m unittest discover -s demo-app/tests`; Streamlit `AppTest` smoke test

**Target Platform**: Local development on Windows, macOS, and Linux with Python 3.11+

**Project Type**: Single-project local web application

**Performance Goals**: Complete analysis of the supplied Shopizer checkout in a single interactive run; no latency SLA is asserted until measured on a pinned machine/revision

**Constraints**: Current analyzer is read-only; no network/model calls or Shopizer test execution; report revision unavailability; source parsing is best-effort; no real customer data; no silent persistence. Future code/test execution requires explicit approval and isolation.

**Scale/Scope**: One local Maven repository per analysis run; three capabilities (order, cart, customer); eight Markdown artifacts

## Constitution Check

*Gate: checked before research; re-check after design.*

- Evidence grounding: PASS. Route claims include source path and line; test files have explicit execution status.
- Read-only analysis: PASS. Scanner reads POM/Java files and queries Git revision only; it does not write to the selected repository or execute Shopizer code.
- Complete traceability: PASS. Each source-derived route requirement gets a traceability row and proposed test ID.
- Privacy/provider boundary: PASS. Pipeline is deterministic and makes no external requests; synthetic fixtures contain no customer values.
- Honest verification/human approval: PASS. Test suggestions and inferred story seeds are labeled as unexecuted/unapproved drafts.

## Design Decisions

See [research.md](research.md). Use deterministic route discovery and structured XML parsing for the current Shopizer case. Keep outputs in memory and preview/download them. Model-backed drafting is an opt-in future phase after provider/data approval; it cannot replace evidence validation. Approved artifact persistence, implementation generation, test execution, and drift comparison require separate design and safety review.

## Delivery Phases

- **MVP (implemented)**: local source discovery, draft BRD/spec/test/traceability outputs, Streamlit review/download, and fixture tests.
- **Next**: reviewer-owned approval/versioning and an opt-in provider adapter after data-owner approval.
- **Future**: map enhancement requests to approved requirements, implement/test changes in an isolated work area, and compare later source revisions for drift.

## Project Structure

### Documentation (this feature)

```text
specs/001-shopizer-analysis/
├── spec.md
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── local-analysis.md
├── checklists/
│   └── requirements.md
└── tasks.md
```

### Source Code (repository root)

```text
demo-app/
├── streamlit_app.py
├── agents/
│   ├── code_discovery_agent.py
│   ├── business_understanding_agent.py
│   ├── brd_agent.py
│   ├── sdd_agent.py
│   ├── test_agent.py
│   ├── traceability_agent.py
│   ├── modernization_agent.py
│   └── pipeline.py
├── sample-data/
└── tests/
    └── test_pipeline.py
```

## Complexity Tracking

No constitution violations identified. The current MVP needs no database or model service. Future provider, persistence, or code-execution components require separate approval and safety design.
