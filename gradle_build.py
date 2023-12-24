import subprocess
import os

# Change directory to the Desktop
desktop_path = os.path.expanduser("~/Desktop")
os.chdir(desktop_path)

build = input("To build: ")

# List of directories to navigate
directories = ["hustle", "half a dev", "modding", build]

# Change directory for each folder
for directory in directories:
    os.chdir(directory)
    print(directory)

# Run the 'gradle build' command
subprocess.run(["gradle", "build"])
