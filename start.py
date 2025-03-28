import tkinter as tk
from tkinter import messagebox, filedialog
import os
import shutil
import requests
import random
import subprocess


def downloadFont():
    SRC_FOLDER = "src"
    STARTER_FONT_FILE = "sportsIcons.ttf"
    FONT_URL_400 = "https://cdn-sp.kertn.net/assets/fonts/sport-ui-icons/400/sportsIcons.ttf"
    FONT_URL_100 = "https://cdn-sp.kertn.net/assets/fonts/sport-ui-icons/100/sportsIcons.ttf"
    STARTER_FONT_400_FILE_PATH = os.path.join(SRC_FOLDER, "400", STARTER_FONT_FILE)
    STARTER_FONT_100_FILE_PATH = os.path.join(SRC_FOLDER, "100", STARTER_FONT_FILE)

    v = random.randint(1, 1000)
    font_url_400_with_version = f"{FONT_URL_400}?v={v}"
    font_url_100_with_version = f"{FONT_URL_100}?v={v}"

    print(f"Downloading font from {font_url_400_with_version}")
    print(f"Downloading font from {font_url_100_with_version}")

    response_400 = requests.get(font_url_400_with_version)
    response_100 = requests.get(font_url_100_with_version)

    if response_400.status_code == 200:
        with open(STARTER_FONT_400_FILE_PATH, 'wb') as font_file:
            font_file.write(response_400.content)
        print(f"Font downloaded and saved to {STARTER_FONT_400_FILE_PATH}")
    else:
        print(f"Failed to download the font. Status code: {response_400.status_code}")

    if response_100.status_code == 200:
        with open(STARTER_FONT_100_FILE_PATH, 'wb') as font_file:
            font_file.write(response_100.content)  # ✅ fixed path
        print(f"Font downloaded and saved to {STARTER_FONT_100_FILE_PATH}")
    else:
        print(f"Failed to download the font. Status code: {response_100.status_code}")



def downloadCSS():
    SRC_FOLDER = "src"
    STARTER_CSS_FILE = "starterCSS.css"
    FONT_URL = "https://cdn-sp.kertn.net/assets/fonts/sport-ui-icons/style.css"
    STARTER_CSS_FILE_PATH = os.path.join(SRC_FOLDER, STARTER_CSS_FILE)
    # Add versioning (optional)
    v = random.randint(1, 1000)
    css_url_with_version = f"{FONT_URL}?v={v}"

    # Download the font every time
    print(f"Downloading font from {css_url_with_version}")
    response = requests.get(css_url_with_version)
    if response.status_code == 200:
        with open(STARTER_CSS_FILE_PATH, 'wb') as css_file:
            css_file.write(response.content)
        print(f"Font downloaded and saved to {STARTER_CSS_FILE_PATH}")
    else:
        print(f"Failed to download the font. Status code: {response.status_code}")

def clear_directory(directory_path):
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

def call_ffpython(script_path, mode):
    ffpython_path = os.path.join('deps/bin', 'ffpython.exe')
    if not os.path.exists(ffpython_path):
        raise FileNotFoundError(f"ffpython.exe not found at {ffpython_path}")
    
    downloadFont()
    downloadCSS()

    def run_script():
        try:
            result = subprocess.run([ffpython_path, script_path, mode], check=True, capture_output=True, text=True)
            print("Output:", result.stdout)
        except subprocess.CalledProcessError as e:
            print("Error:", e.stderr)

    run_script()


def create_ui():
    def add_files():
        clear_directory(os.path.join("src", "add"))
        file_paths = filedialog.askopenfilenames(title="Select Files To Add")
        if file_paths:
            for file_path in file_paths:
                shutil.copy(file_path, os.path.join("src", "add"))
            print("Files added to src/add")

            apply_to_400 = messagebox.askyesno("Apply to 400?", "Do you want to add these glyphs to the 400 variant?")
            apply_to_100 = messagebox.askyesno("Apply to 100?", "Do you want to add these glyphs to the 100 variant?")

            if not apply_to_400 and not apply_to_100:
                print("No variant selected. Aborting.")
                return

            # Write selected variants to a temporary config file
            with open("variant_flags.txt", "w") as flag_file:
                flag_file.write(f"400={str(apply_to_400)}\n")
                flag_file.write(f"100={str(apply_to_100)}\n")

            call_ffpython('main.py', 'add')


    def replace_files():
        clear_directory(os.path.join("src", "replace"))
        file_paths = filedialog.askopenfilenames(title="Select Files To Replace")
        if file_paths:
            for file_path in file_paths:
                shutil.copy(file_path, os.path.join("src", "replace"))
            print("Files added to src/replace")
            call_ffpython('main.py', 'replace')  # Call with 'replace' mode

    def generate():
        call_ffpython('main.py', 'generate')  # Call with 'generate' mode

    # Create the main window
    root = tk.Tk()
    root.title("FONT EDITOR")
    root.geometry("400x400")

    # Define color palette
    bg_color = "#2cb5a0"
    button_add_color = "#0b293d"
    button_replace_color = "#0b293d"
    button_generate_color = "#ffffff"
    button_generate_text_color = "#0b293d"
    button_text_color = "#ffffff"
    button_font = ("Helvetica", 12, "bold")

    # Set background color
    root.configure(bg=bg_color)

    # Create UI elements with customized colors and sizes
    add_button = tk.Button(root, text="Add Glyphs", command=add_files, width=30, height=2, bg=button_add_color, fg=button_text_color, font=button_font)
    add_button.pack(pady=10)

    replace_button = tk.Button(root, text="Replace Glyphs", command=replace_files, width=30, height=2, bg=button_replace_color, fg=button_text_color, font=button_font)
    replace_button.pack(pady=10)

    generate_button = tk.Button(root, text="Generate Font", command=generate, width=30, height=4, bg=button_generate_color, fg=button_generate_text_color, font=button_font)
    generate_button.pack(pady=40)

    # edit_json_button = tk.Button(root, text="Edit JSON File", command=open_json_editor, width=25, height=2, bg=button_generate_color, fg=button_text_color, font=button_font)
    # edit_json_button.pack(pady=20)

    # Start the main event loop
    root.mainloop()

def open_json_editor():
    json_editor_root = tk.Tk()
    json_editor_root.mainloop()

if __name__ == "__main__":
    create_ui()
