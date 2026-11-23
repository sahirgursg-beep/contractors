"""State contractor license guides. Every figure is taken from the issuing agency or the statute and
re-checked on CHECKED. Approved by the site owner on 2026-11-23."""

CHECKED = "2026-11-23"

T = lambda head, rows: ('<div class="tablewrap"><table><thead><tr>' + "".join(f"<th{' class=num' if i else ''}>{h}</th>" for i, h in enumerate(head))
                        + "</tr></thead><tbody>" + "".join("<tr>" + "".join(f"<td{' class=num' if i else ''}>{c}</td>" for i, c in enumerate(r)) + "</tr>" for r in rows)
                        + "</tbody></table></div>")

GUIDES = [
    {
        "code": "CA", "slug": "california", "name": "California", "agency": "Contractors State License Board (CSLB)",
        "answer": "Yes. California licenses almost all construction work through the Contractors State License Board (CSLB), for jobs of $1,000 or more and for any job that needs a permit.",
        "facts": [("Licensing agency", "CSLB"), ("License needed from", "$1,000"), ("Contractor bond", "$25,000"), ("Experience", "4 years")],
        "body": """
<h2>When you need a license</h2>
<p>You need a CSLB license when labor and materials on a job add up to $1,000 or more. The limit was $500 until January 1, 2025, when AB 2622 raised it.</p>
<p>The exemption has two conditions. It does not apply if the work needs a building permit, or if you use any employees or helpers on the job. In either case you need a license even when the price is under $1,000. Splitting a larger project into smaller contracts to stay under the limit is not allowed.</p>
<h2>How to get a license</h2>
<ol>
<li><b>Choose a classification.</b> A is general engineering, B is general building, B-2 is residential remodeling, and the C classes cover specialty trades such as C-10 electrical and C-36 plumbing.</li>
<li><b>Name a qualifying individual.</b> Every classification on a license needs one. For a company this is the responsible managing officer or employee.</li>
<li><b>Show experience.</b> The qualifier needs four years of journey-level experience (or higher) within the last ten years.</li>
<li><b>Apply and get fingerprinted.</b> File the application with the $450 fee. Every applicant goes through a Live Scan background check.</li>
<li><b>Pass the exams.</b> The Law and Business exam, the trade exam for your classification, and an open-book asbestos exam.</li>
<li><b>Post the bond and pay the license fee.</b> CSLB sends a bond and fee letter once the exams are passed.</li>
</ol>
<h2>Costs</h2>
{costs}
<p class="note">The initial license fee covers two years.</p>
<h2>Insurance</h2>
<p>Workers' compensation insurance is already required for roofing (C-39), concrete (C-8), HVAC (C-20), asbestos abatement (C-22) and tree service (D-49) contractors, even with no employees.</p>
<p>For every other classification, the rule that all contractors carry workers' compensation was moved from January 1, 2026 to January 1, 2028 by SB 1455. Until then, a contractor with no employees in those classes can still file an exemption. Many guides still give the 2026 date.</p>
<p>A limited liability company also needs liability insurance and an LLC employee/worker bond.</p>
""",
        "costs": [["Application fee", "$450"], ["Initial license fee, sole owner", "$200"], ["Initial license fee, other businesses", "$350"],
                  ["Contractor bond", "$25,000"], ["Bond of qualifying individual, when required", "$25,000"]],
        "links": [("CSLB: before applying for the exam", "https://www.cslb.ca.gov/Contractors/Applicants/Contractors_License/Exam_Application/Before_Applying_For_License.aspx"),
                  ("CSLB: issuing your license (fees and bonds)", "https://web.cslb.ca.gov/contractors/applicants/contractors_license/exam_application/Issuing_My_License.aspx"),
                  ("CSLB bulletin: minor work limit rises to $1,000", "https://www.cslb.ca.gov/Resources/IndustryBulletins/2024/AB%202622%20Implementation.FINAL.pdf"),
                  ("CSLB bulletin: SB 1455 workers' comp changes", "https://www.cslb.ca.gov/Resources/IndustryBulletins/2024/SB%201455%20changes.FINAL.pdf")],
    },
    {
        "code": "TX", "slug": "texas", "name": "Texas", "agency": "No state general contractor license",
        "answer": "Texas has no statewide general contractor license, exam or bond. The state licenses specific trades — electrical, HVAC, plumbing — and cities handle registration and permits.",
        "facts": [("State GC license", "None"), ("Electrical and HVAC", "TDLR"), ("Plumbing", "TSBPE"), ("HVAC Class A insurance", "$300,000")],
        "body": """
<h2>Trades the state licenses</h2>
<p>These trades need a state license no matter how small the job:</p>
<ul>
<li><b>Electrical</b>, licensed by the Texas Department of Licensing and Regulation (TDLR): apprentice, journeyman and master electricians, and electrical contractors.</li>
<li><b>Air conditioning and refrigeration</b>, also licensed by TDLR. See the HVAC section below.</li>
<li><b>Plumbing</b>, licensed by the Texas State Board of Plumbing Examiners (TSBPE): tradesman-limited, journeyman and master plumbers. Master plumbers can contract for plumbing work directly.</li>
<li>TDLR also licenses irrigators and water well drillers.</li>
</ul>
<h2>Trades with no state license</h2>
<p>General contractors, remodelers, roofers, painters and handymen do not need a state license in Texas.</p>
<h2>What a general contractor still needs</h2>
<p>Many cities require contractors to register with the building department before pulling permits, and each city runs its own process. Check with the permit office where the job is. You also need a sales and use tax permit from the Texas Comptroller, and the insurance your clients and the city require.</p>
<h2>HVAC contractor license</h2>
<p>A Class A license covers equipment of any size. A Class B license is limited to systems of up to 25 tons of cooling or 1.5 million BTU per hour of heating. To qualify you need 48 months of practical experience under a licensed contractor within the last 72 months, then pass the exam. The license must be renewed every year, and you must carry commercial general liability insurance while it is active.</p>
{costs}
""",
        "costs": [["Class A: per occurrence (property damage and bodily injury)", "$300,000"], ["Class A: aggregate", "$600,000"],
                  ["Class A: products and completed operations aggregate", "$300,000"]],
        "costs_head": ["HVAC Class A minimum insurance", "Amount"],
        "links": [("TDLR: apply for an air conditioning and refrigeration contractor license", "https://www.tdlr.texas.gov/acr/contractor-apply.htm"),
                  ("Texas State Board of Plumbing Examiners", "https://tsbpe.texas.gov/"),
                  ("16 Tex. Admin. Code § 75.40: contractor insurance requirements", "https://www.law.cornell.edu/regulations/texas/16-Tex-Admin-Code-SS-75-40")],
    },
    {
        "code": "FL", "slug": "florida", "name": "Florida", "agency": "Construction Industry Licensing Board (CILB)",
        "answer": "Yes. Florida licenses contractors through the Construction Industry Licensing Board (CILB), part of the Department of Business and Professional Regulation (DBPR). Only small jobs under $2,500 are exempt.",
        "facts": [("Licensing agency", "CILB / DBPR"), ("Small-job exemption", "under $2,500"), ("Experience", "4 years"), ("Credit score", "660+")],
        "body": """
<h2>When you need a license</h2>
<p>Most construction work in Florida needs a license. The exemption in section 489.103(9) of the Florida Statutes covers only work that is casual, minor or inconsequential and where the total contract price for labor, materials and everything else is under $2,500. Older guides often say $1,000.</p>
<h2>Certified or registered</h2>
<ul>
<li><b>Certified</b> contractors pass the state exam and meet the experience and financial requirements. A certified license is valid anywhere in Florida and renews on August 31 of even-numbered years.</li>
<li><b>Registered</b> contractors hold a local county or city license. A registered license is valid only in that area and renews on August 31 of odd-numbered years.</li>
</ul>
<h2>How to get a certified license</h2>
<ol>
<li><b>Experience.</b> Four years in the license category, including at least one year as a supervisor. Up to three years of college credit or military service can count toward the four years, but not toward the supervisory year. General and building contractors must show experience in four of six listed work areas.</li>
<li><b>Exam.</b> Pass the Florida contractor exam: the trade portion and the business and finance portion. People already certified in another category skip business and finance.</li>
<li><b>Credit.</b> Submit a credit report with a FICO score of 660 or higher. With a lower score you must complete a board-approved 14-hour financial responsibility course. There is no minimum net worth.</li>
<li><b>Insurance.</b> Show the liability coverage below, plus workers' compensation or an exemption, before the license goes active.</li>
</ol>
<h2>Insurance</h2>
{costs}
""",
        "costs": [["General and building contractors", "$300,000", "$50,000"], ["All other categories", "$100,000", "$25,000"]],
        "costs_head": ["Category", "Public liability", "Property damage"],
        "links": [("DBPR: construction industry FAQs", "https://www2.myfloridalicense.com/construction-industry/faqs/"),
                  ("Florida Statutes 489.103: exemptions", "https://www.flsenate.gov/Laws/Statutes/2025/489.103")],
    },
    {
        "code": "NY", "slug": "new-york", "name": "New York", "agency": "Local: NYC DCWP and DOB, counties",
        "answer": "New York State has no general contractor license. Licensing is local, and New York City is the strictest: residential work over $200 needs a Home Improvement Contractor license.",
        "facts": [("State GC license", "None"), ("NYC license needed over", "$200"), ("NYC bond or trust fund", "$20,000 / $200"), ("NYC exam fee", "$50")],
        "body": """
<h2>New York City</h2>
<p>Contractors in the five boroughs may need two separate credentials from two city agencies.</p>
<h3>Home Improvement Contractor license (DCWP)</h3>
<p>The Department of Consumer and Worker Protection (DCWP) issues this license. You need it for construction, repair, remodeling or other home improvement work on residential land or buildings when the job is over $200. That includes work such as patios, porches, sidewalks, swimming pools and terraces.</p>
<p>To apply you need:</p>
<ul>
<li>A passing score on the Home Improvement exam ($50, covering two attempts)</li>
<li>Either enrollment in the DCWP Trust Fund ($200) or a $20,000 surety bond</li>
<li>Fingerprints for the owners and officers</li>
<li>An insurance certificate naming DCWP as certificate holder, and proof of workers' compensation coverage or an exemption</li>
<li>EPA lead-safe (RRP) or lead abatement certification, or a signed affirmation that you will not need it</li>
<li>A New York State sales tax ID</li>
</ul>
{costs}
<h3>General Contractor registration (DOB)</h3>
<p>The Department of Buildings (DOB) registers general contractors who pull permits. You must register to build a new one-, two- or three-family home. Alterations to one- to four-family homes and individual apartments need both the DCWP license and DOB registration.</p>
<h2>Outside New York City</h2>
<p>Nassau, Suffolk, Westchester, Rockland and Putnam counties, and some cities, run their own home improvement licensing. Requirements and fees differ, so check with the county consumer affairs office where the job is.</p>
<h2>State-level requirements</h2>
<p>The New York State Department of Labor licenses asbestos, crane and some other specialty work, and contractors on public works projects must register with it.</p>
""",
        "costs": [["Home Improvement exam (two attempts)", "$50"], ["Trust Fund enrollment, or", "$200"], ["Surety bond instead of the Trust Fund", "$20,000"],
                  ["License fee, prorated by filing date", "$25–$100"], ["Renewal, every two years", "$100"]],
        "costs_head": ["NYC Home Improvement Contractor costs", "Amount"],
        "links": [("NYC DCWP: Home Improvement Contractor license checklist", "https://www.nyc.gov/site/dca/businesses/license-checklist-home-improvement-contractor.page"),
                  ("NYC Business: Home Improvement Contractor license", "https://nyc-business.nyc.gov/nycbusiness/description/home-improvement-contractor-license"),
                  ("NYC DOB: contractors", "https://www.nyc.gov/site/buildings/industry/contractors.page")],
    },
    {
        "code": "AZ", "slug": "arizona", "name": "Arizona", "agency": "Registrar of Contractors (ROC)",
        "answer": "Yes. The Arizona Registrar of Contractors (ROC) licenses commercial, residential and dual contractors statewide. A license is needed for jobs over $1,000 and for any job that needs a permit.",
        "facts": [("Licensing agency", "ROC"), ("License needed over", "$1,000"), ("Residential GC bond", "from $9,000"), ("Recovery fund, new", "$370")],
        "body": """
<h2>When you need a license</h2>
<p>Under Arizona's handyman exemption, you can work without a license only when labor and materials total $1,000 or less and the job does not need a building permit. If a permit is required, you need a license whatever the price. Bills to raise the limit have been filed in recent sessions, but none has become law.</p>
<h2>Commercial, residential or dual</h2>
<ul>
<li><b>Commercial:</b> A (general engineering), B-1 and B-2 (general commercial) and the C specialty classes.</li>
<li><b>Residential:</b> B (general residential), B-3 to B-10 and the R specialty classes.</li>
<li><b>Dual:</b> KA, KB-1, KB-2 and the CR classes, which cover both residential and commercial work.</li>
</ul>
<h2>How to get a license</h2>
<ol>
<li><b>Name a qualifying party.</b> The qualifying party must be regularly employed by the business and have the experience for the classification.</li>
<li><b>Pass the exams.</b> The qualifying party passes the Statutes and Rules exam and the trade exam, unless they qualify for an in-state or out-of-state waiver. For B-1, B-2, KB-1 and KB-2, the NASCLA commercial building exam can replace the ROC trade exam.</li>
<li><b>Background check, ID and bond.</b> Everyone listed on the application submits a background check and ID, and the bond goes in with a bond verification form.</li>
<li><b>Apply and pay.</b> Residential and dual applicants also pay into the Residential Contractors' Recovery Fund.</li>
</ol>
<h2>Fees for a new license</h2>
{costs}
<p class="note">License fees cover two years. Residential and dual renewals carry a $270 recovery fund assessment.</p>
<h2>Bonds</h2>
<p>The bond depends on the license scope and the yearly volume you expect. A residential general contractor expecting less than $750,000 a year posts a $9,000 bond; $750,000 or more posts $15,000. Commercial bonds go up to $50,000 for more than $10 million a year. A dual license adds the residential and commercial amounts together.</p>
<p>Instead of paying the recovery fund assessment, a residential contractor can post a $200,000 bond. The fund can repay a homeowner harmed by a licensed residential contractor up to $30,000.</p>
""",
        "costs": [["General commercial (A, B-1, B-2)", "$200", "$580", "–", "$780"], ["Specialty commercial (C)", "$100", "$480", "–", "$580"],
                  ["General residential (B, B-3 to B-10)", "$180", "$320", "$370", "$870"], ["Specialty residential (R)", "$80", "$270", "$370", "$720"],
                  ["General dual (KA, KB-1, KB-2)", "$200", "$480", "$370", "$1,050"], ["Specialty dual (CR)", "$100", "$380", "$370", "$850"]],
        "costs_head": ["Classification", "Application", "License", "Recovery fund", "Total"],
        "links": [("ROC: license classifications and handyman exemption", "https://azroc.gov/license-classifications"),
                  ("ROC: license and renewal fees", "https://www.azroc.gov/licensing-fees"),
                  ("ROC: bond information", "https://azroc.gov/bond-information")],
    },
]

for g in GUIDES:
    g["body"] = g["body"].replace("{costs}", T(g.get("costs_head", ["Item", "Amount"]), g["costs"]))
