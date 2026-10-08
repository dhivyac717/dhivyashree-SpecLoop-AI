# Business Requirements: Shopizer Case Study

Status: draft synthesized from source code; not stakeholder-approved. See service-level BRDs for detailed evidence.

## Business Context

The case study examines Shopizer storefront order checkout, shopping-cart operations, and customer identity capabilities. API and test evidence establishes current software behavior, not business policy or desired outcomes.

## Draft Requirements

- BR-ORD-01/02: Support the existing authenticated and anonymous checkout paths for valid carts.
- BR-ORD-03: Return the existing order-confirmation data for successful checkout.
- BR-CART-01/02/03: Create carts and add, update, or remove cart lines through the storefront API.
- BR-CART-05: Restrict authenticated cart retrieval to the authorized customer and store context.
- BR-CUST-01/02/03: Register and authenticate customers with store-scoped duplicate checks.
- BR-CUST-04/05: Protect customer profile operations and keep them correctly scoped.
- BR-CUST-06/07: Apply reviewed password-recovery and privacy requirements before treating these as acceptance criteria.

## Approval and Evidence

Stakeholders and acceptance measures remain unconfirmed. Source-derived capabilities and proposed security expectations are distinguished in `case-studies/shopizer/*/generated-brd.md`. Do not use this document as an approved business contract until reviewed.