# Xcode Project Rename Utility

This Python script automates the process of renaming an Xcode project, including updating file contents and renaming directories and files.

## Features

- Renames all occurrences of the old project name in file contents
- Renames directories and files
- Handles both space-separated and underscore-separated project names
- Git-aware: uses `git mv` for renaming if the project is in a Git repository
- Dry-run option to preview changes without modifying files
- Verbose output option for detailed information about the renaming process

## Requirements

- Python 3.6 or higher
- Git (optional, for Git repository support)

## Installation

1. Download the `xcode_rename_project.py` script from the `xcode/rename_project/` directory to your desired location.
2. Make the script executable:
   ```
   chmod +x xcode_rename_project.py
   ```

## Usage

```
python xcode/rename_project/xcode_rename_project.py <project_directory> <old_name> <new_name> [options]
```

### Arguments

- `<project_directory>`: The root directory of your Xcode project
- `<old_name>`: The current name of your Xcode project
- `<new_name>`: The new name you want to give your Xcode project

### Options

- `--dry-run`: Run the script without making any changes (preview mode)
- `-v, --verbose`: Enable verbose output for detailed information about the renaming process

### Examples

1. Rename a project with verbose output:
   ```
   python xcode/rename_project/xcode_rename_project.py . "Old Project Name" "New Project Name" -v
   ```

2. Perform a dry run to preview changes:
   ```
   python xcode/rename_project/xcode_rename_project.py . "Old Project Name" "New Project Name" --dry-run
   ```

## How It Works

1. The script first processes all text files in the project directory, replacing occurrences of the old project name with the new name in the file contents.
2. After updating file contents, it renames directories and files that contain the old project name.
3. If the project is in a Git repository, the script uses `git mv` for renaming to preserve Git history.

## Important Notes

- Always backup your project before running this script.
- The script assumes that your project follows standard Xcode naming conventions.
- Binary files are skipped during the content replacement phase.
- While the script attempts to handle various edge cases, manual verification is recommended after running the script.

## Contributing

Contributions to improve the script are welcome. Please submit a pull request or open an issue to discuss proposed changes.

## License

This script is released under the MIT License. See the LICENSE file for details.

Copyright 2024, Bill Heyman (bill@bytecoder.com)