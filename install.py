#!/usr/bin/env python3

import os
import shutil
import argparse
import toml
import sys

def read_install_config():
    with open('install.toml', 'r') as f:
        return toml.load(f)

def prompt_user(message, yes_all):
    if yes_all:
        return True
    response = input(f"{message} (y/n): ").lower().strip()
    return response == 'y' or response == 'yes'

def get_dest_filename(file):
    basename = os.path.basename(file)
    return os.path.splitext(basename)[0]

def install_files(config, yes_all):
    bin_dir = os.path.expanduser('~/bin')
    os.makedirs(bin_dir, exist_ok=True)

    for file in config['files']:
        src = file
        dest_filename = get_dest_filename(file)
        dest = os.path.join(bin_dir, dest_filename)
        
        if os.path.exists(dest):
            if prompt_user(f"{dest_filename}: File already exists. Overwrite?", yes_all):
                shutil.copy2(src, dest)
                print(f"{dest_filename}: installed (overwritten) to {dest}", file=sys.stderr)
            else:
                print(f"{dest_filename}: skipped (not overwritten)", file=sys.stderr)
        else:
            shutil.copy2(src, dest)
            print(f"{dest_filename}: installed to {dest}", file=sys.stderr)

    if bin_dir not in os.environ['PATH']:
        print(f"PATH: warning - {bin_dir} is not in your PATH. You may need to add it.", file=sys.stderr)

def uninstall_files(config, yes_all):
    bin_dir = os.path.expanduser('~/bin')

    for file in config['files']:
        dest_filename = get_dest_filename(file)
        dest = os.path.join(bin_dir, dest_filename)
        if os.path.exists(dest):
            if prompt_user(f"{dest_filename}: Uninstall this file?", yes_all):
                os.remove(dest)
                print(f"{dest_filename}: uninstalled", file=sys.stderr)
            else:
                print(f"{dest_filename}: skipped (not uninstalled)", file=sys.stderr)
        else:
            print(f"{dest_filename}: skipped (not found)", file=sys.stderr)

def main():
    parser = argparse.ArgumentParser(description="Install or uninstall development tools")
    parser.add_argument('--uninstall', action='store_true', help="Uninstall the files")
    parser.add_argument('-y', '--yes', action='store_true', help="Answer yes to all prompts")
    args = parser.parse_args()

    config = read_install_config()

    if args.uninstall:
        uninstall_files(config, args.yes)
    else:
        install_files(config, args.yes)

if __name__ == "__main__":
    main()