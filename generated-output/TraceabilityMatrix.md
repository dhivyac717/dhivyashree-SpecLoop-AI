# Shopizer Case Study Traceability Matrix

Status: source-mapped draft; test execution and stakeholder approval are not implied.

| Capability | Requirement IDs | Primary source | Existing test evidence | Main gap |
| --- | --- | --- | --- | --- |
| Order checkout | BR-ORD-01..06 | `sm-shop/.../api/v1/order/OrderApi.java`; order facade; core `OrderService` | `OrderApiIntegrationTest` exists but is ignored/incomplete | Active checkout end-to-end coverage |
| Cart | BR-CART-01..06 | `sm-shop/.../api/v1/shoppingCart/ShoppingCartApi.java`; core `ShoppingCartService` | `ShoppingCartAPIIntegrationTest` covers common line operations | Authorization/store isolation, validation, concurrency |
| Customer | BR-CUST-01..07 | `sm-shop/.../api/v1/customer/AuthenticateCustomerApi.java`; `CustomerApi.java`; customer facade | `CustomerRegistrationIntegrationTest` covers registration/login | Authorization, duplicates, recovery/token/privacy behavior |

Detailed requirement-to-design-to-test mappings are in `case-studies/shopizer/{OrderService,ShoppingCartService,CustomerService}/generated-traceability.md`. `..` in requirement ranges is shorthand for the inclusive IDs, not a generated link.