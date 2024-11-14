import os
import json

# this should automatically make a file if not put in config.json/ask where to put it
def load_config(config_option):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(script_directory, "config.json")

    # Check if the config file exists
    if os.path.exists(config_file_path):
        with open(config_file_path, "r") as config_file:
            config_stuff = json.load(config_file)
    else:
        print("Config file not found. Creating a new one.")
        config_stuff = {}

    # Prompt the user to input value for the specified configuration option
    if config_option not in config_stuff:
        value = input(f"Enter the value for {config_option}: ")
        config_stuff[config_option] = value

        # Update the config file with the user-provided value
        with open(config_file_path, "w") as config_file:
            json.dump(config_stuff, config_file, indent=4)

    return config_stuff.get(config_option)


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
