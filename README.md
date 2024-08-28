# Bytecoder's Full-Stack Development Tools and Scripts

Welcome to my collection of development scripts and tools for full-stack development. This repository contains various utilities that I've created or customized to streamline my development workflow.

## Tools Summary

### 1. JWT Decoding Script
**Location:** web/jwt/jwt_decode

A Bash script that decodes JSON Web Tokens (JWTs) directly from the command line, supporting input via command-line argument or stdin.

### 2. Markdown to DOCX Converter
**Location:** text/md_to_docx

A Python script that converts Markdown files to DOCX format with advanced formatting and structure preservation.

### 3. Mobile App Icon Generator
**Location:** mobile/icon_generator

A Python script that generates app icons for iOS and Android platforms from a single source image. It creates icons in various required sizes and formats for both platforms.

### 4. Tarty: AI-Friendly Archive Creator
**Location:** ai/tarty

A Python script that creates compressed custom archives suitable for AI ingestion by processing and compressing text files from a given directory.

### 5. Xcode Project Rename Utility
**Location:** xcode/rename_project

A Python script that automates the process of renaming an Xcode project. It updates file contents, renames directories and files, and works with Git repositories.

For detailed instructions on how to use each tool, please refer to the README.md file in its respective directory.

## Installation

This repository includes an installation script (`install.sh`) that allows you to easily deploy the tools to your local environment.

### install.toml

The `install.toml` file contains a list of all scripts and tools that will be installed. You can modify this file to add or remove tools as needed. The file structure is as follows:

```toml
files = [
    "ai/tarty/tarty.py",
    "mobile/icon_generator/mobile_generate_app_icons.py",
    "text/md_to_docx/md_to_docx.py",
    "web/jwt/jwt_decode.sh",
    "xcode/rename_project/xcode_rename_project.py",
    # Add more files here as needed
]
```

### install.sh

The `install.sh` script reads the `install.toml` file and copies the specified files to your `~/bin` directory. To use the installation script:

1. Ensure that both `install.sh` and `install.toml` are in the root directory of this repository.
2. Make the script executable:
   ```
   chmod +x install.sh
   ```
3. Run the script:
   ```
   ./install.sh
   ```

#### Options:

- `--overwrite`: Use this flag to overwrite existing files in the destination directory.
  ```
  ./install.sh --overwrite
  ```

The script will create the `~/bin` directory if it doesn't exist and will inform you if this directory is not in your PATH.

## Contributing

Contributions to this collection are welcome! If you have suggestions for improvements or have found a bug, please open an issue or submit a pull request.

## License

Each tool in this repository is licensed separately. Please refer to the LICENSE file in each tool's directory for specific licensing information.

---

I hope you find these tools useful in your development work. Happy coding!

Contact: Bill Heyman (bill@bytecoder.com)