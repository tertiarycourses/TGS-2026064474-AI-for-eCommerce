#!/usr/bin/env python3
"""Generate the standalone labs/ markdown files + labs/README.md index from the
same single source (course_data.py + data_domainN.py) that drives the deck, LP
and LG, so a lab can never drift from the guide.

One file per activity: labs/lab-NN-<slug>.md
"""
import os, re, sys

HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import course_data as C
from data_domain1 import DOMAIN1; from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3; from data_domain4 import DOMAIN4
from data_domain5 import DOMAIN5
ACT=DOMAIN1+DOMAIN2+DOMAIN3+DOMAIN4+DOMAIN5

def _find_repo(start):
    env=os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env): return env
    d=start
    for _ in range(8):
        d=os.path.dirname(d)
        if os.path.isdir(os.path.join(d,"courseware")) and os.path.isdir(os.path.join(d,"labs")): return d
    return os.path.dirname(os.path.dirname(HERE))
REPO=_find_repo(HERE)
LABS=os.path.join(REPO,"labs")
os.makedirs(LABS,exist_ok=True)

TOPICS={t["num"]:t for t in C.TOPICS}
FOOTER=f"---\n*© 2026 {C.ORG}. All rights reserved. · www.tertiarycourses.com.sg*\n"

def slug(s):
    s=s.lower()
    s=re.sub(r"[^a-z0-9]+","-",s)
    return re.sub(r"-+","-",s).strip("-")

written=[]
for a in ACT:
    t=TOPICS[a["topic"]]
    name=f"lab-{a['num']:02d}-{slug(a['title'])}.md"
    L=[]
    L.append(f"# Lab {a['num']} — {a['title']}\n")
    L.append(f"**Course:** {C.TITLE} ({C.COURSE_CODE})  ")
    L.append(f"**Topic {t['code']}:** {t['title']}  ")
    L.append(f"**Objective:** {a['objective']}  ")
    L.append(f"**Platform:** {C.PLATFORM} — {C.PLATFORM_URL}\n")
    L.append("## Goal\n")
    L.append(a["desc"]+"\n")
    L.append("## What you'll build\n")
    L.append(a["build"]+"\n")
    L.append(f"*Uses: {a['services']}.*\n")
    if a.get("image"):
        L.append(f"![{C.PLATFORM} — Lab {a['num']}](../courseware/assets/{a['image']})\n")
    if a.get("business"):
        L.append("## Why the business cares\n")
        L.append(a["business"]+"\n")
    L.append("## Prerequisites\n")
    L.append(f"- Your assigned demo WordPress site — one of **{C.LAB_SITES_RANGE}** — with administrator "
             f"access. Log in at `{C.LAB_LOGIN_PATH}` (for example `https://{C.LAB_SITES[0]}{C.LAB_LOGIN_PATH}`) "
             f"with username `{C.LAB_USER}` and password `{C.LAB_PASS}`.")
    L.append("- A modern browser. A second private/incognito window is useful for viewing the storefront "
             "as a customer while you edit as the administrator.")
    if a["num"]>1:
        L.append(f"- The {C.STORE_NAME} store you set up in Lab 1, with WooCommerce active.")
    L.append(f"- Product images and, for the catalogue labs, the sample product CSV "
             f"([data/{C.STORE_CSV_NAME}](data/{C.STORE_CSV_NAME})).\n")
    L.append("## Step-by-step\n")
    for i,(instr,cmd) in enumerate(a["steps"],1):
        L.append(f"### Step {i} — {instr}\n")
        if cmd:
            L.append("```bash")
            L.append(cmd)
            L.append("```\n")
    L.append("## Test it\n")
    L.append(a["test"]+"\n")
    L.append(FOOTER)
    path=os.path.join(LABS,name)
    with open(path,"w") as f: f.write("\n".join(L))
    written.append((a,name))
    print("Saved",path)

# ---- index ----
idx=[f"# Hands-On Labs — {C.TITLE}\n"]
idx.append(f"**WSQ Course Code:** {C.COURSE_CODE} · Conducted by {C.ORG} ({C.UEN.replace('UEN: ','UEN ')})\n")
_lab_topics=sorted({a["topic"] for a in ACT})
_span=(f"Topics {_lab_topics[0]}–{_lab_topics[-1]}" if len(_lab_topics)>1 else f"Topic {_lab_topics[0]}")
_dayword = "day" if C.DAYS == 1 else "days"
idx.append(f"All labs run on **{C.PLATFORM}** — {C.PLATFORM_URL} — and are completed "
           f"across {_span} (90 minutes of practical time over {C.DAYS} training {_dayword}). Work "
           f"through them in order; each lab builds on the one before.\n")
idx.append("Full step-by-step instructions are also in the Learner Guide. The slide deck shows each "
           "lab's purpose and outcome only.\n")
idx.append("## Demo Training Sites\n")
idx.append(f"Each learner is assigned ONE demo WordPress site by the trainer. Across the seven labs you "
           f"build **{C.STORE_NAME}** — {C.STORE_TAGLINE} — on your site, from an empty WordPress install "
           f"to a working, measured store. The sites are reset before each class.\n")
idx.append("| Site | Login | Username | Password |")
idx.append("|------|-------|----------|----------|")
for site in C.LAB_SITES:
    idx.append(f"| {site} | https://{site}{C.LAB_LOGIN_PATH} | `{C.LAB_USER}` | `{C.LAB_PASS}` |")
idx.append("")
idx.append(f"The sample product CSV for Lab 4 is at [data/{C.STORE_CSV_NAME}](data/{C.STORE_CSV_NAME}).\n")
by_topic={}
for a,name in written: by_topic.setdefault(a["topic"],[]).append((a,name))
for tn in sorted(by_topic):
    t=TOPICS[tn]
    idx.append(f"## Topic {t['code']} — {t['title']}  ({t['weighting']})\n")
    for a,name in by_topic[tn]:
        idx.append(f"- [Lab {a['num']}: {a['title']}]({name}) — {a['build']}")
    idx.append("")
idx.append(FOOTER)
with open(os.path.join(LABS,"README.md"),"w") as f: f.write("\n".join(idx))
print("Saved",os.path.join(LABS,"README.md"))

# ---- sample product CSV (Lab 4 import) ----
# WooCommerce product CSV importer column headers → labs/data/<STORE_CSV_NAME>
import csv
DATA=os.path.join(LABS,"data"); os.makedirs(DATA,exist_ok=True)
CSV_PATH=os.path.join(DATA,C.STORE_CSV_NAME)
with open(CSV_PATH,"w",newline="") as f:
    w=csv.writer(f)
    w.writerow(["Type","SKU","Name","Published","Short description","Regular price",
                "Sale price","Categories","Tags","In stock?","Stock","Weight (kg)"])
    SHORT={
        "LINEN-SHIRT-001":"Lightweight 100% linen shirt, cut for hot-weather comfort.",
        "JACKET-DENIM-001":"A timeless unisex denim jacket in mid-wash indigo.",
        "TOTE-CANVAS-001":"Heavy-duty canvas tote for groceries, gym and laptops.",
        "SCARF-MERINO-001":"Ultra-soft merino scarf for travel and air-conditioned offices.",
        "BELT-LEATHER-001":"Full-grain leather belt with a brushed-steel buckle.",
    }
    for name,sku,reg,sale,cat,tags,stock,weight in C.STORE_CSV_PRODUCTS:
        w.writerow(["simple",sku,name,"1",SHORT[sku],reg,sale,cat,tags,"1",stock,weight])
print("Saved",CSV_PATH)
print(f"{len(written)} lab file(s) generated.")
