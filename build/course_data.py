"""
SINGLE SOURCE OF TRUTH — AI for eCommerce.

WSQ Course Code: TGS-2026064474
TSC: RET-CIE-4002-1.1 Content Management System Utilisation (Level 4)

Content is carried over from the approved v14 Master Trainer Slides
("WSQ - Master Trainer Slides - Building a Successful eCommerce Store with
WooCommerce - v14.pptx", course code TGS-2020503869) and re-authored into the
current Tertiary Infotech house style: an all-white, highly visual deck built
from tile grids, flow diagrams, stat bands, card grids and product screenshots
rather than bullet walls.

Every artifact — the slide deck (PPT), Lesson Plan (LP), Learner Guide (LG) and
the labs/ folder — is generated from the data in this module plus
data_domain1.py … data_domain5.py, so titles, learning-unit numbering,
activities, learning outcomes and the schedule can never drift apart.

Course structure: ONE training day of 8 hours, plus a 1.5-hour final
assessment, per the approved Assessment Plan (CRS-Q-0040881-RET v1.0):
Practical Performance 75 min + Oral Questioning 15 min.

STEP-BY-STEP RULE: the `steps` in each domain module drive the LEARNER GUIDE
and labs/*.md ONLY. The slide deck shows each lab's OVERVIEW and OUTCOME
visually — never the numbered steps.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "AI for eCommerce"
SHORT_TITLE  = "AI for eCommerce"
COURSE_CODE  = "TGS-2026064474"
VERSION      = "v15.2"
VERSION_DATE = "28 September 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
DAYS         = 1

# TSC reference (printed on the Skills Framework slide + LP/LG)
TSC_TITLE = "Content Management System Utilisation"
TSC_CODE  = "RET-CIE-4002-1.1"
TSC_DESC  = ("Manage the utilisation of content management systems to create, edit, curate and publish web "
             "content, monitor adherence to content management policies and guidelines, measure system "
             "performance, and recommend improvements to the organisation's web properties and assets.")

# The platform every lab runs on
PLATFORM      = "WooCommerce"
PLATFORM_URL  = "https://woocommerce.com"
PLATFORM_DOCS = "https://woocommerce.com/documentation/"
PLATFORM_REPO = "https://wordpress.org/plugins/woocommerce/"

# The environment used in class
HARDWARE      = "WordPress + WooCommerce"
HARDWARE_ALT  = "WooCommerce Storefront theme"

# Demo WordPress training sites for the hands-on labs — one site per learner,
# assigned by the trainer at the start of class. All five carry a fresh
# WordPress install and are reset before each class run.
LAB_SITES       = [f"wp{i}.tertiarytraining.com" for i in range(1, 6)]
LAB_SITES_RANGE = "wp1.tertiarytraining.com – wp5.tertiarytraining.com"
LAB_LOGIN_PATH  = "/wp-admin"
LAB_USER        = "admin"
LAB_PASS        = "admin12345"
LAB_LOGIN_EXAMPLE = "https://wp1.tertiarytraining.com/wp-admin   ·   Username: admin   ·   Password: admin12345"

# The demo store every lab builds — the same retailer the Practical Performance
# scenario uses, so the labs are a direct rehearsal of the assessment.
STORE_NAME    = "Harbour & Co"
STORE_TAGLINE = "a small Singapore apparel and accessories retailer going online"
STORE_ADDRESS = "71 Ayer Rajah Crescent, #02-18, Singapore 139951"

# Harbour & Co demo catalogue — the mock products used across Labs 2-7.
# (name, sku, regular, sale, category, tags, stock, weight_kg)
STORE_PRODUCTS = [
    ("Classic Cotton T-Shirt", "TSHIRT-CLASSIC-001", "29.90", "24.90", "Apparel > Shirts",   "cotton, unisex, casual",   "50", "0.2"),
    ("Premium Polo Shirt",     "POLO-PREMIUM-001",   "39.90", "",      "Apparel > Shirts",   "polo, smart-casual",       "25", "0.25"),
    ("Cotton Cap",             "CAP-COTTON-001",     "19.90", "",      "Accessories",         "cotton, cap, everyday",    "60", "0.1"),
]
# Rows shipped in the sample import CSV (labs/data) used in Lab 4.
STORE_CSV_NAME = "harbour-co-products.csv"
STORE_CSV_PRODUCTS = [
    ("Linen Summer Shirt",   "LINEN-SHIRT-001",  "49.90", "",      "Apparel > Shirts",     "linen, summer, breathable", "40", "0.25"),
    ("Classic Denim Jacket", "JACKET-DENIM-001", "89.90", "79.90", "Apparel > Outerwear",  "denim, unisex",             "25", "0.7"),
    ("Canvas Tote Bag",      "TOTE-CANVAS-001",  "24.90", "",      "Accessories",           "canvas, eco, everyday",     "60", "0.3"),
    ("Merino Wool Scarf",    "SCARF-MERINO-001", "34.90", "",      "Accessories",           "merino, winter, travel",    "35", "0.15"),
    ("Leather Belt",         "BELT-LEATHER-001", "32.90", "",      "Accessories",           "leather, formal",           "45", "0.2"),
]
# The mock customer and promotion used in the sales-management lab (Lab 6).
STORE_CUSTOMER = "Tan Wei Ling · tan.weiling@example.com · 8 Marina Boulevard, #12-04, Singapore 018981"
STORE_COUPON   = "WELCOME10 — 10% percentage discount · minimum spend S$50 · one use per customer"

# Prerequisite stated on the deck
PREREQUISITE = "Basic WordPress operation is assumed in this course."

# ------------------------------------------------------------------ TSC abilities & knowledge
ABILITIES = [
    ("A1", "Monitor adherence to content management policies, guidelines and permissions on content management"),
    ("A2", "Develop and review metrics to measure performance of content management systems"),
    ("A3", "Recommend areas for improvements for a better customer experience in terms of organisation's web properties and assets"),
    ("A4", "Ensure smooth maintenance and consistent updates of content management systems"),
    ("A5", "Highlight and resolve issues related to content management systems"),
    ("A6", "Edit and curate web content"),
]
KNOWLEDGE = [
    ("K1", "Content management policies, guidelines and permissions on content management"),
    ("K2", "Web content for deployment"),
    ("K3", "Organisation's web properties and assets"),
    ("K4", "Creation and curation of web content guidelines"),
    ("K5", "Web content and platform management systems"),
    ("K6", "Types of performance metrics of content management systems"),
    ("K7", "Criteria for evaluating metrics to measure performance of content management systems"),
]

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Setup and monitor WooCommerce CMS to ensure adherence to guidelines and policies. (A1, K1)",
    "LO2: Edit and curate product website on WooCommerce CMS. (A6, K2, K4)",
    "LO3: Maintain product web content on WooCommerce CMS. (A4, K2, K4)",
    "LO4: Recommend payment and shipping methods on WooCommerce CMS to improve customer experience. (A3, K3)",
    "LO5: Manage issues related to WooCommerce CMS such as sales, out-of-stock, promotion etc. (A5, K5)",
    "LO6: Manage WooCommerce CMS performance. (A2, K6, K7)",
]

# ------------------------------------------------------------------ topics (= learning units)
TOPICS = [
    dict(num=1, code="01",
         title="Overview of WooCommerce CMS",
         subtitle="What WooCommerce is · Setup wizard · Themes · Widgets & shortcodes · Settings, currency & tax",
         weighting="LO1 · A1, K1 · Day 1 AM",
         concepts=[
            ("What WooCommerce is", "An open-source, fully customisable eCommerce platform built on WordPress, powering a large share of the world's online stores."),
            ("Six steps to a store", "Choose hosting, install WordPress, pick a theme, activate WooCommerce, run the setup wizard, then extend with plugins."),
            ("System requirements", "PHP 7.2+, MySQL 5.6+ or MariaDB 10.0+, a 128 MB WordPress memory limit, and HTTPS support."),
            ("Taxonomies and post types", "WooCommerce adds its own post types and taxonomies to WordPress to group and structure products."),
            ("Themes and widgets", "The theme sets the storefront's look; widgets surface products, filters and categories in widgetised areas."),
            ("Settings, currency and tax", "General, Products, Tax, Shipping, Payments and Privacy settings define how the store behaves and prices goods."),
         ]),
    dict(num=2, code="02",
         title="Manage Products on WooCommerce Store",
         subtitle="Product types · Images & galleries · Variations · Categories, tags & attributes · Up-sells · CSV import",
         weighting="LO2, LO3 · A4, A6, K2, K4 · Day 1 AM/PM",
         concepts=[
            ("Product types", "Simple, Grouped, Virtual, Downloadable, External/Affiliate and Variable each model a different kind of offer."),
            ("The Product Data panel", "General, Inventory, Shipping, Linked Products and Attributes — where the substance of a product is defined."),
            ("Images and galleries", "A featured image plus a gallery, with catalogue visibility controlling where the product appears."),
            ("Categories, tags, attributes", "Categories are hierarchical, tags are flat, and attributes drive filtering and product variations."),
            ("Up-sells and cross-sells", "Up-sells appear on the product page; cross-sells appear in the cart; related products are automatic."),
            ("CSV import and export", "Create or update hundreds of products in one pass, including variations, from a single CSV file."),
         ]),
    dict(num=3, code="03",
         title="Manage Payments and Shipping",
         subtitle="Online & offline payment methods · Gateways · Shipping zones · Flat rate, free shipping & local pickup",
         weighting="LO4 · A3, K3 · Day 1 PM",
         concepts=[
            ("Payment methods", "Online gateways such as Stripe and PayPal, plus offline options like bank transfer, cheque and cash on delivery."),
            ("Choosing a gateway", "Location, fees, supported currencies and whether the customer stays on your site all shape the decision."),
            ("Shipping zones", "A zone is a geographic region; each zone carries its own shipping methods and rates."),
            ("Flat rate shipping", "A standard cost per order, per item or per shipping class, defined inside a shipping zone."),
            ("Free shipping", "A powerful incentive — commonly gated behind a minimum order amount or a valid coupon."),
            ("Local pickup", "Lets the customer collect the order themselves, with optional cost and tax status."),
         ]),
    dict(num=4, code="04",
         title="Manage Sales on WooCommerce Store",
         subtitle="Orders & order statuses · Editing single orders · Refunds & restocking · Coupons and promotions",
         weighting="LO5 · A5, K5 · Day 1 PM",
         concepts=[
            ("Orders and statuses", "Pending, Processing, Completed, On-Hold, Cancelled, Refunded and Failed track an order's life."),
            ("Managing orders", "View, filter and edit orders; change status, edit line items, add fees and apply coupons."),
            ("Adding orders manually", "Phone and offline sales can be entered by hand and emailed to the customer for payment."),
            ("Refunds", "Refund manually or through the gateway, with the option to restock the returned items."),
            ("Stock issues", "Stock management, low-stock thresholds and out-of-stock handling prevent overselling."),
            ("Coupons and promotions", "Percentage, fixed cart and fixed product discounts, with usage limits and expiry dates."),
         ]),
    dict(num=5, code="05",
         title="Manage WooCommerce Performance",
         subtitle="Sales reports · Customer & stock reports · Dashboard widgets · eCommerce metrics · Google Analytics",
         weighting="LO6 · A2, K6, K7 · Day 1 PM",
         concepts=[
            ("WooCommerce Reports", "Orders, Customers, Stock and Taxes — the built-in view of how the store is performing."),
            ("Sales reports", "Gross and net sales by date, product and category, plus top sellers, top earners and coupon usage."),
            ("Customer and stock reports", "Customers versus guests, and low-stock, out-of-stock and on-backorder items."),
            ("Dashboard widgets", "At-a-glance store status on the WordPress dashboard, configurable through Screen Options."),
            ("eCommerce metrics", "Conversion rate, traffic, revenue by source, retention, repeat purchase and refund rate."),
            ("Google Analytics", "Integrating analytics attributes revenue to channels and shows where customers drop off."),
         ]),
]

# ------------------------------------------------------------------ discussion activities
DISCUSSIONS = [
    dict(topic=1, code="D1", knowledge="K1",
         title="Discussion — Content Management Policies for Your Store",
         mins=15,
         brief=("In pairs, consider a store you would run. Decide what content management policies, guidelines and "
                "user permissions it needs, and how you would monitor that people actually follow them."),
         prompts=[
            "Who should be able to publish a product, and who should only be able to draft one?",
            "Which WordPress/WooCommerce roles map to those responsibilities?",
            "What product-content guidelines would you set — image size, description length, mandatory fields?",
            "How would you detect that a policy is not being followed?",
         ],
         output="A short policy statement: the roles, the content guidelines, and how adherence is monitored."),
    dict(topic=3, code="D3", knowledge="K3",
         title="Discussion — Recommend Payment and Shipping for Customer Experience",
         mins=15,
         brief=("Working from the store you have built, recommend the payment and shipping mix that would give "
                "your customers the best experience — and justify the trade-offs."),
         prompts=[
            "Which payment methods do your customers expect, and what does each one cost you?",
            "Does the customer stay on your site, or get redirected? Why does that matter for conversion?",
            "Would free shipping above a threshold raise your average order value or erode your margin?",
            "Which shipping zones do you actually serve, and what happens to orders outside them?",
         ],
         output="A recommended payment and shipping configuration with the customer-experience reason for each choice."),
    dict(topic=5, code="D5", knowledge="K6 and K7",
         title="Discussion — Metrics to Measure Store Performance",
         mins=15,
         brief=("Decide which metrics you would use to judge whether the store is succeeding, and what criteria "
                "make a metric worth tracking at all."),
         prompts=[
            "Which three metrics would you put in front of the business owner every week?",
            "What makes a metric useful — is it actionable, comparable, and tied to a decision?",
            "What does a rising refund rate or a falling repeat-customer rate actually tell you?",
            "Which report or tool produces each metric — WooCommerce Reports or Google Analytics?",
         ],
         output="A shortlist of performance metrics with the criteria used to select them and their data source."),
]

# ------------------------------------------------------------------ day themes
DAY_THEMES = {
    1: "Building, Running and Measuring a WooCommerce Store",
}

# ------------------------------------------------------------------ assessment
# Per the approved Assessment Plan (CRS-Q-0040881-RET v1.0):
# Practical Performance 75 min (A1–A6) + Oral Questioning 15 min (K1–K7)
ASSESSMENT = dict(
    written="Oral Questioning (OQ) — 15 minutes, open book, 1:1. Covers K1–K7.",
    practical="Practical Performance (PP) — 75 minutes, open book, individually completed. Covers A1–A6.",
    note="A minimum of 75% attendance is required to be eligible for assessment and funding.",
)

# ------------------------------------------------------------------ recommended follow-on courses
RECOMMENDED = [
    "WSQ - Search Engine Optimization (SEO) to Enhance Brand Awareness and Online Business",
    "WSQ - Creating High-Converting Email Campaigns with Mailchimp",
    "WSQ - Building Professional Websites with WordPress",
    "WSQ - Search Engine Optimization (SEO) for Small and Medium Enterprises",
    "WSQ - Business Innovation with Blockchain Technology",
]
