# Shopizer Shopping Cart Software Design Description

Status: describes inspected endpoints; not a proposal to change behavior.

## Scope

Storefront cart operations and their handoff to authenticated customer state.

## Existing Architecture

`ShoppingCartApi` (`sm-shop`, base path `/api/v1`) delegates operations to cart facades and the core `ShoppingCartService`. `ShoppingCartFacadeImpl` loads a customer by ID and store, retrieves the persisted cart, optionally merges a supplied session cart, then maps to `ReadableShoppingCart`.

## Interfaces and Data

- `POST /cart`: create from `PersistableShoppingCartItem`.
- `PUT /cart/{code}`: add/update a line.
- `POST /cart/{code}/multi`: apply multiple line updates.
- `GET /cart/{code}`: retrieve by cart code.
- `DELETE /cart/{code}/product/{sku}?body={boolean}`: remove a line and optionally return remaining cart.
- `GET /auth/customer/cart`: resolve authenticated principal and return the authorized customer cart.

The older `/customers/{id}/cart` and `/auth/customer/{id}/cart` routes are deprecated; one deprecated mutation explicitly throws `OperationNotAllowedException`.

## Security and Failure Handling

Customer cart retrieval checks the principal through the customer facade. Store and language are request context for storefront operations. Treat cart codes as identifiers, not authorization tokens; verify access control for every operation that accepts a code. Existing API maps missing carts to 404 in read/update paths.

## Verification Strategy

The existing `ShoppingCartAPIIntegrationTest` exercises create (201), add/update (201), invalid cart code (404), multi-update, quantity zero, delete (204), and delete-with-body (200). Add focused tests for principal/cart mismatch, store isolation, invalid SKU/quantity, concurrent updates, merge behavior, and repeatable test data. Validate test ordering and static shared state.