#!/usr/bin/env python3
"""Build the static site in docs/ (served by GitHub Pages at skills.nxlongevity.com).

Usage: python scripts/build_site.py
Requires: pyyaml, markdown
"""
import collections
import html
import re
import shutil
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs"
REPO = "https://github.com/NEXALongevity/skillset"
VERSION = "v0.1"

STAGES = [
    ("learn", "01", "了解", "Learn"),
    ("assess", "02", "评估", "Assess"),
    ("match", "03", "匹配", "Match"),
    ("travel", "04", "就医", "Travel"),
    ("recover", "05", "康复", "Recover"),
]
CROSS = ("cross-cutting", "∞", "全程", "Always on")
STAGE_INFO = {s[0]: s for s in STAGES + [CROSS]}

DIRECTIONS = [
    ("oncology", "肿瘤", "Oncology", "肿瘤学"),
    ("cardio-cerebrovascular", "心脑血管", "Cardio & cerebrovascular", "心血管病"),
    ("reproductive", "生殖", "Reproductive medicine", "生殖医学"),
    ("checkup-longevity", "体检与抗衰老", "Check-ups & longevity", "健康管理"),
    ("orthopedics", "骨科", "Orthopedics", "骨科"),
    ("aesthetics", "医疗美容", "Medical aesthetics", "整形外科"),
    ("tcm", "中医", "Traditional Chinese medicine", None),
]

ICON = {  # 24px stroke icons
    "china-healthcare-guide": '<path d="M3 21h18M5 21V8l7-5 7 5v13M9 21v-6h6v6M12 8v4M10 10h4"/>',
    "hospital-lookup": '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5M11 8v6M8 11h6"/>',
    "medical-record-summary": '<path d="M7 3h7l5 5v13H7zM14 3v5h5M10 13h6M10 17h6"/>',
    "needs-assessment": '<path d="M4 12h4l2-6 4 12 2-6h4"/>',
    "doctor-matching": '<circle cx="7" cy="7" r="3"/><circle cx="17" cy="17" r="3"/><path d="M10 7h4a3 3 0 0 1 3 3v4M7 10v4a3 3 0 0 0 3 3h4"/>',
    "visa-itinerary": '<path d="M2 16l20-8-4 10-6-3-3 4v-5z"/>',
    "multilingual-communication": '<path d="M4 5h8M8 3v2M6 5c0 4 3 7 6 8M10 5c0 3-3 7-6 8M13 21l4-9 4 9M14.5 18h5"/>',
    "compliance-check": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="m9 12 2 2 4-4"/>',
}

