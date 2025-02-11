import os

# Define the base directory where recup_dir.* directories are located
base_dir = os.getcwd()

# List to store paths of found files
found_files = []

# Walk through all directories and files in the base directory
for root, dirs, files in os.walk(base_dir):
    for file in files:
        # Check if the file starts with "hyprland.conf"
        if file.startswith("hyprland.conf"):
            found_files.append(os.path.join(root, file))

# Print the found files
if found_files:
    print("Found files:")
    for file in found_files:
        print(file)
else:
    print("No files starting with 'hyprland.conf' were found.")

