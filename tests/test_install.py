"""Exercise installation against isolated payloads, homes, and projects."""

from pathlib import Path
import os
import shutil
import subprocess
import sys
import tempfile
import unittest


INSTALLER = Path(__file__).resolve().parents[1] / "scripts" / "install.py"


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.source = self.root / "bundle"
        (self.source / "scripts").mkdir(parents=True)
        shutil.copy2(INSTALLER, self.source / "scripts" / "install.py")
        (self.source / "SKILL.md").write_text("---\nname: delphi-plus\ndescription: Delphi writing\n---\n", encoding="utf-8")
        for directory in ("agents", "references", "assets"):
            (self.source / directory).mkdir()
            (self.source / directory / "resource.md").write_text(directory, encoding="utf-8")
        for extra in ("README.md", "original.docx"):
            (self.source / extra).write_text("must stay in repository", encoding="utf-8")
        (self.source / ".git").mkdir()
        (self.source / ".git" / "config").write_text("private metadata", encoding="utf-8")
        self.home = self.root / "home"
        self.home.mkdir()
        self.environment = dict(os.environ, HOME=str(self.home), USERPROFILE=str(self.home), PYTHONUTF8="1")

    def run_installer(self, *arguments):
        return subprocess.run(
            [sys.executable, str(self.source / "scripts" / "install.py"), *arguments],
            capture_output=True, text=True, encoding="utf-8", env=self.environment, check=False,
        )

    def test_user_platform_paths_and_payload_isolation(self):
        roots = {
            "codex": ".agents/skills",
            "antigravity": ".gemini/config/skills",
            "claude-code": ".claude/skills",
        }
        for target, relative_root in roots.items():
            with self.subTest(target=target):
                result = self.run_installer("--target", target)
                self.assertEqual(result.returncode, 0, result.stderr)
                installed = self.home / relative_root / "delphi-plus"
                actual = {str(path.relative_to(installed)) for path in installed.rglob("*") if path.is_file()}
                self.assertEqual(actual, {"SKILL.md", "agents/resource.md", "references/resource.md", "assets/resource.md"})

    def test_existing_destination_is_never_overwritten(self):
        destination = self.home / ".agents" / "skills" / "delphi-plus"
        destination.mkdir(parents=True)
        marker = destination / "SKILL.md"
        marker.write_text("existing version", encoding="utf-8")
        for extra in ((), ("--dry-run",)):
            result = self.run_installer("--target", "codex", *extra)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("already exists", result.stderr)
            self.assertEqual(marker.read_text(encoding="utf-8"), "existing version")
            self.assertEqual(list(destination.iterdir()), [marker])

    def test_project_dry_run_writes_nothing_then_installs(self):
        for target, directory in (("codex", ".agents"), ("antigravity", ".agents"), ("claude-code", ".claude")):
            with self.subTest(target=target):
                project = self.root / (target + " project")
                project.mkdir()
                arguments = ("--target", target, "--scope", "project", "--project", str(project))
                dry = self.run_installer(*arguments, "--dry-run")
                destination = project / directory / "skills" / "delphi-plus"
                self.assertEqual(dry.returncode, 0, dry.stderr)
                self.assertIn(str(destination), dry.stdout)
                self.assertEqual(list(project.iterdir()), [])
                result = self.run_installer(*arguments)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertTrue((destination / "SKILL.md").is_file())

    def test_invalid_project_arguments_fail_without_installing(self):
        cases = [
            ("--scope", "project"),
            ("--scope", "project", "--project", str(self.root / "missing")),
            ("--scope", "project", "--project", str(self.source / "SKILL.md")),
            ("--project", str(self.root)),
        ]
        for arguments in cases:
            with self.subTest(arguments=arguments):
                result = self.run_installer("--target", "codex", *arguments)
                self.assertEqual(result.returncode, 2, result.stderr)
                self.assertFalse((self.home / ".agents").exists())

    def test_installing_into_source_subtree_is_rejected(self):
        result = self.run_installer("--target", "codex", "--scope", "project", "--project", str(self.source))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("inside it", result.stderr)
        self.assertFalse((self.source / ".agents").exists())

    @unittest.skipUnless(hasattr(os, "symlink"), "Symlinks are unavailable")
    def test_payload_symlink_cannot_escape_source(self):
        outside = self.root / "outside.md"
        outside.write_text("private", encoding="utf-8")
        try:
            (self.source / "references" / "escape.md").symlink_to(outside)
        except OSError as exc:
            self.skipTest("Cannot create symlinks: {}".format(exc))
        result = self.run_installer("--target", "codex")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("escapes", result.stderr)
        self.assertFalse((self.home / ".agents").exists())


if __name__ == "__main__":
    unittest.main()
