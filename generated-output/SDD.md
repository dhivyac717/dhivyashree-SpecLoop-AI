# Software Design Description: Shopizer Case Study

Status: describes inspected implementation boundaries; not a redesign or approved target architecture.

## System Context

Shopizer is a Java 11 Maven multi-module application; storefront REST endpoints are in `sm-shop`, core services in `sm-core`, and commerce models in `sm-core-model`/`sm-shop-model`. Root parent is Spring Boot 2.5.12.

## Order Flow

`OrderApi` exposes authenticated and anonymous cart checkout under `/api/v1`. It resolves the cart for merchant-store context and delegates checkout to the storefront order facade, which coordinates cart items, customer, pricing, shipping, payment, and core `OrderService`. A response facade maps the readable confirmation.

## Cart and Customer Flows

`ShoppingCartApi` exposes cart line operations and authenticated customer-cart retrieval. `AuthenticateCustomerApi` provides registration/login, while `CustomerApi` exposes private and authenticated profile operations. Facades bridge API models to core services.

## Constraints and Gaps

Current API and test details are documented in the individual case SDDs. The order integration test is ignored/incomplete. This document does not establish transaction guarantees, deployment topology, or security sufficiency. Preserve external API compatibility unless an explicit change is approved.