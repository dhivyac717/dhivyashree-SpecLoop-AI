# Shopizer Order Flow Source Analysis

Status: code-derived analysis; business policy and checkout guarantees require stakeholder and owner review. Source was inspected from the current Shopizer workspace; record the commit SHA before treating this as a reproducible baseline.

## Scope and Source Locations

- `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java`: order listing and authenticated/anonymous checkout endpoints under `/api/v1`.
- `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java`: initializes orders, prepares totals/payment, delegates processing, and associates the processed order with the cart.
- `sm-shop/src/main/java/com/salesmanager/shop/store/facade/order/OrderFacadeImpl.java`: shapes the v1 order confirmation, including customer addresses, totals, products, shipping label, payment type, and order ID.
- `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderService.java`: core order operations, total calculation, order processing, invoice generation, and capturable-order queries.
- `sm-core-model/src/main/java/com/salesmanager/core/model/order/Order.java` and `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/`: domain and API models.
- `sm-shop/src/test/java/com/salesmanager/test/shop/integration/order/OrderApiIntegrationTest.java`: present order API test is `@Ignore`; its `createOrder` method only creates a sample cart and has no assertions or checkout request.

## Observed Behavior

1. Authenticated checkout is `POST /api/v1/auth/cart/{code}/checkout`. It resolves the principal to a customer, resolves the cart by code and merchant store, sets the cart/customer IDs on the request, processes the order, and returns a readable confirmation. Errors are caught and reported as a service-unavailable response.
2. Anonymous checkout is `POST /api/v1/cart/{code}/checkout`. It requires a customer payload, resolves the cart, optionally validates a supplied password/repeat-password pair, rejects an already-registered email when a password is supplied, then processes the order and builds a confirmation.
3. Order confirmation maps products and totals, sorts totals by sort order, selects the `order.total.total` entry as grand total when present, and includes the order ID. Shipping display text is localized from the shipping module code when available.
4. `OrderService` exposes total calculations and processing with payment/transaction variants. The storefront facade coordinates cart, pricing, shipping, payment, customer, and order services.

## Dependencies and Data

The flow crosses storefront API, facade, core order/cart/customer services, payment and shipping modules, and order/cart models. The cart is located using its code and store. The order contains customer, product, total, payment, shipping, and status-related data; verify persistence and transaction guarantees in the concrete service implementation before making stronger claims.

## Unknowns and Risks

- End-to-end checkout behavior is not currently demonstrated by the ignored, incomplete order integration test.
- Confirm checkout idempotency, cart reuse/consumption rules, inventory reservation, payment failure recovery, and transaction boundaries with maintainers.
- Confirm whether service errors should consistently map to 503 and which error details are safe to expose.
- Business rules for guest account creation and email/password handling need product/security review.