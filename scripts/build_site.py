#!/usr/bin/env python3
"""Build the static site in docs/ (served by GitHub Pages at skills.nxlongevity.com).

Usage: python scripts/build_site.py
Requires: pyyaml, markdown
"""
import html
import re
import shutil
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs"
REPO = "https://github.com/NEXALongevity/skillset"
STAGE_ORDER = ["learn", "assess", "match", "travel", "recover", "cross-cutting"]
STAGE_LABEL = {
    "learn": ("了解", "Learn"), "assess": ("评估", "Assess"), "match": ("匹配", "Match"),
    "travel": ("就医", "Travel"), "recover": ("康复", "Recover"), "cross-cutting": ("全程", "All stages"),
}
DIRECTION_LABEL = {
    "oncology": ("肿瘤", "Oncology"), "cardio-cerebrovascular": ("心脑血管", "Cardio & cerebrovascular"),
    "reproductive": ("生殖", "Reproductive medicine"), "checkup-longevity": ("体检与抗衰老", "Check-ups & longevity"),
    "orthopedics": ("骨科", "Orthopedics"), "aesthetics": ("医疗美容", "Medical aesthetics"),
}

CSS = """
:root{--bg:#fbfaf7;--fg:#1d2522;--muted:#5d6864;--line:#e3e0d8;--card:#fff;--accent:#0f6b5c;--accent-soft:#e4f1ee}
@media (prefers-color-scheme:dark){:root{--bg:#131816;--fg:#e8ece9;--muted:#9aa6a1;--line:#2a332f;--card:#1a201e;--accent:#5cc2ad;--accent-soft:#1d2d29}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Noto Sans SC",sans-serif}
a{color:var(--accent)}.wrap{max-width:960px;margin:0 auto;padding:0 16px}
header{border-bottom:1px solid var(--line)}header .wrap{display:flex;justify-content:space-between;align-items:center;padding:14px 16px;gap:12px;flex-wrap:wrap}
.brand{font-weight:700;letter-spacing:.02em;text-decoration:none;color:var(--fg)}.brand span{color:var(--accent)}
nav a{margin-left:16px;text-decoration:none;color:var(--muted);font-size:14px}
.hero{padding:56px 0 32px}.hero h1{font-size:clamp(28px,5vw,42px);line-height:1.2;margin:0 0 12px}
.hero p{color:var(--muted);max-width:680px;margin:0 0 8px}.tag{display:inline-block;background:var(--accent-soft);color:var(--accent);border-radius:999px;padding:2px 10px;font-size:13px;margin-bottom:16px}
.btn{display:inline-block;background:var(--accent);color:#fff;padding:10px 18px;border-radius:8px;text-decoration:none;margin:16px 8px 0 0;font-weight:600}
.btn.ghost{background:transparent;color:var(--accent);border:1px solid var(--accent)}
h2{font-size:22px;margin:40px 0 4px}.sub{color:var(--muted);margin:0 0 16px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:12px}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px;text-decoration:none;color:var(--fg);display:block}
.card:hover{border-color:var(--accent)}.card .stage{font-size:12px;color:var(--accent);font-weight:600;text-transform:uppercase;letter-spacing:.04em}
.card h3{margin:6px 0 4px;font-size:17px}.card p{margin:0;color:var(--muted);font-size:14px}
table{border-collapse:collapse;width:100%;font-size:14px}th,td{border-bottom:1px solid var(--line);padding:8px 6px;text-align:left;vertical-align:top}
.tablewrap{overflow-x:auto}.note{background:var(--accent-soft);border-radius:10px;padding:14px 16px;font-size:14px;margin:32px 0}
footer{border-top:1px solid var(--line);margin-top:48px;padding:24px 0;color:var(--muted);font-size:13px}
article{padding:32px 0}article h1{font-size:28px}article pre{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:12px;overflow-x:auto;font-size:13px}
article code{font-size:.92em}
"""


def page(title, body, depth=0):
    up = "../" * depth
    return f"""<!doctype html><html lang="zh"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="Open-source AI Skills for cross-border medical travel to China, by NEXA Longevity.">
<link rel="stylesheet" href="{up}style.css"></head><body>
<header><div class="wrap"><a class="brand" href="{up}index.html">NEXA <span>Skills</span></a>
<nav><a href="{up}index.html#skills">Skills</a><a href="{up}index.html#data">数据 Data</a><a href="{REPO}">GitHub</a></nav></div></header>
<main class="wrap">{body}</main>
<footer><div class="wrap">© NEXA Longevity · <a href="https://nxlongevity.com">nxlongevity.com</a> · 代码 Apache-2.0，内容 CC BY 4.0，使用请署名 NEXA Longevity。<br>
本站内容仅提供信息与流程支持，不构成医疗建议，一切以执业医生意见为准。Not medical advice.</div></footer>
</body></html>"""