CSS = r"""
:root{
  --bg:#05070d;--bg2:#0a0f1c;--panel:rgba(255,255,255,.035);--panel-b:rgba(255,255,255,.08);
  --fg:#eef2fb;--muted:#8d97ad;--dim:#5b6478;
  --navy:#1d4f91;--blue:#3d8bff;--teal:#2ee6c8;--violet:#9b7bff;--pink:#ff7ac6;
  --grad:linear-gradient(100deg,#3d8bff 0%,#2ee6c8 38%,#9b7bff 72%,#ff7ac6 100%);
  --mono:ui-monospace,"SF Mono","JetBrains Mono",Menlo,Consolas,monospace;
  --sans:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Noto Sans SC",sans-serif;
}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.7 var(--sans);-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:inherit}
::selection{background:rgba(46,230,200,.3)}
.wrap{max-width:1160px;margin:0 auto;padding:0 24px}
@media(max-width:600px){.wrap{padding:0 16px}}
.mono{font-family:var(--mono)}
.grad{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}

/* nav */
.nav{position:fixed;inset:0 0 auto;z-index:50;backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);background:rgba(5,7,13,.6);border-bottom:1px solid var(--panel-b)}
.nav .wrap{display:flex;align-items:center;justify-content:space-between;height:64px}
.logo{display:flex;align-items:center;gap:10px;text-decoration:none;font-weight:700;letter-spacing:.14em;font-size:15px}
.logo .mark{width:28px;height:28px;border-radius:8px;background:var(--grad);display:grid;place-items:center;color:#05070d;font-family:var(--mono);font-size:13px;letter-spacing:0}
.logo small{font-weight:500;letter-spacing:.06em;color:var(--muted);font-size:12px;border-left:1px solid var(--panel-b);padding-left:10px}
.nav nav{display:flex;gap:28px;align-items:center;font-size:14px}
.nav nav a{text-decoration:none;color:var(--muted);transition:color .2s}.nav nav a:hover{color:var(--fg)}
.gh{display:inline-flex;align-items:center;gap:8px;border:1px solid var(--panel-b);padding:7px 14px;border-radius:999px;color:var(--fg)!important}
.gh:hover{border-color:var(--teal)}
@media(max-width:760px){.nav nav a:not(.gh){display:none}.logo small{display:none}}

/* hero */
.hero{position:relative;min-height:100vh;display:flex;align-items:center;padding:120px 0 80px;overflow:hidden}
#ribbons{position:absolute;inset:0;width:100%;height:100%;opacity:.9}
.hero::before{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px);background-size:56px 56px;mask-image:radial-gradient(ellipse 80% 70% at 50% 40%,#000 30%,transparent 80%);-webkit-mask-image:radial-gradient(ellipse 80% 70% at 50% 40%,#000 30%,transparent 80%)}
.hero::after{content:"";position:absolute;inset:auto 0 0;height:200px;background:linear-gradient(transparent,var(--bg))}
.hero .wrap{position:relative;z-index:2;width:100%}
.eyebrow{display:inline-flex;align-items:center;gap:10px;font:12px/1 var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--teal);border:1px solid rgba(46,230,200,.3);background:rgba(46,230,200,.06);padding:8px 14px;border-radius:999px}
.dot{width:7px;height:7px;border-radius:50%;background:var(--teal);box-shadow:0 0 12px var(--teal);animation:pulse 2s infinite}
@keyframes pulse{50%{opacity:.35}}
.hero h1{font-size:clamp(40px,7.2vw,92px);line-height:1.02;letter-spacing:-.035em;margin:28px 0 24px;font-weight:700}
.hero h1 .zh{display:block;font-size:.5em;letter-spacing:.02em;font-weight:600;margin-top:18px;color:var(--fg)}
.lead{font-size:clamp(16px,1.6vw,19px);color:var(--muted);max-width:640px;margin:0}
.lead b{color:var(--fg);font-weight:600}
.cta{display:flex;gap:14px;flex-wrap:wrap;margin-top:40px}
.btn{display:inline-flex;align-items:center;gap:10px;padding:14px 24px;border-radius:12px;text-decoration:none;font-weight:600;font-size:15px;transition:transform .2s,box-shadow .2s}
.btn.primary{background:var(--grad);color:#05070d;box-shadow:0 10px 40px -10px rgba(46,230,200,.5)}
.btn.primary:hover{transform:translateY(-2px);box-shadow:0 16px 50px -10px rgba(46,230,200,.7)}
.btn.ghost{border:1px solid var(--panel-b);background:var(--panel)}
.btn.ghost:hover{border-color:rgba(255,255,255,.25)}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;margin-top:72px;max-width:780px;background:var(--panel-b);border:1px solid var(--panel-b);border-radius:16px;overflow:hidden}
.stat{background:rgba(5,7,13,.75);padding:20px 22px;backdrop-filter:blur(6px)}
.stat b{display:block;font:600 34px/1 var(--mono);letter-spacing:-.02em}
.stat span{font-size:13px;color:var(--muted)}
@media(max-width:640px){.stats{grid-template-columns:repeat(2,1fr)}}

/* sections */
section.block{padding:120px 0;position:relative}
.kicker{font:12px/1 var(--mono);letter-spacing:.16em;color:var(--teal);text-transform:uppercase;margin-bottom:18px}
.kicker::before{content:"// ";color:var(--dim)}
h2.title{font-size:clamp(30px,4.4vw,54px);line-height:1.1;letter-spacing:-.025em;margin:0 0 18px;font-weight:700}
.sub{color:var(--muted);max-width:640px;margin:0 0 56px;font-size:17px}

/* pipeline */
.pipe{position:relative;display:grid;grid-template-columns:repeat(5,1fr);gap:16px}
.pipe::before{content:"";position:absolute;top:27px;left:5%;right:5%;height:1px;background:linear-gradient(90deg,transparent,var(--blue),var(--teal),var(--violet),transparent);opacity:.6}
.stage{position:relative}
.node{width:56px;height:56px;border-radius:16px;display:grid;place-items:center;font:600 14px var(--mono);background:var(--bg2);border:1px solid var(--panel-b);position:relative;z-index:1;margin-bottom:18px}
.stage.on .node{border-color:transparent;background:linear-gradient(var(--bg2),var(--bg2)) padding-box,var(--grad) border-box;border:1px solid transparent;box-shadow:0 0 30px -6px rgba(46,230,200,.45)}
.stage h3{margin:0;font-size:20px}.stage h3 small{font:12px var(--mono);color:var(--muted);margin-left:8px;letter-spacing:.06em}
.stage.off{opacity:.45}
.chips{display:flex;flex-direction:column;gap:8px;margin-top:14px}
.chip{display:block;font-size:13px;text-decoration:none;padding:8px 12px;border-radius:10px;background:var(--panel);border:1px solid var(--panel-b);transition:border-color .2s,transform .2s}
.chip:hover{border-color:var(--teal);transform:translateX(3px)}
.chip.soon{color:var(--dim);border-style:dashed}
.always{margin-top:28px;display:flex;align-items:center;gap:16px;flex-wrap:wrap;padding:18px 20px;border-radius:16px;border:1px solid var(--panel-b);background:linear-gradient(90deg,rgba(61,139,255,.06),rgba(155,123,255,.06))}
.always .lbl{font:12px var(--mono);color:var(--violet);letter-spacing:.12em;text-transform:uppercase}
@media(max-width:860px){.pipe{grid-template-columns:1fr 1fr}.pipe::before{display:none}}
@media(max-width:520px){.pipe{grid-template-columns:1fr}}

/* skill cards */
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px}
.card{position:relative;display:flex;flex-direction:column;padding:26px;border-radius:20px;background:var(--panel);border:1px solid var(--panel-b);text-decoration:none;overflow:hidden;transition:transform .3s,border-color .3s}
.card::before{content:"";position:absolute;inset:0;background:radial-gradient(400px circle at var(--mx,50%) var(--my,0%),rgba(46,230,200,.12),transparent 40%);opacity:0;transition:opacity .3s}
.card:hover{transform:translateY(-4px);border-color:rgba(46,230,200,.35)}.card:hover::before{opacity:1}
.card svg{width:26px;height:26px;stroke:url(#g);fill:none;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}
.card .meta{display:flex;justify-content:space-between;align-items:center;margin-bottom:22px}
.tag{font:11px var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--muted);border:1px solid var(--panel-b);padding:4px 8px;border-radius:6px}
.card h3{margin:0 0 4px;font-size:19px}
.card .en{font:12px var(--mono);color:var(--dim);margin-bottom:12px}
.card p{margin:0;color:var(--muted);font-size:14px;line-height:1.65;flex:1;display:-webkit-box;-webkit-line-clamp:4;-webkit-box-orient:vertical;overflow:hidden}
.card .go{margin-top:20px;font:12px var(--mono);color:var(--teal)}

/* terminal */
.split{display:grid;grid-template-columns:1fr 1.15fr;gap:56px;align-items:center}
@media(max-width:900px){.split{grid-template-columns:1fr}}
.term{border-radius:18px;border:1px solid var(--panel-b);background:#070b14;box-shadow:0 40px 120px -40px rgba(61,139,255,.35);overflow:hidden;font:13.5px/1.85 var(--mono)}
.term .bar{display:flex;gap:7px;align-items:center;padding:12px 16px;border-bottom:1px solid var(--panel-b);background:rgba(255,255,255,.02)}
.term .bar i{width:11px;height:11px;border-radius:50%;background:#2a3244}
.term .bar span{margin-left:10px;color:var(--dim);font-size:12px}
.term pre{margin:0;padding:22px 22px 26px;overflow-x:auto;white-space:pre}
.c-dim{color:var(--dim)}.c-t{color:var(--teal)}.c-b{color:var(--blue)}.c-v{color:var(--violet)}.c-p{color:var(--pink)}.c-w{color:var(--fg)}
.cursor{display:inline-block;width:8px;height:16px;background:var(--teal);vertical-align:-3px;animation:pulse 1s steps(1) infinite}
.steps{list-style:none;padding:0;margin:0;counter-reset:s}
.steps li{counter-increment:s;padding:0 0 26px 52px;position:relative;color:var(--muted)}
.steps li::before{content:"0" counter(s);position:absolute;left:0;top:0;font:600 13px var(--mono);color:var(--teal);border:1px solid rgba(46,230,200,.3);border-radius:8px;width:36px;height:28px;display:grid;place-items:center}
.steps b{display:block;color:var(--fg);font-size:17px;margin-bottom:2px}
.steps code{font:13px var(--mono);color:var(--fg);background:var(--panel);border:1px solid var(--panel-b);padding:2px 6px;border-radius:6px}

/* data */
.data{display:grid;grid-template-columns:1.4fr 1fr;gap:20px}
@media(max-width:900px){.data{grid-template-columns:1fr}}
.dirs{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:12px}
.dir{padding:20px;border-radius:16px;background:var(--panel);border:1px solid var(--panel-b)}
.dir .top{display:flex;justify-content:space-between;align-items:baseline}
.dir h4{margin:0;font-size:17px}.dir .n{font:600 26px var(--mono)}
.dir .en{font:11px var(--mono);color:var(--dim);letter-spacing:.06em;text-transform:uppercase}
.dir ol{margin:14px 0 0;padding:0;list-style:none;font-size:13px;color:var(--muted)}
.dir ol li{display:flex;gap:10px;padding:3px 0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.dir ol li span{font-family:var(--mono);color:var(--dim);width:18px;flex:none}
.dir details{margin-top:6px;font-size:13px;color:var(--muted)}
.dir summary{cursor:pointer;font:12px var(--mono);color:var(--teal);list-style:none}
.dir.soon{border-style:dashed;opacity:.6}
.panel{align-self:start;padding:26px;border-radius:20px;background:var(--panel);border:1px solid var(--panel-b)}
.panel h4{margin:0 0 4px;font-size:17px}.panel .sm{color:var(--muted);font-size:13px;margin-bottom:20px}
.bars{display:flex;flex-direction:column;gap:9px}
.bar-row{display:grid;grid-template-columns:52px 1fr 26px;gap:12px;align-items:center;font-size:13px}
.bar-row .track{height:8px;border-radius:99px;background:rgba(255,255,255,.05);overflow:hidden}
.bar-row .fill{height:100%;border-radius:99px;background:var(--grad);transform-origin:left;transform:scaleX(0);transition:transform 1.2s cubic-bezier(.2,.8,.2,1)}
.in .bar-row .fill{transform:scaleX(1)}
.bar-row .v{font-family:var(--mono);color:var(--muted);text-align:right}
.src{margin-top:22px;font-size:12px;color:var(--dim);line-height:1.6}
.src a{color:var(--muted)}

/* principles */
.prin{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
@media(max-width:900px){.prin{grid-template-columns:1fr 1fr}}@media(max-width:520px){.prin{grid-template-columns:1fr}}
.prin>div{padding:26px;border-radius:18px;border:1px solid var(--panel-b);background:var(--panel)}
.prin .k{font:600 13px var(--mono);color:var(--violet);margin-bottom:14px}
.prin h4{margin:0 0 8px;font-size:18px}.prin p{margin:0;font-size:14px;color:var(--muted)}

/* roadmap */
.road{display:grid;grid-template-columns:1fr 1fr;gap:16px}
@media(max-width:760px){.road{grid-template-columns:1fr}}
.ver{padding:30px;border-radius:20px;border:1px solid var(--panel-b);background:var(--panel)}
.ver.now{background:linear-gradient(var(--bg2),var(--bg2)) padding-box,var(--grad) border-box;border:1px solid transparent}
.ver .v{font:600 30px var(--mono)}.ver .st{font:12px var(--mono);color:var(--teal);letter-spacing:.1em;text-transform:uppercase;margin-left:10px}
.ver ul{margin:18px 0 0;padding:0;list-style:none;color:var(--muted);font-size:15px}
.ver li{padding:6px 0 6px 26px;position:relative}.ver li::before{content:"▸";position:absolute;left:4px;color:var(--teal)}
.ver:not(.now) li::before{content:"○";color:var(--dim)}

/* cta band + footer */
.band{margin:0 auto;padding:72px 48px;border-radius:28px;text-align:center;position:relative;overflow:hidden;border:1px solid var(--panel-b);background:radial-gradient(800px 300px at 50% 0%,rgba(61,139,255,.25),transparent),radial-gradient(600px 300px at 80% 100%,rgba(155,123,255,.2),transparent),var(--bg2)}
.band h2{font-size:clamp(28px,4vw,46px);margin:0 0 14px;letter-spacing:-.02em}
.band p{color:var(--muted);margin:0 auto 32px;max-width:560px}
.band .cta{justify-content:center;margin:0}
@media(max-width:600px){.band{padding:48px 20px}}
footer{padding:64px 0 48px;color:var(--dim);font-size:13px}
footer .row{display:flex;justify-content:space-between;gap:24px;flex-wrap:wrap;border-top:1px solid var(--panel-b);padding-top:32px}
footer a{color:var(--muted)}
.disc{max-width:620px;line-height:1.7}

/* reveal */
.rv{opacity:0;transform:translateY(24px);transition:opacity .8s,transform .8s}
.rv.in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){.rv{opacity:1;transform:none}.dot,.cursor{animation:none}html{scroll-behavior:auto}}

/* skill detail page */
.doc-hero{padding:130px 0 48px;border-bottom:1px solid var(--panel-b);position:relative;overflow:hidden}
.doc-hero::before{content:"";position:absolute;inset:0;background:radial-gradient(700px 300px at 20% 0%,rgba(61,139,255,.18),transparent),radial-gradient(500px 260px at 90% 20%,rgba(155,123,255,.14),transparent)}
.doc-hero .wrap{position:relative}
.crumb{font:12px var(--mono);color:var(--dim);margin-bottom:22px}.crumb a{color:var(--muted);text-decoration:none}
.doc-hero h1{font-size:clamp(32px,5vw,56px);line-height:1.1;letter-spacing:-.025em;margin:0 0 10px}
.doc-hero .en{font:14px var(--mono);color:var(--muted)}
.doc-hero .desc{max-width:720px;color:var(--muted);margin-top:18px}
.doc{display:grid;grid-template-columns:240px 1fr;gap:56px;padding:56px 0 40px}
@media(max-width:900px){.doc{grid-template-columns:1fr;gap:24px}}
.side{position:sticky;top:90px;align-self:start;display:flex;flex-direction:column;gap:14px}
@media(max-width:900px){.side{position:static}}
.kv{padding:16px;border-radius:14px;border:1px solid var(--panel-b);background:var(--panel);font-size:13px}
.kv div{display:flex;justify-content:space-between;padding:5px 0;gap:10px}.kv span{color:var(--dim);font-family:var(--mono);font-size:12px}
.kv .pend{color:#ffb86b}
.prose{min-width:0}
.prose h1{display:none}
.prose h2{font-size:22px;margin:44px 0 14px;padding-top:4px;letter-spacing:-.01em}
.prose h2:first-of-type{margin-top:0}
.prose p,.prose li{color:#c5ccdb}.prose strong{color:var(--fg)}
.prose a{color:var(--teal)}
.prose table{width:100%;border-collapse:collapse;font-size:14px;margin:8px 0 18px;display:block;overflow-x:auto}
.prose th,.prose td{border-bottom:1px solid var(--panel-b);padding:10px 12px;text-align:left;vertical-align:top}
.prose th{font:12px var(--mono);color:var(--muted);letter-spacing:.05em}
.prose pre{background:#070b14;border:1px solid var(--panel-b);border-radius:14px;padding:18px;overflow-x:auto;font:13px/1.75 var(--mono);color:#cfd6e6}
.prose code{font:.9em var(--mono);background:var(--panel);border:1px solid var(--panel-b);padding:1px 6px;border-radius:6px}
.prose pre code{background:none;border:0;padding:0}
.prose hr{border:0;border-top:1px solid var(--panel-b);margin:36px 0}
.prose blockquote{margin:0 0 16px;padding:10px 16px;border-left:2px solid var(--violet);color:var(--muted);background:var(--panel);border-radius:0 10px 10px 0}
.ex{margin-top:16px;border:1px solid var(--panel-b);border-radius:16px;background:var(--panel)}
.ex summary{cursor:pointer;padding:16px 20px;font-weight:600;list-style:none;display:flex;justify-content:space-between}
.ex summary::after{content:"+";font-family:var(--mono);color:var(--teal)}.ex[open] summary::after{content:"−"}
.ex .body{padding:0 20px 8px}
"""

