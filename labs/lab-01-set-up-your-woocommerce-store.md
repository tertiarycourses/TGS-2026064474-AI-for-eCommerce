# Lab 1 — Set Up Your WooCommerce Store

**Course:** Building a Successful eCommerce Store with WooCommerce (TGS-2026064474)  
**Topic 01:** Overview of WooCommerce CMS  
**Objective:** Set up and monitor a WooCommerce CMS so it adheres to store guidelines and policies (A1, K1).  
**Platform:** WooCommerce — https://woocommerce.com

## Goal

Install the WooCommerce plugin on a WordPress site, work through the setup wizard to define the store's location, currency and industry, then apply the Storefront theme and confirm the shop, cart, checkout and My Account pages have been created. You finish by setting the currency and tax options that every price in the store will follow.

## What you'll build

A working WooCommerce store with its currency, tax and core pages configured

*Uses: Plugins > Add New · WooCommerce Setup Wizard · Appearance > Themes · WooCommerce > Settings.*

![WooCommerce — Lab 1](../courseware/assets/woo-setup-wizard.png)

## Why the business cares

The setup wizard is where store-wide policy is set. Currency, tax treatment and page structure decide how every product is priced and presented — getting them right first avoids re-pricing an entire catalogue later.

## Prerequisites

- Your assigned demo WordPress site — one of **wp1.tertiarytraining.com – wp5.tertiarytraining.com** — with administrator access. Log in at `/wp-admin` (for example `https://wp1.tertiarytraining.com/wp-admin`) with username `admin` and password `admin12345`.
- A modern browser. A second private/incognito window is useful for viewing the storefront as a customer while you edit as the administrator.
- Product images and, for the catalogue labs, the sample product CSV ([data/harbour-co-products.csv](data/harbour-co-products.csv)).

## Step-by-step

### Step 1 — Log in to your assigned demo WordPress site as an administrator. Each learner is assigned one of the five demo training sites wp1.tertiarytraining.com to wp5.tertiarytraining.com — open your site's /wp-admin login page and sign in with the classroom credentials. The demo hosting already meets the WooCommerce requirements: PHP 7.2 or greater, MySQL 5.6+ (or MariaDB 10.0+), a WordPress memory limit of 128 MB or greater, and HTTPS support.

```bash
https://wp1.tertiarytraining.com/wp-admin   ·   Username: admin   ·   Password: admin12345
```

### Step 2 — Go to Plugins > Add New and search for 'WooCommerce'. Check that the author is Automattic, then click Install Now followed by Activate.

```bash
Plugins > Add New > search: WooCommerce
```

### Step 3 — The WooCommerce Setup Wizard opens automatically on first activation. Click Let's go! to begin. (Choosing 'Not right now' lets you configure the store manually from WooCommerce > Settings instead.)

### Step 4 — On the Store Details step enter the store's address, city, country/region and postcode, then choose the currency the store will price in and the type of product you plan to sell (physical, downloadable, or both). Throughout today's labs you are building the demo store 'Harbour & Co', a small Singapore apparel and accessories retailer going online.

```bash
Store: Harbour & Co   ·   Address: 71 Ayer Rajah Crescent, #02-18, Singapore 139951
Country: Singapore   ·   Currency: Singapore dollar (S$)   ·   Products: physical
```

### Step 5 — Indicate whether you also sell goods and services in person — this determines which payment gateways the wizard offers you.

### Step 6 — Complete the remaining wizard steps and finish. WooCommerce creates the Shop, Cart, Checkout and My Account pages, and adds its product post types and taxonomies to WordPress.

### Step 7 — Verify the pages exist: go to Pages and confirm Shop, Cart, Checkout and My Account are listed. These pages hold the WooCommerce shortcodes, for example [woocommerce_cart] and [woocommerce_checkout].

```bash
Pages > Shop · Cart · Checkout · My Account
```

### Step 8 — Apply a WooCommerce-compatible theme. Go to Appearance > Themes > Add New, search for 'Storefront', then Install and Activate it. Storefront is the official WooCommerce theme and is built to work with every core feature.

```bash
Appearance > Themes > Add New > Storefront
```

### Step 9 — Confirm the store currency. Go to WooCommerce > Settings > General > Currency options and set the Currency, Currency position, Thousand separator, Decimal separator and Number of decimals.

```bash
Currency position: Left ($99.99)   ·   Decimals: 2
```

### Step 10 — Enable taxes. Still on WooCommerce > Settings > General, tick 'Enable taxes and tax calculations' and save changes. A Tax tab now appears in the settings.

```bash
WooCommerce > Settings > General > Enable taxes
```

### Step 11 — Open WooCommerce > Settings > Tax and set 'Prices entered with tax'. Choosing inclusive means catalogue prices already contain the base tax rate; exclusive means tax is added at checkout. This decision governs how you enter every product price from now on.

```bash
Prices entered with tax:  Yes, I will enter prices inclusive of tax
```

### Step 12 — Review the user roles that WooCommerce added — Customer and Shop Manager — under Users > All Users. Note which role may publish products and which may only manage orders; this is the permissions basis for your store's content management policy.

```bash
Users > All Users > Role: Shop manager
```

## Test it

Your WordPress site has WooCommerce active, the Storefront theme applied, the four WooCommerce pages created, and the store currency and tax options saved. Visiting /shop shows an empty but working storefront.

---
*© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved. · www.tertiarycourses.com.sg*
