from pytube import YouTube, Playlist
from pytube.exceptions import VideoUnavailable
import os
import json

from helper_methods import create_folder_possibly


def load_config(file_path_config="config.json"):
    with open(file_path_config, "r") as config_file:
        config_stuff = json.load(config_file)
    return config_stuff


# Load the configuration
config = load_config()

file_videos = config.get("file_path_videos")


def download_video(video_link, video_format, folder_name):
    create_folder_possibly(folder_name, file_videos)
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
            stream.download(os.path.join(file_videos, folder_name))
            print(f"Download Complete of video: {video.title}")
        elif video_format == "Audio":
            stream = video.streams.filter(only_audio=True).first()
            stream.download(os.path.join(file_videos, folder_name), filename=f"{video.title}.mp3")
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
