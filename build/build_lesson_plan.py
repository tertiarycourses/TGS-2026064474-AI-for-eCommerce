#!/usr/bin/env python3
"""Generate the AI for eCommerce
(TGS-2026064474) Lesson Plan (LP) DOCX in the Tertiary house format.

Cover page + Document Version Control Record + auto TOC + Arial 11pt body +
colour-coded schedule table + page numbers.

ONE training day of 8 hours (9:30am-6:30pm with a 1-hour lunch). The
component split is fixed by the approved Course Proposal
(CA-WSQ-2020-002216-v3) and the Assessment Plan (CRS-Q-0040881-RET v1.0):
    Classroom Facilitation   300 min  (5.0 h, tea breaks counted within)
    Practical / Practicum     90 min  (1.5 h — the seven WooCommerce labs)
    Assessment                90 min  (1.5 h — PP 75 min + OQ 15 min)
    ----------------------------------
    Total training           480 min  (8.0 h, excluding the 1-hour lunch)

The build asserts this split, so the LP can never silently drift out of
alignment with the accredited proposal.
"""
import os, sys
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

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

BRAND=RGBColor(0x1F,0x6F,0xEB); DARK=RGBColor(0x11,0x18,0x27); GREY=RGBColor(0x55,0x5B,0x66)
HEADER_FILL="1F6FEB"; TOPIC_FILL="E8F0FE"; BREAK_FILL="FFF4E5"; LUNCH_FILL="FDE9D9"
ASSESS_FILL="E8F7EE"; LAB_FILL="E6FAF3"

LAB_LIST="; ".join(f"Lab {a['num']}: {a['title']}" for a in ACT)

# ------------------------------------------------ schedule (single source of truth for timing)
# (start, end, minutes, kind, activity_text)   kind: admin/topic/lab/break/lunch/assess
def _labs_for(*topics):
    """Lab list for the given topic numbers, used inside the schedule text."""
    return "; ".join(f"Lab {a['num']}: {a['title']}" for a in ACT if a["topic"] in topics)

# ---- Day 1: 9:30am–6:30pm, 8 training hours (1-hour lunch excluded) --------
# The day is expressed as (minutes, kind, text) blocks and the clock times are
# COMPUTED, so the printed times and the component totals can never disagree.
# Budget (approved Course Proposal CA-WSQ-2020-002216-v3):
#   Classroom 300 min = admin 55 + tea breaks 30 + topic 215
#   Practical  90 min  ·  Assessment 90 min  ·  Total 480 min (+ 1 h lunch)
_BLOCKS = [
    (15,"admin","Welcome, trainer and learner introductions, ground rules, and mandatory digital attendance (AM)"),
    (15,"admin",f"Learning outcomes, course outline and Skills Framework (TSC {C.TSC_CODE}) briefing"),
    (30,"topic","Topic 1 — Overview of WooCommerce CMS: what WooCommerce is, the six steps to a store, system requirements, installing the plugin, the setup wizard, taxonomies and post types.  (LO1 / A1, K1)"),
    (15,"break","Tea break"),
    (30,"topic","Topic 1 — Themes, widgets and shortcodes; the WooCommerce admin menu; the Settings screens including currency options and tax configuration; facilitated discussion 'Content Management Policies for Your Store'.  (LO1 / A1, K1)"),
    (15,"lab","Topic 1 — HANDS-ON PRACTICAL. "+_labs_for(1)),
    (20,"topic","Topic 2 — Manage Products on WooCommerce Store: the six product types, the Product Data panel, product titles, descriptions and short descriptions.  (LO2 / A6, K2, K4)"),
    (60,"lunch","Lunch break"),
    (10,"admin","Mandatory digital attendance (PM)"),
    (30,"topic","Topic 2 — Product images and galleries, catalogue visibility, categories, tags and attributes, grouped, virtual and downloadable products, and variable products with variations.  (LO2, LO3 / A4, A6, K2, K4)"),
    (20,"lab","Topic 2 — HANDS-ON PRACTICAL. Lab 2: Create and Curate a Simple Product; Lab 3: Create a Variable Product with Attributes and Variations"),
    (25,"topic","Topic 2 — Curating the catalogue: up-sells, cross-sells and related products, the WooCommerce Customizer, WooCommerce Blocks, and the product CSV importer/exporter.  (LO3 / A4, K2, K4)"),
    (15,"lab","Topic 2 — HANDS-ON PRACTICAL. Lab 4: Curate the Catalogue — Linked Products and CSV Import"),
    (15,"break","Tea break"),
    (30,"topic","Topic 3 — Manage Payments and Shipping: online and offline payment methods, choosing a gateway, shipping zones, flat rate, free shipping, local pickup and shipping classes; facilitated discussion 'Recommend Payment and Shipping for Customer Experience'.  (LO4 / A3, K3)"),
    (15,"lab","Topic 3 — HANDS-ON PRACTICAL. "+_labs_for(3)),
    (25,"topic","Topic 4 — Manage Sales on WooCommerce Store: orders and order statuses, viewing and editing single orders, creating orders manually, refunds and restocking, coupons and the three discount types.  (LO5 / A5, K5)"),
    (15,"lab","Topic 4 — HANDS-ON PRACTICAL. "+_labs_for(4)),
    (25,"topic","Topic 5 — Manage WooCommerce Performance: sales, customer and stock reports, dashboard widgets, eCommerce metrics and the criteria for evaluating them, Google Analytics; facilitated discussion 'Metrics to Measure Store Performance'.  (LO6 / A2, K6, K7)"),
    (10,"lab","Topic 5 — HANDS-ON PRACTICAL. "+_labs_for(5)),
    (15,"admin","Course summary and Q&A, TRAQOM survey, Assessment digital attendance, and Briefing for Assessment"),
    (75,"assess","Practical Performance (PP) — 75 minutes, open book, individually completed. Assesses abilities A1–A6."),
    (15,"assess","Oral Questioning (OQ) — 15 minutes, open book, conducted 1:1. Assesses knowledge K1–K7."),
]

