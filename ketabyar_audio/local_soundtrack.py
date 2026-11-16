"""KetabYar offline soundtrack library. Python 3.10+, FFmpeg/FFprobe only."""
from __future__ import annotations
import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path

FORMATS = {".wav", ".flac", ".ogg", ".opus", ".mp3", ".m4a"}
SAFE = {"CC0", "CC0-1.0", "PUBLIC-DOMAIN", "PUBLIC DOMAIN"}
WITH_CREDIT = {"CC-BY-3.0", "CC-BY-4.0"}
MOODS = {
    "curious": {"curious", "curiosity", "mystery", "wonder", "puzzle", "question", "discovery"},
    "tense": {"tense", "tension", "suspense", "dark", "uncertainty", "anxious", "confusion"},
    "hopeful": {"hopeful", "uplifting", "inspiring", "warm", "optimistic", "breakthrough", "resolution"},
    "calm": {"calm", "gentle", "quiet", "peaceful", "ambient", "meditative", "soft"},
    "playful": {"playful", "quirky", "light", "comic", "bouncy"},
    "dramatic": {"dramatic", "cinematic", "epic", "impactful", "intense"},
    "reflective": {"reflective", "melancholic", "thoughtful", "emotional", "nostalgic"},
}
VOCAL = {"vocals", "vocal", "singing", "lyrics", "speech"}
BUSY = {"heavy", "busy", "aggressive", "loud"}


def words(value):
    return set(re.findall(r"[a-z0-9]+", str(value).lower().replace("_", " ").replace("-", " ")))


def mood_name(value):
    value = str(value or "calm").lower().strip()
    for name, aliases in MOODS.items():
        if value == name or value in aliases:
            return name
    return value


def duration_of(path):
    if not shutil.which("ffprobe"):
        return None
    try:
        raw = subprocess.check_output([
            "ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", str(path)
        ], stderr=subprocess.DEVNULL, text=True, timeout=20).strip()
        return round(float(raw), 3)
    except (OSError, ValueError, subprocess.SubprocessError):
        return None


def index_library(folder, pack_license="UNKNOWN", source_url=""):
    """Files without a confirmed license are indexed but not selectable.

    The pack_license argument must only be used for verified single-license packs.
    A file.wav.json sidecar overrides its license and metadata.
    """
    folder = Path(folder).resolve()
    if not folder.is_dir():
        raise ValueError("Library directory does not exist: " + str(folder))
    records = []
    for f in sorted(folder.rglob("*")):
        if not f.is_file() or f.suffix.lower() not in FORMATS:
            continue
        sidecar = Path(str(f) + ".json")
        meta = json.loads(sidecar.read_text(encoding="utf-8")) if sidecar.is_file() else {}
        if not isinstance(meta, dict):
            raise ValueError("Sidecar must contain a JSON object: " + str(sidecar))
        guessed = words(f.stem + " " + str(f.parent.relative_to(folder)))
        moods = meta.get("moods") or meta.get("mood") or []
        if isinstance(moods, str):
            moods = [moods]
        if not moods:
            moods = [m for m, aliases in MOODS.items() if guessed & (aliases | {m})] or ["calm"]
        tags = meta.get("tags", [])
        if isinstance(tags, str):
            tags = [tags]
        if "energy" in meta:
            energy = max(1, min(5, int(meta["energy"])))
        else:
            energy = 4 if guessed & {"epic", "tense", "intense"} else 2 if guessed & {"ambient", "calm", "soft"} else 3
        relative = f.relative_to(folder).as_posix()
        records.append({
            "id": relative, "file": relative, "title": str(meta.get("title") or f.stem),
            "creator": str(meta.get("creator") or ""),
            "license": str(meta.get("license") or pack_license).upper(),
            "source_url": str(meta.get("source_url") or source_url),
            "attribution": str(meta.get("attribution") or ""),
            "moods": sorted({mood_name(m) for m in moods}),
            "tags": sorted(set(str(t).lower() for t in tags) | guessed),
            "energy": energy, "bpm": meta.get("bpm"),
            "loopable": bool(meta.get("loopable", True)),
            "speech_friendly": bool(meta.get("speech_friendly", not bool(guessed & VOCAL))),
            "duration_sec": meta.get("duration_sec") or duration_of(f),
        })
    catalog = {"schema_version": 1, "tracks": records}
    (folder / "catalog.json").write_text(json.dumps(catalog, ensure_ascii=False, indent=2), encoding="utf-8")
    return catalog


def eligible(track, allow_cc_by=False):
    license_id = str(track.get("license") or "UNKNOWN").upper()
    if license_id in SAFE:
        return True
    return (bool(allow_cc_by) and license_id in WITH_CREDIT
            and all(track.get(field) for field in ("creator", "source_url", "attribution")))


