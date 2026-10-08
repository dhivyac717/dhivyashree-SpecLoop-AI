# Shopizer Case Study Test Cases

Status: a mix of existing test evidence and recommendations; this analysis did not execute the Shopizer test suite.

## Existing Coverage

- Cart: `ShoppingCartAPIIntegrationTest` covers new cart creation, adding another item, invalid cart code, multi-item updates, quantity zero, deletion without body, and deletion with body.
- Customer: `CustomerRegistrationIntegrationTest` covers registration followed by login and token presence.
- Order: `OrderApiIntegrationTest` is annotated `@Ignore`; `createOrder()` does not submit checkout or assert a result.

## Highest-Priority Additions

- Authenticated and anonymous successful checkout, unknown cart, customer/store mismatch, duplicate guest email, payment failure, and confirmation mapping.
- Cart cross-customer/store access, invalid quantity/product behavior, merge behavior, and test isolation.
- Customer duplicate registration, missing required address, invalid login, cross-customer access, token/reset expiry and reuse, and sensitive-data redaction.

Detailed IDs and expected results are in each service's `generated-tests.md`. Proposed cases are not passing tests.