import os
import shutil
import yt_dlp
import sys

def progress_hook(d):
    if d.get('status') == 'downloading':
        p = d.get('_percent_str') or ''
        speed = d.get('_speed_str') or ''
        eta = d.get('_eta_str') or ''
        sys.stdout.write(f"\rDownloading: {p} at {speed} ETA {eta}")
        sys.stdout.flush()
    elif d.get('status') == 'finished':
        print("\nDownload finished, now post-processing...")

def find_ffmpeg(ffmpeg_path_input=None):
    if ffmpeg_path_input:
        ff = ffmpeg_path_input.strip()
        if os.path.isfile(ff) or shutil.which(ff):
            return ff
        binpath = os.path.join(ff, "ffmpeg.exe") if os.name == "nt" else os.path.join(ff, "ffmpeg")
        if os.path.isfile(binpath):
            return binpath
    ff = shutil.which("ffmpeg")
    return ff

def download_youtube(url, download_type="video", cookies_file=None, ffmpeg_location=None):
    if download_type.lower() == "audio":
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
        }
    else:
        ydl_opts = {
            'format': 'bestvideo[height<=2160]+bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
            'postprocessors': [{'key': 'FFmpegMetadata'}],
        }

    ydl_opts.update({
        'ignoreerrors': False,
        'quiet': False,
        'no_warnings': True,
        'noplaylist': False,
        'geo_bypass': True,
        'force_generic_extractor': False,
        'progress_hooks': [progress_hook],
        'headers': {
            'User-Agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/117.0.0.0 Safari/537.36'
            )
        }
    })

    if cookies_file:
        cookies_file = os.path.expanduser(cookies_file)
        if os.path.exists(cookies_file):
            ydl_opts['cookiefile'] = cookies_file
            print(f"Using cookiefile: {cookies_file}")
        else:
            print(f"Warning: cookiefile '{cookies_file}' not found; skipping cookies.")
            cookies_file = None

    if not cookies_file:
        ydl_opts['cookies_from_browser'] = ('chrome',)

    ff = find_ffmpeg(ffmpeg_location)
    if ff:
        ydl_opts['ffmpeg_location'] = ff
        print(f"FFmpeg found: {ff}")
    else:
        print("WARNING: ffmpeg not found in PATH. Merging may fail.")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            if not info:
                print("Failed to download: video may be restricted or unavailable.")
                return False
            print(f"\n{download_type.capitalize()} download completed successfully!")
            return True
    except yt_dlp.utils.DownloadError as de:
        print(f"\nDownloadError: {de}")
    except Exception as e:
        print(f"\nUnexpected error: {e}")
    return False

if __name__ == "__main__":
    print("=== yt-dlp downloader (4K video or MP3 audio) ===")
    url = input("Enter YouTube playlist or video URL: ").strip()
    if not url:
        print("No URL provided. Exiting.")
        sys.exit(1)

    choice = input("Download type? Enter 'video' for 4K video or 'audio' for MP3 [video]: ").strip().lower() or "video"
    cookies_path = input("Enter full path to cookies.txt (or leave blank to auto-detect browser): ").strip() or r"C:\Users\COCO\Downloads\cookies.txt"
    if cookies_path == "": 
        cookies_path = None

    ff_path = input("Optional: Enter full path to ffmpeg executable (or leave blank to auto-detect): ").strip() or r'C:\ffmpeg\bin\ffmpeg.exe'
    if ff_path == "":
        ff_path = None

    download_youtube(url, download_type=choice, cookies_file=cookies_path, ffmpeg_location=ff_path)
