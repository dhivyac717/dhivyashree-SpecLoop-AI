"""Interactive, read-only Shopizer source analysis and artifact preview."""

from __future__ import annotations

import io
import zipfile
from pathlib import Path

import streamlit as st

from agents.pipeline import run_pipeline
from agents.azure_openai_brd import AzureOpenAIError, generate_brd_draft


DEFAULT_REPOSITORY = Path(__file__).resolve().parents[2] / "shopizer"

st.set_page_config(page_title="SpecLoop-AI | Shopizer", layout="wide")
st.title("SpecLoop-AI / Shopizer")
st.caption("Read-only Java/Maven discovery with evidence-linked SDD artifacts")
st.info("AI drafting is optional and off by default. The local evidence scan never transmits source code. Drafts require human review; tests are inventoried, not executed.")

with st.form("analysis-form"):
	repository_path = st.text_input("Shopizer repository root", value=str(DEFAULT_REPOSITORY))
	with st.expander("Optional Azure OpenAI BRD draft (off by default)"):
		allow_ai_draft = st.checkbox(
			"I confirm organizational approval and consent for this run: send my business context and discovered route/source-reference metadata to the configured Azure OpenAI deployment.",
			value=False,
		)
		business_context = st.text_area(
			"Business context for the BRD draft",
			max_chars=3000,
			help="Do not enter customer data, credentials, tokens, payment details, or other secrets.",
		)
		st.caption("Only your written context and route/source-reference metadata are sent; Java file contents and API keys are not included in the prompt. Do not paste source code, customer data, or secrets. Configure the endpoint, deployment, API version, and API key in the environment before starting Streamlit.")
	start_analysis = st.form_submit_button("Analyze repository", type="primary")

if start_analysis:
	try:
		with st.spinner("Scanning Maven modules, API mappings, and relevant tests..."):
			analysis_result = run_pipeline(repository_path)
		if allow_ai_draft:
			try:
				analysis_result["ai_brd"] = generate_brd_draft(
					business_context,
					analysis_result["requirements"],
				)
				analysis_result["markdown"]["AIAssistedBRD.md"] = analysis_result["ai_brd"]["markdown"]
			except AzureOpenAIError as error:
				analysis_result["ai_brd_error"] = str(error)
		st.session_state["analysis_result"] = analysis_result
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
	if result.get("ai_brd_error"):
		st.warning(f"AI draft was not generated. The deterministic artifacts are still available. {result['ai_brd_error']}")
	elif result.get("ai_brd"):
		st.success("AI-assisted BRD draft generated. It is unapproved and must be reviewed.")

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
		"BRD Evidence",
		"AI BRD Draft",
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
		st.markdown(result["markdown"]["BRDEvidence.md"])
	with tabs[2]:
		if result.get("ai_brd"):
			st.markdown(result["ai_brd"]["markdown"])
		else:
			st.info("No business-requirement draft was generated. Review the BRD evidence and, if approved, enable the optional Azure OpenAI draft on a new analysis run.")
	with tabs[3]:
		st.markdown(result["markdown"]["SDD.md"])
	with tabs[4]:
		st.markdown(result["markdown"]["FunctionalRequirements.md"])
		st.divider()
		st.markdown(result["markdown"]["UserStories.md"])
	with tabs[5]:
		st.markdown(result["markdown"]["TestCases.md"])
	with tabs[6]:
		st.markdown(result["markdown"]["TraceabilityMatrix.md"])
	with tabs[7]:
		st.markdown(result["markdown"]["ModernizationAssessment.md"])
else:
	st.markdown("### Analyze a Shopizer checkout")
	st.write("Choose the root of a Shopizer Maven repository and run a local source scan. The analyzer never modifies the selected repository.")