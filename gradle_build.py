import subprocess
import os
import json


def load_directories(file_path="config.json"):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
    return data.get("file_path_gradlebuild_directories", [])


directories_data = load_directories()

build = input("To build: ")

# List of directories to navigate
directories = directories_data if directories_data else []


# Change directory for each folder
for directory in directories:
    full_path = os.path.abspath(os.path.join(os.getcwd(), directory))
    os.chdir(full_path)

os.chdir(build)

# Run the 'gradle build' command
subprocess.run(["gradle", "build"])

os.chdir("build")
os.chdir("libs")
