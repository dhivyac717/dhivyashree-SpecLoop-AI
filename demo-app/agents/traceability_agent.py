"""Link Shopizer requirements to source, design inventory, and proposed tests."""

from __future__ import annotations


def run(artifacts: dict) -> dict:
    """Build traceability rows while preserving verification status."""
    rows = []
    for requirement in artifacts["requirements"]["requirements"]:
        design = next(
            (item for item in artifacts["design"]["capabilities"] if item["name"] == requirement["capability"]),
            None,
        )
        tests = [
            test["id"]
            for test in artifacts["tests"]["proposedTests"]
            if test["requirementId"] == requirement["id"]
        ]
        rows.append({
            "requirementId": requirement["id"],
            "sources": requirement["evidence"],
            "designCapability": design["name"] if design else None,
            "proposedTests": tests,
            "verification": "source link discovered; tests proposed, not executed",
        })
    return {"rows": rows}