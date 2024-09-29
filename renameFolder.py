import os
from utils import load_name_mapping
name_mapping_json_path = os.path.join("src", "name_mapping.json")

name_mapping = load_name_mapping(name_mapping_json_path)
# Define your mapping

def rename_files_based_on_mapping():
    for file in os.listdir("toRename"):
        if file.endswith(".svg"):
            # Get the filename without the extension
            name = os.path.splitext(file)[0]
            
            # Check if the current file name is in the mapping
            new_name = None
            for key, value in name_mapping.items():
                if value == name:  # Check if the file name matches a mapped value
                    new_name = key  # Set the new name from the mapping (key)
                    break
            
            # If a match was found in the mapping, rename the file
            if new_name:
                old_file_path = os.path.join("toRename", file)
                new_file_path = os.path.join("toRename", f"{new_name}.svg")
                os.rename(old_file_path, new_file_path)
                print(f"Renamed {file} to {new_name}.svg")
            else:
                print(f"No mapping found for {file}, skipping.")

# Call the function
rename_files_based_on_mapping()
