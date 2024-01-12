import json
import os.path
import subprocess

import helper_methods
from helper_methods import create_folder_possibly

config = helper_methods.load_config()

file_repositories = config.get("file_path_repositories")

repository_copy = input("Repository to copy: ")
repository_folder = input("Folder to copy to: ")

create_folder_possibly(repository_folder, file_repositories)

os.chdir(os.path.join(file_repositories, repository_folder))
subprocess.run(["git", "clone", repository_copy])
print(f"Repository '{repository_copy}' cloned to '{repository_folder}'.")
