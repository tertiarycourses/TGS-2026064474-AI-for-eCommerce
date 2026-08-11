# Lab 6 — Process Orders, Refunds and Coupons

**Course:** Building a Successful eCommerce Store with WooCommerce (TGS-2026064474)  
**Topic 04:** Manage Sales on WooCommerce Store  
**Objective:** Highlight and resolve issues related to sales, stock, refunds and promotions (A5, K5).  
**Platform:** WooCommerce — https://woocommerce.com

## Goal

Run the store as a shop manager. You walk an order through its statuses, edit and manually create orders, issue a refund that restocks the item, then build a coupon and prove it applies at checkout — the day-to-day issue resolution the CMS is used for.

## What you'll build

A processed order, a completed refund with restocking, and a working discount coupon

*Uses: WooCommerce > Orders · Order statuses · Refund · WooCommerce > Coupons · Checkout.*

![WooCommerce — Lab 6](../courseware/assets/woo-single-order.png)

## Why the business cares

Orders, refunds and promotions are where customer problems surface. Resolving them quickly and correctly — with stock and revenue staying accurate — is the operational heart of the store.

## Prerequisites

- Your assigned demo WordPress site — one of **wp1.tertiarytraining.com – wp5.tertiarytraining.com** — with administrator access. Log in at `/wp-admin` (for example `https://wp1.tertiarytraining.com/wp-admin`) with username `admin` and password `admin12345`.
- A modern browser. A second private/incognito window is useful for viewing the storefront as a customer while you edit as the administrator.
- The Harbour & Co store you set up in Lab 1, with WooCommerce active.
- Product images and, for the catalogue labs, the sample product CSV ([data/harbour-co-products.csv](data/harbour-co-products.csv)).

## Step-by-step

### Step 1 — Go to WooCommerce > Orders. If you placed a test order in the previous lab it is listed here with an order number, customer name, date, status, address and total.

```bash
WooCommerce > Orders
```

### Step 2 — Click Screen Options at the top right to choose which columns and how many rows to display. Use the Preview 'eye' icon on an order row to see its contents without leaving the list.

### Step 3 — Open the order by clicking its number. Review the three panels: Order data (status, customer, dates), Order items (products, quantities, totals) and Order notes on the right.

### Step 4 — Work through the order statuses and note what each means: Pending payment (unpaid), Processing (paid, stock reduced, awaiting fulfilment), On hold (awaiting payment confirmation), Completed (fulfilled), Cancelled, Refunded and Failed.

```bash
Status:  Processing  →  Completed
```

### Step 5 — Change the status to Completed and click Update. Check Order notes — WooCommerce logs the status change, and a completion email is sent to the customer.

### Step 6 — Create an order by hand, as you would for a phone or offline sale. Go to WooCommerce > Orders and click Add order. Set the customer — use the mock walk-in customer below — then click 'Add item(s)' to add products.

```bash
Customer: Tan Wei Ling · tan.weiling@example.com
Billing: 8 Marina Boulevard, #12-04, Singapore 018981
Items: 1 x Merino Wool Scarf (S$34.90) · 1 x Leather Belt (S$32.90)
```

### Step 7 — With line items added, click 'Recalculate' so WooCommerce works out the totals and tax. Set the status to Pending payment and Create the order.

### Step 8 — Use the Order actions dropdown to send 'Email invoice / order details to customer', which gives them payment instructions for the manual order.

```bash
Order actions:  Email invoice / order details to customer
```

### Step 9 — Issue a refund. Open a Completed or Processing order and click the Refund button below the line items. Enter the quantity or amount to refund and add a refund reason.

```bash
Refund: 1 x Classic Cotton T-Shirt  S$29.90   ·   Reason: wrong size delivered
```

### Step 10 — Tick 'Restock refunded items' so the returned stock goes back into inventory, then click 'Refund manually'. Manual refund records the refund in WooCommerce; a gateway refund would also return the money automatically.

```bash
Restock refunded items: ticked  →  Refund manually
```

### Step 11 — Verify the stock movement: open the refunded product and confirm its Inventory quantity has increased, and check the order notes for the refund entry.

### Step 12 — Enable coupons if they are not already on. Go to WooCommerce > Settings > General and tick 'Enable the use of coupon codes', then save.

```bash
Settings > General > Enable coupons
```

### Step 13 — Go to Marketing > Coupons (WooCommerce > Coupons on older versions) and click Add coupon. Enter or generate a Coupon code and a Description for internal reference.

```bash
Code:  WELCOME10
```

### Step 14 — On the General tab choose the Discount type and amount. Percentage discount takes a share of the qualifying items; Fixed cart discount takes a flat sum off the whole cart; Fixed product discount takes a set amount off each qualifying item. Set an expiry date and tick 'Allow free shipping' if appropriate.

```bash
Discount type: Percentage discount   ·   Amount: 10
```

### Step 15 — On the Usage restriction tab set a Minimum spend and any product or category limits. On the Usage limits tab set 'Usage limit per coupon' and 'Usage limit per user' so the promotion cannot be abused. Publish the coupon.

```bash
Minimum spend: 50   ·   Usage limit per user: 1
```

### Step 16 — Test the promotion: open the store in a private window, add products to the cart, and apply your coupon code at the cart or checkout. Confirm the discount is deducted and complete the checkout.

```bash
Apply coupon:  WELCOME10
```

### Step 17 — Return to WooCommerce > Orders, open the new order and confirm the coupon is recorded against it. Check Marketing > Coupons to see the usage count has incremented.

## Test it

You have moved an order to Completed, created an order manually, refunded an item with stock restored, and redeemed a coupon at checkout that shows on the resulting order.

---
*© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved. · www.tertiarycourses.com.sg*
