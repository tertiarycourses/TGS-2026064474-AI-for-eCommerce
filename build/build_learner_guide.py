#!/usr/bin/env python3
"""Generate the Building a Successful eCommerce Store with WooCommerce
(TGS-2026064474) Learner Guide as
BOTH a Markdown mirror (LG-*.md at repo root) and a DOCX (courseware/LG-*.docx)
from one source, so the two can never diverge.

House format: cover page, Document Version Control Record, page-numbered TOC,
Arial 11pt body, one section per topic (key concepts + the facilitated
discussion) and per lab (Objective, Goal, What you'll build, platform
screenshot, Why the business cares, Step-by-step with commands, Test it), plus
setup, troubleshooting and a WooCommerce glossary.

This is where the STEP-BY-STEP lab instructions live. The slide deck shows each
lab's purpose and outcome only — by design.
"""
import os, sys
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import course_data as C
from data_domain1 import DOMAIN1; from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3; from data_domain4 import DOMAIN4
from data_domain5 import DOMAIN5
ACT=DOMAIN1+DOMAIN2+DOMAIN3+DOMAIN4+DOMAIN5
import prodoc
def _find_repo(start):
    env=os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env): return env
    d=start
    for _ in range(8):
        d=os.path.dirname(d)
        if os.path.isdir(os.path.join(d,"courseware")) and os.path.isdir(os.path.join(d,"labs")): return d
    return os.path.dirname(os.path.dirname(HERE))
REPO=_find_repo(HERE); ASSETS=os.path.join(os.path.dirname(HERE),"assets")
# Course diagrams & screenshots. The assets folder sits beside this build/ dir
# in this repo, but under courseware/ in others — take the first that exists.
IMG=next((p for p in (os.path.join(os.path.dirname(HERE),"assets"),
                      os.path.join(REPO,"courseware","assets"),
                      os.path.join(REPO,"assets"))
          if os.path.isdir(p)), os.path.join(REPO,"courseware","assets"))

# ---------------- block DSL (single content stream → MD + DOCX) ----------------
B=[]
def h1(t): B.append(("h1",t))
def h2(t): B.append(("h2",t))
def h3(t): B.append(("h3",t))
def p(t):  B.append(("p",t))
def bullets(xs): B.append(("bullets",xs))
def steps(xs): B.append(("steps",xs))
def code(t): B.append(("code",t))
def note(t): B.append(("note",t))
def rule(): B.append(("rule",))
def image(path,caption=""): B.append(("image",path,caption))

# ---------------- content ----------------
h1("Introduction")
p(f"This Learner Guide accompanies the WSQ course {C.TITLE} ({C.COURSE_CODE}), conducted by {C.ORG}. "
  f"It is a one-day (8-hour) course mapped to the Skills Framework TSC "
  f"{C.TSC_TITLE} ({C.TSC_CODE}, Level 4).")
p("The course is deliberately practical. Topic 1 sets up the store and its policies; Topic 2 builds and "
  "curates the product catalogue; Topic 3 configures how customers pay and receive their goods; Topic 4 "
  "runs the store day to day through orders, refunds and promotions; and Topic 5 measures whether any of "
  f"it is working. Every lab runs on {C.PLATFORM} ({C.PLATFORM_URL}), the open-source eCommerce platform "
  f"for WordPress ({C.PLATFORM_REPO}).")
p("This guide contains the full step-by-step instructions for every lab. The slide deck deliberately "
  "shows only each lab's purpose and outcome, so follow the numbered steps here while the trainer "
  "demonstrates. Keep this guide with you during the assessment — it is open book.")

h1("Course Learning Outcomes")
p("On completion of this course, you will be able to:")
bullets(C.LEARNING_OUTCOMES)

h1("How This Course Is Assessed")
p("The assessment has two instruments, both open book, conducted at the end of the training day:")
bullets([
 C.ASSESSMENT["written"],
 C.ASSESSMENT["practical"],
 "Open book means you may refer to the course slides, this Learner Guide and any approved materials.",
 C.ASSESSMENT["note"],
 "An appeal process is available if you disagree with the assessment outcome.",
])
p("The Oral Questioning covers the seven knowledge statements (K1–K7) and the Practical Performance "
  "covers the six abilities (A1–A6). Each topic in this guide is labelled with the ability and "
  "knowledge it develops, so you can see exactly what each session is preparing you for.")

h1("Skills Framework Mapping")
h3("Abilities — assessed by the Practical Performance")
bullets([f"{code} — {txt}" for code,txt in C.ABILITIES])
h3("Knowledge — assessed by the Oral Questioning")
bullets([f"{code} — {txt}" for code,txt in C.KNOWLEDGE])

