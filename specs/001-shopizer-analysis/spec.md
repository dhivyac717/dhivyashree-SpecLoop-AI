# Feature Specification: Source-to-Specification Development Loop

**Feature Branch**: `001-shopizer-analysis` (Spec Kit feature identifier; no Git branch was created)

**Created**: 2026-10-07

**Status**: Draft

**Input**: Hackathon idea: recover business and technical knowledge from Shopizer source code, produce reviewable requirements/specifications/tests, then use approved specifications to guide future changes.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Analyze a Shopizer Repository (Priority: P1)

As a developer or analyst, I want to point the tool at a Shopizer repository and inspect discovered modules, API routes, relevant tests, and source locations so I can understand the evidence behind a capability analysis.

**Why this priority**: Source discovery is the evidence base for every later artifact.

**Independent Test**: Analyze a synthetic Maven fixture and the current Shopizer checkout; verify metadata, routes, test status, and source references are displayed.

**Acceptance Scenarios**:

1. **Given** a readable Shopizer root with a Maven descriptor, **When** I start analysis, **Then** I see discovered modules, capability routes, relevant test files, and the available source revision.
2. **Given** a repository without Git metadata, **When** I start analysis, **Then** discovery continues and clearly reports the revision as unavailable.
3. **Given** a path without a valid root Maven descriptor, **When** I start analysis, **Then** I receive an actionable error and no report is shown as successful.

### User Story 2 - Review and Approve Specifications (Priority: P1)

As a product owner or analyst, I want the discovered evidence organized into a BRD, functional and technical specifications, user stories, test scenarios, and traceability so I can review the recovered system knowledge and approve a baseline for future work.

**Why this priority**: Recovered knowledge only guides future development when it is organized, traceable, reviewable, and explicitly approved.

**Independent Test**: Run analysis on the fixture, verify all eight Markdown outputs are previewable/downloadable, and confirm unapproved requirements remain labeled as drafts.

**Acceptance Scenarios**:

1. **Given** a successful analysis, **When** I open each artifact view, **Then** I can inspect its content and source/test status.
2. **Given** a successful analysis, **When** I download the artifact bundle, **Then** it contains source analysis, BRD, functional/technical specifications, stories, tests, traceability, and modernization observations.
3. **Given** a requirement observation, **When** I inspect traceability, **Then** its source reference and proposed test link are visible.

### User Story 3 - Distinguish Evidence from Decisions (Priority: P1)

As a reviewer, I want source observations, unapproved interpretations, proposed tests, and unexecuted checks labeled distinctly so generated drafts cannot be mistaken for approved policy or passing verification.

**Why this priority**: Order, cart, and customer flows affect commerce and personal data; false confidence is a material risk.

**Independent Test**: Use fixture tests with an ignored test and confirm the test inventory reports it as ignored, suggestions as unexecuted, and requirements as source-derived drafts.

**Acceptance Scenarios**:

1. **Given** a test file with an ignore/disable annotation, **When** it appears in the report, **Then** it is marked ignored/disabled.
2. **Given** the analyzer generates candidate checks, **When** they appear in the report, **Then** they are labeled proposed and not executed.
3. **Given** the scanner finds an API mapping, **When** it drafts a requirement, **Then** the wording states the source observation and includes a source location instead of claiming stakeholder approval.

### User Story 4 - Develop Changes Against an Approved Specification (Priority: P2)

As a development team, I want a future change request linked to approved requirements and acceptance tests so implementation and verification stay consistent with the agreed behavior.

**Why this priority**: This closes the intended loop from recovered specifications through code and tests; it follows the trustworthy evidence and approval foundation.

**Independent Test**: Given a synthetic approved feature spec, verify that change tasks and candidate tests cite its requirement IDs and that test status distinguishes executed from not-run.

**Acceptance Scenarios**:

1. **Given** an approved specification and a new change request, **When** work is planned, **Then** affected requirement IDs and acceptance criteria are identified.
2. **Given** candidate implementation and tests, **When** validation is requested, **Then** recorded results map to acceptance criteria and unrun tests are not marked passed.
3. **Given** code conflicts with an approved requirement, **When** the change is reviewed, **Then** the conflict is surfaced for explicit human resolution.

### User Story 5 - Detect Specification Drift (Priority: P3)

As a maintainer, I want later source revisions compared with approved evidence so stale specifications and untraced behavior changes become visible.

**Why this priority**: Drift detection keeps specifications useful after the initial analysis and change cycle.

**Independent Test**: Change a route in a synthetic repository revision and verify that the affected source link and specification are reported for review.

**Acceptance Scenarios**:

