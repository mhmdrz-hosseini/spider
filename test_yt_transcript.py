import urllib.request
import re
import json

url = 'https://www.youtube.com/watch?v=VL4ULwKjsjI'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')

matches = re.findall(r'"captionTracks":(\[.*?\])', html)
print('Found captionTracks:', len(matches))
if matches:
    tracks = json.loads(matches[0])
    for idx, t in enumerate(tracks):
        print(f"Track {idx}: {t.get('languageCode')} - {t.get('name', {}).get('simpleText')}")
        base_url = t['baseUrl'] + '&fmt=json3'
        sub_res = urllib.request.urlopen(base_url).read().decode('utf-8')
        sub_data = json.loads(sub_res)
        print(f"Total subtitle events: {len(sub_data.get('events', []))}")
        for ev in sub_data.get('events', [])[:10]:
            segs = ev.get('segs', [])
            text = ''.join(s.get('utf8', '') for s in segs).strip()
            if text:
                t_sec = round(ev.get("tStartMs", 0) / 1000, 2)
                print(f"  [{t_sec}s] {text}")
