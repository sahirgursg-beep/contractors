"""Explainer guides: /guides/ and /guides/<slug>/."""
from html import escape as e

REVIEWED = "2026-11-27"

GUIDES = [
    {
        "slug": "how-to-bid-federal-construction-contracts",
        "title": "How to find and bid on federal construction contracts",
        "short": "Bidding on federal work",
        "desc": "SAM.gov registration, NAICS codes and size standards, set-asides, Miller Act bonds and Davis-Bacon wages: what a contractor needs before bidding on federal construction.",
        "tool": ("/federal-bids/", "See open federal construction bids"),
        "body": """
<p>Federal agencies buy billions of dollars of construction every year, from roof repairs at a post office to new buildings at military bases. Most of it is advertised publicly on SAM.gov, and small businesses get a large share through set-asides. The paperwork is front-loaded: get it done once and every bid after that is easier.</p>
<h2>1. Register in SAM.gov</h2>
<p>To be awarded a federal contract, your business must be registered in the System for Award Management (SAM.gov). Registration gives you a Unique Entity ID (UEI) and asks for your legal business details, banking information, NAICS codes and representations and certifications. Registration is free and must be renewed every year; be wary of companies that charge to “register” you.</p>
<h2>2. Choose your NAICS codes and check your size</h2>
<p>Construction work falls under NAICS sector 23: 236 for building construction, 237 for heavy and civil engineering, and 238 for specialty trades. Each code has a small business size standard set by the SBA, usually measured by average annual receipts. If your receipts are under the standard for the code on a solicitation, you count as small for that contract.</p>
<h2>3. Understand set-asides</h2>
<p>Many solicitations are reserved for small businesses or for programs such as 8(a), HUBZone, service-disabled veteran-owned (SDVOSB) and women-owned (WOSB). The solicitation states the set-aside; you need the matching status or certification before you bid.</p>
<h2>4. Bonds</h2>
<p>Under the Miller Act, federal construction contracts over $150,000 require performance and payment bonds, normally each for 100% of the contract price, and a bid guarantee (bid bond) when bonds are required. For contracts over $35,000 up to $150,000 the contracting officer requires alternative payment protection, such as a payment bond or an irrevocable letter of credit. Talk to a surety early: your bonding capacity limits the size of the jobs you can win.</p>
<h2>5. Davis-Bacon wages</h2>
<p>Federal construction contracts over $2,000 are covered by the Davis-Bacon Act: you must pay laborers and mechanics at least the prevailing wages and fringe benefits in the wage determination attached to the solicitation, and submit certified payrolls weekly. Price your bid with those rates, not your usual pay scale.</p>
<h2>6. Read the notice type</h2>
<ul><li><b>Sources sought / RFI:</b> market research. Responding is how you tell the agency small businesses can do the work, which can lead to a set-aside.</li>
<li><b>Presolicitation:</b> advance notice that a solicitation is coming.</li>
<li><b>Solicitation:</b> the actual invitation for bids (IFB) or request for proposals (RFP), with a response deadline.</li></ul>
<h2>7. Still need a state license</h2>
<p>A federal contract does not replace state and local licensing. Many states require a contractor license for work on federal property in the state, and subcontractors in licensed trades still need their licenses.</p>
""",
        "sources": [("SAM.gov", "https://sam.gov/"), ("FAR 28.102-1: performance and payment bonds", "https://www.acquisition.gov/far/28.102-1"),
                    ("SBA: size standards", "https://www.sba.gov/federal-contracting/contracting-guide/size-standards"),
                    ("U.S. Department of Labor: Davis-Bacon and Related Acts", "https://www.dol.gov/agencies/whd/government-contracts/construction")],
    },
    {
        "slug": "contractor-license-vs-registration-vs-permit",
        "title": "Contractor license, registration and permit: what each one means",
        "short": "License vs registration vs permit",
        "desc": "The difference between a state contractor license, a contractor registration, a trade license and a building permit, and how to tell which ones your project needs.",
        "tool": ("/state/", "Check your state’s rules"),
        "body": """
<p>Contractors and homeowners often use “licensed” loosely. In practice there are four different things, issued by different offices, and a job can need several of them at once.</p>
<h2>Contractor license</h2>
<p>A license means a state board has checked your qualifications. Depending on the state, that can include an exam, years of experience, financial statements or net worth, a bond and insurance. California, Florida, Arizona, Nevada and North Carolina are examples of states with licensing boards for general contractors. Licenses often carry limits on the type of work (a classification) or the size of a single project.</p>
<h2>Contractor registration</h2>
<p>Registration means you have told a state agency who you are and met basic requirements, usually insurance and sometimes a bond, but there is no exam. Washington’s L&I registration and Pennsylvania’s home improvement contractor registration with the Attorney General are registrations, not licenses. They exist mainly to protect consumers and to give them a way to complain.</p>
<h2>Trade license</h2>
<p>Electricians, plumbers and HVAC technicians are licensed separately in almost every state, often both as individuals (journeyman, master) and as businesses. A general contractor license usually does not let you do licensed trade work yourself; you hire licensed subcontractors for it.</p>
<h2>Local license and building permit</h2>
<p>Many cities and counties require their own contractor license or registration, especially in states without a statewide general contractor license, such as Illinois and Ohio. Separately, most structural, electrical, plumbing and mechanical work needs a building permit for each project, and the inspector checks the work against the code.</p>
<h2>How to work out what a job needs</h2>
<ol><li>Check the state rule for the type and value of the work. Thresholds range from a few hundred dollars to tens of thousands.</li>
<li>Check whether any trade work is involved and who is licensed for it.</li>
<li>Ask the local building department about city or county registration and permits.</li>
<li>For homeowners: look the contractor up on the state board’s license search and ask for the permit number before work starts.</li></ol>
""",
        "sources": [("ContractorRules state guides (with official board links)", "/state/")],
    },
]


def build(pages, page, intro):
    idx = "/guides/"
    crumbs = [("/", "ContractorRules"), (idx, "Guides")]
    lis = "".join(f'<li><a href="{idx}{g["slug"]}/"><b>{e(g["title"])}</b></a><br>{e(g["desc"])}</li>' for g in GUIDES)
    body = intro("Contractor guides", "Plain-English explainers on federal bidding and contractor licensing.", crumbs)
    body += f'<section><div class="wrap prose"><ul>{lis}</ul></div></section>'
    pages[idx] = page(idx, "Contractor guides: federal bidding and licensing explained | ContractorRules",
                      "Plain-English guides to bidding on federal construction contracts and to contractor licenses, registrations and permits.", body, "guides")
    for g in GUIDES:
        u = f"{idx}{g['slug']}/"
        src = "".join(f'<li><a href="{s}"{"" if s.startswith("/") else " rel=noopener"}>{e(t)}</a></li>' for t, s in g["sources"])
        more = "".join(f'<li><a href="{idx}{x["slug"]}/">{e(x["title"])}</a></li>' for x in GUIDES if x is not g)
        body = intro(g["title"], e(g["desc"]), crumbs + [(u, g["short"])])
        body += f"""<section><div class="wrap prose">{g["body"]}
<p><a class="btn" href="{g["tool"][0]}">{e(g["tool"][1])}</a></p>
<h2>Sources</h2><ul>{src}</ul>
<p class="note">Last reviewed {REVIEWED}. General information, not legal advice.</p>
<h2>More guides</h2><ul>{more}</ul></div></section>"""
        pages[u] = page(u, f"{g['title']} | ContractorRules", g["desc"], body, "guides")
    return GUIDES
