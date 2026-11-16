"""
Dr. Justin Sung Channel — Batch Offline Whisper Transcriber (10 Videos)
========================================================================
1. Extracts clean 16kHz MP3 audio from all 10 downloaded videos via FFmpeg.
2. Runs local AI speech-to-text transcription via `faster-whisper` (tiny.en, CPU int8).
3. Produces timestamped segment JSONs (_transcript.json) and formatted readable transcripts (_transcript.txt).
4. Mirrors all audio and transcript artifacts to:
   - `downloaded video/justinsung/`
   - `b2c-content-gtm-system/b2c-content-gtm-system/projects/P-03_fahva/research/justinsung/`
5. Outputs a full transcription benchmark report (speedup, words count, duration).
"""

import os
import sys
import json
import time
import shutil
import subprocess
from pathlib import Path
from faster_whisper import WhisperModel

# Ensure UTF-8 output on Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

WORKSPACE = Path(r"D:\code\SPIDER")
DOWNLOADS_DIR = WORKSPACE / "downloaded video" / "justinsung"
RESEARCH_DIR = WORKSPACE / "b2c-content-gtm-system" / "b2c-content-gtm-system" / "projects" / "P-03_fahva" / "research" / "justinsung"

# Ordered list of latest 10 videos
LATEST_10_IDS = [
    ("0Jpx6eNfpoo", "In 32 Minutes, You'll Actually Understand Procrastination (and how to cure it)"),
    ("-gqYldhjZVk", "How to memorise (almost) anything you read in 20 minutes"),
    ("R7jC6TUB8P4", "If You’re A Slow Learner, I’ll Help You Fix It In 17 Minutes"),
    ("3wLgRw6wpbM", "Give Me 18 Minutes, and You’ll Learn Faster Than 99.9% of People"),
    ("umVX5wK6OZc", "Why Critical Thinking Is Disappearing - The Rise of Effortless Education"),
    ("rQHA7EYq8sw", "The Hypothetical Structure Method - How to Think Like A Genius"),
    ("6Z3I-9HvBQA", "5 Thinking Habits That Make You Look Smarter"),
    ("nIABz0Z4IRA", "How to Learn So Fast People Assume You're Naturally Gifted"),
    ("KnyXpuhbgSc", "11 Tiny Habits To Learn and Think Like The Top 1%"),
    ("CQQTwvDb5xg", "My Exact 14-Step Guide To Learn Anything Faster"),
]


def extract_audio_ffmpeg(video_path: Path, mp3_path: Path) -> bool:
    """Extracts MP3 audio from video stream if not present."""
    if mp3_path.exists() and mp3_path.stat().st_size > 1000:
        return True

    cmd = [
        "ffmpeg", "-y",
        "-i", str(video_path),
        "-vn",
        "-acodec", "libmp3lame",
        "-q:a", "2",
        "-ar", "16000",
        "-ac", "1",
        str(mp3_path)
    ]
    res = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return res.returncode == 0 and mp3_path.exists()


