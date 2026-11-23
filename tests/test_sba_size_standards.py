import io, json, sys, tempfile, unittest
from pathlib import Path

import openpyxl

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "pipelines"))
import sba_size_standards as s


def xlsx(rows):
    wb = openpyxl.Workbook()
    wb.active.title = "overview"
    wb.active.append(["U. S. Small Business Administration"])
    ws = wb.create_sheet("table_of_size_standards-all")
    ws.append(["SBA Table of Size Standards"])
    ws.append([])
    ws.append(["NAICS Codes", "NAICS Industry Description", "Size Standards in millions of dollars", "Size standards in number of employees", "Footnotes"])
    for r in rows:
        ws.append(list(r))
    b = io.BytesIO()
    wb.save(b)
    return b.getvalue()


def base(n=950):
    rows = [(f"{100000 + i}", f"Industry {i}", 10.0, None, None) for i in range(n)]
    rows += [("236220", "Commercial and Institutional Building Construction", 45.0, None, None),
             ("238210", "Electrical Contractors and Other Wiring Installation Contractors", 19.0, None, None),
             ("237310", "Highway, Street, and Bridge Construction", 45.0, None, None),
             ("212114", "Surface Coal Mining", None, 1300, None)]
    return rows


class T(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        s.OUT = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_parse_and_write(self):
        self.assertTrue(s.run(xlsx(base()), "u", "2023-03-17"))
        d = json.loads((s.OUT / "size-standards.json").read_text())
        r = next(x for x in d if x["naics"] == "236220")
        self.assertEqual(r["receipts_musd"], 45.0)
        self.assertEqual(next(x for x in d if x["naics"] == "212114")["employees"], 1300)
        self.assertEqual(json.loads((s.OUT / "state.json").read_text())["effective"], "2023-03-17")
        self.assertFalse(s.run(xlsx(base()), "u", "2023-03-17"))

    def test_missing_key_code_refused(self):
        rows = [r for r in base() if r[0] != "236220"]
        with self.assertRaises(SystemExit):
            s.run(xlsx(rows), "u", "x")

    def test_too_few_rows_refused(self):
        with self.assertRaises(SystemExit):
            s.run(xlsx(base(10)), "u", "x")

    def test_current_file_picks_latest(self):
        html = ('<a href="https://data.sba.gov/x/sba-table-of-size-standards_effective-december-19-2022_v0.xlsx">'
                '<a href="https://data.sba.gov/x/sba-table-of-size-standards_effective-march-17-2023_v0.xlsx">'
                '<a href="https://data.sba.gov/x/sba-table-of-size-standards_effective-august-19-2019_v0.xlsx">')
        url, eff = s.current_file(html)
        self.assertEqual(eff, "2023-03-17")
        self.assertIn("march-17-2023", url)


if __name__ == "__main__":
    unittest.main()