def _clock(mins_from_930):
    """Render minutes-after-9:30am as a 12-hour time string."""
    total=9*60+30+mins_from_930
    h,m=divmod(total,60); ap="am" if h<12 else "pm"
    hh=h if 1<=h<=12 else (h-12 if h>12 else 12)
    return f"{hh}:{m:02d}{ap}"

def _expand(blocks):
    out=[]; t=0
    for mins,kind,text in blocks:
        out.append((_clock(t),_clock(t+mins),mins,kind,text)); t+=mins
    return out

SCHEDULE_D1 = _expand(_BLOCKS)

SCHEDULES = {1: SCHEDULE_D1}
SCHEDULE = SCHEDULE_D1

# Component split, computed from the schedules above so the Course Information
# table can never contradict the per-day totals printed under each schedule.
def _split():
    cls=lab=ass=0
    for day in SCHEDULES.values():
        for _s,_e,mins,kind,_t in day:
            if kind in ("topic","admin","break"): cls+=mins
            elif kind=="lab": lab+=mins
            elif kind=="assess": ass+=mins
    return cls,lab,ass
_CLS,_LAB,_ASS = _split()
COMPONENTS_TEXT = (f"Classroom Facilitation {_CLS/60:.1f} h · "
                   f"Practical / Practicum {_LAB/60:.1f} h · "
                   f"Assessment {_ASS/60:.1f} h")

# Which topics carry a facilitated discussion — read from the single source of
# truth so this can never name a topic the course no longer has.
_dt = sorted(d["topic"] for d in C.DISCUSSIONS)
DISC_TOPICS = ("Topics " + ", ".join(str(x) for x in _dt[:-1]) + f" and {_dt[-1]}") if len(_dt) > 1 else f"Topic {_dt[0]}"

# ------------------------------------------------ build document
doc=Document()
normal=doc.styles["Normal"]; normal.font.name="Arial"; normal.font.size=Pt(11)
prodoc.style_headings(doc)

prodoc.add_cover_page(doc,"LESSON PLAN",C.TITLE,C.VERSION.lstrip("v"),
                      org_logo=os.path.join(ASSETS,"tertiary-infotech-logo.png"),
                      course_logo=None, course_code=C.COURSE_CODE)
