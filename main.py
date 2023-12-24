import subprocess


def main():
    print("Hello, what can I do for you today?")
    print("1. Build Project")
    print("2. Download Videos")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        build_script_path = "/home/shibeo/PycharmProjects/automation/gradle_build.py"
        subprocess.run(["/usr/bin/python3.10", build_script_path], check=True)
    elif choice == "2":
        download_script_path = "/home/shibeo/PycharmProjects/automation/youtube_downloader.py"
        subprocess.run(["/usr/bin/python3.10", download_script_path], check=True)
    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
