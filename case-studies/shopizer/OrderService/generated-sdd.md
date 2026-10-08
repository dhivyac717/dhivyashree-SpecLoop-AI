# Shopizer Order Flow Software Design Description

Status: describes the inspected implementation; proposed guarantees need review.

## Scope

Document storefront checkout from cart code through order creation and confirmation. This is not a redesign proposal.

## Existing Architecture

`OrderApi` (`sm-shop`, `/api/v1`) dispatches to the order facade. The facade validates/converts request data, obtains cart items, coordinates pricing, shipping and payment dependencies, calls core `OrderService`, then links the persisted order to the cart. The v1 response facade maps the result to a readable confirmation.

## Existing Interfaces and Data

- Authenticated: `POST /api/v1/auth/cart/{code}/checkout`, request `PersistableOrder`.
- Anonymous: `POST /api/v1/cart/{code}/checkout`, request `PersistableAnonymousOrder` with a customer payload.
- Both paths resolve `{code}` against the current `MerchantStore`.
- Confirmation includes order ID, products, totals, billing/delivery, and available shipping/payment labels.

## Security and Failure Handling

The authenticated route uses the request principal to resolve the customer. The anonymous route has distinct account/credential logic; do not assume authentication or guest-account policy beyond the implementation. The authenticated handler currently catches broad exceptions and maps them through `sendError(503, ...)`; define and test a stable error contract before changing it. Avoid logging or returning credentials/payment data.

## Verification Strategy

Replace/enable `OrderApiIntegrationTest` with API-level cases for guest and authenticated checkout, cart ownership/store mismatch, missing cart, duplicate email, invalid customer/address data, payment failures, response mapping, and repeat submission. Assert persisted order/cart linkage and transaction behavior using the existing test fixtures. Existing test is `@Ignore` and does not submit a checkout request.