prodoc.add_version_control(doc,[
 ("14.0","20 February 2023","Previous release of 'Building a Successful eCommerce Store with WooCommerce' "
  "(under the superseded course accreditation), one training day with five topics and four "
  "in-class activities.",C.TRAINER),
 ("15.0","10 August 2026",
  "Major revision under the current course accreditation. Content carried forward from the approved "
  "v14 Master Trainer Slides and re-authored to the current house visual standard: an all-white, highly "
  "visual deck of tile grids, flow diagrams, stat bands and product screenshots in place of bullet walls. "
  "The four legacy activities are expanded into seven structured hands-on labs with full step-by-step "
  "instructions in the Learner Guide. Assessment stated as Practical Performance 75 min plus Oral "
  "Questioning 15 min, per the approved Assessment Plan CRS-Q-0040881-RET v1.0.",C.TRAINER),
 ("15.1","11 August 2026",
  "Adds the classroom demo lab environment — five demo WordPress training sites "
  f"({C.LAB_SITES_RANGE}, login at {C.LAB_LOGIN_PATH}), one assigned per learner and reset before each "
  f"class — and a realistic demo-store storyline: the labs build {C.STORE_NAME}, the same Singapore "
  "apparel retailer used in the Practical Performance scenario, with named mock products, SKUs, prices "
  "and stock levels, plus a sample product CSV for the import lab.",C.TRAINER),
 (C.VERSION.lstrip("v"),C.VERSION_DATE,
  "Course retitled from 'Building a Successful eCommerce Store with WooCommerce' to 'AI for eCommerce' to match the current course listing. Topics, labs, schedule and assessment are unchanged.",C.TRAINER),
])
prodoc.add_toc(doc)

def H(text,level=1):
    return doc.add_heading(text,level=level)

H("Course Information",1)
info=[("Course Title",C.TITLE),("WSQ Course Reference",C.COURSE_CODE),
      ("Training Provider",C.ORG+"  ("+C.UEN.replace('UEN: ','UEN ')+")"),
      ("TSC Title / Code",f"{C.TSC_TITLE}  ·  {C.TSC_CODE}  (Level 4)"),
      ("Duration",f"{C.DAYS} training day · {_CLS+_LAB+_ASS} minutes "
                  f"({(_CLS+_LAB+_ASS)/60:.0f} training hours, excluding a 1-hour lunch break)"),
      ("Daily Timing","9:30 am – 6:30 pm (1-hour lunch; tea breaks counted within training time)"),
      ("Course Components",COMPONENTS_TEXT),
      ("Mode","Instructor-led classroom facilitation with hands-on labs on a live WordPress + WooCommerce store"),
      ("Platform",f"{C.PLATFORM} — {C.PLATFORM_URL}"),
      ("Lab Environment",f"Five demo WordPress training sites — {C.LAB_SITES_RANGE} — one assigned per "
                         f"learner, login at {C.LAB_LOGIN_PATH}, reset before each class"),
      ("Trainer",C.TRAINER)]
t=doc.add_table(rows=0,cols=2); t.style="Table Grid"
for k,v in info:
    c=t.add_row().cells; c[0].text=""; r=c[0].paragraphs[0].add_run(k); r.bold=True; r.font.size=Pt(10)
    prodoc._shade_cell(c[0],TOPIC_FILL)
    c[1].text=""; c[1].paragraphs[0].add_run(v).font.size=Pt(10)

H("Learning Outcomes",1)
doc.add_paragraph("On completion of this course, learners will be able to:")
for lo in C.LEARNING_OUTCOMES:
    p=doc.add_paragraph(style="List Bullet"); p.add_run(lo).font.size=Pt(10.5)

H(f"Skills Framework Mapping (TSC {C.TSC_CODE} {C.TSC_TITLE})",1)
doc.add_paragraph(C.TSC_DESC)
tm=doc.add_table(rows=0,cols=2); tm.style="Table Grid"
hdr=tm.add_row().cells
for i,htext in enumerate(["Abilities (assessed by the Practical Performance)","Knowledge (assessed by the Oral Questioning)"]):
    cell=hdr[i]; cell.text=""
    r=cell.paragraphs[0].add_run(htext); r.bold=True; r.font.size=Pt(10)
    r.font.color.rgb=RGBColor(0xFF,0xFF,0xFF); prodoc._shade_cell(cell,HEADER_FILL)
for i in range(max(len(C.ABILITIES),len(C.KNOWLEDGE))):
    cells=tm.add_row().cells
    for j,src in enumerate((C.ABILITIES,C.KNOWLEDGE)):
        cells[j].text=""
        if i<len(src):
            code,txt=src[i]
            p=cells[j].paragraphs[0]
            rb=p.add_run(code+" — "); rb.bold=True; rb.font.size=Pt(9.5)
            p.add_run(txt).font.size=Pt(9.5)

