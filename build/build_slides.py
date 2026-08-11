#!/usr/bin/env python3
"""Generate the Building a Successful eCommerce Store with WooCommerce
(TGS-2026064474) slide deck (all-white Tertiary house style).

Design helpers are the same set used by the tertiary-course-slides skill that
produced the n8n reference deck (cover, section, content, two_col, cards3,
big_statement, tile_grid, flow_h, trainer_slide, brk). Content is driven
entirely by course_data.py + data_domainN.py so the deck stays 100% aligned
with the LP, LG and labs.

DECK POLICY FOR THIS COURSE
  * NO step-by-step slides. The deck shows each lab's purpose, what the learner
    builds and why it matters to the business; the numbered commands live ONLY
    in the Learner Guide and labs/*.md. (step_slide is intentionally unused.)
  * High visual density: tile grids, flow diagrams, cards and stat bands
    instead of bullet walls.
"""
import os, sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import course_data as C
from data_domain1 import DOMAIN1
from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3
from data_domain4 import DOMAIN4
from data_domain5 import DOMAIN5
ACTIVITIES = DOMAIN1 + DOMAIN2 + DOMAIN3 + DOMAIN4 + DOMAIN5

def _find_repo(start):
    """Locate the course repo (a dir containing both courseware/ and labs/).
    Env COURSE_REPO overrides. Keeps the build working wherever the skill lives."""
    env = os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env):
        return env
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")):
            return d
    return os.path.dirname(os.path.dirname(HERE))
REPO = _find_repo(HERE)
ASSETS = os.path.join(os.path.dirname(HERE), "assets")   # co-located with the skill
# Course diagrams & screenshots. Depending on how the repo is laid out the
# assets folder sits either beside this build/ dir or under courseware/, so
# take the first candidate that actually exists rather than assuming one.
IMG = next((p for p in (os.path.join(os.path.dirname(HERE), "assets"),
                        os.path.join(REPO, "courseware", "assets"),
                        os.path.join(REPO, "assets"))
            if os.path.isdir(p)),
           os.path.join(REPO, "courseware", "assets"))

# ---------------- palette (matches reference) ----------------
BLUE=RGBColor(0x1F,0x6F,0xEB); TEAL=RGBColor(0x10,0xB9,0x81); AMBER=RGBColor(0xF5,0x9E,0x0B)
INK=RGBColor(0x16,0x1B,0x26); GREY=RGBColor(0x5B,0x63,0x72); LIGHT=RGBColor(0xF5,0xF8,0xFC)
WHITE=RGBColor(0xFF,0xFF,0xFF); LINE=RGBColor(0xE2,0xE8,0xF0); VIOLET=RGBColor(0x7C,0x3A,0xED)

prs=Presentation(); prs.slide_width=Inches(13.333); prs.slide_height=Inches(7.5)
SW,SH=prs.slide_width,prs.slide_height
BLANK=prs.slide_layouts[6]

def slide(): return prs.slides.add_slide(BLANK)
def rect(s,x,y,w,h,color,line=None):
    sp=s.shapes.add_shape(1,x,y,w,h); sp.fill.solid(); sp.fill.fore_color.rgb=color
    if line is None: sp.line.fill.background()
    else: sp.line.color.rgb=line; sp.line.width=Pt(1)
    sp.shadow.inherit=False; return sp
def oval(s,x,y,w,h,color):
    sp=s.shapes.add_shape(9,x,y,w,h); sp.fill.solid(); sp.fill.fore_color.rgb=color
    sp.line.fill.background(); sp.shadow.inherit=False; return sp
def txt(s,x,y,w,h,runs,align=PP_ALIGN.LEFT,anchor=MSO_ANCHOR.TOP,space=4):
    tb=s.shapes.add_textbox(x,y,w,h); tf=tb.text_frame; tf.word_wrap=True; tf.vertical_anchor=anchor
    for i,line in enumerate(runs):
        p=tf.paragraphs[0] if i==0 else tf.add_paragraph()
        p.alignment=align; p.space_after=Pt(space)
        for t,sz,col,bold in line:
            r=p.add_run(); r.text=t; r.font.size=Pt(sz); r.font.bold=bold
            r.font.color.rgb=col; r.font.name="Arial"
    return tb
def bullets(s,x,y,w,h,items,size=18,color=INK,gap=10,mcolor=BLUE):
    tb=s.shapes.add_textbox(x,y,w,h); tf=tb.text_frame; tf.word_wrap=True
    for i,it in enumerate(items):
        p=tf.paragraphs[0] if i==0 else tf.add_paragraph(); p.space_after=Pt(gap)
        lvl=it[1] if isinstance(it,tuple) else 0
        text=it[0] if isinstance(it,tuple) else it
        r=p.add_run(); r.text=("•  " if lvl==0 else "–  ")+text
        r.font.size=Pt(size if lvl==0 else size-2); r.font.color.rgb=color if lvl==0 else GREY
        r.font.name="Arial"; r.font.bold=(lvl==0 and isinstance(it,tuple) and len(it)>2 and it[2])
    return tb

PAGE={"n":1}   # slide 1 is the cover (no footer); slide 2 prints "2"
def footer(s):
    PAGE["n"]+=1
    txt(s,Inches(0.4),Inches(7.05),Inches(7.5),Inches(0.35),
        [[(f"{C.SHORT_TITLE}  ·  {C.COURSE_CODE}",9,GREY,False)]])
    txt(s,Inches(5.0),Inches(7.05),Inches(3.3),Inches(0.35),
        [[("© 2026 Tertiary Infotech Academy Pte Ltd",9,GREY,False)]],align=PP_ALIGN.CENTER)
    txt(s,Inches(12.4),Inches(7.05),Inches(0.6),Inches(0.35),
        [[(str(PAGE["n"]),9,GREY,False)]],align=PP_ALIGN.RIGHT)
def head(s,title,kicker=None,kcolor=BLUE):
    rect(s,0,0,SW,SH,WHITE); rect(s,0,0,Inches(0.28),Inches(1.55),kcolor)
    if kicker: txt(s,Inches(0.85),Inches(0.5),Inches(11.6),Inches(0.4),[[(kicker,14,kcolor,True)]])
    # Auto-shrink long titles so they never wrap past the header rule into the
    # slide body. ~52 chars fits on one line at 29pt across the 11.9in box.
    n=len(title)
    size=29 if n<=52 else (25 if n<=68 else (22 if n<=84 else 20))
    txt(s,Inches(0.85),Inches(0.9),Inches(11.9),Inches(0.9),[[(title,size,INK,True)]],
        anchor=MSO_ANCHOR.MIDDLE)
    rect(s,Inches(0.85),Inches(1.7),Inches(11.63),Inches(0.02),LINE)
    return s
def _logo(name):
    p=os.path.join(ASSETS,name)
    return p if os.path.exists(p) else None

# ---------------- slide templates ----------------
def cover():
    s=slide(); rect(s,0,0,SW,SH,WHITE)
    rect(s,0,0,SW,Inches(0.22),BLUE); rect(s,0,Inches(7.28),SW,Inches(0.22),TEAL)
    org=_logo("tertiary-infotech-logo.png")
    if org: s.shapes.add_picture(org,Inches(0.85),Inches(0.7),height=Inches(1.05))
    # course badge (top-right) — WooCommerce badge, else a drawn storefront mark
    badge=_logo("woocommerce-logo.png")
    if badge:
        s.shapes.add_picture(badge,Inches(10.05),Inches(0.6),width=Inches(2.5))
    else:
        WOO=RGBColor(0x7F,0x54,0xB3)          # WooCommerce purple
        bx,by=Inches(10.75),Inches(0.62)
        rect(s,bx,by,Inches(1.85),Inches(1.2),WOO)
        # drawn storefront mark: an awning over a shop front with a cart wheel
        cx=int(bx+Inches(0.925)); ty=int(by+Inches(0.16))
        rect(s,int(cx-Inches(0.4)),ty,Inches(0.8),Inches(0.1),WHITE)      # awning
        for i in range(3):                                                # shop bays
            rect(s,int(cx-Inches(0.36)+Inches(0.25)*i),int(ty+Inches(0.15)),
                 Inches(0.18),Inches(0.24),RGBColor(0xD9,0xC7,0xEE))
        rect(s,int(cx-Inches(0.4)),int(ty+Inches(0.44)),Inches(0.8),Inches(0.04),WHITE)
        txt(s,bx,by+Inches(0.74),Inches(1.85),Inches(0.34),
            [[("WooCommerce",10,WHITE,True)]],align=PP_ALIGN.CENTER)
    txt(s,Inches(0.9),Inches(2.3),Inches(12),Inches(0.6),[[("COURSE SLIDES  ·  WSQ",16,BLUE,True)]])
    txt(s,Inches(0.9),Inches(2.85),Inches(12.0),Inches(1.9),[[(C.TITLE,40,INK,True)]])
    rect(s,Inches(0.92),Inches(4.75),Inches(2.4),Inches(0.06),TEAL)
    txt(s,Inches(0.9),Inches(5.05),Inches(12),Inches(1.4),
        [[(f"WSQ Course Code: {C.COURSE_CODE}",16,GREY,False)],
         [("Conducted by Tertiary Infotech Academy Pte Ltd  ·  UEN 201200696W",14,GREY,False)]],space=6)
    txt(s,Inches(0.9),Inches(6.5),Inches(12),Inches(0.4),[[(f"Version {C.VERSION}  ·  {C.VERSION_DATE}",12,GREY,False)]])
    txt(s,Inches(0.9),Inches(6.85),Inches(12),Inches(0.34),[[("© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved.  ·  www.tertiarycourses.com.sg",10,GREY,False)]])

