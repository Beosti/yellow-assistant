import os
import json


def load_config(file_path_config="config.json"):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    config_file_path_special = os.path.join(script_directory, file_path_config)

    with open(config_file_path_special, "r") as config_file:
        config_stuff = json.load(config_file)

    return config_stuff


def create_folder_possibly(folder_name, base_folder):
    # Define the path to the Videos folder in the user's home directory
    folder_path = os.path.expanduser(base_folder)

    # Combine the Videos folder path with the new folder name
    new_folder_path = os.path.join(folder_path, folder_name)

    # Check if the folder exists
    if not os.path.exists(new_folder_path):
        # If it doesn't exist, create the folder
        os.makedirs(new_folder_path)
        print(f"Folder '{folder_name}' created inside '{folder_path}'.")
    else:
        # If it already exists, do nothing
        print(f"Folder '{folder_name}' inside '{folder_path}' already exists.")
