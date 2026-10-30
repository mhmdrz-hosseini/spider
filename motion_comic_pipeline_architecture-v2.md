# System Architecture & Pipeline Specification (v2.0)
## Automated "Engineered Motion Comic" Video Production Engine
**Version:** 2.0 (Expanded Multi-Reference Forensic Edition)

---

## 1. Executive Summary & Core Paradigm

The **Engineered Motion Comic** format achieves high viewer retention and cinematic immersion using **0% AI Video Generation (0% I2V)** in standard production. Forensic analysis across six reference productions demonstrates that the illusion of animation is engineered entirely through:

1. **The Two-Act "Parable-to-Real-Life Bridge" Narrative Structure:** Stories open with a concrete visual parable or sensory metaphor (Act I) and pivot at the 60%–70% mark into a modern psychological or workplace parallel (Act II).
2. **State-Locked Scene Families (Inpainting & Pose Toggling):** Keeping 85%–95% of environmental pixels identical while toggling character poses, expressions, or focal objects across 2 to 4 sequential states.
3. **2.5D Multi-Axis Camera Choreography:** Utilizing wide/tall master canvases to execute horizontal story pans (panning from Subject A to Subject B within one image), vertical tilt-downs, and shared-camera continuous zooms across state dissolves.
4. **Diagrammatic & Sensory Visual Metaphors:** Embedding X-ray underground cross-sections, vector directional arrows, split-screen comparison frames, and focal-color isolation directly into the dark-noir artwork.
5. **Cross-Video Canonical Asset Library (Global Scene Reuse):** Reusing high-performing "canonical life scenes" (e.g., late-night laptop deep work, walking out the front gate at dawn, exhausted bedroom collapse, boardroom presentation) across multiple videos to cut generation costs by 25%–40%.
6. **Foley-Driven Action Illusion:** Replacing visual motion with hyper-literal Foley sound effects (water droplets, footsteps on gravel, car engines, crowd laughter, scribbling pens) synced to static visual cues.

---

## 2. End-to-End System Architecture

```
+-----------------------------------------------------------------------------------+
|                        INPUT LAYER (RAW CONTENT & CONFIG)                         |
|  [Raw Topic / Script]  +  [Channel Style Guide JSON]  +  [Character Sheet Assets] |
+-----------------------------------------+-----------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|                MODULE 1: NARRATIVE ARCHITECT & PARABLE-BRIDGE ENGINE              |
|  - Structures script into Act I (Visual Parable/Metaphor) & Act II (Modern Life)  |
|  - Breaks script into 2.5s - 4.0s narrative beats                                 |
|  - Tags beats with Emotional State, Time-of-Day Lighting, and Foley SFX Cues      |
+-----------------------------------------+-----------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|                MODULE 2: VISUAL DIRECTOR & SCENE-STATE COMPILER                   |
|  - Queries Global Canonical Asset Library for reusable Act II life/work scenes    |
|  - Groups new beats into Master Scenes (S1, S2...) and Sub-States (S1_A, S1_B...) |
|  - Assigns Shot Archetypes: Multi-Angle Coverage, X-Ray Cutaway, Split-Compare,   |
|    or Wide Pan Canvas                                                             |
+-----------------------------------------+-----------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|                MODULE 3: STATE-LOCKED IMAGE GENERATION ENGINE                     |
|  - Pass 1: Generates Master Keyframes (9:16 standard, or 4:5 / 9:20 for Pans)     |
|  - Pass 2: Generates Sub-States via Masked Inpainting / Instruction Editing       |
|  - Enforces Color Isolation (#FFC928 Protagonist/Focal Object vs. Monochrome)     |
|  - Archives reusable generic scenes into the Global Canonical Asset Library       |
+-----------------------------------------+-----------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|                MODULE 4: AUDIO SYNTHESIS, FOLEY ENGINE & WORD ALIGNMENT           |
|  - Generates dramatic TTS Voiceover with engineered pauses                        |
|  - Extracts millisecond Word-Level Timestamps (Whisper Forced Alignment)          |
|  - Maps 3-Layer Audio Track: Voiceover + Literal Action Foley + Sub-Bass/Risers   |
+-----------------------------------------+-----------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|                MODULE 5: 2.5D CAMERA CHOREOGRAPHER & VFX LAYER ENGINE             |
|  - Computes Shared-Camera Matrices (Continuous Zoom across State Dissolves)       |
|  - Executes Spatial Reveal Pans (Left-to-Right Subject Pan, Vertical Tilt-Down)   |
|  - Inserts Flashback Recap Cuts & Bookend Loop Anchors                            |
|  - Composites Atmospheric Overlays (Dust Motes, Wet Floor Specular Glow, Vignette)|
+-----------------------------------------+-----------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|                MODULE 6: PROGRAMMATIC COMPOSITING & RENDER ENGINE                 |
|  - Renders Eye-Tracked Micro-Captions (1-2 words at Center-of-Gravity X:50% Y:52%)|
|  - Mixes multi-track audio with sidechain ducking                                 |
|  - Outputs final 9:16 H.264/MP4 master at 24/30/60 FPS                            |
+-----------------------------------------------------------------------------------+
```

