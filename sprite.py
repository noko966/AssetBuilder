from PIL import Image
import csv
import os

spriteFileName = "sportImages"
small_sprite_size = 48
src_folder_path = "spriteSrc"
dist_folder_path = "spriteDist"
csv_file_path = os.path.join(src_folder_path, "mapping.csv")
sprite_folder_path = os.path.join(dist_folder_path, "spriteVars")
css_file_path = os.path.join(sprite_folder_path, "style.css")
html_file_path = os.path.join(sprite_folder_path, "index.html")

# Ensure the sprite directory exists
if not os.path.exists(sprite_folder_path):
    os.makedirs(sprite_folder_path)

# Read the CSV file to get the order and filenames
ordered_filenames = []
with open(csv_file_path, mode='r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        key = row[1]  # Assuming the second column is the key
        filename = f"{key}.png"
        ordered_filenames.append(filename)

# Determine the size of each image (assuming all images are the same size)
img_width, img_height = 48, 48  # Adjust if different

# Calculate the total height of the sprite (including spaces for missing images)
total_height = img_height * len(ordered_filenames)

# Create a new image for the sprite
sprite_image = Image.new('RGBA', (img_width, total_height), (255, 255, 255, 0))  # Transparent background

# Initial CSS content
css_content = f""".imgSpr {{
    --sportCount: {len(ordered_filenames)};
    --imageSize: {img_width}px; 
    flex-shrink: 0;
    background-repeat: no-repeat;
    background-image: url("{spriteFileName}.png");
    background-position: 0 calc(-151* var(--imageSize));
    width: var(--imageSize);
    height: var(--imageSize);
    background-size: var(--imageSize) calc(var(--sportCount) * var(--imageSize));
    overflow: hidden;
}}
"""

# Initial HTML content
html_content = f"""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
    <style>
        *{{
            box-sizing: border-box;
        }}
        .demo_block{{
            background-color: #121212;
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 24px;
            border: 1px solid #181818;
            flex-wrap: wrap;
        }}
    </style>
    <body>
"""

html_medium_sprites = f"""<div class="demo_block">
"""

# Paste each image into the sprite and add CSS rules
current_y = 0
index = 0
for filename in ordered_filenames:
    file_path = os.path.join(src_folder_path, 'images', filename)
    # file_path = os.path.join(src_folder_path, 'images_o', filename)

    if os.path.exists(file_path):
        img = Image.open(file_path)
        sprite_image.paste(img, (0, current_y))
        img.close()

    # Extract the base name without the extension for CSS class
    base_name = os.path.splitext(filename)[0]
    cssClass_suffix = f"imgSpr{base_name}"

    # Generate CSS for this item
    css_content += f".{cssClass_suffix} {{\n"
    css_content += f"    background-position: 0 calc(-{index} * var(--imageSize));\n"
    css_content += "}\n"

    html_medium_sprites += f"<div class='imgSpr {cssClass_suffix}'></div>"

    # Update y_position for the next image
    current_y += img_height
    index += 1

# Save the sprite image
sprite_path = os.path.join(sprite_folder_path, f"{spriteFileName}.png")
sprite_image.save(sprite_path)
print("Sprite created successfully.")

# Write CSS file
with open(css_file_path, 'w') as css_file:
    css_file.write(css_content)
print("CSS file has been created successfully.")


# end of HTML content

html_medium_sprites += f"""
    </div>
"""

html_content += f"""
        {html_medium_sprites}
    </body>
</html>
"""

# Write HTML file
with open(html_file_path, 'w') as html_file:
    html_file.write(html_content)
print("HTML file has been created successfully.")
