"""
Free Local Audio & Video Transcriber (Whisper)
-----------------------------------------------
100% free, local, open-source Speech-to-Text with Whisper.
Runs completely offline on your CPU with zero API costs.

Usage:
    python transcribe_reel.py <PATH_TO_AUDIO_OR_VIDEO> [options]

Examples:
    python transcribe_reel.py "downloaded_videos/instagram_reel_1.mp3"
    python transcribe_reel.py "downloaded_videos/instagram_reel_2_crab_mentality.mp4"
    python transcribe_reel.py "downloaded_videos/instagram_reel_1.mp3" --model base
"""

import argparse
import json
import os
import sys
import time
import warnings

# Suppress PyTorch storage warnings
warnings.filterwarnings("ignore")

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def transcribe(file_path: str, model_name: str = "tiny", save_output: bool = True):
    if not os.path.exists(file_path):
        print(f"[!] File not found: {file_path}")
        return None

    import whisper

    print(f"\n=======================================================")
    print(f"[>] Transcribing: {os.path.basename(file_path)}")
    print(f"[>] Engine: Whisper ({model_name} model, running locally on CPU)")
    print(f"=======================================================")

    t0 = time.time()
    print("[1/2] Loading Whisper model into memory...")
    model = whisper.load_model(model_name)

    print("[2/2] Processing speech recognition...")
    result = model.transcribe(file_path, fp16=False)
    elapsed = round(time.time() - t0, 2)

    full_text = result.get("text", "").strip()
    detected_lang = result.get("language", "unknown")
    segments = result.get("segments", [])

    print(f"\n[OK] Completed in {elapsed}s | Detected Language: {detected_lang.upper()}")
    print("-" * 60)
    print(full_text)
    print("-" * 60)

    if save_output:
        base_name = os.path.splitext(file_path)[0]
        txt_path = f"{base_name}_transcript.txt"
        json_path = f"{base_name}_transcript.json"

        # Save plain text
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(full_text)

        # Save structured timestamps
        structured = {
            "file": os.path.basename(file_path),
            "language": detected_lang,
            "duration_processed": elapsed,
            "full_text": full_text,
            "segments": [
                {
                    "start": round(s["start"], 2),
                    "end": round(s["end"], 2),
                    "text": s["text"].strip()
                }
                for s in segments
            ]
        }
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(structured, f, indent=2, ensure_ascii=False)

        print(f"[✓] Saved text:       {txt_path}")
        print(f"[✓] Saved timestamps: {json_path}")

    return result


def main():
    parser = argparse.ArgumentParser(description="Free Local Video/Audio Transcriber")
    parser.add_argument("media_file", help="Path to video (.mp4) or audio (.mp3, .m4a, .wav)")
    parser.add_argument(
        "--model",
        default="tiny",
        choices=["tiny", "base", "small", "medium"],
        help="Whisper model size (default: tiny - fastest; base - slightly more accurate)"
    )
    parser.add_argument("--no-save", action="store_true", help="Do not save output text/json files")

    args = parser.parse_args()
    transcribe(args.media_file, model_name=args.model, save_output=not args.no_save)


if __name__ == "__main__":
    main()
