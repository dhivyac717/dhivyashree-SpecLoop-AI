# Shopizer Order Flow Traceability

Status: code-reference links are initial analysis; stakeholder approval and test execution are outstanding.

| Requirement | Source evidence | Design/story | Test |
| --- | --- | --- | --- |
| BR-ORD-01 | `sm-shop/.../api/v1/order/OrderApi.java`: `/auth/cart/{code}/checkout`; principal resolves customer | SDD authenticated route; US-ORD-01 | TC-ORD-01, TC-ORD-04 |
| BR-ORD-02 | `OrderApi.java`: `/cart/{code}/checkout`; anonymous payload and customer processing | SDD anonymous route; US-ORD-02 | TC-ORD-02, TC-ORD-08 |
| BR-ORD-03 | `sm-shop/.../store/facade/order/OrderFacadeImpl.java`: `orderConfirmation`; maps totals/products/addresses | SDD response mapping | TC-ORD-07 |
| BR-ORD-04 | `OrderApi.java`: cart lookup by code and `MerchantStore`; missing cart raises not-found | SDD interfaces | TC-ORD-03, TC-ORD-05 |
| BR-ORD-05 | `OrderApi.java`; customer authorization utilities and store-scoped service calls | SDD security | TC-ORD-04, TC-ORD-05 |
| BR-ORD-06 | `OrderApi.java`: broad exception handler maps authenticated checkout failures to 503 | SDD failure handling | TC-ORD-06 |

Test evidence: `sm-shop/src/test/java/com/salesmanager/test/shop/integration/order/OrderApiIntegrationTest.java` is ignored and incomplete. No requirement in this table is marked end-to-end verified.