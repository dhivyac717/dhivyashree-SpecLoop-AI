# Shopizer Shopping Cart Traceability

Status: initial source mapping; proposed cases remain unverified.

| Requirement | Source evidence | Design | Test evidence |
| --- | --- | --- | --- |
| BR-CART-01 | `sm-shop/.../api/v1/shoppingCart/ShoppingCartApi.java`: `POST /cart` | SDD create interface | TC-CART-01 existing |
| BR-CART-02 | Same API: `PUT /cart/{code}`, `POST /cart/{code}/multi` | SDD quantity updates | TC-CART-02, 04, 05 existing |
| BR-CART-03 | Same API: `DELETE /cart/{code}/product/{sku}`, `body` option | SDD removal interface | TC-CART-06, 07 existing |
| BR-CART-04 | Same API: `GET /cart/{code}` and 404 handling | SDD read interface | TC-CART-03 existing invalid-code path |
| BR-CART-05 | Same API: `GET /auth/customer/cart`; `ShoppingCartFacadeImpl.get` | SDD principal/customer/store flow | TC-CART-08, 09 proposed |
| BR-CART-06 | `sm-core/.../services/shoppingcart/ShoppingCartService.java`; validate concrete implementation and product services | SDD domain validation | TC-CART-10 proposed |

Existing tests: `sm-shop/src/test/java/com/salesmanager/test/shop/integration/cart/ShoppingCartAPIIntegrationTest.java`. The test class uses ordered methods and static state; isolation should be reviewed.