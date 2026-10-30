# Spider: Project Context & Handover Guide

> **Note for AI Assistant on the other device**: This file contains the complete operational context, codebase architecture, benchmark history, and instructions to resume work on this project seamlessly without missing a beat.

---

## 1. Project Overview & Mission

**Spider** is a high-performance Python toolkit designed for automated harvesting, downloading, extracting, and transcribing social media video content—with primary focus on **Instagram Reels** and **YouTube content**.

### Key Capabilities
- **Zero-API Instagram Scraper**: Uses headless Playwright to monitor network GraphQL responses and intercept post/reel shortcodes directly from channel pages, bypassing client-side login walls and anti-bot overlays.
- **Robust Multi-Stream Downloader**: Powered by `yt-dlp` and `ffmpeg`, extracts the highest-resolution MP4 video, separates high-quality MP3 audio tracks, outputs structured metadata JSON (`.info.json`), and grabs keyframe thumbnails.
- **100% Free Offline Speech-to-Text**: Integrated local transcription using OpenAI Whisper (running on CPU with PyTorch), generating both plain-text transcripts and timestamped segment JSONs with zero API costs.
- **Automated Batch Processing & Benchmarking**: Scripts to pull 20+ videos from specified accounts, measure throughput, retry transient errors, and generate structured benchmark analytics.

---

## 2. Repository & Device Handover

- **GitHub Repository**: `https://github.com/mhmdrz-hosseini/spider.git`
- **Current Branch**: `main`
- **Target Continuation Device**: Windows / Linux / macOS with Python 3.10+ and FFmpeg.

### 📋 Prompt to Paste into the New Chat on Your Other Device:
```text
I am continuing work on the "Spider" project cloned from https://github.com/mhmdrz-hosseini/spider.git.
Please inspect PROJECT_CONTEXT.md in the root directory to get full context on the existing scripts (insta_downloader.py, download_channels.py, batch_download_20.py, transcribe_reel.py, etc.) and benchmark results. We are ready to continue development.
```

---

## 3. Directory Layout & File Manifest

| File / Folder | Role & Description |
|---|---|
| `insta_downloader.py` | **Core downloader engine & CLI**. Downloads MP4 videos, extracts MP3 audio via FFmpeg, dumps `.info.json` metadata, extracts keyframes, and invokes Whisper speech-to-text. |
| `download_channels.py` | **Multi-channel harvester & downloader**. Automates scraping reels from multiple accounts (e.g., `@gordol.tips`, `@swolotips`) via Playwright GraphQL capture and downloads them into structured folders. |
| `batch_download_20.py` | **Batch downloader & benchmarking script**. Processes the first 20 URLs from `recode_mind_20_urls.txt`, logs execution time, file sizes, and generates JSON benchmark reports. |
| `run_all_20.py` | **Production-grade batch runner**. Features a 3-attempt retry loop per video, cache detection to prevent duplicate downloads, and comprehensive benchmark reporting. |
| `scrape_reels.py` | **Playwright URL harvester**. Emulates human scrolling on Instagram channel `/reels/` pages and extracts reel links into a clean list. |
| `transcribe_reel.py` | **Standalone Speech-to-Text transcriber**. Runs local Whisper (`tiny` or `base` model) on CPU. Outputs `_transcript.txt` and timestamped `_transcript.json`. |
| `test_yt_transcript.py` | **Direct YouTube transcript extractor**. Fetches and decodes native YouTube timed text (`captionTracks`) via urllib without API keys. |
| `recode_mind_20_urls.txt` | Clean URL list of 20 reels harvested from `@recode_mind_`. |
| `benchmark_results.json` | First pass benchmark data of downloaded reels. |
| `final_20_reels_benchmark.json` | Comprehensive final benchmark report for 20 reels: 100% success rate, timing, and storage metrics. |
| `motion_comic_pipeline_architecture-v2.md` | **System Architecture & Pipeline Spec (v2.0)**: Complete blueprint for the automated 0% I2V "Engineered Motion Comic" production engine (narrative bridge, state-locked scenes, 2.5D camera choreography, Foley design). |
| `skill/channel_to_persian_brand_skill.md` | **Channel to Persian Brand Skill**: Strategic workflow for reverse-engineering foreign short-form channels and localizing content for Persian brand identity and retention funnels. |
| `requirements.txt` | Python library requirements (`yt-dlp`, `playwright`, `openai-whisper`, `torch`, `torchaudio`). |
| `.gitignore` | Excludes downloaded media files (`.mp4`, `.mp3`), `__pycache__`, virtual environments, and external sub-repos. |
| `Agent-Reach/` | External cloned submodule/tool repository for web & agent automation. |
| `rea/` | External cloned reverse engineering & MCP analysis tool suite. |

---

## 4. Empirical Benchmark Results

During testing on Instagram channel `@recode_mind_`:
- **Total Reels Tested**: 20
- **Success Rate**: **100% (20/20)**
- **Total Download Time**: **3 minutes 52 seconds (232.83s)**
- **Average Time per Reel**: ~11.6 seconds
- **Total MP4 Video Volume**: 227.88 MB
- **Total MP3 Audio Volume**: 16.24 MB
- **Tested Channels**:
  - `@recode_mind_` (20 reels)
  - `@gordol.tips` (5 reels)
  - `@swolotips` (5 reels)

---

## 5. Prerequisites & Environment Setup

### 1. System Requirements
- **Python**: Version 3.10, 3.11, or 3.12 recommended.
- **FFmpeg**: Must be installed and present on your system `PATH` (used for audio extraction and keyframes).
  - *Windows*: `winget install Gyan.FFmpeg` or `choco install ffmpeg`
  - *macOS*: `brew install ffmpeg`
  - *Ubuntu/Debian*: `sudo apt-get install ffmpeg`

### 2. Python Dependencies
```bash
# Clone the repository
git clone https://github.com/mhmdrz-hosseini/spider.git
cd spider

# Create and activate virtual environment (optional but recommended)
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Install Playwright browser binaries
playwright install chromium
```

---

## 6. CLI Usage Cheat Sheet

### Download a Single Reel (Video + Audio + Metadata)
```bash
python insta_downloader.py "https://www.instagram.com/reel/DeilynlS0YN/"
```

### Download and Transcribe with Whisper (Local CPU)
```bash
python insta_downloader.py "https://www.instagram.com/reel/DeilynlS0YN/" --transcribe
```

### Download Reels from a Text File
```bash
python insta_downloader.py -f recode_mind_20_urls.txt -o downloaded_reels
```

### Batch Harvest & Download from Specific Channels
```bash
python download_channels.py
```

### Standalone Transcribe an Audio or Video File
```bash
python transcribe_reel.py "downloaded_videos/sample.mp4" --model tiny
```

---

## 7. Next Steps & Ideas for the Project
1. **Concurrency / Async Queue**: Implement multi-threaded or `asyncio` parallel downloads with rate-limiting to download 20 reels in < 45 seconds.
2. **Database / SQLite Store**: Replace standalone JSON files with an SQLite or DuckDB metadata store to query reels by hashtags, duration, or view count.
3. **Web UI / Dashboard**: Build a lightweight FastAPI or Gradio frontend to paste URLs, watch downloads progress live, and search video transcripts.
4. **Proxy Support & Session Rotation**: Add proxy cycling support to `insta_downloader.py` and `download_channels.py` for large-scale scrapers.
