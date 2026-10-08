# Shopizer Customer Capabilities Software Design Description

Status: describes inspected code paths; privacy/security requirements need formal review.

## Scope

Storefront customer registration, login, authenticated customer operations, and password recovery.

## Existing Architecture

`AuthenticateCustomerApi` and `CustomerApi` are REST controllers in `sm-shop` under `/api/v1`. They delegate to customer facades and core `CustomerService`. Authentication uses Spring Security and JWT-related services; the facade maps customer/address DTOs and coordinates email and cart merge where required.

## Interfaces and Data

- `POST /customer/register`: validated customer payload, store/language context, registration plus authentication response.
- `POST /customer/login`: username/password authentication; successful response contains customer identifier/token; bad credentials map to 401.
- `/auth/customer/...`: authenticated profile, address, refresh, and password-related operations.
- `/private/customer...`: operator/private customer administration routes.

Customer records include identifying and address data. Minimize fields in reports, fixtures, logs, and generated artifacts.

## Security and Failure Handling

Registration uses email as username and performs a store-scoped duplicate lookup. Authenticated facade authorization compares principal name and customer nickname. Verify that every customer route applies equivalent authorization and store scoping. Confirm JWT/password/reset token policy from configuration; do not infer that a route's presence proves security controls are sufficient.

## Verification Strategy

Extend `CustomerRegistrationIntegrationTest` with duplicate registration, missing country/address validation, bad password, cross-customer profile/address access, cross-store isolation, token expiry/refresh, reset-token expiry/reuse, and privacy-safe error/log assertions. Use synthetic data only.