H("Assessment",1)
for a in [C.ASSESSMENT["written"],C.ASSESSMENT["practical"],
          "Format: Open Book — course slides, Learner Guide and approved materials only.",
          "The assessment is conducted at the end of the training day, after the Briefing for Assessment.",
          "Assessor-to-learner ratio: 1:3 to 1:10 for both the WA (Q&A) and the Practical Performance.",
          C.ASSESSMENT["note"]]:
    p=doc.add_paragraph(style="List Bullet"); p.add_run(a).font.size=Pt(10.5)

def set_cell(cell,text,bold=False,size=9.5,color=None,fill=None,align=None):
    cell.text=""; p=cell.paragraphs[0]
    if align: p.alignment=align
    r=p.add_run(text); r.bold=bold; r.font.size=Pt(size); r.font.name="Arial"
    if color: r.font.color.rgb=color
    if fill: prodoc._shade_cell(cell,fill)

KIND_FILL={"topic":TOPIC_FILL,"break":BREAK_FILL,"lunch":LUNCH_FILL,"assess":ASSESS_FILL,
           "admin":"F3F5F8","lab":LAB_FILL}

H("Course Schedule",1)
totals={"training":0,"classroom":0,"practical":0,"assessment":0}
for day in sorted(SCHEDULES):
    H(f"Day {day} — {C.DAY_THEMES[day]}",2)
    tbl=doc.add_table(rows=0,cols=3); tbl.style="Table Grid"; tbl.alignment=WD_TABLE_ALIGNMENT.CENTER
    hdr=tbl.add_row().cells
    for i,htext in enumerate(["Time","Duration","Topic / Activity"]):
        set_cell(hdr[i],htext,bold=True,size=10,color=RGBColor(0xFF,0xFF,0xFF),fill=HEADER_FILL)
    training=classroom=practical=assessment=0
    for start,end,mins,kind,text in SCHEDULES[day]:
        cells=tbl.add_row().cells; fill=KIND_FILL.get(kind)
        set_cell(cells[0],f"{start}–{end}",bold=(kind in ("topic","assess","lab")),size=9.5,fill=fill)
        set_cell(cells[1],f"{mins} min",size=9.5,fill=fill)
        set_cell(cells[2],text,bold=(kind in ("topic","assess","lab")),size=9.5,fill=fill)
        if kind!="lunch": training+=mins
        if kind in ("topic","admin","break"): classroom+=mins
        elif kind=="lab": practical+=mins
        elif kind=="assess": assessment+=mins
    for row in tbl.rows:
        row.cells[0].width=Inches(1.15); row.cells[1].width=Inches(0.9); row.cells[2].width=Inches(4.75)
    p=doc.add_paragraph()
    r=p.add_run(f"Day {day} training time: {training} minutes ({training/60:.0f} hours), excluding the 1-hour lunch break. "
                f"Classroom Facilitation {classroom} min · Practical/Practicum {practical} min"
                +(f" · Assessment {assessment} min." if assessment else "."))
    r.italic=True; r.font.size=Pt(9.5); r.font.color.rgb=GREY
    totals["training"]+=training; totals["classroom"]+=classroom
    totals["practical"]+=practical; totals["assessment"]+=assessment

p=doc.add_paragraph()
r=p.add_run(f"Course total: {totals['training']} minutes ({totals['training']/60:.0f} hours) across {C.DAYS} training days, "
            f"excluding lunch breaks. Classroom Facilitation {totals['classroom']} min ({totals['classroom']/60:.1f} h) · "
            f"Practical/Practicum {totals['practical']} min ({totals['practical']/60:.1f} h) · "
            f"Assessment {totals['assessment']} min ({totals['assessment']/60:.1f} h).")
r.bold=True; r.font.size=Pt(9.5); r.font.color.rgb=GREY

# Guard: the LP can never drift from the accredited structure.
# 1 training day of 8 h = 480 min, of which 90 min is the final assessment
# (approved Course Proposal CA-WSQ-2020-002216-v3: classroom 5 h, practical 1.5 h, assessment 1.5 h).
assert totals["training"]==480,   f"Training minutes = {totals['training']}, expected 480"
assert totals["assessment"]==90,  f"Assessment minutes = {totals['assessment']}, expected 90"
assert totals["practical"]==90,   f"Practical minutes = {totals['practical']}, expected 90"
assert totals["classroom"]==300,  f"Classroom minutes = {totals['classroom']}, expected 300"
assert totals["classroom"]+totals["practical"]+totals["assessment"]==totals["training"], "Component split does not sum"

