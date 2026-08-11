"""
Topic 2 — Manage Products on WooCommerce Store (LO2, LO3 / A4, A6, K2, K4).

Lab 2: create a simple product with images, categories and tags.
Lab 3: create a variable product with attributes, variations and stock.
Lab 4: curate the catalogue — up-sells, cross-sells and CSV import.

Labs 2 and 3 carry forward the "Activity: Simple Product" and
"Activity: Variable Product" activities from the approved v14 deck.

The `steps` here drive the LEARNER GUIDE and the labs/*.md files only.
The slide deck shows the lab OVERVIEW + OUTCOME visually — never the steps.
"""

DOMAIN2 = [
    dict(
        num=2,
        topic=2,
        title="Create and Curate a Simple Product",
        image="woo-add-simple-product.png",
        objective="Edit and curate product web content on the WooCommerce CMS (A6, K2, K4).",
        desc=("Build your first catalogue entry. You add a simple product with a title, long and short description, "
              "price and SKU, upload a featured image and a gallery, then file it under a category and tag so "
              "customers can find it. This is the core content-curation task the CMS exists to support."),
        build="A published simple product, complete with images, price, SKU, category and tag",
        services="Products > Add New · Product Data panel · Product image & gallery · Categories · Tags",
        business=("Product content is the storefront's sales copy. Consistent titles, descriptions and imagery are "
                  "exactly the content guidelines a CMS policy governs — and the reason curation matters."),
        steps=[
            ("Go to Products > Add New. Enter a clear, descriptive product Title — this becomes the product page's heading and its URL slug.", "Title:  Classic Cotton T-Shirt"),
            ("Write the long Description in the main editor. This appears in the Product Description tab on the product page. Cover what the product is, what it is made of, and who it is for.", "A relaxed-fit everyday tee in 100% combed cotton (180 gsm). Pre-shrunk,\nbreathable and machine-washable — Harbour & Co's best-selling basic for\nwork, weekends and everything in between."),
            ("Scroll to the Product data panel and leave the type as 'Simple product'. Tick Virtual only if the product needs no shipping, or Downloadable if the customer receives a file.", "Product data:  Simple product"),
            ("On the General tab enter the Regular price. Optionally set a Sale price and schedule its start and end dates.", "Regular price:  29.90     Sale price:  24.90"),
            ("Open the Inventory tab and enter a unique SKU. Tick 'Manage stock?' to track quantity, then set the Stock quantity and choose what happens when it runs out (Allow backorders or not).", "SKU:  TSHIRT-CLASSIC-001     Stock quantity:  50"),
            ("Open the Shipping tab and enter the Weight and Dimensions. These feed weight-based and dimension-based shipping rates later.", "Weight: 0.2 kg   ·   Dimensions: 30 x 20 x 2 cm"),
            ("Fill in the Product short description box below the editor. This excerpt appears beside the product image at the top of the page and is the first copy a customer reads — keep it to two or three lines.", "Short description:  Soft 100% combed cotton tee in a relaxed unisex fit.\nPre-shrunk and machine-washable. Made for everyday Singapore weather."),
            ("In the right-hand column, set the Product categories. Click '+ Add new category' if the category does not exist yet. Every product must belong to at least one category, otherwise it falls into the default 'Uncategorized'.", "Category:  Apparel"),
            ("Add Product tags in the box below. Tags are flat, not hierarchical — use them for cross-cutting themes a customer might browse by.", "Tags:  cotton, unisex, casual"),
            ("Set the Product image (the featured image) from the right-hand column. Then click 'Add product gallery images' and upload two or three additional views.", ""),
            ("Set the Catalog visibility in the Publish box. 'Shop and search' shows the product everywhere; 'Search only', 'Shop only' and 'Hidden' restrict where it appears. Tick 'This is a featured product' to mark it for featured-product widgets and blocks.", "Catalog visibility:  Shop and search"),
            ("Click Publish, then click 'View product' to see the live product page. Check the title, price, short description, image gallery, category and tag all render as intended.", ""),
        ],
        test=("Your product appears on the /shop page and its own product page shows the featured image, gallery, "
              "price, short description, full description tab, category and tags."),
    ),
    dict(
        num=3,
        topic=2,
        title="Create a Variable Product with Attributes and Variations",
        image="woo-virtual-product.png",
        objective="Maintain product web content that carries options, pricing and stock per variation (A4, K2, K4).",
        desc=("Most real products come in options. You define a custom attribute such as Size or Colour, generate "
              "the variations from it, then give each variation its own SKU, price, stock level and image — and "
              "verify the dropdowns work on the storefront."),
        build="A published variable product whose variations each carry their own price, SKU and stock",
        services="Product data > Variable product · Attributes tab · Variations tab · Used for variations",
        business=("Variations keep one product page instead of five near-duplicates. That is cleaner content, "
                  "better SEO, and far less maintenance when a price or description changes."),
        steps=[
            ("Go to Products > Add New and enter a Title and Description as you did for the simple product.", "Title:  Premium Polo Shirt"),
            ("In the Product data panel, change the dropdown from 'Simple product' to 'Variable product'. The price fields disappear — price now belongs to each variation, not the parent.", "Product data:  Variable product"),
            ("Open the Attributes tab and click 'Add new'. Name the attribute and enter its values separated by a vertical bar. Tick 'Visible on the product page' and, critically, tick 'Used for variations'. Click Save attributes.", "Name: Size    Value(s):  Small | Medium | Large"),
            ("Add a second attribute the same way so you can see how combinations multiply. Remember to tick 'Used for variations' for this one too, then Save attributes.", "Name: Colour   Value(s):  Black | White"),
            ("Open the Variations tab. From the dropdown choose 'Generate variations' to create every combination automatically, and confirm the prompt. With 3 sizes and 2 colours you get 6 variations.", "Generate variations  →  6 variations created"),
            ("Expand the first variation and enter its own SKU and Regular price. Repeat for every variation — a variation with no price cannot be purchased and will not appear in the dropdown.", "POLO-S-BLK 39.90 · POLO-M-BLK 39.90 · POLO-L-BLK 41.90\nPOLO-S-WHT 39.90 · POLO-M-WHT 39.90 · POLO-L-WHT 41.90"),
            ("Within each variation tick 'Manage stock?' and set a Stock quantity, so each size/colour combination tracks its own inventory.", "Stock quantity:  25"),
            ("Upload a variation image for at least one variation by clicking the image placeholder inside the expanded variation. The product image swaps when the customer selects that option.", ""),
            ("Set the Default form values at the top of the Variations tab if you want a combination pre-selected when the page loads. Click Save changes.", "Default:  Size = Medium, Colour = Black"),
            ("Assign the product to a category and tag, set the Product image and gallery, then click Publish.", "Category:  Apparel"),
            ("Test on the front end: open the product page, choose a size and colour, and confirm the price, SKU, image and stock message update. Set one variation's stock to 0 and confirm it shows as out of stock.", ""),
        ],
        test=("Selecting each combination on the live product page updates the price and SKU, the variation image "
              "swaps where you set one, and a zero-stock variation is reported as unavailable."),
    ),
    dict(
        num=4,
        topic=2,
        title="Curate the Catalogue — Linked Products and CSV Import",
        image="woo-linked-products.png",
        objective="Ensure smooth maintenance and consistent bulk updates of the product catalogue (A4, K2, K4).",
        desc=("Grow and maintain the catalogue efficiently. You organise categories and global attributes, link "
              "products together as up-sells and cross-sells to raise order value, then import a batch of products "
              "from a CSV file and export the catalogue for bulk editing."),
        build="A curated catalogue with categories, attributes, up-sells, cross-sells and CSV-imported products",
        services="Products > Categories · Products > Attributes · Linked Products tab · Product CSV Importer/Exporter",
        business=("Editing products one at a time does not scale. Bulk import and export is how a real store "
                  "launches a catalogue, runs a seasonal price change, or syncs with a supplier feed."),
        steps=[
            ("Go to Products > Categories. Add a category with a Name, an optional URL-friendly Slug, a Parent if it is a subcategory, a Description, a Display type and an Image.", "Name: Apparel   ·   Display type: Products"),
            ("Add a child category by setting its Parent to the category you just created, to see how a hierarchy forms. Drag and drop the rows to reorder them — this order is used on the storefront.", "Name: Shirts   ·   Parent: Apparel"),
            ("Go to Products > Attributes and create a global attribute that any product can reuse. Add a Name and Slug, enable Archives if you want a browsable page per term, choose a default sort order, and click Add attribute.", "Name: Material   ·   Sort order: Name"),
            ("Click 'Configure terms' beside your new attribute and add its values. Global attributes are what the 'Filter Products by Attribute' widget uses for layered navigation.", "Terms:  Cotton, Polyester, Linen"),
            ("Open one of your products and go to Product data > Linked Products. In the Upsells field, search for and add a more premium product. Up-sells display on the product page as a recommendation instead of the current item.", "Upsells:  Premium Polo Shirt"),
            ("In the same panel add a complementary product to the Cross-sells field. Cross-sells are promoted in the cart, based on what the customer is already buying. Click Update.", "Cross-sells:  Cotton Cap"),
            ("Understand related products: these are chosen automatically by WooCommerce from products sharing the same categories or tags. You influence them by how you categorise and tag, not by naming them directly.", ""),
            ("Export your catalogue as a template: go to Products and click Export. Choose the columns and product types to include, then click 'Generate CSV' and open the downloaded file.", "Products > Export > Generate CSV"),
            ("Open the sample product CSV supplied for this lab (labs/data/harbour-co-products.csv) in a spreadsheet. It contains five new Harbour & Co products — Linen Summer Shirt (LINEN-SHIRT-001, 49.90), Classic Denim Jacket (JACKET-DENIM-001, 89.90 on sale at 79.90), Canvas Tote Bag (TOTE-CANVAS-001, 24.90), Merino Wool Scarf (SCARF-MERINO-001, 34.90) and Leather Belt (BELT-LEATHER-001, 32.90) — each with a name, SKU, prices, categories, tags, stock and weight. Review the columns, then save it unchanged as CSV.", "Columns:  Name, SKU, Regular price, Sale price, Categories, Tags, Stock, Published"),
            ("Go to Products and click Import. Choose harbour-co-products.csv, click Continue, review the column mapping WooCommerce proposes, then click 'Run the importer'. Do not refresh the browser while it runs.", "Products > Import > harbour-co-products.csv > Run the importer"),
            ("Confirm the imported products appear in Products > All Products, then re-import the same file with 'Update existing products' ticked in the importer's advanced options to see how a bulk price change is applied.", ""),
        ],
        test=("Your store has a category hierarchy and a global attribute, one product shows an up-sell on its page "
              "and a cross-sell in the cart, and the CSV-imported products appear in the catalogue."),
    ),
]
