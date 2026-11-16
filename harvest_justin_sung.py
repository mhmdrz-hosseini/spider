"""
Dr. Justin Sung Study Reference Harvester & Knowledge Extractor
==============================================================
Harvests Dr. Justin Sung's deep-learning research videos, transcripts,
and visual pedagogical diagrams to power Fahva (P-03_fahva).

Workflow:
1. Queries curated Justin Sung videos (Cognitive Load, Mind Mapping, Rote Learning, Feynman).
2. Downloads metadata (.info.json) and audio/video streams via yt-dlp.
3. Extracts clean timestamped transcript JSONs.
4. Mirrors assets to:
   - `downloaded video/justinsung/`
   - `projects/P-03_fahva/research/justinsung/`
5. Compiles `justin_sung_pedagogy_matrix.md` linking Justin Sung principles
   directly to Fahva's 5 Sprint-01 scripts and product features.
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
PROJECT_DIR = WORKSPACE / "b2c-content-gtm-system" / "b2c-content-gtm-system" / "projects" / "P-03_fahva"
RESEARCH_DIR = PROJECT_DIR / "research" / "justinsung"
MIRROR_DIR = WORKSPACE / "downloaded video" / "justinsung"
COOKIES_PATH = WORKSPACE / "cookies.txt"
PROXY = "socks5h://127.0.0.1:10808"

# Curated high-impact study videos from Dr. Justin Sung for Fahva
CURATED_JUSTIN_SUNG_VIDEOS = [
    {
        "id": "-gqYldhjZVk",
        "title": "How to memorise (almost) anything you read in 20 minutes",
        "topic": "The 20-minute reading trap vs. structural encoding",
        "fahva_mapping": "CNT-001 (Summary Delusion)"
    },
    {
        "id": "umVX5wK6OZc",
        "title": "Why Critical Thinking Is Disappearing - The Rise of Effortless Education",
        "topic": "Effortless consumption, superficial cheat sheets, and cognitive atrophy",
        "fahva_mapping": "CNT-001 & Product Brief (Beachhead Problem)"
    },
    {
        "id": "rQHA7EYq8sw",
        "title": "The Hypothetical Structure Method - How to Think Like A Genius",
        "topic": "Non-linear structural mapping, 4-pillar conceptual geometry",
        "fahva_mapping": "CNT-003 (Tarh-e Koli Geometry & Mind Maps)"
    },
    {
        "id": "nIABz0Z4IRA",
        "title": "How to Learn So Fast People Assume You're Naturally Gifted",
        "topic": "Higher-order Bloom's taxonomy: analysis vs rote facts",
        "fahva_mapping": "CNT-004 (The Debater's Freeze & Verbatim Proof)"
    },
    {
        "id": "CQQTwvDb5xg",
        "title": "My Exact 14-Step Guide To Learn Anything Faster",
        "topic": "Self-questioning, cognitive schema, and Feynman explanation loops",
        "fahva_mapping": "CNT-005 (The Feynman Protocol for Dense Texts)"
    },
    {
        "id": "0Jpx6eNfpoo",
        "title": "In 32 Minutes, You'll Actually Understand Procrastination (and how to cure it)",
        "topic": "Cognitive friction, task aversion in heavy texts",
        "fahva_mapping": "Study Companion UX & Retention Funnels"
    }
]


def setup_directories():
    RESEARCH_DIR.mkdir(parents=True, exist_ok=True)
    MIRROR_DIR.mkdir(parents=True, exist_ok=True)


def download_video_and_transcript(v_meta: dict) -> bool:
    vid_id = v_meta["id"]
    title = v_meta["title"]
    url = f"https://www.youtube.com/watch?v={vid_id}"

    out_tmpl = RESEARCH_DIR / f"{vid_id}.%(ext)s"
    info_target = RESEARCH_DIR / f"{vid_id}.info.json"
    transcript_target = RESEARCH_DIR / f"{vid_id}_transcript.json"

    print(f"\n[JustinSung] [{vid_id}] {title}")
    print(f"  -> Fahva Target: {v_meta['fahva_mapping']}")

    # If already cached
    if transcript_target.exists():
        print("  [cache] Transcript and metadata already harvested.")
        for f in RESEARCH_DIR.glob(f"{vid_id}*"):
            shutil.copy2(f, MIRROR_DIR / f.name)
        return True

    cmd = [
        sys.executable, "-m", "yt_dlp",
        "--remote-components", "ejs:github",
        "--js-runtimes", "node",
        "--proxy", PROXY,
        "--cookies", str(COOKIES_PATH),
        "--format", "bestvideo[height<=720]+bestaudio/best[height<=720]/best",
        "--write-info-json",
        "--write-auto-subs",
        "--sub-lang", "en.*,en-orig",
        "--sub-format", "json3",
        "-o", str(out_tmpl),
        url
    ]

    print("  [yt-dlp] Downloading stream & subtitles...")
    ret = subprocess.run(cmd, capture_output=True, text=True)
    if ret.returncode != 0:
        err = ret.stderr.splitlines()[-1] if ret.stderr else "Unknown error"
        print(f"  [!] yt-dlp notice: {err}")

    # Look for downloaded subtitle file (.json3, .vtt, etc.)
    sub_files = list(RESEARCH_DIR.glob(f"{vid_id}*.json3")) + list(RESEARCH_DIR.glob(f"{vid_id}*.vtt"))
    if sub_files:
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
                        "topic": v_meta["topic"],
                        "fahva_mapping": v_meta["fahva_mapping"],
                        "full_text": complete_text,
                        "segments": segments
                    }, f, indent=2, ensure_ascii=False)
                txt_path = RESEARCH_DIR / f"{vid_id}_transcript.txt"
                txt_path.write_text(complete_text, encoding="utf-8")
                print(f"  [✓] Converted native subtitles to: {transcript_target.name}")
            except Exception as e:
                print(f"  [!] Subtitle parse error: {e}")

    # Mirror all generated files to downloaded video/justinsung/
    for f in RESEARCH_DIR.glob(f"{vid_id}*"):
        shutil.copy2(f, MIRROR_DIR / f.name)

    return True


def compile_pedagogy_matrix():
    matrix_file = PROJECT_DIR / "research" / "justin_sung_pedagogy_matrix.md"
    content = """# Dr. Justin Sung Pedagogical Reference Matrix — Fahva (P-03_fahva)

