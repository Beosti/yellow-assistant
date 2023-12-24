from pytube import YouTube, Playlist
from pytube.exceptions import VideoUnavailable
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


def download_video(video_link, video_format, folder_name):
    create_video_folder(folder_name)
    try:
        if "playlist" in video_link.lower():
            playlist = Playlist(video_link)
            for video in playlist.videos:
                download_single_video(video, video_format, folder_name)
        else:
            youtube = YouTube(video_link)
            download_single_video(youtube, video_format, folder_name)
    except VideoUnavailable as e:
        print(f"Error: {e}")
        print("The video is unavailable or age-restricted. Skipping download.")
    except Exception as e:
        print(f"Error: {e}")
        print("An unexpected error occurred. Skipping download.")


def download_single_video(video, video_format, folder_name):
    try:
        if video_format == "Video":
            stream = video.streams.get_highest_resolution()  # gets ready to download
            stream.download(f'/home/shibeo/Videos/{folder_name}')
            print(f"Download Complete of video: {video.title}")
        elif video_format == "Audio":
            stream = video.streams.filter(only_audio=True).first()
            stream.download(f'/home/shibeo/Videos/{folder_name}', filename=f"{video.title}.mp3")
            print(f"Download Complete of audio: {video.title}")
        else:
            print("Not a valid format!")
    except Exception as e:
        print(f"Error: {e}")
        print(f"An unexpected error occurred while downloading {video.title}. Skipping download.")


if __name__ == "__main__":
    videoLink = input("Link: ")
    videoFormat = input("Video or Audio: ")
    folderName = input("Folder name: ")
    download_video(videoLink, videoFormat, folderName)
