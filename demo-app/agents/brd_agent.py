"""Draft a source-grounded capability brief from Shopizer API evidence."""

from __future__ import annotations


_PREFIXES = {
    "OrderService": "ORD",
    "ShoppingCartService": "CART",
    "CustomerService": "CUST",
}


def run(business_context: dict) -> dict:
    """Create stable, explicitly code-derived capability requirements."""
    requirements = []
    for capability in business_context["capabilities"]:
        prefix = _PREFIXES.get(capability["name"], "CAP")
        for index, route in enumerate(capability["apiRoutes"], start=1):
            requirements.append({
                "id": f"BR-{prefix}-{index:02d}",
                "capability": capability["name"],
                "statement": f"The storefront source declares {route['method']} {route['path']}.",
                "status": "observed_from_source; not stakeholder-approved business policy",
                "evidence": [{"source": route["source"], "line": route["line"]}],
            })
    return {
        "requirements": requirements,
        "approvalStatus": "draft; stakeholder review required",
    }