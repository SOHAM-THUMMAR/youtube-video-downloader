🎥 Auto YouTube Downloader (4K Video & MP3) for Windows

A fully automated YouTube downloader built with Python + yt-dlp + FFmpeg.
It automatically handles everything — from installing missing dependencies to downloading FFmpeg and fetching the best-quality audio/video for you.

🚀 Features

✅ Automatic Package Installation — Installs yt-dlp if missing
✅ Automatic FFmpeg Setup — Downloads and extracts FFmpeg if not installed
✅ 4K Video or MP3 Audio — Automatically selects the best available format
✅ Simple Command Line Interface (CLI) — Easy to use with zero setup
✅ Auto Mode Detection — Detects audio/video mode based on the URL content
✅ Windows Optimized — Designed and tested for Windows systems

🧰 Requirements

Make sure you have:

🐍 Python 3.8+ installed

💻 Internet connection (for auto FFmpeg + video download)

That’s it — no manual installations needed!

⚙️ Installation & Usage
1️⃣ Clone this Repository
git clone https://github.com/<your-username>/Auto-YouTube-Downloader.git
cd Auto-YouTube-Downloader

2️⃣ Run the Script
python downloader.py

3️⃣ Enter YouTube URL

You’ll be prompted to enter:

🎥 Enter YouTube video or playlist URL: https://youtu.be/example


The script will automatically:

Detect whether it’s music or video

Install dependencies if missing

Download FFmpeg if needed

Start downloading immediately 🚀

🎬 Examples
▶ Download 4K Video
python downloader.py https://youtu.be/dQw4w9WgXcQ

🎵 Download Audio (MP3)
python downloader.py https://youtu.be/dQw4w9WgXcQ music


OR — The script will automatically detect "music", "audio", or "song" in the URL and switch to MP3 mode.

🧠 How It Works
Component	Description
install_package()	Automatically installs missing Python packages
ensure_ffmpeg()	Checks for FFmpeg or downloads it automatically
progress_hook()	Displays live download progress in terminal
download_youtube()	Handles YouTube downloading with yt-dlp
main	Orchestrates the automation workflow
🪄 Folder Structure
📦 Auto-YouTube-Downloader
├── downloader.py        # Main Python script<br>
├── ffmpeg/              # Auto-downloaded FFmpeg folder<br>
├── README.md            # Documentation<br>
└── requirements.txt     # (Optional) Dependency list<br>

⚠️ Notes

This script is for educational and personal use only.

Do not use it to download copyrighted material without permission.

The project relies on yt-dlp (a modern fork of youtube-dl).

💡 Future Improvements

 Add GUI version (Tkinter / PyQt5)

 Support automatic playlist downloading

 Add cross-platform (Linux & macOS) support

 Add auto-updater for yt-dlp

👨‍💻 Author

Soham Thummar
💬 AI | ML | Robotics | IoT Enthusiast
📧 [your-email@example.com
]
🌐 GitHub: github.com/your-username

⭐ Support

If you like this project, please give it a ⭐ on GitHub — it helps others find it too!
