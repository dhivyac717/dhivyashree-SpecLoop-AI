# Shopizer Analysis Data Flow

Status: documents the current static-analysis flow and future provider/persistence boundaries.

## Data Sources

Read-only Shopizer source at a recorded commit: Java modules, Maven descriptors, REST endpoints, service contracts, models, and tests. Case-study outputs are derived documents, not runtime commerce data.

## Processing and Storage

Repository discovery -> source evidence records -> draft artifacts -> in-memory preview and user download. Reviewer approval and persistent baselines are future work. Current sample JSON contains synthetic source references and behavioral summaries only. No database or telemetry store is configured.

## Trust Boundaries and Sensitive Data

Source and build files may contain internal implementation details; customer/authentication modules concern PII and credentials. Apply read-only least privilege, redact secrets, avoid real customer records, and do not transmit source externally until provider/data terms are approved.

## Retention and Deletion

Retention, access control, encryption, and deletion policy remain undecided. Before deployment, define where source snapshots, prompts, model responses, and generated artifacts are stored and how they are removed.