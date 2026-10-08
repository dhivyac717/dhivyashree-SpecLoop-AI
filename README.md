# SpecLoop-AI

## From Source Code Discovery to Specification-Driven Engineering

SpecLoop-AI is a hackathon prototype for recovering application knowledge from source code and turning it into reviewable requirements, specifications, test scenarios, and traceability. The Shopizer case study focuses on order checkout, shopping-cart operations, and customer registration/authentication.

**Hackathon repository**: [dhivyac717/dhivyashree-SpecLoop-AI](https://github.com/dhivyac717/dhivyashree-SpecLoop-AI)

### The Problem

In many organizations, source code is the only artifact that accurately reflects how an application behaves. Requirements become outdated, design documents are forgotten, and tests drift. New team members and modernization teams spend time reconstructing system knowledge before they can safely make changes.

### The Idea

SpecLoop-AI starts with the existing application rather than assuming complete, current documentation. It discovers source and test evidence, drafts business and technical artifacts, and links requirements to code and tests. Reviewed specifications can then guide future feature work and validation.

```text
Source Code and Tests
	|
	v
Evidence Discovery -> BRD -> Functional / Technical Specifications
				     |
				     v
			Specification-Driven Development
			      /                 \
			   Code               Tests
			      \                 /
			 Traceability and Drift Review
```

### What Works in This Prototype

- Read-only discovery of Shopizer Maven metadata, Java API mappings, relevant source files, test files, and ignore annotations.
- Deterministic generation of eight reviewable Markdown artifacts, including a BRD evidence inventory, with source references, test status, and traceability.
- Optional ninth artifact: an Azure OpenAI BRD draft from analyst-provided context and route/source-reference metadata, gated by explicit per-run consent and environment configuration.
- Streamlit UI to analyze a local repository, review artifacts, and download Markdown files or a ZIP bundle.
- Official GitHub Spec Kit workflow initialized for Copilot, with a project constitution and feature specification.

The default analysis is deterministic and makes no network call. A separate Azure OpenAI option can draft business requirements only after organizational approval, environment configuration, and explicit per-run consent. It sends analyst-entered context and selected route/source-reference metadata, not Java source contents. Generated text remains unapproved. The prototype does not generate or modify application code, execute Shopizer tests, or detect drift across historical revisions.

### Shopizer Case Study

The scanner reads the root `pom.xml` and targets the five declared modules: `sm-core-model`, `sm-core-modules`, `sm-core`, `sm-shop-model`, and `sm-shop`. The reviewed source includes authenticated and anonymous order checkout, cart operations, and customer registration/login.

The order integration test is ignored and incomplete in the inspected checkout. Existing cart/customer tests cover selected flows only. Reports distinguish test discovery from test execution; no Shopizer tests are run by this tool.

Shopizer reference: [shopizer-ecommerce/shopizer](https://github.com/shopizer-ecommerce/shopizer). The source code is not bundled in this project. See [NOTICE.md](NOTICE.md) for attribution and licensing context.

### Run Locally

Prerequisite: Python 3.11 or newer.

```powershell
python -m pip install -r demo-app/requirements.txt
python -m streamlit run demo-app/streamlit_app.py
```

In the app, select the local Shopizer repository root and choose **Analyze repository**. Source discovery is read-only and makes no external model call. The optional Azure BRD draft sends only analyst context and route/source-reference metadata after explicit consent.

### Specification Workflow

This repository is initialized with GitHub Spec Kit for Copilot. Open `SpecLoop-AI` as the VS Code workspace and use `/speckit-specify`, `/speckit-plan`, `/speckit-tasks`, and `/speckit-analyze` to evolve the feature artifacts. The current feature is [001-shopizer-analysis](specs/001-shopizer-analysis/spec.md).

Run the deterministic pipeline test:

```powershell
python -m unittest discover -s demo-app/tests -v
```

### Repository Structure

```text
.github/skills/       Spec Kit workflow skills for Copilot
.specify/             Spec Kit templates, scripts, constitution, and feature pointer
.spec-kit/             Hackathon requirements, design, and project backlog
specs/                 Versioned feature spec, plan, research, contracts, and tasks
architecture/          Shopizer and proposed agent/data/deployment architecture
case-studies/shopizer/ Order, cart, and customer evidence/artifacts
diagrams/              Source-to-specification and traceability diagrams
demo-app/               Streamlit app, deterministic agents, and synthetic tests/data
generated-output/        Curated consolidated Shopizer report drafts
pitch/                   Executive summary and hackathon one-pager
```

### Safety and Status

Generated business intent remains a draft until stakeholder approval. Do not commit customer PII, credentials, tokens, payment details, private source archives, or secrets. No productivity, quality, security, or modernization benefit is claimed as measured. Choose and review this project's license before public release; see [LICENSE.md](LICENSE.md).