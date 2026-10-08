# Azure OpenAI Design for Shopizer Analysis (Exploratory)

Status: option study only. No Azure OpenAI resource, model, endpoint, or connection is configured.

## Candidate Use

If approved, use a model only to draft summaries and artifacts from a curated evidence inventory of Shopizer order, cart, and customer code. Deterministic discovery and source references remain the authority.

## Identity, Network, and Secrets

Use managed identity where supported, private/network-restricted access where required, and managed secret storage. Never put API keys in source, sample JSON, prompts, or screenshots. Restrict repository access to approved users.

## Data Handling and Safety

Shopizer source may be proprietary and customer modules concern PII/authentication. Obtain data-owner approval and review provider retention/training terms before sending any source or prompts externally. Redact credentials, tokens, personal data, and payment data. Keep generated claims tied to source evidence and human review.

## Evaluation and Cost

No token cost or benefit is measured. Before adoption, evaluate source-reference accuracy, unsupported-claim rate, reviewer corrections, latency, and cost on a fixed synthetic/approved test set.