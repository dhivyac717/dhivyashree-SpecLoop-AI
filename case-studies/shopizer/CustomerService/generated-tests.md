# Shopizer Customer Capability Test Cases

Existing evidence and proposed security coverage are separated. This report did not execute tests.

| ID | Requirement | Scenario | Expected result | Current evidence |
| --- | --- | --- | --- | --- |
| TC-CUST-01 | BR-CUST-01, 03 | Register valid customer then log in | Registration/login succeed; auth response contains a token | Existing `registerCustomer` test |
| TC-CUST-02 | BR-CUST-02 | Register same email twice in same store | Conflict; no duplicate account | Add integration test |
| TC-CUST-03 | BR-CUST-01 | Omit required billing country | Validation error; customer not persisted | Add integration test |
| TC-CUST-04 | BR-CUST-03 | Submit invalid credentials | 401; no token issued | Login code maps bad credentials to 401; test absent |
| TC-CUST-05 | BR-CUST-04 | Customer requests another customer's profile/address | Denied; no personal data disclosed | Add authorization integration test |
| TC-CUST-06 | BR-CUST-05 | Same email in separate stores | Behavior matches approved uniqueness scope; no cross-store lookup | Add store-scope test |
| TC-CUST-07 | BR-CUST-06 | Request password reset for existing/non-existing identity | Public response avoids account enumeration; token expires and cannot be reused | Add security tests |
| TC-CUST-08 | BR-CUST-07 | Exercise auth/reset failure paths | Logs and responses omit password, token, and unnecessary PII | Add log/error review |

Only TC-CUST-01 is represented by the reviewed integration test class. Other cases are recommendations, not completed tests.