# Shopizer Case Study: Solution Architecture

Status: source-informed architecture view, not a complete deployment architecture.

## Context and Scope

Shopizer is the analyzed target; SpecLoop-AI is a separate proposed analysis tool. The Shopizer root Maven POM aggregates `sm-core-model`, `sm-core-modules`, `sm-core`, `sm-shop-model`, and `sm-shop`, targets Java 11, and inherits Spring Boot 2.5.12.

## Shopizer Components Observed

- `sm-shop`: storefront application and `/api/v1` REST endpoints.
- `sm-core`: business service contracts/implementations, including order, shopping-cart, and customer services.
- `sm-core-model`: core commerce models such as order, cart, and customer.
- `sm-shop-model`: storefront/API request and response models.
- `sm-core-modules`: shared business modules; exact runtime dependencies vary by workflow.

The order flow in the inspected code delegates from `OrderApi` through a storefront facade to core `OrderService`, with cart, customer, pricing, payment, and shipping collaborators. Cart and customer flows have separate storefront API/facade paths.

## SpecLoop-AI Components

Read-only repository discovery -> evidence inventory -> deterministic capability artifacts -> Streamlit preview/download. An optional Azure OpenAI adapter drafts BRD requirements from analyst context and route/source-reference metadata after per-run consent. The default path makes no provider call. No database, code-generation agent, Shopizer test runner, or drift service is implemented.

## Interfaces and Dependencies

Shopizer API routes are evidence inputs; this project does not currently invoke Shopizer endpoints. Keep the analysis boundary read-only and avoid requiring a running Shopizer service for static discovery.

## Quality Attributes

Traceability, source-revision reproducibility, privacy, explainable confidence, and human approval take precedence over autonomous generation. Validate architecture claims against source before presenting them as complete.