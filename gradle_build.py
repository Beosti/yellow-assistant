import os
import json
import subprocess
import shutil


def load_config(file_path_config="config.json"):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    config_file_path_special = os.path.join(script_directory, file_path_config)

    with open(config_file_path_special, "r") as config_file:
        config_stuff = json.load(config_file)

    return config_stuff


def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"File '{old_name}' renamed to '{new_name}'.")
    except Exception as e:
        print(f"Error: {e}")


# Load directories from the configuration
directories_data = load_config().get("file_path_gradlebuild_directories")

# Get the build input from the user
build = input("To build: ")

os.chdir(directories_data)
os.chdir(build)

# Run the 'gradle build' command
subprocess.run(["gradle", "build"])

# Change to the 'build/libs' directory
os.chdir("build")
os.chdir("libs")

# Get the list of files in the 'libs' directory
files_in_libs = os.listdir()

# Check the number of files in the 'libs' directory
if len(files_in_libs) == 1:
    # If there is only one file, use it
    old_file_name = files_in_libs[0]
else:
    # If there are multiple files, prompt the user to choose
    print("Multiple files found in 'libs' directory. Choose a file to rename:")
    for i, file in enumerate(files_in_libs, start=1):
        print(f"{i}. {file}")

    choice = int(input("Enter the number corresponding to the file: "))

    # Validate the user's choice
    if 1 <= choice <= len(files_in_libs):
        old_file_name = files_in_libs[choice - 1]
    else:
        print("Invalid choice. Exiting.")
        exit()

# Get the new file name input from the user
file_name = input("Rename file to: ")
new_file_name = file_name + ".jar"

# Rename the file
rename_file(old_file_name, new_file_name)

source_file = os.getcwd() + "/" + new_file_name

os.getcwd()

# Load the configuration
config_file_path = load_config().get("file_path_builds")
directory_name = input("Put in file: ")

new_folder_path = os.path.join(config_file_path, directory_name)
if not os.path.exists(new_folder_path):
    os.makedirs(new_folder_path)
    print(f"Folder '{directory_name}' created inside '{new_folder_path}'.")
else:
    print(f"Folder '{directory_name}' inside '{new_folder_path}' already exists.")

shutil.move(source_file, new_folder_path)
# Move the file
# move_file(new_file_name, destination_directory)
