# Lab 4 — Curate the Catalogue — Linked Products and CSV Import

**Course:** AI for eCommerce (TGS-2026064474)  
**Topic 02:** Manage Products on WooCommerce Store  
**Objective:** Ensure smooth maintenance and consistent bulk updates of the product catalogue (A4, K2, K4).  
**Platform:** WooCommerce — https://woocommerce.com

## Goal

Grow and maintain the catalogue efficiently. You organise categories and global attributes, link products together as up-sells and cross-sells to raise order value, then import a batch of products from a CSV file and export the catalogue for bulk editing.

## What you'll build

A curated catalogue with categories, attributes, up-sells, cross-sells and CSV-imported products

*Uses: Products > Categories · Products > Attributes · Linked Products tab · Product CSV Importer/Exporter.*

![WooCommerce — Lab 4](../courseware/assets/woo-linked-products.png)

## Why the business cares

Editing products one at a time does not scale. Bulk import and export is how a real store launches a catalogue, runs a seasonal price change, or syncs with a supplier feed.

## Prerequisites

- Your assigned demo WordPress site — one of **wp1.tertiarytraining.com – wp5.tertiarytraining.com** — with administrator access. Log in at `/wp-admin` (for example `https://wp1.tertiarytraining.com/wp-admin`) with username `admin` and password `admin12345`.
- A modern browser. A second private/incognito window is useful for viewing the storefront as a customer while you edit as the administrator.
- The Harbour & Co store you set up in Lab 1, with WooCommerce active.
- Product images and, for the catalogue labs, the sample product CSV ([data/harbour-co-products.csv](data/harbour-co-products.csv)).

## Step-by-step

### Step 1 — Go to Products > Categories. Add a category with a Name, an optional URL-friendly Slug, a Parent if it is a subcategory, a Description, a Display type and an Image.

```bash
Name: Apparel   ·   Display type: Products
```

### Step 2 — Add a child category by setting its Parent to the category you just created, to see how a hierarchy forms. Drag and drop the rows to reorder them — this order is used on the storefront.

```bash
Name: Shirts   ·   Parent: Apparel
```

### Step 3 — Go to Products > Attributes and create a global attribute that any product can reuse. Add a Name and Slug, enable Archives if you want a browsable page per term, choose a default sort order, and click Add attribute.

```bash
Name: Material   ·   Sort order: Name
```

### Step 4 — Click 'Configure terms' beside your new attribute and add its values. Global attributes are what the 'Filter Products by Attribute' widget uses for layered navigation.

```bash
Terms:  Cotton, Polyester, Linen
```

### Step 5 — Open one of your products and go to Product data > Linked Products. In the Upsells field, search for and add a more premium product. Up-sells display on the product page as a recommendation instead of the current item.

```bash
Upsells:  Premium Polo Shirt
```

### Step 6 — In the same panel add a complementary product to the Cross-sells field. Cross-sells are promoted in the cart, based on what the customer is already buying. Click Update.

```bash
Cross-sells:  Cotton Cap
```

### Step 7 — Understand related products: these are chosen automatically by WooCommerce from products sharing the same categories or tags. You influence them by how you categorise and tag, not by naming them directly.

### Step 8 — Export your catalogue as a template: go to Products and click Export. Choose the columns and product types to include, then click 'Generate CSV' and open the downloaded file.

```bash
Products > Export > Generate CSV
```

### Step 9 — Open the sample product CSV supplied for this lab (labs/data/harbour-co-products.csv) in a spreadsheet. It contains five new Harbour & Co products — Linen Summer Shirt (LINEN-SHIRT-001, 49.90), Classic Denim Jacket (JACKET-DENIM-001, 89.90 on sale at 79.90), Canvas Tote Bag (TOTE-CANVAS-001, 24.90), Merino Wool Scarf (SCARF-MERINO-001, 34.90) and Leather Belt (BELT-LEATHER-001, 32.90) — each with a name, SKU, prices, categories, tags, stock and weight. Review the columns, then save it unchanged as CSV.

```bash
Columns:  Name, SKU, Regular price, Sale price, Categories, Tags, Stock, Published
```

### Step 10 — Go to Products and click Import. Choose harbour-co-products.csv, click Continue, review the column mapping WooCommerce proposes, then click 'Run the importer'. Do not refresh the browser while it runs.

```bash
Products > Import > harbour-co-products.csv > Run the importer
```

### Step 11 — Confirm the imported products appear in Products > All Products, then re-import the same file with 'Update existing products' ticked in the importer's advanced options to see how a bulk price change is applied.

## Test it

Your store has a category hierarchy and a global attribute, one product shows an up-sell on its page and a cross-sell in the cart, and the CSV-imported products appear in the catalogue.

---
*© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved. · www.tertiarycourses.com.sg*
