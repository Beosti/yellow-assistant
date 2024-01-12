import os
import random
import string
import json

import helper_methods


def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


userName = input("Enter your username: ")
eMail = input("Enter your email: ")
site = input("For what site: ")
while True:
    passswordLengthBool = input("Enter the password length: ")

    try:
        passswordLength = int(passswordLengthBool)
        break
    except ValueError:
        print("Please enter a valid integer")

passwordGenerated = generate_password(passswordLength)


# Function to load configuration from the JSON file
config = helper_methods.load_config()

file_path = config.get("file_path_passwords")

with open(file_path, "a") as file:
    file.write(f"Site:  {site}\n")
    file.write(f"Username: {userName}\n")
    file.write(f"Email: {eMail}\n")
    file.write(f"Password: {passwordGenerated}\n")
    file.write("-" * 20 + "\n")

print(f"Password has been saved to {file_path}")
