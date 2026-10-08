"""Interactive, read-only Shopizer source analysis and artifact preview."""

from __future__ import annotations

import io
import zipfile
from pathlib import Path

import streamlit as st

from agents.pipeline import run_pipeline


DEFAULT_REPOSITORY = Path(__file__).resolve().parents[2] / "shopizer"

st.set_page_config(page_title="SpecLoop-AI | Shopizer", layout="wide")
st.title("SpecLoop-AI / Shopizer")
st.caption("Read-only Java/Maven discovery with evidence-linked SDD artifacts")
st.info("No AI provider is called. Requirements and story seeds describe discovered code, not approved business policy. Tests are inventoried, not executed.")

with st.form("analysis-form"):
	repository_path = st.text_input("Shopizer repository root", value=str(DEFAULT_REPOSITORY))
	start_analysis = st.form_submit_button("Analyze repository", type="primary")

if start_analysis:
	try:
		with st.spinner("Scanning Maven modules, API mappings, and relevant tests..."):
			st.session_state["analysis_result"] = run_pipeline(repository_path)
	except (OSError, ValueError) as error:
		st.session_state.pop("analysis_result", None)
		st.error(str(error))

result = st.session_state.get("analysis_result")
if result:
	source = result["source"]
	capabilities = result["context"]["capabilities"]
	route_count = sum(len(capability["apiRoutes"]) for capability in capabilities)
	existing_tests = result["tests"]["existingTests"]
	ignored_count = sum(test["ignored"] for test in existing_tests)
	st.success(f"Analysis complete for {source['source'] if 'source' in source else source['repository']}")
	st.caption(f"Git revision: {source['revision'] or 'unavailable'} | Java {source['project']['javaVersion']} | Spring Boot {source['project']['springBootVersion']}")

	metric_columns = st.columns(4)
	metric_columns[0].metric("Maven modules", len(source["project"]["modules"]))
	metric_columns[1].metric("API mappings", route_count)
	metric_columns[2].metric("Test files", len(existing_tests))
	metric_columns[3].metric("Ignored/disabled", ignored_count)

	archive = io.BytesIO()
	with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as package:
		for filename, content in result["markdown"].items():
			package.writestr(filename, content)
	st.download_button(
		"Download all artifacts (.zip)",
		data=archive.getvalue(),
		file_name="shopizer-analysis-artifacts.zip",
		mime="application/zip",
	)

	with st.expander("Download individual Markdown files"):
		for filename, content in result["markdown"].items():
			st.download_button(
				f"Download {filename}",
				data=content,
				file_name=filename,
				mime="text/markdown",
				key=f"download-{filename}",
			)

	tabs = st.tabs([
		"Overview",
		"BRD",
		"SDD",
		"Requirements & stories",
		"Tests",
		"Traceability",
		"Modernization",
	])
	with tabs[0]:
		st.markdown("### Discovered capabilities")
		for capability in capabilities:
			with st.expander(f"{capability['name']} ({len(capability['apiRoutes'])} API mappings)"):
				for route in capability["apiRoutes"]:
					st.markdown(f"- `{route['method']} {route['path']}`  ")
					st.caption(f"{route['source']}#L{route['line']}")
		st.markdown("### Source analysis")
		st.markdown(result["markdown"]["SourceAnalysis.md"])
	with tabs[1]:
		st.markdown(result["markdown"]["BRD.md"])
	with tabs[2]:
		st.markdown(result["markdown"]["SDD.md"])
	with tabs[3]:
		st.markdown(result["markdown"]["FunctionalRequirements.md"])
		st.divider()
		st.markdown(result["markdown"]["UserStories.md"])
	with tabs[4]:
		st.markdown(result["markdown"]["TestCases.md"])
	with tabs[5]:
		st.markdown(result["markdown"]["TraceabilityMatrix.md"])
	with tabs[6]:
		st.markdown(result["markdown"]["ModernizationAssessment.md"])
else:
	st.markdown("### Analyze a Shopizer checkout")
	st.write("Choose the root of a Shopizer Maven repository and run a local source scan. The analyzer never modifies the selected repository.")