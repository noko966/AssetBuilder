import os
import re


# Example folder path containing PNG files (use your actual path)
folder_path = os.path.join('spriteSrc', 'images')

# Function to rename PNG files by keeping only the number before the extension
def rename_png_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".png"):
            # Find matches with regex for "_<number>"
            match = re.search(r"_(\d+)", filename)
            if match:
                # Extract the number part and construct the new filename
                new_name = match.group(1) + ".png"
                # Construct the full file paths
                old_file = os.path.join(folder_path, filename)
                new_file = os.path.join(folder_path, new_name)
                # Rename the file
                os.rename(old_file, new_file)

# Run the function to rename the PNG files
rename_png_files(folder_path)

