# Semantic Kernel Flow for Shopizer (Exploratory)

Status: proposed option; Semantic Kernel is not installed or used by the current demo.

## Candidate Flow

1. A read-only discovery component indexes Shopizer module/API/service/test references.
2. A kernel receives only the approved evidence records for one capability (order, cart, or customer).
3. Separate drafting functions produce BRD, SDD, and test suggestions with evidence IDs.
4. A deterministic validator checks required fields and trace links.
5. A human reviews and approves before documents are consolidated.

## Plugin Boundaries

Potential plugins should be read-only for source discovery and have no payment, customer, database-write, or deployment actions. No plugin contracts are implemented yet.

## Validation and Human Review

Reject claims lacking an evidence reference; preserve uncertainty and distinguish existing tests from suggestions. Provider, model, prompt versioning, persistence, and review UI remain undecided.