JS = r"""
(()=>{
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12});
document.querySelectorAll('.rv').forEach(el=>io.observe(el));
document.querySelectorAll('.card').forEach(c=>c.addEventListener('pointermove',e=>{const r=c.getBoundingClientRect();c.style.setProperty('--mx',(e.clientX-r.left)+'px');c.style.setProperty('--my',(e.clientY-r.top)+'px')}));
const cv=document.getElementById('ribbons');if(!cv)return;
const ctx=cv.getContext('2d');let w,h,dpr=Math.min(devicePixelRatio||1,2),t=0;
const still=matchMedia('(prefers-reduced-motion: reduce)').matches;
const cols=[[61,139,255],[46,230,200],[155,123,255],[255,122,198]];
function size(){w=cv.clientWidth;h=cv.clientHeight;cv.width=w*dpr;cv.height=h*dpr;ctx.setTransform(dpr,0,0,dpr,0,0)}
function draw(){ctx.clearRect(0,0,w,h);ctx.globalCompositeOperation='lighter';
 for(let r=0;r<4;r++){const c=cols[r];
  for(let k=0;k<14;k++){ctx.beginPath();
   const amp=h*(.07+.025*r)+k*1.6,base=h*(.52+.07*(r-1.5)),ph=t*(.35+.08*r)+r*1.7+k*.05;
   for(let x=-20;x<=w+20;x+=14){const y=base+Math.sin(x*.0024+ph)*amp+Math.sin(x*.0011-ph*.6+r)*amp*.6+k*2.2;x<0?ctx.moveTo(x,y):ctx.lineTo(x,y)}
   ctx.strokeStyle=`rgba(${c[0]},${c[1]},${c[2]},${.09+.05*Math.sin(k*.6)})`;ctx.lineWidth=1.1;ctx.stroke()}}
 ctx.globalCompositeOperation='source-over';t+=.006;if(!still)requestAnimationFrame(draw)}
addEventListener('resize',size);size();draw();
})();
"""


