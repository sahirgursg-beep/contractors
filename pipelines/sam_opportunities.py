#!/usr/bin/env python3
"""Federal construction contract opportunities from the official SAM.gov Opportunities API (public data).

Each run pulls whole posting days (about 1,000 notices a day across all industries; the API cannot filter
by NAICS prefix) and keeps notices whose NAICS code starts with 23. New days are fetched first; spare
requests fill older days backwards until BACKFILL_DAYS is covered. A request budget per run keeps us well
inside the personal API key's daily limit; on HTTP 429 the run stops and keeps what it has.

Writes data/opportunities/:
  notices.json   construction notices that are still useful (deadline not long past), newest first
  days.csv       one row per fetched posting day: all notices, construction notices
  state.json     which days are done
Needs SAM_API_KEY in the environment. Never prints it.
"""
import csv, json, os, sys, time, urllib.error, urllib.parse, urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

API = "https://api.sam.gov/opportunities/v2/search"
OUT = Path(os.environ.get("OPP_DIR", Path(__file__).resolve().parent.parent / "data" / "opportunities"))
BUDGET = int(os.environ.get("SAM_CALL_BUDGET", "8"))
BACKFILL_DAYS = int(os.environ.get("BACKFILL_DAYS", "45"))
PAGE = 1000
PAUSE = float(os.environ.get("SAM_PAUSE", "1"))
KEEP_AFTER_DEADLINE = 14  # days a notice stays listed after its response deadline
KEEP = ["noticeId", "title", "solicitationNumber", "fullParentPathName", "postedDate", "type", "baseType",
        "typeOfSetAside", "typeOfSetAsideDescription", "responseDeadLine", "naicsCode", "classificationCode",
        "active", "archiveDate", "uiLink"]


class Budget(Exception):
    pass


class Api:
    def __init__(self, key, budget):
        self.key, self.left, self.calls = key, budget, 0

    def get(self, day, page):
        """page is the page index: SAM.gov's 'offset' parameter counts pages, not records."""
        if self.left <= 0:
            raise Budget("request budget used up")
        q = {"api_key": self.key, "postedFrom": day.strftime("%m/%d/%Y"), "postedTo": day.strftime("%m/%d/%Y"),
             "limit": PAGE, "offset": page}
        req = urllib.request.Request(API + "?" + urllib.parse.urlencode(q), headers={"Accept": "application/json"})
        self.left -= 1
        self.calls += 1
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code == 429:
                raise Budget("SAM.gov rate limit reached (HTTP 429)")
            raise SystemExit(f"SAM.gov returned HTTP {e.code} for {day}.")


def slim(n):
    out = {k: n.get(k) for k in KEEP}
    pop = n.get("placeOfPerformance") or {}
    out["state"] = ((pop.get("state") or {}).get("code") or None)
    out["city"] = ((pop.get("city") or {}).get("name") or None)
    off = n.get("officeAddress") or {}
    if not out["state"]:
        out["office_state"] = off.get("state")
    return out


def fetch_day(api, day):
    """Return (all_count, construction notices) for one posting day, or raise Budget."""
    first = api.get(day, 0)
    total = int(first.get("totalRecords") or 0)
    items = list(first.get("opportunitiesData") or [])
    page = 1
    while len(items) < total and page * PAGE < total + PAGE:
        items += list(api.get(day, page).get("opportunitiesData") or [])
        page += 1
    if total and len(items) < total * 0.98:
        raise SystemExit(f"{day}: got {len(items)} of {total} notices; refusing a partial day.")
    con = [slim(n) for n in items if str(n.get("naicsCode") or "").startswith("23")]
    return total, con


def deadline(n):
    d = n.get("responseDeadLine")
    if not d:
        return None
    try:
        return datetime.fromisoformat(d.replace("Z", "+00:00")).date()
    except ValueError:
        return None


def load():
    p = OUT / "notices.json"
    notices = {n["noticeId"]: n for n in json.loads(p.read_text())} if p.exists() else {}
    s = OUT / "state.json"
    state = json.loads(s.read_text()) if s.exists() else {"done": []}
    days = list(csv.DictReader((OUT / "days.csv").open())) if (OUT / "days.csv").exists() else []
    return notices, state, days


def save(notices, state, days, today):
    OUT.mkdir(parents=True, exist_ok=True)
    cutoff = today - timedelta(days=KEEP_AFTER_DEADLINE)
    keep = []
    for n in notices.values():
        dl = deadline(n)
        posted = (n.get("postedDate") or "")[:10]
        if dl and dl < cutoff:
            continue
        if not dl and posted and posted < (today - timedelta(days=60)).isoformat():
            continue
        keep.append(n)
    keep.sort(key=lambda n: (n.get("postedDate") or "", n["noticeId"]), reverse=True)
    (OUT / "notices.json").write_text(json.dumps(keep, ensure_ascii=False, indent=0) + "\n", encoding="utf-8")
    days.sort(key=lambda r: r["day"])
    with (OUT / "days.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["day", "all_notices", "construction"])
        w.writeheader()
        w.writerows(days)
    state["done"] = sorted(set(state["done"]))[-400:]
    state["updated_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    state["listed"] = len(keep)
    (OUT / "state.json").write_text(json.dumps(state, indent=1) + "\n")
    return keep


def plan(state, today):
    """Days to fetch, newest first: recent days not done (re-fetch yesterday once more), then backfill."""
    done = set(state["done"])
    want = []
    for i in range(1, BACKFILL_DAYS + 1):
        d = today - timedelta(days=i)
        if d.isoformat() not in done:
            want.append(d)
    return want


def run(api, today=None):
    today = today or date.today()
    notices, state, days = load()
    by_day = {r["day"]: r for r in days}
    fetched = []
    try:
        for d in plan(state, today):
            total, con = fetch_day(api, d)
            for n in con:
                notices[n["noticeId"]] = n
            by_day[d.isoformat()] = {"day": d.isoformat(), "all_notices": total, "construction": len(con)}
            # Yesterday's list can still grow during the day; only mark days older than that as done.
            if d < today - timedelta(days=1):
                state["done"].append(d.isoformat())
            fetched.append((d.isoformat(), total, len(con)))
            time.sleep(PAUSE)
    except Budget as b:
        print(f"Stopped: {b}.")
    keep = save(notices, state, list(by_day.values()), today)
    print(f"API calls: {api.calls}. Days fetched: {fetched}. Construction notices listed: {len(keep)}.")
    return fetched


if __name__ == "__main__":
    key = os.environ.get("SAM_API_KEY")
    if not key:
        raise SystemExit("SAM_API_KEY is not set.")
    run(Api(key, BUDGET))