h1("Before You Start — Setting Up for the Hands-On Labs")
h3("What you need")
bullets([
 f"Your assigned demo WordPress training site — one of the five sites {C.LAB_SITES_RANGE}, assigned by "
 f"the trainer at the start of class. You have full administrator access to your site for the day.",
 "The demo hosting already meets the WooCommerce requirements: PHP 7.2 or greater, MySQL 5.6+ "
 "(or MariaDB 10.0+), a WordPress memory limit of 128 MB or greater, and HTTPS support.",
 f"The {C.PLATFORM} plugin — installed from Plugins > Add New during Lab 1. It is free ({C.PLATFORM_URL}).",
 "The Storefront theme, the official WooCommerce theme, also installed during Lab 1.",
 "A laptop with a modern web browser. A second private/incognito window is useful for viewing the "
 "storefront as a customer while you edit as the administrator.",
 f"Two or three product images (any photographs will do) and the sample product CSV file "
 f"(labs/data/{C.STORE_CSV_NAME}) for the catalogue labs.",
])
h3("Log in to your demo training site")
p(f"Before Lab 1 the trainer assigns each learner one demo WordPress site: {C.LAB_SITES_RANGE}. Open "
  f"your site's login page at {C.LAB_LOGIN_PATH} and sign in with the classroom credentials below. "
  "Everything else in this course happens inside that dashboard. The sites are reset before every class, "
  "so treat your site as yours for the day and experiment freely.")
code(f"Open https://{C.LAB_SITES[0]}{C.LAB_LOGIN_PATH}   (use YOUR assigned site: wp1 ... wp5)\n"
     f"Username: {C.LAB_USER}     Password: {C.LAB_PASS}")
h3("The demo store you will build")
p(f"Across the seven labs you build one coherent store — {C.STORE_NAME}, {C.STORE_TAGLINE}, at "
  f"{C.STORE_ADDRESS}. Lab 1 sets the store up; Labs 2–4 build its catalogue (the Classic Cotton "
  "T-Shirt, the Premium Polo Shirt in six size/colour variations, and five more products imported from "
  "CSV); Lab 5 makes it purchasable with payment methods and Singapore shipping zones; Lab 6 runs its "
  "orders, refunds and the WELCOME10 coupon; and Lab 7 measures the result. The Practical Performance "
  "assessment uses the same retailer, so the labs are a direct rehearsal for it.")
h3("Conventions used in every lab")
bullets([
 "Menu paths are written the way they appear in the WordPress admin sidebar, for example "
 "WooCommerce > Settings > General.",
 f"Values in the shaded boxes are the {C.STORE_NAME} demo data — product names, SKUs, prices, the "
 "mock customer and the coupon code. Use them as given so your store matches the trainer's demo, "
 "or substitute your own; the steps matter more than the specific values.",
 "Placeholders in CAPITALS or angle brackets are replaced with your own values.",
 "After changing any setting, click Save changes. WooCommerce does not save automatically, and an "
 "unsaved settings screen is the most common reason a step appears not to work.",
 "Keep a second browser window open on the storefront so you can see each change as a customer sees it.",
])
note("Work only on your assigned demo training site, never on a live shop. Several labs create test "
     "orders, refunds and coupons, and a refund issued against a real order moves real money. The demo "
     "sites exist precisely so you can experiment without consequences.")

# ---------------- per-topic, per-lab ----------------
DISC_BY_TOPIC={d["topic"]:d for d in C.DISCUSSIONS}
for t in C.TOPICS:
    h1(f"Topic {t['code']} — {t['title']}  ({t['weighting']})")
    p(t["subtitle"])
    h3("Key concepts")
    bullets([f"{name} — {desc}" for name,desc in t["concepts"]])

    # Facilitated discussion for the lecture-only topics
    d=DISC_BY_TOPIC.get(t["num"])
    if d:
        h2(f"Activity — {d['title']}  ({d['mins']} minutes)")
        p(d["brief"])
        h3("Discussion prompts")
        bullets(d["prompts"])
        h3("What to produce")
        p(d["output"])
        note("Write your answer down as you go. The same reasoning is what the Oral Questioning asks "
             f"you to demonstrate for {d.get('knowledge', d['code'])}.")

    # Hands-on labs (Topics 2, 3 and 4)
    for a in [x for x in ACT if x["topic"]==t["num"]]:
        h2(f"Lab {a['num']} — {a['title']}")
        p(f"Objective: {a['objective']}")
        p(f"Goal: {a['desc']}")
        h3("What you'll build")
        p(a["build"]+f"   (Tools: {a['services']}.)")
        if a.get("image"):
            image(a["image"],f"{C.PLATFORM} — Lab {a['num']}: {a['title']}")
        if a.get("business"):
            h3("Why the business cares")
            p(a["business"])
        h3("Step-by-step")
        steps([(instr,cmd) for instr,cmd in a["steps"]])
        h3("Test it")
        p(a["test"])
        note(f"A standalone copy of this lab is in labs/lab-{a['num']:02d}-*.md so you can repeat it "
             f"after the course. Your {C.PLATFORM} project stays available to you.")
        rule()

