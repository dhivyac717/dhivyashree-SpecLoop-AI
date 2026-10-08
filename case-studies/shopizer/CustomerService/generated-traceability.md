# Shopizer Customer Capability Traceability

Status: initial code mapping; security/privacy criteria require owner approval and test execution.

| Requirement | Source evidence | Design | Test |
| --- | --- | --- | --- |
| BR-CUST-01 | `sm-shop/.../api/v1/customer/AuthenticateCustomerApi.java`: `/customer/register` required fields | SDD registration | TC-CUST-01 existing; TC-CUST-03 proposed |
| BR-CUST-02 | `sm-shop/.../controller/customer/facade/CustomerFacadeImpl.java`: store-scoped `checkIfUserExists` | SDD identity scope | TC-CUST-02, 06 proposed |
| BR-CUST-03 | `AuthenticateCustomerApi.java`: `/customer/login`, JWT response, bad-credentials 401 | SDD authentication | TC-CUST-01 existing; TC-CUST-04 proposed |
| BR-CUST-04 | `sm-shop/.../store/facade/customer/CustomerFacadeImpl.java`: principal/customer nickname authorization | SDD authorization | TC-CUST-05 proposed |
| BR-CUST-05 | Customer service calls accept store context; duplicate check uses store ID | SDD store scope | TC-CUST-06 proposed |
| BR-CUST-06 | `sm-shop/.../store/facade/customer/CustomerFacadeImpl.java`: UUID reset token and two-day expiry | SDD password recovery | TC-CUST-07 proposed |
| BR-CUST-07 | Customer DTOs, authentication and reset routes process sensitive data | SDD data minimization | TC-CUST-08 proposed |

Existing test: `sm-shop/src/test/java/com/salesmanager/test/shop/integration/customer/CustomerRegistrationIntegrationTest.java`. It covers a happy-path registration/login only; security requirements remain unverified.