"""
Robert Tolone Channel Batch Harvester & Downloader
--------------------------------------------------
Automated evidence harvesting pipeline for Robert Tolone reference videos:
1. Downloads video streams (MP4) and metadata JSON (.info.json) via yt-dlp.
2. Extracts high-quality audio (MP3) via FFmpeg.
3. Downloads native subtitles or transcribes via faster-whisper.
4. Mirrors output to both 'downloaded video/roberttolone' and 'P-02_zerolab/research/roberttolone'.
"""

import os
import sys
import json
import time
import shutil
import subprocess
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

WORKSPACE = Path(__file__).resolve().parents[1]
DEST_DIRS = [
    WORKSPACE / "downloaded video" / "roberttolone",
    WORKSPACE / "b2c-content-gtm-system" / "b2c-content-gtm-system" / "projects" / "P-02_zerolab" / "research" / "roberttolone"
]

# Curated 20 videos from Robert Tolone
CURATED_20_VIDEOS = [
    {"id": "Hd-UtmKsiss", "title": "Break It Down - Casting Complicated Objects", "duration": "7:42"},
    {"id": "MUdI08TQJTk", "title": "Simple Mold, Complex Casting", "duration": "5:23"},
    {"id": "vhK7WjuFl-o", "title": "Which One To Use, When, How? WHY IS THIS SO HARD? !!!", "duration": "11:09"},
    {"id": "7IT0zf9obFU", "title": "Casting An Object With Holes - HOW ???", "duration": "14:40"},
    {"id": "MuxynPYpy0c", "title": "Tips And Tricks For Making Miniatures", "duration": "21:12"},
    {"id": "eV8J3r36xhI", "title": "Casting A Tiny Car Body", "duration": "37:20"},
    {"id": "wDLWaWZwNm8", "title": "Silicone Mold Making: When To Use A Two-Piece Mold. Part 1", "duration": "31:56"},
    {"id": "TOFZsPmJI2E", "title": "150 Urethane Resin Castings - How To Make A LOT of copies fast!", "duration": "20:31"},
    {"id": "VYO318KFuAA", "title": "All You Need To Know!", "duration": "6:35"},
    {"id": "NnEqHqzceKc", "title": "Squish Molds! A Collaboration With The Crafsman!", "duration": "6:14"},
    {"id": "J-2g6e5Tv-g", "title": "No Matter What Position, Size Matters", "duration": "8:22"},
    {"id": "qDLgTtQybiQ", "title": "Top Ten Tools For A Resin Casting Studio", "duration": "7:08"},
    {"id": "xmlJe5oeYbI", "title": "Sealing Foam Sculptures for Molding", "duration": "9:40"},
    {"id": "6LlXG1aFKr4", "title": "3D Printed Molds For Resin Casting - Does That Even Work?", "duration": "9:32"},
    {"id": "rKWQ0GTNxnk", "title": "Robert Tolone Channel Trailer", "duration": "2:01"},
    {"id": "Rw1NzWHwqH8", "title": "Silicone Rubber Cut Molds: Faster, Cheaper and SO MUCH BETTER", "duration": "18:20"},
    {"id": "3Pvg1tM7TWE", "title": "Everything You Always Wanted To Know About Wax", "duration": "11:14"},
    {"id": "guOcdN_pQ9o", "title": "Why I Dont Use Mold Release", "duration": "10:06"},
    {"id": "NmrAm6h8jzU", "title": "But No Bubbles! Part 1", "duration": "28:26"},
    {"id": "1qOwem_ll68", "title": "Silicone Mold Making - Three Different Ways", "duration": "33:42"},
]


def setup_directories():
    for d in DEST_DIRS:
        d.mkdir(parents=True, exist_ok=True)
    urls_file = DEST_DIRS[1] / "urls.txt"
    with open(urls_file, "w", encoding="utf-8") as f:
        for v in CURATED_20_VIDEOS:
            f.write(f"https://www.youtube.com/watch?v={v['id']}\n")
    print(f"[✓] Setup output directories and saved {len(CURATED_20_VIDEOS)} URLs.")


