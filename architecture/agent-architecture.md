# Shopizer Analysis Agent Architecture

Status: proposed responsibilities; Python files currently raise `NotImplementedError` and do not call models.

## Agent Responsibilities

- Code discovery: locate Shopizer modules, API classes, service interfaces, models, and relevant tests.
- Business understanding: summarize observed user-facing capabilities while flagging inferred stakeholder outcomes.
- BRD and SDD drafting: map source evidence into functional requirements and existing architecture descriptions.
- Test drafting: distinguish present tests from suggested missing cases; never report a suggestion as executed.
- Traceability: link requirement IDs to source references, design sections, and test IDs.
- Modernization: identify evidence-backed risks/opportunities with confidence and scope limitations.

## Inputs and Outputs

Input: repository root, pinned commit, allowed paths, and approved data/provider policy. Output: structured claims with source references and status, then Markdown artifacts. Customer credentials, tokens, or production data are prohibited inputs.

## Orchestration and Human Review

Proposed order: discovery -> evidence review -> capability drafts -> consistency/traceability checks -> human approval -> consolidated outputs. A reviewer must approve inferred requirements and modernization recommendations. No orchestration framework is selected.

## Failure Handling and Evaluation

Report missing/ambiguous source and unsupported claims as unresolved; do not fill gaps with invented behavior. Measure source-reference correctness, claim support, traceability completeness, and reviewer rejection rate on a manually reviewed Shopizer baseline. No evaluation results exist yet.