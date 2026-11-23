#!/usr/bin/env python3
"""ContractorRules static site. Reads data/ and writes dist/. Standard library only.

Usage: python3 site/build.py   (from the repo root)
"""
import html, json, shutil
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA, SRC, DIST = ROOT / "data", ROOT / "site", ROOT / "dist"
SITE = "https://contractorrules.com"
INDEX = True
e = html.escape

GROUPS = {"236": "Construction of buildings", "237": "Heavy and civil engineering construction", "238": "Specialty trade contractors"}
PROPOSED_RULE = "https://www.federalregister.gov/documents/2026/08/20/2026-17042/small-business-size-standards"


def human(d):
    return datetime.strptime(d, "%Y-%m-%d").strftime("%B %-d, %Y")


def std(r):
    if r["receipts_musd"] is not None:
        v = r["receipts_musd"]
        return f"${v:g} million", "average annual receipts"
    if r["employees"] is not None:
        return f"{r['employees']:,} employees", "average employment"
    return "See SBA footnote", ""


def page(path, title, desc, body, current="", extra=""):
    nav = [("/naics/construction/", "Construction NAICS codes", "naics"), ("/about/", "About the data", "about")]
    links = "".join(f'<a href="{h}"{" aria-current=page" if k == current else ""}>{t}</a>' for h, t, k in nav)
    robots = "" if INDEX else '<meta name="robots" content="noindex">\n'
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
{robots}<link rel="canonical" href="{SITE}{path}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{SITE}{path}">
<meta name="theme-color" content="#1F2A33">
<link rel="icon" href="/assets/logo.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
{extra}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top"><div class="wrap">
<a class="brand" href="/"><img src="/assets/logo.svg" alt="" width="34" height="34">ContractorRules</a>
<nav class="nav" aria-label="Main">{links}</nav>
</div></header>
<main id="main">
{body}
</main>
<footer class="foot"><div class="wrap">
<span>ContractorRules organizes public government data for US contractors. It is not legal advice and is not affiliated with any government agency.</span>
<span><a href="/about/">About the data</a> · <a href="/privacy/">Privacy</a> · <a href="mailto:info@sahirgur.com">Contact</a></span>
</div></footer>
</body>
</html>
"""


def intro(h1, p, crumbs=None):
    c = '<div class="crumbs">' + " / ".join(f'<a href="{u}">{e(t)}</a>' for u, t in crumbs) + "</div>" if crumbs else ""
    return f'<section class="intro"><div class="wrap">{c}<h1>{e(h1)}</h1><p>{p}</p></div></section>'


def proposal_notice():
    return (f'<div class="notice"><p><b>Proposed change, not yet in effect.</b> On August 20, 2026 SBA proposed new size standards that would move '
            f'construction from receipts-based to employee-based limits. Until a final rule takes effect, the current standards on this page apply.</p>'
            f'<p class="note"><a href="{PROPOSED_RULE}">Read the proposed rule in the Federal Register</a>.</p></div>')


def build():
    rows = json.loads((DATA / "sba" / "size-standards.json").read_text())
    state = json.loads((DATA / "sba" / "state.json").read_text())
    eff = human(state["effective"])
    con = [r for r in rows if r["naics"].startswith("23")]
    main = [r for r in con if not r["exception"]]
    exc = {r["naics"]: [x for x in con if x["exception"] and x["naics"] == r["naics"]] for r in main}

    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    shutil.copytree(SRC / "assets", DIST / "assets")
    for f in (SRC / "static").glob("*"):
        shutil.copy(f, DIST / f.name)
    pages = {}

    # ---- table of construction codes
    trs = []
    for g, label in GROUPS.items():
        trs.append(f'<tr class="group"><td colspan="3">{g} · {e(label)}</td></tr>')
        for r in [x for x in main if x["naics"].startswith(g)]:
            v, basis = std(r)
            trs.append(f'<tr><td class="code"><a href="/naics/{r["naics"]}/">{r["naics"]}</a></td><td>{e(r["title"])}</td><td class="num"><b>{v}</b></td></tr>')
            for x in exc[r["naics"]]:
                xv, _ = std(x)
                trs.append(f'<tr><td></td><td class="note">Exception: {e(x["title"])}</td><td class="num">{xv}</td></tr>')
    body = intro("SBA size standards for construction NAICS codes",
                 f'The largest a construction business can be and still count as small for federal contracts and SBA programs, for every construction industry code. '
                 f'Source: SBA table of size standards effective {eff}.', [("/", "ContractorRules"), ("/naics/construction/", "NAICS")])
    body += f"""<section><div class="wrap">{proposal_notice()}</div></section>