def beats_from(scene_data):
    """Accept compact beats or existing motion comic v2 scenes/states."""
    beats = scene_data.get("beats")
    if beats is None:
        beats = []
        for scene in scene_data.get("scenes", []):
            for state in scene.get("states", [scene]):
                if "start_sec" not in state or "end_sec" not in state:
                    continue
                beats.append({
                    "id": state.get("state_id") or scene.get("scene_id"),
                    "start_sec": state["start_sec"], "end_sec": state["end_sec"],
                    "mood": state.get("mood") or state.get("emotional_state")
                            or scene.get("mood") or scene.get("emotional_state") or "curious",
                    "energy": state.get("energy") or scene.get("energy") or 2,
                    "keywords": state.get("keywords") or scene.get("keywords") or [],
                })
    normalized = []
    for i, beat in enumerate(beats):
        start, end = float(beat["start_sec"]), float(beat["end_sec"])
        if start < 0 or end <= start:
            raise ValueError("Invalid beat duration at index " + str(i))
        keywords = beat.get("keywords") or []
        normalized.append({
            "id": str(beat.get("id") or i), "start_sec": start, "end_sec": end,
            "mood": mood_name(beat.get("mood")), "energy": max(1, min(5, int(beat.get("energy", 2)))),
            "keywords": keywords if isinstance(keywords, list) else [keywords],
        })
    if not normalized:
        raise ValueError("No scenes/beats with timestamps found")
    normalized.sort(key=lambda item: item["start_sec"])
    for a, b in zip(normalized, normalized[1:]):
        if b["start_sec"] < a["end_sec"] - 0.01:
            raise ValueError("Overlapping beats: " + a["id"] + " and " + b["id"])
    merged = []
    for beat in normalized:
        if (merged and merged[-1]["mood"] == beat["mood"]
                and merged[-1]["energy"] == beat["energy"]
                and abs(merged[-1]["end_sec"] - beat["start_sec"]) < 0.11):
            merged[-1]["end_sec"] = beat["end_sec"]
            merged[-1]["keywords"] += beat["keywords"]
        else:
            merged.append(beat.copy())
    return merged


def score(track, beat, previous=None):
    moods = {mood_name(m) for m in track.get("moods", [])}
    points = 8.0 if beat["mood"] in moods else 0.0
    if beat["mood"] == "curious" and "reflective" in moods:
        points += 2
    if beat["mood"] == "hopeful" and "calm" in moods:
        points += 2
    points -= 1.7 * abs(int(track.get("energy", 3)) - beat["energy"])
    points += 3 if track.get("speech_friendly", True) else -8
    tags = set().union(*(words(tag) for tag in track.get("tags", [])))
    terms = set().union(*(words(term) for term in beat["keywords"])) if beat["keywords"] else set()
    points += min(4, len(tags & terms) * 1.25)
    if tags & VOCAL:
        points -= 7
    if tags & BUSY:
        points -= 2.5
    if previous == track["id"]:
        points += 1.25
    length = track.get("duration_sec")
    if length and float(length) >= beat["end_sec"] - beat["start_sec"]:
        points += 1.5
    elif track.get("loopable", False):
        points += 0.5
    else:
        points -= 7
    return round(points, 3)


def match(catalog_path, scene_path, allow_cc_by=False):
    catalog_path = Path(catalog_path).resolve()
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    scenes = json.loads(Path(scene_path).read_text(encoding="utf-8"))
    candidates = [t for t in catalog.get("tracks", [])
                  if eligible(t, allow_cc_by) and (catalog_path.parent / t["file"]).is_file()]
    if not candidates:
        raise ValueError("No license-approved audio on disk. Download a CC0 pack and run index.")
    selections, previous = [], None
    for beat in beats_from(scenes):
        picked = sorted(candidates, key=lambda t: (-score(t, beat, previous), t["id"]))[0]
        previous = picked["id"]
        selections.append({
            "beat_id": beat["id"], "start_sec": beat["start_sec"], "end_sec": beat["end_sec"],
            "mood": beat["mood"], "track_id": picked["id"],
            "file": str((catalog_path.parent / picked["file"]).resolve()),
            "score": score(picked, beat), "gain_db": -21,
            "fade_in_sec": 0.65, "fade_out_sec": 0.8,
            "license": picked["license"], "title": picked["title"],
            "creator": picked["creator"], "source_url": picked["source_url"],
            "attribution": picked["attribution"],
        })
    return {"schema_version": 1, "duration_sec": max(t["end_sec"] for t in selections),
            "tracks": selections,
            "credits": sorted({t["attribution"] for t in selections if t["attribution"]})}


