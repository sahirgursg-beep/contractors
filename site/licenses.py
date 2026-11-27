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

GUIDES += [
    {
        "code": "GA", "slug": "georgia", "name": "Georgia", "agency": "State Licensing Board for Residential and General Contractors",
        "answer": "Yes. Georgia licenses residential and general contractors through a state board under the Secretary of State, for residential work over $2,500 and for commercial general contracting.",
        "facts": [("Licensing board", "SLBRGC"), ("Residential license from", "over $2,500"), ("Commercial GC net worth", "$150,000"), ("Residential net worth", "$25,000")],
        "body": """
<h2>When you need a license</h2>
<p>Under Title 43, Chapter 41 of the Georgia Code, residential contracting where the value of the work is more than $2,500 needs a residential contractor license, and general (commercial) contracting needs a general contractor license. Specialty trade contractors such as electricians, plumbers and HVAC contractors are licensed separately and do not need this license when they stay within their trade.</p>
<h2>License types</h2>
<ul>
<li><b>Residential-Basic:</b> detached one- and two-family homes and townhouses.</li>
<li><b>Residential-Light Commercial:</b> everything in Residential-Basic plus multifamily and smaller multi-use commercial buildings.</li>
<li><b>General Contractor:</b> commercial work without a project limit, with a separate limited-tier license for smaller projects.</li>
</ul>
<h2>Requirements</h2>
{costs}
<p>Applicants pass the board's exam for the license type, show qualifying experience and apply through the Secretary of State's online system (GOALS). Residential contractors complete continuing education every year: 3 hours for Residential-Basic and 6 hours for Residential-Light Commercial. Commercial general contractors do not have a continuing education requirement.</p>
<h2>Reciprocity</h2>
<p>Georgia has reciprocity agreements with Louisiana and Mississippi for unlimited commercial general contractors and Residential-Basic contractors.</p>
""",
        "costs": [["Residential-Basic", "$25,000", "$300,000 per occurrence"], ["Residential-Light Commercial", "$25,000", "$500,000 per occurrence"],
                  ["Commercial General Contractor", "$150,000", "Set by board rules"]],
        "costs_head": ["License", "Minimum net worth", "General liability insurance"],
        "links": [("Georgia Secretary of State: residential and general contractors FAQ", "https://sos.ga.gov/page/residential-and-general-contractors-faqs"),
                  ("Licensure comparison chart (PDF)", "https://sos.ga.gov/49-reference-licensure-comparison-chart"),
                  ("Georgia Code Title 43, Chapter 41", "https://law.justia.com/codes/georgia/title-43/chapter-41/")],
    },
    {
        "code": "NC", "slug": "north-carolina", "name": "North Carolina", "agency": "Licensing Board for General Contractors (NCLBGC)",
        "answer": "Yes. North Carolina requires a general contractor license from the NCLBGC for any project costing $40,000 or more. Each license carries a limit on project size tied to the contractor's finances.",
        "facts": [("Licensing board", "NCLBGC"), ("License needed from", "$40,000"), ("Limited license, per project", "up to $750,000"), ("Unlimited license bond option", "$1,000,000")],
        "body": """
<h2>When you need a license</h2>
<p>Under G.S. 87-1, anyone who bids on, builds, superintends or manages the construction of a building, highway, public utility, grading or other improvement where the cost of the undertaking is $40,000 or more is a general contractor and must be licensed. The threshold was raised from $30,000 in 2023. Licensed electrical, plumbing, heating and fire sprinkler contractors working within their own trade are covered by separate rules.</p>
<h2>Limitations: how big a project you can take</h2>
{costs}
<p>Instead of showing working capital or net worth, an applicant can post a surety bond in the amount shown. The intermediate and unlimited working capital must be shown in an audited financial statement or an agreed-upon procedures report from a CPA.</p>
<h2>Classifications: what kind of work</h2>
<p>Separately from the limitation, each license lists one or more classifications, such as building, residential, highway or public utilities. The qualifier passes the exam for each classification.</p>
""",
        "costs": [["Limited", "Up to $750,000", "$17,000 working capital or $80,000 net worth", "$175,000"],
                  ["Intermediate", "Up to $1,500,000", "$75,000 working capital", "$500,000"],
                  ["Unlimited", "No limit", "$150,000 working capital", "$1,000,000"]],
        "costs_head": ["Limitation", "Single project value", "Financial requirement", "Or surety bond"],
        "links": [("N.C. General Statutes 87-1", "https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_87/GS_87-1.html"),
                  ("21 NCAC 12A .0204: license limitations", "https://regulations.justia.com/states/north-carolina/title-21/chapter-12/subchapter-a/section-0200/section-12a-0204"),
                  ("NC Licensing Board for General Contractors", "https://www.nclbgc.org/")],
    },
    {
        "code": "WA", "slug": "washington", "name": "Washington", "agency": "Department of Labor & Industries (L&I)",
        "answer": "Washington does not license general contractors by exam, but every construction contractor must register with the Department of Labor & Industries, post a bond and carry liability insurance.",
        "facts": [("Registering agency", "L&I"), ("General contractor bond", "$30,000"), ("Specialty contractor bond", "$15,000"), ("Liability insurance", "$250,000")],
        "body": """
<h2>Who must register</h2>
<p>All construction contractors in Washington must register with L&I. There is no general contractor exam. Contractors register either as a <b>general contractor</b>, who can do most kinds of construction work and hire subcontractors, or as a <b>specialty contractor</b> in one of 63 specialties such as roofing, painting or HVAC. A specialty contractor can only work in its specialty and cannot hire subcontractors.</p>
<h2>How to register</h2>
<ol>
<li>Register your business with the Department of Revenue and get a UBI number.</li>
<li>Buy a continuous contractor surety bond, or set up an assignment of savings, in the amount below.</li>
<li>Buy general liability insurance with L&I listed as certificate holder.</li>
<li>Submit the Application for Contractor Registration with the fee. The bond and insurance must show your exact business name.</li>
</ol>
<h2>Bond and insurance</h2>
{costs}
<p>Bond amounts rose on July 1, 2024, the first increase since 2001; contractors move to the new amount at their next renewal. L&I can require a larger bond from contractors with court judgments against them.</p>
<p>Electricians, plumbers and some other trades also need a separate trade license or certificate.</p>
""",
        "costs": [["General contractor bond", "$30,000"], ["Specialty contractor bond", "$15,000"],
                  ["General liability insurance", "$250,000 combined, or $200,000 public liability and $50,000 property damage"]],
        "costs_head": ["Requirement", "Amount"],
        "links": [("L&I: contractor registration", "https://lni.wa.gov/licensing-permits/contractors/"),
                  ("L&I news: higher contractor bonds from July 1, 2024", "https://www.lni.wa.gov/news-events/article/24-13/")],
    },
    {
        "code": "NV", "slug": "nevada", "name": "Nevada", "agency": "Nevada State Contractors Board (NSCB)",
        "answer": "Yes. Nevada licenses almost all paid construction work through the State Contractors Board. Only repair or maintenance under $1,000 that needs no permit is exempt, and every license has a monetary limit and a bond set by the Board.",
        "facts": [("Licensing board", "NSCB"), ("License needed from", "$1,000"), ("Bond range", "$1,000–$500,000"), ("Experience", "4 years")],
        "body": """
<h2>When you need a license</h2>
<p>Nevada's contractor law covers nearly all construction for pay. The main exemption, in NRS 624.031, is work to repair or maintain property worth less than $1,000 including labor and materials, and only if no building permit is required and the work is not a licensed trade. The Board does not issue a handyman license.</p>
<h2>How a Nevada license works</h2>
<ul>
<li><b>Classification:</b> A (general engineering), B (general building) or one of the C specialty classifications.</li>
<li><b>Monetary limit:</b> the largest single contract the license allows, set by the Board from the applicant's financial statement. A limit of $10,000 or more requires a financial statement prepared by a CPA.</li>
<li><b>Bond:</b> set by the Board between $1,000 and $500,000 based on the license type, monetary limit, financial responsibility and experience. It can be a surety bond or a cash deposit.</li>
</ul>
<h2>How to get a license</h2>
<ol>
<li>Show at least four years of experience in the classification.</li>
<li>Pass the management exam and any required trade exam (given by PSI).</li>
<li>Submit the financial statement for the monetary limit you request.</li>
<li>File the bond and proof of workers' compensation insurance or an exemption.</li>
</ol>
<p>Residential contractors also pay into the Residential Recovery Fund, based on their monetary limit.</p>
""",
        "costs": [],
        "links": [("NSCB: exemptions (NRS 624.031)", "https://www.nvcontractorsboard.com/licensing/exemptions/"),
                  ("NSCB: bonds", "https://nvcontractorsboard.com/bonds"),
                  ("NSCB license application (PDF)", "https://www.nvcontractorsboard.com/wp-content/uploads/2025/04/License-App.pdf")],
    },
    {
        "code": "IL", "slug": "illinois", "name": "Illinois", "agency": "Local, plus state roofing and plumbing licenses",
        "answer": "Illinois has no statewide general contractor license. The state licenses roofing contractors (IDFPR) and plumbers (IDPH); general contractors are licensed by cities and counties, most strictly in Chicago.",
        "facts": [("State GC license", "None"), ("Roofing", "IDFPR license"), ("Plumbing", "IDPH license"), ("Chicago GC classes", "A to E")],
        "body": """
<h2>State-level licenses</h2>
<ul>
<li><b>Roofing:</b> anyone doing roofing work anywhere in Illinois needs a roofing contractor license from the Illinois Department of Financial and Professional Regulation (IDFPR). The qualifying party passes the state roofing exam, and the license requires a bond and proof of insurance.</li>
<li><b>Plumbing:</b> plumbers and plumbing contractors are licensed by the Illinois Department of Public Health (IDPH).</li>
</ul>
<h2>General contractors: local rules</h2>
<p>General contractors, remodelers and most other trades are licensed, if at all, by the city or county where the work is. Requirements vary widely, so check with the local building department before you bid.</p>
<h2>Chicago</h2>
<p>The City of Chicago requires a general contractor license for most building construction, alteration, repair and demolition work in the city. Licenses come in five classes, A to E, based on the value of the projects you take on, and the required insurance rises with the class. Electrical, plumbing and other trades need their own city licenses.</p>
""",
        "costs": [],
        "links": [("IDFPR: roofing contractor", "https://idfpr.illinois.gov/profs/roof.html"),
                  ("City of Chicago: general contractor license", "https://www.chicago.gov/city/en/depts/bldgs/supp_info/TLdetails/GC.html")],
    },
]

