"""Regression tests for mode selection before link-plugin indexing."""

from __future__ import annotations

import io
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.parse import unquote

from mkdocs.config import load_config
from mkdocs.structure.files import get_files
from mkdocs.structure.nav import Navigation
from mkdocs.structure.pages import Page


HOOK_PATH = Path(__file__).resolve().parents[1] / "hooks" / "document_modes.py"


class DocumentModesLinkTests(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.root = Path(self.temporary_directory.name)
        self.docs = self.root / "docs"
        self.docs.mkdir()

        # Put a duplicate first so fuzzy lookup cannot accidentally pass.
        self.write("aaa(on-premise)/5.png", b"unrelated image")
        for mode in ("on-premise", "saas"):
            self.write(f"installation({mode})/windows.md", "![Installer](5.png)")
            self.write(f"installation({mode})/5.png", mode.encode())
            self.write(f"installation({mode})/images/diagram.png", mode.encode())
            self.write(f"quick-start/index({mode}).md", f"# {mode}")
        self.write("system-deployment(on-premise)/5.png", b"unrelated image")
        self.write("installation(on-premise)/local-only.md", "# Local only")
        self.write("shared.md", "# Shared")

    def write(self, relative_path, content):
        path = self.docs / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(content, bytes):
            path.write_bytes(content)
        else:
            path.write_text(content, encoding="utf-8")

    def build_files(self, mode):
        configuration = io.StringIO(
            "site_name: Test\n"
            "plugins:\n"
            "  - ezlinks:\n"
            "      reference_links: true\n"
            "hooks:\n"
            f"  - '{HOOK_PATH.as_posix()}'\n"
            "nav:\n"
            "  - Windows: installation/windows.md\n"
            "  - Local: installation/local-only.md\n"
        )
        config = load_config(
            configuration,
            docs_dir=str(self.docs),
            site_dir=str(self.root / "site"),
        )
        with patch.dict(os.environ, {"DOCS_BUILD_MODE": mode}):
            config = config.plugins.on_config(config)
        files = config.plugins.on_files(get_files(config), config=config)
        config.plugins.on_nav(Navigation([], []), config=config, files=files)
        return config, files

    def test_link_plugin_indexes_selected_canonical_paths(self):
        for mode in ("on-premise", "saas"):
            with self.subTest(mode=mode):
                config, files = self.build_files(mode)
                page = Page(None, files.get_file_from_path("installation/windows.md"), config)
                markdown = (
                    "![Installer](5.png)\n"
                    "![Diagram](images/diagram.png)\n"
                    "[Installer][installer]\n\n"
                    "[installer]: 5.png\n"
                )
                rewritten = config.plugins.on_page_markdown(
                    markdown, page=page, config=config, files=files
                )
                normalized = unquote(rewritten).replace("\\", "/")
                self.assertIn("![Installer](5.png)", normalized)
                self.assertIn("![Diagram](images/diagram.png)", normalized)
                self.assertIn("[installer](5.png)", normalized)
                self.assertNotIn("system-deployment", normalized)
                self.assertNotIn("(on-premise)", normalized)
                self.assertNotIn("(saas)", normalized)

                asset = files.get_file_from_path("installation/5.png")
                asset.copy_file()
                self.assertEqual(Path(asset.abs_dest_path).read_bytes(), mode.encode())
                self.assertEqual(
                    files.get_file_from_path("quick-start/index.md").content_string,
                    f"# {mode}",
                )
                self.assertIsNotNone(files.get_file_from_path("shared.md"))
                self.assertFalse(any("(on-premise)" in f.src_uri or "(saas)" in f.src_uri for f in files))

    def test_mode_only_page_is_filtered_from_saas_navigation(self):
        config, files = self.build_files("saas")
        self.assertIsNone(files.get_file_from_path("installation/local-only.md"))
        self.assertEqual(config.nav, [{"Windows": "installation/windows.md"}])


if __name__ == "__main__":
    unittest.main()