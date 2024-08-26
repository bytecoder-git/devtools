#!/usr/bin/env python3

# Copyright 2024, Bill Heyman (bill@bytecoder.com)
#
# This script is released under the MIT License. 
# See the LICENSE file for details.
 
import os
import sys
import argparse
import subprocess
from pathlib import Path
from collections import defaultdict

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def is_text_file(file_path):
    try:
        with open(file_path, 'rb') as f:
            chunk = f.read(8192)
            return b'\0' not in chunk and not chunk.startswith(b'%PDF-')
    except Exception as e:
        return False

def is_git_repository(path):
    return subprocess.call(['git', '-C', path, 'status'], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL) == 0

def rename_item(old_path, new_path, use_git):
    if use_git:
        subprocess.run(['git', 'mv', old_path, new_path], check=True)
    else:
        os.rename(old_path, new_path)

def process_file(file_path, old_name, new_name, old_name_underscored, dry_run):
    messages = []
    try:
        with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()

        new_content = content.replace(old_name, new_name).replace(old_name_underscored, new_name.replace(' ', '_'))
        occurrences = content.count(old_name) + content.count(old_name_underscored)

        if occurrences > 0:
            action = "Would replace" if dry_run else "Replaced"
            messages.append(f"{action} {occurrences} occurrences")
            if not dry_run:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
        else:
            messages.append("No changes needed in file content")
    except Exception as e:
        messages.append(f"Error processing file: {e}")

    return messages

def rename_xcode_project(project_dir, old_name, new_name, dry_run, verbose):
    project_dir = Path(project_dir)
    old_name_underscored = old_name.replace(' ', '_')
    use_git = is_git_repository(project_dir)
    file_messages = defaultdict(list)

    # First, process all file contents
    for root, _, files in os.walk(project_dir):
        for file in files:
            full_path = Path(root) / file
            if is_text_file(full_path):
                file_messages[full_path].append("Processing as text file")
                file_messages[full_path].extend(
                    process_file(full_path, old_name, new_name, old_name_underscored, dry_run)
                )
            else:
                file_messages[full_path].append("Skipping binary file")

    # Then, rename files and directories
    for root, dirs, files in os.walk(project_dir, topdown=False):
        for item in dirs + files:
            old_path = Path(root) / item
            new_item = item.replace(old_name, new_name).replace(old_name_underscored, new_name.replace(' ', '_'))
            new_path = Path(root) / new_item

            if item != new_item:
                action = "Would rename to" if dry_run else "Renamed to"
                file_messages[old_path].append(f"{action} {new_item}")
                if not dry_run:
                    rename_item(old_path, new_path, use_git)

    for file_path, messages in file_messages.items():
        eprint(f"{file_path}:")
        for msg in messages:
            eprint(f"  {msg}")
        eprint()  # Add a blank line between files

def main():
    parser = argparse.ArgumentParser(description="Rename an Xcode project.")
    parser.add_argument("project_dir", help="The directory of the Xcode project")
    parser.add_argument("old_name", help="The current name of the project")
    parser.add_argument("new_name", help="The new name for the project")
    parser.add_argument("--dry-run", action="store_true", help="Print what would happen without making changes")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    rename_xcode_project(args.project_dir, args.old_name, args.new_name, args.dry_run, args.verbose)

if __name__ == "__main__":
    main()
