# Shopizer Shopping Cart Source Analysis

Status: code-derived analysis; record the source commit SHA before using as a reproducible baseline.

## Scope and Source Locations

- `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java`: `/api/v1` cart endpoints.
- `sm-shop/src/main/java/com/salesmanager/shop/store/facade/shoppingCart/ShoppingCartFacadeImpl.java`: customer cart lookup and optional session-cart merge.
- `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartService.java`: cart lookup, save, remove, merge, shipping products, and item operations.
- `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java` and `ShoppingCartItem.java`; API view types are in `sm-shop-model`.
- `sm-shop/src/test/java/com/salesmanager/test/shop/integration/cart/ShoppingCartAPIIntegrationTest.java`: ordered API integration scenarios.

## Observed Behavior

- `POST /api/v1/cart` creates a cart from a product/quantity item and returns HTTP 201.
- `PUT /api/v1/cart/{code}` adds or modifies an item; the API returns 201 when a cart is returned and 404 when facade returns null.
- `POST /api/v1/cart/{code}/multi` applies multiple item quantity changes and returns 201.
- `GET /api/v1/cart/{code}` retrieves a cart by code; missing cart is reported as 404.
- `DELETE /api/v1/cart/{code}/product/{sku}` removes an item; optional `body=true` returns the remaining cart.
- Authenticated cart retrieval is `GET /api/v1/auth/customer/cart`. The facade resolves the customer from the principal, authorizes it, then loads/merges a customer cart.
- The older customer-ID cart routes are deprecated; adding a cart through the deprecated route throws `OperationNotAllowedException`.
- Integration tests cover create, add second item, bad cart code, multi-update, quantity zero, and deletion response modes.

## Dependencies and Data

Cart API depends on product/quantity input, merchant store and language context, cart facade/core service, and optionally authenticated customer state. A cart has a code used by API callers; cart lines carry product and quantity. Cart merge and persistence semantics should be confirmed in concrete implementations.

## Unknowns

The ordered integration tests share mutable static test data; verify isolation and repeatability. Review validation for zero/negative/large quantities, product availability, concurrent updates, expiration, guest-to-customer merge conflicts, and cross-store code use.