def esc(s):
    return html.escape(s, quote=True)


SVG_DEFS = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>'
            '<linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3d8bff"/>'
            '<stop offset=".5" stop-color="#2ee6c8"/><stop offset="1" stop-color="#9b7bff"/></linearGradient></defs></svg>')


def shell(title, desc, body, depth=0):
    up = "../" * depth
    return f"""<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(desc)}">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}">
<meta name="theme-color" content="#05070d">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Cdefs%3E%3ClinearGradient id='a' x2='1' y2='1'%3E%3Cstop stop-color='%233d8bff'/%3E%3Cstop offset='.5' stop-color='%232ee6c8'/%3E%3Cstop offset='1' stop-color='%239b7bff'/%3E%3C/linearGradient%3E%3C/defs%3E%3Crect width='32' height='32' rx='8' fill='url(%23a)'/%3E%3Ctext x='16' y='21' font-family='monospace' font-size='13' font-weight='700' text-anchor='middle' fill='%2305070d'%3ENX%3C/text%3E%3C/svg%3E">
<link rel="stylesheet" href="{up}style.css"></head><body>{SVG_DEFS}
<header class="nav"><div class="wrap">
<a class="logo" href="{up}index.html"><span class="mark">NX</span>NEXA <small>SKILLS · {VERSION}</small></a>
<nav><a href="{up}index.html#journey">旅程 Journey</a><a href="{up}index.html#skills">Skills</a><a href="{up}index.html#data">数据 Data</a><a href="{up}index.html#roadmap">路线 Roadmap</a>
<a class="gh" href="{REPO}"><svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38v-1.33c-2.23.48-2.7-1.07-2.7-1.07-.36-.92-.89-1.17-.89-1.17-.73-.5.06-.49.06-.49.8.06 1.23.83 1.23.83.72 1.22 1.87.87 2.33.67.07-.52.28-.87.5-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.6 7.6 0 0 1 4 0c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48v2.2c0 .21.15.46.55.38A8 8 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>GitHub</a></nav>
</div></header>
{body}
<footer><div class="wrap"><div class="row">
<div class="disc"><b style="color:var(--fg)">NEXA Longevity</b> · Longevity as a Choice<br>
本站内容仅提供信息整理与流程支持，不构成诊断或治疗建议，一切以执业医生意见为准。<br>Information and workflow support only. Not medical advice.</div>
<div>代码 <a href="{REPO}/blob/main/LICENSE">Apache-2.0</a> · 内容 <a href="{REPO}/blob/main/LICENSE-CONTENT">CC BY 4.0</a><br>
使用请署名 NEXA Longevity<br><a href="https://nxlongevity.com">nxlongevity.com</a> · <a href="{REPO}">GitHub</a></div>
</div></div></footer>
<script>{JS}</script></body></html>"""


