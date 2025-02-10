import yt_dlp

# Get the video URL from the user
url = input("Enter the YouTube video URL: ")

# Get the quality preference from the user
quality = input("Enter video quality (e.g., 1080, 720, 480, best, worst): ")

# Define download options
ydl_opts = {
    'format': f'bestvideo[height={quality}]+bestaudio/best' if quality.isdigit() else quality,
    'outtmpl': 'Youtube-Downloads/%(title)s.%(ext)s',
}

# Download the video
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download completed!")
