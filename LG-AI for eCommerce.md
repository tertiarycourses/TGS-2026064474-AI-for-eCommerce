# AI for eCommerce — Learner Guide

**WSQ Course Code:** TGS-2026064474  |  **Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)  |  **Version v15.2 · 28 September 2026**

## Contents

- [Introduction](#introduction)
- [Course Learning Outcomes](#course-learning-outcomes)
- [How This Course Is Assessed](#how-this-course-is-assessed)
- [Skills Framework Mapping](#skills-framework-mapping)
- [Before You Start — Setting Up for the Hands-On Labs](#before-you-start--setting-up-for-the-hands-on-labs)
- [Topic 01 — Overview of WooCommerce CMS  (LO1 · A1, K1 · Day 1 AM)](#topic-01--overview-of-woocommerce-cms--lo1--a1-k1--day-1-am)
  - [Activity — Discussion — Content Management Policies for Your Store  (15 minutes)](#activity--discussion--content-management-policies-for-your-store--15-minutes)
  - [Lab 1 — Set Up Your WooCommerce Store](#lab-1--set-up-your-woocommerce-store)
- [Topic 02 — Manage Products on WooCommerce Store  (LO2, LO3 · A4, A6, K2, K4 · Day 1 AM/PM)](#topic-02--manage-products-on-woocommerce-store--lo2-lo3--a4-a6-k2-k4--day-1-ampm)
  - [Lab 2 — Create and Curate a Simple Product](#lab-2--create-and-curate-a-simple-product)
  - [Lab 3 — Create a Variable Product with Attributes and Variations](#lab-3--create-a-variable-product-with-attributes-and-variations)
  - [Lab 4 — Curate the Catalogue — Linked Products and CSV Import](#lab-4--curate-the-catalogue--linked-products-and-csv-import)
- [Topic 03 — Manage Payments and Shipping  (LO4 · A3, K3 · Day 1 PM)](#topic-03--manage-payments-and-shipping--lo4--a3-k3--day-1-pm)
  - [Activity — Discussion — Recommend Payment and Shipping for Customer Experience  (15 minutes)](#activity--discussion--recommend-payment-and-shipping-for-customer-experience--15-minutes)
  - [Lab 5 — Configure Payment Methods and Shipping Zones](#lab-5--configure-payment-methods-and-shipping-zones)
- [Topic 04 — Manage Sales on WooCommerce Store  (LO5 · A5, K5 · Day 1 PM)](#topic-04--manage-sales-on-woocommerce-store--lo5--a5-k5--day-1-pm)
  - [Lab 6 — Process Orders, Refunds and Coupons](#lab-6--process-orders-refunds-and-coupons)
- [Topic 05 — Manage WooCommerce Performance  (LO6 · A2, K6, K7 · Day 1 PM)](#topic-05--manage-woocommerce-performance--lo6--a2-k6-k7--day-1-pm)
  - [Activity — Discussion — Metrics to Measure Store Performance  (15 minutes)](#activity--discussion--metrics-to-measure-store-performance--15-minutes)
  - [Lab 7 — Measure Store Performance with Reports and Analytics](#lab-7--measure-store-performance-with-reports-and-analytics)
- [Putting It Together — Running a Store End to End](#putting-it-together--running-a-store-end-to-end)
- [Troubleshooting the Labs](#troubleshooting-the-labs)
- [Glossary](#glossary)


## Introduction

This Learner Guide accompanies the WSQ course AI for eCommerce (TGS-2026064474), conducted by Tertiary Infotech Academy Pte Ltd. It is a one-day (8-hour) course mapped to the Skills Framework TSC Content Management System Utilisation (RET-CIE-4002-1.1, Level 4).

The course is deliberately practical. Topic 1 sets up the store and its policies; Topic 2 builds and curates the product catalogue; Topic 3 configures how customers pay and receive their goods; Topic 4 runs the store day to day through orders, refunds and promotions; and Topic 5 measures whether any of it is working. Every lab runs on WooCommerce (https://woocommerce.com), the open-source eCommerce platform for WordPress (https://wordpress.org/plugins/woocommerce/).

This guide contains the full step-by-step instructions for every lab. The slide deck deliberately shows only each lab's purpose and outcome, so follow the numbered steps here while the trainer demonstrates. Keep this guide with you during the assessment — it is open book.


## Course Learning Outcomes

On completion of this course, you will be able to:

- LO1: Setup and monitor WooCommerce CMS to ensure adherence to guidelines and policies. (A1, K1)
- LO2: Edit and curate product website on WooCommerce CMS. (A6, K2, K4)
- LO3: Maintain product web content on WooCommerce CMS. (A4, K2, K4)
- LO4: Recommend payment and shipping methods on WooCommerce CMS to improve customer experience. (A3, K3)
- LO5: Manage issues related to WooCommerce CMS such as sales, out-of-stock, promotion etc. (A5, K5)
- LO6: Manage WooCommerce CMS performance. (A2, K6, K7)


## How This Course Is Assessed

The assessment has two instruments, both open book, conducted at the end of the training day:

- Oral Questioning (OQ) — 15 minutes, open book, 1:1. Covers K1–K7.
- Practical Performance (PP) — 75 minutes, open book, individually completed. Covers A1–A6.
- Open book means you may refer to the course slides, this Learner Guide and any approved materials.
- A minimum of 75% attendance is required to be eligible for assessment and funding.
- An appeal process is available if you disagree with the assessment outcome.

The Oral Questioning covers the seven knowledge statements (K1–K7) and the Practical Performance covers the six abilities (A1–A6). Each topic in this guide is labelled with the ability and knowledge it develops, so you can see exactly what each session is preparing you for.


## Skills Framework Mapping

**Abilities — assessed by the Practical Performance**

- A1 — Monitor adherence to content management policies, guidelines and permissions on content management
- A2 — Develop and review metrics to measure performance of content management systems
- A3 — Recommend areas for improvements for a better customer experience in terms of organisation's web properties and assets
- A4 — Ensure smooth maintenance and consistent updates of content management systems
- A5 — Highlight and resolve issues related to content management systems
- A6 — Edit and curate web content

**Knowledge — assessed by the Oral Questioning**

- K1 — Content management policies, guidelines and permissions on content management
- K2 — Web content for deployment
- K3 — Organisation's web properties and assets
- K4 — Creation and curation of web content guidelines
- K5 — Web content and platform management systems
- K6 — Types of performance metrics of content management systems
- K7 — Criteria for evaluating metrics to measure performance of content management systems


## Before You Start — Setting Up for the Hands-On Labs

**What you need**

- Your assigned demo WordPress training site — one of the five sites wp1.tertiarytraining.com – wp5.tertiarytraining.com, assigned by the trainer at the start of class. You have full administrator access to your site for the day.
- The demo hosting already meets the WooCommerce requirements: PHP 7.2 or greater, MySQL 5.6+ (or MariaDB 10.0+), a WordPress memory limit of 128 MB or greater, and HTTPS support.
- The WooCommerce plugin — installed from Plugins > Add New during Lab 1. It is free (https://woocommerce.com).
- The Storefront theme, the official WooCommerce theme, also installed during Lab 1.
- A laptop with a modern web browser. A second private/incognito window is useful for viewing the storefront as a customer while you edit as the administrator.
- Two or three product images (any photographs will do) and the sample product CSV file (labs/data/harbour-co-products.csv) for the catalogue labs.

**Log in to your demo training site**

Before Lab 1 the trainer assigns each learner one demo WordPress site: wp1.tertiarytraining.com – wp5.tertiarytraining.com. Open your site's login page at /wp-admin and sign in with the classroom credentials below. Everything else in this course happens inside that dashboard. The sites are reset before every class, so treat your site as yours for the day and experiment freely.

```bash
Open https://wp1.tertiarytraining.com/wp-admin   (use YOUR assigned site: wp1 ... wp5)
Username: admin     Password: admin12345
```

**The demo store you will build**

Across the seven labs you build one coherent store — Harbour & Co, a small Singapore apparel and accessories retailer going online, at 71 Ayer Rajah Crescent, #02-18, Singapore 139951. Lab 1 sets the store up; Labs 2–4 build its catalogue (the Classic Cotton T-Shirt, the Premium Polo Shirt in six size/colour variations, and five more products imported from CSV); Lab 5 makes it purchasable with payment methods and Singapore shipping zones; Lab 6 runs its orders, refunds and the WELCOME10 coupon; and Lab 7 measures the result. The Practical Performance assessment uses the same retailer, so the labs are a direct rehearsal for it.

**Conventions used in every lab**

- Menu paths are written the way they appear in the WordPress admin sidebar, for example WooCommerce > Settings > General.
- Values in the shaded boxes are the Harbour & Co demo data — product names, SKUs, prices, the mock customer and the coupon code. Use them as given so your store matches the trainer's demo, or substitute your own; the steps matter more than the specific values.
- Placeholders in CAPITALS or angle brackets are replaced with your own values.
- After changing any setting, click Save changes. WooCommerce does not save automatically, and an unsaved settings screen is the most common reason a step appears not to work.
- Keep a second browser window open on the storefront so you can see each change as a customer sees it.

> **Note:** Work only on your assigned demo training site, never on a live shop. Several labs create test orders, refunds and coupons, and a refund issued against a real order moves real money. The demo sites exist precisely so you can experiment without consequences.


## Topic 01 — Overview of WooCommerce CMS  (LO1 · A1, K1 · Day 1 AM)

What WooCommerce is · Setup wizard · Themes · Widgets & shortcodes · Settings, currency & tax

**Key concepts**

- What WooCommerce is — An open-source, fully customisable eCommerce platform built on WordPress, powering a large share of the world's online stores.
- Six steps to a store — Choose hosting, install WordPress, pick a theme, activate WooCommerce, run the setup wizard, then extend with plugins.
- System requirements — PHP 7.2+, MySQL 5.6+ or MariaDB 10.0+, a 128 MB WordPress memory limit, and HTTPS support.
- Taxonomies and post types — WooCommerce adds its own post types and taxonomies to WordPress to group and structure products.
- Themes and widgets — The theme sets the storefront's look; widgets surface products, filters and categories in widgetised areas.
- Settings, currency and tax — General, Products, Tax, Shipping, Payments and Privacy settings define how the store behaves and prices goods.


### Activity — Discussion — Content Management Policies for Your Store  (15 minutes)

In pairs, consider a store you would run. Decide what content management policies, guidelines and user permissions it needs, and how you would monitor that people actually follow them.

**Discussion prompts**

- Who should be able to publish a product, and who should only be able to draft one?
- Which WordPress/WooCommerce roles map to those responsibilities?
- What product-content guidelines would you set — image size, description length, mandatory fields?
- How would you detect that a policy is not being followed?

**What to produce**

A short policy statement: the roles, the content guidelines, and how adherence is monitored.

> **Note:** Write your answer down as you go. The same reasoning is what the Oral Questioning asks you to demonstrate for K1.


### Lab 1 — Set Up Your WooCommerce Store

Objective: Set up and monitor a WooCommerce CMS so it adheres to store guidelines and policies (A1, K1).

Goal: Install the WooCommerce plugin on a WordPress site, work through the setup wizard to define the store's location, currency and industry, then apply the Storefront theme and confirm the shop, cart, checkout and My Account pages have been created. You finish by setting the currency and tax options that every price in the store will follow.

**What you'll build**

A working WooCommerce store with its currency, tax and core pages configured   (Tools: Plugins > Add New · WooCommerce Setup Wizard · Appearance > Themes · WooCommerce > Settings.)

![WooCommerce — Lab 1: Set Up Your WooCommerce Store](courseware/assets/woo-setup-wizard.png)

*WooCommerce — Lab 1: Set Up Your WooCommerce Store*

**Why the business cares**

The setup wizard is where store-wide policy is set. Currency, tax treatment and page structure decide how every product is priced and presented — getting them right first avoids re-pricing an entire catalogue later.

**Step-by-step**

1. Log in to your assigned demo WordPress site as an administrator. Each learner is assigned one of the five demo training sites wp1.tertiarytraining.com to wp5.tertiarytraining.com — open your site's /wp-admin login page and sign in with the classroom credentials. The demo hosting already meets the WooCommerce requirements: PHP 7.2 or greater, MySQL 5.6+ (or MariaDB 10.0+), a WordPress memory limit of 128 MB or greater, and HTTPS support.

   ```bash
   https://wp1.tertiarytraining.com/wp-admin   ·   Username: admin   ·   Password: admin12345
   ```

2. Go to Plugins > Add New and search for 'WooCommerce'. Check that the author is Automattic, then click Install Now followed by Activate.

   ```bash
   Plugins > Add New > search: WooCommerce
   ```

3. The WooCommerce Setup Wizard opens automatically on first activation. Click Let's go! to begin. (Choosing 'Not right now' lets you configure the store manually from WooCommerce > Settings instead.)
4. On the Store Details step enter the store's address, city, country/region and postcode, then choose the currency the store will price in and the type of product you plan to sell (physical, downloadable, or both). Throughout today's labs you are building the demo store 'Harbour & Co', a small Singapore apparel and accessories retailer going online.

   ```bash
   Store: Harbour & Co   ·   Address: 71 Ayer Rajah Crescent, #02-18, Singapore 139951
Country: Singapore   ·   Currency: Singapore dollar (S$)   ·   Products: physical
   ```

5. Indicate whether you also sell goods and services in person — this determines which payment gateways the wizard offers you.
6. Complete the remaining wizard steps and finish. WooCommerce creates the Shop, Cart, Checkout and My Account pages, and adds its product post types and taxonomies to WordPress.
7. Verify the pages exist: go to Pages and confirm Shop, Cart, Checkout and My Account are listed. These pages hold the WooCommerce shortcodes, for example [woocommerce_cart] and [woocommerce_checkout].

   ```bash
   Pages > Shop · Cart · Checkout · My Account
   ```

8. Apply a WooCommerce-compatible theme. Go to Appearance > Themes > Add New, search for 'Storefront', then Install and Activate it. Storefront is the official WooCommerce theme and is built to work with every core feature.

   ```bash
   Appearance > Themes > Add New > Storefront
   ```

9. Confirm the store currency. Go to WooCommerce > Settings > General > Currency options and set the Currency, Currency position, Thousand separator, Decimal separator and Number of decimals.

   ```bash
   Currency position: Left ($99.99)   ·   Decimals: 2
   ```

10. Enable taxes. Still on WooCommerce > Settings > General, tick 'Enable taxes and tax calculations' and save changes. A Tax tab now appears in the settings.

   ```bash
   WooCommerce > Settings > General > Enable taxes
   ```

11. Open WooCommerce > Settings > Tax and set 'Prices entered with tax'. Choosing inclusive means catalogue prices already contain the base tax rate; exclusive means tax is added at checkout. This decision governs how you enter every product price from now on.

   ```bash
   Prices entered with tax:  Yes, I will enter prices inclusive of tax
   ```

12. Review the user roles that WooCommerce added — Customer and Shop Manager — under Users > All Users. Note which role may publish products and which may only manage orders; this is the permissions basis for your store's content management policy.

   ```bash
   Users > All Users > Role: Shop manager
   ```


**Test it**

Your WordPress site has WooCommerce active, the Storefront theme applied, the four WooCommerce pages created, and the store currency and tax options saved. Visiting /shop shows an empty but working storefront.

> **Note:** A standalone copy of this lab is in labs/lab-01-*.md so you can repeat it after the course. Your WooCommerce project stays available to you.

---


## Topic 02 — Manage Products on WooCommerce Store  (LO2, LO3 · A4, A6, K2, K4 · Day 1 AM/PM)

Product types · Images & galleries · Variations · Categories, tags & attributes · Up-sells · CSV import

**Key concepts**

- Product types — Simple, Grouped, Virtual, Downloadable, External/Affiliate and Variable each model a different kind of offer.
- The Product Data panel — General, Inventory, Shipping, Linked Products and Attributes — where the substance of a product is defined.
- Images and galleries — A featured image plus a gallery, with catalogue visibility controlling where the product appears.
- Categories, tags, attributes — Categories are hierarchical, tags are flat, and attributes drive filtering and product variations.
- Up-sells and cross-sells — Up-sells appear on the product page; cross-sells appear in the cart; related products are automatic.
- CSV import and export — Create or update hundreds of products in one pass, including variations, from a single CSV file.


### Lab 2 — Create and Curate a Simple Product

Objective: Edit and curate product web content on the WooCommerce CMS (A6, K2, K4).

Goal: Build your first catalogue entry. You add a simple product with a title, long and short description, price and SKU, upload a featured image and a gallery, then file it under a category and tag so customers can find it. This is the core content-curation task the CMS exists to support.

**What you'll build**

A published simple product, complete with images, price, SKU, category and tag   (Tools: Products > Add New · Product Data panel · Product image & gallery · Categories · Tags.)

![WooCommerce — Lab 2: Create and Curate a Simple Product](courseware/assets/woo-add-simple-product.png)

*WooCommerce — Lab 2: Create and Curate a Simple Product*

**Why the business cares**

Product content is the storefront's sales copy. Consistent titles, descriptions and imagery are exactly the content guidelines a CMS policy governs — and the reason curation matters.

**Step-by-step**

1. Go to Products > Add New. Enter a clear, descriptive product Title — this becomes the product page's heading and its URL slug.

   ```bash
   Title:  Classic Cotton T-Shirt
   ```

2. Write the long Description in the main editor. This appears in the Product Description tab on the product page. Cover what the product is, what it is made of, and who it is for.

   ```bash
   A relaxed-fit everyday tee in 100% combed cotton (180 gsm). Pre-shrunk,
breathable and machine-washable — Harbour & Co's best-selling basic for
work, weekends and everything in between.
   ```

3. Scroll to the Product data panel and leave the type as 'Simple product'. Tick Virtual only if the product needs no shipping, or Downloadable if the customer receives a file.

   ```bash
   Product data:  Simple product
   ```

4. On the General tab enter the Regular price. Optionally set a Sale price and schedule its start and end dates.

   ```bash
   Regular price:  29.90     Sale price:  24.90
   ```

5. Open the Inventory tab and enter a unique SKU. Tick 'Manage stock?' to track quantity, then set the Stock quantity and choose what happens when it runs out (Allow backorders or not).

   ```bash
   SKU:  TSHIRT-CLASSIC-001     Stock quantity:  50
   ```

6. Open the Shipping tab and enter the Weight and Dimensions. These feed weight-based and dimension-based shipping rates later.

   ```bash
   Weight: 0.2 kg   ·   Dimensions: 30 x 20 x 2 cm
   ```

7. Fill in the Product short description box below the editor. This excerpt appears beside the product image at the top of the page and is the first copy a customer reads — keep it to two or three lines.

   ```bash
   Short description:  Soft 100% combed cotton tee in a relaxed unisex fit.
Pre-shrunk and machine-washable. Made for everyday Singapore weather.
   ```

8. In the right-hand column, set the Product categories. Click '+ Add new category' if the category does not exist yet. Every product must belong to at least one category, otherwise it falls into the default 'Uncategorized'.

   ```bash
   Category:  Apparel
   ```

9. Add Product tags in the box below. Tags are flat, not hierarchical — use them for cross-cutting themes a customer might browse by.

   ```bash
   Tags:  cotton, unisex, casual
   ```

10. Set the Product image (the featured image) from the right-hand column. Then click 'Add product gallery images' and upload two or three additional views.
11. Set the Catalog visibility in the Publish box. 'Shop and search' shows the product everywhere; 'Search only', 'Shop only' and 'Hidden' restrict where it appears. Tick 'This is a featured product' to mark it for featured-product widgets and blocks.

   ```bash
   Catalog visibility:  Shop and search
   ```

12. Click Publish, then click 'View product' to see the live product page. Check the title, price, short description, image gallery, category and tag all render as intended.

**Test it**

Your product appears on the /shop page and its own product page shows the featured image, gallery, price, short description, full description tab, category and tags.

> **Note:** A standalone copy of this lab is in labs/lab-02-*.md so you can repeat it after the course. Your WooCommerce project stays available to you.

---


### Lab 3 — Create a Variable Product with Attributes and Variations

Objective: Maintain product web content that carries options, pricing and stock per variation (A4, K2, K4).

Goal: Most real products come in options. You define a custom attribute such as Size or Colour, generate the variations from it, then give each variation its own SKU, price, stock level and image — and verify the dropdowns work on the storefront.

**What you'll build**

A published variable product whose variations each carry their own price, SKU and stock   (Tools: Product data > Variable product · Attributes tab · Variations tab · Used for variations.)

![WooCommerce — Lab 3: Create a Variable Product with Attributes and Variations](courseware/assets/woo-virtual-product.png)

*WooCommerce — Lab 3: Create a Variable Product with Attributes and Variations*

**Why the business cares**

Variations keep one product page instead of five near-duplicates. That is cleaner content, better SEO, and far less maintenance when a price or description changes.

**Step-by-step**

1. Go to Products > Add New and enter a Title and Description as you did for the simple product.

   ```bash
   Title:  Premium Polo Shirt
   ```

2. In the Product data panel, change the dropdown from 'Simple product' to 'Variable product'. The price fields disappear — price now belongs to each variation, not the parent.

   ```bash
   Product data:  Variable product
   ```

3. Open the Attributes tab and click 'Add new'. Name the attribute and enter its values separated by a vertical bar. Tick 'Visible on the product page' and, critically, tick 'Used for variations'. Click Save attributes.

   ```bash
   Name: Size    Value(s):  Small | Medium | Large
   ```

4. Add a second attribute the same way so you can see how combinations multiply. Remember to tick 'Used for variations' for this one too, then Save attributes.

   ```bash
   Name: Colour   Value(s):  Black | White
   ```

5. Open the Variations tab. From the dropdown choose 'Generate variations' to create every combination automatically, and confirm the prompt. With 3 sizes and 2 colours you get 6 variations.

   ```bash
   Generate variations  →  6 variations created
   ```

6. Expand the first variation and enter its own SKU and Regular price. Repeat for every variation — a variation with no price cannot be purchased and will not appear in the dropdown.

   ```bash
   POLO-S-BLK 39.90 · POLO-M-BLK 39.90 · POLO-L-BLK 41.90
POLO-S-WHT 39.90 · POLO-M-WHT 39.90 · POLO-L-WHT 41.90
   ```

7. Within each variation tick 'Manage stock?' and set a Stock quantity, so each size/colour combination tracks its own inventory.

   ```bash
   Stock quantity:  25
   ```

8. Upload a variation image for at least one variation by clicking the image placeholder inside the expanded variation. The product image swaps when the customer selects that option.
9. Set the Default form values at the top of the Variations tab if you want a combination pre-selected when the page loads. Click Save changes.

   ```bash
   Default:  Size = Medium, Colour = Black
   ```

10. Assign the product to a category and tag, set the Product image and gallery, then click Publish.

   ```bash
   Category:  Apparel
   ```

11. Test on the front end: open the product page, choose a size and colour, and confirm the price, SKU, image and stock message update. Set one variation's stock to 0 and confirm it shows as out of stock.

**Test it**

Selecting each combination on the live product page updates the price and SKU, the variation image swaps where you set one, and a zero-stock variation is reported as unavailable.

> **Note:** A standalone copy of this lab is in labs/lab-03-*.md so you can repeat it after the course. Your WooCommerce project stays available to you.

---


### Lab 4 — Curate the Catalogue — Linked Products and CSV Import

Objective: Ensure smooth maintenance and consistent bulk updates of the product catalogue (A4, K2, K4).

Goal: Grow and maintain the catalogue efficiently. You organise categories and global attributes, link products together as up-sells and cross-sells to raise order value, then import a batch of products from a CSV file and export the catalogue for bulk editing.

**What you'll build**

A curated catalogue with categories, attributes, up-sells, cross-sells and CSV-imported products   (Tools: Products > Categories · Products > Attributes · Linked Products tab · Product CSV Importer/Exporter.)

![WooCommerce — Lab 4: Curate the Catalogue — Linked Products and CSV Import](courseware/assets/woo-linked-products.png)

*WooCommerce — Lab 4: Curate the Catalogue — Linked Products and CSV Import*

**Why the business cares**

Editing products one at a time does not scale. Bulk import and export is how a real store launches a catalogue, runs a seasonal price change, or syncs with a supplier feed.

**Step-by-step**

1. Go to Products > Categories. Add a category with a Name, an optional URL-friendly Slug, a Parent if it is a subcategory, a Description, a Display type and an Image.

   ```bash
   Name: Apparel   ·   Display type: Products
   ```

2. Add a child category by setting its Parent to the category you just created, to see how a hierarchy forms. Drag and drop the rows to reorder them — this order is used on the storefront.

   ```bash
   Name: Shirts   ·   Parent: Apparel
   ```

3. Go to Products > Attributes and create a global attribute that any product can reuse. Add a Name and Slug, enable Archives if you want a browsable page per term, choose a default sort order, and click Add attribute.

   ```bash
   Name: Material   ·   Sort order: Name
   ```

4. Click 'Configure terms' beside your new attribute and add its values. Global attributes are what the 'Filter Products by Attribute' widget uses for layered navigation.

   ```bash
   Terms:  Cotton, Polyester, Linen
   ```

5. Open one of your products and go to Product data > Linked Products. In the Upsells field, search for and add a more premium product. Up-sells display on the product page as a recommendation instead of the current item.

   ```bash
   Upsells:  Premium Polo Shirt
   ```

6. In the same panel add a complementary product to the Cross-sells field. Cross-sells are promoted in the cart, based on what the customer is already buying. Click Update.

   ```bash
   Cross-sells:  Cotton Cap
   ```

7. Understand related products: these are chosen automatically by WooCommerce from products sharing the same categories or tags. You influence them by how you categorise and tag, not by naming them directly.
8. Export your catalogue as a template: go to Products and click Export. Choose the columns and product types to include, then click 'Generate CSV' and open the downloaded file.

   ```bash
   Products > Export > Generate CSV
   ```

9. Open the sample product CSV supplied for this lab (labs/data/harbour-co-products.csv) in a spreadsheet. It contains five new Harbour & Co products — Linen Summer Shirt (LINEN-SHIRT-001, 49.90), Classic Denim Jacket (JACKET-DENIM-001, 89.90 on sale at 79.90), Canvas Tote Bag (TOTE-CANVAS-001, 24.90), Merino Wool Scarf (SCARF-MERINO-001, 34.90) and Leather Belt (BELT-LEATHER-001, 32.90) — each with a name, SKU, prices, categories, tags, stock and weight. Review the columns, then save it unchanged as CSV.

   ```bash
   Columns:  Name, SKU, Regular price, Sale price, Categories, Tags, Stock, Published
   ```

10. Go to Products and click Import. Choose harbour-co-products.csv, click Continue, review the column mapping WooCommerce proposes, then click 'Run the importer'. Do not refresh the browser while it runs.

   ```bash
   Products > Import > harbour-co-products.csv > Run the importer
   ```

11. Confirm the imported products appear in Products > All Products, then re-import the same file with 'Update existing products' ticked in the importer's advanced options to see how a bulk price change is applied.

**Test it**

Your store has a category hierarchy and a global attribute, one product shows an up-sell on its page and a cross-sell in the cart, and the CSV-imported products appear in the catalogue.

> **Note:** A standalone copy of this lab is in labs/lab-04-*.md so you can repeat it after the course. Your WooCommerce project stays available to you.

---


## Topic 03 — Manage Payments and Shipping  (LO4 · A3, K3 · Day 1 PM)

Online & offline payment methods · Gateways · Shipping zones · Flat rate, free shipping & local pickup

**Key concepts**

- Payment methods — Online gateways such as Stripe and PayPal, plus offline options like bank transfer, cheque and cash on delivery.
- Choosing a gateway — Location, fees, supported currencies and whether the customer stays on your site all shape the decision.
- Shipping zones — A zone is a geographic region; each zone carries its own shipping methods and rates.
- Flat rate shipping — A standard cost per order, per item or per shipping class, defined inside a shipping zone.
- Free shipping — A powerful incentive — commonly gated behind a minimum order amount or a valid coupon.
- Local pickup — Lets the customer collect the order themselves, with optional cost and tax status.


### Activity — Discussion — Recommend Payment and Shipping for Customer Experience  (15 minutes)

Working from the store you have built, recommend the payment and shipping mix that would give your customers the best experience — and justify the trade-offs.

**Discussion prompts**

- Which payment methods do your customers expect, and what does each one cost you?
- Does the customer stay on your site, or get redirected? Why does that matter for conversion?
- Would free shipping above a threshold raise your average order value or erode your margin?
- Which shipping zones do you actually serve, and what happens to orders outside them?

**What to produce**

A recommended payment and shipping configuration with the customer-experience reason for each choice.

> **Note:** Write your answer down as you go. The same reasoning is what the Oral Questioning asks you to demonstrate for K3.


### Lab 5 — Configure Payment Methods and Shipping Zones

Objective: Recommend and configure payment and shipping methods that improve customer experience (A3, K3).

Goal: Make the store able to take money and deliver goods. You enable offline and online payment methods, then build a shipping zone for your country and add flat rate, free shipping and local pickup to it — finishing with a test checkout that proves the whole path works.

**What you'll build**

A store that accepts payment and offers three shipping options, verified by a test checkout   (Tools: WooCommerce > Settings > Payments · Settings > Shipping · Shipping zones · Shipping classes.)

![WooCommerce — Lab 5: Configure Payment Methods and Shipping Zones](courseware/assets/woo-shipping.png)

*WooCommerce — Lab 5: Configure Payment Methods and Shipping Zones*

**Why the business cares**

Payment and shipping are where carts are abandoned. Every method you offer, and every rate you set, is a direct customer-experience decision with a measurable effect on conversion.

**Step-by-step**

1. Go to WooCommerce > Settings > Payments. You see the payment methods available to your store, each with a toggle.

   ```bash
   WooCommerce > Settings > Payments
   ```

2. Enable an offline method for classroom testing. Toggle on 'Cash on delivery', then click 'Set up' or Manage to give it a Title and Description — this is the text the customer sees at checkout.

   ```bash
   Title:  Cash on delivery
   ```

3. Enable 'Direct bank transfer (BACS)' and add your account details. Note that offline methods place the order 'On hold' until you confirm payment yourself.
4. Review the online gateways. Stripe supports 25+ countries and keeps the customer on your site; PayPal is active in 200+ countries; Square suits merchants who also sell in person. Choosing between them is a trade-off of fees, currencies, and whether the customer is redirected away.
5. Reorder the payment methods by dragging the rows. The order here is the order the customer sees at checkout — put the method you most want used at the top.
6. Go to WooCommerce > Settings > Shipping. Select the unit of measurement for weight and dimensions if you have not already, under the Shipping options sub-tab.

   ```bash
   Weight unit: kg   ·   Dimensions unit: cm
   ```

7. Click 'Add shipping zone'. Give the zone a name and choose the regions it covers. A zone is a geographic area that carries its own methods and rates.

   ```bash
   Zone name: Singapore   ·   Region: Singapore
   ```

8. Inside the zone click 'Add shipping method' and choose Flat rate. Click on it to edit: enter a Title shown at checkout, set the Tax status, and enter a Cost applied to the whole cart.

   ```bash
   Title: Standard Delivery   ·   Cost: 5.00
   ```

9. Add a second method to the zone: Free shipping. Edit it and set 'Free shipping requires…' to 'A minimum order amount', then enter the threshold. This is the classic lever for raising average order value.

   ```bash
   Requires: A minimum order amount   ·   Minimum: 100.00
   ```

10. Add a third method: Local pickup. Give it a Title, set its Tax status and a Cost of 0 so customers can collect the order themselves at no charge — Harbour & Co has a physical shop, so pickup is a genuine option for its customers.

   ```bash
   Title: Collect in store (71 Ayer Rajah Crescent)   ·   Cost: 0
   ```

11. Optionally create a shipping class under the Shipping classes sub-tab (for example 'Bulky'), assign it to a product on that product's Shipping tab, then give it its own cost inside the Flat rate settings.

   ```bash
   Class: Bulky   ·   Flat rate class cost: 15.00
   ```

12. Test the whole path: open your store in a private browser window, add the Classic Cotton T-Shirt (S$29.90) to the cart, and go to Checkout. Confirm all three shipping options appear, then place an order using Cash on delivery and check the order arrives in WooCommerce > Orders.

   ```bash
   Cart: 1 x Classic Cotton T-Shirt  S$29.90   ·   Standard Delivery  S$5.00
   ```

13. Add more products — for example the Classic Denim Jacket (S$89.90) and a Premium Polo Shirt — to push the cart above your S$100 free-shipping threshold and confirm Free shipping now appears as an option. This proves the rule is working as the customer will experience it.

   ```bash
   Cart total S$159.70  >  S$100  →  Free shipping appears
   ```


**Test it**

At checkout the store offers your payment methods and all three shipping options, free shipping appears only above the threshold you set, and a test order is created successfully.

> **Note:** A standalone copy of this lab is in labs/lab-05-*.md so you can repeat it after the course. Your WooCommerce project stays available to you.

---


## Topic 04 — Manage Sales on WooCommerce Store  (LO5 · A5, K5 · Day 1 PM)

Orders & order statuses · Editing single orders · Refunds & restocking · Coupons and promotions

**Key concepts**

- Orders and statuses — Pending, Processing, Completed, On-Hold, Cancelled, Refunded and Failed track an order's life.
- Managing orders — View, filter and edit orders; change status, edit line items, add fees and apply coupons.
- Adding orders manually — Phone and offline sales can be entered by hand and emailed to the customer for payment.
- Refunds — Refund manually or through the gateway, with the option to restock the returned items.
- Stock issues — Stock management, low-stock thresholds and out-of-stock handling prevent overselling.
- Coupons and promotions — Percentage, fixed cart and fixed product discounts, with usage limits and expiry dates.


### Lab 6 — Process Orders, Refunds and Coupons

Objective: Highlight and resolve issues related to sales, stock, refunds and promotions (A5, K5).

Goal: Run the store as a shop manager. You walk an order through its statuses, edit and manually create orders, issue a refund that restocks the item, then build a coupon and prove it applies at checkout — the day-to-day issue resolution the CMS is used for.

**What you'll build**

A processed order, a completed refund with restocking, and a working discount coupon   (Tools: WooCommerce > Orders · Order statuses · Refund · WooCommerce > Coupons · Checkout.)

![WooCommerce — Lab 6: Process Orders, Refunds and Coupons](courseware/assets/woo-single-order.png)

*WooCommerce — Lab 6: Process Orders, Refunds and Coupons*

**Why the business cares**

Orders, refunds and promotions are where customer problems surface. Resolving them quickly and correctly — with stock and revenue staying accurate — is the operational heart of the store.

**Step-by-step**

1. Go to WooCommerce > Orders. If you placed a test order in the previous lab it is listed here with an order number, customer name, date, status, address and total.

   ```bash
   WooCommerce > Orders
   ```

2. Click Screen Options at the top right to choose which columns and how many rows to display. Use the Preview 'eye' icon on an order row to see its contents without leaving the list.
3. Open the order by clicking its number. Review the three panels: Order data (status, customer, dates), Order items (products, quantities, totals) and Order notes on the right.
4. Work through the order statuses and note what each means: Pending payment (unpaid), Processing (paid, stock reduced, awaiting fulfilment), On hold (awaiting payment confirmation), Completed (fulfilled), Cancelled, Refunded and Failed.

   ```bash
   Status:  Processing  →  Completed
   ```

5. Change the status to Completed and click Update. Check Order notes — WooCommerce logs the status change, and a completion email is sent to the customer.
6. Create an order by hand, as you would for a phone or offline sale. Go to WooCommerce > Orders and click Add order. Set the customer — use the mock walk-in customer below — then click 'Add item(s)' to add products.

   ```bash
   Customer: Tan Wei Ling · tan.weiling@example.com
Billing: 8 Marina Boulevard, #12-04, Singapore 018981
Items: 1 x Merino Wool Scarf (S$34.90) · 1 x Leather Belt (S$32.90)
   ```

7. With line items added, click 'Recalculate' so WooCommerce works out the totals and tax. Set the status to Pending payment and Create the order.
8. Use the Order actions dropdown to send 'Email invoice / order details to customer', which gives them payment instructions for the manual order.

   ```bash
   Order actions:  Email invoice / order details to customer
   ```

9. Issue a refund. Open a Completed or Processing order and click the Refund button below the line items. Enter the quantity or amount to refund and add a refund reason.

   ```bash
   Refund: 1 x Classic Cotton T-Shirt  S$29.90   ·   Reason: wrong size delivered
   ```

10. Tick 'Restock refunded items' so the returned stock goes back into inventory, then click 'Refund manually'. Manual refund records the refund in WooCommerce; a gateway refund would also return the money automatically.

   ```bash
   Restock refunded items: ticked  →  Refund manually
   ```

11. Verify the stock movement: open the refunded product and confirm its Inventory quantity has increased, and check the order notes for the refund entry.
12. Enable coupons if they are not already on. Go to WooCommerce > Settings > General and tick 'Enable the use of coupon codes', then save.

   ```bash
   Settings > General > Enable coupons
   ```

13. Go to Marketing > Coupons (WooCommerce > Coupons on older versions) and click Add coupon. Enter or generate a Coupon code and a Description for internal reference.

   ```bash
   Code:  WELCOME10
   ```

14. On the General tab choose the Discount type and amount. Percentage discount takes a share of the qualifying items; Fixed cart discount takes a flat sum off the whole cart; Fixed product discount takes a set amount off each qualifying item. Set an expiry date and tick 'Allow free shipping' if appropriate.

   ```bash
   Discount type: Percentage discount   ·   Amount: 10
   ```

15. On the Usage restriction tab set a Minimum spend and any product or category limits. On the Usage limits tab set 'Usage limit per coupon' and 'Usage limit per user' so the promotion cannot be abused. Publish the coupon.

   ```bash
   Minimum spend: 50   ·   Usage limit per user: 1
   ```

16. Test the promotion: open the store in a private window, add products to the cart, and apply your coupon code at the cart or checkout. Confirm the discount is deducted and complete the checkout.

   ```bash
   Apply coupon:  WELCOME10
   ```

17. Return to WooCommerce > Orders, open the new order and confirm the coupon is recorded against it. Check Marketing > Coupons to see the usage count has incremented.

**Test it**

You have moved an order to Completed, created an order manually, refunded an item with stock restored, and redeemed a coupon at checkout that shows on the resulting order.

> **Note:** A standalone copy of this lab is in labs/lab-06-*.md so you can repeat it after the course. Your WooCommerce project stays available to you.

---


## Topic 05 — Manage WooCommerce Performance  (LO6 · A2, K6, K7 · Day 1 PM)

Sales reports · Customer & stock reports · Dashboard widgets · eCommerce metrics · Google Analytics

**Key concepts**

- WooCommerce Reports — Orders, Customers, Stock and Taxes — the built-in view of how the store is performing.
- Sales reports — Gross and net sales by date, product and category, plus top sellers, top earners and coupon usage.
- Customer and stock reports — Customers versus guests, and low-stock, out-of-stock and on-backorder items.
- Dashboard widgets — At-a-glance store status on the WordPress dashboard, configurable through Screen Options.
- eCommerce metrics — Conversion rate, traffic, revenue by source, retention, repeat purchase and refund rate.
- Google Analytics — Integrating analytics attributes revenue to channels and shows where customers drop off.


### Activity — Discussion — Metrics to Measure Store Performance  (15 minutes)

Decide which metrics you would use to judge whether the store is succeeding, and what criteria make a metric worth tracking at all.

**Discussion prompts**

- Which three metrics would you put in front of the business owner every week?
- What makes a metric useful — is it actionable, comparable, and tied to a decision?
- What does a rising refund rate or a falling repeat-customer rate actually tell you?
- Which report or tool produces each metric — WooCommerce Reports or Google Analytics?

**What to produce**

A shortlist of performance metrics with the criteria used to select them and their data source.

> **Note:** Write your answer down as you go. The same reasoning is what the Oral Questioning asks you to demonstrate for K6 and K7.


### Lab 7 — Measure Store Performance with Reports and Analytics

Objective: Develop and review metrics to measure the performance of the store (A2, K6, K7).

Goal: Turn the store's activity into evidence. You read the Orders, Customers, Stock and Taxes reports, arrange the dashboard widgets a manager would want, install the Google Analytics integration, and select the handful of metrics you would actually use to judge whether the store is succeeding.

**What you'll build**

A reviewed set of store reports, a configured dashboard, and a defined list of performance metrics   (Tools: WooCommerce > Reports · Analytics · Dashboard widgets · Screen Options · Google Analytics plugin.)

![WooCommerce — Lab 7: Measure Store Performance with Reports and Analytics](courseware/assets/woo-reports.png)

*WooCommerce — Lab 7: Measure Store Performance with Reports and Analytics*

**Why the business cares**

Metrics are only useful if they change a decision. Choosing which few to track — and knowing what each one would tell you — is what separates a measured store from a busy one.

**Step-by-step**

1. Go to WooCommerce > Reports. The reports are grouped into four tabs: Orders, Customers, Stock and Taxes.

   ```bash
   WooCommerce > Reports
   ```

2. On the Orders tab open 'Sales by date'. Switch between Year, Last month, This month and Last 7 days, and note gross sales, net sales, orders placed and items purchased. Use the Custom range to pick your own dates.

   ```bash
   Orders > Sales by date > Last 7 days
   ```

3. Open 'Sales by product'. Search for one of your products to see its sales volume, then review the Top sellers, Top freebies and Top earners lists on the right — these tell you what to promote and what to stock. After the day's test orders, the Classic Cotton T-Shirt should appear among your top sellers.

   ```bash
   Sales by product > Search:  Classic Cotton T-Shirt
   ```

4. Open 'Sales by category' and 'Coupons by date'. Coupon reports show which promotions were actually redeemed and how much discount they cost you — the direct measure of a campaign's uptake.
5. Go to the Customers tab. 'Customers vs. Guests' compares registered purchasers against one-off guest checkouts; the Customer list shows who your buyers are. A high guest ratio suggests account creation is a barrier.
6. Go to the Stock tab and review Low in stock, Out of stock and Most stocked. Out-of-stock items on a live storefront are lost revenue and a content issue you should be resolving proactively.

   ```bash
   Stock > Low in stock
   ```

7. If your store has WooCommerce Analytics (bundled in current versions), open Analytics > Overview. It offers the same data with more flexible filtering, comparison against a previous period, and downloadable CSVs.

   ```bash
   Analytics > Overview
   ```

8. Go to the WordPress Dashboard. WooCommerce adds a Status widget summarising the store. Click Screen Options at the top right to show or hide widgets and set the number of columns.

   ```bash
   Dashboard > Screen Options
   ```

9. Drag the widgets to arrange the dashboard so the information a shop manager needs is visible without scrolling. This is a small but real content-management decision about what matters most.
10. Install the analytics integration: go to Plugins > Add New, search for 'WooCommerce Google Analytics Integration', then Install and Activate it.

   ```bash
   Plugins > Add New > WooCommerce Google Analytics Integration
   ```

11. Configure it under WooCommerce > Settings > Integration > Google Analytics. Enter your Google Analytics measurement ID and enable the eCommerce tracking options you need, then save.

   ```bash
   Measurement ID:  G-XXXXXXXXXX
   ```

12. Review the free plugins WooCommerce recommends for extending measurement and marketing: WooCommerce Admin for richer reporting, Mailchimp for WooCommerce for email campaigns, and Facebook for WooCommerce for social channels.
13. Define your metric set. Write down the metrics you would report weekly and, for each, the criteria that justify it: is it actionable, comparable over time, and tied to a decision? Draw from sales, conversion rate, website traffic, revenue by traffic source, email click-through rate, organic acquisition, social engagement, customer retention, repeat customer rate, refund and return rate, and email subscription rate.
14. For each chosen metric, record where it comes from — WooCommerce Reports, WooCommerce Analytics, or Google Analytics — and what value would prompt you to act. A metric with no threshold and no owner will not change anything.

**Test it**

You can produce a sales figure for a chosen period, name your top-selling product, identify any low-stock items, and present a short list of performance metrics with their source and the criteria used to select them.

> **Note:** A standalone copy of this lab is in labs/lab-07-*.md so you can repeat it after the course. Your WooCommerce project stays available to you.

---


## Putting It Together — Running a Store End to End

By the end of the day you should be able to carry one product through the whole arc of the course. This is the reasoning the assessment is built around:

1. Set up and govern the store: install WooCommerce, apply a theme, set the currency and tax treatment, and decide who may publish what. You did this in Lab 1. (A1, K1)
2. Create and curate the content: add a product with a description, images, category and tags, then build a variable product whose variations carry their own price and stock. Labs 2 and 3. (A6, K2, K4)
3. Maintain the catalogue at scale: link up-sells and cross-sells, and import or update products in bulk from a CSV file. Lab 4. (A4, K2, K4)
4. Make it purchasable: recommend and configure the payment methods and shipping zones that give your customers the best experience, then prove it with a test checkout. Lab 5. (A3, K3)
5. Resolve the day-to-day issues: move an order through its statuses, refund an item and restock it, and run a coupon promotion that applies correctly at checkout. Lab 6. (A5, K5)
6. Measure whether it works: read the sales, customer and stock reports, connect analytics, and choose the metrics you would actually report — with the criteria that justify each one. Lab 7. (A2, K6, K7)

> **Note:** If you can work through these six steps for your own store, you are ready for both the Oral Questioning and the Practical Performance.


## Troubleshooting the Labs

- A setting will not take effect — you almost certainly did not click Save changes. WooCommerce settings screens never save automatically.
- The product does not appear in the shop — check that it is Published (not a draft), that its Catalog visibility is 'Shop and search', and that it has a price. A product with no price cannot be purchased.
- A variation cannot be selected on the front end — every variation needs its own Regular price. Variations left without a price are hidden from the dropdown.
- The attribute does not generate variations — you must tick 'Used for variations' on the Attributes tab and click Save attributes before opening the Variations tab.
- No shipping option appears at checkout — confirm the customer's address falls inside a shipping zone that has at least one shipping method added to it.
- Free shipping never shows — check the 'Free shipping requires…' condition and that the cart total actually exceeds the minimum order amount you set.
- The coupon is rejected — confirm coupons are enabled under Settings > General, that the code matches exactly, and that the cart meets any minimum spend or product restriction.
- The CSV import fails or creates duplicates — check the column mapping screen before running the importer, and tick 'Update existing products' when you intend to update rather than create.
- Reports look empty — the built-in reports only count orders in a paid status, so place and complete a test order first.


## Glossary

- **Attribute** — A characteristic of a product such as Size or Colour. Global attributes power layered navigation and are required to create variations.
- **Backorder** — Allowing a product to be ordered when its stock has reached zero, to be fulfilled later.
- **Catalog visibility** — Where a product appears — shop and search, shop only, search only, or hidden.
- **Category** — A hierarchical grouping of products. Every product must belong to at least one; unassigned products fall into 'Uncategorized'.
- **Checkout** — The page where the customer supplies their details, chooses shipping and payment, and places the order.
- **CMS (Content Management System)** — Software for creating, editing, curating and publishing web content — here, WordPress with WooCommerce.
- **Coupon** — A code that applies a percentage, fixed cart or fixed product discount, optionally with limits, restrictions and an expiry date.
- **Cross-sell** — A complementary product promoted on the cart page, based on what the customer is already buying.
- **CSV importer / exporter** — The built-in tool for creating or updating many products at once from a comma-separated file.
- **Downloadable product** — A product delivered as a file after purchase, with an optional download limit and expiry.
- **Gateway** — A payment service such as Stripe, PayPal or Square that processes the customer's payment.
- **Grouped product** — A collection of related simple products that are purchased individually.
- **Order status** — The stage an order has reached — pending payment, processing, completed, on hold, cancelled, refunded or failed.
- **Permalink / slug** — The URL-friendly version of a name, used in the address of a product, category or tag.
- **Product Data panel** — The metabox on the product edit screen holding the General, Inventory, Shipping, Linked Products and Attributes tabs.
- **Related products** — Products shown automatically because they share categories or tags with the current product.
- **Restock** — Returning refunded items to inventory so the stock figure stays accurate.
- **Shipping class** — A grouping of products that share a shipping cost — for example bulky or fragile items.
- **Shipping zone** — A geographic region with its own shipping methods and rates.
- **Shortcode** — A bracketed tag such as [woocommerce_cart] that renders WooCommerce content inside a post or page.
- **Simple product** — A standard shipped product with no options — the majority of a typical catalogue.
- **SKU** — Stock Keeping Unit — the unique internal code identifying a product or variation.
- **Storefront** — The official WooCommerce theme, built to work with every core feature.
- **Tag** — A flat, non-hierarchical label used to relate products across categories.
- **Taxonomy** — A way of grouping content. WooCommerce adds product categories, tags and attributes to WordPress.
- **Up-sell** — A higher-value or better-quality product recommended on the product page instead of the current item.
- **Variable product** — A product with variations, each of which may carry its own SKU, price, stock level and image.
- **Variation** — One purchasable combination of a variable product's attributes, for example Size = Medium, Colour = Black.
- **Virtual product** — A product that requires no shipping, such as a service.
- **Widget** — A block of content placed in a theme's widget area — product lists, filters, categories, cart or search.
- **WooCommerce Blocks** — Gutenberg blocks that display products by category, tag, attribute, rating or sales inside any post or page.
