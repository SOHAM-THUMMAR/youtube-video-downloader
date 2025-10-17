# YouTube Video Downloader (4K Video & MP3) — Windows-friendly

A small, opinionated, and easy-to-use Python script that automatically downloads YouTube videos (including up to 4K when available) or extracts high-quality MP3 audio. The script manages missing dependencies (yt-dlp, FFmpeg) for you and provides a simple command-line interface so you can start downloading quickly.

This repository is maintained by Soham Thummar — geared for Windows usage but straightforward to adapt for other platforms.

---

Table of contents
- About
- Features
- Requirements
- Quick install
- Usage
- Examples
- How it works (high level)
- Folder structure
- Troubleshooting
- Contributing
- License
- Author & Contact

---

About
-----
This script automates the common boilerplate around downloading YouTube content:
- Detects whether you want audio (MP3) or video (best quality, up to 4K)
- Installs missing Python package yt-dlp automatically
- Downloads and configures FFmpeg if it's not available on the system PATH
- Shows basic live progress in the terminal

Use it for educational and personal purposes only. Respect copyrights and terms of service of content providers.

Features
--------
- Automatic dependency handling (yt-dlp)
- Automatic FFmpeg download/extract (if missing)
- Best-quality video selection (including 4K when available)
- MP3 audio extraction option with high bitrate
- Simple, zero-configuration CLI
- Works well on Windows (tested). May work on Linux/macOS with minor changes.

Requirements
------------
- Python 3.8 or newer
- Internet connection (for downloading FFmpeg and content)
- Windows (tested). Cross-platform usage may require adapting FFmpeg detection/path logic.

Quick install
-------------
1. Clone the repo:
   git clone https://github.com/SOHAM-THUMMAR/youtube-video-downloader.git
   cd youtube-video-downloader

2. Run the downloader:
   python downloader.py

The script will prompt for a YouTube URL and handle the rest (dependency installation, FFmpeg setup, download).

Usage
-----
Basic usage (interactive):
- Run python downloader.py and follow the prompts.

Direct CLI usage:
- Download best video:
  python downloader.py https://youtu.be/dQw4w9WgXcQ

- Force audio (MP3):
  python downloader.py https://youtu.be/dQw4w9WgXcQ audio

- Playlist support (if implemented/available in the script):
  python downloader.py <playlist-url>

Notes on modes:
- If you pass a second argument "music", "audio", or "song", the script will extract MP3 audio.
- If you pass nothing, the script tries to infer whether the link is mostly music or video. You can always force a mode using the second argument.

Examples
--------
- Download a 4K video when available:
  python downloader.py https://www.youtube.com/watch?v=dQw4w9WgXcQ

- Download MP3 audio:
  python downloader.py https://www.youtube.com/watch?v=dQw4w9WgXcQ music

How it works (high level)
-------------------------
- install_package(): ensures required Python packages (yt-dlp) are installed
- ensure_ffmpeg(): checks for ffmpeg on PATH; if not present, downloads and extracts a portable ffmpeg copy into a local folder and uses it
- progress_hook(): receives progress updates from yt-dlp and prints download percentage, ETA, and speed
- download_youtube(): builds yt-dlp options to select best video/audio formats and calls yt-dlp to download
- main(): CLI + orchestration

Folder structure
----------------
Auto-YouTube-Downloader/<br>
├── downloader.py        # Main script (entry point)<br>
├── ffmpeg/              # Auto-downloaded FFmpeg (created at runtime if needed)<br>
├── README.md            # This file<br>
└── requirements.txt     # Optional list of dependencies<br>

Troubleshooting
---------------
- yt-dlp installation fails:
  - Ensure you have a working internet connection.
  - Try: python -m pip install --upgrade yt-dlp

- FFmpeg not found and auto-download fails:
  - Check network/proxy settings.
  - As a workaround, install ffmpeg manually and add it to your PATH: https://ffmpeg.org/download.html

- Permission errors on Windows:
  - Run the terminal as Administrator if you encounter permission issues when creating files or folders.

Safety & Legal
--------------
This script is provided for educational and personal use. Do not use it to download copyrighted material without permission. You are responsible for ensuring downloads comply with YouTube’s Terms of Service and applicable law.

Contributing
------------
Contributions, bug reports and improvements are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch: git checkout -b feature/my-feature
3. Make your changes & tests.
4. Open a pull request describing your changes.

Planned improvements
- Add a GUI (Tkinter or PyQt)
- Add robust playlist support
- Improve cross-platform support (Linux/macOS)
- Auto-updater for yt-dlp and FFmpeg

Author & Contact
----------------
Soham Thummar  
GitHub: https://github.com/SOHAM-THUMMAR

