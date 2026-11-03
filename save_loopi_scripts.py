"""
Script to format and save the new LOOPI Sprint-01 Production Scripts (CNT-001 to CNT-005)
and validate against the SPIDER Studio contract.
"""

import sys
import subprocess
from pathlib import Path

# Ensure UTF-8
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

TARGET_FILE = Path(r"D:\code\SPIDER\b2c-content-gtm-system\b2c-content-gtm-system\projects\P-02_zerolab\context\05-scripts-batch.md")
PACK_FILE = Path(r"D:\code\SPIDER\scriptwriter_agent_pack\04_FEW_SHOT_GOLD_SCRIPTS.md")

DOCUMENT_CONTENT = """---
document_type: production_scripts_batch
source_roadmap: 03-editorial-roadmap.md
creative_system: 04-creative-system.md
sprint: Sprint-01
target_style: Warm Scientific Maker (LOOPI Host)
---

# Production Scripts Batch — Sprint-01 (CNT-001…005 / SHD-01A…02B)

Human-readable AV scripts with exact Beat Intent, timings, SFX cues, and scene descriptions.
The machine contract is appended in the ````json script_blocks```` block below and validated by `contracts/validate.py`.

---

## CNT-001 (SHD-01A): کابوس حبس هوا در مجسمه‌های پیچیده (The Nightmare of Trapped Air in Complex Sculpts)
- **Series:** روایت‌های کارگاه (Workshop Chronicles — PIL-01)
- **Skeleton:** `parable_bridge` | **Format:** `explainer_reel` | **Duration:** 41.5s | **KPI:** `shares`
- **Hook:** نمای ماکرو از پارگی قالب سیلیکونی و شکستن دست مجسمه حین خروج از قالب در استودیوی روشن.

| Timecode | Act | Spoken Narration (fa) | On-Screen Text | SFX Cue | Scene Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 00:00–04.5 | act_1_parable | فیگور پیچیده‌ای که دو هفته پای ساختش نشستی، توی اولین قالب‌گیری تیکه‌تیکه میشه. | فاجعه‌ی قالب‌گیری | `silicone_tear_snap` | Macro close-up in a warm ivory studio (#E9DDC9): maker's hands pulling a complex figurine from a one-piece mold; silicone tears and the figure's arm snaps off, highlighted in Wax Rose (#DCA69A). |
| 04.5–09.0 | act_1_parable | سازنده به هوای قالب‌گیریِ راحت، کل مجسمه رو یکجا داخل سیلیکون غرق می‌کنه. | قالبِ یک‌تکه | `viscous_pour_heavy` | Clean workbench in Mold Taupe (#B99D80) tones: liquid silicone pouring over an intricate multi-limbed sculpture inside a tall cylindrical cup. |
| 09.0–14.0 | act_1_parable | سیلیکون میره لای انگشت‌ها و زیرِ شونه‌ی مجسمه قفل میشه و راهِ فراری نداره. | قفلِ سیلیکون | `rubber_tension_creak` | 3D illustrative cutaway: translucent silicone cured tightly inside deep undercuts between fingers and shoulders, shaded in Wax Rose (#DCA69A). |
| 14.0–19.0 | act_1_parable | موقع بیرون کشیدنِ ماکت، هم دیواره‌ی قالب پاره میشه و هم دستِ قطعه می‌شکنه. | پارگیِ قالب | `ceramic_crack_soft` | Locked-off comparison shot: torn silicone shreds stuck inside the figurine's undercuts beside a broken resin cast with missing limbs. |
| 19.0–23.5 | act_1_parable | توی هر بار ریخته‌گری هم، حباب‌های درشتِ هوا دقیقاً توی همون شکاف‌ها زندانی میشن. | تله‌ی حباب | `bubble_pop_subtle` | Cross-section diagram in Charcoal (#26221E) line work showing pockets of air trapped under the raised arms during resin pouring. |
| 23.5–27.0 | bridge | توی کارگاه‌های حرفه‌ای شمع و رزین، هیچ‌وقت با فرم‌های پیچیده این‌طوری نمی‌جنگن... | قانونِ کارگاه | `soft_tonal_chime` | Warm medium shot: LOOPI in matte Warm Ivory (#E9DDC9) standing on the workbench with a calm, thoughtful expression, pointing gently toward the complex figurine. |
| 27.0–32.0 | act_2_application | راه‌حل مهندسیِ رابرت تولونه «قانون تجزیه» است: فرمِ پیچیده رو به استوانه‌های ساده بشکن. | قانونِ تجزیه | `clean_slice_click` | Exploded 3D view: the complex figurine separates cleanly along clear axes into three simple cylindrical volumes (head, torso, arms) highlighted in Sage (#89917B). |
| 32.0–37.0 | act_2_application | دست و سر و تنه جدا قالب‌گیری میشن؛ بدونِ آندرکات، بدونِ حباب و در پنج ثانیه مونتاژ. | حبابِ صفر | `tactile_demold_pop` | Process flow animation: three small, simple molds releasing flawless cast parts that snap together seamlessly in 5 seconds. |
| 37.0–41.5 | act_2_application | برای گرفتنِ شابلونِ تفکیکِ قطعاتِ پیچیده، همین الان کلمه‌ی «شکستن» رو کامنت کن. | کامنت: شکستن | `warm_studio_outro` | Final takeaway frame: completed flawless sculpture on a Mold Taupe (#B99D80) plinth; LOOPI gives a pleased nod beside a clean Charcoal (#26221E) label. |

---

## CNT-002 (SHD-01B): قانون شیب صعودی رزین (The Uphill Resin Slope Rule)
- **Series:** فیزیک ریخته‌گری بی‌نقص (The Flawless Cast Physics — PIL-02)
- **Skeleton:** `parable_bridge` | **Format:** `explainer_reel` | **Duration:** 41.0s | **KPI:** `saves`
- **Hook:** نمای برش‌خورده از حبس شدن حباب هوا زیر سقف افقی قالبِ صاف روی میز.

| Timecode | Act | Spoken Narration (fa) | On-Screen Text | SFX Cue | Scene Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 00:00–04.5 | act_1_parable | اگه قالبت رو صاف روی میز بذاری، خودت داری حباب‌ها رو زیرِ کار زندانی می‌کنی! | تله‌ی میزِ صاف | `liquid_pour_steady` | 3D cutaway view in a warm ivory studio (#E9DDC9): a silicone mold sitting completely flat (0 degrees) on a level workbench as liquid resin pours inside. |
| 04.5–09.0 | act_1_parable | وقتی رزین یا موم رو داخلِ قالبِ تراز می‌ریزی، مایع به صورتِ افقی جلو میره. | حرکتِ افقی | `fluid_ripple_soft` | Macro cross-section: the flat horizontal fluid front advancing across the bottom floor of the cavity. |
| 09.0–14.0 | act_1_parable | به محضِ رسیدن به اولین پله‌ی نود درجه، موجِ مایع راهِ فرارِ هوا رو می‌بنده. | زاویه‌ی ۹۰ درجه | `air_trap_seal` | Technical diagram with Charcoal (#26221E) callouts: resin hits a 90-degree internal step, sealing an air pocket highlighted in Wax Rose (#DCA69A). |
| 14.0–19.0 | act_1_parable | یک حفره‌ی بزرگِ هوا زیرِ سقفِ قالب حبس میشه و لبه‌ی قطعه خورده‌شده درمیاد. | لبه‌ی ناقص | `demold_defect_thud` | Close-up of the demolded cast part: a deep missing corner void shaded in Wax Rose (#DCA69A) ruining the clean geometry. |
| 19.0–23.5 | act_1_parable | هر چقدر هم به بدنه ضربه بزنی، اون حباب از زیرِ سقفِ افقی تکون نمی‌خوره. | ضربه‌ی بی‌فایده | `finger_tap_silicone` | Real process shot: maker's fingers tapping the side of the flat silicone mold while the trapped bubble in the cutaway stays motionless. |
| 23.5–27.0 | bridge | فکر می‌کنی متریالت خرابه یا دستگاهِ وکیوم کم داری؟ نه، زاویه‌ی قالبت غلطه... | زاویه‌ی غلط | `soft_tonal_chime` | Medium shot: LOOPI looking curious with a slight head tilt beside the flat mold, pointing toward an angle protractor graphic. |
| 27.0–32.0 | act_2_application | طبقِ «قانونِ شیبِ صعودی»، قالب رو موقعِ ریخته‌گری دقیقاً سی درجه کج نگه دار. | شیبِ ۳۰ درجه | `wooden_wedge_slide` | A Mold Taupe (#B99D80) 30-degree wedge slides under the mold; clean Charcoal (#26221E) arc label displays "30°". |
| 32.0–37.0 | act_2_application | این‌طوری مایع از پایین‌ترین نقطه بالا میاد و مثلِ جارو، هوا رو به خروجی هل میده. | رانشِ طبیعیِ هوا | `smooth_uphill_flow` | 3D cutaway simulation in Sage (#89917B): resin flows uphill along the 30-degree slope, smoothly pushing air bubbles out through the top vent. |
| 37.0–41.0 | act_2_application | این پست رو سیو کن تا دفعه‌ی بعد، قالبت رو با زاویه‌ی سی درجه پر کنی. | سیو برای بعد | `warm_studio_outro` | Macro shot of a razor-sharp, bubble-free cast edge on the warm ivory workbench; LOOPI smiles softly in the background. |

---

## CNT-003 (SHD-01C): راز هواکش حلقه‌ای زیر چانه (The Loop Vent Secret)
- **Series:** فیزیک ریخته‌گری بی‌نقص (The Flawless Cast Physics — PIL-02)
- **Skeleton:** `parable_bridge` | **Format:** `explainer_reel` | **Duration:** 41.5s | **KPI:** `comments`
- **Hook:** نمای نزدیک از خط درز زشت قالب روی صورت یک مجسمه و خراب شدن بافت چهره با سنباده.

| Timecode | Act | Spoken Narration (fa) | On-Screen Text | SFX Cue | Scene Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 00:00–04.5 | act_1_parable | چرا همیشه خطِ درزِ قالب، صاف میفته وسطِ صورتِ مجسمه یا شمعِ دفرمه‌ات؟ | زخم روی صورت | `sandpaper_scrape_harsh` | Extreme macro close-up in warm studio light: a sculptural bust candle with a raised seam line running directly across the nose and lips, highlighted in Wax Rose (#DCA69A). |
| 04.5–09.0 | act_1_parable | زیرِ چانه و نوکِ بینی، نقاطِ کوری هستن که هوا موقعِ ریخته‌گری توشون گیر می‌افته. | تله‌ی زیرِ چانه | `bubble_trap_low` | 3D cross-section of an inverted portrait mold: air pocket trapped inside the upward chin undercut, marked in Wax Rose (#DCA69A). |
| 09.0–14.0 | act_1_parable | سازنده برای فرار دادنِ این حباب، خطِ برشِ قالب رو مستقیم از وسطِ صورت رد می‌کنه. | برش از صورت | `blade_cut_silicone` | Top-down view: a surgical blade slicing a parting line straight down the center of the sculpture's face mold. |
| 14.0–19.0 | act_1_parable | نتیجه؟ یک پلیسه‌ی ضخیم روی لب و گونه می‌مونه که مجبوری با سنباده بغلش کنی. | پلیسه‌ی ضخیم | `resin_flash_snap` | Close-up on the cast piece showing rough flash along the facial profile on a Warm Ivory (#E9DDC9) surface. |
| 19.0–23.5 | act_1_parable | اما اولین حرکتِ سنباده، تمامِ بافتِ ظریفِ پوست و جزئیاتِ چهره رو برای همیشه محو می‌کنه. | نابودیِ جزئیات | `sandpaper_rub_dull` | Split comparison: crisp original sculpt vs. chalky, flattened nose and lips ruined by sanding. |
| 23.5–27.0 | bridge | خطِ درز روی صورتِ کار، یعنی مرگِ ارزشِ هنری و قیمتیِ محصول در اینستاگرام... | افتِ ارزشِ کار | `soft_tonal_chime` | Medium shot: LOOPI with a concerned expression inspecting the scarred sculpture on the Mold Taupe (#B99D80) workbench. |
| 27.0–32.0 | act_2_application | راه‌حلِ مهندسی «کانالِ هواکشِ حلقه‌ای» است: یک مفتولِ مومیِ یک‌ونیم میلی‌متری بردار. | هواکشِ حلقه‌ای | `wax_wire_bend` | Macro shot: artisan hands holding a flexible 1.5mm wax wire, labeled in Charcoal (#26221E) typography. |
| 32.0–37.0 | act_2_application | از زیرِ چانه به سینه پل بزن تا هوا فرار کنه و صورت کاملاً بی‌درز بمونه. | صورتِ بی‌درز | `air_vent_whoosh_soft` | 3D cutaway in Sage (#89917B): U-shaped wax loop bridges the chin to the chest; trapped air escapes smoothly while the face remains untouched by parting lines. |
| 37.0–41.5 | act_2_application | برای دریافتِ دیاگرامِ جایگذاریِ کانال‌های هواکش، کلمه‌ی «هواکش» رو کامنت کن. | کامنت: هواکش | `warm_studio_outro` | A fingernail effortlessly snips off the tiny 1.5mm sprue pip under the chin, revealing a pristine sculpture as LOOPI smiles approvingly. |

---

## CNT-004 (SHD-02A): تکنیک تزریق چندرنگ بدون درز (Multi-Pour Color Blocking Without Seams)
- **Series:** تکنیک‌های تولید پرسرعت (High-Speed Studio Production — PIL-04)
- **Skeleton:** `parable_bridge` | **Format:** `explainer_reel` | **Duration:** 41.5s | **KPI:** `comments`
- **Hook:** شره کردن رنگ قلم‌مو روی نوک و چشم فیگور دست‌ساز و پوسته شدن رنگ.

| Timecode | Act | Spoken Narration (fa) | On-Screen Text | SFX Cue | Scene Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 00:00–04.5 | act_1_parable | هنوز چشم و نوکِ فیگورهای دست‌سازِت رو بعد از تولید با قلم‌مو رنگ می‌کنی؟ | رنگ‌آمیزیِ دستی؟ | `brush_stroke_wet` | Macro close-up in a warm ivory studio (#E9DDC9): a fine paintbrush trembling as it tries to paint the beak of a cast owl figurine; paint bleeds over the edge, highlighted in Wax Rose (#DCA69A). |
| 04.5–09.0 | act_1_parable | رنگ زدنِ روی سطحِ رزین، مرزهای کج‌ومعوج میندازه و رنگ توی شیارها شره می‌کنه. | شره کردنِ رنگ | `liquid_drip_small` | Extreme close-up showing uneven brush marks and pigment pooling inside the fine feather grooves. |
| 09.0–14.0 | act_1_parable | بدتر از اون، با اولین تماسِ دست یا شست‌وشو، لایه‌ی رنگ پوسته میده و می‌ریزه. | پوسته‌شدنِ رنگ | `paint_flake_peel` | A thumb rubs across the painted beak and flakes of acrylic paint peel right off the smooth resin surface. |
| 14.0–19.0 | act_1_parable | برای یه سفارشِ پنجاه‌تایی، باید روزها وقت بذاری و تک‌تکِ قطعات رو با ذره‌بین رنگ کنی. | اتلافِ وقت | `clock_tick_fast` | Overhead shot of fifty unpainted white owl castings lined up on a Mold Taupe (#B99D80) workbench beside messy paint cups. |
| 19.0–23.5 | act_1_parable | آخرش هم کار به جای یک محصولِ کلکسیونی، شبیه کاردستیِ ارزان به نظر میاد. | ظاهرِ دست‌دوم | `dull_thud_soft` | Side-by-side view of two hand-painted owls with mismatched, smudged eyes. |
| 23.5–27.0 | bridge | رنگ‌آمیزیِ دستی بعد از تولید، سرعتِ کارگاهت رو پنج برابر کم می‌کنه و سودت رو می‌خوره... | توقفِ تولید | `soft_tonal_chime` | Medium shot: LOOPI standing beside a clean pipette and a one-piece silicone mold, gesturing calmly toward the mold cavity. |
| 27.0–32.0 | act_2_application | تکنیکِ «تزریقِ چندمرحله‌ای»: قالب رو کج کن و با پیپت، چند قطره رزینِ رنگی توی نوک بریز. | تزریقِ مرحله‌ای | `pipette_drop_precise` | 3D cutaway view in Sage (#89917B): the one-piece mold is tilted; a pipette places drops of amber-tinted resin precisely into the beak recess. |
| 32.0–37.0 | act_2_application | پنج دقیقه صبر کن تا حالتِ ژل بگیره، بعد رنگِ بدنه رو بریز تا پیوندِ مولکولی بگیرن. | پیوندِ مولکولی | `chemical_bond_hum` | Infographic overlay in Charcoal (#26221E) shows "5 min Gel Phase"; ivory body resin is poured over the gelled beak, bonding chemically without seams. |
| 37.0–41.5 | act_2_application | جدولِ زمان‌بندیِ ژل‌تایم برای انواعِ رزین‌ها رو با کامنت کردنِ کلمه‌ی «چندرنگ» بگیر. | کامنت: چندرنگ | `tactile_demold_pop` | Macro demold reveal: a multi-colored owl pops out of the single-piece mold with razor-sharp color boundaries and zero paint; LOOPI nods with a warm smile. |

---

## CNT-005 (SHD-02B): برش رهایی در آندرکات‌های تیز (The Beak Undercut Relief Cut)
- **Series:** فیزیک ریخته‌گری بی‌نقص (The Flawless Cast Physics — PIL-02)
- **Skeleton:** `parable_bridge` | **Format:** `explainer_reel` | **Duration:** 41.0s | **KPI:** `saves`
- **Hook:** کنده شدن گوشت داخلی قالب سیلیکونی توسط نوک تیز قطعه در زمان خروج از قالب.

| Timecode | Act | Spoken Narration (fa) | On-Screen Text | SFX Cue | Scene Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 00:00–04.5 | act_1_parable | موقعِ بیرون کشیدنِ قطعه، یه صدای تق میاد و تیکه‌ای از گوشتِ قالب کنده میشه! | کنده‌شدنِ قالب | `silicone_rip_sharp` | Macro close-up in a Warm Ivory (#E9DDC9) studio: a freshly demolded bird figurine with a chunk of torn silicone rubber stuck under its sharp beak, highlighted in Wax Rose (#DCA69A). |
| 04.5–09.0 | act_1_parable | جاهایی مثلِ نوکِ تیزِ پرنده یا لبه‌های برگشته‌ی شمع، نقاطِ گیردارِ قالب هستن. | نقاطِ گیردار | `tension_stretch_low` | 3D cross-section: a sharp hook-shaped undercut on the master model deeply embedded inside the silicone wall. |
| 09.0–14.0 | act_1_parable | سازنده به امیدِ خاصیتِ کشسانیِ سیلیکون، قطعه رو با زور از دهانه‌ی تنگ بیرون می‌کشه. | کشیدن با زور | `rubber_strain_creak` | Cutaway animation: upward pull arrows in Charcoal (#26221E) show extreme shear stress concentrating in Wax Rose (#DCA69A) right at the sharp beak tip. |
| 14.0–19.0 | act_1_parable | لبه‌ی تیزِ قطعه مثلِ چاقو عمل می‌کنه و دیواره‌ی داخلیِ سیلیکون رو از ریشه می‌بُره. | برشِ داخلی | `blade_nick_rubber` | Macro zoom on the internal cavity wall: the sharp resin edge slices into the stretched silicone rubber during extraction. |
| 19.0–23.5 | act_1_parable | فقط با چند بار دیمولد کردن، دویست گرم سیلیکونِ گران‌قیمتت راهیِ سطلِ زباله میشه. | مرگِ قالب | `trash_drop_heavy` | Ruined silicone mold with a jagged internal cavity hole sitting on the Mold Taupe (#B99D80) workbench. |
| 23.5–27.0 | bridge | سیلیکون در کششِ آزاد قویه، اما در برابرِ تنشِ برشیِ لبه‌های تیز کاملاً بی‌دفاعه... | تنشِ برشی | `soft_tonal_chime` | Medium shot: LOOPI holding a surgical #11 scalpel calmly, pointing toward the outer rim of a fresh silicone mold. |
| 27.0–32.0 | act_2_application | راه‌حلِ مهندسی «برشِ رهاییِ موضعی» است: پشتِ نقطه‌ی گیر، یک شکافِ دو میلی‌متری بزن. | برشِ رهایی | `scalpel_slice_clean` | Macro overhead shot: a sharp blade makes a controlled 2mm relief slit directly behind the beak undercut, highlighted in Sage (#89917B) with a "2 mm" Charcoal (#26221E) callout. |
| 32.0–37.0 | act_2_application | موقعِ خروج، دهانه بدونِ کشش باز میشه و موقعِ ریخته‌گری، شکاف خودبه‌خود کیپ می‌مونه. | خروجِ بی‌تنش | `silicone_release_smooth` | Dual-state comparison: left side shows the slit hinging open effortlessly during demold; right side shows the elastic slit self-sealing tightly when banded. |
| 37.0–41.0 | act_2_application | این پست رو سیو کن تا دفعه‌ی بعد، قالب‌هات سرِ لبه‌های تیز پاره نشن. | سیو برای بعد | `warm_studio_outro` | Intact silicone mold beside a flawless cast bird figurine on the Warm Ivory (#E9DDC9) surface; LOOPI gives an approving smile. |

---

```json script_blocks
[
  {
    "content_id": "CNT-001",
    "narrative_skeleton": "parable_bridge",
    "series_name": "روایت‌های کارگاه",
    "format_archetype": "explainer_reel",
    "target_duration_seconds": 41.5,
    "estimated_word_count": 115,
    "primary_kpi": "shares",
    "selected_hook": {
      "spoken": "فیگور پیچیده‌ای که دو هفته پای ساختش نشستی، توی اولین قالب‌گیری تیکه‌تیکه میشه.",
      "visual_frame_1": "Macro close-up in a warm ivory studio (#E9DDC9): maker's hands pulling a complex figurine from a one-piece mold; silicone tears and the figure's arm snaps off, highlighted in Wax Rose (#DCA69A).",
      "on_screen_text": "فاجعه‌ی قالب‌گیری"
    },
    "act_1_parable_end_pct": 56.6,
    "bridge_pivot_phrase": "توی کارگاه‌های حرفه‌ای شمع و رزین، هیچ‌وقت با فرم‌های پیچیده این‌طوری نمی‌جنگن...",
    "act_2_application": "Applying Robert Tolone's Break It Down principle by decomposing complex undercut sculptures into simple cylindrical volumes for zero-bubble, zero-tear molding.",
    "beats": [
      {
        "beat_id": "B01",
        "act_marker": "act_1_parable",
        "start_sec": 0.0,
        "end_sec": 4.5,
        "spoken_narration": "فیگور پیچیده‌ای که دو هفته پای ساختش نشستی، توی اولین قالب‌گیری تیکه‌تیکه میشه.",
        "on_screen_text": "فاجعه‌ی قالب‌گیری",
        "sfx_cue": "silicone_tear_snap",
        "scene_description": "Macro close-up in a warm ivory studio (#E9DDC9): maker's hands pulling a complex figurine from a one-piece mold; silicone tears and the figure's arm snaps off, highlighted in Wax Rose (#DCA69A).",
        "archetype_hint": "ARCH_STATE_PAIR"
      },
      {
        "beat_id": "B02",
        "act_marker": "act_1_parable",
        "start_sec": 4.5,
        "end_sec": 9.0,
        "spoken_narration": "سازنده به هوای قالب‌گیریِ راحت، کل مجسمه رو یکجا داخل سیلیکون غرق می‌کنه.",
        "on_screen_text": "قالبِ یک‌تکه",
        "sfx_cue": "viscous_pour_heavy",
        "scene_description": "Clean workbench in Mold Taupe (#B99D80) tones: liquid silicone pouring over an intricate multi-limbed sculpture inside a tall cylindrical cup.",
        "archetype_hint": "ARCH_STATE_PAIR"
      },
      {
        "beat_id": "B03",
        "act_marker": "act_1_parable",
        "start_sec": 9.0,
        "end_sec": 14.0,
        "spoken_narration": "سیلیکون میره لای انگشت‌ها و زیرِ شونه‌ی مجسمه قفل میشه و راهِ فراری نداره.",
        "on_screen_text": "قفلِ سیلیکون",
        "sfx_cue": "rubber_tension_creak",
        "scene_description": "3D illustrative cutaway: translucent silicone cured tightly inside deep undercuts between fingers and shoulders, shaded in Wax Rose (#DCA69A).",
        "archetype_hint": "ARCH_XRAY_CUTAWAY"
      },
      {
        "beat_id": "B04",
        "act_marker": "act_1_parable",
        "start_sec": 14.0,
        "end_sec": 19.0,
        "spoken_narration": "موقع بیرون کشیدنِ ماکت، هم دیواره‌ی قالب پاره میشه و هم دستِ قطعه می‌شکنه.",
        "on_screen_text": "پارگیِ قالب",
        "sfx_cue": "ceramic_crack_soft",
        "scene_description": "Locked-off comparison shot: torn silicone shreds stuck inside the figurine's undercuts beside a broken resin cast with missing limbs.",
        "archetype_hint": "ARCH_SPLIT_COMPARE"
      },
      {
        "beat_id": "B05",
        "act_marker": "act_1_parable",
        "start_sec": 19.0,
        "end_sec": 23.5,
        "spoken_narration": "توی هر بار ریخته‌گری هم، حباب‌های درشتِ هوا دقیقاً توی همون شکاف‌ها زندانی میشن.",
        "on_screen_text": "تله‌ی حباب",
        "sfx_cue": "bubble_pop_subtle",
        "scene_description": "Cross-section diagram in Charcoal (#26221E) line work showing pockets of air trapped under the raised arms during resin pouring.",
        "archetype_hint": "ARCH_XRAY_CUTAWAY"
      },
      {
        "beat_id": "B06",
        "act_marker": "bridge",
        "start_sec": 23.5,
        "end_sec": 27.0,
        "spoken_narration": "توی کارگاه‌های حرفه‌ای شمع و رزین، هیچ‌وقت با فرم‌های پیچیده این‌طوری نمی‌جنگن...",
        "on_screen_text": "قانونِ کارگاه",
        "sfx_cue": "soft_tonal_chime",
        "scene_description": "Warm medium shot: LOOPI in matte Warm Ivory (#E9DDC9) standing on the workbench with a calm, thoughtful expression, pointing gently toward the complex figurine.",
        "archetype_hint": "ARCH_STATE_PAIR"
      },
      {
        "beat_id": "B07",
        "act_marker": "act_2_application",
        "start_sec": 27.0,
        "end_sec": 32.0,
        "spoken_narration": "راه‌حل مهندسیِ رابرت تولونه «قانون تجزیه» است: فرمِ پیچیده رو به استوانه‌های ساده بشکن.",
        "on_screen_text": "قانونِ تجزیه",
        "sfx_cue": "clean_slice_click",
        "scene_description": "Exploded 3D view: the complex figurine separates cleanly along clear axes into three simple cylindrical volumes (head, torso, arms) highlighted in Sage (#89917B).",
        "archetype_hint": "ARCH_MULTI_ANGLE"
      },
      {
        "beat_id": "B08",
        "act_marker": "act_2_application",
        "start_sec": 32.0,
        "end_sec": 37.0,
        "spoken_narration": "دست و سر و تنه جدا قالب‌گیری میشن؛ بدونِ آندرکات، بدونِ حباب و در پنج ثانیه مونتاژ.",
        "on_screen_text": "حبابِ صفر",
        "sfx_cue": "tactile_demold_pop",
        "scene_description": "Process flow animation: three small, simple molds releasing flawless cast parts that snap together seamlessly in 5 seconds.",
        "archetype_hint": "ARCH_STATE_PAIR"
      },
      {
        "beat_id": "B09",
        "act_marker": "act_2_application",
        "start_sec": 37.0,
        "end_sec": 41.5,
        "spoken_narration": "برای گرفتنِ شابلونِ تفکیکِ قطعاتِ پیچیده، همین الان کلمه‌ی «شکستن» رو کامنت کن.",
        "on_screen_text": "کامنت: شکستن",
        "sfx_cue": "warm_studio_outro",
        "scene_description": "Final takeaway frame: completed flawless sculpture on a Mold Taupe (#B99D80) plinth; LOOPI gives a pleased nod beside a clean Charcoal (#26221E) label.",
        "archetype_hint": "ARCH_RECAP_LOOP"
      }
    ]
  },
  {
    "content_id": "CNT-002",
    "narrative_skeleton": "parable_bridge",
    "series_name": "فیزیک ریخته‌گری بی‌نقص",
    "format_archetype": "explainer_reel",
    "target_duration_seconds": 41.0,
    "estimated_word_count": 114,
    "primary_kpi": "saves",
    "selected_hook": {
      "spoken": "اگه قالبت رو صاف روی میز بذاری، خودت داری حباب‌ها رو زیرِ کار زندانی می‌کنی!",
      "visual_frame_1": "3D cutaway view in a warm ivory studio (#E9DDC9): a silicone mold sitting completely flat (0 degrees) on a level workbench as liquid resin pours inside.",
      "on_screen_text": "تله‌ی میزِ صاف"
    },
    "act_1_parable_end_pct": 57.3,
    "bridge_pivot_phrase": "فکر می‌کنی متریالت خرابه یا دستگاهِ وکیوم کم داری؟ نه، زاویه‌ی قالبت غلطه...",
    "act_2_application": "Tilting the mold at a 30-degree incline during pouring so gravity and uphill fluid progression naturally sweep air pockets out of 90-degree corners.",
    "beats": [
      {
        "beat_id": "B01",
        "act_marker": "act_1_parable",
        "start_sec": 0.0,
        "end_sec": 4.5,
        "spoken_narration": "اگه قالبت رو صاف روی میز بذاری، خودت داری حباب‌ها رو زیرِ کار زندانی می‌کنی!",
        "on_screen_text": "تله‌ی میزِ صاف",
        "sfx_cue": "liquid_pour_steady",
        "scene_description": "3D cutaway view in a warm ivory studio (#E9DDC9): a silicone mold sitting completely flat (0 degrees) on a level workbench as liquid resin pours inside.",
        "archetype_hint": "ARCH_XRAY_CUTAWAY"
      },
      {
        "beat_id": "B02",
        "act_marker": "act_1_parable",
        "start_sec": 4.5,
        "end_sec": 9.0,
        "spoken_narration": "وقتی رزین یا موم رو داخلِ قالبِ تراز می‌ریزی، مایع به صورتِ افقی جلو میره.",
        "on_screen_text": "حرکتِ افقی",
        "sfx_cue": "fluid_ripple_soft",
        "scene_description": "Macro cross-section: the flat horizontal fluid front advancing across the bottom floor of the cavity.",
        "archetype_hint": "ARCH_XRAY_CUTAWAY"
      },
      {
        "beat_id": "B03",
        "act_marker": "act_1_parable",
        "start_sec": 9.0,
        "end_sec": 14.0,
        "spoken_narration": "به محضِ رسیدن به اولین پله‌ی نود درجه، موجِ مایع راهِ فرارِ هوا رو می‌بنده.",
        "on_screen_text": "زاویه‌ی ۹۰ درجه",
        "sfx_cue": "air_trap_seal",
        "scene_description": "Technical diagram with Charcoal (#26221E) callouts: resin hits a 90-degree internal step, sealing an air pocket highlighted in Wax Rose (#DCA69A).",
        "archetype_hint": "ARCH_XRAY_CUTAWAY"
      },
      {
        "beat_id": "B04",
        "act_marker": "act_1_parable",
        "start_sec": 14.0,
        "end_sec": 19.0,
        "spoken_narration": "یک حفره‌ی بزرگِ هوا زیرِ سقفِ قالب حبس میشه و لبه‌ی قطعه خورده‌شده درمیاد.",
        "on_screen_text": "لبه‌ی ناقص",
        "sfx_cue": "demold_defect_thud",
        "scene_description": "Close-up of the demolded cast part: a deep missing corner void shaded in Wax Rose (#DCA69A) ruining the clean geometry.",
        "archetype_hint": "ARCH_STATE_PAIR"
      },
      {
        "beat_id": "B05",
        "act_marker": "act_1_parable",
        "start_sec": 19.0,
        "end_sec": 23.5,
        "spoken_narration": "هر چقدر هم به بدنه ضربه بزنی، اون حباب از زیرِ سقفِ افقی تکون نمی‌خوره.",
        "on_screen_text": "ضربه‌ی بی‌فایده",
        "sfx_cue": "finger_tap_silicone",
        "scene_description": "Real process shot: maker's fingers tapping the side of the flat silicone mold while the trapped bubble in the cutaway stays motionless.",
        "archetype_hint": "ARCH_STATE_PAIR"
      },
      {
        "beat_id": "B06",
        "act_marker": "bridge",
        "start_sec": 23.5,
        "end_sec": 27.0,
        "spoken_narration": "فکر می‌کنی متریالت خرابه یا دستگاهِ وکیوم کم داری؟ نه، زاویه‌ی قالبت غلطه...",
        "on_screen_text": "زاویه‌ی غلط",
        "sfx_cue": "soft_tonal_chime",
        "scene_description": "Medium shot: LOOPI looking curious with a slight head tilt beside the flat mold, pointing toward an angle protractor graphic.",
        "archetype_hint": "ARCH_STATE_PAIR"
      },
      {
        "beat_id": "B07",
        "act_marker": "act_2_application",
        "start_sec": 27.0,
        "end_sec": 32.0,
        "spoken_narration": "طبقِ «قانونِ شیبِ صعودی»، قالب رو موقعِ ریخته‌گری دقیقاً سی درجه کج نگه دار.",
        "on_screen_text": "شیبِ ۳۰ درجه",
        "sfx_cue": "wooden_wedge_slide",
        "scene_description": "A Mold Taupe (#B99D80) 30-degree wedge slides under the mold; clean Charcoal (#26221E) arc label displays 30 degrees.",
        "archetype_hint": "ARCH_STATE_PAIR"
      },
      {
        "beat_id": "B08",
        "act_marker": "act_2_application",
        "start_sec": 32.0,
        "end_sec": 37.0,
        "spoken_narration": "این‌طوری مایع از پایین‌ترین نقطه بالا میاد و مثلِ جارو، هوا رو به خروجی هل میده.",
        "on_screen_text": "رانشِ طبیعیِ هوا",
        "sfx_cue": "smooth_uphill_flow",
        "scene_description": "3D cutaway simulation in Sage (#89917B): resin flows uphill along the 30-degree slope, smoothly pushing air bubbles out through the top vent.",
        "archetype_hint": "ARCH_XRAY_CUTAWAY"
      },
      {
        "beat_id": "B09",
        "act_marker": "act_2_application",
        "start_sec": 37.0,
        "end_sec": 41.0,
        "spoken_narration": "این پست رو سیو کن تا دفعه‌ی بعد، قالبت رو با زاویه‌ی سی درجه پر کنی.",
        "on_screen_text": "سیو برای بعد",
        "sfx_cue": "warm_studio_outro",
        "scene_description": "Macro shot of a razor-sharp, bubble-free cast edge on the warm ivory workbench; LOOPI smiles softly in the background.",
        "archetype_hint": "ARCH_RECAP_LOOP"
      }
    ]
  },
  {
    "content_id": "CNT-003",
    "narrative_skeleton": "parable_bridge",
    "series_name": "فیزیک ریخته‌گری بی‌نقص",
    "format_archetype": "explainer_reel",
    "target_duration_seconds": 41.5,
    "estimated_word_count": 116,
    "primary_kpi": "comments",
    "selected_hook": {
      "spoken": "چرا همیشه خطِ درزِ قالب، صاف میفته وسطِ صورتِ مجسمه یا شمعِ دفرمه‌ات؟",
      "visual_frame_1": "Extreme macro close-up in warm studio light: a sculptural bust candle with a raised seam line running directly across the nose and lips, highlighted in Wax Rose (#DCA69A).",
      "on_screen_text": "زخم روی صورت"
    },
    "act_1_parable_end_pct": 56.6,
    "bridge_pivot_phrase": "خطِ درز روی صورتِ کار، یعنی مرگِ ارزشِ هنری و قیمتیِ محصول در اینستاگرام...",
    "act_2_application": "Attaching a 1.5mm U-shaped wax wire loop vent from the chin undercut to the chest so trapped air escapes without cutting a seam line across the face.",
    "beats": [
      {
        "beat_id": "B01",
        "act_marker": "act_1_parable",
        "start_sec": 0.0,
        "end_sec": 4.5,
        "spoken_narration": "چرا همیشه خطِ درزِ قالب، صاف میفته وسطِ صورتِ مجسمه یا شمعِ دفرمه‌ات؟",
        "on_screen_text": "زخم روی صورت",
        "sfx_cue": "sandpaper_scrape_harsh",
        "scene_description": "Extreme macro close-up in warm studio light: a sculptural bust candle with a raised seam line running directly across the nose and lips, highlighted in Wax Rose (#DCA69A).",
        "archetype_hint": "ARCH_STATE_PAIR"
      },
      {
        "beat_id": "B02",
        "act_marker": "act_1_parable",
        "start_sec": 4.5,
        "end_sec": 9.0,
        "spoken_narration": "زیرِ چانه و نوکِ بینی، نقاطِ کوری هستن که هوا موقعِ ریخته‌گری توشون گیر می‌افته.",
        "on_screen_text": "تله‌ی زیرِ چانه",
        "sfx_cue": "bubble_trap_low",
        "scene_description": "3D cross-section of an inverted portrait mold: air pocket trapped inside the upward chin undercut, marked in Wax Rose (#DCA69A).",
        "archetype_hint": "ARCH_XRAY_CUTAWAY"
      },
      {
        "beat_id": "B03",
        "act_marker": "act_1_parable",
        "start_sec": 9.0,
        "end_sec": 14.0,
        "spoken_narration": "سازنده برای فرار دادنِ این حباب، خطِ برشِ قالب رو مستقیم از وسطِ صورت رد می‌کنه.",
        "on_screen_text": "برش از صورت",
        "sfx_cue": "blade_cut_silicone",
        "scene_description": "Top-down view: a surgical blade slicing a parting line straight down the center of the sculpture's face mold.",
        "archetype_hint": "ARCH_STATE_PAIR"
      },
      {
        "beat_id": "B04",
        "act_marker": "act_1_parable",
        "start_sec": 14.0,
        "end_sec": 19.0,
        "spoken_narration": "نتیجه؟ یک پلیسه‌ی ضخیم روی لب و گونه می‌مونه که مجبوری با سنباده بغلش کنی.",
        "on_screen_text": "پلیسه‌ی ضخیم",
        "sfx_cue": "resin_flash_snap",
        "scene_description": "Close-up on the cast piece showing rough flash along the facial profile on a Warm Ivory (#E9DDC9) surface.",
        "archetype_hint": "ARCH_STATE_PAIR"
      },
      {
        "beat_id": "B05",
        "act_marker": "act_1_parable",
        "start_sec": 19.0,
        "end_sec": 23.5,
        "spoken_narration": "اما اولین حرکتِ سنباده، تمامِ بافتِ ظریفِ پوست و جزئیاتِ چهره رو برای همیشه محو می‌کنه.",
        "on_screen_text": "نابودیِ جزئیات",
        "sfx_cue": "sandpaper_rub_dull",
        "scene_description": "Split comparison: crisp original sculpt vs. chalky, flattened nose and lips ruined by sanding.",
        "archetype_hint": "ARCH_SPLIT_COMPARE"
      },
      {
        "beat_id": "B06",
        "act_marker": "bridge",
        "start_sec": 23.5,
        "end_sec": 27.0,
        "spoken_narration": "خطِ درز روی صورتِ کار، یعنی مرگِ ارزشِ هنری و قیمتیِ محصول در اینستاگرام...",
        "on_screen_text": "افتِ ارزشِ کار",
        "sfx_cue": "soft_tonal_chime",
        "scene_description": "Medium shot: LOOPI with a concerned expression inspecting the scarred sculpture on the Mold Taupe (#B99D80) workbench.",
        "archetype_hint": "ARCH_STATE_PAIR"
      },
      {
        "beat_id": "B07",
        "act_marker": "act_2_application",
        "start_sec": 27.0,
        "end_sec": 32.0,
        "spoken_narration": "راه‌حلِ مهندسی «کانالِ هواکشِ حلقه‌ای» است: یک مفتولِ مومیِ یک‌ونیم میلی‌متری بردار.",
        "on_screen_text": "هواکشِ حلقه‌ای",
        "sfx_cue": "wax_wire_bend",
        "scene_description": "Macro shot: artisan hands holding a flexible 1.5mm wax wire, labeled in Charcoal (#26221E) typography.",
        "archetype_hint": "ARCH_STATE_PAIR"
      },
      {
        "beat_id": "B08",
        "act_marker": "act_2_application",
        "start_sec": 32.0,
        "end_sec": 37.0,
        "spoken_narration": "از زیرِ چانه به سینه پل بزن تا هوا فرار کنه و صورت کاملاً بی‌درز بمونه.",
        "on_screen_text": "صورتِ بی‌درز",
        "sfx_cue": "air_vent_whoosh_soft",
        "scene_description": "3D cutaway in Sage (#89917B): U-shaped wax loop bridges the chin to the chest; trapped air escapes smoothly while the face remains untouched by parting lines.",
        "archetype_hint": "ARCH_XRAY_CUTAWAY"
      },
      {
        "beat_id": "B09",
        "act_marker": "act_2_application",
        "start_sec": 37.0,
        "end_sec": 41.5,
        "spoken_narration": "برای دریافتِ دیاگرامِ جایگذاریِ کانال‌های هواکش، کلمه‌ی «هواکش» رو کامنت کن.",
        "on_screen_text": "کامنت: هواکش",
        "sfx_cue": "warm_studio_outro",
        "scene_description": "A fingernail effortlessly snips off the tiny 1.5mm sprue pip under the chin, revealing a pristine sculpture as LOOPI smiles approvingly.",
        "archetype_hint": "ARCH_RECAP_LOOP"
      }
    ]
  },
  {
    "content_id": "CNT-004",
    "narrative_skeleton": "parable_bridge",
    "series_name": "تکنیک‌های تولید پرسرعت",
    "format_archetype": "explainer_reel",
    "target_duration_seconds": 41.5,
    "estimated_word_count": 118,
    "primary_kpi": "comments",
    "selected_hook": {
      "spoken": "هنوز چشم و نوکِ فیگورهای دست‌سازِت رو بعد از تولید با قلم‌مو رنگ می‌کنی؟",
      "visual_frame_1": "Macro close-up in a warm ivory studio (#E9DDC9): a fine paintbrush trembling as it tries to paint the beak of a cast owl figurine; paint bleeds over the edge, highlighted in Wax Rose (#DCA69A).",
      "on_screen_text": "رنگ‌آمیزیِ دستی؟"
    },
    "act_1_parable_end_pct": 56.6,
    "bridge_pivot_phrase": "رنگ‌آمیزیِ دستی بعد از تولید، سرعتِ کارگاهت رو پنج برابر کم می‌کنه و سودت رو می‌خوره...",
    "act_2_application": "Using multi-pour color blocking during the 5-minute resin gel phase inside a tilted mold to create permanent molecular bonds between colors without brushwork.",
    "beats": [
      {
        "beat_id": "B01",
        "act_marker": "act_1_parable",
        "start_sec": 0.0,
        "end_sec": 4.5,
        "spoken_narration": "هنوز چشم و نوکِ فیگورهای دست‌سازِت رو بعد از تولید با قلم‌مو رنگ می‌کنی؟",
        "on_screen_text": "رنگ‌آمیزیِ دستی؟",
        "sfx_cue": "brush_stroke_wet",
        "scene_description": "Macro close-up in a warm ivory studio (#E9DDC9): a fine paintbrush trembling as it tries to paint the beak of a cast owl figurine; paint bleeds over the edge, highlighted in Wax Rose (#DCA69A).",
        "archetype_hint": "ARCH_STATE_PAIR"
      },
      {
        "beat_id": "B02",
        "act_marker": "act_1_parable",
        "start_sec": 4.5,
        "end_sec": 9.0,
        "spoken_narration": "رنگ زدنِ روی سطحِ رزین، مرزهای کج‌ومعوج میندازه و رنگ توی شیارها شره می‌کنه.",
        "on_screen_text": "شره کردنِ رنگ",
        "sfx_cue": "liquid_drip_small",
        "scene_description": "Extreme close-up showing uneven brush marks and pigment pooling inside the fine feather grooves.",
        "archetype_hint": "ARCH_STATE_PAIR"
      },
      {
        "beat_id": "B03",
        "act_marker": "act_1_parable",
        "start_sec": 9.0,
        "end_sec": 14.0,
        "spoken_narration": "بدتر از اون، با اولین تماسِ دست یا شست‌وشو، لایه‌ی رنگ پوسته میده و می‌ریزه.",
        "on_screen_text": "پوسته‌شدنِ رنگ",
        "sfx_cue": "paint_flake_peel",
        "scene_description": "A thumb rubs across the painted beak and flakes of acrylic paint peel right off the smooth resin surface.",
        "archetype_hint": "ARCH_STATE_PAIR"
      },
      {
        "beat_id": "B04",
        "act_marker": "act_1_parable",
        "start_sec": 14.0,
        "end_sec": 19.0,
        "spoken_narration": "برای یه سفارشِ پنجاه‌تایی، باید روزها وقت بذاری و تک‌تکِ قطعات رو با ذره‌بین رنگ کنی.",
        "on_screen_text": "اتلافِ وقت",
        "sfx_cue": "clock_tick_fast",
        "scene_description": "Overhead shot of fifty unpainted white owl castings lined up on a Mold Taupe (#B99D80) workbench beside messy paint cups.",
        "archetype_hint": "ARCH_WIDE_PAN"
      },
      {
        "beat_id": "B05",
        "act_marker": "act_1_parable",
        "start_sec": 19.0,
        "end_sec": 23.5,
        "spoken_narration": "آخرش هم کار به جای یک محصولِ کلکسیونی، شبیه کاردستیِ ارزان به نظر میاد.",
        "on_screen_text": "ظاهرِ دست‌دوم",
        "sfx_cue": "dull_thud_soft",
        "scene_description": "Side-by-side view of two hand-painted owls with mismatched, smudged eyes.",
        "archetype_hint": "ARCH_SPLIT_COMPARE"
      },
      {
        "beat_id": "B06",
        "act_marker": "bridge",
        "start_sec": 23.5,
        "end_sec": 27.0,
        "spoken_narration": "رنگ‌آمیزیِ دستی بعد از تولید، سرعتِ کارگاهت رو پنج برابر کم می‌کنه و سودت رو می‌خوره...",
        "on_screen_text": "توقفِ تولید",
        "sfx_cue": "soft_tonal_chime",
        "scene_description": "Medium shot: LOOPI standing beside a clean pipette and a one-piece silicone mold, gesturing calmly toward the mold cavity.",
        "archetype_hint": "ARCH_STATE_PAIR"
      },
      {
        "beat_id": "B07",
        "act_marker": "act_2_application",
        "start_sec": 27.0,
        "end_sec": 32.0,
        "spoken_narration": "تکنیکِ «تزریقِ چندمرحله‌ای»: قالب رو کج کن و با پیپت، چند قطره رزینِ رنگی توی نوک بریز.",
        "on_screen_text": "تزریقِ مرحله‌ای",
        "sfx_cue": "pipette_drop_precise",
        "scene_description": "3D cutaway view in Sage (#89917B): the one-piece mold is tilted; a pipette places drops of amber-tinted resin precisely into the beak recess.",
        "archetype_hint": "ARCH_XRAY_CUTAWAY"
      },
      {
        "beat_id": "B08",
        "act_marker": "act_2_application",
        "start_sec": 32.0,
        "end_sec": 37.0,
        "spoken_narration": "پنج دقیقه صبر کن تا حالتِ ژل بگیره، بعد رنگِ بدنه رو بریز تا پیوندِ مولکولی بگیرن.",
        "on_screen_text": "پیوندِ مولکولی",
        "sfx_cue": "chemical_bond_hum",
        "scene_description": "Infographic overlay in Charcoal (#26221E) shows 5 min Gel Phase; ivory body resin is poured over the gelled beak, bonding chemically without seams.",
        "archetype_hint": "ARCH_XRAY_CUTAWAY"
      },
      {
        "beat_id": "B09",
        "act_marker": "act_2_application",
        "start_sec": 37.0,
        "end_sec": 41.5,
        "spoken_narration": "جدولِ زمان‌بندیِ ژل‌تایم برای انواعِ رزین‌ها رو با کامنت کردنِ کلمه‌ی «چندرنگ» بگیر.",
        "on_screen_text": "کامنت: چندرنگ",
        "sfx_cue": "tactile_demold_pop",
        "scene_description": "Macro demold reveal: a multi-colored owl pops out of the single-piece mold with razor-sharp color boundaries and zero paint; LOOPI nods with a warm smile.",
        "archetype_hint": "ARCH_RECAP_LOOP"
      }
    ]
  },
  {
    "content_id": "CNT-005",
    "narrative_skeleton": "parable_bridge",
    "series_name": "فیزیک ریخته‌گری بی‌نقص",
    "format_archetype": "explainer_reel",
    "target_duration_seconds": 41.0,
    "estimated_word_count": 115,
    "primary_kpi": "saves",
    "selected_hook": {
      "spoken": "موقعِ بیرون کشیدنِ قطعه، یه صدای تق میاد و تیکه‌ای از گوشتِ قالب کنده میشه!",
      "visual_frame_1": "Macro close-up in a Warm Ivory (#E9DDC9) studio: a freshly demolded bird figurine with a chunk of torn silicone rubber stuck under its sharp beak, highlighted in Wax Rose (#DCA69A).",
      "on_screen_text": "کنده‌شدنِ قالب"
    },
    "act_1_parable_end_pct": 57.3,
    "bridge_pivot_phrase": "سیلیکون در کششِ آزاد قویه، اما در برابرِ تنشِ برشیِ لبه‌های تیز کاملاً بی‌دفاعه...",
    "act_2_application": "Making a controlled 2mm local relief cut behind sharp undercuts so the silicone hinges open without shear tearing during demold and self-seals when clamped.",
    "beats": [
      {
        "beat_id": "B01",
        "act_marker": "act_1_parable",
        "start_sec": 0.0,
        "end_sec": 4.5,
        "spoken_narration": "موقعِ بیرون کشیدنِ قطعه، یه صدای تق میاد و تیکه‌ای از گوشتِ قالب کنده میشه!",
        "on_screen_text": "کنده‌شدنِ قالب",
        "sfx_cue": "silicone_rip_sharp",
        "scene_description": "Macro close-up in a Warm Ivory (#E9DDC9) studio: a freshly demolded bird figurine with a chunk of torn silicone rubber stuck under its sharp beak, highlighted in Wax Rose (#DCA69A).",
        "archetype_hint": "ARCH_STATE_PAIR"
      },
      {
        "beat_id": "B02",
        "act_marker": "act_1_parable",
        "start_sec": 4.5,
        "end_sec": 9.0,
        "spoken_narration": "جاهایی مثلِ نوکِ تیزِ پرنده یا لبه‌های برگشته‌ی شمع، نقاطِ گیردارِ قالب هستن.",
        "on_screen_text": "نقاطِ گیردار",
        "sfx_cue": "tension_stretch_low",
        "scene_description": "3D cross-section: a sharp hook-shaped undercut on the master model deeply embedded inside the silicone wall.",
        "archetype_hint": "ARCH_XRAY_CUTAWAY"
      },
      {
        "beat_id": "B03",
        "act_marker": "act_1_parable",
        "start_sec": 9.0,
        "end_sec": 14.0,
        "spoken_narration": "سازنده به امیدِ خاصیتِ کشسانیِ سیلیکون، قطعه رو با زور از دهانه‌ی تنگ بیرون می‌کشه.",
        "on_screen_text": "کشیدن با زور",
        "sfx_cue": "rubber_strain_creak",
        "scene_description": "Cutaway animation: upward pull arrows in Charcoal (#26221E) show extreme shear stress concentrating in Wax Rose (#DCA69A) right at the sharp beak tip.",
        "archetype_hint": "ARCH_XRAY_CUTAWAY"
      },
      {
        "beat_id": "B04",
        "act_marker": "act_1_parable",
        "start_sec": 14.0,
        "end_sec": 19.0,
        "spoken_narration": "لبه‌ی تیزِ قطعه مثلِ چاقو عمل می‌کنه و دیواره‌ی داخلیِ سیلیکون رو از ریشه می‌بُره.",
        "on_screen_text": "برشِ داخلی",
        "sfx_cue": "blade_nick_rubber",
        "scene_description": "Macro zoom on the internal cavity wall: the sharp resin edge slices into the stretched silicone rubber during extraction.",
        "archetype_hint": "ARCH_STATE_PAIR"
      },
      {
        "beat_id": "B05",
        "act_marker": "act_1_parable",
        "start_sec": 19.0,
        "end_sec": 23.5,
        "spoken_narration": "فقط با چند بار دیمولد کردن، دویست گرم سیلیکونِ گران‌قیمتت راهیِ سطلِ زباله میشه.",
        "on_screen_text": "مرگِ قالب",
        "sfx_cue": "trash_drop_heavy",
        "scene_description": "Ruined silicone mold with a jagged internal cavity hole sitting on the Mold Taupe (#B99D80) workbench.",
        "archetype_hint": "ARCH_STATE_PAIR"
      },
      {
        "beat_id": "B06",
        "act_marker": "bridge",
        "start_sec": 23.5,
        "end_sec": 27.0,
        "spoken_narration": "سیلیکون در کششِ آزاد قویه، اما در برابرِ تنشِ برشیِ لبه‌های تیز کاملاً بی‌دفاعه...",
        "on_screen_text": "تنشِ برشی",
        "sfx_cue": "soft_tonal_chime",
        "scene_description": "Medium shot: LOOPI holding a surgical #11 scalpel calmly, pointing toward the outer rim of a fresh silicone mold.",
        "archetype_hint": "ARCH_STATE_PAIR"
      },
      {
        "beat_id": "B07",
        "act_marker": "act_2_application",
        "start_sec": 27.0,
        "end_sec": 32.0,
        "spoken_narration": "راه‌حلِ مهندسی «برشِ رهاییِ موضعی» است: پشتِ نقطه‌ی گیر، یک شکافِ دو میلی‌متری بزن.",
        "on_screen_text": "برشِ رهایی",
        "sfx_cue": "scalpel_slice_clean",
        "scene_description": "Macro overhead shot: a sharp blade makes a controlled 2mm relief slit directly behind the beak undercut, highlighted in Sage (#89917B) with a 2mm Charcoal (#26221E) callout.",
        "archetype_hint": "ARCH_MULTI_ANGLE"
      },
      {
        "beat_id": "B08",
        "act_marker": "act_2_application",
        "start_sec": 32.0,
        "end_sec": 37.0,
        "spoken_narration": "موقعِ خروج، دهانه بدونِ کشش باز میشه و موقعِ ریخته‌گری، شکاف خودبه‌خود کیپ می‌مونه.",
        "on_screen_text": "خروجِ بی‌تنش",
        "sfx_cue": "silicone_release_smooth",
        "scene_description": "Dual-state comparison: left side shows the slit hinging open effortlessly during demold; right side shows the elastic slit self-sealing tightly when banded.",
        "archetype_hint": "ARCH_SPLIT_COMPARE"
      },
      {
        "beat_id": "B09",
        "act_marker": "act_2_application",
        "start_sec": 37.0,
        "end_sec": 41.0,
        "spoken_narration": "این پست رو سیو کن تا دفعه‌ی بعد، قالب‌هات سرِ لبه‌های تیز پاره نشن.",
        "on_screen_text": "سیو برای بعد",
        "sfx_cue": "warm_studio_outro",
        "scene_description": "Intact silicone mold beside a flawless cast bird figurine on the Warm Ivory (#E9DDC9) surface; LOOPI gives an approving smile.",
        "archetype_hint": "ARCH_RECAP_LOOP"
      }
    ]
  }
]
```
"""

def main():
    TARGET_FILE.parent.mkdir(parents=True, exist_ok=True)
    PACK_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    TARGET_FILE.write_text(DOCUMENT_CONTENT, encoding="utf-8")
    print(f"[OK] Written to {TARGET_FILE}")
    
    PACK_FILE.write_text(DOCUMENT_CONTENT, encoding="utf-8")
    print(f"[OK] Written to {PACK_FILE}")
    
    # Run validator
    validator_path = Path(r"D:\code\SPIDER\b2c-content-gtm-system\b2c-content-gtm-system\contracts\validate.py")
    res = subprocess.run([sys.executable, str(validator_path), "script", str(TARGET_FILE)], capture_output=True, text=True)
    print("Validation STDOUT:", res.stdout.strip())
    if res.stderr.strip():
        print("Validation STDERR:", res.stderr.strip())
    if res.returncode == 0:
        print("[SUCCESS] All 5 LOOPI scripts PASSED contract validation!")
    else:
        print("[FAILED] Validation error code:", res.returncode)

if __name__ == "__main__":
    main()
