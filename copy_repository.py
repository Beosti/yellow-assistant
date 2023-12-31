import json
import os.path
import subprocess

from helper_methods import create_folder_possibly


def load_config(file_path_config="config.json"):
    with open(file_path_config, "r") as config_file:
        config_stuff = json.load(config_file)
    return config_stuff


config = load_config()
file_repositories = config.get("file_path_repositories")

repository_copy = input("Repository to copy: ")
repository_folder = input("Folder to copy to: ")

create_folder_possibly(repository_folder, file_repositories)

os.chdir(os.path.join(file_repositories, repository_folder))
subprocess.run(["git", "clone", repository_copy])
print(f"Repository '{repository_copy}' cloned to '{repository_folder}'.")
