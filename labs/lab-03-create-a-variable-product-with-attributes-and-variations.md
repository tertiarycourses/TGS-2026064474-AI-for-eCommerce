# Lab 3 — Create a Variable Product with Attributes and Variations

**Course:** AI for eCommerce (TGS-2026064474)  
**Topic 02:** Manage Products on WooCommerce Store  
**Objective:** Maintain product web content that carries options, pricing and stock per variation (A4, K2, K4).  
**Platform:** WooCommerce — https://woocommerce.com

## Goal

Most real products come in options. You define a custom attribute such as Size or Colour, generate the variations from it, then give each variation its own SKU, price, stock level and image — and verify the dropdowns work on the storefront.

## What you'll build

A published variable product whose variations each carry their own price, SKU and stock

*Uses: Product data > Variable product · Attributes tab · Variations tab · Used for variations.*

![WooCommerce — Lab 3](../courseware/assets/woo-virtual-product.png)

## Why the business cares

Variations keep one product page instead of five near-duplicates. That is cleaner content, better SEO, and far less maintenance when a price or description changes.

## Prerequisites

- Your assigned demo WordPress site — one of **wp1.tertiarytraining.com – wp5.tertiarytraining.com** — with administrator access. Log in at `/wp-admin` (for example `https://wp1.tertiarytraining.com/wp-admin`) with username `admin` and password `admin12345`.
- A modern browser. A second private/incognito window is useful for viewing the storefront as a customer while you edit as the administrator.
- The Harbour & Co store you set up in Lab 1, with WooCommerce active.
- Product images and, for the catalogue labs, the sample product CSV ([data/harbour-co-products.csv](data/harbour-co-products.csv)).

## Step-by-step

### Step 1 — Go to Products > Add New and enter a Title and Description as you did for the simple product.

```bash
Title:  Premium Polo Shirt
```

### Step 2 — In the Product data panel, change the dropdown from 'Simple product' to 'Variable product'. The price fields disappear — price now belongs to each variation, not the parent.

```bash
Product data:  Variable product
```

### Step 3 — Open the Attributes tab and click 'Add new'. Name the attribute and enter its values separated by a vertical bar. Tick 'Visible on the product page' and, critically, tick 'Used for variations'. Click Save attributes.

```bash
Name: Size    Value(s):  Small | Medium | Large
```

### Step 4 — Add a second attribute the same way so you can see how combinations multiply. Remember to tick 'Used for variations' for this one too, then Save attributes.

```bash
Name: Colour   Value(s):  Black | White
```

### Step 5 — Open the Variations tab. From the dropdown choose 'Generate variations' to create every combination automatically, and confirm the prompt. With 3 sizes and 2 colours you get 6 variations.

```bash
Generate variations  →  6 variations created
```

### Step 6 — Expand the first variation and enter its own SKU and Regular price. Repeat for every variation — a variation with no price cannot be purchased and will not appear in the dropdown.

```bash
POLO-S-BLK 39.90 · POLO-M-BLK 39.90 · POLO-L-BLK 41.90
POLO-S-WHT 39.90 · POLO-M-WHT 39.90 · POLO-L-WHT 41.90
```

### Step 7 — Within each variation tick 'Manage stock?' and set a Stock quantity, so each size/colour combination tracks its own inventory.

```bash
Stock quantity:  25
```

### Step 8 — Upload a variation image for at least one variation by clicking the image placeholder inside the expanded variation. The product image swaps when the customer selects that option.

### Step 9 — Set the Default form values at the top of the Variations tab if you want a combination pre-selected when the page loads. Click Save changes.

```bash
Default:  Size = Medium, Colour = Black
```

### Step 10 — Assign the product to a category and tag, set the Product image and gallery, then click Publish.

```bash
Category:  Apparel
```

### Step 11 — Test on the front end: open the product page, choose a size and colour, and confirm the price, SKU, image and stock message update. Set one variation's stock to 0 and confirm it shows as out of stock.

## Test it

Selecting each combination on the live product page updates the price and SKU, the variation image swaps where you set one, and a zero-stock variation is reported as unavailable.

---
*© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved. · www.tertiarycourses.com.sg*
