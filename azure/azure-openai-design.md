# Azure OpenAI Design for Shopizer Analysis

Status: optional BRD-drafting adapter implemented. No Azure endpoint, deployment, or credentials are configured in the repository or current demo environment.

## Candidate Use

When explicitly enabled, the adapter drafts BRD statements from analyst-entered context and a curated list of Shopizer route/source-reference metadata. It does not send Java file contents. The adapter accepts only citations from the supplied evidence list; deterministic discovery remains the authority for source facts.

## Identity, Network, and Secrets

The local prototype reads `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_DEPLOYMENT`, and optional `AZURE_OPENAI_API_VERSION` from the process environment. Do not commit these values. Production use should prefer managed identity where supported, private/network-restricted access where required, and managed secret storage. Restrict repository access to approved users.

## Data Handling and Safety

Shopizer source may be proprietary and customer modules concern PII/authentication. Obtain data-owner approval and review provider retention/training terms before sending any source or prompts externally. Redact credentials, tokens, personal data, and payment data. Keep generated claims tied to source evidence and human review.

## Evaluation and Cost

No token cost or benefit is measured. Before adoption, evaluate source-reference accuracy, unsupported-claim rate, reviewer corrections, latency, and cost on a fixed synthetic/approved test set.