---

## 3. Detailed Module Specifications (Updated with v2 Forensic Insights)

### Module 1: Channel Style Guide & Character Registry (`config/channel_bible.json`)
Defines the immutable visual DNA of the channel so that any story—whether set in an ancient village, a laboratory, or a modern corporate office—maintains instant brand recognition.

* **Color Psychology & Focal Isolation Rules:**
  * **Protagonist (`CHAR_PROTAGONIST`):** Glowing Knowledge Gold (`#FFC928`) spherical 2D head with minimal black oval eyes and simple eyebrow lines. Even when the protagonist changes roles across parables (e.g., Farmer in overalls, Office Worker in shirt and tie, Student in black hoodie), the `#FFC928` spherical head remains 100% identical.
  * **Society / Antagonists / Mentors (`CHAR_SECONDARY`):** Stark white/grey (`#E5E5E5`) spherical heads. Used for mocking crowds, toxic bosses, scientists, family members, or wise mentors.
  * **Focal-Object Color Pop:** In monochrome environments (such as a black-and-white laboratory or dark bedroom), the single narrative catalyst object (e.g., a single grain of rice `#FFC928`, a sprouting green shoot `#4CAF50`, or blue water droplets `#29B6F6`) is rendered in high-saturation glowing color to command 100% viewer eye fixation.
* **Environmental Rendering Rules:**
  * **Dark Noir Line-Art Base:** Pitch-black backgrounds (`#111111`) with crisp white/grey architectural outlines (`#CCCCCC`) for distant buildings, trees, bookshelves, and furniture.
  * **Specular Wet-Floor & Rim Lighting:** Ground surfaces in markets, streets, and offices use high-contrast specular reflections of warm amber lights (`#FFC928` / `#B87932`) to create depth without complex shading.
  * **Time-of-Day Emotional Lighting:**
    * *Struggle / Grind / Isolation:* Pitch-black night sky with a stark white full moon and cool/amber local lamp light.
    * *Breakthrough / Realization / Ideal Outcome:* Warm golden-hour sunrise/sunset gradient (`#B87932` to `#FFC928`) on the horizon.

---

### Module 2: Narrative Architect & Visual Director (The Parable-to-Real-Life Compiler)

#### 2.1 The Two-Act "Parable-to-Modern-Life Bridge" Formula
Analysis of top-performing scripts reveals a strict two-act structural template:
* **Act I: The Concrete Parable or Sensory Metaphor (0% to 65% of runtime):**
  * Tells a highly visual, easy-to-follow story with physical stakes (e.g., a horse and donkey carrying grain sacks; a farmer watering two seeds differently; a scientist testing a rat in a jar; a man visiting a fish market vs. a perfume shop; driving a car at night with headlights).
* **The Bridge Transition (at ~65% mark):**
  * Triggered by a signature pivot phrase: *"And the same thing happens in real life..."*, *"In life, we make the exact same mistake..."*, or *"That's the power of your environment."*
  * Accompanied by a heavy Sub-Bass Drop and an immediate visual cut from the parable setting to a modern urban/domestic setting.
