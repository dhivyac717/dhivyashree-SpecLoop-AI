# Shopizer Shopping Cart Test Cases

Existing API integration coverage is listed separately from proposed coverage. This report did not execute the tests.

| ID | Requirement | Scenario | Expected result | Current evidence |
| --- | --- | --- | --- | --- |
| TC-CART-01 | BR-CART-01 | Add one product to a new cart | 201; cart code returned; total quantity is one | Existing `addToCart` test |
| TC-CART-02 | BR-CART-02 | Add a second product to existing cart | 201; quantity reflects both lines | Existing `addSecondToCart` test |
| TC-CART-03 | BR-CART-04 | Update using an unknown cart code | 404; no unintended cart mutation | Existing `addToWrongToCartId` test |
| TC-CART-04 | BR-CART-02 | Batch-update two quantities | 201; returned total quantity matches updates | Existing `updateMultiWCartId` test |
| TC-CART-05 | BR-CART-02 | Set a line quantity to zero | Line is removed; remaining quantity is correct | Existing `updateMultiWZeroOnOneProd` test |
| TC-CART-06 | BR-CART-03 | Delete a line without body | 204 and no response body | Existing `deleteCartItem` test |
| TC-CART-07 | BR-CART-03 | Delete a line with `body=true` | 200 with updated cart representation | Existing `deleteCartItemWithBody` test |
| TC-CART-08 | BR-CART-05 | Customer requests another customer's cart | Access denied; cart data is not disclosed | Add test; absent from reviewed test class |
| TC-CART-09 | BR-CART-05 | Reuse cart code under a different store | Not found/denied; no cross-store disclosure | Add test; store passed to lookup |
| TC-CART-10 | BR-CART-06 | Invalid/unavailable product or negative/oversized quantity | Documented validation error and unchanged cart | Add service/API boundary tests |

These cases are not all currently implemented: TC-CART-01 through TC-CART-07 correspond to existing source test methods; TC-CART-08 through TC-CART-10 are recommendations.