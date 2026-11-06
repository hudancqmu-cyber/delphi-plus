#!/usr/bin/env python3
"""Install the portable Delphi Plus payload without overwriting existing files."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import shutil
import sys
from typing import List, Optional, Set, Tuple


SKILL_NAME = "delphi-plus"
PAYLOAD_DIRECTORIES = ("agents", "references", "assets")
USER_ROOTS = {
    "codex": Path(".agents") / "skills",
    "antigravity": Path(".gemini") / "config" / "skills",
    "claude-code": Path(".claude") / "skills",
}
PROJECT_ROOTS = {
    "codex": Path(".agents") / "skills",
    "antigravity": Path(".agents") / "skills",
    "claude-code": Path(".claude") / "skills",
}


class InstallError(Exception):
    """A predictable error that should be displayed without a traceback."""


def exists_including_symlink(path: Path) -> bool:
    return os.path.lexists(str(path))


def payload_plan(source: Path) -> Tuple[List[Path], List[Tuple[Path, Path]]]:
    """Validate the payload, resolving internal links and rejecting link cycles."""
    source = source.resolve(strict=True)
    directories: List[Path] = []
    files: List[Tuple[Path, Path]] = []

    def visit(path: Path, relative: Path, ancestors: Set[Path]) -> None:
        try:
            resolved = path.resolve(strict=True)
        except (OSError, RuntimeError) as exc:
            raise InstallError("Cannot resolve payload entry: {} ({})".format(path, exc))
        if not resolved.is_relative_to(source):
            raise InstallError("Payload link escapes the source directory: {}".format(path))
        if resolved.is_dir():
            if resolved in ancestors:
                raise InstallError("Payload directory link creates a cycle: {}".format(path))
            directories.append(relative)
            for entry in sorted(resolved.iterdir(), key=lambda item: item.name):
                visit(entry, relative / entry.name, ancestors | {resolved})
        elif resolved.is_file():
            files.append((resolved, relative))
        else:
            raise InstallError("Payload contains an unsupported entry: {}".format(path))

    entrypoint = source / "SKILL.md"
    if not entrypoint.is_file():
        raise InstallError("Source must contain a readable SKILL.md: {}".format(source))
    visit(entrypoint, Path("SKILL.md"), set())
    for name in PAYLOAD_DIRECTORIES:
        candidate = source / name
        if exists_including_symlink(candidate):
            if not candidate.is_dir():
                raise InstallError("Payload directory is invalid: {}".format(candidate))
            visit(candidate, Path(name), set())
    return directories, files


def install(source: Path, destination: Path, dry_run: bool = False) -> int:
    source = source.resolve(strict=True)
    destination = destination.absolute()
    resolved_destination = destination.resolve(strict=False)
    if resolved_destination.is_relative_to(source):
        raise InstallError("Destination cannot be the source or inside it: {}".format(destination))
    if exists_including_symlink(destination):
        raise InstallError("Destination already exists; nothing was overwritten: {}".format(destination))
    directories, files = payload_plan(source)
    print("Source: {}".format(source))
    print("Destination: {}".format(destination))
    if dry_run:
        print("Dry run: would install {} files; no files were changed.".format(len(files)))
        return len(files)

    destination.parent.mkdir(parents=True, exist_ok=True)
    # exist_ok=False also protects against a destination created since validation.
    destination.mkdir(exist_ok=False)
    for relative in directories:
        (destination / relative).mkdir(exist_ok=False)
    for actual, relative in files:
        shutil.copy2(str(actual), str(destination / relative))
    print("Installed Delphi Plus ({} files).".format(len(files)))
    return len(files)


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True, choices=tuple(USER_ROOTS))
    parser.add_argument("--scope", default="user", choices=("user", "project"))
    parser.add_argument("--project", type=Path, help="Existing project root; required for --scope project")
    parser.add_argument("--dry-run", action="store_true", help="Validate and show the destination without writing")
    args = parser.parse_args(argv)
    if args.scope == "project":
        if args.project is None:
            parser.error("--project is required for --scope project")
        project = args.project.expanduser().absolute()
        if not project.is_dir():
            parser.error("--project must name an existing directory: {}".format(project))
        destination = project / PROJECT_ROOTS[args.target] / SKILL_NAME
    else:
        if args.project is not None:
            parser.error("--project is only valid with --scope project")
        destination = Path.home() / USER_ROOTS[args.target] / SKILL_NAME
    try:
        install(Path(__file__).resolve().parents[1], destination, args.dry_run)
    except (InstallError, OSError, RuntimeError) as exc:
        print("Installation failed: {}".format(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