* **Act II: The Modern Psychological/Workplace Application (65% to 100% of runtime):**
  * Maps the lesson onto relatable modern struggles: office burnout, toxic bosses, New Year's resolution gym/study burnout, overthinking on the sofa, or surrounding oneself with mentors vs. negative friends.

#### 2.2 Advanced Shot Archetypes (Beyond Simple Keyframes)
The Visual Director assigns every narrative beat to one of seven specialized visual archetypes:

| Archetype Code | Name | Visual & Technical Description | Reference Example |
| :--- | :--- | :--- | :--- |
| **`ARCH_STATE_PAIR`** | **State-Locked Inpaint Pair** | Identical background and framing; only character expression, posture, or foreground prop changes via 8-frame dissolve. | Scientist smirking -> Scientist shocked; Cafe man sad -> Cafe man smirking with cigarette. |
| **`ARCH_WIDE_PAN`** | **Single-Canvas Spatial Pan** | A wider composition where the camera pans horizontally from Subject A on the left to Subject B on the right (or tilts vertically from top to bottom) to reveal narrative contrast without cutting. | Panning from lightly loaded horse on left to overburdened donkey on right; Panning from tired man at door to laughing family on sofa. |
| **`ARCH_MULTI_ANGLE`** | **Cinematic Multi-Camera Coverage** | Rapid 2-second cuts showing the same continuous action from 3-4 distinct camera angles (Front 3/4, Interior POV, Dead-Center Front, Rear Tracking). | Night driving sequence (exterior front -> interior windshield POV -> front headlights -> rear taillights). |
| **`ARCH_XRAY_CUTAWAY`** | **Cross-Section Diagrammatic Cutaway** | Cuts beneath the surface (e.g., underground soil cross-section) and overlays 2D vector indicators (glowing arrows, gauges, thought knots) to show invisible mechanisms. | Underground seed absorbing blue water drops with inward directional arrows -> expanding white root network. |
| **`ARCH_SPLIT_COMPARE`** | **Symmetrical Side-by-Side Comparison** | Places two outcomes side-by-side in a single frame with in-scene text signs/labels to crystallize the core contrast. | Farmer sitting on left (cracked soil, sign: `SAME WATER`) vs. right (green shoot, sign: `SAME WATER`). |
| **`ARCH_RECAP_LOOP`** | **Flashback Recap / Bookend Anchor** | Reuses an earlier keyframe from the same video (with a reversed or faster camera zoom) during the summary to reinforce memory and save generation compute. | Re-showing the 10-liter flood frame and single-drop root frame at 00:52; Reusing the 00:00 golden rice harvest frame at 00:22. |
| **`ARCH_CANONICAL_LIB`** | **Global Canonical Library Scene** | Pulls a pre-existing, high-impact modern life illustration from the channel's permanent asset database for Act II sequences. | Bedroom late-night laptop study shot; Walking out the front house gate with backpack. |

---

### Module 3: State-Locked Image Generation & Global Asset Library

#### 3.1 Solving the Consistency Bottleneck
To guarantee zero background jitter during state transitions (`ARCH_STATE_PAIR`):
1. **Master Keyframe Generation:** Generate `State_A` using the locked Channel Style prefix and Character Sheet reference.
2. **Instruction-Based / Masked State Editing:** Generate `State_B` by passing `State_A` into an image-editing or inpainting pipeline with a strict mask over only the mutable region (e.g., character head/arms or soil patch), leaving 85%+ of the background pixels untouched.
3. **Graphical Overlay Compositing:** For diagrammatic elements (scribbled overthinking clouds above the head, speedometers, directional arrows), either prompt them inside the masked region or composite clean SVG/PNG vector overlays programmatically in Module 5.