def main():
    print("=" * 70)
    print("🎙️ Dr. Justin Sung (@JustinSung) — Batch AI Whisper Transcription")
    print("   Engine: faster-whisper (tiny.en, CPU int8, beam_size=5)")
    print("=" * 70)

    DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)
    RESEARCH_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Initialize Whisper Model
    print("\n[1/3] Loading faster-whisper tiny.en model...")
    t_load = time.time()
    model = WhisperModel("tiny.en", device="cpu", compute_type="int8")
    print(f"  [✓] Model loaded in {round(time.time() - t_load, 2)}s.\n")

    # 2. Process all 10 videos
    benchmark_records = []
    total_audio_seconds = 0.0
    total_transcribe_seconds = 0.0

    print("[2/3] Processing 10 videos...")
    for idx, (vid_id, title) in enumerate(LATEST_10_IDS, 1):
        print(f"\n[{idx}/10] {title} ({vid_id})")

        # Find video file in downloads or research
        vid_candidates = list(DOWNLOADS_DIR.glob(f"{vid_id}.*")) + list(RESEARCH_DIR.glob(f"{vid_id}.*"))
        vid_files = [f for f in vid_candidates if f.suffix in [".mp4", ".webm", ".mkv"]]

        if not vid_files:
            print(f"  [!] Video file not found for {vid_id}, skipping.")
            continue

        vid_path = vid_files[0]
        mp3_path = DOWNLOADS_DIR / f"{vid_id}.mp3"

        # Step A: Extract MP3
        print(f"  [ffmpeg] Extracting 16kHz mono audio from {vid_path.name}...")
        ok = extract_audio_ffmpeg(vid_path, mp3_path)
        if not ok:
            print(f"  [!] Failed to extract audio for {vid_id}")
            continue

        mp3_size_mb = round(mp3_path.stat().st_size / (1024 * 1024), 2)
        print(f"  [audio] Audio track ready: {mp3_path.name} ({mp3_size_mb} MB)")

        # Check if already transcribed with faster-whisper
        json_file_down = DOWNLOADS_DIR / f"{vid_id}_transcript.json"
        if json_file_down.exists():
            try:
                existing_data = json.loads(json_file_down.read_text(encoding="utf-8"))
                if existing_data.get("engine", "").startswith("faster-whisper"):
                    print(f"  [cache] Whisper transcript already exists for {vid_id} ({existing_data.get('word_count', 0):,} words)")
                    if (DOWNLOADS_DIR / mp3_path.name).exists() and not (RESEARCH_DIR / mp3_path.name).exists():
                        shutil.copy2(DOWNLOADS_DIR / mp3_path.name, RESEARCH_DIR / mp3_path.name)
                    shutil.copy2(json_file_down, RESEARCH_DIR / json_file_down.name)
                    txt_down = DOWNLOADS_DIR / f"{vid_id}_transcript.txt"
                    if txt_down.exists():
                        shutil.copy2(txt_down, RESEARCH_DIR / txt_down.name)
                    benchmark_records.append({
                        "index": idx,
                        "id": vid_id,
                        "title": title,
                        "audio_seconds": existing_data.get("audio_duration_seconds", 0),
                        "transcription_seconds": existing_data.get("transcription_time_seconds", 0),
                        "speedup": float(str(existing_data.get("speedup_ratio", "1")).rstrip("x")),
                        "words": existing_data.get("word_count", 0),
                        "segments": existing_data.get("total_segments", 0)
                    })
                    total_audio_seconds += existing_data.get("audio_duration_seconds", 0)
                    total_transcribe_seconds += existing_data.get("transcription_time_seconds", 0)
                    continue
            except Exception:
                pass

        # Step B: Transcribe with Whisper
        print(f"  [whisper] Running faster-whisper AI transcription...")
        t0 = time.time()
        segments_gen, info = model.transcribe(str(mp3_path), beam_size=5)

        full_sentences = []
        structured_segments = []
        for s in segments_gen:
            clean_text = s.text.strip()
            if clean_text:
                full_sentences.append(clean_text)
                structured_segments.append({
                    "id": s.id,
                    "start": round(s.start, 2),
                    "end": round(s.end, 2),
                    "text": clean_text
                })

        elapsed = round(time.time() - t0, 2)
        full_text = " ".join(full_sentences)
        word_count = len(full_text.split())
        audio_dur = round(info.duration, 2)
        speedup = round(audio_dur / elapsed, 1) if elapsed > 0 else 1.0

        total_audio_seconds += audio_dur
        total_transcribe_seconds += elapsed

        # Construct payload
        payload = {
            "video_id": vid_id,
            "title": title,
            "audio_file": mp3_path.name,
            "engine": "faster-whisper-tiny.en-int8",
            "audio_duration_seconds": audio_dur,
            "transcription_time_seconds": elapsed,
            "speedup_ratio": f"{speedup}x",
            "word_count": word_count,
            "total_segments": len(structured_segments),
            "full_text": full_text,
            "segments": structured_segments
        }

        # Save & mirror artifacts (avoid self-copy)
        if mp3_path.parent != RESEARCH_DIR:
            try:
                shutil.copy2(mp3_path, RESEARCH_DIR / mp3_path.name)
            except Exception as e:
                pass

        for target_dir in [DOWNLOADS_DIR, RESEARCH_DIR]:
            json_file = target_dir / f"{vid_id}_transcript.json"
            txt_file = target_dir / f"{vid_id}_transcript.txt"

            json_file.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
            txt_file.write_text(full_text, encoding="utf-8")

        print(f"  [✓] Complete in {elapsed}s (Audio: {audio_dur}s | {speedup}x speed) | Words: {word_count:,}")

        benchmark_records.append({
            "index": idx,
            "id": vid_id,
            "title": title,
            "audio_seconds": audio_dur,
            "transcription_seconds": elapsed,
            "speedup": speedup,
            "words": word_count,
            "segments": len(structured_segments)
        })

    # 3. Save benchmark summary
    overall_speedup = round(total_audio_seconds / total_transcribe_seconds, 1) if total_transcribe_seconds > 0 else 1.0
    summary = {
        "channel": "@JustinSung",
        "videos_processed": len(benchmark_records),
        "total_audio_duration_minutes": round(total_audio_seconds / 60, 2),
        "total_transcription_time_seconds": round(total_transcribe_seconds, 2),
        "overall_speedup_factor": f"{overall_speedup}x real-time",
        "total_words_extracted": sum(r["words"] for r in benchmark_records),
        "records": benchmark_records
    }

    for target_dir in [DOWNLOADS_DIR, RESEARCH_DIR]:
        b_path = target_dir / "transcription_benchmark_10.json"
        b_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

    print("\n" + "=" * 70)
    print("🎉 BATCH TRANSCRIPTION COMPLETED")
    print(f"Total Audio Duration:      {round(total_audio_seconds / 60, 1)} minutes")
    print(f"Total Processing Time:     {round(total_transcribe_seconds, 1)} seconds (~{overall_speedup}x real-time)")
    print(f"Total Words Extracted:     {summary['total_words_extracted']:,}")
    print("=" * 70)


if __name__ == "__main__":
    main()
