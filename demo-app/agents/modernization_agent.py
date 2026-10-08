"""Report evidence-backed Shopizer modernization observations without scoring risk."""

from __future__ import annotations


def run(source_analysis: dict, rubric: dict | None = None) -> dict:
    """Summarize detectable test gaps and platform metadata; infer no vulnerability status."""
    criteria = (rubric or {}).get(
        "criteria",
        ["ignored/disabled relevant tests", "declared runtime and framework baseline"],
    )
    findings = []
    for capability_name, capability in source_analysis["capabilities"].items():
        ignored = [test for test in capability["tests"] if test["ignored"]]
        if ignored:
            findings.append({
                "capability": capability_name,
                "observation": f"{len(ignored)} relevant test file(s) contain an ignore/disable annotation.",
                "evidence": [test["source"] for test in ignored],
                "confidence": "high for source annotation; runtime test status not executed",
                "recommendation": "Review the ignored tests and add active coverage for the corresponding API flow.",
            })

    project = source_analysis["project"]
    findings.append({
        "capability": "Project baseline",
        "observation": f"The root POM declares Java {project['javaVersion']} and Spring Boot {project['springBootVersion']}.",
        "evidence": ["pom.xml"],
        "confidence": "high for declared POM values; support/vulnerability status not assessed",
        "recommendation": "Compare the declared baseline with current organizational support policy before planning an upgrade.",
    })
    return {
        "rubric": {
            "criteria": criteria,
            "mode": "evidence inventory only; no risk scoring",
        },
        "findings": findings,
        "limitations": [
            "No Maven tests, dependency scan, runtime telemetry, performance benchmark, or security audit was run.",
            "This static scan does not determine whether a dependency is vulnerable or unsupported.",
        ],
    }