# Shopizer Case Study User Stories

Status: draft inferred from API behavior; validate actors and outcomes with stakeholders.

- US-ORD-01: As a signed-in shopper, I want to check out my cart so that an order is associated with my account. Acceptance: authenticated route resolves principal/customer and returns a confirmation; cart ownership and repeat submission need explicit tests.
- US-ORD-02: As a guest shopper, I want to submit checkout details for my cart so that I can place an order without signing in. Acceptance: anonymous route requires customer details and a valid cart; guest/account policy needs approval.
- US-CART-01: As a shopper, I want to add products and update quantities so that my cart reflects intended purchases. Acceptance: created/updated cart response reflects line quantities; zero quantity removes a line as covered by the existing test.
- US-CART-02: As a shopper, I want to remove a cart item and optionally see the updated cart. Acceptance: deletion status/body follows the requested response mode.
- US-CUST-01: As a shopper, I want to register and sign in so that I can use customer-scoped storefront features. Acceptance: valid registration/login returns the configured auth response; duplicate and invalid cases need additional tests.

See each case-study story/test artifact for source references and unresolved policy decisions.