<section style="padding-top:0"><div class="wrap">
<h2>All {len(main)} construction industries</h2>
<p class="sub">All construction size standards are measured in average annual receipts. Select a code to check a business against it.</p>
<div class="tablewrap"><table><thead><tr><th>NAICS</th><th>Industry</th><th class="num">Size standard</th></tr></thead><tbody>{"".join(trs)}</tbody></table></div>
<p class="note">Source: U.S. Small Business Administration, Table of Small Business Size Standards (13 CFR 121.201), effective {eff}. Retrieved from data.sba.gov.</p>
</div></section>"""
    pages["/naics/construction/"] = page("/naics/construction/", "SBA size standards for construction NAICS codes (236, 237, 238) | ContractorRules",
        f"Current SBA small business size standards for all {len(main)} construction NAICS codes: $45 million for building and heavy construction, $19 million for most specialty trades.", body, "naics")

    # ---- one page per code
    for r in main:
        code, g = r["naics"], r["naics"][:3]
        v, basis = std(r)
        sib = [x for x in main if x["naics"].startswith(g) and x["naics"] != code]
        sib_rows = "".join(f'<tr><td class="code"><a href="/naics/{x["naics"]}/">{x["naics"]}</a></td><td>{e(x["title"])}</td><td class="num">{std(x)[0]}</td></tr>' for x in sib)
        exc_html = ""
        if exc[code]:
            exc_html = "<h2>Exceptions under this code</h2><p class=\"sub\">SBA sets a different standard for these activities within the code.</p><div class=\"tablewrap\"><table><tbody>" + "".join(
                f'<tr><td>{e(x["title"])}</td><td class="num"><b>{std(x)[0]}</b></td><td class="note">{e(x["footnote"] or "")}</td></tr>' for x in exc[code]) + "</tbody></table></div>"
        limit = r["receipts_musd"]
        checker = ""
        if limit is not None:
            checker = f"""<div class="card"><h3>Check a business</h3>
<form class="check" id="check" novalidate>
<label for="rec">Average annual receipts, in US dollars<input id="rec" inputmode="decimal" autocomplete="off" placeholder="e.g. 12,500,000"></label>
<button type="submit">Check against {v}</button>
<div id="out" role="status"></div>
</form>
<p class="note">Use the average of the business’s receipts over its last five completed fiscal years, including affiliates. This is a quick screen, not an official size determination.</p></div>
<script>
(function(){{var f=document.getElementById('check'),i=document.getElementById('rec'),o=document.getElementById('out'),L={limit}*1e6;
f.addEventListener('submit',function(ev){{ev.preventDefault();var n=parseFloat(String(i.value).replace(/[$,\\s]/g,''));
if(!isFinite(n)||n<0){{o.className='result no';o.textContent='Enter an amount in dollars, for example 12500000.';return;}}
if(n<=L){{o.className='result yes';o.textContent='At or under the limit: likely small under NAICS {code} ('+Math.round((L-n)/1e5)/10+' million below {v}).';}}
else{{o.className='result no';o.textContent='Over the limit: not small under NAICS {code} ('+Math.round((n-L)/1e5)/10+' million above {v}).';}}}});}})();
</script>"""
        body = intro(f"NAICS {code}: {r['title']}",
                     f'SBA small business size standard: <b>{v}</b> in {basis}. Effective {eff}.',
                     [("/", "ContractorRules"), ("/naics/construction/", "Construction NAICS codes")])
        body += f"""<section><div class="wrap grid">
<div class="card"><div class="k">SBA size standard</div><div class="v">{v}</div><div class="n">{basis}, including affiliates</div></div>
{checker}
</div></section>
<section style="padding-top:0"><div class="wrap"><div class="prose">
<h2>What the size standard means</h2>
<p>A business whose primary industry is NAICS {code} counts as small for federal contracting and most SBA programs if its {basis} are at or below {v}. Receipts are averaged over the business’s latest five completed fiscal years, and the receipts of affiliated companies are added in.</p>
<p>Federal contracting officers assign one NAICS code to each solicitation. When you bid on a small business set-aside, you must be small under the code on that solicitation, which may differ from your primary code. You represent your size for each NAICS code in your SAM.gov registration.</p>
</div></div></section>
<section style="padding-top:0"><div class="wrap">{proposal_notice()}</div></section>
<section style="padding-top:0"><div class="wrap">{exc_html}
<h2>Other codes in {g} · {e(GROUPS[g])}</h2>
<div class="tablewrap"><table><thead><tr><th>NAICS</th><th>Industry</th><th class="num">Size standard</th></tr></thead><tbody>{sib_rows}</tbody></table></div>
<p class="note">Source: U.S. Small Business Administration, Table of Small Business Size Standards (13 CFR 121.201), effective {eff}. Size is determined under 13 CFR 121.104 (receipts) and 121.103 (affiliation). Confirm with SBA before relying on it for a bid.</p>
</div></section>"""
        pages[f"/naics/{code}/"] = page(f"/naics/{code}/", f"NAICS {code} size standard: {v} | {r['title']} | ContractorRules",
            f"SBA small business size standard for NAICS {code} ({r['title']}): {v} in {basis}. Check a business in seconds.", body, "naics")

    # ---- home
    n45 = sum(1 for r in main if r["receipts_musd"] == 45)
    n19 = sum(1 for r in main if r["receipts_musd"] == 19)
    body = intro("Compliance data for US construction contractors",
                 "Federal and state rules for contractors are spread across dozens of agencies. ContractorRules collects them from official sources, keeps them current and puts them in one place.")
    body += f"""<section><div class="wrap grid">
