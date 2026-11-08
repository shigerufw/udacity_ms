#!/usr/bin/env python3
"""
Generate a Markdown representation of the project folder tree for README.md.

Usage:
    python3 generate_map.py
    python3 generate_map.py --root /path/to/dir --output map.md --max-depth 4
"""

import argparse
import fnmatch
from pathlib import Path
from typing import List, Optional, Set

DEFAULT_IGNORED_NAMES: Set[str] = {
    ".git",
    ".DS_Store",
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
    ".mypy_cache",
    ".ipynb_checkpoints",
    ".venv",
    "venv",
    "map.md",
    "import_test.py",
}


def load_gitignore_patterns(root_path: Path) -> List[str]:
    """Load exclusion patterns from .gitignore if present."""
    gitignore_path = root_path / ".gitignore"
    patterns: List[str] = []
    if gitignore_path.is_file():
        try:
            with open(gitignore_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        # Remove leading/trailing slashes for easier matching
                        clean = line.strip("/")
                        if clean:
                            patterns.append(clean)
        except OSError:
            pass
    return patterns


def is_ignored(
    path: Path,
    root_path: Path,
    ignored_names: Set[str],
    gitignore_patterns: List[str],
    include_hidden: bool,
    output_filename: str,
) -> bool:
    """Determine whether a given file or directory should be excluded."""
    name = path.name

    # Skip output file itself to avoid circular mapping
    if name == output_filename:
        return True

    # Check hidden files/directories unless explicitly requested
    if not include_hidden and name.startswith(".") and name != ".":
        return True

    # Check default ignored folder/file names
    if name in ignored_names:
        return True

    # Check gitignore patterns
    try:
        rel_path = path.relative_to(root_path).as_posix()
    except ValueError:
        rel_path = name

    for pattern in gitignore_patterns:
        # Match either the file name or relative path
        if fnmatch.fnmatch(name, pattern) or fnmatch.fnmatch(rel_path, pattern):
            return True
        # Match directory pattern against relative path or any part
        if fnmatch.fnmatch(rel_path, f"*{pattern}*"):
            return True

    return False


def build_tree(
    dir_path: Path,
    root_path: Path,
    prefix: str = "",
    max_depth: Optional[int] = None,
    current_depth: int = 0,
    dirs_only: bool = False,
    dirs_first: bool = False,
    include_hidden: bool = False,
    ignored_names: Optional[Set[str]] = None,
    gitignore_patterns: Optional[List[str]] = None,
    output_filename: str = "map.md",
) -> List[str]:
    """Recursively build ASCII tree representation of the folder structure."""
    if ignored_names is None:
        ignored_names = DEFAULT_IGNORED_NAMES
    if gitignore_patterns is None:
        gitignore_patterns = []

    if max_depth is not None and current_depth >= max_depth:
        return []

    lines: List[str] = []

    try:
        entries = [
            e
            for e in dir_path.iterdir()
            if not is_ignored(
                e,
                root_path,
                ignored_names,
                gitignore_patterns,
                include_hidden,
                output_filename,
            )
        ]
    except PermissionError:
        return [f"{prefix}[Permission Denied]"]

    if dirs_only:
        entries = [e for e in entries if e.is_dir()]

    if dirs_first:
        entries.sort(key=lambda x: (not x.is_dir(), x.name.lower()))
    else:
        entries.sort(key=lambda x: x.name.lower())

    total = len(entries)
    for idx, entry in enumerate(entries):
        is_last = idx == (total - 1)
        connector = "└── " if is_last else "├── "
        display_name = entry.name + ("/" if entry.is_dir() else "")
        lines.append(f"{prefix}{connector}{display_name}")

        if entry.is_dir():
            child_prefix = prefix + ("    " if is_last else "│   ")
            child_lines = build_tree(
                entry,
                root_path=root_path,
                prefix=child_prefix,
                max_depth=max_depth,
                current_depth=current_depth + 1,
                dirs_only=dirs_only,
                dirs_first=dirs_first,
                include_hidden=include_hidden,
                ignored_names=ignored_names,
                gitignore_patterns=gitignore_patterns,
                output_filename=output_filename,
            )
            lines.extend(child_lines)

    return lines


def generate_map_file(
    root_dir: str = ".",
    output_file: str = "map.md",
    max_depth: Optional[int] = None,
    dirs_only: bool = False,
    dirs_first: bool = True,
    include_hidden: bool = False,
    respect_gitignore: bool = True,
) -> None:
    """Generate Markdown map file from the specified directory."""
    root_path = Path(root_dir).resolve()
    output_path = Path(output_file).resolve()

    gitignore_patterns = (
        load_gitignore_patterns(root_path) if respect_gitignore else []
    )

    tree_lines = [f"{root_path.name}/"]
    tree_lines.extend(
        build_tree(
            root_path,
            root_path=root_path,
            prefix="",
            max_depth=max_depth,
            current_depth=0,
            dirs_only=dirs_only,
            dirs_first=dirs_first,
            include_hidden=include_hidden,
            ignored_names=DEFAULT_IGNORED_NAMES,
            gitignore_patterns=gitignore_patterns,
            output_filename=output_path.name,
        )
    )

    tree_content = "\n".join(tree_lines)

    markdown_doc = f"""# Project Structure

```text
{tree_content}
```

<!--
Copy and paste the code block above directly into your README.md under the "## Structure" section.
-->
"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown_doc)

    print(f"Map successfully generated at: {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Map folder hierarchy and export as a Markdown tree representation."
    )
    parser.add_argument(
        "--root",
        "-r",
        default=".",
        help="Root folder to map (default: current directory)",
    )
    parser.add_argument(
        "--output",
        "-o",
        default="map.md",
        help="Output Markdown file name or path (default: map.md)",
    )
    parser.add_argument(
        "--max-depth",
        "-d",
        type=int,
        default=None,
        help="Maximum depth to map (default: unlimited)",
    )
    parser.add_argument(
        "--dirs-only",
        action="store_true",
        help="List only directories, omitting files",
    )
    parser.add_argument(
        "--alphabetical",
        action="store_true",
        help="Sort alphabetically instead of placing directories first",
    )
    parser.add_argument(
        "--include-hidden",
        action="store_true",
        help="Include hidden files and folders",
    )
    parser.add_argument(
        "--no-gitignore",
        action="store_true",
        help="Do not filter based on .gitignore patterns",
    )

    args = parser.parse_args()

    generate_map_file(
        root_dir=args.root,
        output_file=args.output,
        max_depth=args.max_depth,
        dirs_only=args.dirs_only,
        dirs_first=not args.alphabetical,
        include_hidden=args.include_hidden,
        respect_gitignore=not args.no_gitignore,
    )


if __name__ == "__main__":
    main()
