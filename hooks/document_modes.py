"""Select mode-specific Markdown variants for MkDocs builds."""

from __future__ import annotations

import logging
import os
import re
from collections import defaultdict
from typing import Any

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.exceptions import PluginError
from mkdocs.structure.files import File, Files

_LOG = logging.getLogger("mkdocs.hooks.document_modes")

_DEFAULT_MODE = "on-premise"
_ENVIRONMENT_VARIABLE = "DOCS_BUILD_MODE"
_MODES = ("on-premise", "saas")
_FILE_VARIANT_PATTERN = re.compile(
    r"^(?P<stem>.+)\((?P<mode>on-premise|saas)\)\.md$",
    re.IGNORECASE,
)
_FOLDER_VARIANT_PATTERN = re.compile(
    r"^(?P<name>.+)\((?P<mode>on-premise|saas)\)$",
    re.IGNORECASE,
)
_DROP_NAV_ITEM = object()

_active_mode = _DEFAULT_MODE


def on_config(config: MkDocsConfig) -> MkDocsConfig:
    """Select and validate the documentation build mode."""

    global _active_mode

    _active_mode = os.getenv(
        _ENVIRONMENT_VARIABLE,
        _DEFAULT_MODE,
    ).strip().lower()

    if _active_mode not in _MODES:
        modes = ", ".join(_MODES)
        raise PluginError(
            f"Unknown documentation mode '{_active_mode}'. "
            f"Set {_ENVIRONMENT_VARIABLE} to one of: {modes}"
        )

    config.extra["document_mode"] = _active_mode
    _LOG.info("Using documentation mode '%s'", _active_mode)
    return config


def on_files(files: Files, *, config: MkDocsConfig) -> Files:
    """Map selected file and folder variants to their canonical paths."""

    variants: dict[str, dict[str, File]] = defaultdict(dict)

    for file in list(files):
        variant = _resolve_variant(file.src_uri)
        if variant is None:
            continue

        canonical_uri, mode = variant
        if mode in variants[canonical_uri]:
            other = variants[canonical_uri][mode]
            raise PluginError(
                f"Mode-specific documents '{other.src_uri}' and "
                f"'{file.src_uri}' both map to '{canonical_uri}' in mode '{mode}'"
            )
        variants[canonical_uri][mode] = file

    unavailable_pages: set[str] = set()

    for canonical_uri, mode_files in sorted(variants.items()):
        if files.get_file_from_path(canonical_uri) is not None:
            sources = ", ".join(file.src_uri for file in mode_files.values())
            raise PluginError(
                f"Mode-specific document '{sources}' conflicts with "
                f"canonical document '{canonical_uri}'"
            )

        # Neither suffixed source file should be copied or compiled directly.
        for variant_file in mode_files.values():
            files.remove(variant_file)

        selected_file = mode_files.get(_active_mode)
        if selected_file is None:
            if canonical_uri.lower().endswith(".md"):
                unavailable_pages.add(canonical_uri)
            _LOG.info(
                "File '%s' is unavailable in mode '%s'",
                canonical_uri,
                _active_mode,
            )
            continue

        canonical_file = File.generated(
            config,
            canonical_uri,
            abs_src_path=selected_file.abs_src_path,
            inclusion=selected_file.inclusion,
        )
        files.append(canonical_file)
        _LOG.debug(
            "Mapped '%s' to '%s'",
            selected_file.src_uri,
            canonical_uri,
        )

    if config.nav is not None and unavailable_pages:
        filtered_nav = _filter_nav(config.nav, unavailable_pages)
        config.nav = [] if filtered_nav is _DROP_NAV_ITEM else filtered_nav

    _LOG.info(
        "Resolved %d mode-specific document(s) for '%s'",
        len(variants),
        _active_mode,
    )
    return files


def _resolve_variant(source_uri: str) -> tuple[str, str] | None:
    """Return the canonical URI and mode encoded in a file or folder name."""

    source_parts = source_uri.replace("\\", "/").split("/")
    canonical_parts: list[str] = []
    modes: set[str] = set()

    for index, part in enumerate(source_parts):
        is_filename = index == len(source_parts) - 1
        match = (
            _FILE_VARIANT_PATTERN.fullmatch(part)
            if is_filename
            else _FOLDER_VARIANT_PATTERN.fullmatch(part)
        )

        if match is None:
            canonical_parts.append(part)
            continue

        mode = match.group("mode").lower()
        modes.add(mode)
        canonical_parts.append(
            f"{match.group('stem')}.md"
            if is_filename
            else match.group("name")
        )

    if not modes:
        return None

    if len(modes) > 1:
        modes_text = ", ".join(sorted(modes))
        raise PluginError(
            f"Path '{source_uri}' contains conflicting mode suffixes: {modes_text}"
        )

    return "/".join(canonical_parts), modes.pop()


def _filter_nav(nav: Any, unavailable_pages: set[str]) -> Any:
    """Remove unavailable page paths and any sections left empty by removal."""

    if isinstance(nav, str):
        path = nav.replace("\\", "/").lstrip("/")
        return _DROP_NAV_ITEM if path in unavailable_pages else nav

    if isinstance(nav, list):
        filtered_items = []
        for item in nav:
            filtered_item = _filter_nav(item, unavailable_pages)
            if filtered_item is not _DROP_NAV_ITEM:
                filtered_items.append(filtered_item)
        return filtered_items if filtered_items else _DROP_NAV_ITEM

    if isinstance(nav, dict):
        filtered_items = {}
        for title, item in nav.items():
            filtered_item = _filter_nav(item, unavailable_pages)
            if filtered_item is not _DROP_NAV_ITEM:
                filtered_items[title] = filtered_item
        return filtered_items if filtered_items else _DROP_NAV_ITEM

    return nav
