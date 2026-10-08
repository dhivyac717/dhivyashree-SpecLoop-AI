# Quickstart: Shopizer Analysis

## Prerequisites

- Python 3.11 or newer.
- The SpecLoop-AI project dependencies installed from `demo-app/requirements.txt`.
- A local Shopizer Maven repository with a root `pom.xml` and Java source.

## Run

From the SpecLoop-AI repository root:

```powershell
python -m pip install -r demo-app/requirements.txt
python -m streamlit run demo-app/streamlit_app.py
```

Enter the Shopizer repository root and choose **Analyze repository**. Review the source analysis and artifact tabs, then download individual Markdown files or the ZIP bundle.

### Optional Azure OpenAI BRD Draft

The deterministic evidence scan works without Azure configuration. After obtaining organizational/provider approval, configure these variables in the process environment before starting Streamlit: `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_API_KEY`, and `AZURE_OPENAI_DEPLOYMENT`. Optionally set `AZURE_OPENAI_API_VERSION`.

In the app, expand **Optional Azure OpenAI BRD draft**, enter analyst-reviewed business context, and provide explicit per-run consent before analysis. The request sends that context and discovered route/source-reference metadata, not Java file contents. The response is citation-validated and remains an unapproved draft. Do not enter customer data, source excerpts, credentials, or secrets. Never place the API key in this repository.

## Verify

```powershell
python -m unittest discover -s demo-app/tests -v
```

Expected: the scanner fixture test passes, all generated requirements have traceability rows, and the report states that Shopizer tests were not executed.

For an interactive check, run Streamlit AppTest against `demo-app/streamlit_app.py`, click **Analyze repository**, and verify eight tabs plus the ZIP and deterministic artifact download buttons. Mock-provider tests cover the Azure path without contacting a real endpoint.

## Verification Record

Validated 2026-10-08 against Shopizer revision `6a4a0a65a`:

- `python -m unittest discover -s demo-app/tests -v`: 4 tests passed.
- `python -m compileall -q demo-app`: passed.
- Streamlit AppTest: default path rendered eight tabs and deterministic downloads without an exception.
- Streamlit AppTest: Azure consent enabled with no endpoint configured produced an actionable warning and retained deterministic artifacts; no request was made.
- Azure adapter unit tests use a mock client; no live Azure deployment or Shopizer test suite was run.

## Current Scope Versus Roadmap

This quickstart verifies the deterministic source-to-artifact MVP and optional Azure BRD draft. Approved-baseline persistence, code generation, Shopizer test execution, and source-revision drift comparison are not included in this run path.

## Safety

The deterministic analyzer is read-only and makes no external AI calls. The optional Azure action sends only analyst-entered context and route/source-reference metadata after explicit consent. It inventories tests but does not execute Shopizer code or tests. Verify generated drafts before treating them as approved business policy.