H("Topic and Activity Reference",1)
tt=doc.add_table(rows=0,cols=3); tt.style="Table Grid"
hdr=tt.add_row().cells
for i,htext in enumerate(["Topic / Learning Unit","Outcome & TSC mapping","In-class activity"]):
    set_cell(hdr[i],htext,bold=True,size=10,color=RGBColor(0xFF,0xFF,0xFF),fill=HEADER_FILL)
DISC_BY_TOPIC={d["topic"]:d for d in C.DISCUSSIONS}
for tp in C.TOPICS:
    acts=[a for a in ACT if a["topic"]==tp["num"]]
    cells=tt.add_row().cells
    set_cell(cells[0],f"Topic {tp['code']}: {tp['title']}",bold=True,size=9.5,fill=TOPIC_FILL)
    set_cell(cells[1],tp["weighting"],size=9.5,fill=TOPIC_FILL)
    if acts:
        act=", ".join(f"Lab {a['num']}: {a['title']}" for a in acts)
    else:
        d=DISC_BY_TOPIC.get(tp["num"])
        act=f"{d['title']} ({d['mins']} min facilitated discussion)" if d else "Lecture and didactic questioning"
    set_cell(cells[2],act,size=9.5)

H("Hands-On Labs (Topics 1–5 — Practical / Practicum, 90 minutes)",1)
doc.add_paragraph(
    f"All labs run on {C.PLATFORM} ({C.PLATFORM_URL}). Full step-by-step instructions are in the "
    f"Learner Guide; the slide deck presents each lab's purpose and outcome only.")
tl=doc.add_table(rows=0,cols=3); tl.style="Table Grid"
hdr=tl.add_row().cells
for i,htext in enumerate(["Lab","Title","What the learner builds"]):
    set_cell(hdr[i],htext,bold=True,size=10,color=RGBColor(0xFF,0xFF,0xFF),fill=HEADER_FILL)
for a in ACT:
    cells=tl.add_row().cells
    set_cell(cells[0],f"Lab {a['num']}",bold=True,size=9.5,fill=LAB_FILL)
    set_cell(cells[1],a["title"],size=9.5)
    set_cell(cells[2],a["build"],size=9.5)
for row in tl.rows:
    row.cells[0].width=Inches(0.7); row.cells[1].width=Inches(2.5); row.cells[2].width=Inches(3.6)

H("Instructional Methods",1)
for m in ["Lecture — trainer-led explanation of concepts with visual slides.",
          "Didactic questioning — the trainer poses questions to check and deepen understanding.",
          f"Facilitated discussion — learners apply each topic to their own organisation ({DISC_TOPICS}).",
          "Demonstration — the trainer demonstrates each WooCommerce task on screen before the learners attempt it.",
          "Hands-on practical — learners complete Labs 1–7 on their own WooCommerce store (Topics 1–5)."]:
    p=doc.add_paragraph(style="List Bullet"); p.add_run(m).font.size=Pt(10.5)

H("Resources Required",1)
for m in ["Classroom with projector or large screen, whiteboard and high-speed WiFi.",
          "One laptop per learner with a modern web browser (spare laptops are available).",
          f"A demo WordPress training site per learner with administrator access — {C.LAB_SITES_RANGE} "
          f"(login at {C.LAB_LOGIN_PATH} with the classroom credentials), assigned by the trainer and "
          "reset before each class.",
          f"The {C.PLATFORM} plugin ({C.PLATFORM_URL}) and the Storefront theme, installed during Lab 1.",
          f"The {C.STORE_NAME} sample product CSV (labs/data/{C.STORE_CSV_NAME}) and product images for "
          "the catalogue labs.",
          "Course slides, Learner Guide and Lesson Plan available on https://lms-tms.tertiaryinfotech.com."]:
    p=doc.add_paragraph(style="List Bullet"); p.add_run(m).font.size=Pt(10.5)

prodoc.add_page_numbers(doc)
prodoc.enable_update_fields(doc)
OUT=os.path.join(REPO,"courseware",f"LP-{C.SHORT_TITLE}.docx")
doc.save(OUT)
print("Saved",OUT)
print(f"  training={totals['training']} classroom={totals['classroom']} "
      f"practical={totals['practical']} assessment={totals['assessment']}  ({C.DAYS} days)")
