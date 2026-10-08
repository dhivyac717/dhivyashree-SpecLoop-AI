"""Summarize existing Shopizer tests and propose unexecuted API checks."""

from __future__ import annotations


def run(requirements: dict, design: dict) -> dict:
    """Keep discovered tests separate from deterministic test suggestions."""
    existing = []
    for capability in design["capabilities"]:
        existing.extend(
            {"capability": capability["name"], **test}
            for test in capability["tests"]
        )

    proposals = []
    for requirement in requirements["requirements"]:
        proposals.append({
            "id": f"TC-{requirement['id'][3:]}",
            "requirementId": requirement["id"],
            "capability": requirement["capability"],
            "scenario": f"Exercise {requirement['statement']} with valid and invalid inputs.",
            "status": "proposed; not implemented or executed",
        })
    return {
        "existingTests": existing,
        "proposedTests": proposals,
        "executionStatus": "No tests were executed by this analysis.",
    }