h1("Putting It Together — Running a Store End to End")
p("By the end of the day you should be able to carry one product through the whole arc of the course. "
  "This is the reasoning the assessment is built around:")
steps([
 ("Set up and govern the store: install WooCommerce, apply a theme, set the currency and tax treatment, "
  "and decide who may publish what. You did this in Lab 1. (A1, K1)",""),
 ("Create and curate the content: add a product with a description, images, category and tags, then "
  "build a variable product whose variations carry their own price and stock. Labs 2 and 3. (A6, K2, K4)",""),
 ("Maintain the catalogue at scale: link up-sells and cross-sells, and import or update products in bulk "
  "from a CSV file. Lab 4. (A4, K2, K4)",""),
 ("Make it purchasable: recommend and configure the payment methods and shipping zones that give your "
  "customers the best experience, then prove it with a test checkout. Lab 5. (A3, K3)",""),
 ("Resolve the day-to-day issues: move an order through its statuses, refund an item and restock it, and "
  "run a coupon promotion that applies correctly at checkout. Lab 6. (A5, K5)",""),
 ("Measure whether it works: read the sales, customer and stock reports, connect analytics, and choose "
  "the metrics you would actually report — with the criteria that justify each one. Lab 7. (A2, K6, K7)",""),
])
note("If you can work through these six steps for your own store, you are ready for both the Oral "
     "Questioning and the Practical Performance.")

h1("Troubleshooting the Labs")
bullets([
 "A setting will not take effect — you almost certainly did not click Save changes. WooCommerce settings "
 "screens never save automatically.",
 "The product does not appear in the shop — check that it is Published (not a draft), that its Catalog "
 "visibility is 'Shop and search', and that it has a price. A product with no price cannot be purchased.",
 "A variation cannot be selected on the front end — every variation needs its own Regular price. "
 "Variations left without a price are hidden from the dropdown.",
 "The attribute does not generate variations — you must tick 'Used for variations' on the Attributes tab "
 "and click Save attributes before opening the Variations tab.",
 "No shipping option appears at checkout — confirm the customer's address falls inside a shipping zone "
 "that has at least one shipping method added to it.",
 "Free shipping never shows — check the 'Free shipping requires…' condition and that the cart total "
 "actually exceeds the minimum order amount you set.",
 "The coupon is rejected — confirm coupons are enabled under Settings > General, that the code matches "
 "exactly, and that the cart meets any minimum spend or product restriction.",
 "The CSV import fails or creates duplicates — check the column mapping screen before running the "
 "importer, and tick 'Update existing products' when you intend to update rather than create.",
 "Reports look empty — the built-in reports only count orders in a paid status, so place and complete a "
 "test order first.",
])

