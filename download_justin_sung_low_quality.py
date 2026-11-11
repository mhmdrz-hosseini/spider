"""
Dr. Justin Sung Channel — Latest 10 Videos Batch Harvester (Low Quality)
=======================================================================
Downloads the latest 10 videos from https://www.youtube.com/@JustinSung in low quality (360p)
along with metadata (.info.json) and timestamped transcript JSONs.

Artifacts:
- MP4 / WebM video (360p Low Quality for fast indexing & plate extraction)
- .info.json metadata
- _transcript.json & _transcript.txt
- Mirrors to:
    1. `downloaded video/justinsung/`
    2. `b2c-content-gtm-system/b2c-content-gtm-system/projects/P-03_ketabyar/research/justinsung/`
"""

import os
import sys
import json
import shutil
import subprocess
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

WORKSPACE = Path(r"D:\code\SPIDER")
COOKIES_PATH = WORKSPACE / "cookies.txt"
PROXY = "socks5h://127.0.0.1:10808"

DEST_DIRS = [
    WORKSPACE / "downloaded video" / "justinsung",
    WORKSPACE / "b2c-content-gtm-system" / "b2c-content-gtm-system" / "projects" / "P-03_ketabyar" / "research" / "justinsung"
]

LATEST_10_VIDEOS = [
    {"index": 1, "id": "0Jpx6eNfpoo", "title": "In 32 Minutes, You'll Actually Understand Procrastination (and how to cure it)", "duration": "32:32"},
    {"index": 2, "id": "-gqYldhjZVk", "title": "How to memorise (almost) anything you read in 20 minutes", "duration": "20:13"},
    {"index": 3, "id": "R7jC6TUB8P4", "title": "If You’re A Slow Learner, I’ll Help You Fix It In 17 Minutes", "duration": "17:01"},
    {"index": 4, "id": "3wLgRw6wpbM", "title": "Give Me 18 Minutes, and You’ll Learn Faster Than 99.9% of People", "duration": "18:10"},
    {"index": 5, "id": "umVX5wK6OZc", "title": "Why Critical Thinking Is Disappearing - The Rise of Effortless Education", "duration": "11:27"},
    {"index": 6, "id": "rQHA7EYq8sw", "title": "The Hypothetical Structure Method - How to Think Like A Genius", "duration": "11:33"},
    {"index": 7, "id": "6Z3I-9HvBQA", "title": "5 Thinking Habits That Make You Look Smarter", "duration": "14:09"},
    {"index": 8, "id": "nIABz0Z4IRA", "title": "How to Learn So Fast People Assume You're Naturally Gifted", "duration": "8:23"},
    {"index": 9, "id": "KnyXpuhbgSc", "title": "11 Tiny Habits To Learn and Think Like The Top 1%", "duration": "19:44"},
    {"index": 10, "id": "CQQTwvDb5xg", "title": "My Exact 14-Step Guide To Learn Anything Faster", "duration": "27:11"},
]


def setup_directories():
    for d in DEST_DIRS:
        d.mkdir(parents=True, exist_ok=True)


