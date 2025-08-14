import os
from PIL import Image

# === CONFIGURATION ===
INPUT_FOLDER = "desktop"       # Folder with original images
OUTPUT_FOLDER = "output_image"     # Folder to save processed images
NEW_SIZE = (800, 600)               # Width x Height in pixels
OUTPUT_FORMAT = "PNG"               # Change to "JPEG", "WEBP", etc.

def resize_and_convert_images(input_dir, output_dir, size, output_format):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through files in the input folder
    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)

        # Skip non-files
        if not os.path.isfile(file_path):
            continue

        try:
            with Image.open(file_path) as img:
                # Resize the image
                resized_img = img.resize(size)

                # Create new filename
                base_name = os.path.splitext(filename)[0]
                new_filename = f"{base_name}.{output_format.lower()}"
                save_path = os.path.join(output_dir, new_filename)

                # Save in desired format
                resized_img.save(save_path, output_format)
                print(f"✅ Saved: {save_path}")

        except Exception as e:
            print(f"❌ Could not process {filename}: {e}")

if __name__ == "__main__":
    resize_and_convert_images(INPUT_FOLDER, OUTPUT_FOLDER, NEW_SIZE, OUTPUT_FORMAT)
    print("🎯 Batch image processing complete!")
