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
STARTER_FONT_FILE_PATH = os.path.join(SRC_FOLDER, STARTER_FONT_FILE)
TEMP_FONT_FILE_PATH = os.path.join(SRC_FOLDER, TEMP_FONT_FILE)
FONT_FILE_NAME = "sportsIcons"
FONT_FAMILY_NAME = "digiSportIcons"
CSS_CLASS = "dg_icon"
ICON_SIZE = "24"
name_mapping_json_path = os.path.join(SRC_FOLDER, "name_mapping.json")


name_mapping = load_name_mapping(name_mapping_json_path)
new_names_mapping = {}
filesArray = []


FONT = fontforge.open(STARTER_FONT_FILE_PATH)
LAST_FREE_GLYPH_INDEX = 0xE000
FILES_TO_ADD = os.listdir(TO_ADD_GLYPHS_PATH)
FILES_TO_REPLACE = os.listdir(TO_REPLACE_GLYPHS_PATH)

def initialLookFont(): 
    FONT = fontforge.open(STARTER_FONT_FILE_PATH)
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
                    # scale_glyph(glyph)
                    LAST_FREE_GLYPH_INDEX = code_point
                    # print(LAST_FREE_GLYPH_INDEX)
            else:
                custom_print(f"Does not exist {code_point}")
    
    # return LAST_FREE_GLYPH_INDEX

def addToFont(): 
    global LAST_FREE_GLYPH_INDEX
    global FILES_TO_ADD
    global FONT
    if LAST_FREE_GLYPH_INDEX is not None:
        start_index = LAST_FREE_GLYPH_INDEX + 1
        for idx, file in enumerate(FILES_TO_ADD, start=start_index):
            if idx >= 0xE7B6:  # Prevent overflow of PUA range
                break
            glyph_code = "uni" + format(idx, "04X")
            glyph = FONT.createChar(idx, glyph_code)
            glyph.importOutlines(os.path.join(TO_ADD_GLYPHS_PATH, file))
            scale_glyph(glyph)
            name = transform_name(os.path.splitext(file)[0])
            print(name, 'nn')
            new_names_mapping[idx] = name
    else:
        custom_print("No existing glyphs were found in the specified range.")
    update_name_mapping(new_names_mapping, name_mapping_json_path)
    

        
def replaceGlyphs():
    global FILES_TO_REPLACE
    global FONT
    
    for file in os.listdir(TO_REPLACE_GLYPHS_PATH):
        if file.endswith(".svg"):
            name = os.path.splitext(file)[0]
            try:
                glyph_code = "uni" + format(int(name), "04X")
                
                try:
                    # Try to get the glyph by glyph_code
                    glyph = FONT[glyph_code]
                    glyph.clear()  # Clear the existing glyph before replacing
                except (TypeError, KeyError):
                    # If glyph doesn't exist, create it
                    print(f"Glyph for {glyph_code} not found in FONT, creating new glyph.")
                    idx = int(name)  # Assuming the name can be converted into an index for createChar
                    glyph = FONT.createChar(idx, glyph_code)
                
                # Import the SVG outline and scale the glyph
                glyph.importOutlines(os.path.join(TO_REPLACE_GLYPHS_PATH, file))
                scale_glyph(glyph)
                print(f"Glyph for {glyph_code} replaced by the file {file}")
                
            except ValueError:
                print(f"Filename {file} is not a valid number for glyph code.")



def createHTMLCSS():
    global FONT
    html_content = get_html_template()
    V = random.randint(1, 1000)
    css_content = get_css_template(FONT_FILE_NAME, FONT_FAMILY_NAME, V)
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
                    
                    # print(f"name is {name} code_point is {code_point} glyph_code is {glyph_code}")
                    
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
                        messageDiv.style.display = 'block';  // Show the message
                        setTimeout(() => {
                            messageDiv.style.display = 'none';  // Hide the message after 2 seconds
                        }, 2000);
                    }).catch(err => {
                        console.error('Failed to copy text: ', err);
                    });
                });
            });
            </script>
            </html>     
    """


    # Save HTML file
    html_file_path = "output/index.html"
    with open(html_file_path, "w") as html_file:
        html_file.write(html_content)
        
    # Save CSS file
    css_file_path = "output/style.css"
    with open(css_file_path, "w") as css_file:
        css_file.write(css_content)

# Save the updated name mapping

def saveNewFont():
    
    global FONT

    output_dir = "output"
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

    if mode == "add":
        FONT = fontforge.open(STARTER_FONT_FILE_PATH) 
        initialLookFont()
        print(LAST_FREE_GLYPH_INDEX)
        addToFont()
        createHTMLCSS()
        saveNewFont()
        open_html_file()
        FONT.save(TEMP_FONT_FILE_PATH)
        
    elif mode == "replace":
        initialLookFont()
        replaceGlyphs()
        createHTMLCSS()
        saveNewFont()
        open_html_file()
        FONT.save(TEMP_FONT_FILE_PATH)
        
    elif mode == "generate":
        FONT = fontforge.open(STARTER_FONT_FILE_PATH) 
        initialLookFont()
        print(LAST_FREE_GLYPH_INDEX)
        createHTMLCSS()
        saveNewFont()
        open_html_file()
    
    

