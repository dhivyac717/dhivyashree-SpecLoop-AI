# Shopizer Order Flow Test Cases

Status: proposed cases; no new tests were executed for this report.

| ID | Requirement | Scenario | Expected result | Existing evidence |
| --- | --- | --- | --- | --- |
| TC-ORD-01 | BR-ORD-01 | Authenticated customer checks out a valid cart | Success confirmation identifies created order and includes mapped products/totals | No active checkout integration test found |
| TC-ORD-02 | BR-ORD-02 | Guest checks out with valid customer and cart details | Success confirmation; guest/account behavior matches approved policy | No active checkout integration test found |
| TC-ORD-03 | BR-ORD-04 | Checkout references unknown cart code | Not-found/client-safe error; no order created | No active checkout integration test found |
| TC-ORD-04 | BR-ORD-05 | Authenticated customer attempts checkout against another customer's cart | Request is rejected; no cross-customer order is created | Security behavior needs a focused test |
| TC-ORD-05 | BR-ORD-05 | Cart code belongs to another merchant store | Request is rejected; no cross-store order is created | Store context is passed to cart lookup; test absent |
| TC-ORD-06 | BR-ORD-06 | Payment or order service fails | Documented error response, no misleading confirmation, state is recoverable | Error mapping/transaction behavior needs verification |
| TC-ORD-07 | BR-ORD-03 | Successful order has totals, products, addresses, shipping and payment values | Confirmation maps available fields and computes grand-total display as implemented | Mapper exists; end-to-end assertion absent |
| TC-ORD-08 | BR-ORD-02 | Guest supplies an email already registered with password flow | Conflict behavior is returned; no unintended account/order mutation | Branch exists; focused assertion absent |

Existing test status: `OrderApiIntegrationTest` is `@Ignore`; `createOrder()` has no checkout call or assertions. These cases are recommendations, not completed tests.