1. **Given** a new source revision, **When** it is compared with an approved analysis, **Then** changed or missing source references are listed.
2. **Given** an approved requirement without current implementation or test evidence, **When** drift analysis runs, **Then** it is reported as uncovered.

### Edge Cases

- The root Maven descriptor is missing or malformed.
- A declared module or source/test directory is missing.
- Java source contains unsupported or malformed text; scanning must continue where possible and report no false route claim.
- Git is unavailable or the selected directory has no Git revision.
- No relevant API routes or tests are found.
- A relevant test is disabled, ignored, or has no test annotations.
- The source repository is large; the interface must remain usable and must not write into it.
- A source file contains sensitive-looking values; no source contents are uploaded to an external service.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST accept a user-selected local repository path and validate that its root Maven descriptor can be read.
- **FR-002**: The system MUST report project metadata and Maven modules declared by the root descriptor.
- **FR-003**: The system MUST discover relevant order, cart, and customer Java source/test files and supported REST route mappings with source file and line references.
- **FR-004**: The system MUST report a source revision when available and continue with an explicit unavailable status when it is not.
- **FR-005**: The system MUST distinguish active-looking, ignored/disabled, and proposed test information, and MUST state that the analyzer did not execute tests.
- **FR-006**: The system MUST produce eight reviewable Markdown artifacts: source analysis, BRD, SDD, user-story seeds, functional requirements, test cases, traceability matrix, and modernization assessment.
- **FR-007**: Each source-derived requirement MUST include at least one source reference, and every generated requirement MUST have a traceability row.
- **FR-008**: The system MUST label generated requirements as source-derived drafts and user stories as inferred seeds requiring review.
- **FR-009**: The system MUST allow each artifact and the complete artifact bundle to be downloaded without silently writing into the analyzed repository.
- **FR-010**: The system MUST handle invalid input paths and unreadable/malformed project descriptors with a clear error state.
- **FR-011**: The system MUST NOT make external model/provider calls or claim to execute Shopizer tests.
- **FR-012**: The system MUST NOT include real customer data, credentials, tokens, payment data, or secrets in generated sample data.
- **FR-013**: The system MUST support explicit human approval of a specification before it becomes a baseline for future feature work.
- **FR-014**: Future code/test generation MUST be traceable to approved requirement identifiers and acceptance criteria and MUST require explicit user action.
- **FR-015**: The system MUST surface conflicts between implementation, tests, and approved specifications rather than silently rewriting the baseline.
- **FR-016**: The system MUST be able to compare a later source revision with approved evidence and report affected/stale traceability links.
- **FR-017**: External GenAI processing MUST remain disabled unless a provider and source-data handling policy have been explicitly approved and disclosed.

### Key Entities

- **Analysis Run**: One read-only scan of a repository path and revision, with project metadata and capability discoveries.
- **Evidence Reference**: A source file, line, route, or test record supporting a report claim.
- **Requirement Observation**: A stable identifier, capability, source-derived statement, evidence references, and draft status.
- **Test Record**: A discovered test file and its annotation/ignore status; this does not represent test execution.
- **Artifact Bundle**: The eight Markdown outputs produced for one analysis run, available for preview/download.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: On the supplied Shopizer checkout, one analysis run discovers all five root Maven modules and the authenticated and anonymous checkout routes.
- **SC-002**: Every generated requirement observation has at least one source reference and exactly one traceability row.
- **SC-003**: All eight Markdown artifacts are available after a successful analysis and are included in the downloaded archive.
- **SC-004**: An ignored order integration test is reported as ignored/disabled, and no report claims Shopizer tests were executed.
- **SC-005**: Invalid repository input produces an actionable error without an unhandled application exception.
- **SC-006**: Analysis leaves the selected source repository unchanged and makes no external provider call.
- **SC-007**: Every feature task and candidate test generated from an approved specification identifies at least one requirement or acceptance-criterion ID.
- **SC-008**: Every recorded pass/fail/skipped test state is backed by a test execution result; all other test suggestions remain not-run.
- **SC-009**: A change to a referenced route in a pinned test repository revision produces a traceability drift item linked to the affected artifact.

## Assumptions

- The initial supported target is a local Shopizer Maven repository with a readable root `pom.xml` and Java source files.
- The current release is deterministic and local; model-backed generation, persistent approval/versioning, implementation generation, test execution, and drift comparison are future phases.
- Repository route and test discovery is best-effort static analysis; it does not establish full runtime behavior, authorization correctness, or test pass status.
- The current Shopizer checkout is a validation example, not the only supported input.
- Generated BRD/story language is a draft derived from code; stakeholders must approve business intent and acceptance policy.
- Hackathon benefits such as faster onboarding, productivity, quality improvement, and modernization acceleration are hypotheses until measured against a baseline.
