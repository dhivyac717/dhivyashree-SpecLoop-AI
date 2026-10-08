# SpecLoop-AI Project Backlog

Status: current local prototype includes deterministic discovery, draft artifacts, traceability, Streamlit previews/downloads, and Spec Kit setup. See `specs/001-shopizer-analysis/tasks.md` for the executable feature task breakdown.

## Completed Prototype Work

- [x] Discover Shopizer Maven metadata, supported Java API mappings, relevant tests, and ignored/disabled annotations.
- [x] Generate eight source-linked Markdown artifacts and expose them in the local Streamlit app.
- [x] Add fixture tests for route extraction, test classification, and artifact traceability.
- [x] Initialize official GitHub Spec Kit for Copilot and add the project constitution.

## Future Work

- [ ] Add opt-in model-provider adapter only after data-owner and retention approval.
- [ ] Add reviewer approval/versioning workflow for accepted requirements and specifications.
- [ ] Add implementation task generation from approved specifications.
- [ ] Add isolated worktree/branch support for generated code changes and explicit test execution.
- [ ] Compare pinned source revisions to approved specifications to report drift.
- [ ] Evaluate source-reference accuracy and analyst time against a measured baseline.
- [ ] Define publication license and obtain project-owner approval.