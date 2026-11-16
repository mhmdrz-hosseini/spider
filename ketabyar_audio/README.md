# KetabYar Offline Soundtrack Library

This is a **standalone adapter** for the Audio Synthesis / Foley Engine and Compositing modules in `motion_comic_pipeline_architecture-v2.md`. The repository currently includes the specification and scraper scripts, **not** the full video-renderer implementation. Integration into that renderer still requires its source code.

**Runs locally:** Python standard library + installed FFmpeg/FFprobe. No account, paid plan, hosted API, or ML checkpoint.

## Obtain the audio library (one-time manual download)

Recommended: [Tallbeard / Abstraction Music Loop Bundle](https://tallbeard.itch.io/music-loop-bundle) — 200+ CC0 loops. Check the creator's published CC0 declaration at acquisition, download and extract locally.

Other collections: [CLR Music packs](https://clr.fm/music/packs/) (mixed licenses; see individual LICENSES.txt) or [OpenGameArt](https://opengameart.org/) (filter and verify each item).

Keep music files outside Git, for example `D:/KetabYar/assets/music/` or `~/KetabYar/assets/music/`. The repository ignores audio file extensions. Preserve original license files and sources.

**IMPORTANT:** `--license CC0-1.0` is for verified uniform-CC0 collections **only**. Never apply it to a mixed-license pack. By default tracks without a known license cannot be selected.

## Commands

```bash
# Index verified local CC0 collection
python -m ketabyar_audio.local_soundtrack index --root "D:/KetabYar/assets/music" --license CC0-1.0 --source-url "https://tallbeard.itch.io/music-loop-bundle"

# Match scenes to tracks without network access
python -m ketabyar_audio.local_soundtrack match --catalog "D:/KetabYar/assets/music/catalog.json" --scenes examples/ketabyar_audio_beats.json --out soundtrack_plan.json

# Use the ORIGINAL isolated TTS as voice input
python -m ketabyar_audio.local_soundtrack render --plan soundtrack_plan.json --voice narration.wav --out audio_master.wav

# Attach mixed audio to final silent video
python -m ketabyar_audio.local_soundtrack mux --video silent_video.mp4 --audio audio_master.wav --out ketabyar_final.mp4
```

The matcher also reads `scenes[].states[]` from the repository's v2 motion-comic specification, provided the scenes have timestamps; an explicit `mood` and `energy` on each scene is recommended.

The mixer loops short tracks, fades and time-aligns the chosen cues, sidechain-ducks music beneath Persian speech, and exports a stereo 48 kHz 24-bit WAV before making an AAC MP4. Inspect the resulting soundtrack and audio loudness before publishing.

## Precise manual metadata

Create a sidecar file alongside a music file, named like `question_theme.wav.json`:

```json
{
  "title": "Question Theme",
  "creator": "Composer name",
  "license": "CC0-1.0",
  "source_url": "https://example.org/original-source",
  "moods": ["curious", "reflective"],
  "tags": ["minimal", "piano", "ambient", "instrumental"],
  "energy": 2,
  "speech_friendly": true,
  "loopable": true
}
```

Filename/parent-folder mood inference is intentionally a *fallback*; precise tagging produces superior results. Unrecognized licenses, including NC, are blocked. CC BY 3.0/4.0 can be included with `--allow-cc-by` only if creator, attribution, and source URL are present. Preserve the licensing records; even legitimate CC0 music may attract erroneous copyright matches.

## Matcher model

Deterministic ranking considers mood alignment (highest importance), energy (1–5), instrumental/speech-friendliness, prompt keywords, track length/loopability, and continuity with previous cue. No AI checkpoint required. The timeline keeps adjacent same-emotion beats together rather than changing music on every cut. Output `soundtrack_plan.json` records selected IDs, files, source and credits. Review/tune the plan before rendering.

For more intelligent *optional* local retrieval, add LAION CLAP embeddings in a later version; this requires checking model-weight licenses separately.

## Limitations

- This is not a music generator and does not ship audio assets.
- It does not yet include a manual audio preview UI, timbre-aware ranking, beat-sync, or curated content scoring.
- Do not pass an existing mixed voice+music track as narration or it will be duplicated.
- Because the renderer application itself is absent from Spider, this module is **not automatically invoked** by existing downloader commands.
- Run unit tests: `python -m unittest discover -s tests -p test_local_soundtrack.py`.
