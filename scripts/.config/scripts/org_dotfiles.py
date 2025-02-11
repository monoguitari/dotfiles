import os
import shutil

# Define the base directory
base_dir = os.path.expanduser("~/.dotfiles")

# Check if the base directory exists
if os.path.exists(base_dir):
    # Iterate through all top-level directories in ~/.dotfiles
    for folder in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder)
        if os.path.isdir(folder_path):
            # Create a .config directory inside each top-level folder
            config_dir = os.path.join(folder_path, ".config")
            if not os.path.exists(config_dir):
                os.makedirs(config_dir)

            # Move all subfolders into the .config directory
            for item in os.listdir(folder_path):
                item_path = os.path.join(folder_path, item)
                if os.path.isdir(item_path) and item != ".config":
                    shutil.move(item_path, config_dir)
                    print(f"Moved: {item_path} -> {config_dir}")
else:
    print(f"Base directory {base_dir} does not exist.")

