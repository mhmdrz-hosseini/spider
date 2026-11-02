"""
Batch Offline Whisper Transcriber for Robert Tolone Channel
------------------------------------------------------------
Transcribes all 20 downloaded MP3 tracks using local faster-whisper.
Outputs clean punctuated transcripts (.txt) and timestamped segment JSONs (.json).
Mirrors results to both project research and downloaded video folders.
"""

import os
import sys
import json
import time
from pathlib import Path
from faster_whisper import WhisperModel

# Ensure UTF-8 output on Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

WORKSPACE = Path(__file__).resolve().parents[1]
RESEARCH_DIR = WORKSPACE / "b2c-content-gtm-system" / "b2c-content-gtm-system" / "projects" / "P-02_zerolab" / "research" / "roberttolone"
DOWNLOADS_DIR = WORKSPACE / "downloaded video" / "roberttolone"


def main():
    print("=" * 70)
    print("   Robert Tolone Channel Batch Whisper Transcription")
    print("   Engine: faster-whisper (tiny model, CPU int8)")
    print("=" * 70)

    mp3_files = sorted(list(DOWNLOADS_DIR.glob("*.mp3")))
    if not mp3_files:
        print("[!] No MP3 files found in", DOWNLOADS_DIR)
        sys.exit(1)

    print(f"[>] Found {len(mp3_files)} audio tracks to transcribe.")
    print("[>] Initializing faster-whisper model in memory...")
    t0 = time.time()
    model = WhisperModel("tiny", device="cpu", compute_type="int8")
    print(f"[✓] Model initialized in {round(time.time() - t0, 2)}s.\n")

    total_duration = 0.0
    total_processing_time = 0.0

    for idx, mp3_path in enumerate(mp3_files, 1):
        vid_id = mp3_path.stem
        print(f"[{idx}/{len(mp3_files)}] Transcribing: {vid_id}...")
        t_start = time.time()

        segments, info = model.transcribe(str(mp3_path), beam_size=5)

        full_sentences = []
        structured_segments = []
        for s in segments:
            clean_text = s.text.strip()
            if clean_text:
                full_sentences.append(clean_text)
                structured_segments.append({
                    "id": s.id,
                    "start": round(s.start, 2),
                    "end": round(s.end, 2),
                    "text": clean_text
                })

        elapsed = round(time.time() - t_start, 2)
        full_text = " ".join(full_sentences)
        total_duration += info.duration
        total_processing_time += elapsed

        # Construct transcript data
        payload = {
            "file": f"{vid_id}.mp4",
            "audio_file": mp3_path.name,
            "language": info.language,
            "audio_duration_seconds": round(info.duration, 2),
            "transcription_time_seconds": elapsed,
            "engine": "faster-whisper-tiny-int8",
            "total_segments": len(structured_segments),
            "full_text": full_text,
            "segments": structured_segments
        }

        # Save to both directories
        for target_dir in [RESEARCH_DIR, DOWNLOADS_DIR]:
            txt_file = target_dir / f"{vid_id}_transcript.txt"
            json_file = target_dir / f"{vid_id}_transcript.json"

            with open(txt_file, "w", encoding="utf-8") as f:
                f.write(full_text)

            with open(json_file, "w", encoding="utf-8") as f:
                json.dump(payload, f, indent=2, ensure_ascii=False)

        print(f"    [✓] Done in {elapsed}s (Audio: {round(info.duration, 1)}s) | Words: {len(full_text.split())} | Segments: {len(structured_segments)}")

    avg_speedup = round(total_duration / total_processing_time, 1) if total_processing_time > 0 else 0
    print("\n" + "=" * 70)
    print(f"Batch Transcription Completed!")
    print(f"Total Audio Processed: {round(total_duration / 60, 1)} minutes")
    print(f"Total Elapsed Time:    {round(total_processing_time, 1)} seconds (~{avg_speedup}x real-time)")
    print("=" * 70)


if __name__ == "__main__":
    main()
