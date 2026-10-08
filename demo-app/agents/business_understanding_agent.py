"""Summarize Shopizer capabilities from discovered source and test evidence."""

from __future__ import annotations


def run(source_analysis: dict) -> dict:
    """Build capability summaries without turning implementation into policy."""
    capabilities = []
    for name, discovered in source_analysis["capabilities"].items():
        routes = discovered["apiRoutes"]
        capabilities.append({
            "name": name,
            "sourceFiles": discovered["sourceFiles"],
            "apiRoutes": routes,
            "tests": discovered["tests"],
            "observations": [
                {
                    "claim": f"The source declares {route['method']} {route['path']}.",
                    "source": route["source"],
                    "line": route["line"],
                    "status": "observed_from_source",
                }
                for route in routes
            ],
        })
    return {
        "project": source_analysis["project"],
        "revision": source_analysis["revision"],
        "capabilities": capabilities,
        "businessApproval": "not reviewed; inferred business intent is intentionally not asserted",
    }