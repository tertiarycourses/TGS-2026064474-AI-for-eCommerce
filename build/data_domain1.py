"""
Topic 1 — Overview of WooCommerce CMS (LO1 / A1, K1).

Lab 1: install and configure WooCommerce, run the setup wizard, and set the
store's general, currency and tax options so the store adheres to the
content-management policies and guidelines agreed for it.

The `steps` here drive the LEARNER GUIDE and the labs/*.md files only.
The slide deck shows the lab OVERVIEW + OUTCOME visually — never the steps.
"""

DOMAIN1 = [
    dict(
        num=1,
        topic=1,
        title="Set Up Your WooCommerce Store",
        image="woo-setup-wizard.png",
        objective="Set up and monitor a WooCommerce CMS so it adheres to store guidelines and policies (A1, K1).",
        desc=("Install the WooCommerce plugin on a WordPress site, work through the setup wizard to define the "
              "store's location, currency and industry, then apply the Storefront theme and confirm the shop, "
              "cart, checkout and My Account pages have been created. You finish by setting the currency and "
              "tax options that every price in the store will follow."),
        build="A working WooCommerce store with its currency, tax and core pages configured",
        services="Plugins > Add New · WooCommerce Setup Wizard · Appearance > Themes · WooCommerce > Settings",
        business=("The setup wizard is where store-wide policy is set. Currency, tax treatment and page structure "
                  "decide how every product is priced and presented — getting them right first avoids re-pricing "
                  "an entire catalogue later."),
        steps=[
            ("Log in to your assigned demo WordPress site as an administrator. Each learner is assigned one of the five demo training sites wp1.tertiarytraining.com to wp5.tertiarytraining.com — open your site's /wp-admin login page and sign in with the classroom credentials. The demo hosting already meets the WooCommerce requirements: PHP 7.2 or greater, MySQL 5.6+ (or MariaDB 10.0+), a WordPress memory limit of 128 MB or greater, and HTTPS support.", "https://wp1.tertiarytraining.com/wp-admin   ·   Username: admin   ·   Password: admin12345"),
            ("Go to Plugins > Add New and search for 'WooCommerce'. Check that the author is Automattic, then click Install Now followed by Activate.", "Plugins > Add New > search: WooCommerce"),
            ("The WooCommerce Setup Wizard opens automatically on first activation. Click Let's go! to begin. (Choosing 'Not right now' lets you configure the store manually from WooCommerce > Settings instead.)", ""),
            ("On the Store Details step enter the store's address, city, country/region and postcode, then choose the currency the store will price in and the type of product you plan to sell (physical, downloadable, or both). Throughout today's labs you are building the demo store 'Harbour & Co', a small Singapore apparel and accessories retailer going online.", "Store: Harbour & Co   ·   Address: 71 Ayer Rajah Crescent, #02-18, Singapore 139951\nCountry: Singapore   ·   Currency: Singapore dollar (S$)   ·   Products: physical"),
            ("Indicate whether you also sell goods and services in person — this determines which payment gateways the wizard offers you.", ""),
            ("Complete the remaining wizard steps and finish. WooCommerce creates the Shop, Cart, Checkout and My Account pages, and adds its product post types and taxonomies to WordPress.", ""),
            ("Verify the pages exist: go to Pages and confirm Shop, Cart, Checkout and My Account are listed. These pages hold the WooCommerce shortcodes, for example [woocommerce_cart] and [woocommerce_checkout].", "Pages > Shop · Cart · Checkout · My Account"),
            ("Apply a WooCommerce-compatible theme. Go to Appearance > Themes > Add New, search for 'Storefront', then Install and Activate it. Storefront is the official WooCommerce theme and is built to work with every core feature.", "Appearance > Themes > Add New > Storefront"),
            ("Confirm the store currency. Go to WooCommerce > Settings > General > Currency options and set the Currency, Currency position, Thousand separator, Decimal separator and Number of decimals.", "Currency position: Left ($99.99)   ·   Decimals: 2"),
            ("Enable taxes. Still on WooCommerce > Settings > General, tick 'Enable taxes and tax calculations' and save changes. A Tax tab now appears in the settings.", "WooCommerce > Settings > General > Enable taxes"),
            ("Open WooCommerce > Settings > Tax and set 'Prices entered with tax'. Choosing inclusive means catalogue prices already contain the base tax rate; exclusive means tax is added at checkout. This decision governs how you enter every product price from now on.", "Prices entered with tax:  Yes, I will enter prices inclusive of tax"),
            ("Review the user roles that WooCommerce added — Customer and Shop Manager — under Users > All Users. Note which role may publish products and which may only manage orders; this is the permissions basis for your store's content management policy.", "Users > All Users > Role: Shop manager"),
        ],
        test=("Your WordPress site has WooCommerce active, the Storefront theme applied, the four WooCommerce pages "
              "created, and the store currency and tax options saved. Visiting /shop shows an empty but working "
              "storefront."),
    ),
]