h1("Glossary")
B.append(("dl",[
 ("Attribute","A characteristic of a product such as Size or Colour. Global attributes power layered navigation and are required to create variations."),
 ("Backorder","Allowing a product to be ordered when its stock has reached zero, to be fulfilled later."),
 ("Catalog visibility","Where a product appears — shop and search, shop only, search only, or hidden."),
 ("Category","A hierarchical grouping of products. Every product must belong to at least one; unassigned products fall into 'Uncategorized'."),
 ("Checkout","The page where the customer supplies their details, chooses shipping and payment, and places the order."),
 ("CMS (Content Management System)","Software for creating, editing, curating and publishing web content — here, WordPress with WooCommerce."),
 ("Coupon","A code that applies a percentage, fixed cart or fixed product discount, optionally with limits, restrictions and an expiry date."),
 ("Cross-sell","A complementary product promoted on the cart page, based on what the customer is already buying."),
 ("CSV importer / exporter","The built-in tool for creating or updating many products at once from a comma-separated file."),
 ("Downloadable product","A product delivered as a file after purchase, with an optional download limit and expiry."),
 ("Gateway","A payment service such as Stripe, PayPal or Square that processes the customer's payment."),
 ("Grouped product","A collection of related simple products that are purchased individually."),
 ("Order status","The stage an order has reached — pending payment, processing, completed, on hold, cancelled, refunded or failed."),
 ("Permalink / slug","The URL-friendly version of a name, used in the address of a product, category or tag."),
 ("Product Data panel","The metabox on the product edit screen holding the General, Inventory, Shipping, Linked Products and Attributes tabs."),
 ("Related products","Products shown automatically because they share categories or tags with the current product."),
 ("Restock","Returning refunded items to inventory so the stock figure stays accurate."),
 ("Shipping class","A grouping of products that share a shipping cost — for example bulky or fragile items."),
 ("Shipping zone","A geographic region with its own shipping methods and rates."),
 ("Shortcode","A bracketed tag such as [woocommerce_cart] that renders WooCommerce content inside a post or page."),
 ("Simple product","A standard shipped product with no options — the majority of a typical catalogue."),
 ("SKU","Stock Keeping Unit — the unique internal code identifying a product or variation."),
 ("Storefront","The official WooCommerce theme, built to work with every core feature."),
 ("Tag","A flat, non-hierarchical label used to relate products across categories."),
 ("Taxonomy","A way of grouping content. WooCommerce adds product categories, tags and attributes to WordPress."),
 ("Up-sell","A higher-value or better-quality product recommended on the product page instead of the current item."),
 ("Variable product","A product with variations, each of which may carry its own SKU, price, stock level and image."),
 ("Variation","One purchasable combination of a variable product's attributes, for example Size = Medium, Colour = Black."),
 ("Virtual product","A product that requires no shipping, such as a service."),
 ("Widget","A block of content placed in a theme's widget area — product lists, filters, categories, cart or search."),
 ("WooCommerce Blocks","Gutenberg blocks that display products by category, tag, attribute, rating or sales inside any post or page."),
]))

# ---------------- render Markdown ----------------
def _anchor(txt):
    return "".join(ch.lower() if ch.isalnum() else ("-" if ch in " -" else "") for ch in txt)

def render_md():
    out=[f"# {C.TITLE} — Learner Guide",""]
    out.append(f"**WSQ Course Code:** {C.COURSE_CODE}  |  **Conducted by:** {C.ORG} ({C.UEN.replace('UEN: ','UEN ')})  |  **Version {C.VERSION} · {C.VERSION_DATE}**")
    out.append("")
    # TOC (h1 + h2)
    out.append("## Contents"); out.append("")
    for kind,*rest in B:
        if kind=="h1": out.append(f"- [{rest[0]}](#{_anchor(rest[0])})")
        elif kind=="h2": out.append(f"  - [{rest[0]}](#{_anchor(rest[0])})")
    out.append("")
    for kind,*rest in B:
        if kind=="h1": out+=["",f"## {rest[0]}",""]
        elif kind=="h2": out+=["",f"### {rest[0]}",""]
        elif kind=="h3": out+=[f"**{rest[0]}**",""]
        elif kind=="p": out+=[rest[0],""]
        elif kind=="bullets": out+=[f"- {x}" for x in rest[0]]+[""]
        elif kind=="steps":
            for i,(instr,cmd) in enumerate(rest[0],1):
                out.append(f"{i}. {instr}")
                if cmd: out+=["",f"   ```bash",f"   {cmd}","   ```",""]
            out.append("")
        elif kind=="code": out+=["```bash",rest[0],"```",""]
        elif kind=="note": out+=[f"> **Note:** {rest[0]}",""]
        elif kind=="rule": out+=["---",""]
        elif kind=="image":
            out+=[f"![{rest[1]}](courseware/assets/{rest[0]})","",f"*{rest[1]}*",""]
        elif kind=="dl":
            for term,defn in rest[0]: out.append(f"- **{term}** — {defn}")
            out.append("")
    return "\n".join(out)

MD_OUT=os.path.join(REPO,f"LG-{C.SHORT_TITLE}.md")
with open(MD_OUT,"w") as f: f.write(render_md())
print("Saved",MD_OUT)

