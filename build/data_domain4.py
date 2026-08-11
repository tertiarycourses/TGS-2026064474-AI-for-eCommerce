"""
Topic 4 — Manage Sales on WooCommerce Store (LO5 / A5, K5).

Lab 6: process an order end to end, issue a refund with restocking, and
create a coupon then redeem it at checkout.

Carries forward the "Activity: Manage Sales" activity from the approved
v14 deck.

The `steps` here drive the LEARNER GUIDE and the labs/*.md files only.
The slide deck shows the lab OVERVIEW + OUTCOME visually — never the steps.
"""

DOMAIN4 = [
    dict(
        num=6,
        topic=4,
        title="Process Orders, Refunds and Coupons",
        image="woo-single-order.png",
        objective="Highlight and resolve issues related to sales, stock, refunds and promotions (A5, K5).",
        desc=("Run the store as a shop manager. You walk an order through its statuses, edit and manually create "
              "orders, issue a refund that restocks the item, then build a coupon and prove it applies at "
              "checkout — the day-to-day issue resolution the CMS is used for."),
        build="A processed order, a completed refund with restocking, and a working discount coupon",
        services="WooCommerce > Orders · Order statuses · Refund · WooCommerce > Coupons · Checkout",
        business=("Orders, refunds and promotions are where customer problems surface. Resolving them quickly and "
                  "correctly — with stock and revenue staying accurate — is the operational heart of the store."),
        steps=[
            ("Go to WooCommerce > Orders. If you placed a test order in the previous lab it is listed here with an order number, customer name, date, status, address and total.", "WooCommerce > Orders"),
            ("Click Screen Options at the top right to choose which columns and how many rows to display. Use the Preview 'eye' icon on an order row to see its contents without leaving the list.", ""),
            ("Open the order by clicking its number. Review the three panels: Order data (status, customer, dates), Order items (products, quantities, totals) and Order notes on the right.", ""),
            ("Work through the order statuses and note what each means: Pending payment (unpaid), Processing (paid, stock reduced, awaiting fulfilment), On hold (awaiting payment confirmation), Completed (fulfilled), Cancelled, Refunded and Failed.", "Status:  Processing  →  Completed"),
            ("Change the status to Completed and click Update. Check Order notes — WooCommerce logs the status change, and a completion email is sent to the customer.", ""),
            ("Create an order by hand, as you would for a phone or offline sale. Go to WooCommerce > Orders and click Add order. Set the customer — use the mock walk-in customer below — then click 'Add item(s)' to add products.", "Customer: Tan Wei Ling · tan.weiling@example.com\nBilling: 8 Marina Boulevard, #12-04, Singapore 018981\nItems: 1 x Merino Wool Scarf (S$34.90) · 1 x Leather Belt (S$32.90)"),
            ("With line items added, click 'Recalculate' so WooCommerce works out the totals and tax. Set the status to Pending payment and Create the order.", ""),
            ("Use the Order actions dropdown to send 'Email invoice / order details to customer', which gives them payment instructions for the manual order.", "Order actions:  Email invoice / order details to customer"),
            ("Issue a refund. Open a Completed or Processing order and click the Refund button below the line items. Enter the quantity or amount to refund and add a refund reason.", "Refund: 1 x Classic Cotton T-Shirt  S$29.90   ·   Reason: wrong size delivered"),
            ("Tick 'Restock refunded items' so the returned stock goes back into inventory, then click 'Refund manually'. Manual refund records the refund in WooCommerce; a gateway refund would also return the money automatically.", "Restock refunded items: ticked  →  Refund manually"),
            ("Verify the stock movement: open the refunded product and confirm its Inventory quantity has increased, and check the order notes for the refund entry.", ""),
            ("Enable coupons if they are not already on. Go to WooCommerce > Settings > General and tick 'Enable the use of coupon codes', then save.", "Settings > General > Enable coupons"),
            ("Go to Marketing > Coupons (WooCommerce > Coupons on older versions) and click Add coupon. Enter or generate a Coupon code and a Description for internal reference.", "Code:  WELCOME10"),
            ("On the General tab choose the Discount type and amount. Percentage discount takes a share of the qualifying items; Fixed cart discount takes a flat sum off the whole cart; Fixed product discount takes a set amount off each qualifying item. Set an expiry date and tick 'Allow free shipping' if appropriate.", "Discount type: Percentage discount   ·   Amount: 10"),
            ("On the Usage restriction tab set a Minimum spend and any product or category limits. On the Usage limits tab set 'Usage limit per coupon' and 'Usage limit per user' so the promotion cannot be abused. Publish the coupon.", "Minimum spend: 50   ·   Usage limit per user: 1"),
            ("Test the promotion: open the store in a private window, add products to the cart, and apply your coupon code at the cart or checkout. Confirm the discount is deducted and complete the checkout.", "Apply coupon:  WELCOME10"),
            ("Return to WooCommerce > Orders, open the new order and confirm the coupon is recorded against it. Check Marketing > Coupons to see the usage count has incremented.", ""),
        ],
        test=("You have moved an order to Completed, created an order manually, refunded an item with stock "
              "restored, and redeemed a coupon at checkout that shows on the resulting order."),
    ),
]
