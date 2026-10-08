---
description: "User-story task plan for the Shopizer source-to-specification loop"
---

# Tasks: Source-to-Specification Development Loop

**Input**: Design documents in `specs/001-shopizer-analysis/`

**Prerequisites**: `spec.md`, `plan.md`, `research.md`, `data-model.md`, and `contracts/local-analysis.md`.

**Organization**: Tasks are grouped by user story. The deterministic analysis MVP already exists; tasks below cover remaining robustness, human approval, and roadmap capabilities.

## Phase 1: Setup

**Purpose**: Establish reproducible, privacy-safe development and demo inputs.

- [ ] T001 Record the tested Shopizer revision and supported source layout in `specs/001-shopizer-analysis/quickstart.md`.
- [ ] T002 Add synthetic fixtures for normal, malformed, and unsupported Maven/Java inputs in `demo-app/tests/fixtures/`.
- [ ] T003 Pin supported Python and Streamlit dependency bounds in `demo-app/requirements.txt`.

## Phase 2: Foundational

**Purpose**: Strengthen evidence records and gates used by every story.

- [ ] T004 [P] Add typed analysis/evidence/result models in `demo-app/agents/models.py` and validate required source/status fields.
- [ ] T005 Add source revision and analyzer-version metadata to every artifact in `demo-app/agents/pipeline.py`.
- [ ] T006 Add output validation that rejects requirements without resolvable evidence or trace rows in `demo-app/agents/traceability_agent.py`.
- [ ] T007 Add safe error handling and path/read-only checks around repository discovery in `demo-app/agents/code_discovery_agent.py`.
- [ ] T008 Add unit tests for malformed POM, missing modules, no Git metadata, unsupported Java mappings, and no matching tests in `demo-app/tests/test_pipeline.py`.

## Phase 3: User Story 1 - Recover Application Knowledge (Priority: P1)

**Goal**: Reliably discover Shopizer evidence and generate a source-linked business-requirement draft.

**Independent Test**: Analyze the pinned Shopizer checkout and a fixture; assert all selected capability claims resolve to source locations and absent evidence is not invented.

- [ ] T009 [US1] Expand supported route extraction and controller base-path handling in `demo-app/agents/code_discovery_agent.py`.
- [ ] T010 [P] Add fixture coverage for composed/multiline route mappings and source line references in `demo-app/tests/test_pipeline.py`.
- [ ] T011 [US1] Add capability summaries and confidence/status provenance to `demo-app/agents/business_understanding_agent.py`.
- [ ] T012 [US1] Generate separate business requirements and source-observation records in `demo-app/agents/brd_agent.py`.
- [ ] T013 [US1] Add BRD acceptance review notes and source links to `demo-app/agents/pipeline.py`.
- [ ] T014 [US1] Verify source-derived BRD coverage against the three Shopizer case studies in `demo-app/tests/test_pipeline.py`.

## Phase 4: User Story 2 - Review and Approve Specifications (Priority: P1)

**Goal**: Produce functional/technical specs, stories, tests, and traceability that a human can review and approve as a baseline.

**Independent Test**: Generate artifacts from a fixture, reject one draft claim, approve the remaining baseline, and verify the approved revision is distinct from drafts.

- [ ] T015 [US2] Separate functional requirements from API observations and keep stable identifiers in `demo-app/agents/brd_agent.py`.
- [ ] T016 [US2] Generate evidence-linked technical specification sections from repository structure in `demo-app/agents/sdd_agent.py`.
- [ ] T017 [P] Add reviewer accept/reject/edit state for generated artifacts in `demo-app/streamlit_app.py`.
- [ ] T018 [US2] Add versioned approved-baseline records with source revision and reviewer state in `demo-app/agents/approval_store.py`.
- [ ] T019 [US2] Add an artifact-history data model and persistence policy documentation in `specs/001-shopizer-analysis/data-model.md`.
- [ ] T020 [US2] Add UI and unit tests for draft, approved, rejected, and superseded artifact states in `demo-app/tests/test_pipeline.py`.

## Phase 5: User Story 3 - Distinguish Evidence from Decisions (Priority: P1)

**Goal**: Prevent inferred, proposed, and unexecuted items from appearing as facts or successful verification.

**Independent Test**: Feed an ignored test and an unsupported route claim through the pipeline; verify the ignored state is preserved and unsupported evidence is rejected.

- [ ] T021 [US3] Define explicit observed/inferred/proposed/approved status enums in `demo-app/agents/models.py`.
- [ ] T022 [US3] Preserve test discovery, ignore annotations, and actual execution as separate states in `demo-app/agents/test_agent.py`.
- [ ] T023 [P] Add report rendering for confidence, evidence, approval, and execution state in `demo-app/agents/pipeline.py`.
- [ ] T024 [US3] Add UI warnings and reviewer filters for unapproved/unsupported claims in `demo-app/streamlit_app.py`.
- [ ] T025 [US3] Add regression tests proving no proposed or unexecuted test is reported as passing in `demo-app/tests/test_pipeline.py`.