GUIDES += [
    {
        "code": "OH", "slug": "ohio", "name": "Ohio", "agency": "Local governments, plus the Ohio Construction Industry Licensing Board (OCILB) for five trades",
        "answer": "Ohio has no statewide general contractor license. The state licenses five commercial trades through the OCILB; general contractors register with the cities and counties where they work.",
        "facts": [("State GC license", "None"), ("State trade licenses", "OCILB"), ("Trades licensed", "5"), ("GC registration", "Local")],
        "body": """
<h2>What the state licenses</h2>
<p>The Ohio Construction Industry Licensing Board, part of the Ohio Department of Commerce, licenses commercial contractors in five trades: <b>electrical, plumbing, HVAC, hydronics and refrigeration</b>. If your company does any of that work, a qualified person on staff needs the OCILB license for that trade.</p>
<h2>General contractors and remodelers</h2>
<p>For general construction and remodeling outside those trades, Ohio leaves licensing to local governments. Columbus, Cleveland, Cincinnati and many other cities require contractors to register or hold a city license before they pull permits, with their own insurance and bond rules. Check with the building department in each city or county where you plan to work.</p>
<h2>Other state requirements</h2>
<ul><li>Register your business with the Ohio Secretary of State.</li>
<li>Employers must carry workers’ compensation through the Ohio Bureau of Workers’ Compensation, Ohio’s state fund.</li></ul>
""",
        "costs": [],
        "links": [("Ohio Department of Commerce", "https://com.ohio.gov/")],
    },
    {
        "code": "PA", "slug": "pennsylvania", "name": "Pennsylvania", "agency": "Office of Attorney General (home improvement registration)",
        "answer": "Pennsylvania has no state general contractor license, but anyone doing $5,000 or more of home improvement work a year must register with the Attorney General. Cities such as Philadelphia add their own licenses.",
        "facts": [("State GC license", "None"), ("HIC registration from", "$5,000 a year"), ("Liability insurance", "$50,000 / $50,000"), ("Registration valid", "2 years")],
        "body": """
<h2>Home improvement contractor registration</h2>
<p>Under the Home Improvement Consumer Protection Act, contractors who perform home improvements on residential property in Pennsylvania must register with the Office of Attorney General and use their PA HIC number on contracts and advertising. Contractors who do less than $5,000 of home improvement work in a calendar year are exempt.</p>
{costs}
<p>There is no exam. Registrations last two years and must be renewed. A home improvement contract that does not meet the Act’s requirements can be void and unenforceable by the contractor, so the written contract matters as much as the registration.</p>
<h2>Commercial work and local licenses</h2>
<p>The state does not license general contractors for commercial work. Philadelphia, Pittsburgh and other municipalities have their own contractor licenses and permit rules, and trades such as plumbing and electrical are often licensed locally.</p>
""",
        "costs": [["Personal injury liability insurance", "at least $50,000"], ["Property damage insurance", "at least $50,000"]],
        "costs_head": ["Requirement", "Minimum"],
        "links": [("PA Attorney General: home improvement contractor registration", "https://hic.attorneygeneral.gov/"),
                  ("PA Attorney General: contractor FAQ", "https://www.attorneygeneral.gov/?p=6380")],
    },
    {
        "code": "MI", "slug": "michigan", "name": "Michigan", "agency": "Department of Licensing and Regulatory Affairs (LARA)",
        "answer": "Yes, for residential work. Michigan requires a Residential Builder or Maintenance & Alteration Contractor license from LARA for residential jobs of $600 or more. There is no state license for commercial general contracting.",
        "facts": [("Licensing agency", "LARA"), ("Residential license from", "$600"), ("Prelicensure course", "60 hours"), ("Exam", "PSI")],
        "body": """
<h2>Two residential licenses</h2>
<ul><li><b>Residential Builder:</b> new homes and any residential construction, remodeling or repair.</li>
<li><b>Maintenance & Alteration (M&A) Contractor:</b> limited to the specific trades listed on the license, such as roofing, siding, carpentry or basement waterproofing.</li></ul>
<h2>How to get licensed</h2>
<ol><li>Complete 60 hours of approved prelicensure education, with at least 6 hours in each required subject, such as business management and estimating, and design and building science.</li>
<li>Apply to LARA online or on paper.</li>
<li>After LARA approves the application, pass the state exam, which is given by PSI.</li></ol>
<p>Electrical, plumbing and mechanical work need separate trade licenses. Commercial general contracting has no state license, but local permits and codes still apply.</p>
""",
        "costs": [],
        "links": [("LARA: residential builders and M&A contractors", "https://www.michigan.gov/lara/bureau-list/bcc/Sections/Licensing-Section"),
                  ("LARA: prelicensure education requirements", "https://www.michigan.gov/lara/bureau-list/bcc/Sections/Licensing-Section/residential-builders/forms/prelicensure-education-requirements-for-residential-builder-and-maintenance-alteration-contractor-a")],
    },
    {
        "code": "VA", "slug": "virginia", "name": "Virginia", "agency": "Department of Professional and Occupational Regulation (DPOR), Board for Contractors",
        "answer": "Yes. Virginia requires a DPOR contractor license for construction, repair or improvement work over $1,000. The class (A, B or C) depends on the size of your contracts, and the thresholds were raised in 2025.",
        "facts": [("Licensing board", "Board for Contractors"), ("License needed from", "over $1,000"), ("Class A net worth", "$45,000"), ("Class B net worth", "$15,000")],
        "body": """
<h2>License classes</h2>
{costs}
<p>Annual revenue limits also apply to Class B and C licenses; check the current limits with DPOR before you choose a class. Contracts that exceed your class are not allowed, so pick the class for the largest jobs you expect.</p>
<h2>Requirements</h2>
<ul><li>A designated employee or qualified individual with experience in each specialty on the license.</li>
<li>A Board-approved pre-license course, and for Class A and B, passing the exams.</li>
<li>For Class A and B, proof of net worth ($45,000 and $15,000), or a $50,000 surety bond instead.</li></ul>
<p>Each license also lists specialties (for example building, electrical or plumbing) that limit the type of work. Trade workers such as electricians and plumbers need individual tradesman licenses as well.</p>
""",
        "costs": [["Class C", "Over $1,000 and under $30,000"], ["Class B", "$30,000 to under $150,000"], ["Class A", "$150,000 or more"]],
        "costs_head": ["Class", "Single contract or project"],
        "links": [("DPOR: contractor licensing step guide (PDF)", "https://www.dpor.virginia.gov/sites/default/files/boards/Contractors/Contractors_Step_Guide.pdf"),
                  ("Statement of consumer protections (DPOR form)", "https://ris.dls.virginia.gov/uploads/18VAC50/forms/Contractor%20Statement%20of%20Consumer%20Protections-20250609100802.pdf")],
    },
    {
        "code": "TN", "slug": "tennessee", "name": "Tennessee", "agency": "Board for Licensing Contractors (Department of Commerce & Insurance)",
        "answer": "Yes. Tennessee requires a contractor’s license for projects of $25,000 or more, and a Home Improvement license for residential remodeling from $3,000 to $24,999 in nine counties.",
        "facts": [("Licensing board", "Board for Licensing Contractors"), ("Contractor license from", "$25,000"), ("Home improvement license", "$3,000–$24,999"), ("HI counties", "9")],
        "body": """
<h2>Contractor’s license ($25,000 and up)</h2>
<p>Any project where the total cost is $25,000 or more needs a contractor’s license from the Board for Licensing Contractors, in every county. Licensing includes a trade exam and a business and law exam, a financial statement that sets your monetary limit, and proof of insurance. From July 1, 2026, the Board’s exams are given by Prov.</p>
<h2>Home Improvement license ($3,000 to $24,999)</h2>
<p>Residential remodeling where the total cost, labor and materials included, is from $3,000 to less than $25,000 needs a Home Improvement license in the counties that adopted the law: Bradley, Davidson, Hamilton, Haywood, Knox, Marion, Robertson, Rutherford and Shelby.</p>
{costs}
<p>The Home Improvement license does not cover electrical, gas, mechanical, HVAC or plumbing work, which have their own licenses, including limited licenses for electrical and plumbing jobs under $25,000.</p>
""",
        "costs": [["Exam", "None"], ["Application fee", "$250 for a two-year license"]],
        "costs_head": ["Home Improvement license", "Detail"],
        "links": [("Tennessee Board for Licensing Contractors", "https://www.tn.gov/commerce/regboards/contractor"),
                  ("Home Improvement license requirements", "https://www.tn.gov/commerce/regboards/hi/application-requirements-process.html")],
    },
]

for g in GUIDES:
    g["body"] = g["body"].replace("{costs}", T(g.get("costs_head", ["Item", "Amount"]), g["costs"]) if g["costs"] else "")