# ---------------- render DOCX ----------------
BRAND=RGBColor(0x1F,0x6F,0xEB); DARK=RGBColor(0x11,0x18,0x27); GREY=RGBColor(0x55,0x5B,0x66)
INKCODE=RGBColor(0x0B,0x30,0x60)
doc=Document()
normal=doc.styles["Normal"]; normal.font.name="Arial"; normal.font.size=Pt(11)
prodoc.style_headings(doc)
prodoc.add_cover_page(doc,"LEARNER GUIDE",C.TITLE,C.VERSION.lstrip("v"),
                      org_logo=os.path.join(ASSETS,"tertiary-infotech-logo.png"),
                      course_logo=None, course_code=C.COURSE_CODE)
prodoc.add_version_control(doc,[
 ("14.0","20 February 2023","Previous release of 'Building a Successful eCommerce Store with WooCommerce' "
  "(under the superseded course accreditation), one training day with five topics and four "
  "in-class activities.",C.TRAINER),
 ("15.0","10 August 2026",
  "Major revision under the current course accreditation. Content carried forward from the approved "
  "v14 Master Trainer Slides and re-authored to the current house standard. The four legacy activities "
  "are expanded into seven structured hands-on labs with full step-by-step instructions in this guide; "
  "the slide deck now shows each lab's purpose and outcome only. Adds a Skills Framework mapping "
  "section, a lab troubleshooting section and a WooCommerce glossary. Assessment stated as Practical "
  "Performance 75 min plus Oral Questioning 15 min, per Assessment Plan CRS-Q-0040881-RET v1.0.",C.TRAINER),
 (C.VERSION.lstrip("v"),C.VERSION_DATE,
  "Adds the classroom demo lab environment — five demo WordPress training sites "
  f"({C.LAB_SITES_RANGE}, login at {C.LAB_LOGIN_PATH}), one assigned per learner and reset before each "
  f"class — and a realistic demo-store storyline: every lab now builds {C.STORE_NAME}, the same Singapore "
  "apparel retailer used in the Practical Performance scenario, with named mock products, SKUs, prices "
  "and stock levels carried consistently across the labs, and a sample product CSV "
  f"(labs/data/{C.STORE_CSV_NAME}) supplied for the import lab.",C.TRAINER),
])
prodoc.add_toc(doc)

def code_para(text):
    for line in text.split("\n"):
        para=doc.add_paragraph(); prodoc._shade_para(para) if hasattr(prodoc,"_shade_para") else None
        r=para.add_run(line); r.font.name="Consolas"; r.font.size=Pt(9.5); r.font.color.rgb=INKCODE

for kind,*rest in B:
    if kind=="h1": doc.add_heading(rest[0],level=1)
    elif kind=="h2": doc.add_heading(rest[0],level=2)
    elif kind=="h3":
        para=doc.add_paragraph(); r=para.add_run(rest[0]); r.bold=True; r.font.size=Pt(11); r.font.color.rgb=BRAND
    elif kind=="p": doc.add_paragraph(rest[0])
    elif kind=="bullets":
        for x in rest[0]: doc.add_paragraph(x,style="List Bullet")
    elif kind=="steps":
        for i,(instr,cmd) in enumerate(rest[0],1):
            para=doc.add_paragraph(style="List Number"); para.add_run(instr)
            if cmd: code_para(cmd)
    elif kind=="code": code_para(rest[0])
    elif kind=="note":
        para=doc.add_paragraph(); r=para.add_run("Note: "); r.bold=True; r.font.color.rgb=BRAND
        para.add_run(rest[0]).font.size=Pt(10)
    elif kind=="rule": doc.add_paragraph("")
    elif kind=="image":
        ipath=os.path.join(IMG,rest[0])
        if not os.path.exists(ipath):
            # Silently dropping a lab screenshot ships an LG that looks complete
            # but has no visuals — fail the build instead.
            raise SystemExit(f"ERROR: Learner Guide image not found: {ipath}")
        if True:
            from docx.shared import Inches as _In
            doc.add_picture(ipath,width=_In(6.0))
            doc.paragraphs[-1].alignment=WD_ALIGN_PARAGRAPH.CENTER
            cap=doc.add_paragraph(); cap.alignment=WD_ALIGN_PARAGRAPH.CENTER
            cr=cap.add_run(rest[1]); cr.italic=True; cr.font.size=Pt(9); cr.font.color.rgb=GREY
    elif kind=="dl":
        for term,defn in rest[0]:
            para=doc.add_paragraph(style="List Bullet")
            r=para.add_run(term+" — "); r.bold=True; para.add_run(defn)

prodoc.add_page_numbers(doc)
prodoc.enable_update_fields(doc)
DOCX_OUT=os.path.join(REPO,"courseware",f"LG-{C.SHORT_TITLE}.docx")
doc.save(DOCX_OUT)
print("Saved",DOCX_OUT)
