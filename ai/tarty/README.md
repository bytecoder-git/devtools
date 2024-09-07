# Tarty: AI-Friendly Archive Creator

This Python script creates compressed custom archives suitable for AI ingestion by processing and compressing text files from a given directory.

## Features

- Processes text, code, and markup files
- Removes comments and unnecessary whitespace
- Skips binary files and files with unsupported extensions
- Ignores hidden files (starting with a dot)
- Respects .gitignore rules
- Creates a custom archive format with file headers
- Git-aware: compatible with Git repositories
- Quiet mode option to suppress output
- Detailed output about processed, skipped, and ignored files
- Custom ignore patterns support
- Displays compressed file sizes

## Requirements

- Python 3.6 or higher
- pathspec library

## Installation

1. Download the `tarty.py` script to your desired location.
2. Make the script executable:
   ```
   chmod +x tarty.py
   ```
3. Install the required dependency:
   ```
   pip install pathspec
   ```

## Usage

```
python tarty.py -i <input_directory> -o <output_file> [options]
```

### Arguments

- `-i, --input_dir`: The root directory containing files to process
- `-o, --output_file`: The name of the output archive file

### Options

- `-q, --quiet`: Suppress output of processed files
- `--ignore`: Additional patterns to ignore, separated by semicolons

### Examples

1. Create an archive with detailed output:
   ```
   python tarty.py -i /path/to/input/directory -o output_archive.txt
   ```

2. Create an archive in quiet mode:
   ```
   python tarty.py -i /path/to/input/directory -o output_archive.txt -q
   ```

3. Create an archive with custom ignore patterns:
   ```
   python tarty.py -i /path/to/input/directory -o output_archive.txt --ignore "file.txt;*.json;tmp/"
   ```

## How It Works

1. The script walks through the input directory and processes all supported text files.
2. It checks for a .gitignore file in the input directory and respects its rules.
3. Hidden files (starting with a dot) are automatically ignored.
4. Custom ignore patterns (if provided) are applied alongside .gitignore rules.
5. For each file:
   - If the file is ignored by .gitignore, custom patterns, or is hidden, it's skipped.
   - If the file is binary or has an unsupported extension, it's skipped.
   - For supported files, it removes comments and unnecessary whitespace while preserving essential structure.
6. Processed files are added to a custom archive format, with each file preceded by a header.
7. The resulting archive is optimized for AI ingestion, with reduced file sizes and preserved content structure.
8. The script displays the compressed size of each added file.

## Supported File Types

- Text: .txt, .csv, .md
- Code: .c, .cpp, .h, .hh, .hpp, .js, .ts, .m, .mm, .swift, .rs, .py, .sh, .rb, .kt, .go
- Markup: .json, .xml, .xib, .storyboard, .toml

## Important Notes

- Always backup your data before running this script on important files.
- The script is designed to work with common text, code, and markup file formats. Unsupported file types will be skipped.
- While the script attempts to handle various edge cases, manual verification of the output is recommended for critical data.
- The script requires the `pathspec` library to handle .gitignore rules. Make sure to install it before running the script.

## Contributing

Contributions to improve the script are welcome. Please submit a pull request or open an issue to discuss proposed changes.

## License

This script is released under the MIT License.

Copyright 2024 Bill Heyman (bill@bytecoder.com)