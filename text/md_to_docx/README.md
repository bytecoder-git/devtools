# md_to_docx: Markdown to DOCX Converter

This Python script converts Markdown files to DOCX format with advanced formatting and structure preservation.

## Features

- Converts Markdown to DOCX format
- Preserves headings, paragraphs, tables, and lists
- Adds a title page with the document title
- Includes headers and footers with page numbers
- Supports section breaks
- Allows custom book title and date input
- Extracts title from the first H1 heading if not provided
- Handles input from file or standard input
- Flexible output file naming

## Requirements

- Python 3.6 or higher
- python-docx library
- markdown library
- beautifulsoup4 library

## Installation

1. Download the `md_to_docx.py` script to your desired location.
2. Make the script executable:
   ```
   chmod +x md_to_docx.py
   ```
3. Install the required dependencies:
   ```
   pip install python-docx markdown beautifulsoup4
   ```

## Usage

```
python md_to_docx.py [-i INPUT] [-o OUTPUT] [-t TITLE] [-d DATE]
```

### Arguments

- `-i, --input`: Input Markdown file (optional, uses stdin if not provided)
- `-o, --output`: Output DOCX file (optional, defaults to 'output.docx')
- `-t, --title`: Book title (optional, extracts from first H1 if not provided)
- `-d, --date`: Date to include in footer (format: YYYY-MM-DD, optional)

### Examples

1. Convert a Markdown file to DOCX:
   ```
   python md_to_docx.py -i input.md -o output.docx
   ```

2. Convert with a custom title and date:
   ```
   python md_to_docx.py -i input.md -o output.docx -t "My Book" -d 2024-08-28
   ```

3. Read from standard input:
   ```
   cat input.md | python md_to_docx.py -o output.docx
   ```

## How It Works

1. The script reads Markdown content from a file or standard input.
2. It converts the Markdown to HTML using the `markdown` library.
3. The HTML is then parsed with BeautifulSoup to extract structural elements.
4. A new DOCX document is created using the `python-docx` library.
5. The script adds a title page, headers, and footers to the document.
6. It processes the content, converting headings, paragraphs, tables, and lists to their DOCX equivalents.
7. The resulting DOCX file is saved with the specified or default name.

## Supported Markdown Elements

- Headings (H1 to H6)
- Paragraphs
- Tables
- Unordered and ordered lists
- Horizontal rules (converted to section breaks)

## Important Notes

- The script uses the first H1 heading as the document title if not provided via command-line argument.
- Tables are converted to simple grid-style tables in the DOCX output.
- The script adds page numbers, the current date (or user-specified date), and section names to the footer.
- While the script handles common Markdown elements, complex or nested structures might not be perfectly converted.

## Contributing

Contributions to improve the script are welcome. Please submit a pull request or open an issue to discuss proposed changes.

## License

This script is released under the MIT License.

Copyright 2024 Bill Heyman (bill@bytecoder.com)
