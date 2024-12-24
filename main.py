import os
import yt_dlp

# Get the current working directory
save_path = os.getcwd()  # This will set the save path to the current directory

# Define the playlist URL (user input or fixed URL)
playlist_url = input("Enter YouTube playlist URL: ")

# Download the playlist with high quality
def download_playlist(url, path):
    ydl_opts = {
        'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),  # Save files with video title
        'format': 'bestvideo+bestaudio/best',  # Download best video and best audio
        'noplaylist': False,  # Make sure to download the whole playlist
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Start downloading
download_playlist(playlist_url, save_path)
