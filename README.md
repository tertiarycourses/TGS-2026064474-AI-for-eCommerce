# Building a Successful eCommerce Store with WooCommerce — WSQ Courseware

**WSQ Course Code:** TGS-2026064474
**Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)
**Trainer:** Dr. Alfred Ang
**Duration:** 1 day · 8 training hours (9:30 am – 6:30 pm, 1-hour lunch)
**Skills Framework:** Content Management System Utilisation — RET-CIE-4002-1.1 (Retail, Level 4)
**Version:** v15.1 · 11 August 2026
**Course page:** https://www.tertiarycourses.com.sg/wsq-building-a-successful-ecommerce-store-with-woocommerce.html

A hands-on, one-day course in running WordPress + WooCommerce as a content management
system. Across seven labs you build one continuous store — **Harbour & Co**, a small
Singapore apparel and accessories retailer going online — from an empty WordPress install
through a curated catalogue, payments and shipping, day-to-day order management, and
finally the reports that tell you whether any of it worked.

## Contents

| Artifact | Path |
|---|---|
| Trainer slide deck (143 slides) | [courseware/Building a Successful eCommerce Store with WooCommerce-v15.1.pptx](courseware/Building%20a%20Successful%20eCommerce%20Store%20with%20WooCommerce-v15.1.pptx) |
| Learner slides (PDF) | [courseware/Building a Successful eCommerce Store with WooCommerce-v15.1.pdf](courseware/Building%20a%20Successful%20eCommerce%20Store%20with%20WooCommerce-v15.1.pdf) |
| Lesson Plan | [courseware/LP-Building a Successful eCommerce Store with WooCommerce.docx](courseware/LP-Building%20a%20Successful%20eCommerce%20Store%20with%20WooCommerce.docx) · [PDF](courseware/LP-Building%20a%20Successful%20eCommerce%20Store%20with%20WooCommerce.pdf) |
| Learner Guide | [courseware/LG-Building a Successful eCommerce Store with WooCommerce.docx](courseware/LG-Building%20a%20Successful%20eCommerce%20Store%20with%20WooCommerce.docx) · [PDF](courseware/LG-Building%20a%20Successful%20eCommerce%20Store%20with%20WooCommerce.pdf) |
| Learner Guide (Markdown mirror) | [LG-Building a Successful eCommerce Store with WooCommerce.md](LG-Building%20a%20Successful%20eCommerce%20Store%20with%20WooCommerce.md) |
| Hands-on labs (7) | [labs/](labs/) — see [labs/README.md](labs/README.md) |
| Sample product CSV | [labs/data/harbour-co-products.csv](labs/data/harbour-co-products.csv) |
| Build source (single source of truth) | [build/](build/) |

The slide deck is **visual only** — every detailed step-by-step procedure lives in the
Learner Guide and the `labs/` files, by design.

Assessment materials (question papers and answer keys) are confidential and are
distributed through Google Drive and the LMS only — they are never published here.

## Learning outcomes

- **LO1** — Setup and monitor WooCommerce CMS to ensure adherence to guidelines and policies. (A1, K1)
- **LO2** — Edit and curate product website on WooCommerce CMS. (A6, K2, K4)
- **LO3** — Maintain product web content on WooCommerce CMS. (A4, K2, K4)
- **LO4** — Recommend payment and shipping methods on WooCommerce CMS to improve customer experience. (A3, K3)
- **LO5** — Manage issues related to WooCommerce CMS such as sales, out-of-stock, promotion etc. (A5, K5)
- **LO6** — Manage WooCommerce CMS performance. (A2, K6, K7)

## Topics and labs

| Topic | TSC mapping | Labs |
|---|---|---|
| 1 · Overview of WooCommerce CMS | LO1 · A1, K1 | 1 — Set up your WooCommerce store |
| 2 · Manage Products | LO2, LO3 · A4, A6, K2, K4 | 2 — Simple product · 3 — Variable product with variations · 4 — Curate the catalogue and CSV import |
| 3 · Manage Payments and Shipping | LO4 · A3, K3 | 5 — Payment methods and shipping zones |
| 4 · Manage Sales | LO5 · A5, K5 | 6 — Orders, refunds and coupons |
| 5 · Manage Performance | LO6 · A2, K6, K7 | 7 — Reports and analytics |

## Lab environment — demo WordPress training sites

Each learner is assigned **one** demo WordPress site by the trainer. The sites are wiped
and re-imaged before every class, so learners can experiment freely.

| Site | Login | Username | Password |
|------|-------|----------|----------|
| wp1.tertiarytraining.com | https://wp1.tertiarytraining.com/wp-admin | `admin` | `admin12345` |
| wp2.tertiarytraining.com | https://wp2.tertiarytraining.com/wp-admin | `admin` | `admin12345` |
| wp3.tertiarytraining.com | https://wp3.tertiarytraining.com/wp-admin | `admin` | `admin12345` |
| wp4.tertiarytraining.com | https://wp4.tertiarytraining.com/wp-admin | `admin` | `admin12345` |
| wp5.tertiarytraining.com | https://wp5.tertiarytraining.com/wp-admin | `admin` | `admin12345` |

These are disposable classroom sandboxes reset before each run — they hold no real
customer, payment or business data.

## The course store — Harbour & Co

Every lab builds the same fictitious retailer: **Harbour & Co**, an apparel and
accessories shop at 71 Ayer Rajah Crescent, Singapore, pricing in Singapore dollars.

- **Lab 2** — Classic Cotton T-Shirt (`TSHIRT-CLASSIC-001`, S$29.90, sale S$24.90)
- **Lab 3** — Premium Polo Shirt in 6 variations (3 sizes × 2 colours), each with its own SKU, price and stock
- **Lab 4** — five more products imported from [labs/data/harbour-co-products.csv](labs/data/harbour-co-products.csv): linen shirt, denim jacket, canvas tote, merino scarf, leather belt
- **Lab 5** — Singapore shipping zone: flat rate S$5, free shipping above S$100, local pickup
- **Lab 6** — a walk-in order for Tan Wei Ling, a refund with restocking, and the `WELCOME10` coupon
- **Lab 7** — the reports that measure it all

The Practical Performance assessment uses the same retailer, so the labs are a direct
rehearsal for it.

## Tools

- **WooCommerce** — https://woocommerce.com (free, open source)
- **WordPress** with the **Storefront** theme — installed during Lab 1
- **WooCommerce Google Analytics Integration** — Lab 7

## Rebuilding the courseware

All artifacts are generated from one content module, so the deck, Lesson Plan, Learner
Guide and labs can never drift apart:

```bash
bash build/build_courseware.sh
```

Course content lives in [build/course_data.py](build/course_data.py) (metadata, outcomes,
topics, schedule) and `build/data_domain1.py` … `data_domain5.py` (one file per topic,
holding that topic's labs and their step-by-step instructions).

---
*© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved. · www.tertiarycourses.com.sg*