def section(kicker,title,n,sub=""):
    s=slide(); rect(s,0,0,SW,SH,WHITE); rect(s,0,0,Inches(0.28),SH,BLUE)
    rect(s,Inches(0.85),Inches(2.5),Inches(0.14),Inches(2.0),TEAL)
    txt(s,Inches(1.25),Inches(2.55),Inches(11),Inches(0.6),[[(kicker,18,BLUE,True)]])
    txt(s,Inches(1.25),Inches(3.0),Inches(11.4),Inches(1.6),[[(title,40,INK,True)]])
    if sub: txt(s,Inches(1.27),Inches(4.55),Inches(11),Inches(0.8),[[(sub,16,GREY,False)]])
    txt(s,Inches(10.0),Inches(0.7),Inches(2.8),Inches(1.6),[[(n,72,RGBColor(0xE2,0xE8,0xF0),True)]],align=PP_ALIGN.RIGHT)
    footer(s)
def content(title,items,kicker=None,size=20):
    s=head(slide(),title,kicker); bullets(s,Inches(0.85),Inches(1.95),Inches(11.6),Inches(4.9),items,size=size); footer(s); return s
def two_col(title,left,right,kicker=None,lhead="",rhead=""):
    s=head(slide(),title,kicker)
    rect(s,Inches(0.85),Inches(1.95),Inches(5.7),Inches(4.7),LIGHT); rect(s,Inches(6.95),Inches(1.95),Inches(5.55),Inches(4.7),LIGHT)
    if lhead: txt(s,Inches(1.1),Inches(2.15),Inches(5.2),Inches(0.4),[[(lhead,16,BLUE,True)]])
    if rhead: txt(s,Inches(7.2),Inches(2.15),Inches(5.0),Inches(0.4),[[(rhead,16,TEAL,True)]])
    bullets(s,Inches(1.1),Inches(2.7),Inches(5.2),Inches(3.8),left,size=16)
    bullets(s,Inches(7.2),Inches(2.7),Inches(5.05),Inches(3.8),right,size=16,mcolor=TEAL); footer(s); return s
def cards3(title,cards,kicker):
    s=head(slide(),title,kicker); xs=[Inches(0.85),Inches(5.0),Inches(9.15)]
    for i,c in enumerate(cards[:3]):
        x=xs[i]; col=c[0]
        rect(s,x,Inches(1.95),Inches(3.65),Inches(4.7),LIGHT); rect(s,x,Inches(1.95),Inches(3.65),Inches(0.12),col)
        txt(s,x+Inches(0.25),Inches(2.2),Inches(3.2),Inches(0.6),[[(c[1],19,col,True)]])
        bullets(s,x+Inches(0.25),Inches(2.95),Inches(3.2),Inches(3.4),c[2],size=14,mcolor=col,gap=9)
    footer(s); return s
def big_statement(line1,line2,kicker,color=BLUE):
    s=slide(); rect(s,0,0,SW,SH,WHITE); rect(s,0,0,Inches(0.28),SH,color)
    txt(s,Inches(1.1),Inches(2.2),Inches(11),Inches(0.5),[[(kicker,16,color,True)]])
    txt(s,Inches(1.1),Inches(2.8),Inches(11.3),Inches(2.4),[[(line1,38,INK,True)]])
    if line2: txt(s,Inches(1.12),Inches(4.9),Inches(11),Inches(1.2),[[(line2,20,GREY,False)]])
    footer(s); return s