<a class="card" href="/naics/construction/" style="text-decoration:none;color:inherit">
<div class="k">Federal contracting · SBA</div><h2 style="margin:6px 0">Construction size standards</h2>
<p class="note" style="margin:0">Is your business “small” for set-aside contracts? {n45} building and heavy construction codes have a $45 million limit and {n19} specialty trade codes a $19 million limit. Check any of the {len(main)} construction codes.</p>
<p style="margin:14px 0 0"><span style="text-decoration:underline;text-decoration-color:var(--amber);text-decoration-thickness:2px">See all construction codes</span></p></a>
<div class="card"><div class="k">Coming next</div><h2 style="margin:6px 0">More rules, state by state</h2>
<p class="note" style="margin:0">Contractor license requirements by state and trade, California license data, and federal prevailing wage rates.</p></div>
</div></section>
<section style="padding-top:0"><div class="wrap">{proposal_notice()}</div></section>"""
    pages["/"] = page("/", "ContractorRules: compliance data for US construction contractors",
                      "SBA size standards for every construction NAICS code, with more contractor rules coming. Collected from official sources.", body)

    about = intro("About the data", "Where every rule on ContractorRules comes from, how it is kept current and what it can’t tell you.")
    about += f"""<section><div class="wrap"><div class="prose">
<h2>Sources</h2>
<p><b>Size standards</b> come from the U.S. Small Business Administration’s Table of Small Business Size Standards, published on data.sba.gov. The current table took effect on {eff}. An automated job checks for a newer table every week.</p>
<h2>How it is checked</h2>
<p>Each new file is compared with the previous one. If its layout changes or records disappear, nothing is published until a person has checked it.</p>
<h2>What it can’t tell you</h2>
<p>ContractorRules shows public government data as published. It is not legal advice and does not replace an official size determination, license verification or a contracting officer’s decision. Always confirm with the issuing agency before you bid or sign.</p>
<h2>Corrections</h2>
<p>If you spot an error, email <a href="mailto:info@sahirgur.com">info@sahirgur.com</a>.</p>
</div></div></section>"""
    pages["/about/"] = page("/about/", "About the data | ContractorRules", "Sources, update method and limits of ContractorRules data.", about, "about")

    privacy = intro("Privacy", "What ContractorRules collects about visitors.")
    privacy += """<section><div class="wrap"><div class="prose">
<p>ContractorRules has no accounts and no analytics or advertising cookies. The size check runs entirely in your browser: the numbers you type are not sent anywhere. Our hosting provider keeps standard server logs (such as IP address and pages requested) for security and to keep the site running.</p>
<p>If analytics or advertising are added later, this page will be updated first and will explain what those services collect and how to opt out.</p>
<p>Questions: <a href="mailto:info@sahirgur.com">info@sahirgur.com</a>.</p>
</div></div></section>"""
    pages["/privacy/"] = page("/privacy/", "Privacy | ContractorRules", "What ContractorRules collects about visitors.", privacy)
    pages["/404.html"] = page("/404.html", "Page not found | ContractorRules", "Page not found.",
                              intro("Page not found", 'The address may have changed. Try the <a href="/">home page</a>.'))

    for path, content in pages.items():
        out = DIST / "404.html" if path == "/404.html" else DIST / path.strip("/") / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(content, encoding="utf-8")
    urls = [p for p in pages if p != "/404.html"]
    (DIST / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
                                      "".join(f"<url><loc>{SITE}{u}</loc></url>\n" for u in urls) + "</urlset>\n", encoding="utf-8")
    (DIST / "robots.txt").write_text("User-agent: *\n" + ("Allow: /\n" if INDEX else "Disallow:\n") + f"Sitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
    print(f"pages: {len(pages)}")


if __name__ == "__main__":
    build()