def parse_subtitles(primary_dir: Path, vid_id: str, title: str) -> bool:
    transcript_target = primary_dir / f"{vid_id}_transcript.json"
    txt_target = primary_dir / f"{vid_id}_transcript.txt"

    sub_files = list(primary_dir.glob(f"{vid_id}*.json3")) + list(primary_dir.glob(f"{vid_id}*.vtt"))
    if not sub_files:
        return False

    sub_file = sub_files[0]
    if sub_file.suffix == ".json3":
        try:
            with open(sub_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            events = data.get("events", [])
            segments = []
            full_text = []
            for ev in events:
                segs = ev.get("segs", [])
                txt = "".join(s.get("utf8", "") for s in segs).strip()
                if txt and txt != "\n":
                    start_sec = round(ev.get("tStartMs", 0) / 1000, 2)
                    dur_sec = round(ev.get("dDurationMs", 0) / 1000, 2)
                    segments.append({
                        "start": start_sec,
                        "end": round(start_sec + dur_sec, 2),
                        "text": txt
                    })
                    full_text.append(txt)
            complete_text = " ".join(full_text).strip()
            with open(transcript_target, "w", encoding="utf-8") as f:
                json.dump({
                    "video_id": vid_id,
                    "title": title,
                    "full_text": complete_text,
                    "segments": segments
                }, f, indent=2, ensure_ascii=False)
            txt_target.write_text(complete_text, encoding="utf-8")
            print(f"  [✓] Subtitles parsed: {transcript_target.name}")
            return True
        except Exception as e:
            print(f"  [!] Subtitle parse error: {e}")
    return False


def process_video(item: dict) -> dict:
    idx = item["index"]
    vid_id = item["id"]
    title = item["title"]
    dur = item["duration"]
    url = f"https://www.youtube.com/watch?v={vid_id}"

    primary_dir = DEST_DIRS[1]
    mirror_dir = DEST_DIRS[0]

    out_tmpl = primary_dir / f"{vid_id}.%(ext)s"

    print(f"\n=======================================================")
    print(f"[{idx}/10] {title} ({dur})")
    print(f"URL: {url}")
    print(f"=======================================================")

    # Check if video file already exists in primary or mirror
    existing_videos = list(primary_dir.glob(f"{vid_id}.*")) + list(mirror_dir.glob(f"{vid_id}.*"))
    video_files = [f for f in existing_videos if f.suffix in [".mp4", ".webm", ".mkv"]]

    if video_files and (primary_dir / f"{vid_id}_transcript.json").exists():
        print(f"  [cache] Video & transcript already cached: {video_files[0].name} ({video_files[0].stat().st_size:,} bytes)")
        for f in primary_dir.glob(f"{vid_id}*"):
            shutil.copy2(f, mirror_dir / f.name)
        return {
            "id": vid_id,
            "title": title,
            "duration": dur,
            "file": video_files[0].name,
            "size_bytes": video_files[0].stat().st_size,
            "status": "cached"
        }

    # Low Quality format string: 360p MP4 or best format with height <= 360
    # 18 is 360p avc1+mp4a (typically 20-50MB)
    format_spec = "18/bestvideo[height<=360]+bestaudio/best[height<=360]/worst"

    cmd = [
        sys.executable, "-m", "yt_dlp",
        "--remote-components", "ejs:github",
        "--js-runtimes", "node",
        "--proxy", PROXY,
        "--cookies", str(COOKIES_PATH),
        "--format", format_spec,
        "--write-info-json",
        "--write-auto-subs",
        "--sub-lang", "en.*,en-orig",
        "--sub-format", "json3",
        "-o", str(out_tmpl),
        url
    ]

    print(f"  [yt-dlp] Downloading Low Quality (360p)...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        err = res.stderr.splitlines()[-1] if res.stderr else "Unknown error"
        print(f"  [!] yt-dlp error: {err}")

    parse_subtitles(primary_dir, vid_id, title)

    # Find the downloaded video file
    downloaded = list(primary_dir.glob(f"{vid_id}.*"))
    vid_file = None
    for f in downloaded:
        if f.suffix in [".mp4", ".webm", ".mkv"]:
            vid_file = f
            break

    file_size = vid_file.stat().st_size if vid_file else 0
    file_name = vid_file.name if vid_file else "none"

    if vid_file:
        print(f"  [✓] Downloaded: {file_name} ({file_size:,} bytes)")

    # Mirror all generated files to downloaded video/justinsung/
    for f in primary_dir.glob(f"{vid_id}*"):
        shutil.copy2(f, mirror_dir / f.name)

    return {
        "id": vid_id,
        "title": title,
        "duration": dur,
        "file": file_name,
        "size_bytes": file_size,
        "status": "downloaded" if vid_file else "failed"
    }


def main():
    setup_directories()
    print("=" * 65)
    print("📥 Dr. Justin Sung (@JustinSung) — Latest 10 Videos Batch Harvester")
    print("   Quality Target: LOW QUALITY (360p / Small File Size)")
    print("=" * 65)

    manifest_results = []
    for item in LATEST_10_VIDEOS:
        res = process_video(item)
        manifest_results.append(res)

    summary_file = DEST_DIRS[1] / "agent_reach_harvest_10_lowq.json"
    summary_file.write_text(json.dumps(manifest_results, indent=2, ensure_ascii=False), encoding="utf-8")
    shutil.copy2(summary_file, DEST_DIRS[0] / summary_file.name)

    print("\n" + "=" * 65)
    print("📊 BATCH HARVEST SUMMARY (10/10)")
    print("=" * 65)
    total_size = sum(r.get("size_bytes", 0) for r in manifest_results)
    for r in manifest_results:
        status_icon = "✅" if r["status"] in ["cached", "downloaded"] else "❌"
        print(f" {status_icon} [{r['id']}] {r['title'][:45]:<45} | {r['duration']:<7} | {r['size_bytes'] / (1024*1024):.1f} MB ({r['status']})")

    print(f"\nTotal Downloaded Volume: {total_size / (1024*1024):.1f} MB")
    print(f"Summary JSON saved: {summary_file}")


if __name__ == "__main__":
    main()