def load_skills():
    skills = []
    for d in sorted((ROOT / "skills").iterdir()):
        if not d.is_dir() or d.name.startswith("_"):
            continue
        text = (d / "SKILL.md").read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
        fm, body = yaml.safe_load(m.group(1)), m.group(2)
        title = re.search(r"^#\s+(.+)$", body, re.M).group(1)
        zh_title, _, en_title = title.partition(" · ")
        purpose = re.search(r"## 用途.*?\n\n(.+?)\n", body, re.S).group(1).replace("`", "")
        skills.append({"dir": d, "name": fm["name"], "desc": fm["description"], "meta": fm["metadata"],
                       "stage": fm["metadata"]["stage"], "zh": zh_title, "en": en_title,
                       "purpose": purpose, "body": body})
    order = [s[0] for s in STAGES] + ["cross-cutting"]
    skills.sort(key=lambda s: (order.index(s["stage"]), s["name"]))
    return skills


def md(text):
    return markdown.markdown(text, extensions=["tables", "fenced_code"])


def load_data():
    by_dir, cities, ids = {}, collections.Counter(), set()
    for f in sorted((ROOT / "data" / "hospitals").glob("*.yaml")):
        recs = yaml.safe_load(f.read_text(encoding="utf-8"))
        by_dir[f.stem] = recs
        for r in recs:
            cities[r["city"]] += 1
            ids.add(r["id"])
    return by_dir, cities, ids


