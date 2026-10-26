import tempfile
import unittest
from pathlib import Path

from scripts.validate_repository import validate_repository


class RepositoryValidationTests(unittest.TestCase):
    def write_fixture(self, root: Path, *, module_type="foundational", link="README.md"):
        (root / "modules").mkdir(parents=True, exist_ok=True)
        (root / "README.md").write_text("# Test\n", encoding="utf-8")
        (root / "modules" / "example.md").write_text(
            "---\n"
            'name: "Example"\n'
            f'type: "{module_type}"\n'
            'version: "0.1"\n'
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

    def test_invalid_metadata_type_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_fixture(root, module_type="mystery")
            errors = validate_repository(root)
            self.assertTrue(any("unsupported type" in error for error in errors), errors)

    def test_broken_local_link_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_fixture(root, link="missing.md")
            errors = validate_repository(root)
            self.assertTrue(any("broken local link" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
