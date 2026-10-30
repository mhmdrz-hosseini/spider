import time
import re
from playwright.sync_api import sync_playwright

def get_reels(username="recode_mind_", count=20):
    url = f"https://www.instagram.com/{username}/reels/"
    reels = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 900}
        )
        page = context.new_page()
        print(f"Navigating to {url}...")
        page.goto(url, wait_until="networkidle", timeout=60000)
        
        # Check title
        print("Page title:", page.title())
        
        # Scroll and collect links
        retries = 0
        while len(reels) < count and retries < 15:
            links = page.eval_on_selector_all("a[href*='/reel/'], a[href*='/p/']", "elements => elements.map(e => e.href)")
            for l in links:
                # normalize to https://www.instagram.com/reel/SHORTCODE/
                m = re.search(r'/(reel|p)/([A-Za-z0-9_-]+)', l)
                if m:
                    shortcode = m.group(2)
                    clean = f"https://www.instagram.com/reel/{shortcode}/"
                    if clean not in reels:
                        reels.append(clean)
                        print(f"[{len(reels)}/{count}] Found: {clean}")
                        if len(reels) >= count:
                            break
            
            if len(reels) >= count:
                break
                
            page.mouse.wheel(0, 2000)
            time.sleep(2)
            retries += 1
            
        browser.close()
        
    return reels

if __name__ == "__main__":
    reels = get_reels()
    print("\nTotal reels found:", len(reels))
    for r in reels:
        print(r)