def skill_page(s):
    st = STAGE_INFO[s["stage"]]
    meta = s["meta"]
    reviewed = meta.get("reviewed_by") or ""
    review_html = (f'<span>{esc(reviewed)} · {esc(str(meta.get("reviewed_on","")))}</span>' if reviewed
                   else '<b class="pend">待审核 Pending</b>')
    examples = sorted((s["dir"] / "examples").glob("*.md"))
    ex = "".join(
        f'<details class="ex"{" open" if i == 0 else ""}><summary>{esc(re.sub(r"^#\s*", "", e.read_text(encoding="utf-8").splitlines()[0]))}</summary>'
        f'<div class="body prose">{md(chr(10).join(e.read_text(encoding="utf-8").splitlines()[1:]))}</div></details>'
        for i, e in enumerate(examples))
    body = f"""
<section class="doc-hero"><div class="wrap">
<div class="crumb"><a href="../index.html">NEXA Skills</a> / <a href="../index.html#journey">{st[2]} {st[3]}</a> / {esc(s["name"])}</div>
<h1>{esc(s["zh"])}</h1><div class="en">{esc(s["en"])}</div>
<p class="desc">{esc(s["purpose"])}</p>
</div></section>
<div class="wrap"><div class="doc">
<aside class="side">
<div class="kv"><div><span>skill</span>{esc(s["name"])}</div><div><span>stage</span>{st[2]} · {st[3]}</div>
<div><span>version</span>{esc(str(meta.get("version","")))}</div><div><span>lang</span>{" / ".join(meta.get("languages",[]))}</div>
<div><span>review</span>{review_html}</div><div><span>license</span>CC BY 4.0</div></div>
<a class="btn primary" href="{REPO}/tree/main/skills/{s["name"]}">查看源码 Source</a>
<a class="btn ghost" href="{REPO}/archive/refs/heads/main.zip">下载全部 Download</a>
</aside>
<article class="prose">{md(s["body"])}<h2>示例 · Examples</h2>{ex}</article>
</div></div>"""
    return shell(f'{s["zh"]} · {s["en"]} | NEXA Skills', s["desc"], body, 1)


