#!/usr/bin/env python3
"""SBA table of small business size standards (current), by NAICS code.

Source: SBA open data, dataset "Small Business Size Standards" (data.sba.gov). The newest
"sba-table-of-size-standards_effective-<date>" file is the current table.

Writes data/sba/:
  size-standards.json   every NAICS industry with its receipts ($ millions) or employee standard
  state.json            effective date and source file
Refuses (exit non-zero, writes nothing) if the layout is unexpected or rows go missing.
Needs openpyxl.
"""
import io, json, os, re, sys, urllib.request
from datetime import datetime, timezone
from pathlib import Path

DATASET = "https://data.sba.gov/dataset/small-business-size-standards"
OUT = Path(os.environ.get("SBA_DIR", Path(__file__).resolve().parent.parent / "data" / "sba"))
UA = "ContractorRules data pipeline (+https://contractorrules.com)"
MIN_ROWS = 900
MONTHS = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read()


def current_file(html):
    best = None
    for m in re.finditer(r'(https://data\.sba\.gov/[^"\s]*sba-table-of-size-standards_effective-([a-z]+)-(\d{1,2})-(\d{4})_v(\d+)\.xlsx)', html):
        url, mon, day, year, ver = m.groups()
        if mon not in MONTHS:
            continue
        key = (int(year), MONTHS.index(mon) + 1, int(day), int(ver))
        if not best or key > best[0]:
            best = (key, url)
    if not best:
        raise SystemExit("No 'sba-table-of-size-standards_effective-...' file found on the dataset page.")
    (y, mth, d, _), url = best
    return url, f"{y}-{mth:02d}-{d:02d}"


def num(v):
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return v
    s = str(v).replace("$", "").replace(",", "").strip()
    try:
        return float(s) if "." in s else int(s)
    except ValueError:
        return None


def parse(raw):
    import openpyxl
    wb = openpyxl.load_workbook(io.BytesIO(raw), read_only=True, data_only=True)
    ws = wb.worksheets[0]
    rows = list(ws.iter_rows(values_only=True))
    hdr_i = None
    for i, r in enumerate(rows[:40]):
        cells = [str(c or "").lower() for c in r]
        if any("naics" in c and "code" in c for c in cells) and any("employee" in c for c in cells):
            hdr_i = i
            break
    if hdr_i is None:
        preview = "\n".join(repr(r[:8]) for r in rows[:8])
        raise SystemExit(f"Header row with NAICS code and employees not found. Sheets: {wb.sheetnames}. First rows:\n{preview}")
    hdr = [re.sub(r"\s+", " ", str(c or "")).strip().lower() for c in rows[hdr_i]]

    def col(*words):
        for j, h in enumerate(hdr):
            if all(w in h for w in words):
                return j
        return None
    c_code, c_title = col("naics", "code"), col("description") if col("description") is not None else col("industry")
    c_rec, c_emp = col("millions"), col("employee")
    c_foot = col("footnote")
    if None in (c_code, c_title, c_rec, c_emp):
        raise SystemExit(f"Columns not recognised: {hdr}")
    out = []
    for r in rows[hdr_i + 1:]:
        code = str(r[c_code] or "").strip()
        m = re.match(r"^(\d{6})(?:\s*\(?([a-z0-9 ]+)\)?)?", code, re.I)
        if not m:
            continue
        title = re.sub(r"\s+", " ", str(r[c_title] or "")).strip()
        out.append({"naics": m.group(1), "exception": (m.group(2) or "").strip() or None, "title": title,
                    "receipts_musd": num(r[c_rec]), "employees": num(r[c_emp]),
                    "footnote": (str(r[c_foot]).strip() if c_foot is not None and r[c_foot] not in (None, "") else None)})
    return out


def validate(rows, old):
    if len(rows) < MIN_ROWS:
        raise SystemExit(f"Only {len(rows)} rows; refusing (minimum {MIN_ROWS}).")
    codes = {r["naics"] for r in rows}
    for must in ("236220", "238210", "237310"):
        if must not in codes:
            raise SystemExit(f"Expected NAICS {must} missing.")
    if any(r["receipts_musd"] is None and r["employees"] is None for r in rows if not r["exception"]):
        bad = [r["naics"] for r in rows if r["receipts_musd"] is None and r["employees"] is None][:5]
        raise SystemExit(f"Rows without any size standard, e.g. {bad}.")
    if old and len(rows) < len(old) * 0.9:
        raise SystemExit(f"Rows fell from {len(old)} to {len(rows)}; needs a human check.")


def run(raw, url, effective):
    p = OUT / "size-standards.json"
    old = json.loads(p.read_text()) if p.exists() else None
    rows = parse(raw)
    validate(rows, old)
    OUT.mkdir(parents=True, exist_ok=True)
    if old == rows:
        print("No change.")
        return False
    p.write_text(json.dumps(rows, indent=1) + "\n")
    (OUT / "state.json").write_text(json.dumps({"effective": effective, "source": url, "rows": len(rows),
                                                "updated_at": datetime.now(timezone.utc).isoformat(timespec="seconds")}, indent=1) + "\n")
    c = [r for r in rows if r["naics"].startswith("23")]
    print(f"{len(rows)} rows (construction: {len(c)}), effective {effective}")
    return True


if __name__ == "__main__":
    url, eff = current_file(fetch(DATASET).decode("utf-8", "replace"))
    run(fetch(url), url, eff)
