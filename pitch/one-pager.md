# SpecLoop-AI / Shopizer One-Pager

Status: draft for discussion; not an approved product or benefits claim.

## Challenge

Understand and specify Shopizer order, cart, and customer flows across a Java multi-module codebase without losing links to implementation and test evidence.

## Approach

The current deterministic prototype discovers source/API/service/model/test evidence, drafts capability artifacts, and keeps findings reviewable. The full vision adds GenAI-assisted BRD/spec drafting, human approval, spec-linked change implementation and testing, and drift insights.

## Demonstration

The current Streamlit app analyzes a local Shopizer checkout and generates downloadable evidence-linked artifacts for:

- Order checkout: authenticated and guest routes; order integration test is ignored/incomplete.
- Shopping cart: create/update/delete routes with selected integration coverage.
- Customer: registration/login happy path with additional security cases proposed.

The current pipeline is deterministic; GenAI provider connections, spec approval/versioning, code generation, actual Shopizer test execution, and historical drift comparison are roadmap items.

## Outcomes and Next Steps

Measure factual accuracy, review effort, traceability, and time against a manual baseline. First decisions: stakeholders, data policy, pinned Shopizer revision, and acceptance rubric. Do not claim ROI before measurement.