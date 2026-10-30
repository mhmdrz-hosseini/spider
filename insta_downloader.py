"""
Instagram Reel MP4 & MP3 Downloader
------------------------------------
Based on yt-dlp & ffmpeg stream extraction.
Downloads high-definition video (MP4), extracted audio track (MP3),
and complete metadata (JSON) for any public Instagram Reel or post.

Usage:
    python insta_downloader.py <URL_OR_SHORTCODE> [options]

Examples:
    # Download MP4, MP3, and JSON metadata
    python insta_downloader.py "https://www.instagram.com/reel/DeilynlS0YN/"

    # Download multiple reels
    python insta_downloader.py "https://www.instagram.com/reel/DeilynlS0YN/" "https://www.instagram.com/reel/DeW9fzti6Tu/"

    # Download from a text file containing links
    python insta_downloader.py -f links.txt

    # Audio only (MP3)
    python insta_downloader.py "https://www.instagram.com/reel/DeilynlS0YN/" --audio-only

    # Video only (MP4)
    python insta_downloader.py "https://www.instagram.com/reel/DeilynlS0YN/" --video-only

    # Extract keyframes as well
    python insta_downloader.py "https://www.instagram.com/reel/DeilynlS0YN/" --frames
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def check_dependencies():
    """Verify yt-dlp and ffmpeg are available."""
    missing = []
    try:
        import yt_dlp
    except ImportError:
        missing.append("yt-dlp (run: python -m pip install yt-dlp)")

    if shutil.which("ffmpeg") is None:
        missing.append("ffmpeg (ensure ffmpeg is installed and added to PATH)")

    if missing:
        print("\n[ERROR] Missing dependencies:")
        for item in missing:
            print(f"  - {item}")
        sys.exit(1)


def normalize_instagram_url(raw_url: str) -> str:
    """Extract clean Instagram post/reel URL from dirty links with tracking parameters."""
    raw_url = raw_url.strip()
    match = re.search(r'(?:instagram\.com/(?:reel|p|reels)/|)([A-Za-z0-9_-]{11})', raw_url)
    if match:
        shortcode = match.group(1)
        return f"https://www.instagram.com/reel/{shortcode}/", shortcode
    # Fallback to stripped URL
    clean = raw_url.split("?")[0].rstrip("/") + "/"
    shortcode = clean.split("/")[-2] if "/" in clean else "instagram_video"
    return clean, shortcode


def download_reel(
    url: str,
    output_dir: str = "downloads",
    get_video: bool = True,
    get_audio: bool = True,
    get_metadata: bool = True,
    get_frames: bool = False,
    do_transcribe: bool = False,
    verbose: bool = False
):
    """Download video, extract MP3, write metadata, and optionally extract frames or transcribe."""
    import yt_dlp

    clean_url, shortcode = normalize_instagram_url(url)
    os.makedirs(output_dir, exist_ok=True)

    print(f"\n=======================================================")
    print(f"[>] Processing: {clean_url} (Shortcode: {shortcode})")
    print(f"=======================================================")

    base_output_template = os.path.join(output_dir, f"{shortcode}")

    # Configure yt-dlp extraction options
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': f"{base_output_template}.%(ext)s",
        'quiet': not verbose,
        'no_warnings': True,
        'socket_timeout': 30,
        'retries': 5,
        'extractor_retries': 3,
    }

    info_data = None
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("[1/4] Extracting media stream links...")
            info_data = ydl.extract_info(clean_url, download=get_video)

        mp4_path = f"{base_output_template}.mp4"

        # Check if downloaded file ended up with a slightly different extension
        if not os.path.exists(mp4_path):
            for ext in [".mp4", ".mkv", ".webm"]:
                candidate = f"{base_output_template}{ext}"
                if os.path.exists(candidate):
                    mp4_path = candidate
                    break

        if get_video and os.path.exists(mp4_path):
            print(f"[OK] MP4 Video saved: {mp4_path} ({os.path.getsize(mp4_path):,} bytes)")

        mp3_path = f"{base_output_template}.mp3"
        # Step 2: Extract MP3
        if (get_audio or do_transcribe) and os.path.exists(mp4_path):
            print("[2/4] Extracting high-quality MP3 audio track...")
            cmd = [
                "ffmpeg", "-y", "-i", mp4_path,
                "-vn", "-acodec", "libmp3lame", "-q:a", "2",
                mp3_path
            ]
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if os.path.exists(mp3_path):
                print(f"[OK] MP3 Audio saved: {mp3_path} ({os.path.getsize(mp3_path):,} bytes)")

        # Step 3: Write metadata JSON
        if get_metadata and info_data:
            json_path = f"{base_output_template}.info.json"
            print("[3/4] Writing metadata JSON...")
            clean_meta = {
                "id": info_data.get("id"),
                "shortcode": shortcode,
                "url": clean_url,
                "title": info_data.get("title"),
                "description": info_data.get("description"),
                "uploader": info_data.get("uploader"),
                "uploader_id": info_data.get("uploader_id"),
                "channel": info_data.get("channel"),
                "timestamp": info_data.get("timestamp"),
                "upload_date": info_data.get("upload_date"),
                "duration": info_data.get("duration"),
                "view_count": info_data.get("view_count"),
                "like_count": info_data.get("like_count"),
                "comment_count": info_data.get("comment_count"),
                "width": info_data.get("width"),
                "height": info_data.get("height"),
                "fps": info_data.get("fps"),
            }
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(clean_meta, f, indent=2, ensure_ascii=False)
            print(f"[OK] Metadata saved:  {json_path}")

        # Step 4: Extract Keyframes (Optional)
        if get_frames and os.path.exists(mp4_path):
            frames_dir = os.path.join(output_dir, f"{shortcode}_frames")
            os.makedirs(frames_dir, exist_ok=True)
            print(f"[4/4] Extracting sample frames to: {frames_dir}...")
            timestamps = [1, 5, 10, 20]
            for sec in timestamps:
                out_frame = os.path.join(frames_dir, f"frame_{sec}s.jpg")
                cmd = ["ffmpeg", "-y", "-ss", str(sec), "-i", mp4_path, "-frames:v", "1", "-q:v", "2", out_frame]
                subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"[OK] Frames saved:    {len(os.listdir(frames_dir))} image(s)")

        # Step 5: Free Local Speech-to-Text Transcription (Optional)
        if do_transcribe and os.path.exists(mp3_path):
            print("[5/5] Transcribing audio with Whisper (free, local CPU)...")
            try:
                import whisper
                model = whisper.load_model("tiny")
                res = model.transcribe(mp3_path, fp16=False)
                txt_path = f"{base_output_template}_transcript.txt"
                with open(txt_path, "w", encoding="utf-8") as f:
                    f.write(res.get("text", "").strip())
                print(f"[OK] Transcript saved: {txt_path}")
            except Exception as te:
                print(f"[!] Transcription error: {te}")

        print(f"[DONE] Successfully processed {shortcode}!\n")
        return True

    except Exception as e:
        print(f"[!] Error processing {url}: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Fast Instagram Reel & Post Downloader (MP4 + MP3 + Metadata)"
    )
    parser.add_argument(
        "urls",
        nargs="*",
        help="One or more Instagram Reel URLs or shortcodes"
    )
    parser.add_argument(
        "-f", "--file",
        help="Path to a text file containing Instagram URLs (one per line)"
    )
    parser.add_argument(
        "-o", "--output-dir",
        default="downloaded_reels",
        help="Target folder to save downloaded media (default: downloaded_reels)"
    )
    parser.add_argument(
        "--video-only",
        action="store_true",
        help="Download only MP4 video (skip MP3 extraction)"
    )
    parser.add_argument(
        "--audio-only",
        action="store_true",
        help="Keep only MP3 audio (delete intermediate MP4)"
    )
    parser.add_argument(
        "--no-metadata",
        action="store_true",
        help="Skip writing .info.json metadata file"
    )
    parser.add_argument(
        "--frames",
        action="store_true",
        help="Extract keyframes from the video for thumbnail/visual inspection"
    )
    parser.add_argument(
        "--transcribe",
        action="store_true",
        help="Free local Speech-to-Text transcription with Whisper (saves _transcript.txt)"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output"
    )

    args = parser.parse_args()
    check_dependencies()

    all_urls = list(args.urls) if args.urls else []
    if args.file and os.path.exists(args.file):
        with open(args.file, "r", encoding="utf-8") as f:
            for line in f:
                stripped = line.strip()
                if stripped and not stripped.startswith("#"):
                    all_urls.append(stripped)

    if not all_urls:
        parser.print_help()
        print("\n[!] Please provide at least one URL or a file with -f.")
        sys.exit(1)

    get_video = not args.audio_only
    get_audio = not args.video_only
    get_meta = not args.no_metadata

    successful = 0
    for u in all_urls:
        ok = download_reel(
            url=u,
            output_dir=args.output_dir,
            get_video=get_video,
            get_audio=get_audio,
            get_metadata=get_meta,
            get_frames=args.frames,
            do_transcribe=args.transcribe,
            verbose=args.verbose
        )
        if ok:
            successful += 1

    print("-------------------------------------------------------")
    print(f"Summary: {successful}/{len(all_urls)} Reel(s) successfully downloaded.")
    print(f"Destination: {os.path.abspath(args.output_dir)}")
    print("-------------------------------------------------------")


if __name__ == "__main__":
    main()
