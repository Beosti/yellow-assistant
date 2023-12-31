import json
import os
import subprocess


def load_config(file_path_config="config.json"):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    config_file_path_special = os.path.join(script_directory, file_path_config)

    with open(config_file_path_special, "r") as config_file:
        config_stuff = json.load(config_file)

    return config_stuff


def run_mgba_with_rom(rom_pathing):
    flatpak_command = [
        "flatpak",
        "run",
        "io.mgba.mGBA",
        rom_pathing
    ]

    subprocess.run(flatpak_command)


# Load configuration
directories_data = load_config().get("file_path_rom")
rom_path = os.path.join(directories_data, "pokeemerald.gba")

# Change to the specified directory and run "make -j4"
os.chdir(directories_data)
subprocess.run(["make", "-j4"])

# Run mGBA with the ROM
run_mgba_with_rom(rom_path)

# Return to the base directory
home_directory = os.path.expanduser("~")
os.chdir(home_directory)
