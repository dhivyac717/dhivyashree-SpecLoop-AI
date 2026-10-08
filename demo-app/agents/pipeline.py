"""Run the local Shopizer analysis and render reviewable Markdown artifacts."""

from __future__ import annotations

from agents import (
    brd_agent,
    business_understanding_agent,
    code_discovery_agent,
    modernization_agent,
    sdd_agent,
    test_agent,
    traceability_agent,
)


def _source_reference(evidence: dict) -> str:
    return f"`{evidence['source']}#L{evidence['line']}`"


def _render_source_analysis(source: dict, context: dict) -> str:
    project = source["project"]
    sections = [
        "# Shopizer Source Analysis",
        "",
        f"- Repository: `{source['repository']}`",
        f"- Revision: `{source['revision'] or 'unknown (Git revision unavailable)'}`",
        f"- Maven artifact/version: `{project['name']}:{project['version']}`",
        f"- Java: `{project['javaVersion'] or 'not declared'}`",
        f"- Spring Boot parent: `{project['springBootVersion'] or 'not detected'}`",
        f"- Modules: {', '.join(f'`{module}`' for module in project['modules'])}",
        f"- Status: {source['analysisStatus']}",
        "",
        "This is static source discovery. It does not execute Shopizer or its tests.",
    ]
    for capability in context["capabilities"]:
        sections.extend(["", f"## {capability['name']}", "", "### API mappings"])
        if capability["apiRoutes"]:
            sections.extend(
                f"- `{route['method']} {route['path']}` ({_source_reference(route)})"
                for route in capability["apiRoutes"]
            )
        else:
            sections.append("No matching API mapping was discovered.")
        sections.extend(["", "### Relevant source files"])
        sections.extend(f"- `{path}`" for path in capability["sourceFiles"][:40])
        if len(capability["sourceFiles"]) > 40:
            sections.append(f"- ... {len(capability['sourceFiles']) - 40} additional files (see structured scan results).")
        sections.extend(["", "### Relevant tests"])
        if capability["tests"]:
            for test in capability["tests"]:
                sections.append(
                    f"- `{test['name']}`: **{test['status']}**; "
                    f"{test['testAnnotationCount']} `@Test` annotation(s); `{test['source']}`"
                )
        else:
            sections.append("No matching test file was discovered.")
    return "\n".join(sections) + "\n"


def _render_brd(requirements: dict, context: dict, revision: str | None) -> str:
    lines = [
        "# Shopizer Capability Requirements (Draft)",
        "",
        f"Source revision: `{revision or 'unknown'}`.",
        "",
        "These are **source-derived capability observations**, not stakeholder-approved business requirements. "
        "Statements deliberately describe declared API mappings rather than infer business intent.",
    ]
    for capability in context["capabilities"]:
        items = [item for item in requirements["requirements"] if item["capability"] == capability["name"]]
        lines.extend(["", f"## {capability['name']}"])
        if not items:
            lines.append("No API route observations were discovered.")
        for item in items:
            evidence = ", ".join(_source_reference(entry) for entry in item["evidence"])
            lines.append(f"- **{item['id']}** ({item['status']}): {item['statement']} Evidence: {evidence}.")
    lines.extend(["", "## Approval", "", requirements["approvalStatus"] + "."])
    return "\n".join(lines) + "\n"


def _render_user_stories(context: dict) -> str:
    lines = [
        "# Shopizer User-Story Seeds",
        "",
        "These are inferred templates based on discovered APIs, not validated user needs or approved acceptance criteria.",
    ]
    for capability in context["capabilities"]:
        lines.extend([
            "",
            f"## {capability['name']}",
            "",
            f"As an API consumer, I want to use the discovered {capability['name']} endpoints so that I can interact with the capability exposed by Shopizer.",
            "",
            "Candidate acceptance evidence:",
        ])
        if capability["apiRoutes"]:
            lines.extend(
                f"- `{route['method']} {route['path']}` ({_source_reference(route)})"
                for route in capability["apiRoutes"]
            )
        else:
            lines.append("- No route was discovered; identify the intended user outcome with stakeholders.")
        lines.append("- Product owner review is required to define actual value and success criteria.")
    return "\n".join(lines) + "\n"


def _render_functional_requirements(requirements: dict) -> str:
    lines = [
        "# Shopizer Functional Requirement Observations",
        "",
        "Each row records a route declared by source code. These observations do not define complete request validation, authorization, or business policy.",
        "",
        "| ID | Capability | Source-derived observation | Evidence | Status |",
        "| --- | --- | --- | --- | --- |",
    ]
    for requirement in requirements["requirements"]:
        evidence = ", ".join(_source_reference(item) for item in requirement["evidence"])
        lines.append(
            f"| `{requirement['id']}` | {requirement['capability']} | {requirement['statement']} | {evidence} | Observed route declaration; behavior requires review |"
        )
    return "\n".join(lines) + "\n"


