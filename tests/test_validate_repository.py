import tempfile
import unittest
from pathlib import Path

from scripts.validate_repository import validate_repository


class RepositoryValidationTests(unittest.TestCase):
    def write_fixture(self, root: Path, *, module_type="foundational", link="target-v0.1.0.md"):
        module_dir = root / "modules"
        module_dir.mkdir(parents=True, exist_ok=True)
        (root / "README.md").write_text("# Test\n", encoding="utf-8")
        (module_dir / "target-v0.1.0.md").write_text(
            "---\n"
            'name: "Target"\n'
            'type: "specialized"\n'
            'version: "0.1.0"\n'
            'purpose: "A test target."\n'
            'use_when: "When testing links."\n'
            "---\n\n# Target\n",
            encoding="utf-8",
        )
        (module_dir / "example-v0.1.0.md").write_text(
            "---\n"
            'name: "Example"\n'
            f'type: "{module_type}"\n'
            'version: "0.1.0"\n'
            'purpose: "A test module."\n'
            'use_when: "When testing."\n'
            "---\n\n"
            f"[Entry]({link})\n",
            encoding="utf-8",
        )

    def test_valid_repository_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_fixture(root)
            self.assertEqual(validate_repository(root), [])

    def test_stable_document_filename_is_allowed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_fixture(root, link="target.md")
            (root / "modules" / "target-v0.1.0.md").rename(root / "modules" / "target.md")
            (root / "modules" / "example-v0.1.0.md").rename(root / "modules" / "example.md")
            self.assertEqual(validate_repository(root), [])

    def test_invalid_metadata_type_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_fixture(root, module_type="mystery")
            errors = validate_repository(root)
            self.assertTrue(any("unsupported type" in error for error in errors), errors)

    def test_non_semver_version_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_fixture(root)
            example = root / "modules" / "example-v0.1.0.md"
            example.write_text(example.read_text(encoding="utf-8").replace('version: "0.1.0"', 'version: "0.1"'), encoding="utf-8")
            errors = validate_repository(root)
            self.assertTrue(any("MAJOR.MINOR.PATCH SemVer" in error for error in errors), errors)

    def test_filename_and_front_matter_versions_must_match(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_fixture(root)
            example = root / "modules" / "example-v0.1.0.md"
            renamed = root / "modules" / "example-v0.2.0.md"
            example.rename(renamed)
            errors = validate_repository(root)
            self.assertTrue(any("filename version" in error for error in errors), errors)

    def test_broken_local_link_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_fixture(root, link="missing-v0.1.0.md")
            errors = validate_repository(root)
            self.assertTrue(any("broken local link" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
