# KetabYar Local Soundtrack Curator — Agent Skill

## Mission
Use an **offline library of verified-license audio**, not cloud generation or paid APIs. Choose expressive, minimal music that supports Persian narration and Booki's scene arc.

## Inputs
- Timed scene JSON containing `beats[]` or v2 `scenes[].states[]`.
- Isolated Persian narration track.
- Local indexed music library with verified licenses.

## Workflow
1. Tag each major narrative section with mood, energy (1–5), keywords, and timestamps.
2. Prefer curiosity -> uncertainty -> reflective thought -> hopeful clarity as appropriate to the actual script.
3. Prefer instrumental, low-density music with space for TTS. Avoid vocals, aggressive drums, and generic constant epic scores.
4. Group contiguous beats by musical emotion; don't change tracks on every visual cut.
5. Run `python -m ketabyar_audio.local_soundtrack match --catalog ... --scenes ... --out soundtrack_plan.json`.
6. Inspect the plan, audition candidates, and revise any inappropriate cues.
7. Use `render` with a clean narration source and FFmpeg ducking; check phone playback.
8. Use `mux` to place final stereo audio into the video.

## License safety
Never mark a mixed-license collection as CC0. Never import unknown/NC music automatically. Save license records. CC BY needs complete attribution and `--allow-cc-by`. No scraping YouTube/Instagram soundtracks into commercial production.

## Integration notes
The Spider repo contains a pipeline architecture document but not the running KetabYar rendering app. This skill enables the soundtrack adapter and defines a handoff to that future renderer, not a finished renderer hookup. Documentation: `ketabyar_audio/README.md`.
