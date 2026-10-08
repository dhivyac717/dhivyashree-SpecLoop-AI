# Shopizer Order Flow User Stories

Status: draft inferred from the API; confirm with product owners.

## Stories

### US-ORD-01: Authenticated checkout

As a signed-in shopper, I want to submit checkout details for my cart so that I can place an order tied to my account.

Acceptance criteria: the request uses the authenticated checkout route; the customer is resolved from the principal; an unknown cart is rejected; success returns an order confirmation for the created order. Define ownership and repeat-submit behavior with the team.

### US-ORD-02: Guest checkout

As a guest shopper, I want to check out with the required customer details so that I can place an order without first signing in.

Acceptance criteria: the anonymous route requires customer details and a valid cart; duplicate registered email behavior is explicit; success returns the created order confirmation. Confirm guest identity and password policy with product/security owners.

### US-ORD-03: Store operator order lookup

As an authorized store operator, I want to list and view orders in my store so that I can support fulfillment.

Acceptance criteria: access is authorized for the operator and scoped to the selected store; pagination and not-found behavior are documented. Validate against the private order endpoints and security configuration.