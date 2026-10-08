# Shopizer Case Study Functional Requirements

Status: code-derived draft. IDs correspond to details in the service-level BRDs; business acceptance remains subject to review.

## Order

- BR-ORD-01: Accept authenticated checkout for an existing cart and resolve the customer from the principal.
- BR-ORD-02: Accept anonymous checkout with the required customer data and an existing cart.
- BR-ORD-03: Return order confirmation fields mapped by the current implementation.
- BR-ORD-04: Reject an unknown cart code.

## Shopping Cart

- BR-CART-01: Create a cart by adding a product and quantity.
- BR-CART-02: Add/update one or multiple cart lines; quantity zero removes a line in the tested scenario.
- BR-CART-03: Remove a cart product, optionally returning the resulting cart.
- BR-CART-04: Retrieve a cart by code and report unknown carts.
- BR-CART-05: Resolve authenticated cart access for the principal and store context.

## Customer

- BR-CUST-01/02: Register with required billing-country data and check duplicate username within store context.
- BR-CUST-03: Authenticate a registered user and return the configured auth response.
- BR-CUST-04/05: Enforce customer authorization and store scoping for private/profile operations.

Security/privacy requirements BR-ORD-05/06, BR-CART-06, and BR-CUST-06/07 are proposals requiring owner review and additional test evidence.