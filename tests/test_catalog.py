"""Exercise maintenance commands as a contributor would use them."""

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
ENTRY = {
    "id": "sample", "title": "A | B", "year": 2026, "venue": "arXiv",
    "category": "afd", "status": "boundary", "arxiv": "2601.12345",
    "source": "https://arxiv.org/abs/2601.12345", "code": None,
    "tags": ["AFD", "MoE"], "why_it_matters": "Studies transfer costs.",
    "limitation": "Measured on one topology.", "verified": "2026-10-13",
    "artifact_type": "paper",
}


class CatalogCommands(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copytree(ROOT / "scripts", self.root / "scripts")
        (self.root / "docs").mkdir()
        (self.root / "data").mkdir()

    def write(self, entries):
        lines = []
        for entry in entries:
            for index, (key, value) in enumerate(entry.items()):
                lines.append(f"{'- ' if index == 0 else '  '}{key}: {json.dumps(value)}")
        (self.root / "papers.yaml").write_text("\n".join(lines) + "\n")

    def run_script(self, name, *args):
        return subprocess.run(
            [sys.executable, str(self.root / "scripts" / name), *args],
            capture_output=True, text=True, cwd=self.root,
        )

    def test_valid_entry(self):
        self.write([ENTRY])
        self.assertEqual(self.run_script("validate_papers.py").returncode, 0)

    def test_rejects_invalid_values(self):
        bad = {
            "year": "next year", "category": "typo", "status": "accepted",
            "arxiv": "https://arxiv.org/abs/2601.12345", "code": "javascript:alert(1)",
            "source": None, "verified": "2026-02-31", "tags": [""],
            "title": "", "artifact_type": "production",
        }
        for key, value in bad.items():
            with self.subTest(field=key):
                self.write([{**ENTRY, key: value}])
                result = self.run_script("validate_papers.py")
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(key, result.stdout + result.stderr)

    def test_rejects_duplicate_ids(self):
        self.write([ENTRY, ENTRY])
        self.assertNotEqual(self.run_script("validate_papers.py").returncode, 0)

    def test_rejects_duplicate_arxiv(self):
        self.write([ENTRY, {**ENTRY, "id": "different"}])
        result = self.run_script("validate_papers.py")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("arxiv", result.stdout + result.stderr)

    def test_rejects_duplicate_keys(self):
        self.write([ENTRY])
        with (self.root / "papers.yaml").open("a") as stream:
            stream.write('  title: "Overwritten silently"\n')
        self.assertNotEqual(self.run_script("validate_papers.py").returncode, 0)

    def test_rejects_unknown_keys(self):
        self.write([{**ENTRY, "soruce": "https://example.org"}])
        result = self.run_script("validate_papers.py")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("soruce", result.stdout + result.stderr)

    def test_empty_catalog_is_invalid(self):
        (self.root / "papers.yaml").write_text("# no records\n")
        self.assertNotEqual(self.run_script("validate_papers.py").returncode, 0)

    def test_bad_yaml_is_reported(self):
        (self.root / "papers.yaml").write_text('- id: sample\n  tags: ["AFD",\n')
        result = self.run_script("validate_papers.py")
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("Traceback", result.stderr)

    def test_unsupported_yaml_scalars_are_rejected(self):
        for raw in ("|", "'Single quoted'", "*missing_anchor", "plain string"):
            with self.subTest(value=raw):
                self.write([ENTRY])
                path = self.root / "papers.yaml"
                path.write_text(path.read_text().replace('title: "A | B"', f"title: {raw}"))
                result = self.run_script("validate_papers.py")
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("Line 2", result.stderr)

    def test_invalid_url_ports_are_rejected(self):
        for port in ("bogus", "99999"):
            with self.subTest(port=port):
                self.write([{**ENTRY, "source": f"https://example.org:{port}/paper"}])
                self.assertNotEqual(self.run_script("validate_papers.py").returncode, 0)

    def test_markdown_destinations_are_encoded(self):
        self.write([{**ENTRY, "source": "https://example.org/a|b)extra", "code": "https://github.com/org/repo)extra"}])
        result = self.run_script("generate_tables.py")
        self.assertEqual(result.returncode, 0)
        self.assertIn("https://example.org/a%7Cb%29extra", result.stdout)
        self.assertIn("https://github.com/org/repo%29extra", result.stdout)

    def test_source_link_for_paper_without_arxiv(self):
        self.write([{**ENTRY, "arxiv": None, "source": "https://example.org/paper"}])
        result = self.run_script("generate_tables.py")
        self.assertEqual(result.returncode, 0)
        self.assertIn("https://example.org/paper", result.stdout)

    def test_generator_escapes_table_cells_and_includes_limitations(self):
        self.write([{**ENTRY, "code": "https://github.com/example/project"}])
        result = self.run_script("generate_tables.py")
        self.assertEqual(result.returncode, 0)
        self.assertIn("A &#124; B", result.stdout)
        self.assertIn("Measured on one topology.", result.stdout)
        self.assertIn("https://github.com/example/project", result.stdout)

    def test_write_and_check_generated_files(self):
        self.write([ENTRY])
        result = self.run_script("generate_tables.py", "--write")
        self.assertEqual(result.returncode, 0)
        self.assertTrue((self.root / "docs" / "catalog.md").is_file())
        exported = self.root / "data" / "papers.json"
        self.assertTrue(exported.is_file())
        self.assertIsInstance(json.loads(exported.read_text())[0]["year"], int)
        self.assertEqual(self.run_script("generate_tables.py", "--check").returncode, 0)
        exported.write_text("[]\n")
        self.assertNotEqual(self.run_script("generate_tables.py", "--check").returncode, 0)

    def test_check_does_not_write_missing_files(self):
        self.write([ENTRY])
        self.assertNotEqual(self.run_script("generate_tables.py", "--check").returncode, 0)
        self.assertFalse((self.root / "docs" / "catalog.md").exists())

    def test_search_combines_filters(self):
        self.write([
            {**ENTRY, "code": "https://github.com/example/project"},
            {**ENTRY, "id": "older", "arxiv": "2501.12345", "year": 2025},
        ])
        result = self.run_script("search_papers.py", "--tag", "afd", "--year", "2026", "--code", "--json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual([r["id"] for r in json.loads(result.stdout)], ["sample"])

    def test_search_matches_summary_and_category(self):
        self.write([ENTRY])
        result = self.run_script("search_papers.py", "transfer", "--category", "afd", "--json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(json.loads(result.stdout)), 1)

    def test_search_empty_result_is_json_list(self):
        self.write([ENTRY])
        result = self.run_script("search_papers.py", "nonexistent", "--json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), [])

    def test_search_rejects_unknown_category(self):
        self.write([ENTRY])
        self.assertNotEqual(self.run_script("search_papers.py", "--category", "typo").returncode, 0)

    def test_search_finds_historical_alias(self):
        self.write([{**ENTRY, "aliases": ["FormerName"]}])
        result = self.run_script("search_papers.py", "formername", "--json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual([r["id"] for r in json.loads(result.stdout)], ["sample"])

    def test_rejects_malformed_alias_and_related_sources(self):
        for key, value in (("aliases", "FormerName"), ("related_sources", ["not-a-url"]), ("operator_subtype", "typo")):
            self.write([{**ENTRY, key: value}])
            result = self.run_script("validate_papers.py")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn(key, result.stderr)

    def write_discovery(self):
        row = {**ENTRY, "id": "survey-other", "title": "Discovered workload",
               "arxiv": "2602.12345", "source": "https://arxiv.org/abs/2602.12345",
               "class": "O", "subtype": "O2", "source_check": "metadata-verified",
               "main_id": None, "survey_key": "other2026", "checked": "2026-10-13"}
        (self.root / "data" / "discovery.json").write_text(json.dumps([row]))
        return row

    def test_search_discovery_and_combined_deduplication(self):
        self.write([ENTRY])
        row = self.write_discovery()
        result = self.run_script("search_papers.py", "--collection", "all", "--json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(json.loads(result.stdout)), 2)
        row["main_id"] = "sample"
        (self.root / "data" / "discovery.json").write_text(json.dumps([row]))
        result = self.run_script("search_papers.py", "--collection", "all", "--json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual([r["id"] for r in json.loads(result.stdout)], ["sample"])

    def test_discovery_class_filter(self):
        self.write([ENTRY])
        self.write_discovery()
        result = self.run_script("search_papers.py", "--collection", "discovery", "--class", "O", "--json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(json.loads(result.stdout)), 1)
        result = self.run_script("search_papers.py", "--collection", "discovery", "--class", "P", "--json")
        self.assertEqual(json.loads(result.stdout), [])

    def test_discovery_generation_and_freshness(self):
        self.write([ENTRY])
        self.write_discovery()
        result = self.run_script("generate_discovery.py", "--write")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.root / "docs" / "discovery" / "operator.md").is_file())
        self.assertEqual(self.run_script("generate_discovery.py", "--check").returncode, 0)
        (self.root / "docs" / "discovery" / "operator.md").write_text("stale")
        self.assertNotEqual(self.run_script("generate_discovery.py", "--check").returncode, 0)

    def test_discovery_dangling_main_id_fails(self):
        self.write([ENTRY])
        row = self.write_discovery()
        row["main_id"] = "missing"
        (self.root / "data" / "discovery.json").write_text(json.dumps([row]))
        result = self.run_script("generate_discovery.py", "--write")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("main_id", result.stderr)

    def test_discovery_duplicate_ids_and_bad_status_fail(self):
        self.write([ENTRY])
        row = self.write_discovery()
        for entries in ([row, row], [{**row, "source_check": "verified-everything"}]):
            (self.root / "data" / "discovery.json").write_text(json.dumps(entries))
            self.assertNotEqual(self.run_script("generate_discovery.py", "--write").returncode, 0)

    def test_combined_search_matches_mapped_discovery_alias(self):
        self.write([ENTRY])
        row = self.write_discovery()
        row.update(main_id="sample", aliases=["HistoricalAlias"], tags=["legacy-tag"])
        (self.root / "data" / "discovery.json").write_text(json.dumps([row]))
        result = self.run_script("search_papers.py", "HistoricalAlias", "--collection", "all", "--tag", "legacy-tag", "--json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual([r["id"] for r in json.loads(result.stdout)], ["sample"])

    def test_discovery_bad_category_reports_without_traceback(self):
        self.write([ENTRY])
        row = self.write_discovery()
        row["category"] = []
        (self.root / "data" / "discovery.json").write_text(json.dumps([row]))
        result = self.run_script("generate_discovery.py", "--write")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("category", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_discovery_rejects_duplicate_json_keys(self):
        self.write([ENTRY])
        row = self.write_discovery()
        path = self.root / "data" / "discovery.json"
        path.write_text(json.dumps([row]).replace('"source_check": "metadata-verified"', '"source_check": "reference-only", "source_check": "metadata-verified"'))
        result = self.run_script("generate_discovery.py", "--write")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("duplicate", result.stderr.lower())

    def test_discovery_text_shows_source_check(self):
        self.write([ENTRY])
        row = self.write_discovery()
        row.update(source_check="reference-only", checked=None)
        (self.root / "data" / "discovery.json").write_text(json.dumps([row]))
        result = self.run_script("search_papers.py", "--collection", "discovery")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("reference-only", result.stdout)
        self.assertIn("O/O2", result.stdout)

    def test_discovery_rejects_bad_identifiers_and_metadata_url(self):
        self.write([ENTRY])
        row = self.write_discovery()
        for key, value in (("arxiv", "garbage"), ("metadata_source", "javascript:alert(1)")):
            with self.subTest(key=key):
                (self.root / "data" / "discovery.json").write_text(json.dumps([{**row, key: value}]))
                result = self.run_script("generate_discovery.py", "--write")
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(key, result.stderr)

    def test_discovery_id_cannot_collide_with_curated_id(self):
        self.write([ENTRY])
        row = self.write_discovery()
        row.update(id="sample", main_id=None)
        (self.root / "data" / "discovery.json").write_text(json.dumps([row]))
        result = self.run_script("generate_discovery.py", "--write")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("id", result.stderr)


if __name__ == "__main__":
    unittest.main()
