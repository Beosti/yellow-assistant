import os


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