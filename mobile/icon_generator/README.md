# Mobile App Icon Generator

This Python script automates the process of generating app icons for iOS and Android platforms from a single source image.

## Features

- Generates iOS icons in various required sizes
- Generates Android icons for different screen densities
- Creates additional iOS icons including a standard icon, subject-only icon, and tinted icon
- Supports aspect fill scaling to maintain image proportions
- Copies the source image to the output directory
- Supports generating icons for iOS, Android, or both platforms

## Requirements

- Python 3.6 or higher
- Dependencies listed in `requirements.txt`

## Installation

1. Clone this repository or download the `mobile_generate_app_icons.py` script.
2. Install the required dependencies using the provided `requirements.txt` file:
   ```
   pip install -r requirements.txt
   ```
3. Make the script executable:
   ```
   chmod +x mobile_generate_app_icons.py
   ```

## Usage

You can now run the script directly as an executable:

```
./mobile_generate_app_icons.py <source_img> [options]
```

Alternatively, you can still use Python to run the script:

```
python3 mobile_generate_app_icons.py <source_img> [options]
```

### Arguments

- `<source_img>`: The source PNG image file (must be at least 1024x1024 pixels)

### Options

- `--platform {iOS,Android,all}`: Target platform (default: all)
- `--output_dir OUTPUT_DIR`: Output directory (default: output)

### Examples

1. Generate icons for both iOS and Android:
   ```
   ./mobile_generate_app_icons.py app_icon.png
   ```

2. Generate icons for iOS only:
   ```
   ./mobile_generate_app_icons.py app_icon.png --platform iOS
   ```

3. Generate icons with a custom output directory:
   ```
   ./mobile_generate_app_icons.py app_icon.png --output_dir my_icons
   ```

## How It Works

1. The script resizes the source image to various required sizes for iOS and Android platforms.
2. For iOS, it generates additional variations including a subject-only icon and a tinted icon.
3. For Android, it creates icons for different screen densities (ldpi, mdpi, hdpi, etc.).
4. All generated icons are saved in the specified output directory, organized by platform.
5. The source image is copied to the output directory for reference.

## Important Notes

- The source image should be a high-quality PNG file with dimensions of at least 1024x1024 pixels.
- The script uses aspect fill scaling to maintain the image's proportions, which may result in some cropping.
- Generated icons are saved in PNG format.
- Make sure to install all dependencies listed in `requirements.txt` before running the script.
- Ensure the script has execute permissions before running it directly.

## Contributing

Contributions to improve the script are welcome. Please submit a pull request or open an issue to discuss proposed changes.

## License

This script is released under the MIT License. See the LICENSE file for details.

Copyright 2024, Bill Heyman (bill@bytecoder.com)