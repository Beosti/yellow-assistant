import subprocess
import os

current_directory = os.path.dirname(os.path.abspath(__file__))


def main():
    print("Hello, what can I do for you today? :)")
    print("1. Build Project")
    print("2. Download Videos")
    print("3. Generate a random password")
    print("4. Copy a github repository")
    print("5. Compile a rom file")
    print("6. Convert a Video to a Gif file")

    choice = input("Enter your choice (1, 2, 3, 4, 5 or 6) or ask me a question: ")

    if choice == "1":
        script_path = os.path.join(current_directory, "gradle_build.py")
    elif choice == "2":
        script_path = os.path.join(current_directory, "youtube_downloader.py")
    elif choice == "3":
        script_path = os.path.join(current_directory, "generate_passwords.py")
    elif choice == "4":
        script_path = os.path.join(current_directory, "copy_repository.py")
    elif choice == "5":
        script_path = os.path.join(current_directory, "compile_rom.py")
    elif choice == "6":
        script_path = os.path.join(current_directory, "mp4_to_gif.py")
    elif choice == "Do you have sentience?":
        print("No.")
        input("")
    else:
        print("Invalid choice. Please enter 1, 2, 3 or 4.")
    # Run the selected script
    subprocess.run(["python3", script_path], check=True)


if __name__ == "__main__":
    main()
