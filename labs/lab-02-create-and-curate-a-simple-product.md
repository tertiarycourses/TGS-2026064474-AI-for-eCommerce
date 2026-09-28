# Lab 2 — Create and Curate a Simple Product

**Course:** AI for eCommerce (TGS-2026064474)  
**Topic 02:** Manage Products on WooCommerce Store  
**Objective:** Edit and curate product web content on the WooCommerce CMS (A6, K2, K4).  
**Platform:** WooCommerce — https://woocommerce.com

## Goal

Build your first catalogue entry. You add a simple product with a title, long and short description, price and SKU, upload a featured image and a gallery, then file it under a category and tag so customers can find it. This is the core content-curation task the CMS exists to support.

## What you'll build

A published simple product, complete with images, price, SKU, category and tag

*Uses: Products > Add New · Product Data panel · Product image & gallery · Categories · Tags.*

![WooCommerce — Lab 2](../courseware/assets/woo-add-simple-product.png)

## Why the business cares

Product content is the storefront's sales copy. Consistent titles, descriptions and imagery are exactly the content guidelines a CMS policy governs — and the reason curation matters.

## Prerequisites

- Your assigned demo WordPress site — one of **wp1.tertiarytraining.com – wp5.tertiarytraining.com** — with administrator access. Log in at `/wp-admin` (for example `https://wp1.tertiarytraining.com/wp-admin`) with username `admin` and password `admin12345`.
- A modern browser. A second private/incognito window is useful for viewing the storefront as a customer while you edit as the administrator.
- The Harbour & Co store you set up in Lab 1, with WooCommerce active.
- Product images and, for the catalogue labs, the sample product CSV ([data/harbour-co-products.csv](data/harbour-co-products.csv)).

## Step-by-step

### Step 1 — Go to Products > Add New. Enter a clear, descriptive product Title — this becomes the product page's heading and its URL slug.

```bash
Title:  Classic Cotton T-Shirt
```

### Step 2 — Write the long Description in the main editor. This appears in the Product Description tab on the product page. Cover what the product is, what it is made of, and who it is for.

```bash
A relaxed-fit everyday tee in 100% combed cotton (180 gsm). Pre-shrunk,
breathable and machine-washable — Harbour & Co's best-selling basic for
work, weekends and everything in between.
```

### Step 3 — Scroll to the Product data panel and leave the type as 'Simple product'. Tick Virtual only if the product needs no shipping, or Downloadable if the customer receives a file.

```bash
Product data:  Simple product
```

### Step 4 — On the General tab enter the Regular price. Optionally set a Sale price and schedule its start and end dates.

```bash
Regular price:  29.90     Sale price:  24.90
```

### Step 5 — Open the Inventory tab and enter a unique SKU. Tick 'Manage stock?' to track quantity, then set the Stock quantity and choose what happens when it runs out (Allow backorders or not).

```bash
SKU:  TSHIRT-CLASSIC-001     Stock quantity:  50
```

### Step 6 — Open the Shipping tab and enter the Weight and Dimensions. These feed weight-based and dimension-based shipping rates later.

```bash
Weight: 0.2 kg   ·   Dimensions: 30 x 20 x 2 cm
```

### Step 7 — Fill in the Product short description box below the editor. This excerpt appears beside the product image at the top of the page and is the first copy a customer reads — keep it to two or three lines.

```bash
Short description:  Soft 100% combed cotton tee in a relaxed unisex fit.
Pre-shrunk and machine-washable. Made for everyday Singapore weather.
```

### Step 8 — In the right-hand column, set the Product categories. Click '+ Add new category' if the category does not exist yet. Every product must belong to at least one category, otherwise it falls into the default 'Uncategorized'.

```bash
Category:  Apparel
```

### Step 9 — Add Product tags in the box below. Tags are flat, not hierarchical — use them for cross-cutting themes a customer might browse by.

```bash
Tags:  cotton, unisex, casual
```

### Step 10 — Set the Product image (the featured image) from the right-hand column. Then click 'Add product gallery images' and upload two or three additional views.

### Step 11 — Set the Catalog visibility in the Publish box. 'Shop and search' shows the product everywhere; 'Search only', 'Shop only' and 'Hidden' restrict where it appears. Tick 'This is a featured product' to mark it for featured-product widgets and blocks.

```bash
Catalog visibility:  Shop and search
```

### Step 12 — Click Publish, then click 'View product' to see the live product page. Check the title, price, short description, image gallery, category and tag all render as intended.

## Test it

Your product appears on the /shop page and its own product page shows the featured image, gallery, price, short description, full description tab, category and tags.

---
*© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved. · www.tertiarycourses.com.sg*
