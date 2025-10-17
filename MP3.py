import yt_dlp

def download_4k_video_audio(url):
    ydl_opts = {
        'format': 'bestvideo[height<=2160]+bestaudio/best',  # Max 4K video + best audio
        'outtmpl': '%(title)s.%(ext)s',                     # Save with video title
        'merge_output_format': 'mp4',                       # Merge video+audio as mp4
        'ignoreerrors': True,
        'quiet': False,
        'no_warnings': True,
        'noplaylist': False,                                # Download full playlist if URL is playlist
        'postprocessors': [{
            'key': 'FFmpegMetadata',                        # Optional: embed metadata
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            print("4K video with high-quality audio downloaded successfully!")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    video_url = input("Enter YouTube playlist or video URL: ").strip()
    download_4k_video_audio(video_url)
