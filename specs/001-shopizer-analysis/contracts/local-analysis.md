# Local Analysis Contract

## Input

- One local directory selected by the user.
- The directory must contain a readable root `pom.xml` with Maven project metadata.
- Java source and test discovery is limited to module directories declared in the root POM.

## Output

- One structured analysis result containing project metadata and three capability inventories.
- Eight Markdown artifact strings: SourceAnalysis, BRD, SDD, UserStories, FunctionalRequirements, TestCases, TraceabilityMatrix, and ModernizationAssessment.
- Source-derived claims include a repository-relative file path and 1-based line where available.

## Safety and Status Semantics

- The selected repository is read-only; analysis does not execute source or tests.
- Missing Git metadata is reported as unavailable and does not fail valid source discovery.
- Invalid root path or missing/malformed root `pom.xml` returns a clear error and no successful result.
- Discovered test files are not considered executed. Ignored/disabled annotations are reported separately.
- Proposed tests, inferred stories, and requirement observations are drafts, never approval or pass claims.
- No external network/model request is made. No artifact is written to the selected repository.

## Roadmap Contracts (Not Implemented)

- **Approval**: reviewer action creates a versioned approved baseline; generated output alone never implies approval.
- **Change workflow**: a user-selected request references approved requirement IDs and acceptance criteria; generated code is isolated and requires explicit confirmation.
- **Test execution**: results are recorded only after an explicitly authorized command runs; proposed/not-run tests remain distinct.
- **Drift report**: a later pinned repository revision is compared with an approved baseline; findings link changed evidence and require human disposition.
- **GenAI adapter**: disabled by default; configuration must disclose provider, sent data, retention terms, and source-owner approval.