def load_skills():
    skills = []
    for d in sorted((ROOT / "skills").iterdir()):
        if not d.is_dir() or d.name.startswith("_"):
            continue
        text = (d / "SKILL.md").read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
        fm, body = yaml.safe_load(m.group(1)), m.group(2)
        title = re.search(r"^#\s+(.+)$", body, re.M).group(1)
        zh = re.search(r"## 用途.*?\n\n(.+?)\n", body, re.S).group(1).replace("`", "")
        skills.append({"dir": d, "name": fm["name"], "desc": fm["description"], "stage": fm["metadata"]["stage"],
                       "title": title, "zh": zh, "body": body})
    skills.sort(key=lambda s: (STAGE_ORDER.index(s["stage"]), s["name"]))
    return skills


def md(text):
    return markdown.markdown(text, extensions=["tables", "fenced_code"])


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "skills").mkdir(parents=True)
    (OUT / "style.css").write_text(CSS, encoding="utf-8")
    (OUT / "CNAME").write_text("skills.nxlongevity.com\n")
    (OUT / ".nojekyll").write_text("")

    skills = load_skills()
    cards = []
    for s in skills:
        zh, en = STAGE_LABEL[s["stage"]]
        cards.append(f'<a class="card" href="skills/{s["name"]}.html"><div class="stage">{zh} · {en}</div>'
                     f'<h3>{html.escape(s["title"])}</h3><p>{html.escape(s["zh"])}</p></a>')
        examples = sorted((s["dir"] / "examples").glob("*.md"))
        ex_html = "".join(f"<h2>{html.escape(e.stem)}</h2>" + md(e.read_text(encoding="utf-8")) for e in examples)
        body = (f'<article>{md(s["body"])}<p><a class="btn" href="{REPO}/tree/main/skills/{s["name"]}">'
                f'在 GitHub 查看 / View on GitHub</a></p><h2>示例 Examples</h2>{ex_html}</article>')
        (OUT / "skills" / f'{s["name"]}.html').write_text(page(s["title"] + " · NEXA Skills", body, 1), encoding="utf-8")

    rows, total = [], 0
    for f in sorted((ROOT / "data" / "hospitals").glob("*.yaml")):
        recs = yaml.safe_load(f.read_text(encoding="utf-8"))
        total += len(recs)
        zh, en = DIRECTION_LABEL.get(f.stem, (f.stem, f.stem))
        names = "、".join(r["name_zh"] for r in recs)
        rows.append(f"<tr><td><b>{zh}</b><br><span class='sub'>{en}</span></td><td>{len(recs)}</td><td>{html.escape(names)}</td></tr>")

    body = f"""
<section class="hero"><span class="tag">v0.1 · Open source</span>
<h1>跨境医疗旅游 Skills 库<br>Medical Travel Skills for China</h1>
<p>一套开源的 AI Skills，帮助跨境医疗从业人员为国际患者找到中国合适的医生、医院与治疗方案，并精准、及时地完成赴华就医。</p>
<p>Open-source AI Skills that help medical travel professionals guide international patients to the right hospitals and treatments in China.</p>
<p><b>Longevity as a Choice.</b></p>
<a class="btn" href="{REPO}">GitHub</a><a class="btn ghost" href="#skills">浏览 Skills</a></section>

<h2 id="skills">Skills（{len(skills)}）</h2><p class="sub">按患者旅程组织：了解 → 评估 → 匹配 → 就医，另有贯穿全程的支持。</p>
<div class="grid">{''.join(cards)}</div>

<h2>如何使用 · How to use</h2>
<p class="sub">每个 Skill 是一个包含 SKILL.md 的目录，可直接放入 Claude Code、Claude.ai 或其他支持 Agent Skills 的工具。</p>
<pre style="background:var(--card);border:1px solid var(--line);border-radius:8px;padding:12px;overflow-x:auto"><code>git clone {REPO}
cp -r skillset/skills/doctor-matching ~/.claude/skills/</code></pre>

<h2 id="data">医院知识库 · Hospital data</h2>
<p class="sub">v0.1 共 {total} 条，取自复旦大学医院管理研究所《2023年度中国医院专科声誉排行榜》，每条注明来源与核实日期。中医方向在 v0.2 加入。</p>
<div class="tablewrap"><table><tr><th>方向</th><th>数量</th><th>医院</th></tr>{''.join(rows)}</table></div>

<div class="note"><b>医学声明 · Disclaimer</b><br>本库仅提供信息整理、解释与流程支持，不提供诊断或治疗决策，一切以执业医生意见为准。This library provides information and workflow support only and is not medical advice.</div>
"""
    (OUT / "index.html").write_text(page("NEXA Medical Travel Skills · 跨境医疗旅游 Skills 库", body), encoding="utf-8")
    print(f"Built {len(skills)} skill pages, {total} hospital records -> {OUT}")


if __name__ == "__main__":
    main()
