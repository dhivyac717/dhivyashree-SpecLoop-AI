"""Read-only discovery of Shopizer Maven modules, API routes, and tests."""

from __future__ import annotations

import re
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path


_CAPABILITY_PATTERNS = {
    "OrderService": re.compile(r"order", re.IGNORECASE),
    "ShoppingCartService": re.compile(r"shopping.?cart|cart", re.IGNORECASE),
    "CustomerService": re.compile(r"customer|authenticatecustomer", re.IGNORECASE),
}
_MAPPING = re.compile(
    r"@(Get|Post|Put|Delete|Patch)Mapping\s*(?:\((.*?)\))?"
    r"|@RequestMapping\s*\((.*?)\)",
    re.DOTALL,
)


def _local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _children_text(element: ET.Element, child_name: str) -> str | None:
    for child in element:
        if _local_name(child.tag) == child_name and child.text:
            return child.text.strip()
    return None


def _mapping_path(arguments: str) -> str | None:
    named_path = re.search(r"(?:value|path)\s*=\s*\{?\s*\"([^\"]+)\"", arguments)
    if named_path:
        return named_path.group(1)
    positional_path = re.match(r"\s*\"([^\"]+)\"", arguments)
    return positional_path.group(1) if positional_path else None


def _class_base_path(source: str) -> str:
    class_match = re.search(r"@RequestMapping\s*\((.*?)\)\s*(?:@[\w.]+(?:\([^)]*\))?\s*)*public\s+class", source, re.DOTALL)
    if not class_match:
        return ""
    return _mapping_path(class_match.group(1)) or ""


def _api_routes(source_path: Path, source: str, repository: Path) -> list[dict]:
    base_path = _class_base_path(source)
    routes = []
    for match in _MAPPING.finditer(source):
        annotation = match.group(1)
        arguments = match.group(2) if annotation else match.group(3)
        if not arguments:
            continue
        route_path = _mapping_path(arguments)
        if route_path is None:
            continue
        if annotation:
            method = annotation.upper()
        else:
            method_match = re.search(r"RequestMethod\.(GET|POST|PUT|DELETE|PATCH)", arguments)
            if not method_match:
                continue
            method = method_match.group(1)
        full_path = "/".join(part.strip("/") for part in (base_path, route_path) if part)
        routes.append({
            "method": method,
            "path": f"/{full_path}" if full_path else "/",
            "source": source_path.relative_to(repository).as_posix(),
            "line": source.count("\n", 0, match.start()) + 1,
        })
    return routes


def _git_revision(repository: Path) -> str | None:
    result = subprocess.run(
        ["git", "-C", str(repository), "rev-parse", "--short", "HEAD"],
        capture_output=True,
        text=True,
        check=False,
    )
    return result.stdout.strip() if result.returncode == 0 else None


def _project_metadata(repository: Path) -> dict:
    pom_path = repository / "pom.xml"
    if not pom_path.is_file():
        raise ValueError(f"No pom.xml found at repository root: {repository}")
    try:
        pom = ET.parse(pom_path).getroot()
    except ET.ParseError as error:
        raise ValueError(f"Could not parse root pom.xml: {error}") from error

    modules = []
    properties = {}
    for element in pom.iter():
        local_name = _local_name(element.tag)
        if local_name == "module" and element.text:
            modules.append(element.text.strip())
        elif local_name == "properties":
            for property_element in element:
                properties[_local_name(property_element.tag)] = (property_element.text or "").strip()

    parent = next((element for element in pom if _local_name(element.tag) == "parent"), None)
    return {
        "name": _children_text(pom, "artifactId") or repository.name,
        "version": _children_text(pom, "version"),
        "javaVersion": properties.get("java.version"),
        "springBootVersion": _children_text(parent, "version") if parent is not None else None,
        "modules": modules,
    }


def _is_relevant_test(path: Path) -> bool:
    return bool(
        re.search(r"(order|cart|customer).*?(test|tests|it)\.java$", path.name, re.IGNORECASE)
        or re.search(r"(test|tests|it).*?(order|cart|customer).*\.java$", path.name, re.IGNORECASE)
    )


def _test_summary(path: Path, source: str, repository: Path) -> dict:
    ignored = bool(re.search(r"@(Ignore|Disabled)\b", source))
    test_annotations = len(re.findall(r"@Test\b", source))
    methods = re.findall(r"@Test(?:\s*\([^)]*\))?\s+(?:public\s+)?(?:void|\w+)\s+(\w+)\s*\(", source)
    return {
        "name": path.name,
        "source": path.relative_to(repository).as_posix(),
        "status": "ignored/disabled" if ignored else "declared; execution not verified",
        "ignored": ignored,
        "testAnnotationCount": test_annotations,
        "testMethods": methods,
    }


def run(repository_path: str) -> dict:
    """Discover project metadata and evidence for the three Shopizer case studies."""
    repository = Path(repository_path).expanduser().resolve()
    if not repository.is_dir():
        raise ValueError(f"Repository path is not a directory: {repository}")

    metadata = _project_metadata(repository)
    source_files = []
    test_files = []
    for module in metadata["modules"]:
        module_root = repository / module
        source_root = module_root / "src" / "main" / "java"
        test_root = module_root / "src" / "test" / "java"
        if source_root.is_dir():
            source_files.extend(source_root.rglob("*.java"))
        if test_root.is_dir():
            test_files.extend(path for path in test_root.rglob("*.java") if _is_relevant_test(path))

    capabilities = {}
    for capability_name, pattern in _CAPABILITY_PATTERNS.items():
        matched_sources = [path for path in source_files if pattern.search(path.name) or pattern.search(path.as_posix())]
        matched_tests = [path for path in test_files if pattern.search(path.name) or pattern.search(path.as_posix())]
        routes = []
        for source_path in matched_sources:
            if source_path.name.endswith("Api.java"):
                source = source_path.read_text(encoding="utf-8", errors="replace")
                routes.extend(_api_routes(source_path, source, repository))
        tests = [
            _test_summary(path, path.read_text(encoding="utf-8", errors="replace"), repository)
            for path in matched_tests
        ]
        capabilities[capability_name] = {
            "sourceFiles": [path.relative_to(repository).as_posix() for path in matched_sources],
            "apiRoutes": routes,
            "tests": tests,
        }

    return {
        "repository": str(repository),
        "revision": _git_revision(repository),
        "project": metadata,
        "capabilities": capabilities,
        "analysisStatus": "read-only static discovery; tests were not executed",
    }