def index_page(skills, by_dir, cities, ids):
    total = sum(len(v) for v in by_dir.values())
    by_stage = collections.defaultdict(list)
    for s in skills:
        by_stage[s["stage"]].append(s)

    pipe = []
    for key, num, zh, en in STAGES:
        items = by_stage.get(key, [])
        chips = "".join(f'<a class="chip" href="skills/{s["name"]}.html">{esc(s["zh"])}</a>' for s in items) \
            or '<span class="chip soon">出院与回国随访 · v0.2</span>'
        pipe.append(f'<div class="stage {"on" if items else "off"} rv"><div class="node">{num}</div>'
                    f'<h3>{zh}<small>{en.upper()}</small></h3><div class="chips">{chips}</div></div>')
    always = "".join(f'<a class="chip" href="skills/{s["name"]}.html">{esc(s["zh"])}</a>' for s in by_stage["cross-cutting"])

    cards = []
    for s in skills:
        st = STAGE_INFO[s["stage"]]
        cards.append(f'<a class="card rv" href="skills/{s["name"]}.html"><div class="meta">'
                     f'<svg viewBox="0 0 24 24">{ICON.get(s["name"], "")}</svg><span class="tag">{st[1]} · {st[3]}</span></div>'
                     f'<h3>{esc(s["zh"])}</h3><div class="en">{esc(s["en"])}</div><p>{esc(s["purpose"])}</p>'
                     f'<div class="go">./skills/{s["name"]} →</div></a>')

    dirs = []
    for key, zh, en, spec in DIRECTIONS:
        recs = by_dir.get(key)
        if not recs:
            dirs.append(f'<div class="dir soon rv"><div class="top"><h4>{zh}</h4><span class="n">—</span></div>'
                        f'<div class="en">{en}</div><ol><li>v0.2 收录，待选定权威公开名单</li></ol></div>')
            continue
        top = "".join(f'<li><span>{r["ranking"]["rank"]:02d}</span>{esc(r["name_zh"])}</li>' for r in recs[:3])
        rest = "".join(f'<li><span>{r["ranking"]["rank"]:02d}</span>{esc(r["name_zh"])}</li>' for r in recs[3:])
        dirs.append(f'<div class="dir rv"><div class="top"><h4>{zh}</h4><span class="n">{len(recs)}</span></div>'
                    f'<div class="en">{en} · 榜单专科「{spec}」</div><ol>{top}</ol>'
                    f'<details><summary>+ 查看全部 {len(recs)} 家</summary><ol>{rest}</ol></details></div>')
    mx = max(cities.values())
    bars = "".join(f'<div class="bar-row"><span>{esc(c)}</span><div class="track"><div class="fill" style="width:{n / mx * 100:.0f}%"></div></div><span class="v">{n}</span></div>'
                   for c, n in cities.most_common(10))

    term = f"""<span class="c-dim"># 1 · 安装 install</span>
<span class="c-t">$</span> git clone {REPO}
<span class="c-t">$</span> cp -r skillset/skills/* ~/.claude/skills/

<span class="c-dim"># 2 · 用自然语言调用 just ask</span>
<span class="c-v">›</span> <span class="c-w">一位 47 岁泰国患者，左乳浸润性导管癌，想来广州看第二意见</span>

<span class="c-b">●</span> needs-assessment        <span class="c-t">✓</span> 适合推进 · 肿瘤
<span class="c-b">●</span> medical-record-summary  <span class="c-t">✓</span> 4 份材料 → 中英双语摘要
<span class="c-b">●</span> compliance-check        <span class="c-t">✓</span> 跨境传输已获同意
<span class="c-b">●</span> hospital-lookup         <span class="c-t">✓</span> 肿瘤学 · 10 家 · 有来源
<span class="c-b">●</span> doctor-matching         <span class="c-t">✓</span> 候选 3 家 · 含待确认问题
<span class="c-p">◆</span> 输出已附医学声明 · 以执业医生意见为准 <span class="cursor"></span>"""

    body = f"""
<section class="hero"><canvas id="ribbons" aria-hidden="true"></canvas><div class="wrap">
<span class="eyebrow"><span class="dot"></span>Open source · {VERSION} live</span>
<h1><span class="grad">AI Skills</span> for<br>medical travel to China.<span class="zh">跨境医疗旅游 Skills 库</span></h1>
<p class="lead">把中国顶尖医疗资源，变成任何 AI 都能调用的专业能力。<b>从病情评估、医院匹配到签证行程</b>，每一步都有统一、可溯源、守医学边界的标准流程。</p>
<p class="lead" style="margin-top:10px;font-size:15px">Open-source Skills that turn China's leading hospitals into structured, verifiable know-how any AI agent can use.</p>
<div class="cta"><a class="btn primary" href="#skills">探索 Skills →</a><a class="btn ghost" href="{REPO}">★ Star on GitHub</a></div>
<div class="stats">
<div class="stat"><b class="grad">{len(skills)}</b><span>Skills · 中英双语</span></div>
<div class="stat"><b>{len(ids)}</b><span>家医院 · {len(cities)} 座城市</span></div>
<div class="stat"><b>{len(by_dir)}</b><span>个重点方向</span></div>
<div class="stat"><b>100%</b><span>数据注明来源与核实日期</span></div>
</div></div></section>

<section class="block" id="journey"><div class="wrap">
<div class="kicker rv">Patient journey</div>
<h2 class="title rv">一条旅程，<span class="grad">五个阶段</span>。</h2>
<p class="sub rv">Skills 按国际患者赴华就医的真实路径组织。每个阶段的输出，都是下一阶段的标准输入。</p>
<div class="pipe">{''.join(pipe)}</div>
<div class="always rv"><span class="lbl">∞ Always on · 全程</span>{always}</div>
</div></section>

<section class="block" id="skills" style="padding-top:40px"><div class="wrap">
<div class="kicker rv">Skill library</div>
<h2 class="title rv">{len(skills)} 个 Skills，<span class="grad">即插即用</span>。</h2>
<p class="sub rv">每个 Skill 都是一个包含 SKILL.md 的目录：用途、输入、步骤、输出格式、边界与医学声明一应俱全，附虚构病例示例，兼作测试用例。</p>
<div class="grid">{''.join(cards)}</div>
</div></section>

<section class="block"><div class="wrap split">
<div class="rv"><div class="kicker">Get started</div>
<h2 class="title">两行命令，<br><span class="grad">顾问变专家团</span>。</h2>
<ol class="steps">
<li><b>克隆仓库</b>放进 Claude Code、Claude.ai 或任何支持 Agent Skills 的工具。</li>
<li><b>用自然语言描述病例</b>AI 会按需调用对应 Skill，不需要记任何命令。</li>
<li><b>拿到可复核的结果</b>每条医院信息都带来源与核实日期，可用 <code>scripts/validate.py</code> 校验。</li>
</ol></div>
<div class="term rv"><div class="bar"><i></i><i></i><i></i><span>nexa-skills — 示例会话 example</span></div><pre>{term}</pre></div>
</div></section>

<section class="block" id="data"><div class="wrap">
<div class="kicker rv">Verified knowledge base</div>
<h2 class="title rv">只收录<span class="grad">有出处</span>的数据。</h2>
<p class="sub rv">{VERSION} 共 {total} 条医院记录，来自复旦大学医院管理研究所《2023 年度中国医院专科声誉排行榜》。查不到就说查不到，绝不凭记忆补充。</p>
<div class="data"><div class="dirs">{''.join(dirs)}</div>
<div class="panel rv"><h4>城市分布 · Top 10</h4><div class="sm">{len(ids)} 家医院分布在 {len(cities)} 座城市（按记录数）</div>
<div class="bars">{bars}</div>
<div class="src">来源：<a href="https://www.cn-healthcare.com/article/20241116/content-585244.html">复旦版 2023 年度中国医院专科声誉排行榜</a>（健康界经授权发布）· 核实日期 2026-11-27 · 排名仅反映该榜单评价，不代表推荐。</div></div>
</div></div></section>

<section class="block" style="padding-top:40px"><div class="wrap">
<div class="kicker rv">Principles</div>
<h2 class="title rv">专业，<span class="grad">从边界开始</span>。</h2>
<p class="sub rv">每个 Skill 上线前都要通过医学审核与合规审核。</p>
<div class="prin">
<div class="rv"><div class="k">01 / SOURCED</div><h4>来源可溯</h4><p>医院与政策信息只用官方公开资料，逐条标注来源与核实日期。</p></div>
<div class="rv"><div class="k">02 / BOUNDED</div><h4>守医学边界</h4><p>只做信息整理与流程支持，不诊断、不推荐治疗，以执业医生意见为准。</p></div>
<div class="rv"><div class="k">03 / PRIVATE</div><h4>隐私优先</h4><p>最小必要原则，跨境传输前取得同意；仓库只用虚构病例。</p></div>
<div class="rv"><div class="k">04 / OPEN</div><h4>开源署名</h4><p>代码 Apache-2.0，内容 CC BY 4.0，自由使用，署名 NEXA Longevity。</p></div>
</div></div></section>

<section class="block" id="roadmap" style="padding-top:40px"><div class="wrap">
<div class="kicker rv">Roadmap</div>
<h2 class="title rv">这只是<span class="grad">开始</span>。</h2>
<div class="road" style="margin-top:40px">
<div class="ver now rv"><span class="v">{VERSION}</span><span class="st">● Live</span><ul>
<li>8 个 P0 Skills，覆盖了解、评估、匹配、就医与全程支持</li><li>6 个方向 {total} 条医院记录，全部注明来源</li><li>医学术语表、开发规范与自动校验</li><li>中文、英文</li></ul></div>
<div class="ver rv"><span class="v">v0.2</span><span class="st" style="color:var(--muted)">Next</span><ul>
<li>中医方向、脑血管专科、专家档案</li><li>民营医院与在华外资医院</li><li>P1 Skills：方案对比、远程会诊、报价、陪同手册、随访、案例复盘</li><li>法语、西班牙语、繁体中文</li></ul></div>
</div></div></section>

<section class="block" style="padding-top:20px"><div class="wrap"><div class="band rv">
<h2>一起定义<span class="grad">跨境医疗的标准</span></h2>
<p>欢迎医生、医疗机构、跨境医疗从业者和开发者参与贡献。每一个 Skill，都让下一位国际患者少走一段弯路。</p>
<div class="cta"><a class="btn primary" href="{REPO}">参与贡献 Contribute →</a><a class="btn ghost" href="https://nxlongevity.com">了解 NEXA Longevity</a></div>
</div></div></section>
"""
    return shell("NEXA Skills · 跨境医疗旅游 Skills 库 | AI Skills for medical travel to China",
                 "Open-source AI Skills for cross-border medical travel to China, by NEXA Longevity.", body)


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "skills").mkdir(parents=True)
    (OUT / "style.css").write_text(CSS, encoding="utf-8")
    (OUT / "CNAME").write_text("skills.nxlongevity.com\n")
    (OUT / ".nojekyll").write_text("")
    skills = load_skills()
    by_dir, cities, ids = load_data()
    for s in skills:
        (OUT / "skills" / f'{s["name"]}.html').write_text(skill_page(s), encoding="utf-8")
    (OUT / "index.html").write_text(index_page(skills, by_dir, cities, ids), encoding="utf-8")
    print(f"Built {len(skills)} skill pages, {sum(len(v) for v in by_dir.values())} records, {len(ids)} hospitals")


if __name__ == "__main__":
    main()