## Phase 6: User Story 4 - Develop Changes Against an Approved Specification (Priority: P2)

**Goal**: Start a future enhancement from approved requirement IDs and verify candidate changes against acceptance criteria.

**Independent Test**: Given a synthetic approved requirement, generate a candidate change plan in an isolated workspace and report test results only after an explicitly authorized command runs.

- [ ] T026 [US4] Define a change proposal model linking request, approved requirement IDs, and acceptance criteria in `demo-app/agents/models.py`.
- [ ] T027 [US4] Design and document an isolated candidate-worktree lifecycle and rollback contract in `specs/001-shopizer-analysis/contracts/local-analysis.md`.
- [ ] T028 [US4] Add user confirmation and an allowlisted test-command runner with captured result states in `demo-app/agents/change_workflow.py`.
- [ ] T029 [US4] Add authorization, isolation, rollback, and test-result tests in `demo-app/tests/test_change_workflow.py`.
- [ ] T030 [US4] Add a change-planning and validation view linked to approved requirements in `demo-app/streamlit_app.py`.

## Phase 7: User Story 5 - Detect Specification Drift (Priority: P3)

**Goal**: Compare a later source revision with an approved baseline and surface changed or missing evidence.

**Independent Test**: Change a route in a second fixture revision and verify linked baseline artifacts receive a drift finding requiring review.

- [ ] T031 [US5] Define pinned baseline and drift-finding records in `demo-app/agents/models.py`.
- [ ] T032 [US5] Implement source-reference normalization and revision comparison in `demo-app/agents/drift_agent.py`.
- [ ] T033 [US5] Add changed, removed, and unchanged evidence fixture tests in `demo-app/tests/test_drift_agent.py`.
- [ ] T034 [US5] Add drift review and resolution status to `demo-app/streamlit_app.py`.
- [ ] T035 [US5] Document baseline retention, comparison limits, and reviewer disposition in `specs/001-shopizer-analysis/data-model.md`.

## Phase 8: GenAI-Assisted Drafting (Future, Approval-Gated)

**Goal**: Optionally use an approved model to improve drafts without replacing evidence or review.

**Independent Test**: With a mock provider, verify the request includes only approved evidence, each generated claim cites evidence, and disabling the provider makes no network call.

- [ ] T036 [US2] Define provider configuration, source-data notice, retention, and opt-in requirements in `specs/001-shopizer-analysis/research.md`.
- [ ] T037 [P] Implement a provider-neutral draft interface with a deterministic fallback in `demo-app/agents/llm_provider.py`.
- [ ] T038 [US2] Add mock-provider tests for evidence grounding, disabled mode, and safe failures in `demo-app/tests/test_llm_provider.py`.
- [ ] T039 [US2] Add explicit user consent and provider disclosure controls in `demo-app/streamlit_app.py`.

## Phase 9: Polish and Cross-Cutting Concerns

- [ ] T040 [P] Update hackathon architecture diagrams to distinguish implemented and roadmap components in `diagrams/`.
- [ ] T041 Update demo/README instructions and supported limitations in `README.md`.
- [ ] T042 Add a reproducible benchmark protocol for source-reference accuracy and analyst-time measurement in `metrics/business-impact.md`.
- [ ] T043 Run unit and Streamlit AppTest suites and record actual outcomes in `specs/001-shopizer-analysis/quickstart.md`.
- [ ] T044 Review public-release contents for secrets, personal data, license clarity, and third-party attribution in `NOTICE.md` and `LICENSE.md`.

## Dependencies and Execution Order

- Foundation (T004-T008) precedes stories that add models, persistence, or execution.
- US1, US2, and US3 build on the current MVP and can be advanced independently after foundational provenance work.
- US4 depends on approved-baseline work from US2 and explicit execution safety from US3.
- US5 depends on pinned revision and approved-baseline data from US1/US2.
- GenAI work is blocked on data-owner/provider approval; it is not required for the deterministic MVP.

## Parallel Opportunities

- T004 and T010 can proceed independently after repository fixtures are agreed.
- T015 and T017 touch separate agent/UI files after the artifact contract is agreed.
- T021 and T023 are parallel after the shared status model is approved.
- T031 and T032 should be designed together; T033 can be developed independently once the contract is fixed.

## MVP Scope

The already-working MVP covers the current source-discovery, artifact-preview/download, and traceability path. For the next publishable increment, prioritize T004-T014 and T021-T025: evidence robustness, business/spec distinction, source-linked BRD quality, and truthful review/test status. GenAI, code execution, persistence, and drift are explicitly later phases.