> **Authority Source:** Dr. Justin Sung (`@JustinSung` / iCanStudy)
> **Purpose:** Ground Fahva's product mechanics, motion-comic scripts, and interactive study companion in evidence-based cognitive psychology and deep learning science.

---

## 1. Core Learning Frameworks & Fahva Alignment

| Justin Sung Cognitive Principle | The Flaw in Conventional Study | Fahva Product Solution | Fahva Motion Comic Script |
|---|---|---|---|
| **Non-Linear Cognitive Schema** | Linear reading & note-taking treats knowledge as isolated sequential facts, causing catastrophic forgetting. | **Interactive Mental Map & Concept Graph:** Dynamic visualization linking themes, core doctrines, and arguments across the whole book. | **`CNT-003` (هندسه طرح کلی)**: Deconstructing the 4 pillars (Iman, Tawhid, Nubuwwat, Wilayat) as an interlocking gear system. |
| **The Illusion of Competence** | Passive re-reading, 15-minute book summaries, and audio cheat-sheets create familiarity without neural encoding. | **Authentic Text Interrogation:** Reader engages directly with authentic scanned PDF pages, breaking the passive summary habit. | **`CNT-001` (توهم دانایی)**: Exposing why 50 book summaries leave the mind powerless during a serious debate. |
| **Internal Encoding vs. Hallucination** | Outsourcing thought to generic AI bots that fabricate quotes and invent page numbers destroys academic trust. | **100% Verbatim Clickable Citations:** AI companion only asserts claims anchored with clickable, verbatim page proofs (`document <book> page <N>`). | **`CNT-002` (دادگاه استناد)**: Dramatizing a fake AI reference collapsing in an academic tribunal. |
| **Higher-Order Bloom's Analysis** | Rote memorization of slogans collapses under critical questioning. | **4-Tier Context Lens:** Instant transition from Selected Phrase $\\to$ Page $\\to$ Whole Book $\\to$ Verified Web Fallback. | **`CNT-004` (سکوت در مناظره)**: Speaker freezing when asked for the exact book page number. |
| **Socratic Gap Identification (Feynman)** | Assuming comprehension until asked to articulate the underlying mechanics in simple language. | **Guided Research & Learning Mode:** Voice/text Feynman explanation drills with instant feedback pinpointing conceptual gaps. | **`CNT-005` (پروتکل فاینمن)**: 4-step Feynman learning challenge applied to dense philosophical texts. |

---

## 2. Visual Storytelling & Asset Extraction Guidelines

1. **Mind Map HUD Overlays:** Use Justin Sung's radial and non-linear concept tree layouts as visual blueprints for Fahva's Parchment Gold (`#E5A93C`) HUD overlays.
2. **Cognitive Load Contrasts:** Split-screen comparison between chaotic highlighted notes (red warning `#D62828`) vs. structured relational blueprints (cyanotype `#0D1B2A` & gold `#E5A93C`).
3. **Pacing:** Pair calm, intellectual Socratic narration (`fa-IR-FaridNeural`) with 2.5D camera drift over authentic manuscript pages.
"""
    matrix_file.write_text(content, encoding="utf-8")
    print(f"\n[✓] Compiled Pedagogical Reference Matrix: {matrix_file.name}")


def main():
    setup_directories()
    print("=" * 60)
    print("🎓 Harvesting Dr. Justin Sung Study Reference Channel (@JustinSung)")
    print("=" * 60)

    for v in CURATED_JUSTIN_SUNG_VIDEOS:
        download_video_and_transcript(v)

    compile_pedagogy_matrix()
    print("\n✅ Harvest & Pedagogy Matrix Compilation Complete.")


if __name__ == "__main__":
    main()
