"""
Topic 3 — Manage Payments and Shipping (LO4 / A3, K3).

Lab 5: configure payment methods and shipping zones.

Carries forward the "Activity: Payment and Shipping" activity from the
approved v14 deck.

The `steps` here drive the LEARNER GUIDE and the labs/*.md files only.
The slide deck shows the lab OVERVIEW + OUTCOME visually — never the steps.
"""

DOMAIN3 = [
    dict(
        num=5,
        topic=3,
        title="Configure Payment Methods and Shipping Zones",
        image="woo-shipping.png",
        objective="Recommend and configure payment and shipping methods that improve customer experience (A3, K3).",
        desc=("Make the store able to take money and deliver goods. You enable offline and online payment methods, "
              "then build a shipping zone for your country and add flat rate, free shipping and local pickup to "
              "it — finishing with a test checkout that proves the whole path works."),
        build="A store that accepts payment and offers three shipping options, verified by a test checkout",
        services="WooCommerce > Settings > Payments · Settings > Shipping · Shipping zones · Shipping classes",
        business=("Payment and shipping are where carts are abandoned. Every method you offer, and every rate you "
                  "set, is a direct customer-experience decision with a measurable effect on conversion."),
        steps=[
            ("Go to WooCommerce > Settings > Payments. You see the payment methods available to your store, each with a toggle.", "WooCommerce > Settings > Payments"),
            ("Enable an offline method for classroom testing. Toggle on 'Cash on delivery', then click 'Set up' or Manage to give it a Title and Description — this is the text the customer sees at checkout.", "Title:  Cash on delivery"),
            ("Enable 'Direct bank transfer (BACS)' and add your account details. Note that offline methods place the order 'On hold' until you confirm payment yourself.", ""),
            ("Review the online gateways. Stripe supports 25+ countries and keeps the customer on your site; PayPal is active in 200+ countries; Square suits merchants who also sell in person. Choosing between them is a trade-off of fees, currencies, and whether the customer is redirected away.", ""),
            ("Reorder the payment methods by dragging the rows. The order here is the order the customer sees at checkout — put the method you most want used at the top.", ""),
            ("Go to WooCommerce > Settings > Shipping. Select the unit of measurement for weight and dimensions if you have not already, under the Shipping options sub-tab.", "Weight unit: kg   ·   Dimensions unit: cm"),
            ("Click 'Add shipping zone'. Give the zone a name and choose the regions it covers. A zone is a geographic area that carries its own methods and rates.", "Zone name: Singapore   ·   Region: Singapore"),
            ("Inside the zone click 'Add shipping method' and choose Flat rate. Click on it to edit: enter a Title shown at checkout, set the Tax status, and enter a Cost applied to the whole cart.", "Title: Standard Delivery   ·   Cost: 5.00"),
            ("Add a second method to the zone: Free shipping. Edit it and set 'Free shipping requires…' to 'A minimum order amount', then enter the threshold. This is the classic lever for raising average order value.", "Requires: A minimum order amount   ·   Minimum: 100.00"),
            ("Add a third method: Local pickup. Give it a Title, set its Tax status and a Cost of 0 so customers can collect the order themselves at no charge — Harbour & Co has a physical shop, so pickup is a genuine option for its customers.", "Title: Collect in store (71 Ayer Rajah Crescent)   ·   Cost: 0"),
            ("Optionally create a shipping class under the Shipping classes sub-tab (for example 'Bulky'), assign it to a product on that product's Shipping tab, then give it its own cost inside the Flat rate settings.", "Class: Bulky   ·   Flat rate class cost: 15.00"),
            ("Test the whole path: open your store in a private browser window, add the Classic Cotton T-Shirt (S$29.90) to the cart, and go to Checkout. Confirm all three shipping options appear, then place an order using Cash on delivery and check the order arrives in WooCommerce > Orders.", "Cart: 1 x Classic Cotton T-Shirt  S$29.90   ·   Standard Delivery  S$5.00"),
            ("Add more products — for example the Classic Denim Jacket (S$89.90) and a Premium Polo Shirt — to push the cart above your S$100 free-shipping threshold and confirm Free shipping now appears as an option. This proves the rule is working as the customer will experience it.", "Cart total S$159.70  >  S$100  →  Free shipping appears"),
        ],
        test=("At checkout the store offers your payment methods and all three shipping options, free shipping "
              "appears only above the threshold you set, and a test order is created successfully."),
    ),
]
