#!/usr/bin/env python3

import argparse
import os
import shutil
from PIL import Image, ImageOps
import numpy as np
from rembg import remove

def resize_image(image, size):
    """Resize image using aspect fill scale mode."""
    img_ratio = image.width / image.height
    target_ratio = size[0] / size[1]
    
    if img_ratio > target_ratio:
        # Image is wider, crop width
        new_width = int(target_ratio * image.height)
        left = (image.width - new_width) // 2
        image = image.crop((left, 0, left + new_width, image.height))
    elif img_ratio < target_ratio:
        # Image is taller, crop height
        new_height = int(image.width / target_ratio)
        top = (image.height - new_height) // 2
        image = image.crop((0, top, image.width, top + new_height))
    
    return image.resize(size, Image.LANCZOS)

def generate_ios_icons(source_img, output_dir):
    sizes = [20, 40, 48, 57, 60, 80, 86, 87, 120, 172, 1024, 2048]
    img = Image.open(source_img)
    
    for size in sizes:
        resized_img = resize_image(img, (size, size))
        output_path = os.path.join(output_dir, 'iOS', f'{os.path.splitext(os.path.basename(source_img))[0]}-{size}.png')
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        resized_img.save(output_path, 'PNG')
    
    # Generate additional iOS icons
    generate_additional_ios_icons(source_img, output_dir)
    
    print(f"iOS icons generated successfully in {os.path.join(output_dir, 'iOS')}")

def generate_additional_ios_icons(source_img, output_dir):
    img = Image.open(source_img)
    img_name = os.path.splitext(os.path.basename(source_img))[0]
    ios_dir = os.path.join(output_dir, 'iOS')
    
    # 1. 1024px x 1024px standard icon
    standard_icon = resize_image(img, (1024, 1024))
    standard_icon.save(os.path.join(ios_dir, f'{img_name}-1024.png'), 'PNG')
    
    # 2. 1024px x 1024px with only the subject on a transparent background
    subject_only = remove(standard_icon)
    subject_only.save(os.path.join(ios_dir, f'{img_name}-1024-dark.png'), 'PNG')
    
    # 3. 1024px x 1024px grayscale version of the subject on a transparent background
    grayscale = ImageOps.grayscale(subject_only).convert('RGBA')
    
    # Create a new image with the same alpha channel as the original
    tinted = Image.new('RGBA', grayscale.size)
    
    # Paste the grayscale image onto the new image, using the original alpha channel
    tinted.paste(grayscale, (0, 0), subject_only)
    
    tinted.save(os.path.join(ios_dir, f'{img_name}-1024-tinted.png'), 'PNG')

def generate_android_icons(source_img, output_dir):
    sizes = {
        36: 'mipmap-ldpi',
        48: 'mipmap-mdpi',
        72: 'mipmap-hdpi',
        96: 'mipmap-xhdpi',
        144: 'mipmap-xxhdpi',
        192: 'mipmap-xxxhdpi'
    }
    img = Image.open(source_img)
    
    for size, folder in sizes.items():
        resized_img = resize_image(img, (size, size))
        output_path = os.path.join(output_dir, 'Android', 'res', folder, 'ic_launcher.png')
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        resized_img.save(output_path, 'PNG')
    
    for size in [512, 1024, 2048]:
        resized_img = resize_image(img, (size, size))
        output_path = os.path.join(output_dir, 'Android', f'ic_launcher-{size}.png')
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        resized_img.save(output_path, 'PNG')
    
    print(f"Android icons generated successfully in {os.path.join(output_dir, 'Android')}")

def copy_source_image(source_img, output_dir):
    source_dir = os.path.join(output_dir, 'source')
    os.makedirs(source_dir, exist_ok=True)
    destination = os.path.join(source_dir, os.path.basename(source_img))
    shutil.copy2(source_img, destination)
    print(f"Source image copied to {destination}")

def main():
    parser = argparse.ArgumentParser(description='Generate mobile app icons for iOS and Android.')
    parser.add_argument('source_img', help='Source PNG image file (at least 1024x1024 pixels)')
    parser.add_argument('--platform', choices=['iOS', 'Android', 'all'], default='all', help='Target platform (default: all)')
    parser.add_argument('--output_dir', default='output', help='Output directory (default: output)')
    
    args = parser.parse_args()
    
    if not os.path.isfile(args.source_img):
        print(f"Error: Source image '{args.source_img}' not found.")
        return
    
    img = Image.open(args.source_img)
    if img.width < 1024 or img.height < 1024:
        print(f"Error: Source image must be at least 1024x1024 pixels. Current size: {img.width}x{img.height}")
        return
    
    # Create the output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Copy source image to output directory
    copy_source_image(args.source_img, args.output_dir)
    
    if args.platform in ['iOS', 'all']:
        generate_ios_icons(args.source_img, args.output_dir)
    
    if args.platform in ['Android', 'all']:
        generate_android_icons(args.source_img, args.output_dir)
    
    print(f"Icon generation completed for platform(s): {args.platform}")
    print(f"All outputs have been saved to: {os.path.abspath(args.output_dir)}")

if __name__ == '__main__':
    main()
