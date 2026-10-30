# Spider 🕷️

> Fast, resilient Instagram & social media video downloader, scraper, and local AI transcriber.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://python.org)
[![yt-dlp](https://img.shields.io/badge/Engine-yt--dlp-red.svg)](https://github.com/yt-dlp/yt-dlp)
[![Playwright](https://img.shields.io/badge/Scraper-Playwright-green.svg)](https://playwright.dev)
[![Whisper](https://img.shields.io/badge/AI-OpenAI%20Whisper-orange.svg)](https://github.com/openai/whisper)

---

## Features

- **⚡ Fast Multi-Stream Extraction**: Downloads full HD MP4 videos and extracts clean MP3 audio tracks via `ffmpeg`.
- **📊 Rich Metadata Parsing**: Dumps `.info.json` files with captions, upload dates, author metadata, and view/like stats.
- **🎙️ Zero-Cost Offline Transcription**: Transcribes audio directly on CPU with OpenAI Whisper (no OpenAI API key or paid subscription needed).
- **🌐 Network Interception Scraping**: Headless Playwright script that intercepts Instagram GraphQL responses and collects shortcodes directly without getting blocked by login modals.
- **🔁 Batch Downloader with Benchmarking**: Tested with 20/20 reels (100% success rate) in under 4 minutes with automatic retry mechanisms.

---

## Installation

```bash
# 1. Clone repository
git clone https://github.com/mhmdrz-hosseini/spider.git
cd spider

# 2. Install dependencies
pip install -r requirements.txt
playwright install chromium

# 3. Ensure FFmpeg is installed and added to PATH
# Windows: winget install Gyan.FFmpeg
# macOS:   brew install ffmpeg
# Ubuntu:  sudo apt-get install ffmpeg
```

---

## Quick Start

### 1. Download Single Reel / Post
```bash
python insta_downloader.py "https://www.instagram.com/reel/DeilynlS0YN/"
```

### 2. Download + Local AI Transcription
```bash
python insta_downloader.py "https://www.instagram.com/reel/DeilynlS0YN/" --transcribe
```

### 3. Batch Download from URL List
```bash
python insta_downloader.py -f recode_mind_20_urls.txt -o downloaded_reels
```

### 4. Harvest Channels via Playwright & Auto-Download
```bash
python download_channels.py
```

---

## Project Structure & Handover

For detailed architecture, benchmark records, and instructions on how to continue development on another machine, see [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md).

---

## License

MIT License.
