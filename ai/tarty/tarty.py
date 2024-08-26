#!/usr/bin/env python3

import os
import re
import argparse
import sys
from typing import List, Tuple
from pathspec import PathSpec
from pathspec.patterns import GitWildMatchPattern

# File extensions to process
TEXT_EXTENSIONS = ['.txt', '.csv', '.md']
CODE_EXTENSIONS = ['.c', '.cpp', '.h', '.hh', '.hpp', '.m', '.mm', '.swift', '.rs', '.py', '.sh', '.rb', '.kt']
MARKUP_EXTENSIONS = ['.json', '.xml', '.xib', '.storyboard']

ALL_EXTENSIONS = TEXT_EXTENSIONS + CODE_EXTENSIONS + MARKUP_EXTENSIONS

def load_gitignore(directory: str) -> PathSpec:
    gitignore_path = os.path.join(directory, '.gitignore')
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r') as gitignore_file:
            gitignore_content = gitignore_file.read()
        return PathSpec.from_lines(GitWildMatchPattern, gitignore_content.splitlines())
    return PathSpec([])

def should_ignore_file(file_path: str, gitignore_spec: PathSpec) -> bool:
    file_name = os.path.basename(file_path)
    return file_name.startswith('.') or gitignore_spec.match_file(file_path)

def is_binary(file_path: str) -> bool:
    try:
        with open(file_path, 'rb') as file:
            return b'\0' in file.read(1024)
    except IOError:
        return True

def remove_comments(content: str, file_extension: str) -> str:
    if file_extension in ['.c', '.cpp', '.h', '.hh', '.hpp', '.m', '.mm', '.swift']:
        content = re.sub(r'/\*[\s\S]*?\*/', '', content)
        content = re.sub(r'//.*', '', content)
    elif file_extension in ['.py', '.sh', '.rb']:
        content = re.sub(r'#.*', '', content)
    elif file_extension == '.rs':
        content = re.sub(r'/\*[\s\S]*?\*/', '', content)
        content = re.sub(r'//.*', '', content)
    elif file_extension == '.kt':
        content = re.sub(r'/\*[\s\S]*?\*/', '', content)
        content = re.sub(r'//.*', '', content)
    elif file_extension in ['.xml', '.xib', '.storyboard']:
        content = re.sub(r'<!--[\s\S]*?-->', '', content)
    elif file_extension == '.md':
        content = re.sub(r'<!--[\s\S]*?-->', '', content)
    return content

def compress_content(content: str, file_extension: str) -> str:
    content = remove_comments(content, file_extension)
    
    if file_extension not in MARKUP_EXTENSIONS and file_extension != '.md':
        lines = content.splitlines()
        processed_lines = [line.strip() for line in lines if line.strip()]
        content = '\n'.join(processed_lines)
    elif file_extension in MARKUP_EXTENSIONS:
        content = re.sub(r'>\s+<', '><', content)
        lines = content.splitlines()
        processed_lines = [line.strip() for line in lines if line.strip()]
        content = '\n'.join(processed_lines)
    else:  # Markdown files
        lines = content.splitlines()
        processed_lines = [line.strip() for line in lines]
        content = '\n'.join(processed_lines)
    
    return content

def process_directory(input_dir: str, quiet: bool) -> List[Tuple[str, str]]:
    compressed_files = []
    gitignore_spec = load_gitignore(input_dir)
    
    for root, _, files in os.walk(input_dir):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, input_dir)
            
            if should_ignore_file(relative_path, gitignore_spec):
                if not quiet:
                    print(f"Ignored: {relative_path}")
                continue
            
            _, file_extension = os.path.splitext(file)
            
            if is_binary(file_path):
                if not quiet:
                    print(f"Skipped (binary): {relative_path}")
                continue
            
            if file_extension.lower() not in ALL_EXTENSIONS:
                if not quiet:
                    print(f"Skipped: {relative_path}")
                continue
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                compressed_content = compress_content(content, file_extension.lower())
                compressed_files.append((relative_path, compressed_content))
                
                if not quiet:
                    print(f"Added: {relative_path}")
            except UnicodeDecodeError:
                if not quiet:
                    print(f"Skipped (encoding error): {relative_path}")
    
    return compressed_files

def create_custom_archive(compressed_files: List[Tuple[str, str]], output_file: str) -> int:
    total_bytes = 0
    with open(output_file, 'w', encoding='utf-8') as f:
        for file_path, content in compressed_files:
            header = f"[[FILE:{file_path}]]\n"
            f.write(header)
            f.write(content)
            f.write("\n")  # Add a single newline between files
            total_bytes += len(header.encode('utf-8')) + len(content.encode('utf-8')) + 1  # +1 for the newline

    return total_bytes

def main():
    parser = argparse.ArgumentParser(description="Create compressed custom archives for AI ingestion.")
    parser.add_argument("-i", "--input_dir", required=True, help="Input directory containing files to process")
    parser.add_argument("-o", "--output_file", required=True, help="Output archive file name")
    parser.add_argument("-q", "--quiet", action="store_true", help="Suppress output of processed files")
    args = parser.parse_args()

    compressed_files = process_directory(args.input_dir, args.quiet)
    total_bytes = create_custom_archive(compressed_files, args.output_file)
    sys.stderr.write(f"tarty archive created: {args.output_file} ({total_bytes} bytes)\n")

if __name__ == "__main__":
    main()