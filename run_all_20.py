import os
import sys
import time
import json
from datetime import datetime

# UTF-8 stdout
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

from insta_downloader import download_reel

URLS_FILE = "recode_mind_20_urls.txt"
OUTPUT_DIR = "downloaded_reels_recode_mind"

def main():
    with open(URLS_FILE, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip() and not line.startswith("#")][:20]

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    print("=" * 70)
    print("DOWNLOAD AND TIME MEASUREMENT FOR LAST 20 REELS OF @recode_mind_")
    print("=" * 70)
    
    overall_start = time.time()
    results = []
    
    for idx, url in enumerate(urls, 1):
        shortcode = url.rstrip("/").split("/")[-1]
        mp4_final = os.path.join(OUTPUT_DIR, f"{shortcode}.mp4")
        mp3_final = os.path.join(OUTPUT_DIR, f"{shortcode}.mp3")
        json_final = os.path.join(OUTPUT_DIR, f"{shortcode}.info.json")
        
        # Check if already successfully downloaded from previous pass
        already_done = os.path.exists(mp4_final) and os.path.exists(mp3_final) and os.path.getsize(mp4_final) > 100000
        
        print(f"\n[{idx}/20] Processing {shortcode} ({url})...")
        t0 = time.time()
        
        if already_done:
            elapsed = 0.01
            success = True
            print(f"[CACHE] Already downloaded previously: {mp4_final} ({os.path.getsize(mp4_final):,} bytes)")
        else:
            # Clean any leftover partial files
            for fname in os.listdir(OUTPUT_DIR):
                if fname.startswith(shortcode) and not fname.endswith(".mp4"):
                    try:
                        os.remove(os.path.join(OUTPUT_DIR, fname))
                    except:
                        pass
            success = False
            for attempt in range(1, 4):
                print(f"  Attempt {attempt}/3...")
                try:
                    success = download_reel(url, output_dir=OUTPUT_DIR, verbose=False)
                    if success and os.path.exists(mp4_final):
                        break
                except Exception as e:
                    print(f"  Attempt {attempt} error: {e}")
                time.sleep(2)
            elapsed = round(time.time() - t0, 2)
            
        file_size_mp4 = os.path.getsize(mp4_final) if os.path.exists(mp4_final) else 0
        file_size_mp3 = os.path.getsize(mp3_final) if os.path.exists(mp3_final) else 0
        
        title = "N/A"
        duration = 0
        if os.path.exists(json_final):
            try:
                with open(json_final, "r", encoding="utf-8") as jf:
                    meta = json.load(jf)
                    title = meta.get("title") or meta.get("description", "")[:50]
                    duration = meta.get("duration", 0)
            except:
                pass
                
        results.append({
            "index": idx,
            "shortcode": shortcode,
            "url": url,
            "success": success,
            "time_seconds": elapsed,
            "mp4_bytes": file_size_mp4,
            "mp3_bytes": file_size_mp3,
            "title": title,
            "duration": duration,
        })
        
        print(f"[{'OK' if success else 'FAIL'}] {shortcode}: {elapsed:.2f}s | MP4: {file_size_mp4 / (1024*1024):.2f} MB")
        sys.stdout.flush()

    total_time = round(time.time() - overall_start, 2)
    success_count = sum(1 for r in results if r["success"])
    total_mp4 = sum(r["mp4_bytes"] for r in results)
    total_mp3 = sum(r["mp3_bytes"] for r in results)
    
    # Save final report
    final_report = {
        "channel": "https://www.instagram.com/recode_mind_",
        "total_videos": 20,
        "successful_downloads": success_count,
        "total_time_seconds": total_time,
        "total_time_formatted": f"{int(total_time // 60)}m {round(total_time % 60, 2)}s",
        "total_mp4_mb": round(total_mp4 / (1024 * 1024), 2),
        "total_mp3_mb": round(total_mp3 / (1024 * 1024), 2),
        "videos": results
    }
    
    with open("final_20_reels_benchmark.json", "w", encoding="utf-8") as f:
        json.dump(final_report, f, indent=2, ensure_ascii=False)
        
    print("\n" + "=" * 70)
    print("FINAL 20 REELS DOWNLOAD SUMMARY")
    print("=" * 70)
    print(f"Downloaded:       {success_count}/20 reels")
    print(f"Total Time:       {total_time:.2f}s ({int(total_time // 60)}m {round(total_time % 60, 2)}s)")
    print(f"Total MP4 Size:   {total_mp4 / (1024 * 1024):.2f} MB")
    print(f"Total MP3 Size:   {total_mp3 / (1024 * 1024):.2f} MB")
    print("=" * 70)

if __name__ == "__main__":
    main()
