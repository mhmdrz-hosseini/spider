"""
Interactive YouTube Cookie Exporter
-----------------------------------
Opens a real Chrome browser window.
1. Sign in to your YouTube account (or visit youtube.com).
2. Press Enter in the terminal (or close the browser when done).
3. Saves clean cookies to 'd:\\code\\SPIDER\\cookies.txt'.
"""

import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

WORKSPACE = Path(__file__).resolve().parents[1]
OUTPUT_FILE = WORKSPACE / "cookies.txt"

print("=======================================================")
print("  Interactive YouTube Cookie Exporter")
print("=======================================================")
print("[>] Launching browser window...")
print("[>] Please sign in to YouTube (or complete any bot verification).")

with sync_playwright() as p:
    # Launch headed browser
    browser = p.chromium.launch(
        headless=False,
        args=["--disable-blink-features=AutomationControlled"]
    )
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
    page = context.new_page()
    page.goto("https://www.youtube.com", timeout=60000)

    print("\n[!] Window is now open on your screen.")
    print("[!] When you are signed in on YouTube, press ENTER here in the terminal...")
    try:
        input()
    except EOFError:
        page.wait_for_timeout(30000)

    cookies = context.cookies()
    print(f"[>] Captured {len(cookies)} cookies from browser context.")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# Netscape HTTP Cookie File\n")
        for c in cookies:
            domain = c["domain"]
            flag = "TRUE" if domain.startswith(".") else "FALSE"
            path = c.get("path", "/")
            secure = "TRUE" if c.get("secure", False) else "FALSE"
            expires = int(c.get("expires", 0)) if c.get("expires", -1) > 0 else 0
            name = c["name"]
            value = c["value"]
            f.write(f"{domain}\t{flag}\t{path}\t{secure}\t{expires}\t{name}\t{value}\n")

    browser.close()

print(f"\n[✓] Cookies saved successfully to: {OUTPUT_FILE}")
print("[✓] You can now run: python spider/download_robert_tolone.py\n")
