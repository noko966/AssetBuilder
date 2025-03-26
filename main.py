import fontforge
import os
import sys
import webbrowser
import random

from utils import custom_print, load_name_mapping, update_name_mapping, scale_glyph, createCardHtml, transform_name
from templates import get_html_template, get_css_template

printEnabled = True

# Config for Paths and Names
SRC_FOLDER = "src"
ADD_FOLDER = "add"
REPLACE_FOLDER = "replace"
STARTER_FONT_FILE = "sportsIcons.ttf"
TEMP_FONT_FILE = "sportsIcons_tmp.ttf"

TO_ADD_GLYPHS_PATH = os.path.join(SRC_FOLDER, ADD_FOLDER)
TO_REPLACE_GLYPHS_PATH = os.path.join(SRC_FOLDER, REPLACE_FOLDER)
FONT_FILE_NAME = "sportsIcons"
FONT_FAMILY_NAME = "digiSportIcons"
CSS_CLASS = "dg_icon"
ICON_SIZE = "24"

# Globals that will be updated per weight
STARTER_FONT_FILE_PATH = None
TEMP_FONT_FILE_PATH = None
name_mapping_json_path = None
FONT = None
LAST_FREE_GLYPH_INDEX = 0xE000
new_names_mapping = {}
filesArray = []

def read_variant_flags():
    variant_flags = {"400": True, "100": True}  # default: both True if file not found
    try:
        if os.path.exists("variant_flags.txt"):
            with open("variant_flags.txt", "r") as f:
                lines = f.readlines()
                for line in lines:
                    if line.strip().startswith("400="):
                        variant_flags["400"] = line.strip().split("=")[1].lower() == "true"
                    elif line.strip().startswith("100="):
                        variant_flags["100"] = line.strip().split("=")[1].lower() == "true"
    except Exception as e:
        print(f"Error reading variant flags: {e}. Defaulting to both variants.")
    return variant_flags

def configure_paths(weight):
    global STARTER_FONT_FILE_PATH, TEMP_FONT_FILE_PATH, name_mapping_json_path
    STARTER_FONT_FILE_PATH = os.path.join(SRC_FOLDER, weight, STARTER_FONT_FILE)
    TEMP_FONT_FILE_PATH = os.path.join(SRC_FOLDER, weight, TEMP_FONT_FILE)
    name_mapping_json_path = os.path.join(SRC_FOLDER, "name_mapping.json")

def load_font(weight):
    global FONT
    configure_paths(weight)
    FONT = fontforge.open(STARTER_FONT_FILE_PATH)

FILES_TO_ADD = os.listdir(TO_ADD_GLYPHS_PATH)
FILES_TO_REPLACE = os.listdir(TO_REPLACE_GLYPHS_PATH)


def initialLookFont(): 
    global LAST_FREE_GLYPH_INDEX
    for code_point in range(0xE000, 0xE7B6):
        glyph_code = "uni" + format(code_point, "04X")
        if glyph_code in FONT:
            glyph = FONT[glyph_code]
            if glyph.isWorthOutputting():
                if glyph.foreground.isEmpty():
                    glyph.clear()
                    custom_print(f"Path does not exist for {code_point}")
                else:        
                    LAST_FREE_GLYPH_INDEX = code_point
            else:
                custom_print(f"Does not exist {code_point}")


def addToFont(): 
    global LAST_FREE_GLYPH_INDEX
    if LAST_FREE_GLYPH_INDEX is not None:
        start_index = LAST_FREE_GLYPH_INDEX + 1
        for idx, file in enumerate(FILES_TO_ADD, start=start_index):
            if idx >= 0xE7B6:
                break
            glyph_code = "uni" + format(idx, "04X")
            glyph = FONT.createChar(idx, glyph_code)
            glyph.importOutlines(os.path.join(TO_ADD_GLYPHS_PATH, file))
            scale_glyph(glyph)
            name = transform_name(os.path.splitext(file)[0])
            new_names_mapping[idx] = name
    else:
        custom_print("No existing glyphs were found in the specified range.")
    update_name_mapping(new_names_mapping, name_mapping_json_path)


