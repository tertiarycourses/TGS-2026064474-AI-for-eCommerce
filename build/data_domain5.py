"""
Topic 5 — Manage WooCommerce Performance (LO6 / A2, K6, K7).

Lab 7: read the built-in reports, configure dashboard widgets, and connect
Google Analytics so store performance can be measured against defined metrics.

The `steps` here drive the LEARNER GUIDE and the labs/*.md files only.
The slide deck shows the lab OVERVIEW + OUTCOME visually — never the steps.
"""

DOMAIN5 = [
    dict(
        num=7,
        topic=5,
        title="Measure Store Performance with Reports and Analytics",
        image="woo-reports.png",
        objective="Develop and review metrics to measure the performance of the store (A2, K6, K7).",
        desc=("Turn the store's activity into evidence. You read the Orders, Customers, Stock and Taxes reports, "
              "arrange the dashboard widgets a manager would want, install the Google Analytics integration, and "
              "select the handful of metrics you would actually use to judge whether the store is succeeding."),
        build="A reviewed set of store reports, a configured dashboard, and a defined list of performance metrics",
        services="WooCommerce > Reports · Analytics · Dashboard widgets · Screen Options · Google Analytics plugin",
        business=("Metrics are only useful if they change a decision. Choosing which few to track — and knowing "
                  "what each one would tell you — is what separates a measured store from a busy one."),
        steps=[
            ("Go to WooCommerce > Reports. The reports are grouped into four tabs: Orders, Customers, Stock and Taxes.", "WooCommerce > Reports"),
            ("On the Orders tab open 'Sales by date'. Switch between Year, Last month, This month and Last 7 days, and note gross sales, net sales, orders placed and items purchased. Use the Custom range to pick your own dates.", "Orders > Sales by date > Last 7 days"),
            ("Open 'Sales by product'. Search for one of your products to see its sales volume, then review the Top sellers, Top freebies and Top earners lists on the right — these tell you what to promote and what to stock. After the day's test orders, the Classic Cotton T-Shirt should appear among your top sellers.", "Sales by product > Search:  Classic Cotton T-Shirt"),
            ("Open 'Sales by category' and 'Coupons by date'. Coupon reports show which promotions were actually redeemed and how much discount they cost you — the direct measure of a campaign's uptake.", ""),
            ("Go to the Customers tab. 'Customers vs. Guests' compares registered purchasers against one-off guest checkouts; the Customer list shows who your buyers are. A high guest ratio suggests account creation is a barrier.", ""),
            ("Go to the Stock tab and review Low in stock, Out of stock and Most stocked. Out-of-stock items on a live storefront are lost revenue and a content issue you should be resolving proactively.", "Stock > Low in stock"),
            ("If your store has WooCommerce Analytics (bundled in current versions), open Analytics > Overview. It offers the same data with more flexible filtering, comparison against a previous period, and downloadable CSVs.", "Analytics > Overview"),
            ("Go to the WordPress Dashboard. WooCommerce adds a Status widget summarising the store. Click Screen Options at the top right to show or hide widgets and set the number of columns.", "Dashboard > Screen Options"),
            ("Drag the widgets to arrange the dashboard so the information a shop manager needs is visible without scrolling. This is a small but real content-management decision about what matters most.", ""),
            ("Install the analytics integration: go to Plugins > Add New, search for 'WooCommerce Google Analytics Integration', then Install and Activate it.", "Plugins > Add New > WooCommerce Google Analytics Integration"),
            ("Configure it under WooCommerce > Settings > Integration > Google Analytics. Enter your Google Analytics measurement ID and enable the eCommerce tracking options you need, then save.", "Measurement ID:  G-XXXXXXXXXX"),
            ("Review the free plugins WooCommerce recommends for extending measurement and marketing: WooCommerce Admin for richer reporting, Mailchimp for WooCommerce for email campaigns, and Facebook for WooCommerce for social channels.", ""),
            ("Define your metric set. Write down the metrics you would report weekly and, for each, the criteria that justify it: is it actionable, comparable over time, and tied to a decision? Draw from sales, conversion rate, website traffic, revenue by traffic source, email click-through rate, organic acquisition, social engagement, customer retention, repeat customer rate, refund and return rate, and email subscription rate.", ""),
            ("For each chosen metric, record where it comes from — WooCommerce Reports, WooCommerce Analytics, or Google Analytics — and what value would prompt you to act. A metric with no threshold and no owner will not change anything.", ""),
        ],
        test=("You can produce a sales figure for a chosen period, name your top-selling product, identify any "
              "low-stock items, and present a short list of performance metrics with their source and the "
              "criteria used to select them."),
    ),
]
