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
    if not os.path.exists(URLS_FILE):
        print(f"[ERROR] URL list {URLS_FILE} not found!")
        sys.exit(1)
        
    with open(URLS_FILE, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip() and not line.startswith("#")]
        
    urls = urls[:20]
    total_count = len(urls)
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    print("=" * 70)
    print("INSTAGRAM 20 VIDEOS BATCH DOWNLOAD & PERFORMANCE BENCHMARK")
    print(f"Channel: @recode_mind_ (https://www.instagram.com/recode_mind_)")
    print(f"Target count: {total_count} videos")
    print(f"Destination: {os.path.abspath(OUTPUT_DIR)}")
    print(f"Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    sys.stdout.flush()
    
    overall_start = time.time()
    results = []
    
    for idx, url in enumerate(urls, 1):
        print(f"\n[{idx}/{total_count}] Starting download: {url}")
        sys.stdout.flush()
        
        t0 = time.time()
        success = False
        meta = {}
        file_size_mp4 = 0
        file_size_mp3 = 0
        
        try:
            # Call existing download_reel method
            success = download_reel(
                url=url,
                output_dir=OUTPUT_DIR,
                get_video=True,
                get_audio=True,
                get_metadata=True,
                get_frames=False,
                do_transcribe=False,
                verbose=False
            )
        except Exception as e:
            print(f"[!] Exception downloading {url}: {e}")
            success = False
            
        elapsed = round(time.time() - t0, 2)
        
        # Check files
        shortcode = url.rstrip("/").split("/")[-1]
        mp4_path = os.path.join(OUTPUT_DIR, f"{shortcode}.mp4")
        mp3_path = os.path.join(OUTPUT_DIR, f"{shortcode}.mp3")
        json_path = os.path.join(OUTPUT_DIR, f"{shortcode}.info.json")
        
        title = "N/A"
        duration = 0
        
        if os.path.exists(json_path):
            try:
                with open(json_path, "r", encoding="utf-8") as jf:
                    meta = json.load(jf)
                    title = meta.get("title") or meta.get("description", "")[:50]
                    duration = meta.get("duration", 0)
            except Exception:
                pass
                
        if os.path.exists(mp4_path):
            file_size_mp4 = os.path.getsize(mp4_path)
        if os.path.exists(mp3_path):
            file_size_mp3 = os.path.getsize(mp3_path)
            
        res_item = {
            "index": idx,
            "url": url,
            "shortcode": shortcode,
            "success": success,
            "time_seconds": elapsed,
            "title": title,
            "duration": duration,
            "mp4_bytes": file_size_mp4,
            "mp3_bytes": file_size_mp3,
        }
        results.append(res_item)
        
        status_str = "SUCCESS" if success else "FAILED"
        print(f"[->] Video {idx}/{total_count} [{status_str}] in {elapsed:.2f}s | MP4: {file_size_mp4 / (1024*1024):.2f} MB | MP3: {file_size_mp3 / (1024*1024):.2f} MB")
        sys.stdout.flush()
        
    overall_elapsed = round(time.time() - overall_start, 2)
    successful_count = sum(1 for r in results if r["success"])
    total_mp4_bytes = sum(r["mp4_bytes"] for r in results)
    total_mp3_bytes = sum(r["mp3_bytes"] for r in results)
    avg_time = round(overall_elapsed / total_count, 2) if total_count else 0
    
    minutes = int(overall_elapsed // 60)
    seconds = round(overall_elapsed % 60, 2)
    
    print("\n" + "=" * 70)
    print("BENCHMARK SUMMARY")
    print("=" * 70)
    print(f"Total Videos Processed:    {total_count}")
    print(f"Successfully Downloaded:   {successful_count}/{total_count}")
    print(f"Total Time Taken:          {overall_elapsed:.2f} seconds ({minutes}m {seconds:.2f}s)")
    print(f"Average Time per Video:    {avg_time:.2f} seconds")
    print(f"Total MP4 Data Downloaded: {total_mp4_bytes / (1024*1024):.2f} MB")
    print(f"Total MP3 Audio Extracted: {total_mp3_bytes / (1024*1024):.2f} MB")
    print("=" * 70)
    
    # Save benchmark json
    summary_data = {
        "channel": "https://www.instagram.com/recode_mind_",
        "total_requested": total_count,
        "total_successful": successful_count,
        "total_time_seconds": overall_elapsed,
        "total_time_formatted": f"{minutes}m {seconds:.2f}s",
        "average_time_per_video_seconds": avg_time,
        "total_mp4_mb": round(total_mp4_bytes / (1024*1024), 2),
        "total_mp3_mb": round(total_mp3_bytes / (1024*1024), 2),
        "items": results
    }
    
    with open("benchmark_results.json", "w", encoding="utf-8") as f:
        json.dump(summary_data, f, indent=2, ensure_ascii=False)
        
    print(f"[✓] Benchmark report saved to benchmark_results.json")
    sys.stdout.flush()

if __name__ == "__main__":
    main()