#### 3.2 The Global Canonical Asset Library (`assets/canonical_library/`)
Forensic inspection proves that the reference channel maintains a permanent library of **Canonical Modern-Life Scenes** that are reused verbatim across different videos whenever Act II touches on universal themes:
* `CANON_WORK_01`: Protagonist in dark bedroom working intensely at laptop under desk lamp (used in Environment, Clarity, and Consistency videos).
* `CANON_SUCCESS_01`: Protagonist in shirt, tie, and backpack walking confidently out the black iron house gate with black sedan parked behind (used in Clarity and Consistency videos).
* `CANON_OVERTHINK_01`: Protagonist sitting on dark living room sofa under warm floor lamp, hands on face or scrolling phone.
* `CANON_OFFICE_01`: Protagonist overwhelmed at desk stacked with paper files while white-headed colleagues stand in background.

By tagging Act II beats with canonical theme IDs, the engine retrieves existing master frames from disk instead of calling the image generator, reducing per-video generation cost and latency by 25%–40%.

---

### Module 4: Audio Synthesis, Foley Engine & Word Alignment

Because the visuals contain zero frame-by-frame character animation, **the audio track does 70% of the heavy lifting to sell the illusion of motion**.

#### 4.1 Three-Layer Audio Architecture
1. **Layer 1: Dramatic Narrative Voiceover (TTS / Cloned Voice)**
   * Deep, measured pacing with deliberate 0.3s–0.5s pauses at punctuation marks and before major reveals.
   * Processed with a subtle low-shelf EQ boost (120Hz) and crisp de-essing.
2. **Layer 2: Hyper-Literal Action Foley (The Motion Illusion Layer)**
   * Whenever a static image depicts a physical action, a prominent, crisp Foley sound effect plays simultaneously so the viewer's brain perceives movement:
     * *Watering / Liquid:* Pouring bucket splash, rhythmic single water drop plops, underwater bubbling.
     * *Locomotion:* Horse hooves clopping on dirt, footsteps on wet pavement, car engine hum.
     * *Human / Social:* Mocking crowd laughter, office applause, scribbling pen on paper, heavy exhausted sigh.
3. **Layer 3: Cinematic Transitions & Dark Ambient Score**
   * Low, melancholic piano/synth drone at `-22dB` that shifts to a warm, hopeful chord progression during the Act II resolution.
   * **Structural Audio Markers:** Deep Sub-Bass Drops (`60Hz`) at the Act I -> Act II Bridge, and Whoosh/Riser transitions (`0.4s`) synced to hard visual cuts.

---

### Module 5: 2.5D Camera Choreographer (Motion Without I2V)

Every single frame in the video must be in continuous motion. The Camera Choreographer translates static images into dynamic video clips using five mathematical camera trajectories:

#### 5.1 Trajectory 1: Shared-Camera Continuous Zoom (`SHARED_ZOOM`)
Used for `ARCH_STATE_PAIR` sequences (`State_A` -> `State_B`).
* Instead of resetting the zoom on each image, the camera applies a single continuous scale function $S(t) = S_{start} + (S_{end} - S_{start}) \cdot rac{t}{T_{total}}$ across the combined duration of both states, executing an 8-to-12 frame cross-dissolve (`xfade`) at the state boundary.

#### 5.2 Trajectory 2: Horizontal Story Pan (`SPATIAL_PAN_X`)
Used for `ARCH_WIDE_PAN` sequences (e.g., panning from the horse on the left to the donkey on the right, or from the man at the door to the family on the couch).
* The source image is generated at a wider aspect ratio (e.g., `4:5` or `1:1` at `1200x1376`) or zoomed in to `Scale = 1.25`.
* The `9:16` viewport window slides horizontally from $X_{anchor} = 0.25$ to $X_{anchor} = 0.75$ (and optionally pans back) using a smooth cosine ease-in-out curve:
  $$X(t) = X_{start} + (X_{end} - X_{start}) \cdot rac{1 - \cos(\pi \cdot t / T)}{2}$$

#### 5.3 Trajectory 3: Vertical Inspection Tilt (`SPATIAL_TILT_Y`)
Used for `ARCH_XRAY_CUTAWAY` and soil/object inspection shots (e.g., tilting down from the standing farmer to the cracked soil or emerging green sprout).
* Zooms to `Scale = 1.22` and glides the vertical anchor from $Y_{anchor} = 0.35$ (upper body) down to $Y_{anchor} = 0.72$ (ground/roots).

