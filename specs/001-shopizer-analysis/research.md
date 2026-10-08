# Research: Local Shopizer Analysis and Artifacts

## Decision: Use a deterministic local pipeline for the first release

- **Rationale**: No external AI provider or data-processing approval is configured. The current user goal is to make the Shopizer case-study scaffold work. Deterministic discovery gives verifiable evidence without transmitting source code.
- **Alternatives considered**: Model-generated source summaries; deferred because provider, retention, and source-sharing policies are undecided. Static sample JSON; rejected as the only behavior because it cannot analyze a changed repository.

## Decision: Parse root Maven metadata as structured XML

- **Rationale**: Module, artifact, version, Java, and parent-version values are declared in `pom.xml`; XML parsing avoids fragile text matching.
- **Evidence**: The Shopizer root POM declares five modules, Java 11, and Spring Boot parent 2.5.12.
- **Limit**: Child-property inheritance and Maven profile resolution are not modeled; output reflects root declarations only.

## Decision: Extract route annotations with bounded static source scanning

- **Rationale**: The inspected Shopizer APIs use Spring mapping annotations and the required report needs paths and line references. The current scanner is read-only and deterministic.
- **Evidence**: The inspected `OrderApi`, `ShoppingCartApi`, and `AuthenticateCustomerApi` contain `/api/v1` controller mappings and route annotations.
- **Limit**: This is not a Java parser. Complex composed annotations, constants, multiline expressions, and runtime route registration may not be discovered. Unsupported mappings must not be described as absent behavior.

## Decision: Report discovered tests, not inferred execution results

- **Rationale**: Static source inspection can see test files and annotations but does not prove execution, assertions, or pass status.
- **Evidence**: The order integration class is annotated `@Ignore` and does not perform checkout; cart/customer integration tests cover selected paths.
- **Limit**: Annotation counts are an inventory aid, not a measure of test quality or coverage.

## Decision: Keep artifacts downloadable and non-persistent by default

- **Rationale**: This avoids silently overwriting reviewed drafts and satisfies the read-only source boundary.
- **Alternative considered**: Automatically update `generated-output/`; deferred until review/approval and overwrite semantics are specified.

## Decision: Use Python standard-library tests plus Streamlit AppTest

- **Rationale**: `unittest` validates scanner and traceability behavior without another test dependency; Streamlit AppTest covers the user workflow.
- **Validation observed**: The scanner discovered Shopizer module metadata and checkout routes; the app displayed seven tabs and eight downloads without AppTest exceptions.

## Decision: Treat generated specifications as reviewed baselines

- **Rationale**: Source analysis recovers implementation facts, not definitive current business intent. A designated reviewer must approve artifacts before future work treats them as authoritative.
- **Current state**: The prototype labels requirements and story seeds as drafts; it does not persist approvals or history.
- **Follow-up**: Define reviewer identity, version history, rejection/edit flow, and conflict resolution before adding persistence.

## Decision: GenAI drafting is opt-in and follows evidence discovery

- **Rationale**: The hackathon idea includes GenAI, but Shopizer source may be proprietary and customer-related code contains sensitive fields. No provider or retention terms are approved.
- **Current state**: The demo makes no model calls. Azure OpenAI, Semantic Kernel, and AI Foundry docs are exploratory only.
- **Follow-up**: Select the provider, data boundary, retention policy, disclosure, and evaluation criteria with the data owner before implementation.

## Decision: Future implementation and test execution require isolation

- **Rationale**: The source analyzer is read-only. A future code agent must not weaken that guarantee or mutate the selected source by surprise.
- **Follow-up**: Define a candidate worktree/branch, allowed commands, test-result capture, rollback, and human merge approval before enabling generated code or test execution.

## Decision: Drift analysis compares pinned source revisions

- **Rationale**: Source and line references have meaning only relative to an identified repository revision and approved artifact baseline.
- **Current state**: The scanner reports the current revision; it does not store history or compare revisions.
- **Follow-up**: Design baseline storage, source-location normalization, change detection, and reviewer triage before implementing drift detection.