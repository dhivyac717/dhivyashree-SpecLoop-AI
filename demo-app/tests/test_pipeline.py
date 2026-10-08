"""Tests for deterministic Shopizer source discovery and artifact generation."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

APP_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP_ROOT))

from agents.pipeline import run_pipeline


class PipelineTests(unittest.TestCase):
    def _shopizer_fixture(self, root: Path) -> None:
        (root / "pom.xml").write_text(
            """<project xmlns="http://maven.apache.org/POM/4.0.0">
  <artifactId>shopizer-fixture</artifactId>
  <version>1.0</version>
  <parent><version>2.5.12</version></parent>
  <modules><module>sm-shop</module><module>sm-core</module></modules>
  <properties><java.version>11</java.version></properties>
</project>
""",
            encoding="utf-8",
        )
        api_path = root / "sm-shop/src/main/java/example/OrderApi.java"
        api_path.parent.mkdir(parents=True)
        api_path.write_text(
            """@RestController
@RequestMapping("/api/v1")
public class OrderApi {
    @PostMapping(value = {"/cart/{code}/checkout"})
    public void checkout() {}
}
""",
            encoding="utf-8",
        )
        test_path = root / "sm-shop/src/test/java/example/OrderApiIntegrationTest.java"
        test_path.parent.mkdir(parents=True)
        test_path.write_text(
            """@Ignore
public class OrderApiIntegrationTest {
    @Test
    public void checkout() {}
}
""",
            encoding="utf-8",
        )
        helper_path = root / "sm-shop/src/test/java/example/CartTestBean.java"
        helper_path.write_text("public class CartTestBean {}\n", encoding="utf-8")

    def test_pipeline_discovers_routes_tests_and_traceability(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            repository = Path(temporary_directory)
            self._shopizer_fixture(repository)

            result = run_pipeline(str(repository))

        project = result["source"]["project"]
        self.assertEqual(project["javaVersion"], "11")
        self.assertEqual(project["springBootVersion"], "2.5.12")
        order = result["source"]["capabilities"]["OrderService"]
        self.assertIn(
            "/api/v1/cart/{code}/checkout",
            [route["path"] for route in order["apiRoutes"]],
        )
        self.assertEqual([test["name"] for test in order["tests"]], ["OrderApiIntegrationTest.java"])
        self.assertTrue(order["tests"][0]["ignored"])
        self.assertEqual(len(result["requirements"]["requirements"]), len(result["traceability"]["rows"]))
        self.assertIn("No tests were executed", result["markdown"]["TestCases.md"])
        self.assertEqual(len(result["markdown"]), 8)
        self.assertIn("BRDEvidence.md", result["markdown"])
        self.assertNotIn("BRD.md", result["markdown"])
        self.assertIn("not a business requirements document", result["markdown"]["BRDEvidence.md"])


if __name__ == "__main__":
    unittest.main()