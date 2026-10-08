"""Safety and citation tests for optional Azure OpenAI BRD drafting."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace

APP_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP_ROOT))

from agents.azure_openai_brd import AzureOpenAIError, generate_brd_draft


class _MockAzureClient:
    def __init__(self, completion, captured: dict) -> None:
        def create(**kwargs):
            captured["create"] = kwargs
            return completion

        self.chat = SimpleNamespace(completions=SimpleNamespace(create=create))


class AzureOpenAIBrdTests(unittest.TestCase):
    def setUp(self) -> None:
        self.requirements = {
            "requirements": [
                {
                    "id": "BR-CART-01",
                    "capability": "ShoppingCartService",
                    "statement": "The source declares POST /api/v1/cart.",
                    "evidence": [{"source": "sm-shop/src/ShoppingCartApi.java", "line": 76}],
                }
            ]
        }
        self.evidence_id = "BR-CART-01@sm-shop/src/ShoppingCartApi.java#L76"

    def _completion(self, evidence_id: str):
        content = {
            "requirements": [
                {
                    "id": "BRD-001",
                    "statement": "A shopper can start a cart by adding a product.",
                    "rationale": "The storefront exposes cart creation.",
                    "evidence_ids": [evidence_id],
                }
            ]
        }
        return SimpleNamespace(
            model="mock-deployment",
            choices=[SimpleNamespace(message=SimpleNamespace(content=json.dumps(content)))],
        )

    def test_requires_endpoint_and_consent_configuration_before_network(self) -> None:
        calls = []
        with self.assertRaises(AzureOpenAIError):
            generate_brd_draft(
                "Shopper needs a cart.",
                self.requirements,
                endpoint="",
                api_key="",
                deployment="",
                client_factory=lambda **_kwargs: calls.append(True),
            )
        self.assertEqual(calls, [])

    def test_sends_only_business_context_and_route_evidence_and_labels_draft(self) -> None:
        captured = {}

        def client_factory(**kwargs):
            captured["client_config"] = kwargs
            return _MockAzureClient(self._completion(self.evidence_id), captured)

        result = generate_brd_draft(
            "A shopper should be able to begin a cart.",
            self.requirements,
            endpoint="https://example.openai.azure.com",
            api_key="test-key",
            deployment="mock-deployment",
            client_factory=client_factory,
        )

        serialized_request = json.dumps(captured["create"])
        self.assertIn("A shopper should be able to begin a cart.", serialized_request)
        self.assertIn(self.evidence_id, serialized_request)
        self.assertNotIn("class ShoppingCart", serialized_request)
        self.assertNotIn("api_key", captured["create"])
        self.assertEqual(captured["client_config"]["api_key"], "test-key")
        self.assertEqual(result["requirements"][0]["evidence_ids"], [self.evidence_id])
        self.assertIn("human review required", result["markdown"])

    def test_rejects_unknown_evidence_citation(self) -> None:
        with self.assertRaisesRegex(AzureOpenAIError, "evidence not found"):
            generate_brd_draft(
                "A shopper needs a cart.",
                self.requirements,
                endpoint="https://example.openai.azure.com",
                api_key="test-key",
                deployment="mock-deployment",
                client_factory=lambda **kwargs: _MockAzureClient(
                    self._completion("made-up-evidence"), {}
                ),
            )


if __name__ == "__main__":
    unittest.main()