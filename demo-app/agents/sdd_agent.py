"""Describe Shopizer API and module boundaries from discovered evidence."""

from __future__ import annotations


def run(requirements: dict, source_analysis: dict) -> dict:
    """Create a design inventory and requirement links; propose no code changes."""
    capability_designs = []
    for name, capability in source_analysis["capabilities"].items():
        capability_designs.append({
            "name": name,
            "apiRoutes": capability["apiRoutes"],
            "sourceFiles": capability["sourceFiles"],
            "requirements": [
                requirement["id"]
                for requirement in requirements["requirements"]
                if requirement["capability"] == name
            ],
            "tests": capability["tests"],
        })
    return {
        "project": source_analysis["project"],
        "revision": source_analysis["revision"],
        "modules": source_analysis["project"]["modules"],
        "capabilities": capability_designs,
        "status": "existing implementation inventory; not a proposed target architecture",
    }