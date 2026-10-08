# Data Model: Local Shopizer Analysis

All records are in-memory Python dictionaries for one analysis run. They are not persisted and contain source metadata, not commerce transactions.

## AnalysisRun

- `repository`: resolved local path.
- `revision`: short Git revision or `null` when unavailable.
- `project`: root Maven metadata (`name`, `version`, `javaVersion`, `springBootVersion`, `modules`).
- `capabilities`: map keyed by `OrderService`, `ShoppingCartService`, and `CustomerService`.
- `analysisStatus`: explicit statement that the scan is static and tests were not executed.

## CapabilityEvidence

- `sourceFiles`: repository-relative Java paths matching a capability.
- `apiRoutes`: list of discovered mappings (`method`, `path`, `source`, `line`).
- `tests`: relevant Java test file inventory (`name`, `source`, `status`, `ignored`, `testAnnotationCount`, `testMethods`).
- Missing source/routes/tests are represented as empty lists, not invented evidence.

## RequirementObservation

- `id`: stable capability-prefixed identifier such as `BR-ORD-01`.
- `capability`: capability name.
- `statement`: source-derived API mapping observation, not business policy.
- `status`: draft/source-observed label.
- `evidence`: one or more source path and line records.

## ProposedTest

- `id`, `requirementId`, `capability`, and `scenario`.
- `status`: proposed; not implemented or executed.

## TraceabilityRow

- `requirementId`, source `sources`, `designCapability`, `proposedTests`, and `verification` status.
- Every generated requirement must have a traceability row; test links remain proposals.

## ArtifactBundle

Map of eight Markdown filenames to content strings. The UI offers each file and a ZIP for download; it does not write to the selected source repository.

## Roadmap Entities (Not Implemented)

- **ApprovedBaseline**: reviewed artifact revision, reviewer/approval status, source revision, and effective date.
- **ChangeProposal**: requested enhancement linked to affected approved requirement IDs and acceptance criteria.
- **ImplementationRun**: isolated candidate-workspace reference, changed files, and user authorization state.
- **TestExecution**: actual command, environment, timestamp, result, and linked acceptance criteria; proposed tests are not executions.
- **DriftFinding**: difference between a pinned source revision and approved evidence/specification links, with review status.

These entities require retention, access, identity, and data-safety decisions before persistence or code execution is added.