import os
import sys
import re
import time
import json
from datetime import datetime
from playwright.sync_api import sync_playwright

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

from insta_downloader import download_reel

def fetch_reels_from_channel(username: str, count: int = 5) -> list:
    url = f"https://www.instagram.com/{username}/reels/"
    reels = []
    
    print(f"\n=======================================================")
    print(f"[>] Harvesting {count} reels from: @{username}")
    print(f"=======================================================")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 900}
        )
        page = context.new_page()
        
        def on_response(res):
            if "graphql" in res.url and res.status == 200:
                try:
                    text = res.text()
                    codes = re.findall(r'"code":"([A-Za-z0-9_-]{11})"', text)
                    for c in codes:
                        clean = f"https://www.instagram.com/reel/{c}/"
                        if clean not in reels:
                            reels.append(clean)
                            print(f"  [+] Found (GraphQL): {clean}")
                except Exception:
                    pass
                    
        page.on("response", on_response)
        
        try:
            page.goto(url, wait_until="networkidle", timeout=45000)
        except Exception as e:
            print(f"  [!] Page load timeout/notice: {e}")
            
        # Also grab any links present in the initial DOM
        links = page.eval_on_selector_all("a[href*='/reel/'], a[href*='/p/']", "elements => elements.map(e => e.href)")
        for l in links:
            m = re.search(r'/(reel|p)/([A-Za-z0-9_-]{11})', l)
            if m:
                clean = f"https://www.instagram.com/reel/{m.group(2)}/"
                if clean not in reels:
                    reels.append(clean)
                    print(f"  [+] Found (DOM): {clean}")
                    
        # If we need more, scroll slightly
        retries = 0
        while len(reels) < count and retries < 5:
            page.keyboard.press("Escape")
            page.evaluate("() => { document.body.style.overflow = 'auto'; }")
            page.mouse.wheel(0, 2000)
            page.wait_for_timeout(2000)
            retries += 1
            
        browser.close()
        
    return reels[:count]

def main():
    channels = [
        {"username": "gordol.tips", "folder": "gordol_tips"},
        {"username": "swolotips", "folder": "swolotips"}
    ]
    
    total_start = time.time()
    all_results = {}
    
    for ch in channels:
        username = ch["username"]
        folder_name = ch["folder"]
        out_dir = os.path.join("downloaded_videos", folder_name)
        os.makedirs(out_dir, exist_ok=True)
        
        # 1. Harvest URLs
        reels = fetch_reels_from_channel(username, count=5)
        print(f"\n[✓] Collected {len(reels)} reel(s) for @{username}:")
        for idx, r in enumerate(reels, 1):
            print(f"    {idx}. {r}")
            
        # 2. Download each
        ch_results = []
        for idx, r in enumerate(reels, 1):
            print(f"\n[{username} {idx}/{len(reels)}] Downloading: {r}")
            t0 = time.time()
            ok = download_reel(
                url=r,
                output_dir=out_dir,
                get_video=True,
                get_audio=True,
                get_metadata=True,
                verbose=False
            )
            elapsed = round(time.time() - t0, 2)
            ch_results.append({
                "url": r,
                "success": ok,
                "elapsed_seconds": elapsed
            })
            print(f"[->] Download completed in {elapsed}s (Status: {'SUCCESS' if ok else 'FAILED'})")
            
        all_results[username] = ch_results
        
    total_elapsed = round(time.time() - total_start, 2)
    
    print("\n" + "=" * 70)
    print("DOWNLOAD COMPLETE SUMMARY")
    print("=" * 70)
    for username, items in all_results.items():
        success_count = sum(1 for i in items if i["success"])
        print(f"@{username}: {success_count}/{len(items)} downloaded")
    print(f"Total time elapsed: {total_elapsed}s ({int(total_elapsed // 60)}m {round(total_elapsed % 60, 2)}s)")
    print("=" * 70)

if __name__ == "__main__":
    main()