def render(plan_path, voice_path, output_path):
    """Return a 48kHz/24-bit stereo master; use distinct voice/music inputs."""
    if not shutil.which("ffmpeg"):
        raise RuntimeError("FFmpeg is required")
    plan = json.loads(Path(plan_path).read_text(encoding="utf-8"))
    selections = plan.get("tracks", [])
    if not selections:
        raise ValueError("Plan has no soundtrack cues")
    voice_path, output_path = Path(voice_path).resolve(), Path(output_path).resolve()
    if not voice_path.is_file():
        raise FileNotFoundError(voice_path)
    if output_path.suffix.lower() != ".wav":
        raise ValueError("Output audio master must end in .wav")
    command = ["ffmpeg", "-hide_banner", "-y", "-i", str(voice_path)]
    for track in selections:
        path = Path(track["file"])
        if not path.is_file():
            raise FileNotFoundError(path)
        command += ["-stream_loop", "-1", "-i", str(path)]
    filters, labels = [], []
    for index, cue in enumerate(selections):
        total = float(cue["end_sec"]) - float(cue["start_sec"])
        if total <= 0:
            raise ValueError("Cue duration must be positive")
        fade_in = min(total / 3, float(cue.get("fade_in_sec", 0.65)))
        fade_out = min(total / 3, float(cue.get("fade_out_sec", 0.8)))
        delay_ms = round(float(cue["start_sec"]) * 1000)
        gain = float(cue.get("gain_db", -21))
        label = "m" + str(index)
        filters.append(
            f"[{index+1}:a]aresample=48000,aformat=channel_layouts=stereo,"
            f"atrim=duration={total:.3f},asetpts=PTS-STARTPTS,"
            f"volume={gain:.2f}dB,afade=t=in:st=0:d={fade_in:.3f},"
            f"afade=t=out:st={max(0,total-fade_out):.3f}:d={fade_out:.3f},"
            f"adelay={delay_ms}:all=1[{label}]"
        )
        labels.append("[" + label + "]")
    if len(labels) == 1:
        filters.append(labels[0] + "anull[bed]")
    else:
        filters.append("".join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=longest[bed]")
    filters.append("[bed][0:a]sidechaincompress=threshold=0.03:ratio=7:attack=80:release=450[ducked]")
    filters.append("[0:a][ducked]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95[out]")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    command += ["-filter_complex", ";".join(filters), "-map", "[out]",
                "-ar", "48000", "-ac", "2", "-c:a", "pcm_s24le", str(output_path)]
    subprocess.run(command, check=True)
    return output_path


def mux(video_path, master_audio, output_video):
    if not shutil.which("ffmpeg"):
        raise RuntimeError("FFmpeg is required")
    subprocess.run(["ffmpeg", "-hide_banner", "-y", "-i", str(video_path),
                    "-i", str(master_audio), "-map", "0:v:0", "-map", "1:a:0",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "256k",
                    "-shortest", str(output_video)], check=True)


def main(argv=None):
    parser = argparse.ArgumentParser(description="KetabYar local soundtrack selector (no APIs)")
    commands = parser.add_subparsers(dest="operation", required=True)
    cmd = commands.add_parser("index")
    cmd.add_argument("--root", required=True)
    cmd.add_argument("--license", default="UNKNOWN")
    cmd.add_argument("--source-url", default="")
    cmd = commands.add_parser("match")
    cmd.add_argument("--catalog", required=True)
    cmd.add_argument("--scenes", required=True)
    cmd.add_argument("--out", required=True)
    cmd.add_argument("--allow-cc-by", action="store_true")
    cmd = commands.add_parser("render")
    cmd.add_argument("--plan", required=True)
    cmd.add_argument("--voice", required=True)
    cmd.add_argument("--out", required=True)
    cmd = commands.add_parser("mux")
    cmd.add_argument("--video", required=True)
    cmd.add_argument("--audio", required=True)
    cmd.add_argument("--out", required=True)
    args = parser.parse_args(argv)
    if args.operation == "index":
        index_data = index_library(args.root, args.license, args.source_url)
        print("Indexed", len(index_data["tracks"]), "tracks;", sum(eligible(t) for t in index_data["tracks"]), "are license-approved")
    elif args.operation == "match":
        output = Path(args.out)
        output.parent.mkdir(parents=True, exist_ok=True)
        result = match(args.catalog, args.scenes, args.allow_cc_by)
        output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        print("Selected", len(result["tracks"]), "music cues:", output)
    elif args.operation == "render":
        print(render(args.plan, args.voice, args.out))
    elif args.operation == "mux":
        mux(args.video, args.audio, args.out)
        print(args.out)


if __name__ == "__main__":
    main()
