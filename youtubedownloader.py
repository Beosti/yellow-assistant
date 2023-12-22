from pytube import YouTube
import os


def create_video_folder(folder_name):
    # Define the path to the Videos folder in the user's home directory
    video_path = os.path.expanduser('/home/shibeo/Videos/')

    # Combine the Videos folder path with the new folder name
    new_folder_path = os.path.join(video_path, folder_name)

    # Check if the folder exists
    if not os.path.exists(new_folder_path):
        # If it doesn't exist, create the folder
        os.makedirs(new_folder_path)
        print(f"Folder '{folder_name}' created inside '{video_path}'.")
    else:
        # If it already exists, do nothing
        print(f"Folder '{folder_name}' inside '{video_path}' already exists.")


videoLink = input("Link: ")
videoFormat = input("Video or Audio: ")
folderName = input("Folder name: ")
create_video_folder(folderName)
youtube = YouTube(videoLink)
if videoFormat == "Video":
    video = youtube.streams.get_highest_resolution()  # gets ready to download
    video.download('/home/shibeo/Videos/' + folderName)
    print("Download Complete of video")
elif videoFormat == "Audio":
    video = youtube.streams.filter(only_audio=True).first()
    video.download('/home/shibeo/Videos/' + folderName, filename=f"{video.title}.mp3")
    print("Download Complete of audio")
else:
    print("Not a valid format!")
    exit()
