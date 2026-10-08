# SpecLoop-AI Hackathon Submission

## Theme

GenAI/AgenticAI in Software Engineering: SDLC productivity, engineering excellence, and IT modernization.

## Idea Title

**Spec Loop AI: From Source Code Discovery to Specification-Driven Engineering**

## Problem Statement

In many organizations, source code is the only artifact that truly reflects how an application works. Over time, business requirements become outdated, design documents are forgotten, and test cases fail to keep pace with changes. When new team members join or modernization projects begin, significant effort is spent understanding the application before development can start.

This knowledge gap creates delays, increases dependency on a few experienced team members, and makes it difficult to confidently enhance or modernize applications. Organizations need a way to convert knowledge hidden in source code into clear business requirements and specifications that can drive future development in a structured, sustainable way.

## Idea Description

SpecLoop-AI helps organizations unlock knowledge hidden inside applications and transform it into a foundation for future development.

The journey starts with source code. SpecLoop-AI analyzes the application and prepares evidence-linked drafts of business requirements, functional and technical specifications, user stories, test scenarios, and traceability artifacts. Human reviewers validate business intent before specifications become the baseline for future work.

```text
Source Code and Tests
        |
        v
Evidence Discovery
        |
        v
       BRD
        |
        v
Functional and Technical Specifications
        |
        v
Specification-Driven Development
        |
   +----+----+
   v         v
  Code      Tests
   +----+----+
        v
Traceability, Validation, and Drift Review
```

Once reviewed specifications are established, they guide future enhancements. Proposed changes are linked to affected requirements, code, and tests so teams can validate implementation against the agreed behavior. Specifications become living assets rather than an afterthought.

## Benefits and Impacts

### Faster Understanding of Existing Applications

Reduce the time spent locating relevant modules, APIs, tests, and behavior before development begins.

### Accelerated Modernization

Turn undocumented applications into reviewable specification baselines that can inform modernization planning.

### Reduced Dependency on SMEs

Capture source-backed business and technical knowledge so teams have an inspectable starting point for conversations with experienced subject-matter experts.

### Improved Developer Productivity

Help teams spend less time reconstructing existing behavior and more time evaluating and delivering changes.

### Better Software Quality

Map requirements to test scenarios and make missing or unverified coverage visible before changes are treated as complete.

### End-to-End Traceability

Connect evidence, requirements, specifications, implementation work, and test results, with draft and verification status retained.

These are intended benefits, not measured results. The prototype includes no productivity study or quality benchmark.

## Solution Architecture

```text
Shopizer Source + Tests
          |
          v
Read-only Discovery and Evidence Index
          |
          v
BRD and Functional/Technical Specification Drafts
          |
          v
Human Review and Approval
          |
          v
Specification-Driven Change Plan
          |
     +----+----+
     v         v
  Code Change  Test Scenarios/Results
     +----+----+
          v
 Traceability and Drift Insights
```

### Prototype Tools

- Python 3.11+ for deterministic repository discovery and artifact generation.
- Streamlit for the local analysis, review, and download interface.
- Optional Azure OpenAI BRD drafting through the official OpenAI Python SDK, gated by environment configuration and explicit per-run consent.
- Git metadata to identify the analyzed revision when available.
- GitHub Spec Kit and Copilot skills for project specifications, plans, and tasks.
- Shopizer Java/Maven repository as the case-study source.

The default analysis is deterministic and makes no model call. If the user explicitly opts in and configures an approved Azure OpenAI deployment, the app sends analyst-entered context plus discovered route/source-reference metadata for BRD drafting; it does not send Java source-file contents in that request. External AI use requires organizational source-data and retention approval. The adapter validates citations and labels output as an unapproved draft. The app does not modify Shopizer code or execute Shopizer tests. Semantic Kernel and AI Foundry remain exploratory options.

## What Makes SpecLoop-AI Different?

Most AI solutions help teams generate code from requirements. SpecLoop-AI starts where many enterprises actually struggle: existing source code and missing or stale documentation.

**Traditional approach**: BRD -> Code -> Test

**SpecLoop-AI approach**: Source Code -> Evidence -> BRD -> Specifications -> Code -> Test -> Traceability

## Shopizer Reference

The case study analyzes Shopizer storefront order checkout, shopping cart operations, and customer registration/authentication. It records the inspected repository revision, source references, and test status. In the checked-out source, the order API integration test is ignored and incomplete; this is reported as a coverage gap, not as a passing test result.

Reference project: https://github.com/shopizer-ecommerce/shopizer

## Current Demo

Run the demo using the commands in [README.md](README.md). The local app scans a Shopizer repository, previews eight deterministic Markdown artifacts, and downloads them individually or as a ZIP. With explicit Azure consent/configuration, it adds an AI-assisted BRD draft as an additional artifact. All generated requirements and user-story seeds remain drafts requiring review.

## Reference URL

https://github.com/dhivyac717/dhivyashree-SpecLoop-AI

## Publication Note

The SpecLoop-AI license has not been selected. See [LICENSE.md](LICENSE.md) and [NOTICE.md](NOTICE.md) before making public distribution claims.