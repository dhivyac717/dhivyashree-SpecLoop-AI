# SpecLoop-AI Constitution

## Core Principles

### I. Evidence-Grounded Claims
Every statement about Shopizer behavior MUST cite a source file and line or a test artifact. Mark claims as observed, inferred, proposed, or stakeholder-approved. The analyzer MUST report missing evidence rather than invent behavior or business intent.

### II. Read-Only Source Analysis
Repository discovery MUST NOT modify the selected Shopizer repository, execute its application code, or run its tests. Record the repository revision for each analysis. Generated outputs belong only in the SpecLoop-AI project after an explicit user action.

### III. Complete Traceability
Each generated requirement MUST have a stable identifier and link to source evidence. Design observations, test suggestions, and modernization findings MUST link back to requirements or source evidence. Flag missing links instead of presenting incomplete coverage as complete.

### IV. Privacy and Provider Boundaries
Use synthetic customer examples only. Do not include real customer data, passwords, tokens, payment data, or secrets in prompts, fixtures, logs, screenshots, or generated artifacts. Source or artifact data MUST NOT be sent to an external model unless an owner has approved the provider and data-handling terms.

### V. Honest Verification and Human Approval
Report discovered tests separately from proposed tests, and never imply a test ran unless it did. Generated requirements and designs are drafts until a designated human approves them. Modernization observations MUST state evidence, confidence, and assessment limits; a version number alone is not a vulnerability finding.

## Project Constraints

- The current implementation is a local Python/Streamlit analyzer. Keep source discovery deterministic and avoid adding an AI provider, persistence service, or deployment dependency without an approved requirement.
- Shopizer is the analysis target, not a dependency of the SpecLoop-AI runtime. Work against a repository path supplied by the user and handle missing or malformed project files with actionable errors.
- Do not overwrite reviewed artifacts silently. The default analysis path previews and downloads generated files; persistent output requires a deliberate action.

## Development Workflow

- Add focused tests for route extraction, Maven metadata, test-status classification, generated artifacts, and traceability.
- Validate the UI and artifact generation against a synthetic fixture and a real Shopizer checkout; keep test data synthetic.
- Run `python -m unittest discover -s demo-app/tests` after changes to analysis behavior. Run Streamlit AppTest for changes to the interactive workflow.
- Report unrun checks explicitly. Do not claim Shopizer builds or tests pass unless they were run.

## Governance

This constitution governs SpecLoop-AI changes and takes precedence over conflicting project guidance. Amend it through review: explain the rationale, update the semantic version and amendment date, and check affected specs, plans, tasks, and tests. MAJOR marks incompatible policy changes, MINOR adds or materially expands principles, and PATCH clarifies existing policy. Review compliance when planning and validating each feature. Exceptions require explicit scope, rationale, and approval in the feature artifacts.

**Version**: 1.0.0 | **Ratified**: 2026-10-07 | **Last Amended**: 2026-10-07
