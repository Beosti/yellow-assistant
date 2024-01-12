import os
import shlex
import subprocess

import helper_methods

config = helper_methods.load_config()

file_path = config.get("file_path_to_best-gif")

input_directory = '/home/shibeo/'
output_directory = '/home/shibeo/Desktop/gifs/'

# Get the list of .mp4 files in the input directory
video_files = [f for f in os.listdir(input_directory) if f.endswith('.mp4')]

if not video_files:
    print("No .mp4 files found in the input directory.")
    exit()

# Display available .mp4 files to the user
print("Available .mp4 files:")
for i, video_file in enumerate(video_files, 1):
    print(f"{i}. {video_file}")

# Get user choice for the input video file
choice = int(input("Choose a file (enter the corresponding number): "))
if choice < 1 or choice > len(video_files):
    print("Invalid choice. Exiting.")
    exit()

video_input = os.path.join(input_directory, video_files[choice - 1])
# Get input from the user
# Get user input for the output gif file name
gif_output_name = input("Enter the name for the output gif file (without extension): ")
gif_output = os.path.join(output_directory, f"{gif_output_name}.gif")
# Use subprocess to run the shell script with user-input arguments
try:
    subprocess.run(['/bin/sh', file_path, os.path.normpath(video_input), os.path.normpath(gif_output)], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
