# Contributing

## Evidence and Artifacts

- Record the Shopizer revision and cite source paths/line numbers for observed behavior.
- Label statements as observed, inferred, proposed, or stakeholder-approved.
- Keep test discovery separate from execution results; never imply a test ran when it did not.
- Preserve links among requirements, specifications, implementation, and tests.
- Do not convert implementation details into business policy without owner review.

## Code and Data

- Keep repository discovery read-only. Any future code-generation workflow must use an isolated, user-approved workspace.
- Use synthetic fixtures only. Never commit Shopizer customer PII, passwords, tokens, payment details, source archives, or secrets.
- Add focused tests for scanner, artifact generation, and UI changes.
- External AI/provider integration requires explicit data-owner approval, provider/retention review, secret handling, and user-visible disclosure.

## Pull Request Checklist

- Run `python -m unittest discover -s demo-app/tests -v`.
- Verify generated claims have source evidence and proposed tests are not presented as executed.
- Confirm no local paths, secrets, private screenshots, or customer data were added.
- Update feature artifacts when scope or acceptance criteria change.

## Prototype Limitations

The current app performs deterministic source discovery and artifact drafting. LLM generation, source-to-code implementation, actual Shopizer test execution, revision drift detection, authentication, persistence, and deployment are not implemented.