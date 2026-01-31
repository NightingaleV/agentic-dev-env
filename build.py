#!/usr/bin/env python3
"""
Build script for Agent Development Environment
Processes source files from src/ and generates dist/ output for different agent frameworks.

Features:
- Jinja2 template resolution for {% include %} directives
- Folder name mappings (e.g., prompts → command for OpenCode)
- File suffix transformations (e.g., .md → .agent.md for GitHub agents)
- Target-specific file overrides (target files take precedence over base files)
"""

import argparse
import shutil
import yaml
from pathlib import Path
from typing import Dict, List, Set
from jinja2 import Environment, FileSystemLoader, TemplateNotFound


class BuildSystem:
    def __init__(
        self, config_path: str = "build_config.yaml", project_root: Path = None
    ):
        """Initialize the build system with configuration."""
        self.project_root = project_root or Path.cwd()
        self.config_path = self.project_root / config_path
        self.config = self._load_config()

        # Setup paths
        self.templates_dir = self.project_root / self.config["templates_dir"]
        self.base_dir = self.project_root / self.config["base_dir"]
        self.targets_dir = self.project_root / self.config["targets_dir"]
        self.dist_dir = self.project_root / self.config["dist_dir"]

        # Setup Jinja2 environment with multiple search paths
        # Priority order: templates/ first, then base/ for including base content
        self.jinja_env = Environment(
            loader=FileSystemLoader(
                [
                    str(self.templates_dir),  # src/templates - small reusable templates
                    str(
                        self.base_dir
                    ),  # src/base - allows {% include "prompts/file.md" %}
                ]
            ),
            trim_blocks=False,
            lstrip_blocks=False,
            keep_trailing_newline=True,
        )

        # Track processed files to avoid duplicates
        self.processed_files: Set[Path] = set()

    def _load_config(self) -> dict:
        """Load configuration from YAML file."""
        with open(self.config_path, "r") as f:
            return yaml.safe_load(f)

    def _process_template(self, content: str, file_path: Path) -> str:
        """
        Process Jinja2 template directives in content.

        Args:
            content: File content potentially containing Jinja2 syntax
            file_path: Source file path (for error messages)

        Returns:
            Processed content with templates resolved
        """
        # Check if content contains Jinja2 syntax
        if "{%" not in content and "{{" not in content:
            return content

        try:
            template = self.jinja_env.from_string(content)
            return template.render()
        except TemplateNotFound as e:
            print(f"⚠️  Template not found while processing {file_path}: {e}")
            return content
        except Exception as e:
            print(f"⚠️  Error processing template in {file_path}: {e}")
            return content

    def _should_process_template(self, file_path: Path) -> bool:
        """Check if file should be processed for Jinja2 templates."""
        extensions = self.config.get("template_extensions", [".md"])
        return file_path.suffix in extensions

    def _apply_suffix_rule(
        self, file_path: Path, folder_name: str, suffix_rules: dict
    ) -> Path:
        """
        Apply suffix transformation rule to a file path.

        Args:
            file_path: Original file path
            folder_name: Base folder name (skills, agents, prompts, instructions)
            suffix_rules: Dictionary of folder_name -> new_suffix

        Returns:
            Transformed file path with new suffix if rule applies
        """
        if folder_name not in suffix_rules:
            return file_path

        new_suffix = suffix_rules[folder_name]
        stem = file_path.stem

        # Replace .md extension with new suffix
        if file_path.suffix == ".md":
            return file_path.with_name(stem + new_suffix)

        return file_path

    def _get_target_output_path(
        self,
        base_file: Path,
        target_name: str,
        base_folder: str,
    ) -> Path:
        """
        Calculate output path for a base file in a target.

        Args:
            base_file: Source file path relative to base_dir
            target_name: Target name (.github, .opencode, .codex)
            base_folder: Base folder name (skills, agents, prompts, instructions)

        Returns:
            Output path in dist/ with folder mapping and suffix rules applied
        """
        target_config = self.config["targets"][target_name]
        folder_mappings = target_config["folder_mappings"]
        suffix_rules = target_config.get("file_suffix_rules", {})

        # Get relative path from base folder
        rel_path = base_file.relative_to(self.base_dir / base_folder)

        # Apply folder mapping
        target_folder = folder_mappings.get(base_folder, base_folder)

        # Apply suffix rule
        transformed_rel_path = self._apply_suffix_rule(
            rel_path, base_folder, suffix_rules
        )

        # Build final output path
        return self.dist_dir / target_name / target_folder / transformed_rel_path

    def _target_file_exists(self, output_path: Path, target_name: str) -> bool:
        """
        Check if a target-specific file exists that would override this base file.

        Args:
            output_path: Calculated output path for base file
            target_name: Target name (.github, .opencode, .codex)

        Returns:
            True if target-specific file exists
        """
        # Calculate relative path from dist/target/
        rel_path = output_path.relative_to(self.dist_dir / target_name)

        # Check if exists in src/targets/target/
        target_file = self.targets_dir / target_name / rel_path
        return target_file.exists()

    def _copy_and_process_file(self, src_file: Path, dest_file: Path) -> None:
        """
        Copy file and process templates if applicable.

        Args:
            src_file: Source file path
            dest_file: Destination file path
        """
        # Create parent directory
        dest_file.parent.mkdir(parents=True, exist_ok=True)

        # Read source content
        try:
            content = src_file.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            # Binary file, just copy
            shutil.copy2(src_file, dest_file)
            return

        # Process template if applicable
        if self._should_process_template(src_file):
            content = self._process_template(content, src_file)

        # Write to destination
        dest_file.write_text(content, encoding="utf-8")

    def _process_base_folder(self, target_name: str, folder_name: str) -> int:
        """
        Process a base folder for a specific target.

        Args:
            target_name: Target name (.github, .opencode, .codex)
            folder_name: Base folder name (skills, agents, prompts, instructions)

        Returns:
            Number of files copied
        """
        base_folder = self.base_dir / folder_name
        if not base_folder.exists():
            return 0

        files_copied = 0

        # Walk all files in base folder
        for src_file in base_folder.rglob("*"):
            if not src_file.is_file():
                continue

            # Calculate output path
            output_path = self._get_target_output_path(
                src_file, target_name, folder_name
            )

            # Skip if target-specific file exists
            if self._target_file_exists(output_path, target_name):
                print(f"   ⏭️  Skipping {src_file.name} (target override exists)")
                continue

            # Copy and process file
            self._copy_and_process_file(src_file, output_path)
            self.processed_files.add(output_path)
            files_copied += 1

        return files_copied

    def _process_target_specific_files(self, target_name: str) -> int:
        """
        Copy target-specific files (overrides and additions).

        Args:
            target_name: Target name (.github, .opencode, .codex)

        Returns:
            Number of files copied
        """
        target_src = self.targets_dir / target_name
        if not target_src.exists():
            return 0

        files_copied = 0

        # Walk all files in target folder
        for src_file in target_src.rglob("*"):
            if not src_file.is_file():
                continue

            # Calculate relative path
            rel_path = src_file.relative_to(target_src)
            output_path = self.dist_dir / target_name / rel_path

            # Copy and process file
            self._copy_and_process_file(src_file, output_path)
            self.processed_files.add(output_path)
            files_copied += 1

        return files_copied

    def _process_passthrough_items(self) -> int:
        """
        Process passthrough folders and files (docs, tests, .vscode, AGENTS.md).

        Returns:
            Number of files copied
        """
        files_copied = 0

        # Process passthrough folders
        for folder_name in self.config.get("passthrough_folders", []):
            src_folder = self.targets_dir / folder_name
            dest_folder = self.dist_dir / folder_name

            if not src_folder.exists():
                continue

            # Walk all files in folder
            for src_file in src_folder.rglob("*"):
                if not src_file.is_file():
                    continue

                rel_path = src_file.relative_to(src_folder)
                output_path = dest_folder / rel_path

                self._copy_and_process_file(src_file, output_path)
                self.processed_files.add(output_path)
                files_copied += 1

        # Process passthrough files
        for file_name in self.config.get("passthrough_files", []):
            src_file = self.targets_dir / file_name
            dest_file = self.dist_dir / file_name

            if not src_file.exists():
                continue

            self._copy_and_process_file(src_file, dest_file)
            self.processed_files.add(dest_file)
            files_copied += 1

        return files_copied

    def build_target(self, target_name: str) -> None:
        """
        Build a specific target.

        Args:
            target_name: Target name (.github, .opencode, .codex)
        """
        print(f"\n🔨 Building target: {target_name}")

        target_config = self.config["targets"][target_name]
        include_folders = target_config.get("include_base_folders", [])

        total_files = 0

        # Process base folders
        for folder_name in include_folders:
            files_copied = self._process_base_folder(target_name, folder_name)
            if files_copied > 0:
                print(f"   ✅ {folder_name}: {files_copied} files")
            total_files += files_copied

        # Process target-specific files
        target_files = self._process_target_specific_files(target_name)
        if target_files > 0:
            print(f"   ✅ target-specific: {target_files} files")
        total_files += target_files

        print(f"   📦 Total: {total_files} files")

    def build_all(self, clean: bool = False) -> None:
        """
        Build all targets.

        Args:
            clean: If True, clean dist/ directory before building
        """
        print("🚀 Starting build process...")

        if clean and self.dist_dir.exists():
            print(f"🧹 Cleaning {self.dist_dir}...")
            shutil.rmtree(self.dist_dir)

        # Build each target
        for target_name in self.config["targets"].keys():
            self.build_target(target_name)

        # Process passthrough items
        print(f"\n🔨 Processing passthrough items...")
        passthrough_files = self._process_passthrough_items()
        if passthrough_files > 0:
            print(f"   ✅ {passthrough_files} files")

        print(f"\n✨ Build complete! Generated {len(self.processed_files)} total files")


def main():
    """Main entry point for the build script."""
    parser = argparse.ArgumentParser(
        description="Build agent development environment distribution files"
    )
    parser.add_argument(
        "--target",
        type=str,
        help="Build specific target only (.github, .opencode, .codex)",
    )
    parser.add_argument(
        "--clean", action="store_true", help="Clean dist/ directory before building"
    )
    parser.add_argument(
        "--config",
        type=str,
        default="build_config.yaml",
        help="Path to config file (default: build_config.yaml)",
    )

    args = parser.parse_args()

    # Initialize build system
    builder = BuildSystem(config_path=args.config)

    # Build
    if args.target:
        if args.clean:
            target_dir = builder.dist_dir / args.target
            if target_dir.exists():
                print(f"🧹 Cleaning {target_dir}...")
                shutil.rmtree(target_dir)
        builder.build_target(args.target)
    else:
        builder.build_all(clean=args.clean)


if __name__ == "__main__":
    main()
