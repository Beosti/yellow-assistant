# Keyboard module in Python
import json

import keyboard
import subprocess

print("Hotkeys and shortcuts enabled!")

with open('hotkey_config.json', 'r') as file:
    config = json.load(file)
# TODO add a shortcut for primeflix.lol (maybe abott)
# Extract abbreviation and replacement
abbreviation = config['abbreviation']
replacement = config['replacement']


def open_chrome():
    subprocess.Popen(['start', 'chrome', '--new-window'], shell=True)


def open_file_explorer():
    subprocess.Popen(['explorer', r'C:\\'], shell=True)


# press windows + f to open chrome
keyboard.add_hotkey('linker windows + f', lambda: open_chrome())
# press windows + w to open file explorer
keyboard.add_hotkey('linker windows + w', lambda: open_file_explorer())

keyboard.add_abbreviation(abbreviation, replacement)

keyboard.wait('linker windows + esc')
