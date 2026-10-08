# Copilot Agent Workflow for Shopizer Case Studies

Status: proposed future workflow documentation; the current project is configured with Copilot Spec Kit skills, while the local deterministic pipeline does not invoke Copilot agents.

## Suggested Roles

Use separate reviewable tasks for source discovery, order/cart/customer analysis, requirement/design drafting, test-gap analysis, traceability, and modernization review. Source discovery remains deterministic. A separate Azure OpenAI BRD adapter runs only after per-run consent and configured credentials; it does not modify application code.

## Inputs and Permissions

Pin the Shopizer source revision and grant read-only access to relevant modules/tests. Exclude secrets and real customer records. Require user confirmation before any external model processing or modification of generated outputs.

## Review and Traceability

Every behavior claim should cite Shopizer paths/symbols; inferred business requirements need owner approval; test proposals must be labeled unexecuted. The order checkout test gap and selective cart/customer coverage must be surfaced to reviewers.