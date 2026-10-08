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

## Verify

```powershell
python -m unittest discover -s demo-app/tests -v
```

Expected: the scanner fixture test passes, all generated requirements have traceability rows, and the report states that Shopizer tests were not executed.

For an interactive check, run Streamlit AppTest against `demo-app/streamlit_app.py`, click **Analyze repository**, and verify seven tabs plus the ZIP and eight individual download buttons.

## Current Scope Versus Roadmap

This quickstart verifies the deterministic source-to-artifact MVP only. Approved-baseline persistence, GenAI, code generation, Shopizer test execution, and source-revision drift comparison are not included in this run path.

## Safety

The analyzer is read-only and makes no external AI calls. It inventories test files but does not execute Shopizer code or tests. Verify generated drafts before treating them as approved business policy.