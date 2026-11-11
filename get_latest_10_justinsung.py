import sys
import json
import subprocess
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

WORKSPACE = Path(r"D:\code\SPIDER")
COOKIES_PATH = WORKSPACE / "cookies.txt"
PROXY = "socks5h://127.0.0.1:10808"

cmd = [
    sys.executable, "-m", "yt_dlp",
    "--proxy", PROXY,
    "--cookies", str(COOKIES_PATH),
    "--flat-playlist",
    "--dump-json",
    "--playlist-end", "10",
    "https://www.youtube.com/@JustinSung/videos"
]

print("Fetching latest 10 videos from https://www.youtube.com/@JustinSung/videos...")
res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
lines = [l for l in res.stdout.strip().split("\n") if l.strip().startswith("{")]
print(f"Total entries retrieved: {len(lines)}")

videos = []
for idx, l in enumerate(lines, 1):
    try:
        d = json.loads(l)
        vid_info = {
            "index": idx,
            "id": d.get("id"),
            "title": d.get("title"),
            "url": f"https://www.youtube.com/watch?v={d.get('id')}",
            "duration": d.get("duration_string"),
            "view_count": d.get("view_count")
        }
        videos.append(vid_info)
        print(f"{idx}. [{d.get('id')}] {d.get('title')} ({d.get('duration_string')})")
    except Exception as e:
        print(f"Error parsing line {idx}: {e}")

out_path = WORKSPACE / "downloaded video" / "justinsung" / "agent_reach_harvest_latest_10.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(videos, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"\nSaved metadata to: {out_path}")