#### 5.4 Trajectory 4: Counter-Directional Sequence Pacing
To prevent visual monotony, consecutive shots alternate camera polarity:
* Shot 1: Slow Push-In (`1.00 -> 1.14`)
* Shot 2: Slow Pull-Back (`1.15 -> 1.00`)
* Shot 3: Horizontal Pan Left-to-Right
* Shot 4: Fast Punch-In (`1.00 -> 1.18` over 2.5s for high-tension beats)

---

### Module 6: Programmatic Compositing & Micro-Caption Renderer

1. **Eye-Tracked Center-of-Gravity Micro-Captions:**
   * Using word-level timestamps from forced alignment, captions are grouped into **1 to 2 words maximum**.
   * Rendered in clean white sans-serif typography (`NotoSansArabic-Bold` for Persian, `Inter-Bold` for English) with a subtle dark drop-shadow, positioned at the exact visual center of gravity (`X: 50%, Y: 52%`).
   * **Why this works:** The viewer's foveal vision stays locked on the center of the frame to read each word, allowing peripheral vision to absorb the whole illustration without eye fatigue.
2. **Procedural Atmospheric Overlays:**
   * Applies a global particle layer (floating dust motes or subtle film grain) and a dynamic radial vignette that darkens edges during high-stress narrative beats.

---

## 4. Complete JSON Schema for the v2 Scene-State Compiler

Below is the production JSON schema generated by Module 2 and consumed by Modules 3–6:

```json
{
  "project_id": "two_seeds_consistency_01",
  "language": "fa",
  "aspect_ratio": "9:16",
  "resolution": [768, 1376],
  "fps": 24,
  "narrative_structure": {
    "act_1_parable_end_sec": 55.0,
    "bridge_timestamp_sec": 55.5,
    "act_2_application_start_sec": 56.0
  },
  "scenes": [
    {
      "scene_id": "S04_SOIL_INSPECTION",
      "archetype": "ARCH_XRAY_CUTAWAY",
      "camera_trajectory": {
        "type": "SHARED_ZOOM_AND_TILT_Y",
        "scale_start": 1.02,
        "scale_end": 1.18,
        "y_anchor_start": 0.42,
        "y_anchor_end": 0.65
      },
      "states": [
        {
          "state_id": "S04_A",
          "generation_mode": "MASTER_KEYFRAME",
          "start_sec": 27.0,
          "end_sec": 32.5,
          "prompt": "Dark noir comic style, underground soil cross-section cutaway. Above ground, CHAR_PROTAGONIST (yellow spherical head #FFC928, straw hat, overalls) kneels pouring water drops from a clay pitcher, while 3 white-headed farmers laugh in background. Underground, a single seed absorbs glowing blue water drops (#29B6F6) with 4 glowing blue inward arrows.",
          "foley_sfx": ["water_drip_echo.wav", "distant_mocking_laugh.wav"]
        },
        {
          "state_id": "S04_B",
          "generation_mode": "INPAINT_STATE_EDIT",
          "parent_state": "S04_A",
          "transition_in": "CROSS_DISSOLVE_10F",
          "start_sec": 32.5,
          "end_sec": 36.0,
          "inpaint_instruction": "Keep background and kneeling farmer locked. Place clay pitcher on ground, remove laughing farmers and blue arrows, and expand white root network deep across the underground soil.",
          "foley_sfx": ["deep_earth_rumble_roots.wav"]
        }
      ]
    },
    {
      "scene_id": "S09_MODERN_DEEP_WORK",
      "archetype": "ARCH_CANONICAL_LIB",
      "canonical_asset_id": "CANON_WORK_01",
      "camera_trajectory": {
        "type": "SLOW_PUSH_IN",
        "scale_start": 1.00,
        "scale_end": 1.12
      },
      "states": [
        {
          "state_id": "S09_A",
          "generation_mode": "LOAD_FROM_CANONICAL_LIBRARY",
          "start_sec": 76.5,
          "end_sec": 79.0,
          "foley_sfx": ["keyboard_typing_soft.wav", "whoosh_transition.wav"]
        }
      ]
    }
  ]
}
```
