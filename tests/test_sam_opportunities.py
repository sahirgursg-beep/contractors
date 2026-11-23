import json, sys, tempfile, unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "pipelines"))
import sam_opportunities as o


def notice(i, naics, deadline="2026-12-15T17:00:00-05:00", posted="2026-11-20"):
    return {"noticeId": f"n{i}", "title": f"Notice {i}", "naicsCode": naics, "postedDate": posted, "responseDeadLine": deadline,
            "typeOfSetAsideDescription": "Total Small Business Set-Aside (FAR 19.5)", "uiLink": f"https://sam.gov/opp/n{i}/view",
            "placeOfPerformance": {"state": {"code": "TX"}, "city": {"name": "Austin"}}}


class FakeApi(o.Api):
    def __init__(self, per_day, budget=50, fail_429_after=None):
        super().__init__("k", budget)
        self.per_day, self.fail = per_day, fail_429_after

    def get(self, day, page):
        if self.left <= 0:
            raise o.Budget("budget")
        if self.fail is not None and self.calls >= self.fail:
            raise o.Budget("429")
        self.left -= 1
        self.calls += 1
        items = self.per_day(day)
        return {"totalRecords": len(items), "opportunitiesData": items[page * o.PAGE:(page + 1) * o.PAGE]}


class T(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        o.OUT = Path(self.tmp.name)
        o.BACKFILL_DAYS = 5
        o.PAUSE = 0

    def tearDown(self):
        self.tmp.cleanup()

    def test_keeps_construction_and_paginates(self):
        def per_day(d):
            return [notice(f"{d}-{i}", "238210" if i % 3 == 0 else "541330", posted=d.isoformat()) for i in range(1500)]
        o.run(FakeApi(per_day), today=date(2026, 11, 23))
        n = json.loads((o.OUT / "notices.json").read_text())
        self.assertEqual(len(n), 5 * 500)
        self.assertTrue(all(x["naicsCode"].startswith("23") for x in n))
        self.assertEqual(n[0]["state"], "TX")
        days = (o.OUT / "days.csv").read_text().strip().splitlines()
        self.assertEqual(len(days), 6)
        st = json.loads((o.OUT / "state.json").read_text())
        self.assertNotIn("2026-11-22", st["done"])  # yesterday is fetched again next time
        self.assertIn("2026-11-21", st["done"])

    def test_budget_stops_cleanly_and_resumes(self):
        per_day = lambda d: [notice(f"{d}-1", "236220", posted=d.isoformat())]
        o.run(FakeApi(per_day, budget=2), today=date(2026, 11, 23))
        st = json.loads((o.OUT / "state.json").read_text())
        self.assertEqual(st["done"], ["2026-11-21"])
        o.run(FakeApi(per_day, budget=10), today=date(2026, 11, 23))
        st = json.loads((o.OUT / "state.json").read_text())
        self.assertEqual(len(st["done"]), 4)

    def test_429_keeps_progress(self):
        per_day = lambda d: [notice(f"{d}-1", "237310", posted=d.isoformat())]
        o.run(FakeApi(per_day, fail_429_after=3), today=date(2026, 11, 23))
        self.assertEqual(len(json.loads((o.OUT / "notices.json").read_text())), 3)

    def test_old_deadlines_pruned(self):
        per_day = lambda d: [notice("old", "238160", deadline="2026-10-01T12:00:00Z", posted=d.isoformat()),
                             notice("new", "238160", posted=d.isoformat())]
        o.run(FakeApi(per_day), today=date(2026, 11, 23))
        ids = {x["noticeId"] for x in json.loads((o.OUT / "notices.json").read_text())}
        self.assertEqual(ids, {"nnew"})

    def test_partial_day_refused(self):
        class Short(FakeApi):
            def get(self, day, page):
                r = super().get(day, page)
                r["totalRecords"] = 5000
                return r
        with self.assertRaises(SystemExit):
            o.run(Short(lambda d: [notice(f"{d}-{i}", "238210") for i in range(1200)]), today=date(2026, 11, 23))


if __name__ == "__main__":
    unittest.main()
