# Shopizer Customer Source Analysis

Status: code-derived analysis. Record the source commit SHA for repeatable review; customer-data policy requires owner validation.

## Scope and Source Locations

- `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/customer/AuthenticateCustomerApi.java`: registration, login, token refresh, and password operations.
- `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/customer/CustomerApi.java`: private customer management and authenticated profile/address routes.
- `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java`: customer persistence, duplicate checks, cart merge, and customer model mapping.
- `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java`: v1 authorization and password-reset orchestration.
- `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerService.java`: customer lookups and store-scoped listing/persistence contract.
- `sm-shop/src/test/java/com/salesmanager/test/shop/integration/customer/CustomerRegistrationIntegrationTest.java`: registration followed by login and token assertion.

## Observed Behavior

- `POST /api/v1/customer/register` sets username from email, checks for an existing username in the merchant store, requires billing data and country, registers the customer, authenticates it, and returns an authentication response.
- `POST /api/v1/customer/login` authenticates submitted username/password and returns a JWT response on success; bad credentials map to 401.
- Registration integration test submits a customer with billing country and then logs in, asserting successful responses and a non-null token.
- Customer management exposes private create/update/list/read/delete routes and authenticated profile/address/update/delete routes.
- The v1 customer facade's `authorize` method compares principal name to customer nickname and throws unauthorized on mismatch.
- Password-reset flow generates a UUID token, stores an expiry two days from current date, and builds a reset link; details should be verified against current security requirements.

## Dependencies and Data

The customer API depends on authentication/JWT services, password encoding, merchant-store context, customer service, address/country/zone conversion, email, and optional shopping-cart merge. Customer identity is store-scoped in duplicate checking. Customer models carry PII and credentials-related fields; never copy real customer data into demo fixtures.

## Unknowns and Risks

- Review password policy, token signing/expiry/refresh configuration, reset-token invalidation, rate limiting, and account enumeration protections.
- Confirm uniqueness constraints and concurrency behavior for same email/store registration.
- The registration test uses a simple test-only password; do not reuse sample credentials outside tests.
- Customer API authorization requires tests for cross-customer and cross-store access, not only successful registration/login.