def _render_sdd(design: dict) -> str:
    project = design["project"]
    lines = [
        "# Shopizer Software Design Inventory",
        "",
        f"Status: {design['status']}.",
        f"Source revision: `{design['revision'] or 'unknown'}`.",
        f"Runtime baseline declared by root POM: Java `{project['javaVersion']}`, Spring Boot `{project['springBootVersion']}`.",
        "",
        "## Maven modules",
    ]
    lines.extend(f"- `{module}`" for module in design["modules"])
    for capability in design["capabilities"]:
        lines.extend(["", f"## {capability['name']}", "", "### Routes"])
        if capability["apiRoutes"]:
            lines.extend(
                f"- `{route['method']} {route['path']}`; implementation reference `{route['source']}#L{route['line']}`"
                for route in capability["apiRoutes"]
            )
        else:
            lines.append("No matching route mapping discovered.")
        lines.extend(["", "### Requirement links"])
        lines.extend(f"- `{requirement_id}`" for requirement_id in capability["requirements"])
        lines.extend(["", "### Existing test files"])
        lines.extend(
            f"- `{test['source']}`: {test['status']}"
            for test in capability["tests"]
        )
    return "\n".join(lines) + "\n"


def _render_test_cases(tests: dict) -> str:
    lines = ["# Shopizer Test Inventory and Proposals", "", tests["executionStatus"], ""]
    lines.extend(["## Existing test files", ""])
    if tests["existingTests"]:
        for test in tests["existingTests"]:
            lines.append(
                f"- **{test['capability']} / {test['name']}**: {test['status']}; "
                f"{test['testAnnotationCount']} `@Test` annotation(s); `{test['source']}`"
            )
    else:
        lines.append("No matching test files discovered.")
    lines.extend(["", "## Proposed checks", "", "All rows below are suggestions; none were implemented or executed by this pipeline.", ""])
    for test in tests["proposedTests"]:
        lines.append(f"- **{test['id']}** ({test['requirementId']}): {test['scenario']} _{test['status']}._")
    return "\n".join(lines) + "\n"


def _render_traceability(traceability: dict) -> str:
    lines = [
        "# Shopizer Traceability Matrix",
        "",
        "Source links are discovered from code; proposed tests are not verification results.",
        "",
        "| Requirement | Source evidence | Design capability | Proposed test | Verification status |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in traceability["rows"]:
        source_links = ", ".join(
            f"`{source['source']}#L{source['line']}`" for source in row["sources"]
        )
        tests = ", ".join(f"`{test_id}`" for test_id in row["proposedTests"]) or "None generated"
        lines.append(
            f"| `{row['requirementId']}` | {source_links} | `{row['designCapability']}` | {tests} | {row['verification']} |"
        )
    return "\n".join(lines) + "\n"


def _render_modernization(assessment: dict) -> str:
    lines = [
        "# Shopizer Modernization Observations",
        "",
        "Static review only; this is not a security audit, dependency scan, test run, or modernization estimate.",
    ]
    for finding in assessment["findings"]:
        lines.extend([
            "",
            f"## {finding['capability']}",
            "",
            f"- Observation: {finding['observation']}",
            f"- Evidence: {', '.join(f'`{path}`' for path in finding['evidence'])}",
            f"- Confidence: {finding['confidence']}",
            f"- Next step: {finding['recommendation']}",
        ])
    lines.extend(["", "## Limitations", ""])
    lines.extend(f"- {limitation}" for limitation in assessment["limitations"])
    return "\n".join(lines) + "\n"


def run_pipeline(repository_path: str) -> dict:
    """Run deterministic discovery and return structured evidence plus Markdown files."""
    source = code_discovery_agent.run(repository_path)
    context = business_understanding_agent.run(source)
    requirements = brd_agent.run(context)
    design = sdd_agent.run(requirements, source)
    tests = test_agent.run(requirements, design)
    artifacts = {"requirements": requirements, "design": design, "tests": tests}
    traceability = traceability_agent.run(artifacts)
    modernization = modernization_agent.run(source)

    markdown = {
        "SourceAnalysis.md": _render_source_analysis(source, context),
        "BRD.md": _render_brd(requirements, context, source["revision"]),
        "SDD.md": _render_sdd(design),
        "UserStories.md": _render_user_stories(context),
        "FunctionalRequirements.md": _render_functional_requirements(requirements),
        "TestCases.md": _render_test_cases(tests),
        "TraceabilityMatrix.md": _render_traceability(traceability),
        "ModernizationAssessment.md": _render_modernization(modernization),
    }
    return {
        "source": source,
        "context": context,
        "requirements": requirements,
        "design": design,
        "tests": tests,
        "traceability": traceability,
        "modernization": modernization,
        "markdown": markdown,
    }