def replaceGlyphs():
    for file in os.listdir(TO_REPLACE_GLYPHS_PATH):
        if file.endswith(".svg"):
            name = os.path.splitext(file)[0]
            try:
                glyph_code = "uni" + format(int(name), "04X")
                try:
                    glyph = FONT[glyph_code]
                    glyph.clear()
                except (TypeError, KeyError):
                    print(f"Glyph for {glyph_code} not found in FONT, creating new glyph.")
                    idx = int(name)
                    glyph = FONT.createChar(idx, glyph_code)

                glyph.importOutlines(os.path.join(TO_REPLACE_GLYPHS_PATH, file))
                scale_glyph(glyph)
                print(f"Glyph for {glyph_code} replaced by the file {file}")

            except ValueError:
                print(f"Filename {file} is not a valid number for glyph code.")


def createHTMLCSS():
    html_content = get_html_template()
    css_file_path = "src/starterCSS.css"
    try:
        with open(css_file_path, "r") as css_file:
            css_content = css_file.read()
        print(f"Loaded CSS from {css_file_path}")
    except FileNotFoundError:
        print(f"Error: {css_file_path} not found.")
        return
    V = random.randint(1, 1000)
    css_content += get_css_template(FONT_FILE_NAME, FONT_FAMILY_NAME, V)
    for code_point in range(0xE000, 0xE7B6):
        glyph_code = "uni" + format(code_point, "04X")
        if glyph_code in FONT:
            glyph = FONT[glyph_code]
            if glyph.isWorthOutputting():
                if glyph.foreground.isEmpty():
                    glyph.clear()
                    custom_print(f"Path does not exist for {code_point}")
                else:
                    name = load_name_mapping(name_mapping_json_path).get(str(code_point))
                    html_content += createCardHtml(transform_name(name), format(code_point, "04X"), CSS_CLASS)
                    css_content += f"""
                    .{CSS_CLASS}_{transform_name(name)}::before {{
                        content: "\\{format(code_point, "04X")}";
                    }}
                    """
            else:
                custom_print(f"Does not exist {code_point}")
    html_content += "\n</div>"

    html_content += """
        <div class="message" id="copyMessage">Copied!</div>
            </body>
            <script>
            document.querySelectorAll('.copy_class_btn_js').forEach(item => {
                item.addEventListener('click', function() {
                    const iconContent = this.parentElement.parentElement.querySelector('.copy_class_js').classList[0];
                    navigator.clipboard.writeText(iconContent).then(() => {
                        const messageDiv = document.getElementById('copyMessage');
                        messageDiv.style.display = 'block';
                        setTimeout(() => {
                            messageDiv.style.display = 'none';
                        }, 2000);
                    }).catch(err => {
                        console.error('Failed to copy text: ', err);
                    });
                });
            });
            </script>
            </html>     
    """

    os.makedirs("output", exist_ok=True)
    with open("output/index.html", "w") as html_file:
        html_file.write(html_content)
    with open("output/style.css", "w") as css_file:
        css_file.write(css_content)


def saveNewFont(weight):
    output_dir = os.path.join("output", weight)
    os.makedirs(output_dir, exist_ok=True)
    FONT.generate(f"{output_dir}/{FONT_FILE_NAME}.ttf")
    FONT.generate(f"{output_dir}/{FONT_FILE_NAME}.eot")
    FONT.generate(f"{output_dir}/{FONT_FILE_NAME}.woff")
    FONT.generate(f"{output_dir}/{FONT_FILE_NAME}.woff2")


def open_html_file():
    file_path = os.path.abspath("output/index.html")
    if os.path.exists(file_path):
        webbrowser.open(file_path)
    else:
        print(f"File {file_path} does not exist.")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "add"
    variant_flags = read_variant_flags()
    weights = [w for w in ["400", "100"] if variant_flags.get(w, False)]

    for weight in weights:
        load_font(weight)
        initialLookFont()

        if mode == "add":
            addToFont()
        elif mode == "replace":
            replaceGlyphs()

        saveNewFont(weight)
        FONT.save(TEMP_FONT_FILE_PATH)

    if mode in ["add", "replace", "generate"]:
        # Only generate HTML/CSS once
        createHTMLCSS()
        open_html_file()