import math
PALETTE=[BLUE,TEAL,VIOLET,AMBER]
def tile_grid(title,items,kicker=None,cols=2,size=15,icons=None,accent=BLUE):
    """Grid of light panels, each with a coloured icon/number badge + text.
    items: list of strings (or (title,caption) tuples). Much richer than a bullet list."""
    s=head(slide(),title,kicker,kcolor=accent)
    n=len(items); rows=math.ceil(n/cols)
    X0=Inches(0.85); Y0=Inches(1.95); TOTW=Inches(11.63); AREAH=Inches(4.78)
    gx=Inches(0.3); gy=Inches(0.26)
    cw=int((TOTW-gx*(cols-1))/cols); ch=int((AREAH-gy*(rows-1))/rows)
    bd=Inches(0.6)
    for i,it in enumerate(items):
        r=i//cols; c=i%cols
        x=int(X0+(cw+gx)*c); y=int(Y0+(ch+gy)*r); col=PALETTE[i%len(PALETTE)]
        rect(s,x,y,cw,ch,LIGHT); rect(s,x,y,Inches(0.1),ch,col)
        oval(s,x+Inches(0.28),int(y+ch/2-bd/2),bd,bd,col)
        ic=icons[i] if icons else str(i+1)
        txt(s,x+Inches(0.28),int(y+ch/2-bd/2),bd,bd,[[(ic,19,WHITE,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        tx=x+Inches(1.08); tw=cw-Inches(1.32)
        if isinstance(it,tuple):
            txt(s,tx,int(y+Inches(0.14)),tw,int(ch-Inches(0.2)),
                [[(it[0],size+2,INK,True)],[(it[1],size-2,GREY,False)]],anchor=MSO_ANCHOR.MIDDLE,space=3)
        else:
            txt(s,tx,int(y+Inches(0.1)),tw,int(ch-Inches(0.16)),[[(it,size,INK,False)]],anchor=MSO_ANCHOR.MIDDLE)
    footer(s); return s
def flow_h(title,steps,kicker=None,color=BLUE):
    """Horizontal numbered flow: coloured chips connected by chevrons."""
    s=head(slide(),title,kicker,kcolor=color)
    n=len(steps); X0=Inches(0.85); TOTW=Inches(11.63); gap=Inches(0.34)
    cw=int((TOTW-gap*(n-1))/n); y=Inches(2.55); ch=Inches(3.15); bd=Inches(0.82)
    for i,st in enumerate(steps):
        x=int(X0+(cw+gap)*i)
        rect(s,x,y,cw,ch,LIGHT); rect(s,x,y,cw,Inches(0.1),color)
        oval(s,int(x+cw/2-bd/2),int(y+Inches(0.42)),bd,bd,color)
        txt(s,int(x+cw/2-bd/2),int(y+Inches(0.42)),bd,bd,[[(str(i+1),30,WHITE,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        txt(s,x+Inches(0.16),int(y+Inches(1.55)),cw-Inches(0.32),int(ch-Inches(1.7)),[[(st,14,INK,False)]],align=PP_ALIGN.CENTER)
        if i<n-1:
            txt(s,int(x+cw-Inches(0.04)),int(y+ch/2-Inches(0.3)),int(gap+Inches(0.08)),Inches(0.6),
                [[("▶",15,color,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    footer(s); return s
def trainer_slide(kicker,name,role,rows,initials,accent=BLUE):
    """Profile-card layout: avatar badge + name/role panel on the left, labelled
    info tiles on the right. rows: list of (LABEL, value); blank value → fill-in line."""
    s=head(slide(),"About the Trainer",kicker,kcolor=accent)
    lx=Inches(0.85); lw=Inches(3.65)
    rect(s,lx,Inches(1.95),lw,Inches(4.7),LIGHT); rect(s,lx,Inches(1.95),lw,Inches(0.12),accent)
    bd=Inches(1.7); ax=int(lx+(lw-bd)/2)
    oval(s,ax,Inches(2.5),bd,bd,accent)
    txt(s,ax,Inches(2.5),bd,bd,[[(initials,44,WHITE,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    txt(s,lx+Inches(0.15),Inches(4.55),lw-Inches(0.3),Inches(0.6),[[(name,21,INK,True)]],align=PP_ALIGN.CENTER)
    txt(s,lx+Inches(0.15),Inches(5.2),lw-Inches(0.3),Inches(1.2),[[(role,13,GREY,False)]],align=PP_ALIGN.CENTER)
    rx=Inches(4.9); rw=Inches(7.6); ry=Inches(1.95); rh=Inches(4.7)
    n=len(rows); gy=Inches(0.2); th=int((rh-gy*(n-1))/n)
    for i,(label,val) in enumerate(rows):
        y=int(ry+(th+gy)*i); col=PALETTE[i%len(PALETTE)]
        rect(s,rx,y,rw,th,LIGHT); rect(s,rx,y,Inches(0.1),th,col)
        vruns=[(val,14,INK,False)] if val else [("____________________________________________",13,LINE,False)]
        txt(s,rx+Inches(0.32),y,rw-Inches(0.6),th,
            [[(label.upper(),11,col,True)],vruns],anchor=MSO_ANCHOR.MIDDLE,space=3)
    footer(s); return s
def activity_overview(tag,title,desc,build,services,kicker):
    s=head(slide(),title,kicker,kcolor=TEAL)
    rect(s,Inches(0.85),Inches(1.85),Inches(1.7),Inches(0.5),TEAL)
    txt(s,Inches(0.85),Inches(1.9),Inches(1.7),Inches(0.4),[[(tag,16,WHITE,True)]],align=PP_ALIGN.CENTER)
    txt(s,Inches(0.85),Inches(2.55),Inches(11.7),Inches(1.6),[[(desc,21,INK,False)]])
    rect(s,Inches(0.85),Inches(4.3),Inches(11.7),Inches(2.0),LIGHT)
    txt(s,Inches(1.1),Inches(4.5),Inches(11),Inches(0.4),[[("You'll build",14,BLUE,True)]])
    txt(s,Inches(1.1),Inches(4.9),Inches(11),Inches(0.6),[[(build,18,INK,True)]])
    txt(s,Inches(1.1),Inches(5.6),Inches(11.2),Inches(0.6),[[("Tools:  ",13,GREY,True),(services,13,GREY,False)]]); footer(s); return s
def step_slide(kicker,act_title,n,total,text,cmd=""):
    s=head(slide(),act_title,kicker,TEAL)
    oval(s,Inches(0.85),Inches(2.5),Inches(1.4),Inches(1.4),TEAL)
    txt(s,Inches(0.85),Inches(2.74),Inches(1.4),Inches(0.9),[[(str(n),38,WHITE,True)]],align=PP_ALIGN.CENTER)
    txt(s,Inches(0.95),Inches(1.95),Inches(11),Inches(0.4),[[(f"STEP {n} OF {total}",13,GREY,True)]])
    txt(s,Inches(2.55),Inches(2.4),Inches(10.1),Inches(1.3),[[(text,23,INK,False)]],anchor=MSO_ANCHOR.MIDDLE)
    if cmd:
        rect(s,Inches(2.55),Inches(4.15),Inches(10.1),Inches(0.95),RGBColor(0x0B,0x12,0x20))
        txt(s,Inches(2.8),Inches(4.28),Inches(9.7),Inches(0.7),[[("$ "+cmd,13,RGBColor(0x9C,0xDC,0xFE),False)]],anchor=MSO_ANCHOR.MIDDLE)
    footer(s); return s
def test_slide(act_title,text,kicker):
    s=head(slide(),act_title,kicker,TEAL)
    rect(s,Inches(0.85),Inches(2.3),Inches(11.7),Inches(2.6),RGBColor(0xE8,0xF7,0xEE))
    txt(s,Inches(1.2),Inches(2.6),Inches(11),Inches(0.5),[[("✅  Test it",20,RGBColor(0x12,0x7A,0x3E),True)]])
    txt(s,Inches(1.2),Inches(3.3),Inches(11),Inches(1.4),[[(text,18,INK,False)]]); footer(s); return s
def lab_outcome(a,kicker):
    """Visual lab slide — what you build, the tools, and why the business cares.
    Deliberately replaces per-step slides: the commands live only in the LG."""
    s=head(slide(),a["title"],kicker,kcolor=TEAL)
    rect(s,Inches(0.85),Inches(1.85),Inches(1.75),Inches(0.5),TEAL)
    txt(s,Inches(0.85),Inches(1.9),Inches(1.75),Inches(0.4),
        [[(f"LAB {a['num']}",16,WHITE,True)]],align=PP_ALIGN.CENTER)
    txt(s,Inches(2.8),Inches(1.87),Inches(9.7),Inches(0.55),
        [[(a["objective"],13,GREY,False)]],anchor=MSO_ANCHOR.MIDDLE)
    txt(s,Inches(0.85),Inches(2.55),Inches(11.7),Inches(1.25),[[(a["desc"],17,INK,False)]])
    # two outcome panels: what you build  |  why it matters to the business
    py=Inches(3.95); ph=Inches(1.75)
    rect(s,Inches(0.85),py,Inches(5.72),ph,LIGHT); rect(s,Inches(0.85),py,Inches(5.72),Inches(0.1),BLUE)
    txt(s,Inches(1.1),py+Inches(0.22),Inches(5.2),Inches(0.35),[[("YOU'LL BUILD",11,BLUE,True)]])
    txt(s,Inches(1.1),py+Inches(0.6),Inches(5.25),Inches(1.05),[[(a["build"],15,INK,True)]])
    rect(s,Inches(6.8),py,Inches(5.72),ph,LIGHT); rect(s,Inches(6.8),py,Inches(5.72),Inches(0.1),VIOLET)
    txt(s,Inches(7.05),py+Inches(0.22),Inches(5.2),Inches(0.35),[[("WHY THE BUSINESS CARES",11,VIOLET,True)]])
    txt(s,Inches(7.05),py+Inches(0.6),Inches(5.25),Inches(1.05),
        [[(a.get("business",""),13,GREY,False)]])
    # tools strip
    rect(s,Inches(0.85),Inches(5.95),Inches(11.67),Inches(0.62),RGBColor(0xEE,0xF4,0xFF))
    txt(s,Inches(1.1),Inches(5.95),Inches(11.2),Inches(0.62),
        [[("TOOLS   ",10,BLUE,True),(a["services"],12,GREY,False)]],anchor=MSO_ANCHOR.MIDDLE)
    footer(s); return s

def discussion_slide(d,kicker):
    """Facilitated-discussion activity slide for the lecture-only topics."""
    s=head(slide(),d["title"],kicker,kcolor=AMBER)
    rect(s,Inches(0.85),Inches(1.85),Inches(2.5),Inches(0.5),AMBER)
    txt(s,Inches(0.85),Inches(1.9),Inches(2.5),Inches(0.4),
        [[(f"DISCUSSION · {d['mins']} MIN",13,WHITE,True)]],align=PP_ALIGN.CENTER)
    txt(s,Inches(0.85),Inches(2.6),Inches(11.7),Inches(0.95),[[(d["brief"],17,INK,False)]])
    n=len(d["prompts"]); X0=Inches(0.85); TOTW=Inches(11.67); gx=Inches(0.28)
    cw=int((TOTW-gx*(n-1))/n); y=Inches(3.75); ch=Inches(1.95); bd=Inches(0.56)
    for i,p in enumerate(d["prompts"]):
        x=int(X0+(cw+gx)*i); col=PALETTE[i%len(PALETTE)]
        rect(s,x,y,cw,ch,LIGHT); rect(s,x,y,cw,Inches(0.09),col)
        oval(s,int(x+cw/2-bd/2),int(y+Inches(0.28)),bd,bd,col)
        txt(s,int(x+cw/2-bd/2),int(y+Inches(0.28)),bd,bd,
            [[(str(i+1),19,WHITE,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        txt(s,x+Inches(0.16),int(y+Inches(0.98)),cw-Inches(0.32),int(ch-Inches(1.1)),
            [[(p,11,INK,False)]],align=PP_ALIGN.CENTER)
    rect(s,Inches(0.85),Inches(5.95),Inches(11.67),Inches(0.62),RGBColor(0xE8,0xF7,0xEE))
    txt(s,Inches(1.1),Inches(5.95),Inches(11.2),Inches(0.62),
        [[("YOUR OUTPUT   ",10,RGBColor(0x12,0x7A,0x3E),True),(d["output"],12,INK,False)]],
        anchor=MSO_ANCHOR.MIDDLE)
    footer(s); return s

def download_material(kicker="COURSE PORTAL"):
    """Visual 'Download Course Material' slide — a drawn browser mock of the
    LMS/TMS portal plus the numbered download path (not a bare text link)."""
    s=head(slide(),"Download Your Course Material",kicker,kcolor=BLUE)
    # browser chrome mock
    bx,by,bw,bh=Inches(0.85),Inches(1.95),Inches(6.5),Inches(4.55)
    rect(s,bx,by,bw,bh,WHITE,line=LINE)
    rect(s,bx,by,bw,Inches(0.52),RGBColor(0xEE,0xF2,0xF7))
    for i,c in enumerate([RGBColor(0xFF,0x5F,0x57),RGBColor(0xFE,0xBC,0x2E),RGBColor(0x28,0xC8,0x40)]):
        oval(s,bx+Inches(0.2)+Inches(0.28)*i,by+Inches(0.17),Inches(0.17),Inches(0.17),c)
    rect(s,bx+Inches(1.15),by+Inches(0.12),bw-Inches(1.45),Inches(0.29),WHITE,line=LINE)
    txt(s,bx+Inches(1.28),by+Inches(0.12),bw-Inches(1.6),Inches(0.29),
        [[("🔒  lms-tms.tertiaryinfotech.com",10,GREY,False)]],anchor=MSO_ANCHOR.MIDDLE)
    # portal header + course row
    rect(s,bx,by+Inches(0.52),bw,Inches(0.72),BLUE)
    txt(s,bx+Inches(0.28),by+Inches(0.52),bw-Inches(0.5),Inches(0.72),
        [[("Tertiary Infotech  ·  LMS / TMS",14,WHITE,True)]],anchor=MSO_ANCHOR.MIDDLE)
    txt(s,bx+Inches(0.28),by+Inches(1.42),bw-Inches(0.56),Inches(0.35),
        [[("MY COURSES",10,GREY,True)]])
    rect(s,bx+Inches(0.28),by+Inches(1.78),bw-Inches(0.56),Inches(0.78),LIGHT)
    rect(s,bx+Inches(0.28),by+Inches(1.78),Inches(0.08),Inches(0.78),TEAL)
    txt(s,bx+Inches(0.52),by+Inches(1.78),bw-Inches(1.1),Inches(0.78),
        [[(C.TITLE,11,INK,True)],[(C.COURSE_CODE,9,GREY,False)]],anchor=MSO_ANCHOR.MIDDLE,space=2)
    # download rows
    for i,(label,ext) in enumerate([("Learner Slides","PDF"),("Learner Guide","PDF"),("Lesson Plan","PDF")]):
        ry=by+Inches(2.75)+Inches(0.56)*i
        rect(s,bx+Inches(0.28),ry,bw-Inches(0.56),Inches(0.46),WHITE,line=LINE)
        rect(s,bx+Inches(0.36),ry+Inches(0.07),Inches(0.42),Inches(0.32),BLUE)
        txt(s,bx+Inches(0.36),ry+Inches(0.07),Inches(0.42),Inches(0.32),
            [[(ext,8,WHITE,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        txt(s,bx+Inches(0.9),ry,Inches(3.2),Inches(0.46),[[(label,11,INK,False)]],anchor=MSO_ANCHOR.MIDDLE)
        rect(s,bx+bw-Inches(1.35),ry+Inches(0.08),Inches(0.95),Inches(0.3),TEAL)
        txt(s,bx+bw-Inches(1.35),ry+Inches(0.08),Inches(0.95),Inches(0.3),
            [[("⤓ Download",8,WHITE,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    # numbered path on the right
    steps=[("Go to lms-tms.tertiaryinfotech.com","Open the portal in any browser."),
           ("Log in with your registered email","The same address used to enrol."),
           ("Open this course",f"{C.TITLE}."),
           ("Download the material","Slides, Learner Guide and Lesson Plan."),
           ("Keep them open in class","The assessment is open book.")]
    rx=Inches(7.72); rw=Inches(4.8); ry0=Inches(1.95); rh=Inches(4.55)
    gy=Inches(0.16); th=int((rh-gy*(len(steps)-1))/len(steps)); bd=Inches(0.46)
    for i,(t1,t2) in enumerate(steps):
        y=int(ry0+(th+gy)*i); col=PALETTE[i%len(PALETTE)]
        rect(s,rx,y,rw,th,LIGHT); rect(s,rx,y,Inches(0.09),th,col)
        oval(s,rx+Inches(0.24),int(y+th/2-bd/2),bd,bd,col)
        txt(s,rx+Inches(0.24),int(y+th/2-bd/2),bd,bd,
            [[(str(i+1),15,WHITE,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        txt(s,rx+Inches(0.86),y,rw-Inches(1.1),th,
            [[(t1,12,INK,True)],[(t2,10,GREY,False)]],anchor=MSO_ANCHOR.MIDDLE,space=2)
    footer(s); return s

def stat_band(title,stats,kicker,color=BLUE):
    """Big-number band — n large figures with captions. Pure visual impact."""
    s=head(slide(),title,kicker,kcolor=color)
    n=len(stats); X0=Inches(0.85); TOTW=Inches(11.63); gx=Inches(0.3)
    cw=int((TOTW-gx*(n-1))/n); y=Inches(2.4); ch=Inches(3.4)
    for i,(big,cap) in enumerate(stats):
        x=int(X0+(cw+gx)*i); col=PALETTE[i%len(PALETTE)]
        rect(s,x,y,cw,ch,LIGHT); rect(s,x,y,cw,Inches(0.12),col)
        txt(s,x+Inches(0.2),y+Inches(0.75),cw-Inches(0.4),Inches(1.15),
            [[(big,44,col,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        txt(s,x+Inches(0.24),y+Inches(2.0),cw-Inches(0.48),Inches(1.2),
            [[(cap,13,INK,False)]],align=PP_ALIGN.CENTER)
    footer(s); return s

def brk(kind,dur,color=AMBER):
    s=slide(); rect(s,0,0,SW,SH,WHITE)
    rect(s,0,0,SW,Inches(0.22),color); rect(s,0,Inches(7.28),SW,Inches(0.22),color)
    rect(s,Inches(5.4),Inches(2.35),Inches(2.53),Inches(0.1),color)
    txt(s,0,Inches(2.75),SW,Inches(1.2),[[(kind,48,INK,True)]],align=PP_ALIGN.CENTER)
    txt(s,0,Inches(4.05),SW,Inches(0.8),[[(dur,22,color,True)]],align=PP_ALIGN.CENTER); PAGE["n"]+=1


MISSING_IMAGES=[]
def _img(name):
    p=os.path.join(IMG,name)
    if os.path.exists(p): return p
    MISSING_IMAGES.append(name)          # collected and reported at the end
    return None

def picture_slide(title,image,caption="",kicker=None,accent=BLUE):
    """Full-bleed visual slide: one large diagram/screenshot with a caption.
    Silently degrades to a caption-only slide if the asset is missing."""
    s=head(slide(),title,kicker,kcolor=accent)
    path=_img(image)
    top=Inches(1.9); avail_w=Inches(11.63)
    # Reserve a caption strip only when there is a caption, so tall portrait
    # screenshots can use nearly the full slide height instead of a thin band.
    avail_h=Inches(4.55) if caption else Inches(5.05)
    if path:
        from PIL import Image as _PILImage
        try:
            iw,ih=_PILImage.open(path).size
            ar=iw/ih
        except Exception:
            ar=16/9
        w=avail_w; h=int(w/ar)
        if h>avail_h:
            h=avail_h; w=int(h*ar)
        x=int(Inches(0.85)+(avail_w-w)/2); y=int(top+(avail_h-h)/2)
        s.shapes.add_picture(path,x,y,width=w,height=h)
    if caption:
        txt(s,Inches(0.85),Inches(6.55),Inches(11.63),Inches(0.45),
            [[(caption,12,GREY,False)]],align=PP_ALIGN.CENTER)
    footer(s); return s

# ============================================================ BUILD
cover()

# ---------------- ADMIN (front) ----------------
section("COURSE ADMINISTRATION","Welcome & Housekeeping","")
flow_h("Digital Attendance (Mandatory)",[
 "MORNING (AM)\nScan on arrival",
 "AFTERNOON (PM)\nScan after lunch",
 "ASSESSMENT\nScan before you begin"],kicker="TRAQOM · SSG DIGITAL ATTENDANCE",color=VIOLET)
tile_grid("How Digital Attendance Works",[
 ("Mandatory for WSQ funding","AM, PM and Assessment attendance must all be taken on the training day."),
 ("The QR code","The trainer or administrator displays the QR code generated from the SSG portal."),
 ("How to submit","Scan the QR code with your mobile phone camera and submit your attendance."),
 ("75% minimum","At least 75% attendance is required to be eligible for assessment and funding.")],
 kicker="TRAQOM · SSG DIGITAL ATTENDANCE",cols=2,size=14,accent=VIOLET)
trainer_slide("YOUR TRAINER · GENERAL","Your Trainer","General Trainer template —\nto be completed by the trainer",
 [("Name",""),("Title / Designation",""),("Qualifications",""),
  ("Areas of expertise",""),("Training & industry experience",""),("Contact","")],
 initials="?",accent=GREY)
trainer_slide("YOUR TRAINER",C.TRAINER,"Principal Trainer\nTertiary Infotech Academy Pte Ltd",
 [("Role","Principal Trainer, Tertiary Infotech Academy Pte Ltd"),
  ("Expertise","eCommerce, WordPress and WooCommerce content management systems."),
  ("Delivers","WSQ courses on eCommerce, web development, digital marketing and data analytics."),
  ("Founder","Founder and lead instructor at Tertiary Infotech / Tertiary Courses.")],
 initials="AA",accent=BLUE)
tile_grid("Let's Know Each Other",[
 ("Who you are","Your name, your organisation and the role you play there."),
 ("What you've used","Your experience with WordPress, eCommerce or running an online store."),
 ("What you'll sell","One product or business you would like to sell online by the end of today.")],
 kicker="ICE-BREAKER",cols=1,size=15)
tile_grid("Ground Rules",[
 "Set your mobile phone to silent mode.","Participate actively — no question is too small.",
 "Mutual respect: agree to disagree.","One conversation at a time.",
 "Be punctual; return from breaks on time.","75% attendance is required."],
 kicker="HOUSEKEEPING",cols=2,size=15)
tile_grid("Prerequisite",[
 ("Basic WordPress",C.PREREQUISITE),
 ("Comfortable with a browser","You can navigate a WordPress admin dashboard and upload an image."),
 ("A store to build","Bring a product idea — you will build a real catalogue around it today."),
 ("No coding required","Everything in this course is done through the WooCommerce interface.")],
 kicker="BEFORE WE START",cols=2,size=14,accent=AMBER)
download_material()

# Skills Framework
tile_grid("Skills Framework — TSC",[
 ("TSC Title",C.TSC_TITLE),
 ("TSC Code",C.TSC_CODE),
 ("Sector","Retail"),
 ("Proficiency","Level 4 — Manage the utilisation of content management systems to create, curate and publish web content, measure performance and recommend improvements."),
],kicker="SKILLS FRAMEWORK",cols=2,size=14)
tile_grid("TSC Abilities — Assessed by the Practical Performance",
 [(c,t) for c,t in C.ABILITIES[:3]],
 kicker="WHAT THIS COURSE DEVELOPS  ·  A1–A3",cols=1,size=13)
tile_grid("TSC Abilities — Assessed by the Practical Performance (cont.)",
 [(c,t) for c,t in C.ABILITIES[3:]],
 kicker="WHAT THIS COURSE DEVELOPS  ·  A4–A6",cols=1,size=13)
tile_grid("TSC Knowledge — Assessed by Oral Questioning",
 [(c,t) for c,t in C.KNOWLEDGE[:4]],
 kicker="WHAT THIS COURSE DEVELOPS  ·  K1–K4",cols=1,size=13,accent=TEAL)
tile_grid("TSC Knowledge — Assessed by Oral Questioning (cont.)",
 [(c,t) for c,t in C.KNOWLEDGE[4:]],
 kicker="WHAT THIS COURSE DEVELOPS  ·  K5–K7",cols=1,size=13,accent=TEAL)

# Lesson plan / outline
two_col("Lesson Plan — Day 1",
 [("Digital Attendance (AM) · Introductions",1),
  ("Learning outcomes, outline & TSC briefing",1),
  ("Topic 1: Overview of WooCommerce CMS  (LO1)",1),
  ("Lab 1: Set Up Your WooCommerce Store",1),
  ("Topic 2: Manage Products  (LO2, LO3)",1),
  ("Lab 2: Create and Curate a Simple Product",1),
  ("Lunch Break — 1 hour",1)],
 [("Digital Attendance (PM)",1),
  ("Lab 3: Variable Product · Lab 4: Curate Catalogue",1),
  ("Topic 3: Payments & Shipping  (LO4)  ·  Lab 5",1),
  ("Topic 4: Manage Sales  (LO5)  ·  Lab 6",1),
  ("Topic 5: Manage Performance  (LO6)  ·  Lab 7",1),
  ("Course Feedback & TRAQOM Survey",1),
  ("Final Assessment — PP (75 min) + OQ (15 min)",1)],
 kicker="SCHEDULE · DAY 1 · 9:30am – 6:30pm",lhead="Morning  ·  9:30am – 12:30pm",rhead="Afternoon  ·  1:30pm – 6:30pm")
tile_grid("Learning Outcomes",[
 ("LO1 · Setup and monitor","Setup and monitor WooCommerce CMS to ensure adherence to guidelines and policies. (A1, K1)"),
 ("LO2 · Edit and curate","Edit and curate product website on WooCommerce CMS. (A6, K2, K4)"),
 ("LO3 · Maintain content","Maintain product web content on WooCommerce CMS. (A4, K2, K4)"),
 ("LO4 · Payments & shipping","Recommend payment and shipping methods to improve customer experience. (A3, K3)"),
 ("LO5 · Manage issues","Manage issues such as sales, out-of-stock and promotion. (A5, K5)"),
 ("LO6 · Manage performance","Manage WooCommerce CMS performance. (A2, K6, K7)")],
 kicker="WHAT YOU'LL ACHIEVE",cols=1,size=13)
tile_grid("Course Outline",[
 ("Topic 1 — Overview of WooCommerce CMS","Setup, themes, widgets, shortcodes, settings, currency and tax."),
 ("Topic 2 — Manage Products","Product types, images, variations, categories, attributes, up-sells and CSV import."),
 ("Topic 3 — Payments & Shipping","Payment gateways, shipping zones, flat rate, free shipping and local pickup."),
 ("Topic 4 — Manage Sales","Orders, statuses, refunds, restocking, coupons and promotions."),
 ("Topic 5 — Manage Performance","Sales, customer and stock reports, dashboard widgets and Google Analytics.")],
 kicker="FIVE TOPICS · ONE DAY · SEVEN HANDS-ON LABS",cols=1,size=13)
cards3(f"Hands-On Labs on {C.PLATFORM}",[
 (BLUE,"Morning · Labs 1–2",["Set up your WooCommerce store","Configure currency and tax","Create your first product"]),
 (TEAL,"Afternoon · Labs 3–5",["Build a variable product","Curate the catalogue & CSV import","Payments and shipping zones"]),
 (VIOLET,"Afternoon · Labs 6–7",["Orders, refunds and coupons","Reports and dashboard widgets","Google Analytics integration"])],
 kicker=f"WHAT YOU'LL BUILD  ·  {C.PLATFORM_URL}")
tile_grid("Lab Environment — Demo WordPress Sites",[
 ("Your demo site",f"Each learner is assigned ONE demo site by the trainer: {C.LAB_SITES_RANGE}."),
 ("Log in",f"Open your site's {C.LAB_LOGIN_PATH} page — Username: {C.LAB_USER} · Password: {C.LAB_PASS}. "
           f"For example https://{C.LAB_SITES[0]}{C.LAB_LOGIN_PATH}."),
 ("The demo store",f"All seven labs build {C.STORE_NAME} — {C.STORE_TAGLINE}. The Practical Performance "
                   "uses the same retailer, so the labs rehearse the assessment."),
 ("Reset each class","The sites are wiped and re-imaged before every class — experiment freely; "
                     "nothing you do can break anything that matters.")],
 kicker="HANDS-ON LAB ENVIRONMENT · TERTIARYTRAINING.COM",cols=2,size=14,accent=TEAL)
tile_grid("Briefing for Assessment",[
 "Place phones and other materials under the table or on the floor.",
 "No photos or recording of assessment scripts.",
 "No discussion during the assessment.",
 "Use a black or blue pen for hard-copy assessments.",
 "No liquid paper or correction tape.",
 "Scripts are collected when the time is up."],
 kicker="BEFORE YOU BEGIN",cols=2,size=15,accent=AMBER)
cards3("Final Assessment",[
 (BLUE,"Practical Performance — 75 min",["Build and manage a WooCommerce store","Assesses abilities A1–A6","Open book, done individually"]),
 (TEAL,"Oral Questioning — 15 min",["Open-ended questions, 1:1","Assesses knowledge K1–K7","Open book"]),
 (VIOLET,"What you may use",["The course slides","Your Learner Guide","Approved materials only","An appeal process is available"])],
 kicker="ASSESSMENT · 90 MINUTES TOTAL · END OF DAY")
flow_h("Assessment Flow",[
 "TRAQOM survey — scan the QR code on the LMS",
 "Assessment digital attendance — scan the SSG QR",
 "Complete the Practical Performance — 75 min",
 "Answer the Oral Questioning — 15 min, 1:1",
 "Submit your work as directed",
 "Sign the Assessment Summary Record"],kicker="ON ASSESSMENT DAY")
tile_grid("Criteria for Funding",[
 ("Attendance","Minimum attendance rate of 75% based on the SSG Digital Attendance record."),
 ("Assessment","Complete the assessment and be assessed as 'Competent'."),
 ("Digital attendance","AM, PM and Assessment attendance must all be taken."),
 ("TRAQOM survey","Complete the mandatory feedback survey on the LMS.")],
 kicker="WSQ FUNDING REQUIREMENTS",cols=2,size=14,accent=VIOLET)

# ================================================================ DAY 1
section("DAY 1",C.DAY_THEMES[1],"1",
        "Topics 1–5  ·  Seven hands-on labs  ·  Final assessment")

# ---------------- TOPIC 1 — OVERVIEW OF WOOCOMMERCE CMS ----------------
T=C.TOPICS[0]
section(f"TOPIC {T['num']}",T["title"],T["code"],T["subtitle"])
picture_slide("What is WooCommerce","woo-what-is.png",
 "WooCommerce is an open-source, fully customisable eCommerce platform built on WordPress.",
 kicker="TOPIC 01 · CONTEXT")
tile_grid("Why WooCommerce",[
 ("Open source","Free to use, fully customisable, and owned by you — not rented from a hosted platform."),
 ("Built on WordPress","Runs on the world's most widely used CMS, so your shop and your content live together."),
 ("Every product type","Physical, digital, virtual, variable, subscription and bookable products."),
 ("Endlessly extensible","Hundreds of themes, payment gateways and extensions, plus a full developer API.")],
 kicker="THE OPPORTUNITY",cols=2,size=14)
tile_grid("Key Concepts in This Topic",[(t,d) for t,d in T["concepts"]],
 kicker=f"TOPIC {T['code']} · WHAT YOU'LL LEARN",cols=2,size=13)
picture_slide("WooCommerce Store Showcases","woo-showcase.png",
 "Real stores built on WooCommerce — https://woocommerce.com/showcase/",kicker="TOPIC 01 · INSPIRATION")
picture_slide("WooCommerce Demo Store","woo-demo-store.png",
 "The Storefront demo — https://themes.woocommerce.com/storefront/",kicker="TOPIC 01 · INSPIRATION")
flow_h("Start with WooCommerce in 6 Steps",[
 "HOSTING\nMeet the requirements",
 "INSTALL WP\nSet up WordPress",
 "THEME\nPick Storefront",
 "ACTIVATE\nInstall the plugin",
 "SET UP\nRun the wizard",
 "EXTEND\nAdd plugins"],kicker="TOPIC 01 · THE PATH")
tile_grid("System Requirements",[
 ("PHP 7.2 or greater","The server-side language WordPress and WooCommerce run on."),
 ("MySQL 5.6+ / MariaDB 10.0+","The database that stores products, orders and customers."),
 ("Memory limit 128 MB+","WordPress needs headroom to process a catalogue and orders."),
 ("HTTPS support","Essential — you are handling payment and customer data.")],
 kicker="TOPIC 01 · BEFORE YOU INSTALL",cols=2,size=14,accent=AMBER)
picture_slide("Install WooCommerce","woo-install.png",
 "Plugins > Add New > search 'WooCommerce' by Automattic > Install Now > Activate.",kicker="TOPIC 01 · INSTALL")
picture_slide("The WooCommerce Setup Wizard","woo-setup-wizard.png",
 "On first activation the Setup Wizard configures the store for you.",kicker="TOPIC 01 · INSTALL")
picture_slide("Store Setup","woo-store-setup.png",
 "Location and currency, the type of goods you sell, and whether you sell in person.",kicker="TOPIC 01 · INSTALL")
tile_grid("Taxonomies and Post Types",[
 ("Post types","WordPress separates content into types — posts, pages, attachments. WooCommerce adds 'product'."),
 ("Taxonomies","A grouping of post types — categories and tags. WooCommerce adds product categories, tags and attributes."),
 ("Why it matters","This structure is what lets you filter, browse and curate a catalogue rather than a pile of pages."),
 ("Created for you","The setup wizard registers these automatically when WooCommerce is activated.")],
 kicker="TOPIC 01 · HOW WOOCOMMERCE STRUCTURES CONTENT",cols=2,size=13)
picture_slide("Professional WooCommerce Themes","woo-themes-official.png",
 "Official themes — https://woocommerce.com/product-category/themes",kicker="TOPIC 01 · THEMES")
picture_slide("Third-Party WooCommerce Themes","woo-themes-forest.png",
 "ThemeForest — https://themeforest.net/category/wordpress/ecommerce/woocommerce",kicker="TOPIC 01 · THEMES")
tile_grid("Choosing the Right Theme",[
 ("Aesthetic","Does it suit your brand and the products you sell?"),
 ("Release frequency","An actively maintained theme keeps pace with WooCommerce updates."),
 ("Support","Is there documentation and a responsive support channel?"),
 ("Custom functionality","What does it add beyond styling — and will that lock you in?"),
 ("Responsive","It must work on a phone; most storefront traffic is mobile."),
 ("Compatibility","Confirm it declares WooCommerce support explicitly.")],
 kicker="TOPIC 01 · THEMES",cols=2,size=14,accent=TEAL)
tile_grid("WooCommerce Widgets",[
 ("Product widgets","Products, Products by Rating, Recent Product Reviews, Recently Viewed Products."),
 ("Filter widgets","Filter by Attribute, Filter by Price, Filter by Rating, plus Active Product Filters."),
 ("Navigation widgets","Product Categories as a list or dropdown, and a Product Tag Cloud."),
 ("Utility widgets","Cart and Product Search, so customers can buy and find from any page.")],
 kicker="TOPIC 01 · WIDGETS",cols=2,size=13)
picture_slide("Adding a Widget","woo-add-widget.png",
 "Appearance > Widgets — choose a widget area, then Add Widget.",kicker="TOPIC 01 · WIDGETS")
picture_slide("The Products Widget","woo-product-widget.png",
 "Show products by date, price, sales or randomly — all, featured only, or on sale.",kicker="TOPIC 01 · WIDGETS")
picture_slide("Filter Products by Price","woo-filter-price.png",
 "A slider that auto-detects the minimum and maximum prices on the page.",kicker="TOPIC 01 · WIDGETS")
picture_slide("Filter Products by Attribute","woo-filter-attr.png",
 "Layered navigation — AND returns products matching both terms, OR matches either.",kicker="TOPIC 01 · WIDGETS")
tile_grid("Shortcodes Included with WooCommerce",[
 ("[woocommerce_cart]","Renders the cart page."),
 ("[woocommerce_checkout]","Renders the checkout page."),
 ("[woocommerce_my_account]","Renders the customer account page."),
 ("[woocommerce_order_tracking]","Renders the order tracking form.")],
 kicker="TOPIC 01 · SHORTCODES — ADDED AUTOMATICALLY BY THE WIZARD",cols=2,size=14,accent=VIOLET)
picture_slide("WooCommerce Menu Items","woo-menu-items.png",
 "Orders, Coupons, Reports and Settings — the four places you work every day.",kicker="TOPIC 01 · THE ADMIN")
tile_grid("Configuring WooCommerce Settings",[
 ("General","Store address, selling and shipping locations, taxes and currency options."),
 ("Products","Shop pages, measurements, reviews, inventory and downloadable products."),
 ("Tax","Prices entered with tax, tax rates, and how tax is calculated and displayed."),
 ("Shipping","Shipping zones, methods, classes and shipping options."),
 ("Payments","Which gateways are enabled and the order they appear at checkout."),
 ("Accounts & Privacy","Guest checkout, account creation, and data retention policy.")],
 kicker="TOPIC 01 · WOOCOMMERCE > SETTINGS",cols=2,size=13)
picture_slide("Shop Currency","woo-currency.png",
 "WooCommerce > Settings > General > Currency options.",kicker="TOPIC 01 · SETTINGS")
picture_slide("Enabling Taxes","woo-enable-tax.png",
 "Tick 'Enable taxes and tax calculations' — the Tax tab then appears.",kicker="TOPIC 01 · TAX")
picture_slide("Configuring Tax Options","woo-tax-options.png",
 "WooCommerce > Settings > Tax — visible only once taxes are enabled.",kicker="TOPIC 01 · TAX")
tile_grid("Prices Entered With Tax",[
 ("Inclusive","'Yes, I will enter prices inclusive of tax' — catalogue prices already contain the base tax rate."),
 ("Exclusive","'No, I will enter prices exclusive of tax' — tax is added on top at checkout."),
 ("Inclusive formula","tax_amount = price − ( price / ( ( tax_rate% / 100 ) + 1 ) )"),
 ("Exclusive formula","tax_amount = price × ( tax_rate% / 100 )")],
 kicker="TOPIC 01 · THE MOST IMPORTANT TAX DECISION",cols=2,size=13,accent=AMBER)
lab_outcome(ACTIVITIES[0],kicker=f"TOPIC {T['code']} · HANDS-ON LAB")
discussion_slide(C.DISCUSSIONS[0],kicker=f"TOPIC {T['code']} · DISCUSSION")

# ---------------- TOPIC 2 — MANAGE PRODUCTS ----------------
T=C.TOPICS[1]
section(f"TOPIC {T['num']}",T["title"],T["code"],T["subtitle"])
tile_grid("Key Concepts in This Topic",[(t,d) for t,d in T["concepts"]],
 kicker=f"TOPIC {T['code']} · WHAT YOU'LL LEARN",cols=2,size=13)
tile_grid("Product Types",[
 ("Simple","The majority of products — shipped, with no options. For example, a book."),
 ("Grouped","A collection of related simple products bought individually, e.g. a set of six glasses."),
 ("Virtual","Needs no shipping — a service. Disables all shipping fields and the cart calculator."),
 ("Downloadable","The customer receives a file after purchase — an album, PDF or photo."),
 ("External / Affiliate","Listed and described on your site, but sold elsewhere."),
 ("Variable","Variations with their own SKU, price and stock — e.g. a t-shirt in sizes and colours.")],
 kicker=f"TOPIC {T['code']} · SIX CORE TYPES",cols=2,size=13)
picture_slide("Adding a Simple Product","woo-add-simple-product.png",
 "Products > Add New — a familiar WordPress editing interface.",kicker="TOPIC 02 · PRODUCTS")
picture_slide("The Product Data Panel","woo-product-data.png",
 "General, Inventory, Shipping, Linked Products, Attributes and Advanced.",kicker="TOPIC 02 · PRODUCTS")
picture_slide("Product Short Description","woo-short-desc.png",
 "The excerpt beside the product image; the long description fills the Description tab.",kicker="TOPIC 02 · CONTENT")
picture_slide("Product Categories and Tags","woo-taxonomies.png",
 "Assigned from the right-hand column, exactly like a WordPress post.",kicker="TOPIC 02 · TAXONOMIES")
picture_slide("Product Images and Galleries","woo-product-images.png",
 "A featured image plus a gallery — and catalogue visibility controls where it appears.",kicker="TOPIC 02 · MEDIA")
tile_grid("Catalog Visibility Options",[
 ("Shop and search","Visible everywhere — shop pages, category pages and search results."),
 ("Shop only","Visible in shop and category pages, but not in search results."),
 ("Search only","Visible in search results, but not in the shop or category pages."),
 ("Hidden","Only reachable on its own product page — useful for unlisted or bundled items.")],
 kicker="TOPIC 02 · WHERE A PRODUCT APPEARS",cols=2,size=14,accent=TEAL)
lab_outcome(ACTIVITIES[1],kicker=f"TOPIC {T['code']} · HANDS-ON LAB")
picture_slide("Adding a Grouped Product","woo-grouped-1.png",
 "Select Grouped from the Product data dropdown — price fields disappear.",kicker="TOPIC 02 · GROUPED")
picture_slide("Populating a Grouped Product","woo-grouped-2.png",
 "Add child products from Linked Products > Grouped products, then reorder by dragging.",kicker="TOPIC 02 · GROUPED")
picture_slide("Virtual and Downloadable Products","woo-virtual-product.png",
 "Tick Virtual to remove shipping; tick Downloadable to add a file path and download limit.",kicker="TOPIC 02 · VIRTUAL")
flow_h("Creating a Variable Product",[
 "ADD ATTRIBUTE\ne.g. Size, Colour",
 "ENTER VALUES\nSmall | Medium | Large",
 "USE FOR VARIATIONS\nTick the box, save",
 "GENERATE VARIATIONS\nAll combinations at once",
 "SET PRICE & STOCK\nPer variation"],kicker="TOPIC 02 · VARIABLE PRODUCTS",color=TEAL)
lab_outcome(ACTIVITIES[2],kicker=f"TOPIC {T['code']} · HANDS-ON LAB")
tile_grid("Categories, Tags and Attributes",[
 ("Product categories","Hierarchical — parents and subcategories, with a slug, description, display type and image."),
 ("Product tags","Flat, with no hierarchy. Use them for cross-cutting themes such as 'cat print' or 'summer'."),
 ("Product attributes","Per-product or global. Global attributes power layered navigation and variations."),
 ("The default category","Every product must have a category; unassigned products fall into 'Uncategorized'.")],
 kicker=f"TOPIC {T['code']} · ORGANISING THE CATALOGUE",cols=2,size=13)
picture_slide("The Default Category","woo-default-category.png",
 "'Uncategorized' cannot be deleted while it is the default — but it can be renamed or switched.",kicker="TOPIC 02 · CATEGORIES")
picture_slide("Product Attributes","woo-attributes.png",
 "Attributes drive the Filter by Attribute widget and are required for variations.",kicker="TOPIC 02 · ATTRIBUTES")
picture_slide("Managing Global Attributes","woo-manage-attributes.png",
 "Products > Attributes — add a name, slug, archives option and default sort order.",kicker="TOPIC 02 · ATTRIBUTES")
picture_slide("Linked Products","woo-linked-products.png",
 "Product data > Linked Products — search for the product you want to link.",kicker="TOPIC 02 · LINKED PRODUCTS")
cards3("Up-Sells, Cross-Sells and Related Products",[
 (BLUE,"Up-sells",["Shown on the PRODUCT page","Recommended INSTEAD of this item","Typically higher value or quality","You choose them"]),
 (TEAL,"Cross-sells",["Shown in the CART","Complementary to what's being bought","e.g. a case with a laptop","You choose them"]),
 (VIOLET,"Related products",["Shown on the PRODUCT page","Chosen AUTOMATICALLY","Shares categories or tags","Influenced by how you categorise"])],
 kicker="TOPIC 02 · RAISING ORDER VALUE")
picture_slide("Up-Sells on the Product Page","woo-upsells.png",
 "Up-sells display beneath the product description.",kicker="TOPIC 02 · UP-SELLS")
picture_slide("Cross-Sells in the Cart","woo-crosssells.png",
 "Cross-sells are promoted on the cart page, based on what is already in it.",kicker="TOPIC 02 · CROSS-SELLS")
picture_slide("Related Products","woo-related.png",
 "Automatic — pulled from products sharing the same categories or tags.",kicker="TOPIC 02 · RELATED")
tile_grid("Product CSV Importer and Exporter",[
 ("Built in","Included since WooCommerce 3.1 — no plugin required."),
 ("Every product type","Supports simple, grouped, external and variable products, including variations."),
 ("For new stores","Export a template, fill it in, and launch a whole catalogue in one pass."),
 ("For existing stores","Update hundreds of products, run a sale, or sync multiple storefronts.")],
 kicker=f"TOPIC {T['code']} · BULK MAINTENANCE",cols=2,size=14,accent=AMBER)
picture_slide("Importing Products","woo-import-1.png",
 "Products > Import > choose your CSV > Continue > map columns > Run the importer.",kicker="TOPIC 02 · CSV IMPORT")
picture_slide("Mapping CSV Columns","woo-import-2.png",
 "WooCommerce proposes a column mapping — review it before running the importer.",kicker="TOPIC 02 · CSV IMPORT")
picture_slide("The WooCommerce Customizer","woo-customizer-1.png",
 "Appearance > Customize > WooCommerce — Store Notice, Product Catalog and Product Images.",kicker="TOPIC 02 · CUSTOMIZER")
picture_slide("Product Catalog Options","woo-product-catalog.png",
 "Appearance > Customize > WooCommerce > Product Catalog.",kicker="TOPIC 02 · CUSTOMIZER")
picture_slide("The Shop Page","woo-shop-page.png",
 "Display Products, Categories, or both — one choice gives the cleanest look.",kicker="TOPIC 02 · CUSTOMIZER")
picture_slide("WooCommerce Blocks","woo-blocks.png",
 "Product blocks for any post or page — by tag, category, attribute, best selling, on sale and more.",kicker="TOPIC 02 · BLOCKS")
lab_outcome(ACTIVITIES[3],kicker=f"TOPIC {T['code']} · HANDS-ON LAB")

# ---------------- TOPIC 3 — PAYMENTS AND SHIPPING ----------------
T=C.TOPICS[2]
section(f"TOPIC {T['num']}",T["title"],T["code"],T["subtitle"])
tile_grid("Key Concepts in This Topic",[(t,d) for t,d in T["concepts"]],
 kicker=f"TOPIC {T['code']} · WHAT YOU'LL LEARN",cols=2,size=13)
picture_slide("Online Payment Methods","woo-online-payment.png",
 "Card and wallet gateways that take payment at checkout.",kicker="TOPIC 03 · PAYMENTS")
tile_grid("Choosing a Payment Gateway",[
 ("Stripe","Supports 25+ countries and recurring payments; the customer stays on your site."),
 ("PayPal","Active in 200+ countries, with PayPal Credit available for US stores."),
 ("Square","Suits merchants who also sell in person, in a physical store."),
 ("eWAY","Takes card payments directly on your store without redirecting the customer."),
 ("Klarna","Buy-now-pay-later across Europe, the UK and the US."),
 ("Payfast","A popular South African gateway for card and EFT, with no monthly cost.")],
 kicker=f"TOPIC {T['code']} · ONLINE GATEWAYS",cols=2,size=13)
picture_slide("Offline Payment Methods","woo-offline-payment.png",
 "Direct bank transfer, cheque and cash on delivery — the order is held until you confirm payment.",kicker="TOPIC 03 · PAYMENTS")
picture_slide("Additional Payment Gateways","woo-payment-gateways.png",
 "https://woocommerce.com/product-category/woocommerce-extensions/payment-gateways",kicker="TOPIC 03 · PAYMENTS")
picture_slide("Shipping Options","woo-shipping.png",
 "Set the unit of measurement for weight and dimensions before configuring rates.",kicker="TOPIC 03 · SHIPPING")
flow_h("How Shipping Is Structured",[
 "SHIPPING ZONE\nA geographic region",
 "SHIPPING METHOD\nFlat rate, free, pickup",
 "METHOD SETTINGS\nTitle, tax status, cost",
 "SHIPPING CLASS\nOptional per-product rate",
 "CHECKOUT\nCustomer picks an option"],kicker="TOPIC 03 · SHIPPING ZONES",color=TEAL)
tile_grid("Core Shipping Options",[
 ("Flat rate","A standard cost per order, per item or per shipping class."),
 ("Free shipping","Optionally gated behind a minimum order amount or a valid coupon."),
 ("Local pickup","The customer collects the order themselves, with optional cost."),
 ("Shipping classes","Group products that cost more to ship — bulky, fragile or heavy items.")],
 kicker=f"TOPIC {T['code']} · WHAT'S BUILT IN",cols=2,size=14,accent=TEAL)
picture_slide("Flat Rate Shipping","woo-flat-rate.png",
 "Added to a shipping zone, with a title, tax status and cost applied to the cart.",kicker="TOPIC 03 · SHIPPING")
picture_slide("Free Shipping","woo-free-shipping.png",
 "'Free shipping requires…' — commonly a minimum order amount, to lift average order value.",kicker="TOPIC 03 · SHIPPING")
picture_slide("Local Pickup","woo-local-pickup.png",
 "Let customers collect the order — some stores retitle this 'Collect in store'.",kicker="TOPIC 03 · SHIPPING")
lab_outcome(ACTIVITIES[4],kicker=f"TOPIC {T['code']} · HANDS-ON LAB")
discussion_slide(C.DISCUSSIONS[1],kicker=f"TOPIC {T['code']} · DISCUSSION")

# ---------------- TOPIC 4 — MANAGE SALES ----------------
T=C.TOPICS[3]
section(f"TOPIC {T['num']}",T["title"],T["code"],T["subtitle"])
tile_grid("Key Concepts in This Topic",[(t,d) for t,d in T["concepts"]],
 kicker=f"TOPIC {T['code']} · WHAT YOU'LL LEARN",cols=2,size=13)
picture_slide("Managing Orders","woo-orders.png",
 "An order is created at checkout, gets a unique ID, and carries a status through its life.",kicker="TOPIC 04 · ORDERS")
tile_grid("Order Statuses",[
 ("Pending payment","Order received, no payment initiated — unpaid."),
 ("Processing","Payment received and stock reduced; awaiting fulfilment."),
 ("Completed","Order fulfilled — no further action required."),
 ("On hold","Stock is reduced, but you must confirm payment yourself."),
 ("Cancelled","Cancelled by admin or customer — stock is increased back."),
 ("Refunded / Failed","Refunded by an admin, or payment declined or requiring authentication.")],
 kicker=f"TOPIC {T['code']} · THE LIFE OF AN ORDER",cols=2,size=13,accent=AMBER)
picture_slide("Viewing Orders","woo-view-orders.png",
 "WooCommerce > Orders — number, customer, date, status, address and total.",kicker="TOPIC 04 · ORDERS")
picture_slide("Screen Options and Filtering","woo-screen-options.png",
 "Choose columns and rows, filter by date, search customers, and preview with the 'eye'.",kicker="TOPIC 04 · ORDERS")
picture_slide("The Single Order Page","woo-single-order.png",
 "View and edit everything — status, line items, taxes, coupons, fees and notes.",kicker="TOPIC 04 · ORDERS")
picture_slide("Order Data Panel","woo-order-data.png",
 "Modify the status, the customer note, and which user the order is assigned to.",kicker="TOPIC 04 · ORDERS")
tile_grid("Editing a Single Order",[
 ("Change status","Move the order through its lifecycle and trigger the customer emails."),
 ("Edit order items","Modify products, quantities, prices and taxes on an unpaid order."),
 ("Stock","Reduce or restore stock for the order directly from Order actions."),
 ("Apply coupons","Enter a known coupon code — the order must be unpaid for it to take effect."),
 ("Add a fee","Enter an amount or a percentage; negative fees apportion tax across items."),
 ("Order actions","Email order details to the customer, or regenerate download permissions.")],
 kicker=f"TOPIC {T['code']} · WHAT YOU CAN CHANGE",cols=2,size=13)
picture_slide("Adding an Order Manually","woo-add-order.png",
 "WooCommerce > Orders > Add order — for phone and offline sales.",kicker="TOPIC 04 · ORDERS")
picture_slide("Refunding an Order","woo-refund.png",
 "Open the order, click Refund, enter the amount and a reason, then Refund manually.",kicker="TOPIC 04 · REFUNDS")
picture_slide("Restocking Refunded Items","woo-restock.png",
 "Tick 'Restock refunded items' so returned stock goes back into inventory.",kicker="TOPIC 04 · REFUNDS")
picture_slide("Adding a Coupon","woo-add-coupon.png",
 "Marketing > Coupons > Add coupon — enter or generate a unique code.",kicker="TOPIC 04 · COUPONS")
picture_slide("Coupon Discount Settings","woo-discount-setting.png",
 "Discount type and amount, free shipping, and an expiry date.",kicker="TOPIC 04 · COUPONS")
tile_grid("The Three Discount Types",[
 ("Percentage discount","A share off the qualifying items. 3 shirts at $20 = $60; 10% off gives $6."),
 ("Fixed cart discount","A flat sum off the whole cart. 3 shirts at $20 = $60; $10 off gives $10."),
 ("Fixed product discount","A set amount off EACH qualifying item. 3 shirts, $10 off each, gives $30."),
 ("Restrictions & limits","Minimum spend, product and category limits, usage limit per coupon and per user.")],
 kicker=f"TOPIC {T['code']} · GET THE ARITHMETIC RIGHT",cols=2,size=13,accent=VIOLET)
lab_outcome(ACTIVITIES[5],kicker=f"TOPIC {T['code']} · HANDS-ON LAB")

# ---------------- TOPIC 5 — MANAGE PERFORMANCE ----------------
T=C.TOPICS[4]
section(f"TOPIC {T['num']}",T["title"],T["code"],T["subtitle"])
tile_grid("Key Concepts in This Topic",[(t,d) for t,d in T["concepts"]],
 kicker=f"TOPIC {T['code']} · WHAT YOU'LL LEARN",cols=2,size=13)
picture_slide("WooCommerce Reports","woo-reports.png",
 "WooCommerce > Reports — Orders, Customers, Stock and Taxes.",kicker="TOPIC 05 · REPORTS")
picture_slide("Order Reports","woo-order-report.png",
 "Sales by date, by product, by category, coupons by date and customer downloads.",kicker="TOPIC 05 · REPORTS")
picture_slide("Customer Reports","woo-customer-report.png",
 "Customers vs. Guests, and the customer list — sortable across time periods.",kicker="TOPIC 05 · REPORTS")
picture_slide("Stock Reports","woo-stock-report.png",
 "Low in stock, out of stock, and most stocked — lost revenue you can prevent.",kicker="TOPIC 05 · REPORTS")
picture_slide("Dashboard Widgets","woo-dashboard-widgets.png",
 "WooCommerce adds status widgets to the WordPress dashboard; tune them via Screen Options.",kicker="TOPIC 05 · DASHBOARD")
tile_grid("Metrics for a Successful Store",[
 ("Sales & revenue","Gross and net sales, revenue by traffic source, and average order value."),
 ("Conversion","Sales conversion rate — the share of visitors who actually buy."),
 ("Traffic","Website traffic and organic acquisition traffic."),
 ("Engagement","Email click-through rate, email subscription rate and social media engagement."),
 ("Loyalty","Customer retention rate and repeat customer rate."),
 ("Problems","Refund and return rate, and customer enquiries.")],
 kicker=f"TOPIC {T['code']} · WHAT TO MEASURE  ·  K6, K7",cols=2,size=13,accent=TEAL)
tile_grid("Criteria for Evaluating a Metric",[
 ("Actionable","Does a change in this number tell somebody to do something differently?"),
 ("Comparable","Can you track it consistently over time and against a target?"),
 ("Attributable","Can you tell which channel, campaign or product caused the movement?"),
 ("Owned","Is there a person responsible for it, and a threshold that triggers a response?")],
 kicker=f"TOPIC {T['code']} · CHOOSING WHAT TO TRACK  ·  K7",cols=2,size=14,accent=VIOLET)
picture_slide("WooCommerce Extensions","woo-extensions.png",
 "https://woocommerce.com/product-category/woocommerce-extensions/",kicker="TOPIC 05 · EXTENDING")
picture_slide("Recommended Free Plugins","woo-free-plugins.png",
 "WooCommerce Admin, Mailchimp for WooCommerce, Facebook for WooCommerce and Automated Taxes.",kicker="TOPIC 05 · EXTENDING")
picture_slide("Google Analytics Integration","woo-google-analytics.png",
 "https://wordpress.org/plugins/woocommerce-google-analytics-integration/",kicker="TOPIC 05 · ANALYTICS")
picture_slide("Subscriptions","woo-subscriptions.png",
 "Recurring revenue — https://woocommerce.com/products/woocommerce-subscriptions/",kicker="TOPIC 05 · EXTENDING")
picture_slide("Bookings","woo-bookings.png",
 "Sell time and appointments — https://woocommerce.com/products/woocommerce-bookings/",kicker="TOPIC 05 · EXTENDING")
picture_slide("Memberships","woo-memberships.png",
 "Gate content and offers — https://woocommerce.com/products/woocommerce-memberships/",kicker="TOPIC 05 · EXTENDING")
lab_outcome(ACTIVITIES[6],kicker=f"TOPIC {T['code']} · HANDS-ON LAB")
discussion_slide(C.DISCUSSIONS[2],kicker=f"TOPIC {T['code']} · DISCUSSION")

# ---------------- CLOSE ----------------
section("WRAP-UP","Course Summary & Next Steps","")
tile_grid("What You Achieved",[
 ("LO1 · Setup and monitor","Installed WooCommerce, applied a theme, and set currency, tax and permissions."),
 ("LO2 · Edit and curate","Created products with descriptions, images, galleries, categories and tags."),
 ("LO3 · Maintain content","Built variable products and bulk-updated the catalogue by CSV."),
 ("LO4 · Payments & shipping","Configured gateways and a shipping zone with three delivery options."),
 ("LO5 · Manage issues","Processed orders, issued a refund with restocking, and ran a coupon promotion."),
 ("LO6 · Manage performance","Read the sales, customer and stock reports and defined a metric set.")],
 kicker="LEARNING OUTCOMES",cols=1,size=12)
tile_grid("Your Next Steps",[
 ("Keep building your store","Your WooCommerce site and catalogue stay yours after the course."),
 ("Launch with a real product","Pick one product, price it properly, and take a real order."),
 ("Revisit the Learner Guide","Every lab's step-by-step instructions are there for you to repeat."),
 ("Explore the documentation",f"Official guides at {C.PLATFORM_DOCS}")],
 kicker="AFTER TODAY",cols=2,size=14,accent=TEAL)
tile_grid("Recommended Courses",[
 ("Search Engine Optimization (SEO)","Enhance brand awareness and drive organic traffic to your new store."),
 ("Email Campaigns with Mailchimp","Turn your customer list into repeat revenue with high-converting campaigns."),
 ("Professional Websites with WordPress","Deepen the CMS skills underneath WooCommerce."),
 ("SEO for Small and Medium Enterprises","Practical search optimisation scoped to an SME budget."),
 ("Business Innovation with Blockchain","Explore emerging technology for commerce and payments."),
 ("Full catalogue","Browse everything at www.tertiarycourses.com.sg")],
 kicker="CONTINUE YOUR LEARNING",cols=2,size=13)
tile_grid("Summary & Q&A",[
 ("The platform","WooCommerce turns WordPress into a complete, fully customisable online store."),
 ("The content","Products, categories, attributes and variations are what you curate and maintain."),
 ("The commerce","Payments and shipping are customer-experience decisions that shape conversion."),
 ("The operations","Orders, refunds and coupons are the day-to-day issues a store manager resolves."),
 ("The evidence","Reports and analytics tell you whether any of it is actually working."),
 ("Over to you","Any questions before the assessment?")],
 kicker="SUMMARY",cols=2,size=13)
tile_grid("Support",[
 ("Email","enquiry@tertiaryinfotech.com"),
 ("Telephone","+65 6100 0613"),
 ("Website","www.tertiarycourses.com.sg"),
 ("LMS / TMS portal","https://lms-tms.tertiaryinfotech.com")],
 kicker="WE'RE HERE TO HELP — DURING AND AFTER THE CLASS",cols=2,size=15)
# End-of-deck assessment block, in the mandated order:
# Assessment -> Assessment Flow -> Digital Attendance -> Thank You.
cards3("Final Assessment",[
 (BLUE,"Practical Performance — 75 min",["Build and manage a WooCommerce store","Assesses abilities A1–A6","Open book, done individually"]),
 (TEAL,"Oral Questioning — 15 min",["Open-ended questions, 1:1","Assesses knowledge K1–K7","Open book"]),
 (VIOLET,"Before you begin",["Take the Assessment digital attendance","Complete the TRAQOM survey","Slides + Learner Guide allowed","Submit as directed by your assessor"])],
 kicker="ASSESSMENT · 90 MINUTES TOTAL")
flow_h("Assessment Flow",[
 "TRAQOM survey — scan the QR code on the LMS",
 "Assessment digital attendance — scan the SSG QR",
 "Complete the Practical Performance — 75 min",
 "Answer the Oral Questioning — 15 min, 1:1",
 "Submit your work as directed",
 "Sign the Assessment Summary Record"],kicker="ON ASSESSMENT DAY")
tile_grid("Digital Attendance & TRAQOM Survey (Mandatory)",[
 ("Assessment attendance","Take the Assessment digital attendance before you begin — scan the SSG QR code."),
 ("Cert & TRAQOM survey","Complete the mandatory survey at https://lms-tms.tertiaryinfotech.com/"),
 ("Your certificate","Your certificate is issued through the LMS once you are assessed Competent."),
 ("75% minimum","At least 75% attendance is required to be eligible for assessment and funding.")],
 kicker="TRAQOM · SSG DIGITAL ATTENDANCE",cols=2,size=14,accent=VIOLET)
big_statement("Thank You!",
 "You can now build, run and measure a complete eCommerce store with WooCommerce.",
 "SEE YOU AT THE NEXT COURSE",color=TEAL)

# Guard: a picture slide that silently loses its image looks fine to the build
# but ships a blank slide, so fail loudly instead.
if MISSING_IMAGES:
    raise SystemExit(f"ERROR: {len(MISSING_IMAGES)} image(s) not found in {IMG}: "
                     + ", ".join(sorted(set(MISSING_IMAGES))))

OUT=os.path.join(REPO,"courseware",f"{C.SHORT_TITLE}-{C.VERSION}.pptx")
prs.save(OUT)
print(f"Saved {OUT}  ({len(prs.slides.__iter__.__self__._sldIdLst)} slides)  images from {IMG}")