def convert_subtitle_to_transcript_json(sub_file: Path, out_base: Path):
    """Convert downloaded json3, vtt or srt subtitle into standard _transcript.json."""
    json_target = out_base.with_name(f"{out_base.stem}_transcript.json")
    txt_target = out_base.with_name(f"{out_base.stem}_transcript.txt")
    if json_target.exists() and txt_target.exists():
        return True

    try:
        if sub_file.suffix == ".json3":
            with open(sub_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            events = data.get("events", [])
            segments = []
            full_text = []
            for ev in events:
                segs = ev.get("segs", [])
                text = "".join(s.get("utf8", "") for s in segs).strip()
                if text and text != "\n":
                    start_sec = round(ev.get("tStartMs", 0) / 1000, 2)
                    dur_sec = round(ev.get("dDurationMs", 0) / 1000, 2)
                    segments.append({
                        "start": start_sec,
                        "end": round(start_sec + dur_sec, 2),
                        "text": text
                    })
                    full_text.append(text)
            
            complete_text = " ".join(full_text).strip()
            with open(txt_target, "w", encoding="utf-8") as f:
                f.write(complete_text)
            with open(json_target, "w", encoding="utf-8") as f:
                json.dump({
                    "file": f"{out_base.stem}.mp4",
                    "language": "en",
                    "source": "youtube_captions",
                    "full_text": complete_text,
                    "segments": segments
                }, f, indent=2, ensure_ascii=False)
            print(f"  [subtitles] Converted YouTube captions to: {json_target.name}")
            return True
    except Exception as e:
        print(f"  [!] Subtitle conversion error: {e}")
    return False


def transcribe_fallback(audio_path: Path, output_base: Path):
    """Fallback local transcription using faster-whisper."""
    json_path = output_base.with_name(f"{output_base.stem}_transcript.json")
    txt_path = output_base.with_name(f"{output_base.stem}_transcript.txt")
    if json_path.exists() and txt_path.exists():
        return True

    try:
        from faster_whisper import WhisperModel
        print(f"  [whisper] Transcribing {audio_path.name} via faster-whisper (tiny model, CPU)...")
        model = WhisperModel("tiny", device="cpu", compute_type="int8")
        segments, info = model.transcribe(str(audio_path), beam_size=5)

        full_text = []
        structured_segments = []
        for s in segments:
            full_text.append(s.text.strip())
            structured_segments.append({
                "start": round(s.start, 2),
                "end": round(s.end, 2),
                "text": s.text.strip()
            })

        complete_text = " ".join(full_text).strip()
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(complete_text)

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump({
                "file": audio_path.name,
                "language": info.language,
                "duration": round(info.duration, 2),
                "full_text": complete_text,
                "segments": structured_segments
            }, f, indent=2, ensure_ascii=False)

        print(f"  [✓] Whisper transcript saved: {json_path.name}")
        return True
    except Exception as e:
        print(f"  [!] Whisper transcription error: {e}")
        return False


def process_video(video_meta: dict, cookies_path: str, proxy: str = "socks5h://127.0.0.1:10808"):
    vid_id = video_meta["id"]
    title = video_meta["title"]
    url = f"https://www.youtube.com/watch?v={vid_id}"
    primary_dir = DEST_DIRS[1]  # project research dir
    mirror_dir = DEST_DIRS[0]   # downloaded video dir

    out_template = primary_dir / f"{vid_id}.%(ext)s"
    mp4_target = primary_dir / f"{vid_id}.mp4"
    mp3_target = primary_dir / f"{vid_id}.mp3"
    info_target = primary_dir / f"{vid_id}.info.json"
    transcript_target = primary_dir / f"{vid_id}_transcript.json"

    print(f"\n[{vid_id}] {title} ({video_meta['duration']})")

    # If already fully processed, skip
    if mp4_target.exists() and mp3_target.exists() and transcript_target.exists():
        print(f"  [cache] All artifacts already exist for {vid_id}")
        for f in primary_dir.glob(f"{vid_id}*"):
            shutil.copy2(f, mirror_dir / f.name)
        return True

    cmd = [
        sys.executable, "-m", "yt_dlp",
        "--remote-components", "ejs:github",
        "--js-runtimes", "node",
        "--proxy", proxy,
        "--cookies", cookies_path,
        "--format", "bestvideo[height<=720]+bestaudio/best[height<=720]/best",
        "--write-info-json",
        "--write-auto-subs",
        "--sub-lang", "en.*,en-orig",
        "--sub-format", "json3",
        "-o", str(out_template),
        url
    ]

    print(f"  [yt-dlp] Downloading stream & metadata...")
    ret = subprocess.run(cmd, capture_output=True, text=True)
    if ret.returncode != 0:
        err_msg = ret.stderr.splitlines()[-1] if ret.stderr else "Unknown error"
        print(f"  [!] yt-dlp error: {err_msg}")
        return False

    # Check for downloaded video file
    for cand in primary_dir.glob(f"{vid_id}.*"):
        if cand.suffix in [".mp4", ".mkv", ".webm"]:
            if cand.suffix != ".mp4":
                print(f"  [ffmpeg] Remuxing {cand.suffix} to .mp4...")
                subprocess.run(["ffmpeg", "-y", "-i", str(cand), "-c", "copy", str(mp4_target)],
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                cand.unlink(missing_ok=True)
            break

    # Extract MP3 audio
    if mp4_target.exists() and not mp3_target.exists():
        print(f"  [ffmpeg] Extracting high-quality MP3 audio track...")
        subprocess.run([
            "ffmpeg", "-y", "-i", str(mp4_target),
            "-vn", "-acodec", "libmp3lame", "-q:a", "2",
            str(mp3_target)
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Subtitles to transcript
    json3_subs = list(primary_dir.glob(f"{vid_id}*.json3"))
    transcript_done = False
    if json3_subs:
        transcript_done = convert_subtitle_to_transcript_json(json3_subs[0], primary_dir / vid_id)

    # If no subtitles, run Whisper
    if not transcript_done and mp3_target.exists():
        transcribe_fallback(mp3_target, primary_dir / vid_id)

    # Mirror all generated artifacts to downloaded video directory
    for f in primary_dir.glob(f"{vid_id}*"):
        shutil.copy2(f, mirror_dir / f.name)

    print(f"  [✓] Complete: {vid_id} artifacts verified.")
    return True


def main():
    print("=" * 70)
    print("   Robert Tolone Channel Batch Harvester")
    print("   Target: 20 Benchmark Videos for ZeroLab (P-02_zerolab)")
    print("=" * 70)

    setup_directories()

    cookies_path = str(WORKSPACE / "cookies.txt")
    if not os.path.exists(cookies_path):
        print(f"[!] cookies.txt not found at {cookies_path}")
        sys.exit(1)

    print(f"[auth] Using cookies: {cookies_path} ({os.path.getsize(cookies_path):,} bytes)")

    success_count = 0
    total = len(CURATED_20_VIDEOS)
    t_start = time.time()

    for idx, v in enumerate(CURATED_20_VIDEOS, 1):
        print(f"\n({idx}/{total}) -> Processing: {v['title']}")
        if process_video(v, cookies_path=cookies_path):
            success_count += 1
        time.sleep(1)

    elapsed = round(time.time() - t_start, 1)
    print("\n" + "=" * 70)
    print(f"Batch Finished in {elapsed}s: {success_count}/{total} videos processed successfully.")
    print("=" * 70)


if __name__ == "__main__":
    main()
