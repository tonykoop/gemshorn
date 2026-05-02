#!/usr/bin/env python3
"""Generate the slip-cast gemshorn family build packet."""

from __future__ import annotations

import csv
import datetime as dt
import html
import json
import math
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any


PACKET_DIR = Path(__file__).resolve().parent
TODAY = dt.date.today().isoformat()

BASE_MIDI = 72  # C5
BASE_FREQ_HZ = 440.0 * 2 ** ((BASE_MIDI - 69) / 12)
SPEED_OF_SOUND_IN_S = 13549.0
SHRINKAGE = 0.12

BASE = {
    "centerline_length_in": 9.25,
    "wide_od_in": 1.55,
    "tip_od_in": 0.36,
    "wall_in": 0.13,
    "window_width_in": 0.43,
    "window_height_in": 0.14,
    "windway_height_in": 0.034,
    "labium_setback_in": 0.43,
}

FAMILY_DEFS = [
    {
        "id": "GEM-SC-F3",
        "name": "Bass F",
        "key": "F3",
        "midi": 53,
        "line": "modern slip-cast consort",
        "playing_support": "bench, lap, or simple sling; large horn",
    },
    {
        "id": "GEM-SC-C4",
        "name": "Tenor C",
        "key": "C4",
        "midi": 60,
        "line": "modern slip-cast consort",
        "playing_support": "two-hand standing or seated",
    },
    {
        "id": "GEM-SC-F4",
        "name": "Alto F",
        "key": "F4",
        "midi": 65,
        "line": "modern slip-cast consort",
        "playing_support": "comfortable hand instrument",
    },
    {
        "id": "GEM-SC-C5",
        "name": "Soprano C",
        "key": "C5",
        "midi": 72,
        "line": "modern slip-cast consort baseline",
        "playing_support": "primary pilot size",
    },
    {
        "id": "GEM-SC-F5",
        "name": "Sopranino F",
        "key": "F5",
        "midi": 77,
        "line": "modern slip-cast consort",
        "playing_support": "small hand instrument; hole accuracy is critical",
    },
]

HISTORICAL_DEF = {
    "id": "GEM-HIST-G4",
    "name": "Historical Clay/Horn Archetype",
    "key": "G4",
    "midi": 67,
    "line": "historically informed 4 front plus thumb study",
    "playing_support": "small hand instrument; exact historical pitch is not known",
}

MODERN_HOLES = [
    # hole, next note interval, position from labium as fraction of centerline length, face
    ("H1", 2, 0.479, "front distal", "open first for scale degree 2"),
    ("H2", 4, 0.424, "front", "open second for scale degree 3"),
    ("H3", 5, 0.369, "front", "open third for scale degree 4"),
    ("H4", 7, 0.316, "front", "open fourth for scale degree 5"),
    ("H5", 9, 0.263, "front", "open fifth for scale degree 6"),
    ("H6", 11, 0.210, "front", "open sixth for scale degree 7"),
    ("H7", 12, 0.157, "front proximal", "open seventh for octave"),
    ("T1", 14, 0.157, "back thumb", "opens to ninth or acts as high-note/tuning vent"),
]

HISTORICAL_HOLES = [
    ("F1", 2, 0.430, "front distal", "whole-tone hole"),
    ("F2", 4, 0.340, "front", "third hole"),
    ("F3", 5, 0.270, "front", "fourth hole; omit or wax for stricter 3-front interpretation"),
    ("F4", 7, 0.205, "front proximal", "fifth hole"),
    ("T1", 12, 0.205, "back thumb", "octave-area vent; tune empirically"),
]

SOURCES = [
    {
        "label": "Horace Fitzpatrick, The Gemshorn: a Reconstruction",
        "url": "https://www.cambridge.org/core/journals/proceedings-of-the-royal-musical-association/article/gemshorn-a-reconstruction/0AD60F0FE7748111C8455FA2F4DD1CC3",
        "notes": "Defines the gemshorn as a fipple instrument made from animal horn and calls out the stopped inverted cone bore. Used as the boundary-condition anchor.",
    },
    {
        "label": "Early Music Muse, The gemshorn: a short history",
        "url": "https://earlymusicmuse.com/gemshorn/",
        "notes": "Summarizes the open-end fipple construction, four-hole historical evidence, and the 1455 clay gemshorn-like find. Used for authenticity notes.",
    },
    {
        "label": "Cincinnati Early Music, Medieval Gemshorn",
        "url": "https://cincinnatiearlymusic.com/gemshorn.html",
        "notes": "Contrasts historical four-hole evidence with modern recorder-like reconstructions and consort families. Used to separate historical and modern lines.",
    },
    {
        "label": "Baltimore Recorders, Information about the Gemshorn",
        "url": "https://www.baltimorerecorders.org/gemshorns.html",
        "notes": "Describes front holes, thumb hole, whistle/fipple, tuning ring, and the lack of an outlet other than whistle and fingerholes. Used for construction details.",
    },
    {
        "label": "Institut fuer Musikforschung Wuerzburg, Lo 29-31 Gemshoerner",
        "url": "https://www.musikwissenschaft.uni-wuerzburg.de/musikinstrumente/bestand/inventarliste/lo29-31-gemshoerner/",
        "notes": "Gives measured modern HFK gemshorns in g, d1, and g1 and cautions that modern gemshorns are reconstruction products. Used as dimensional sanity check.",
    },
]


@dataclass
class Formula:
    value: str


def midi_to_freq(midi: int | float) -> float:
    return 440.0 * 2 ** ((float(midi) - 69.0) / 12.0)


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def wall_for_scale(scale: float) -> float:
    return clamp(BASE["wall_in"] * scale**0.65, 0.11, 0.24)


def frustum_volume_in3(length: float, wide_id: float, tip_id: float) -> float:
    r1 = wide_id / 2.0
    r2 = max(tip_id, 0.02) / 2.0
    return math.pi * length / 3.0 * (r1 * r1 + r1 * r2 + r2 * r2)


def window_effective_length(area_in2: float, wall_in: float) -> float:
    equiv_radius = math.sqrt(area_in2 / math.pi)
    return wall_in + 0.85 * equiv_radius


def conductance_for_diameter(diameter_in: float, wall_in: float) -> float:
    radius = diameter_in / 2.0
    area = math.pi * radius * radius
    leff = wall_in + 0.85 * radius
    return area / leff


def diameter_from_conductance(conductance: float, wall_in: float) -> float:
    # Solve G = pi*r^2 / (wall + 0.85*r) for r.
    radius = (
        0.85 * conductance
        + math.sqrt((0.85 * conductance) ** 2 + 4 * math.pi * conductance * wall_in)
    ) / (2 * math.pi)
    return 2.0 * radius


def compute_size(defn: dict[str, Any]) -> dict[str, Any]:
    freq = midi_to_freq(defn["midi"])
    scale = BASE_FREQ_HZ / freq
    wall = wall_for_scale(scale)
    length = BASE["centerline_length_in"] * scale
    wide_od = BASE["wide_od_in"] * scale
    tip_od = BASE["tip_od_in"] * scale
    wide_id = max(0.20, wide_od - 2 * wall)
    tip_id = max(0.03, tip_od - 2 * wall)
    volume = frustum_volume_in3(length, wide_id, tip_id)
    window_w = BASE["window_width_in"] * scale
    window_h = BASE["window_height_in"] * scale
    window_area = window_w * window_h
    window_leff = window_effective_length(window_area, wall)
    g_base = window_area / window_leff
    return {
        **defn,
        "freq_hz": freq,
        "scale": scale,
        "fired_centerline_length_in": length,
        "master_centerline_length_in": length / (1 - SHRINKAGE),
        "fired_wide_od_in": wide_od,
        "master_wide_od_in": wide_od / (1 - SHRINKAGE),
        "fired_tip_od_in": tip_od,
        "fired_wall_in": wall,
        "fired_wide_id_in": wide_id,
        "fired_tip_id_in": tip_id,
        "fired_internal_volume_in3": volume,
        "fired_internal_volume_ml": volume * 16.387064,
        "window_width_in": window_w,
        "window_height_in": window_h,
        "window_area_in2": window_area,
        "window_effective_length_in": window_leff,
        "base_conductance_in": g_base,
        "windway_height_in": clamp(BASE["windway_height_in"] * scale**0.5, 0.026, 0.060),
        "labium_setback_in": BASE["labium_setback_in"] * scale,
        "green_shrink_factor": 1 / (1 - SHRINKAGE),
    }


def compute_hole_rows(size: dict[str, Any], hole_defs: list[tuple[str, int, float, str, str]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    prev_interval = 0
    for hole, interval, pos_frac, face, note in hole_defs:
        target_factor = 2 ** (interval / 6.0)
        prev_factor = 2 ** (prev_interval / 6.0)
        increment_g = size["base_conductance_in"] * (target_factor - prev_factor)
        diameter = diameter_from_conductance(increment_g, size["fired_wall_in"])
        rows.append(
            {
                "instrument_id": size["id"],
                "key": size["key"],
                "hole": hole,
                "face": face,
                "target_interval_semitones": interval,
                "previous_interval_semitones": prev_interval,
                "position_pct_from_labium": pos_frac,
                "fired_position_from_labium_in": pos_frac * size["fired_centerline_length_in"],
                "master_position_from_labium_in": pos_frac * size["master_centerline_length_in"],
                "fired_diameter_in": diameter,
                "greenware_drill_start_in": diameter / (1 - SHRINKAGE),
                "incremental_conductance_in": increment_g,
                "hole_leff_in": size["fired_wall_in"] + 0.85 * diameter / 2.0,
                "note": note,
            }
        )
        prev_interval = interval
    return rows


def round_value(value: Any, places: int = 4) -> Any:
    if isinstance(value, float):
        return round(value, places)
    return value


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({key: round_value(row.get(key, "")) for key in fieldnames})


def csv_markdown(path: Path, max_rows: int | None = None) -> str:
    rows: list[list[str]] = []
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.reader(handle):
            rows.append(row)
            if max_rows is not None and len(rows) > max_rows:
                break
    if not rows:
        return ""
    width = max(len(row) for row in rows)
    padded = [row + [""] * (width - len(row)) for row in rows]
    out = [
        "| " + " | ".join(cell.replace("|", "\\|") for cell in padded[0]) + " |",
        "| " + " | ".join(["---"] * width) + " |",
    ]
    for row in padded[1:]:
        out.append("| " + " | ".join(cell.replace("|", "\\|") for cell in row) + " |")
    return "\n".join(out)


def render_table(headers: list[str], rows: list[list[Any]], places: int = 3) -> str:
    out = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        cells = []
        for value in row:
            if isinstance(value, float):
                cells.append(f"{value:.{places}f}")
            else:
                cells.append(str(value))
        out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out)


def write_design_md(family: list[dict[str, Any]], historical: dict[str, Any]) -> None:
    rows = [
        [
            item["id"],
            item["key"],
            item["freq_hz"],
            item["fired_centerline_length_in"],
            item["master_centerline_length_in"],
            item["fired_wide_od_in"],
            item["fired_internal_volume_ml"],
            item["window_width_in"],
            item["window_height_in"],
        ]
        for item in family
    ]
    family_table = render_table(
        [
            "ID",
            "Key",
            "Hz",
            "Fired L in",
            "Master L in",
            "Wide OD in",
            "Volume ml",
            "Window W in",
            "Window H in",
        ],
        rows,
    )
    text = f"""# Slip-Cast Gemshorn Family Build Packet

Generated: {TODAY}

Packet root: `{PACKET_DIR}`

## Scope

This packet gives you a historically informed gemshorn build path and a practical slip-cast consort family. The two are intentionally separated:

- **Historical archetype:** short curved horn or clay horn, open wide end closed with a fipple/block, closed pointed tip, limited holes, limited range. This is the authenticity target.
- **Slip-cast family:** repeatable ceramic bodies in F/C consort sizes with seven front holes and one thumb/tuning vent. This is the practical ensemble and production target, and it is marked as a modern reconstruction approach.

## Deliverables

- `gemshorn-design-table.xlsx` - parametric workbook with inputs, family dimensions, hole schedules, mold scaling, and validation targets.
- `family-spec.csv` - fired and master dimensions for the slip-cast family.
- `hole-schedule-modern.csv` - modern seven-front-plus-thumb hole diameters and positions.
- `hole-schedule-historical.csv` - historically informed four-front-plus-thumb pilot schedule.
- `drawings/` - SVG shop drawings for body section, family scale, hole layout, voicing detail, mold schematic, and visual BOM.
- `cad/gemshorn_family.scad` - OpenSCAD starter for master geometry.
- `cnc/mold-master-cam-plan.md` - CAM/print/fixture planning notes.
- `bom.csv`, `sourcing.csv`, `cut-list.csv`, `validation.csv` - production and validation tables.
- `assembly-manual.md`, `mold-and-slip-casting-plan.md`, `tuning-and-fingering.md`, `authenticity-notes.md` - shop-facing instructions.
- `authentic-horn-build-plan.md`, `horn-blank-spec.csv` - natural-horn authentic build path and blank selection specs.
- `wolfram-starter.wl` - notebook-ready physics starter.

## Acoustic Model

The working model is a Helmholtz/vessel-flute model, not an open-open flute model:

```text
f = c/(2*pi) * sqrt(G_total / V)
G_total = sum(A_i / L_eff_i)
L_eff circular hole approx wall + 0.85*r
```

For a tuning hole with required incremental conductance `G`, the first-pass hole radius is:

```text
r = (0.85*G + sqrt((0.85*G)^2 + 4*pi*G*wall)) / (2*pi)
```

The body dimensions use geometric scaling from the soprano C5 prototype. That keeps volume, window area, hole area, and neck length in the same acoustic family. Final pitch still requires empirical tuning because ceramic shrinkage, glaze, fipple behavior, hole chamfer, and actual cavity volume dominate the last cents.

## Slip-Cast Family

{family_table}

## Historical Archetype

Prototype: `{historical["id"]}` in `{historical["key"]}`, fired centerline length `{historical["fired_centerline_length_in"]:.2f} in`, wide OD `{historical["fired_wide_od_in"]:.2f} in`, volume `{historical["fired_internal_volume_ml"]:.0f} ml`.

The historical model should be built first with waxable/reworkable holes. If you want the strictest Virdung/Agricola reading, make three front holes plus a back/thumb hole, then treat the fourth front hole in `hole-schedule-historical.csv` as an optional clay-find/modern-convenience variant.

## Manufacturing Assumptions

- Fired clay shrinkage: `{SHRINKAGE * 100:.1f}%` linear. Update this from your actual clay body test bars before committing to molds.
- Clay body: white stoneware or porcelain casting slip, cone 5/6 or cone 10 depending on shop practice.
- Wall: scaled from `{BASE["wall_in"]:.3f} in` at soprano C, clamped between `0.110 in` and `0.240 in`.
- Holes: cast-in undersize dimples or drill leather-hard to the greenware start diameters, then tune by opening slowly after bisque.
- Finish: exterior glaze only around body; keep windway, labium edge, tone-hole interiors, and seating surfaces unglazed or very lightly treated.

## Validation Gates

- Measure fired cavity volume by water fill before final tuning.
- Record closed note, all scale degrees, and high/tuning vent at 68 F reference or with temperature logged.
- Tune by opening holes only. Lower pitch by wax, removable clay-safe filler, or ring/vent control.
- Reject or rework bodies with warped windways, rounded labium edges, cracks at holes, or shrinkage outside the measured clay-body range.

## Open Decisions

- Actual clay body, firing cone, glaze schedule, and shrinkage test result.
- Whether the production family should be C/F consort, G/D historical consort, or both.
- Whether the tuning ring is a brass sleeve, leather wrap with rotating vent, or ceramic collar.
"""
    (PACKET_DIR / "design.md").write_text(text, encoding="utf-8")


def write_authenticity_notes() -> None:
    source_lines = "\n".join(
        f"- [{src['label']}]({src['url']}): {src['notes']}" for src in SOURCES
    )
    text = f"""# Authenticity Notes

Generated: {TODAY}

## What Counts As Authentic Here

For this packet, "authentic gemshorn" means a historically informed instrument rather than a museum-certified copy. The available evidence supports these constraints:

- The body is a short curved horn form, traditionally animal horn and plausibly ceramic in at least one late medieval find.
- It is blown from the wide/open end, which is closed by a fipple/block and voicing window.
- The pointed end stays closed, so the instrument behaves as a stopped inverted cone or vessel flute.
- The range is limited because it does not overblow like a recorder.
- The safest historical hole count is small. Four-hole evidence is stronger than the modern seven-front-hole consort layout.

## What Is Modern In This Packet

The slip-cast consort family uses modern reconstruction logic:

- Repeatable molded ceramic bodies rather than individual animal horns.
- Seven front holes plus a back thumb/tuning vent for ensemble usability.
- Equal-temperament C/F family targets.
- Spreadsheet-derived hole diameters and scaling.

That modern line is useful and buildable, but it should not be labeled as a direct 15th-century copy.

## Historically Informed Build Choices

- Make the first historical pilot in G4 because modern measured reconstructions around that register provide a dimensional sanity check.
- Use a waxed or replaceable tuning ring/vent near the voicing area. Historical and modern sources describe tuning by partially covering a vent/ring or thumb hole.
- Keep a soft, low-wind sound. Overblown recorder behavior is not expected.
- Keep exterior decoration restrained: polished horn, burnished ceramic, leather wrap, or simple incised marks. Avoid shiny glaze near the voicing.

## Source Notes

{source_lines}

## Provenance Warning

No file in this packet claims to reproduce an extant original gemshorn exactly. The historical record is sparse; this packet gives a traceable and tunable workshop path with explicit assumptions.
"""
    (PACKET_DIR / "authenticity-notes.md").write_text(text, encoding="utf-8")
    (PACKET_DIR / "sources.md").write_text(text, encoding="utf-8")


def write_authentic_horn_build_plan(historical: dict[str, Any], historical_holes: list[dict[str, Any]]) -> None:
    hole_table = render_table(
        ["Hole", "Face", "From labium in", "Final dia in", "Green/pilot dia in", "Target"],
        [
            [
                row["hole"],
                row["face"],
                row["fired_position_from_labium_in"],
                row["fired_diameter_in"],
                row["greenware_drill_start_in"],
                "+" + str(row["target_interval_semitones"]) + " semitones",
            ]
            for row in historical_holes
        ],
    )
    text = f"""# Authentic Natural-Horn Gemshorn Build Plan

Generated: {TODAY}

## Intent

This is the most historically conservative build path in the packet: a short curved horn body with a fipple/block at the wide end, closed pointed tip, limited hole count, and soft vessel-flute voice. Use domesticated cow, ox, goat, or sheep horn. Do not source endangered chamois or wild-animal horn.

## Target Prototype

- Prototype ID: `{historical["id"]}`
- Suggested starting pitch: `{historical["key"]}` at `{historical["freq_hz"]:.2f} Hz`
- Design centerline length: `{historical["fired_centerline_length_in"]:.2f} in`
- Wide OD target: `{historical["fired_wide_od_in"]:.2f} in`
- Internal volume target: `{historical["fired_internal_volume_ml"]:.0f} ml`
- Hole system: four front holes plus one back/thumb vent, with the third front hole optional for a stricter three-front-plus-thumb reconstruction.

## Horn Blank Selection

- Pick a horn with a naturally sealed or solid tip and enough length to trim back to pitch.
- Avoid cracks, deep delamination, insect damage, and extremely thin walls near the wide end.
- Prefer a smooth curve that lets the front holes sit under the hands without wrist strain.
- Wide-end OD should be near the target, but volume matters more than exterior size.
- Buy at least three blanks for the first working instrument; horn geometry varies too much for one-shot confidence.

## Cleaning And Prep

1. Remove loose core material mechanically.
2. Degrease with warm water and mild detergent. Avoid boiling unless you already know the horn tolerates it.
3. Dry completely.
4. Scrape, sand, or ream the interior only enough to remove soft material and stabilize the cavity.
5. Keep the tip closed. If the tip opens accidentally, plug it permanently and document the added volume.
6. Measure water-fill volume and update the design table notes.

## Wide-End Fipple

1. Square and flatten the wide-end seating plane enough to accept a block.
2. Fit a removable hardwood or plaster block.
3. Cut a low, even windway.
4. Cut the voicing window in the horn wall and form a crisp labium edge.
5. Use leather, cork, wax, or thread wrap to seal around the block.
6. Add a small tuning vent/ring only after the closed note speaks.

## Historical Hole Pilot

{hole_table}

For animal horn, use these as layout starting points, then tune empirically:

- Drill undersize first.
- Tune low to high.
- Lower over-sharp notes with wax while you learn the horn's response.
- Record the final hole diameter, position, and pitch in `validation.csv`.

## Tuning Workflow

1. Make the closed note speak with no finger holes open.
2. Adjust the fipple/block and window before drilling tone holes.
3. Drill F1 undersize, tune it, then move upward.
4. If the octave/back vent is too aggressive, reduce it with wax or make it a rotating collar vent.
5. Final-polish the mouth area only after tuning is stable.

## Finish

- Polish horn exterior by sanding through fine grits and buffing.
- Oil lightly only after all adhesive and block materials are compatible.
- Keep the windway dry, crisp, and free from oily residue.
- Label the finished instrument as a historically informed reconstruction, not a museum copy.
"""
    (PACKET_DIR / "authentic-horn-build-plan.md").write_text(text, encoding="utf-8")


def write_horn_blank_spec(historical: dict[str, Any]) -> None:
    rows = [
        {
            "use_case": "Historical G4 pilot",
            "preferred_material": "domesticated cow, ox, goat, or sheep horn",
            "blank_centerline_length_in": f"{historical['fired_centerline_length_in'] + 1.0:.2f} to {historical['fired_centerline_length_in'] + 4.0:.2f}",
            "wide_end_od_in": f"{historical['fired_wide_od_in'] * 0.85:.2f} to {historical['fired_wide_od_in'] * 1.25:.2f}",
            "minimum_wall_in": "0.070 near wide end after cleaning",
            "tip_condition": "closed or plug-friendly",
            "reject_if": "cracked, delaminated, moldy core, thin/transparent wall at voicing, severe twist under hands",
            "notes": "Buy several blanks; tune by measured volume and final holes",
        },
        {
            "use_case": "Small high historical pilot",
            "preferred_material": "goat or sheep horn",
            "blank_centerline_length_in": "7.5 to 10.5",
            "wide_end_od_in": "1.2 to 1.8",
            "minimum_wall_in": "0.055 near wide end after cleaning",
            "tip_condition": "closed",
            "reject_if": "too small for removable block or stable windway",
            "notes": "Good fast test for fipple and hole-count behavior",
        },
        {
            "use_case": "Lower/alto horn pilot",
            "preferred_material": "cow or ox horn",
            "blank_centerline_length_in": "13.5 to 18.0",
            "wide_end_od_in": "1.8 to 3.0",
            "minimum_wall_in": "0.080 near wide end after cleaning",
            "tip_condition": "closed or permanently pluggable",
            "reject_if": "wide end too oval to seal with a block",
            "notes": "Likely more playable than very small horns for first tuning tests",
        },
    ]
    write_csv(
        PACKET_DIR / "horn-blank-spec.csv",
        rows,
        [
            "use_case",
            "preferred_material",
            "blank_centerline_length_in",
            "wide_end_od_in",
            "minimum_wall_in",
            "tip_condition",
            "reject_if",
            "notes",
        ],
    )


def write_mold_plan() -> None:
    text = f"""# Mold And Slip-Casting Plan

Generated: {TODAY}

## Build Strategy

Use a sealed master for each size and make a two-part plaster mold with the split line along the outside curvature. The wide end acts as the pour opening and later receives the fipple/block system.

## Master Prep

1. Print or CNC the master from `cad/gemshorn_family.scad` dimensions.
2. Scale all fired dimensions by `1/(1 - shrinkage)`. The default packet value is `{1/(1-SHRINKAGE):.4f}`.
3. Add cast-in centerline marks, hole dimples, window outline, split-line marks, and registration witness marks.
4. Seal print layers with epoxy/primer/shellac until plaster cannot grip the surface.
5. Polish the master enough that a leather-hard cast releases without tearing.

## Mold Layout

- Two main plaster halves.
- Split line follows the low-stress side of the curved horn, avoiding the labium edge.
- Add at least three registration keys per side.
- Leave a broad pour mouth at the wide end.
- Add a removable insert or post only if your chosen shape traps the tip.
- Provide a small witness dimple at each hole location. Do not rely on cast-in final hole sizes for first prototypes.

## Casting Cycle

1. Dry mold fully before first pour.
2. Pour well-mixed casting slip through the wide end.
3. Time wall growth with test coupons, then drain.
4. Release at soft leather hard.
5. Open/clean the pour end and trim the fipple seat.
6. Drill pilot holes undersize using the greenware diameters in `hole-schedule-*.csv`.
7. Dry slowly with the wide end loosely covered for the first day.
8. Bisque fire.
9. Measure shrinkage, volume, mass, hole diameters, and closed-note pitch.
10. Tune by carefully opening holes. Keep all tuning notes in `validation.csv`.

## Fipple And Voicing Options

- **Authentic horn-style:** wood or plaster block fitted into the wide end; leather wrap forms or seals the windway.
- **Ceramic production:** slip-cast body plus fitted hardwood block, removable for service and tuning.
- **All ceramic:** possible, but higher risk. It requires a precise windway insert and more shrinkage control.

## Clay And Finish Rules

- Do not glaze inside the windway or on the labium edge.
- Use exterior-only glaze or burnish/oil finish for prototypes.
- Radius handling edges, but keep the labium clean and crisp.
- Fire sample bars with every clay batch.

## Failure Modes To Watch

- Rounded labium edge: weak or unstable tone.
- Warped windway: airy or non-speaking note.
- Oversized initial holes: sharp pitch with no clean lowering path except wax.
- Thin wall near big bass holes: cracks during drying.
- Heavy glaze around holes: pitch shift and sluggish response.
"""
    (PACKET_DIR / "mold-and-slip-casting-plan.md").write_text(text, encoding="utf-8")


def write_tuning_and_fingering() -> None:
    text = """# Tuning And Fingering

## Modern Slip-Cast Consort

Hole names run from the distal/lower front hand toward the mouth:

```text
T1 on back behind H7

Mouth / fipple
H7 H6 H5 H4 H3 H2 H1
Tip closed
```

First-pass diatonic opening sequence:

| Sounding note above tonic | Fingering idea |
| --- | --- |
| 0 semitones | all holes closed |
| +2 | open H1 |
| +4 | open H1-H2 |
| +5 | open H1-H3 |
| +7 | open H1-H4 |
| +9 | open H1-H5 |
| +11 | open H1-H6 |
| +12 | open H1-H7 |
| +14 | open H1-H7 plus T1 |

Chromatic notes are by half-holing, cross-fingering, removable wax, or a rotating tuning ring. Treat the chart as a tuning scaffold, not a final published fingering chart.

## Historical Archetype

Use the `hole-schedule-historical.csv` pilot. Build it with waxable holes and tune by ear/tuner:

| Sounding note above tonic | Fingering idea |
| --- | --- |
| 0 semitones | all holes closed |
| +2 | open F1 |
| +4 | open F1-F2 |
| +5 | open F1-F3, optional |
| +7 | open F1-F4 |
| +12 | open front holes plus T1/back vent |

The strict historical version should be documented as "limited range, four-hole evidence, exact pitch unknown." The practical consort should be documented as "modern reconstruction."

## Tuning Order

1. Tune closed tonic by cavity volume, window area, and any tuning vent.
2. Tune H1, then H2, working upward.
3. Tune the octave hole after the lower scale speaks reliably.
4. Tune T1 last. It doubles as high note, thumb vent, or pitch control.
5. Leave small holes slightly flat before glaze fire, then do final opening after glaze if needed.

## Cents Formula

```text
cents = 1200 * log2(measured_frequency / target_frequency)
```

Keep final production tolerance to +/-15 cents for first playable prototypes and tighten to +/-8 cents after shrinkage and voicing data are stable.
"""
    (PACKET_DIR / "tuning-and-fingering.md").write_text(text, encoding="utf-8")


def write_assembly_manual() -> None:
    text = f"""# Assembly Manual

Generated: {TODAY}

## Safety

- Wear a respirator for clay dust, plaster dust, sanding, and fired ceramic grinding.
- Use wet cleanup for clay and plaster; do not sweep dry dust.
- Keep plaster out of reclaim clay.
- Use eye protection when drilling bisque or fired ceramic.
- Use lead-free, food-safe-compatible glazes if the instrument may contact the mouth.

## Tools

- Casting slip, plaster mold, mold straps, buckets, sieve, scale, timer.
- Calipers, flexible ruler, pin gauges, drill bits, tapered reamers, needle files.
- Chromatic tuner or microphone/spectrum app, thermometer, hygrometer.
- Hardwood for blocks, cork/leather/wax for seals, fine saw, knife, small chisels.

## Phase 1: Master And Mold

1. Pick a size from `family-spec.csv`.
2. Confirm clay shrinkage with test bars.
3. Update `gemshorn-design-table.xlsx` if shrinkage differs from the default.
4. Make and seal the master.
5. Build a two-part plaster mold using `mold-and-slip-casting-plan.md`.

## Phase 2: Cast Body

1. Pour slip and record drain time.
2. Release at leather hard.
3. Clean seams, mark centerline, and confirm wall thickness at the pour opening.
4. Drill undersize holes from `hole-schedule-modern.csv` or `hole-schedule-historical.csv`.
5. Trim the fipple seat and window area conservatively.
6. Slow dry to bone dry.

## Phase 3: Bisque And Measure

1. Bisque fire.
2. Measure length, wide OD, hole diameters, mass, and cavity volume.
3. Record all measurements in `validation.csv`.
4. Fit a temporary block and test whether the instrument speaks.

## Phase 4: Voice And Tune

1. Make the windway even and low.
2. Sharpen and stabilize the labium.
3. Tune closed note first.
4. Open holes gradually from low to high.
5. Use wax to backtrack if a hole goes sharp.
6. Record every tuning pass, temperature, and action.

## Phase 5: Finish

1. Remove block before glaze unless the block is sacrificial.
2. Mask windway, labium, hole interiors, and tuning seats.
3. Glaze or burnish exterior.
4. Glaze fire.
5. Refit block, final tune, and seal mouth-contact surfaces.

## Maintenance

- Keep removable blocks dry and replaceable.
- Avoid soaking fired ceramic bodies unless the clay/glaze combination is proven.
- Store with a cork or cloth spacer so the labium is protected.
- Keep a small wax kit for tuning during outdoor or temperature-variable use.
"""
    (PACKET_DIR / "assembly-manual.md").write_text(text, encoding="utf-8")


def write_drawing_brief(family: list[dict[str, Any]]) -> None:
    text = f"""# Drawing Brief

Generated: {TODAY}

## Required Drawing Set

1. `drawings/gemshorn-family-scale.svg` - side-by-side family scale and title block.
2. `drawings/gemshorn-body-section.svg` - longitudinal body section with closed tip, wall, cavity, and fipple seat.
3. `drawings/gemshorn-voicing-detail.svg` - windway, block, labium, window, and tuning ring/vent.
4. `drawings/gemshorn-mold-schematic.svg` - two-part plaster mold, split line, keys, pour mouth, and release direction.
5. `drawings/hole-layout-template.svg` - soprano C hole positions and diameters for a drilling template.
6. `drawings/visual-bom-plate.svg` - visual BOM plate layout.

## Datums

- Datum A: labium edge / window lower edge.
- Datum B: centerline curve from labium to sealed tip.
- Datum C: dorsal plane through thumb hole and mold split witness marks.
- Datum D: wide-end block seating plane.

## Critical Dimensions

- Fired and master centerline length.
- Wide-end OD/ID and block seat diameter.
- Tip OD and closed-tip minimum wall.
- Wall thickness target and acceptable range.
- Window width, window height, labium setback, windway height.
- Tone-hole center positions measured from Datum A along the centerline.
- Tone-hole final fired diameters and greenware drill-start diameters.
- Tuning ring or vent position and diameter.

## Tolerances

- Tone-hole final diameter: +/-0.005 in before tuning, final by pitch.
- Window width/height: +/-0.005 in on soprano and smaller, +/-0.010 in on alto and larger.
- Windway height: +/-0.003 in for soprano/sopranino, +/-0.005 in for larger sizes.
- Wall thickness: +/-15% unless structural cracks appear.
- Noncritical exterior profile: +/-0.060 in.

## Current Family Reference

{render_table(["ID", "Key", "Fired length in", "Wide OD in", "Wall in"], [[item["id"], item["key"], item["fired_centerline_length_in"], item["fired_wide_od_in"], item["fired_wall_in"]] for item in family])}

## Notes

The SVGs are shop-reference drawings and review plates. Before making production molds, convert the dimensions into SolidWorks, OpenSCAD/STL, or another CAD system and verify mold release.
"""
    (PACKET_DIR / "drawing-brief.md").write_text(text, encoding="utf-8")


def write_visual_bom_brief() -> None:
    text = """# Visual BOM Brief

## Goal

Create an image-forward resource plate for the slip-cast gemshorn family: finished instrument, mold, master, clay body, fipple block, tuning ring, tools, and measurement/tuning kit.

## Layout

- Header: "Slip-Cast Gemshorn Family", quote/build date, revision, estimated cost status.
- Hero: family scale view with bass F through sopranino F.
- Exploded center: ceramic body, removable block, leather/cork seal, tuning ring/collar, hole/tuning kit.
- Table: item, qty, make/buy, material/spec, source/search term, drawing ref, cost status.
- Footer: shrinkage assumption, clay body TBD, source/history note.

## Image Status

- `drawings/visual-bom-plate.svg` is a generated vector placeholder.
- Replace placeholders with real photos after the first cast, master, mold, and fipple block exist.
- Do not use generated images for critical dimensions.
"""
    (PACKET_DIR / "visual-bom-brief.md").write_text(text, encoding="utf-8")


def write_supplier_rfq(family: list[dict[str, Any]]) -> None:
    max_len = max(item["master_centerline_length_in"] for item in family)
    max_od = max(item["master_wide_od_in"] for item in family)
    text = f"""# Supplier RFQ Draft

Subject: RFQ - slip-cast ceramic gemshorn prototypes and plaster mold materials

Hello,

I am prototyping a family of slip-cast ceramic gemshorns, a small fipple/vessel-flute instrument. I am looking for pricing, lead time, and technical guidance for the following:

1. White stoneware or porcelain casting slip suitable for thin musical-instrument bodies.
2. Pottery plaster or equivalent mold plaster for two-part molds.
3. Optional 3D print or CNC master service for sealed masters up to about {max_len:.1f} in long and {max_od:.1f} in wide.
4. Small hardwood, cork, leather, or silicone sheet suitable for removable fipple blocks and seals.
5. Brass or stainless thin-wall tubing/strip for optional rotating tuning collars.

Please quote unit price, volume price, minimum order, lead time, shipping estimate, data sheets, shrinkage range, recommended firing cone, and any substitutions you recommend.

The current prototype set includes: {", ".join(item["key"] for item in family)}. Critical requirements are stable shrinkage, clean release from plaster molds, and a fired body that can hold crisp tone-hole and voicing edges.

Thank you,
Tony
"""
    (PACKET_DIR / "supplier-rfq.md").write_text(text, encoding="utf-8")


def write_cnc_plan() -> None:
    path = PACKET_DIR / "cnc" / "mold-master-cam-plan.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    text = """# Mold Master CAM And Setup Plan

## Process Options

- 3D print master, seal, sand, and polish.
- CNC positive master in tooling board, then seal.
- CNC negative mold only after the cast geometry has been proven with a plaster hand mold.

## Coordinate System

- X follows the horn centerline projection.
- Y crosses the body width.
- Z is normal to the split plane.
- Datum zero: labium edge / wide-end seating plane intersection on centerline.

## Operations

1. Rough exterior body/master.
2. Finish exterior with small stepover.
3. Mark hole dimples and split line.
4. Add registration witness marks.
5. Seal and polish.
6. Make plaster mold by hand around the master.

## Tooling Placeholders

- 1/4 in ball end for rough surfacing.
- 1/8 in ball end for detail surfacing and hole dimples.
- Engraving bit or laser marker for witness lines if material allows.

## Dry Run Checks

- Master fits mold box with at least 1.5 in plaster around the widest point.
- No undercuts trap the cast in a two-part mold.
- Pour mouth is large enough for slip flow and cleanup.
- Hole dimples are visible after mold release but not final-size holes.
"""
    path.write_text(text, encoding="utf-8")


def write_wolfram(family: list[dict[str, Any]]) -> None:
    rows = ",\n".join(
        '  <|"ID" -> "{id}", "Key" -> "{key}", "MIDI" -> {midi}, "LengthIn" -> {length:.4f}, "VolumeIn3" -> {volume:.4f}, "WindowAreaIn2" -> {area:.5f}, "WallIn" -> {wall:.4f}|>'.format(
            id=item["id"],
            key=item["key"],
            midi=item["midi"],
            length=item["fired_centerline_length_in"],
            volume=item["fired_internal_volume_in3"],
            area=item["window_area_in2"],
            wall=item["fired_wall_in"],
        )
        for item in family
    )
    text = f"""(* Slip-Cast Gemshorn Family Wolfram Starter *)
(* Generated {TODAY}. Paste into Wolfram Desktop or Cloud. *)

ClearAll["Global`*"];

speedOfSoundInPerS = {SPEED_OF_SOUND_IN_S};
shrinkage = {SHRINKAGE};

family = {{
{rows}
}};

midiToFreq[m_] := 440*2^((m - 69)/12);
centsError[measured_, target_] := 1200*Log[2, measured/target];
holeLeff[diameter_, wall_] := wall + 0.85*(diameter/2);
conductance[diameter_, wall_] := Pi*(diameter/2)^2/holeLeff[diameter, wall];
helmholtzHz[conductanceTotal_, volumeIn3_] :=
  speedOfSoundInPerS/(2*Pi)*Sqrt[conductanceTotal/volumeIn3];

Dataset[family]

Manipulate[
 Module[{{freq = midiToFreq[midi], scale, volume, windowArea, wall, windowLeff, gBase, predicted}},
  scale = midiToFreq[{BASE_MIDI}]/freq;
  wall = Min[0.24, Max[0.11, {BASE["wall_in"]}*scale^0.65]];
  windowArea = ({BASE["window_width_in"]}*scale)*({BASE["window_height_in"]}*scale);
  windowLeff = wall + 0.85*Sqrt[windowArea/Pi];
  gBase = windowArea/windowLeff;
  volume = {family[3]["fired_internal_volume_in3"]:.6f}*scale^3;
  predicted = helmholtzHz[gBase, volume];
  Column[{{
    Row[{{"Target Hz: ", NumberForm[freq, {{6, 2}}]}}],
    Row[{{"Predicted closed Hz: ", NumberForm[predicted, {{6, 2}}]}}],
    Row[{{"Cents error: ", NumberForm[centsError[predicted, freq], {{6, 1}}]}}],
    Row[{{"Scale factor: ", NumberForm[scale, {{5, 3}}]}}],
    Row[{{"Volume in3: ", NumberForm[volume, {{7, 3}}]}}],
    Row[{{"Window area in2: ", NumberForm[windowArea, {{6, 4}}]}}]
  }}]
 ],
 {{{{midi, 72, "Closed-note MIDI"}}, 53, 77, 1}}
]

(* Import validation.csv after prototypes exist:
validation = Import["validation.csv", "Dataset"];
*)
"""
    (PACKET_DIR / "wolfram-starter.wl").write_text(text, encoding="utf-8")


def write_scad(family: list[dict[str, Any]]) -> None:
    path = PACKET_DIR / "cad" / "gemshorn_family.scad"
    path.parent.mkdir(parents=True, exist_ok=True)
    entries = ",\n".join(
        '  ["{id}", {length:.4f}, {wide:.4f}, {tip:.4f}, {wall:.4f}]'.format(
            id=item["id"],
            length=item["master_centerline_length_in"],
            wide=item["master_wide_od_in"],
            tip=item["fired_tip_od_in"] / (1 - SHRINKAGE),
            wall=item["fired_wall_in"] / (1 - SHRINKAGE),
        )
        for item in family
    )
    text = f"""// Slip-Cast Gemshorn Family OpenSCAD Starter
// Generated {TODAY}
// Units: inches. This is a master-shape starter, not final production CAD.

$fn = 64;

family = [
{entries}
];

module horn_outer(len, wide_od, tip_od) {{
  hull() {{
    translate([0, 0, 0]) sphere(d=wide_od);
    translate([len*0.38, 0, len*0.12]) sphere(d=wide_od*0.70);
    translate([len*0.72, 0, len*0.17]) sphere(d=wide_od*0.43);
    translate([len, 0, len*0.18]) sphere(d=tip_od);
  }}
}}

module gemshorn_master(len, wide_od, tip_od, wall) {{
  difference() {{
    horn_outer(len, wide_od, tip_od);
    // Wide-end block seat and pour mouth.
    translate([-0.05, 0, 0]) rotate([0, 90, 0]) cylinder(h=wide_od*0.7, d=max(0.20, wide_od - 2*wall));
    // Voicing/window starter. Cut final labium and windway by hand or in detailed CAD.
    translate([wide_od*0.15, -wide_od*0.55, wide_od*0.18]) cube([wide_od*0.22, wide_od*1.1, wide_od*0.10], center=true);
  }}
}}

// Preview all masters side by side.
for (i = [0:len(family)-1]) {{
  translate([0, i*7, 0])
    gemshorn_master(family[i][1], family[i][2], family[i][3], family[i][4]);
}}
"""
    path.write_text(text, encoding="utf-8")


def write_bom_and_sourcing(family: list[dict[str, Any]]) -> None:
    bom_rows = [
        {
            "item": "BOM-000",
            "part": "Natural horn blank",
            "qty": "3 blanks for first authentic prototype",
            "material_spec": "Domesticated cow/ox/goat/sheep horn, closed tip, no cracks",
            "make_buy": "buy",
            "drawing_ref": "horn-blank-spec.csv",
            "notes": "Authentic build path; avoid endangered/wild chamois sourcing",
        },
        {
            "item": "BOM-001",
            "part": "Slip-cast ceramic body",
            "qty": "1 per instrument",
            "material_spec": "White stoneware or porcelain casting slip, measured shrinkage",
            "make_buy": "make",
            "drawing_ref": "drawings/gemshorn-body-section.svg",
            "notes": "Use family-spec.csv for size-specific fired and master dimensions",
        },
        {
            "item": "BOM-002",
            "part": "Two-part plaster mold",
            "qty": "1 per size",
            "material_spec": "Pottery plaster or equivalent",
            "make_buy": "make",
            "drawing_ref": "drawings/gemshorn-mold-schematic.svg",
            "notes": "Add registration keys and pour mouth",
        },
        {
            "item": "BOM-003",
            "part": "Master pattern",
            "qty": "1 per size",
            "material_spec": "3D printed resin/PLA, tooling board, or sealed wood",
            "make_buy": "make or outsource",
            "drawing_ref": "cad/gemshorn_family.scad",
            "notes": "Scale for shrinkage and seal before plaster",
        },
        {
            "item": "BOM-004",
            "part": "Fipple/block",
            "qty": "1 per instrument",
            "material_spec": "Cedar, maple, pear, plaster, or stable hardwood",
            "make_buy": "make",
            "drawing_ref": "drawings/gemshorn-voicing-detail.svg",
            "notes": "Removable block recommended for tuning and service",
        },
        {
            "item": "BOM-005",
            "part": "Seal wrap/gasket",
            "qty": "1 set per instrument",
            "material_spec": "Leather, cork, beeswax, or thin silicone gasket",
            "make_buy": "buy",
            "drawing_ref": "drawings/gemshorn-voicing-detail.svg",
            "notes": "Keep mouth-contact material safe and replaceable",
        },
        {
            "item": "BOM-006",
            "part": "Optional tuning ring/collar",
            "qty": "1 per instrument",
            "material_spec": "Thin brass/stainless ring, leather band, or ceramic collar",
            "make_buy": "buy or make",
            "drawing_ref": "drawings/gemshorn-voicing-detail.svg",
            "notes": "Rotates over vent to lower closed keynote",
        },
        {
            "item": "BOM-007",
            "part": "Tuning and measurement kit",
            "qty": "1 shop set",
            "material_spec": "Pin gauges, drill bits, reamers, tuner, thermometer, wax",
            "make_buy": "buy",
            "drawing_ref": "validation.csv",
            "notes": "Required before final pitch claims",
        },
    ]
    write_csv(
        PACKET_DIR / "bom.csv",
        bom_rows,
        ["item", "part", "qty", "material_spec", "make_buy", "drawing_ref", "notes"],
    )

    sourcing_rows = [
        {
            "item": "Natural horn blank",
            "spec": "Domesticated cow/ox/goat/sheep horn, closed tip, cleanable interior",
            "supplier_or_search_terms": "cow horn blank ox horn craft horn goat horn instrument blank",
            "price_each": "TBD live check",
            "date_checked": "",
            "lead_time": "TBD",
            "substitution_rule": "Do not use endangered species; reject cracked or delaminated blanks",
            "risk": "Each horn has different volume and curvature, so every blank is tuned empirically",
        },
        {
            "item": "Casting slip",
            "spec": "White stoneware or porcelain casting slip; shrinkage data required",
            "supplier_or_search_terms": "ceramic casting slip cone 6 porcelain stoneware gallon",
            "price_each": "TBD live check",
            "date_checked": "",
            "lead_time": "TBD",
            "substitution_rule": "Must provide shrinkage and firing cone",
            "risk": "Shrinkage variation changes all dimensions and pitch",
        },
        {
            "item": "Pottery plaster",
            "spec": "No. 1 pottery plaster or equivalent mold plaster",
            "supplier_or_search_terms": "pottery plaster mold plaster 50 lb",
            "price_each": "TBD live check",
            "date_checked": "",
            "lead_time": "TBD",
            "substitution_rule": "Use ceramic mold plaster, not construction plaster",
            "risk": "Poor absorption causes slow wall growth and release trouble",
        },
        {
            "item": "Hardwood block stock",
            "spec": "Fine-grain stable hardwood blanks, 1/2 to 2 in depending size",
            "supplier_or_search_terms": "cedar pear maple turning blank instrument block",
            "price_each": "TBD live check",
            "date_checked": "",
            "lead_time": "TBD",
            "substitution_rule": "Avoid resinous or mouth-unsafe finishes",
            "risk": "Block swelling or warping changes windway",
        },
        {
            "item": "Leather/cork gasket",
            "spec": "Thin natural leather, cork sheet, or mouth-safe gasket material",
            "supplier_or_search_terms": "thin cork gasket sheet leather scrap beeswax",
            "price_each": "TBD live check",
            "date_checked": "",
            "lead_time": "TBD",
            "substitution_rule": "Must seal without shedding dust",
            "risk": "Leaks make voicing unstable",
        },
        {
            "item": "Tuning ring material",
            "spec": "Thin brass strip/tube or leather collar",
            "supplier_or_search_terms": "thin brass strip tube hobby K&S brass",
            "price_each": "TBD live check",
            "date_checked": "",
            "lead_time": "TBD",
            "substitution_rule": "Collar must rotate smoothly and not chip clay",
            "risk": "Rough collar damages vent edge",
        },
    ]
    write_csv(
        PACKET_DIR / "sourcing.csv",
        sourcing_rows,
        [
            "item",
            "spec",
            "supplier_or_search_terms",
            "price_each",
            "date_checked",
            "lead_time",
            "substitution_rule",
            "risk",
        ],
    )


def write_cut_and_validation(family: list[dict[str, Any]], modern_holes: list[dict[str, Any]], historical_holes: list[dict[str, Any]]) -> None:
    cut_rows: list[dict[str, Any]] = []
    for item in family:
        cut_rows.append(
            {
                "part_id": item["id"] + "-MASTER",
                "part": item["name"] + " scaled master",
                "qty": 1,
                "rough_size": f"{item['master_centerline_length_in'] + 2:.2f} x {item['master_wide_od_in'] + 2:.2f} x {item['master_wide_od_in'] + 2:.2f} in envelope",
                "finished_size": f"{item['master_centerline_length_in']:.2f} in centerline, {item['master_wide_od_in']:.2f} in wide OD",
                "material": "sealed print/tooling board",
                "operation": "print/CNC, seal, sand, polish, mark dimples",
                "yield_or_offcut": "one master per size",
                "notes": "Check mold release before committing plaster",
            }
        )
        cut_rows.append(
            {
                "part_id": item["id"] + "-MOLD",
                "part": item["name"] + " plaster mold",
                "qty": 1,
                "rough_size": f"mold box about {item['master_centerline_length_in'] + 4:.2f} x {item['master_wide_od_in'] + 4:.2f} x {item['master_wide_od_in'] + 4:.2f} in",
                "finished_size": "two plaster halves plus pour opening",
                "material": "pottery plaster",
                "operation": "cast mold halves around sealed master",
                "yield_or_offcut": "reuse for production run after seasoning",
                "notes": "Add registration keys and split-line witness marks",
            }
        )
    write_csv(
        PACKET_DIR / "cut-list.csv",
        cut_rows,
        [
            "part_id",
            "part",
            "qty",
            "rough_size",
            "finished_size",
            "material",
            "operation",
            "yield_or_offcut",
            "notes",
        ],
    )

    validation_rows: list[dict[str, Any]] = []
    for item in family:
        validation_rows.extend(
            [
                {
                    "instrument_id": item["id"],
                    "check": "closed tonic frequency",
                    "target": f"{item['freq_hz']:.2f} Hz",
                    "measured": "",
                    "tolerance": "+/-15 cents prototype",
                    "environment": "record temp F, humidity",
                    "result": "",
                    "action": "adjust cavity/window/vent before hole tuning",
                },
                {
                    "instrument_id": item["id"],
                    "check": "fired centerline length",
                    "target": f"{item['fired_centerline_length_in']:.3f} in",
                    "measured": "",
                    "tolerance": "+/-0.060 in",
                    "environment": "after glaze if glazed",
                    "result": "",
                    "action": "update shrinkage factor if systematic",
                },
                {
                    "instrument_id": item["id"],
                    "check": "fired internal volume",
                    "target": f"{item['fired_internal_volume_ml']:.0f} ml",
                    "measured": "",
                    "tolerance": "+/-5%",
                    "environment": "water-fill, dry after",
                    "result": "",
                    "action": "retune window/vent model",
                },
            ]
        )
    for row in modern_holes + historical_holes:
        validation_rows.append(
            {
                "instrument_id": row["instrument_id"],
                "check": row["hole"] + " final diameter",
                "target": f"{row['fired_diameter_in']:.4f} in",
                "measured": "",
                "tolerance": "by pitch, do not oversize",
                "environment": "after bisque and final tune",
                "result": "",
                "action": "open gradually or wax if sharp",
            }
        )
    write_csv(
        PACKET_DIR / "validation.csv",
        validation_rows,
        ["instrument_id", "check", "target", "measured", "tolerance", "environment", "result", "action"],
    )


def svg_header(width: int, height: int, title: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <rect width="100%" height="100%" fill="#ffffff"/>
  <text x="24" y="34" font-family="Arial, sans-serif" font-size="22" font-weight="700">{html.escape(title)}</text>
  <text x="{width - 260}" y="{height - 24}" font-family="Arial, sans-serif" font-size="12">Generated {TODAY} | Units: inches</text>
'''


def write_svg_drawings(family: list[dict[str, Any]], modern_holes: list[dict[str, Any]]) -> None:
    drawings = PACKET_DIR / "drawings"
    drawings.mkdir(parents=True, exist_ok=True)
    write_family_scale_svg(drawings / "gemshorn-family-scale.svg", family)
    write_body_section_svg(drawings / "gemshorn-body-section.svg", family[3])
    write_voicing_svg(drawings / "gemshorn-voicing-detail.svg", family[3])
    write_mold_svg(drawings / "gemshorn-mold-schematic.svg")
    write_hole_template_svg(drawings / "hole-layout-template.svg", family[3], [r for r in modern_holes if r["instrument_id"] == "GEM-SC-C5"])
    write_visual_bom_svg(drawings / "visual-bom-plate.svg")


def write_family_scale_svg(path: Path, family: list[dict[str, Any]]) -> None:
    width, height = 980, 620
    px_per_in = 15
    y0 = 95
    gap = 92
    parts = [svg_header(width, height, "Gemshorn Slip-Cast Family Scale")]
    parts.append('  <line x1="80" y1="555" x2="900" y2="555" stroke="#111" stroke-width="1"/>')
    parts.append('  <text x="80" y="575" font-family="Arial" font-size="12">Scale bar: 0 to 30 in fired centerline length</text>')
    parts.append('  <line x1="80" y1="545" x2="530" y2="545" stroke="#111" stroke-width="3"/>')
    parts.append('  <text x="80" y="540" font-family="Arial" font-size="12">0</text><text x="520" y="540" font-family="Arial" font-size="12">30 in</text>')
    for idx, item in enumerate(family):
        y = y0 + idx * gap
        x = 120
        length_px = item["fired_centerline_length_in"] * px_per_in
        wide = item["fired_wide_od_in"] * px_per_in
        tip = item["fired_tip_od_in"] * px_per_in
        path_d = f"M {x} {y} C {x + length_px*0.35} {y - wide*0.30}, {x + length_px*0.72} {y - wide*0.20}, {x + length_px} {y - tip*0.10}"
        parts.append(f'  <path d="{path_d}" fill="none" stroke="#995c2d" stroke-width="{max(tip, 4):.1f}" stroke-linecap="round"/>')
        parts.append(f'  <path d="{path_d}" fill="none" stroke="#111111" stroke-width="1.2" stroke-dasharray="4 5"/>')
        parts.append(f'  <circle cx="{x}" cy="{y}" r="{max(wide/2, 4):.1f}" fill="none" stroke="#111" stroke-width="1.2"/>')
        parts.append(f'  <text x="24" y="{y+5}" font-family="Arial" font-size="14" font-weight="700">{item["id"]}</text>')
        parts.append(f'  <text x="{x + length_px + 18:.1f}" y="{y+4:.1f}" font-family="Arial" font-size="13">{item["key"]}, fired L {item["fired_centerline_length_in"]:.2f} in, master L {item["master_centerline_length_in"]:.2f} in</text>')
    parts.append("</svg>\n")
    path.write_text("\n".join(parts), encoding="utf-8")


def write_body_section_svg(path: Path, item: dict[str, Any]) -> None:
    width, height = 980, 430
    parts = [svg_header(width, height, "Gemshorn Body Section - Soprano C Baseline")]
    x0, y0 = 120, 220
    length = 620
    wide = 100
    tip = 24
    parts.append(f'  <path d="M {x0} {y0-wide/2} C {x0+220} {y0-70}, {x0+450} {y0-38}, {x0+length} {y0-tip/2} L {x0+length} {y0+tip/2} C {x0+450} {y0+38}, {x0+220} {y0+70}, {x0} {y0+wide/2} Z" fill="#f5efe4" stroke="#111" stroke-width="2"/>')
    parts.append(f'  <path d="M {x0+30} {y0-34} C {x0+230} {y0-48}, {x0+445} {y0-25}, {x0+length-20} {y0-7} L {x0+length-20} {y0+7} C {x0+445} {y0+25}, {x0+230} {y0+48}, {x0+30} {y0+34} Z" fill="#ffffff" stroke="#333" stroke-dasharray="5 4"/>')
    parts.append(f'  <rect x="{x0-38}" y="{y0-48}" width="46" height="96" fill="#d8b98c" stroke="#111"/>')
    parts.append(f'  <text x="{x0-56}" y="{y0-60}" font-family="Arial" font-size="12">Removable block</text>')
    parts.append(f'  <rect x="{x0+52}" y="{y0-61}" width="58" height="22" fill="#ffffff" stroke="#111"/>')
    parts.append(f'  <text x="{x0+120}" y="{y0-44}" font-family="Arial" font-size="12">Voicing window</text>')
    parts.append(f'  <line x1="{x0}" y1="{y0+84}" x2="{x0+length}" y2="{y0+84}" stroke="#111"/>')
    parts.append(f'  <text x="{x0+215}" y="{y0+105}" font-family="Arial" font-size="12">Datum B centerline to closed tip, fired L {item["fired_centerline_length_in"]:.2f} in</text>')
    parts.append(f'  <text x="{x0}" y="370" font-family="Arial" font-size="13">Wide OD {item["fired_wide_od_in"]:.2f} in | Wall {item["fired_wall_in"]:.3f} in | Volume {item["fired_internal_volume_ml"]:.0f} ml | Window {item["window_width_in"]:.3f} x {item["window_height_in"]:.3f} in</text>')
    parts.append("</svg>\n")
    path.write_text("\n".join(parts), encoding="utf-8")


def write_voicing_svg(path: Path, item: dict[str, Any]) -> None:
    width, height = 760, 420
    parts = [svg_header(width, height, "Gemshorn Voicing Detail - Fipple, Window, Tuning Vent")]
    parts.append('  <rect x="120" y="145" width="420" height="120" rx="6" fill="#f6efe3" stroke="#111" stroke-width="2"/>')
    parts.append('  <path d="M 140 205 L 300 178 L 300 198 L 140 225 Z" fill="#ffffff" stroke="#111"/>')
    parts.append('  <rect x="305" y="166" width="75" height="58" fill="#ffffff" stroke="#111" stroke-width="2"/>')
    parts.append('  <path d="M 380 224 L 430 190" stroke="#111" stroke-width="3"/>')
    parts.append('  <rect x="455" y="150" width="34" height="112" fill="none" stroke="#8f6b2f" stroke-width="7"/>')
    parts.append('  <circle cx="472" cy="205" r="9" fill="#ffffff" stroke="#111"/>')
    parts.append('  <text x="132" y="132" font-family="Arial" font-size="13">Windway height target: {:.3f} in</text>'.format(item["windway_height_in"]))
    parts.append('  <text x="306" y="152" font-family="Arial" font-size="13">Window {:.3f} x {:.3f} in</text>'.format(item["window_width_in"], item["window_height_in"]))
    parts.append('  <text x="388" y="245" font-family="Arial" font-size="13">Labium edge: crisp, unglazed</text>')
    parts.append('  <text x="505" y="204" font-family="Arial" font-size="13">Rotating tuning ring/vent</text>')
    parts.append('  <text x="120" y="310" font-family="Arial" font-size="12">Use this as a geometry brief. Final windway/block fit is tuned by test blows and recorded in validation.csv.</text>')
    parts.append("</svg>\n")
    path.write_text("\n".join(parts), encoding="utf-8")


def write_mold_svg(path: Path) -> None:
    width, height = 820, 520
    parts = [svg_header(width, height, "Two-Part Plaster Mold Schematic")]
    parts.append('  <rect x="140" y="105" width="540" height="300" rx="8" fill="#f1f1f1" stroke="#111" stroke-width="2"/>')
    parts.append('  <line x1="140" y1="255" x2="680" y2="255" stroke="#111" stroke-width="3" stroke-dasharray="8 6"/>')
    parts.append('  <text x="690" y="260" font-family="Arial" font-size="13">Split line</text>')
    parts.append('  <path d="M 235 255 C 330 210, 500 215, 610 255 C 500 295, 330 300, 235 255 Z" fill="#f5efe4" stroke="#111" stroke-width="2"/>')
    parts.append('  <circle cx="190" cy="165" r="18" fill="#ffffff" stroke="#111"/><circle cx="630" cy="165" r="18" fill="#ffffff" stroke="#111"/>')
    parts.append('  <circle cx="190" cy="345" r="18" fill="#ffffff" stroke="#111"/><circle cx="630" cy="345" r="18" fill="#ffffff" stroke="#111"/>')
    parts.append('  <text x="170" y="95" font-family="Arial" font-size="13">Registration keys</text>')
    parts.append('  <path d="M 220 255 L 120 230 L 120 280 Z" fill="#ffffff" stroke="#111" stroke-width="2"/>')
    parts.append('  <text x="46" y="225" font-family="Arial" font-size="13">Pour mouth / wide end</text>')
    parts.append('  <text x="300" y="440" font-family="Arial" font-size="13">Release direction: separate mold halves before pulling cast from wide end.</text>')
    parts.append("</svg>\n")
    path.write_text("\n".join(parts), encoding="utf-8")


def write_hole_template_svg(path: Path, item: dict[str, Any], holes: list[dict[str, Any]]) -> None:
    width, height = 980, 360
    scale = 62
    x0, y0 = 130, 170
    parts = [svg_header(width, height, "Hole Layout Template - Soprano C Fired Dimensions")]
    parts.append(f'  <line x1="{x0}" y1="{y0}" x2="{x0 + item["fired_centerline_length_in"]*scale:.1f}" y2="{y0}" stroke="#111" stroke-width="2"/>')
    parts.append(f'  <rect x="{x0-20}" y="{y0-45}" width="40" height="90" fill="#f5efe4" stroke="#111"/>')
    parts.append(f'  <text x="{x0-34}" y="{y0-58}" font-family="Arial" font-size="12">Datum A labium</text>')
    for hole in holes:
        x = x0 + hole["fired_position_from_labium_in"] * scale
        d = max(hole["fired_diameter_in"] * scale, 7)
        y = y0 - 38 if "back" in hole["face"] else y0
        fill = "#ffffff" if "back" in hole["face"] else "#d9ecff"
        parts.append(f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="{d/2:.1f}" fill="{fill}" stroke="#111" stroke-width="1.5"/>')
        parts.append(f'  <text x="{x-18:.1f}" y="{y+34:.1f}" font-family="Arial" font-size="11">{hole["hole"]}</text>')
        parts.append(f'  <text x="{x-28:.1f}" y="{y+48:.1f}" font-family="Arial" font-size="10">{hole["fired_diameter_in"]:.3f} in</text>')
    parts.append('  <text x="120" y="305" font-family="Arial" font-size="12">Positions are measured from Datum A along the centerline. Use greenware drill-start diameters from CSV before firing.</text>')
    parts.append("</svg>\n")
    path.write_text("\n".join(parts), encoding="utf-8")


def write_visual_bom_svg(path: Path) -> None:
    width, height = 1100, 720
    parts = [svg_header(width, height, "Visual BOM Plate - Slip-Cast Gemshorn Family")]
    parts.append('  <rect x="35" y="60" width="1030" height="620" fill="#fbfbfb" stroke="#111"/>')
    parts.append('  <text x="60" y="92" font-family="Arial" font-size="15" font-weight="700">Hero: ceramic gemshorn family scale</text>')
    parts.append('  <path d="M 80 180 C 210 130, 390 145, 520 190" fill="none" stroke="#995c2d" stroke-width="38" stroke-linecap="round"/>')
    parts.append('  <path d="M 70 255 C 180 220, 330 228, 430 260" fill="none" stroke="#b7773b" stroke-width="25" stroke-linecap="round"/>')
    parts.append('  <rect x="610" y="95" width="390" height="120" fill="#f1f1f1" stroke="#111"/>')
    parts.append('  <text x="635" y="130" font-family="Arial" font-size="14">1. Plaster mold halves</text>')
    parts.append('  <text x="635" y="158" font-family="Arial" font-size="14">2. Sealed master pattern</text>')
    parts.append('  <text x="635" y="186" font-family="Arial" font-size="14">3. Casting slip and shrinkage bars</text>')
    headers = ["Item", "Part", "Qty", "Make/Buy", "Drawing"]
    x_cols = [60, 160, 520, 630, 780]
    y = 340
    for idx, header in enumerate(headers):
        parts.append(f'  <text x="{x_cols[idx]}" y="{y}" font-family="Arial" font-size="13" font-weight="700">{header}</text>')
    items = [
        ("1", "Ceramic body", "1/inst", "make", "body-section"),
        ("2", "Fipple/block", "1/inst", "make", "voicing-detail"),
        ("3", "Seal wrap", "1/inst", "buy", "voicing-detail"),
        ("4", "Tuning collar", "optional", "buy/make", "voicing-detail"),
        ("5", "Tuning kit", "1 shop", "buy", "validation"),
    ]
    for row, values in enumerate(items, start=1):
        yy = y + row * 42
        parts.append(f'  <rect x="48" y="{yy-23}" width="970" height="34" fill="{"#ffffff" if row % 2 else "#f4f4f4"}" stroke="#ddd"/>')
        for idx, val in enumerate(values):
            parts.append(f'  <text x="{x_cols[idx]}" y="{yy}" font-family="Arial" font-size="12">{html.escape(val)}</text>')
    parts.append('  <text x="60" y="640" font-family="Arial" font-size="12">Image placeholders: replace with real master, mold, cast body, block, and tuning photos after first prototype.</text>')
    parts.append("</svg>\n")
    path.write_text("\n".join(parts), encoding="utf-8")


def cell_ref(col: int, row: int) -> str:
    result = ""
    while col:
        col, rem = divmod(col - 1, 26)
        result = chr(65 + rem) + result
    return f"{result}{row}"


def sheet_xml(rows: list[list[Any]]) -> str:
    out = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>']
    out.append('<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">')
    out.append("<sheetData>")
    for r_idx, row in enumerate(rows, start=1):
        out.append(f'<row r="{r_idx}">')
        for c_idx, value in enumerate(row, start=1):
            ref = cell_ref(c_idx, r_idx)
            if isinstance(value, Formula):
                out.append(f'<c r="{ref}"><f>{html.escape(value.value)}</f></c>')
            elif isinstance(value, (int, float)) and not isinstance(value, bool):
                out.append(f'<c r="{ref}"><v>{value}</v></c>')
            elif value is None:
                out.append(f'<c r="{ref}"/>')
            else:
                text = html.escape(str(value))
                out.append(f'<c r="{ref}" t="inlineStr"><is><t>{text}</t></is></c>')
        out.append("</row>")
    out.append("</sheetData>")
    out.append("</worksheet>")
    return "\n".join(out)


def write_xlsx(family: list[dict[str, Any]], modern_holes: list[dict[str, Any]], historical_holes: list[dict[str, Any]]) -> None:
    path = PACKET_DIR / "gemshorn-design-table.xlsx"
    inputs = [
        ["Slip-Cast Gemshorn Parametric Design Table"],
        ["Generated", TODAY],
        ["Parameter", "Value", "Units", "Notes"],
        ["A4 frequency", 440, "Hz", "Equal temperament reference"],
        ["Base MIDI", BASE_MIDI, "MIDI", "C5 soprano baseline"],
        ["Base frequency", Formula("B4*POWER(2,(B5-69)/12)"), "Hz", "Should equal 523.251 Hz"],
        ["Speed of sound", SPEED_OF_SOUND_IN_S, "in/s", "Approx 68 F"],
        ["Shrinkage", SHRINKAGE, "linear fraction", "Replace with fired test-bar value"],
        ["Base centerline length", BASE["centerline_length_in"], "in", "Fired soprano C"],
        ["Base wide OD", BASE["wide_od_in"], "in", "Fired soprano C"],
        ["Base tip OD", BASE["tip_od_in"], "in", "Fired soprano C"],
        ["Base wall", BASE["wall_in"], "in", "Fired soprano C"],
        ["Base window width", BASE["window_width_in"], "in", "Fired soprano C"],
        ["Base window height", BASE["window_height_in"], "in", "Fired soprano C"],
    ]
    family_rows: list[list[Any]] = [
        [
            "ID",
            "Name",
            "Key",
            "MIDI",
            "Frequency Hz",
            "Scale",
            "Fired length in",
            "Master length in",
            "Fired wide OD in",
            "Fired wall in",
            "Fired wide ID in",
            "Volume in3",
            "Volume ml",
            "Window W in",
            "Window H in",
        ]
    ]
    for idx, item in enumerate(family, start=2):
        family_rows.append(
            [
                item["id"],
                item["name"],
                item["key"],
                item["midi"],
                Formula(f"Inputs!$B$4*POWER(2,(D{idx}-69)/12)"),
                Formula(f"Inputs!$B$6/E{idx}"),
                Formula(f"Inputs!$B$9*F{idx}"),
                Formula(f"G{idx}/(1-Inputs!$B$8)"),
                Formula(f"Inputs!$B$10*F{idx}"),
                Formula(f"MAX(0.11,MIN(0.24,Inputs!$B$12*POWER(F{idx},0.65)))"),
                Formula(f"I{idx}-2*J{idx}"),
                Formula(f"PI()*G{idx}/3*((K{idx}/2)^2+(K{idx}/2)*(MAX(0.03,Inputs!$B$11*F{idx}-2*J{idx})/2)+(MAX(0.03,Inputs!$B$11*F{idx}-2*J{idx})/2)^2)"),
                Formula(f"L{idx}*16.387064"),
                Formula(f"Inputs!$B$13*F{idx}"),
                Formula(f"Inputs!$B$14*F{idx}"),
            ]
        )
    hole_rows: list[list[Any]] = [
        [
            "Instrument ID",
            "Hole",
            "Face",
            "Target interval semitones",
            "Prev interval",
            "Position pct",
            "Fired position in",
            "Master position in",
            "Fired diameter in",
            "Greenware drill start in",
            "Incremental conductance",
            "Notes",
        ]
    ]
    for row in modern_holes:
        hole_rows.append(
            [
                row["instrument_id"],
                row["hole"],
                row["face"],
                row["target_interval_semitones"],
                row["previous_interval_semitones"],
                row["position_pct_from_labium"],
                row["fired_position_from_labium_in"],
                row["master_position_from_labium_in"],
                row["fired_diameter_in"],
                row["greenware_drill_start_in"],
                row["incremental_conductance_in"],
                row["note"],
            ]
        )
    historical_rows: list[list[Any]] = [
        [
            "Instrument ID",
            "Hole",
            "Face",
            "Target interval semitones",
            "Prev interval",
            "Position pct",
            "Fired position in",
            "Master position in",
            "Fired diameter in",
            "Greenware drill start in",
            "Incremental conductance",
            "Notes",
        ]
    ]
    for row in historical_holes:
        historical_rows.append(
            [
                row["instrument_id"],
                row["hole"],
                row["face"],
                row["target_interval_semitones"],
                row["previous_interval_semitones"],
                row["position_pct_from_labium"],
                row["fired_position_from_labium_in"],
                row["master_position_from_labium_in"],
                row["fired_diameter_in"],
                row["greenware_drill_start_in"],
                row["incremental_conductance_in"],
                row["note"],
            ]
        )
    validation = [
        ["Check", "Formula/Target", "Notes"],
        ["A4 sanity", Formula("Inputs!B4"), "Should be 440 Hz"],
        ["C5 sanity", Formula("Inputs!B6"), "Should be 523.251 Hz"],
        ["Shrink master factor", Formula("1/(1-Inputs!B8)"), "All master dimensions scale by this"],
        ["Soprano C target volume ml", family[3]["fired_internal_volume_ml"], "Generated value; compare to water-fill measurement"],
    ]

    sheets = [
        ("Inputs", inputs),
        ("Family", family_rows),
        ("Hole Schedule", hole_rows),
        ("Historical 4+T", historical_rows),
        ("Validation", validation),
    ]
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr(
            "[Content_Types].xml",
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
            '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
            '<Default Extension="xml" ContentType="application/xml"/>'
            '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
            + "".join(
                f'<Override PartName="/xl/worksheets/sheet{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
                for i in range(1, len(sheets) + 1)
            )
            + "</Types>",
        )
        zf.writestr(
            "_rels/.rels",
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>'
            "</Relationships>",
        )
        workbook_sheets = "".join(
            f'<sheet name="{html.escape(name)}" sheetId="{i}" r:id="rId{i}"/>'
            for i, (name, _rows) in enumerate(sheets, start=1)
        )
        zf.writestr(
            "xl/workbook.xml",
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
            'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
            f"<sheets>{workbook_sheets}</sheets>"
            '<calcPr calcMode="auto" fullCalcOnLoad="1"/>'
            "</workbook>",
        )
        rels = "".join(
            f'<Relationship Id="rId{i}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{i}.xml"/>'
            for i in range(1, len(sheets) + 1)
        )
        zf.writestr(
            "xl/_rels/workbook.xml.rels",
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            f'<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">{rels}</Relationships>',
        )
        for i, (_name, rows) in enumerate(sheets, start=1):
            zf.writestr(f"xl/worksheets/sheet{i}.xml", sheet_xml(rows))


def write_index_and_manifest(family: list[dict[str, Any]]) -> None:
    file_rows = [
        ["design.md", "Project intent, acoustic model, assumptions, and file map."],
        ["authenticity-notes.md", "Historical/provenance notes and source links."],
        ["authentic-horn-build-plan.md", "Natural-horn authentic build workflow."],
        ["horn-blank-spec.csv", "Horn blank buying/selection requirements."],
        ["gemshorn-design-table.xlsx", "Parametric spreadsheet with formulas."],
        ["family-spec.csv", "Size family dimensions."],
        ["hole-schedule-modern.csv", "Modern consort hole schedule."],
        ["hole-schedule-historical.csv", "Historically informed pilot hole schedule."],
        ["mold-and-slip-casting-plan.md", "Master, mold, and casting workflow."],
        ["assembly-manual.md", "Shop sequence from casting to final tuning."],
        ["drawings/", "SVG drawings and visual BOM plate."],
        ["cad/gemshorn_family.scad", "OpenSCAD master-shape starter."],
        ["wolfram-starter.wl", "Interactive physics starter."],
    ]
    table = render_table(["File", "Purpose"], file_rows, places=2)
    text = f"""# Gemshorn Slip-Cast Family Packet

Generated: {TODAY}

## Quick Start

1. Read `design.md` and `authenticity-notes.md`.
2. Open `gemshorn-design-table.xlsx` and replace shrinkage with your clay test-bar value.
3. Build the soprano C first (`GEM-SC-C5`), then the historical G4 archetype.
4. Make one plaster mold, tune one bisque prototype, and update the validation rows before making the full consort.

## File Map

{table}

## First Build Recommendation

Start with `GEM-SC-C5` because it is small enough to cast quickly and large enough to work by hand. After that, make `GEM-HIST-G4` to test the four-hole historical path.
"""
    (PACKET_DIR / "README.md").write_text(text, encoding="utf-8")
    manifest = {
        "generated": TODAY,
        "packet": str(PACKET_DIR),
        "family_ids": [item["id"] for item in family],
        "shrinkage_assumption": SHRINKAGE,
        "base_midi": BASE_MIDI,
        "base_frequency_hz": BASE_FREQ_HZ,
        "sources": SOURCES,
    }
    (PACKET_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")


def main() -> None:
    family = [compute_size(defn) for defn in FAMILY_DEFS]
    historical = compute_size(HISTORICAL_DEF)
    modern_holes = [row for item in family for row in compute_hole_rows(item, MODERN_HOLES)]
    historical_holes = compute_hole_rows(historical, HISTORICAL_HOLES)

    write_csv(
        PACKET_DIR / "family-spec.csv",
        family + [historical],
        [
            "id",
            "name",
            "key",
            "midi",
            "freq_hz",
            "scale",
            "line",
            "fired_centerline_length_in",
            "master_centerline_length_in",
            "fired_wide_od_in",
            "master_wide_od_in",
            "fired_tip_od_in",
            "fired_wall_in",
            "fired_wide_id_in",
            "fired_tip_id_in",
            "fired_internal_volume_in3",
            "fired_internal_volume_ml",
            "window_width_in",
            "window_height_in",
            "windway_height_in",
            "labium_setback_in",
            "playing_support",
        ],
    )
    write_csv(
        PACKET_DIR / "hole-schedule-modern.csv",
        modern_holes,
        [
            "instrument_id",
            "key",
            "hole",
            "face",
            "target_interval_semitones",
            "previous_interval_semitones",
            "position_pct_from_labium",
            "fired_position_from_labium_in",
            "master_position_from_labium_in",
            "fired_diameter_in",
            "greenware_drill_start_in",
            "incremental_conductance_in",
            "hole_leff_in",
            "note",
        ],
    )
    write_csv(
        PACKET_DIR / "hole-schedule-historical.csv",
        historical_holes,
        [
            "instrument_id",
            "key",
            "hole",
            "face",
            "target_interval_semitones",
            "previous_interval_semitones",
            "position_pct_from_labium",
            "fired_position_from_labium_in",
            "master_position_from_labium_in",
            "fired_diameter_in",
            "greenware_drill_start_in",
            "incremental_conductance_in",
            "hole_leff_in",
            "note",
        ],
    )

    write_design_md(family, historical)
    write_authenticity_notes()
    write_authentic_horn_build_plan(historical, historical_holes)
    write_horn_blank_spec(historical)
    write_mold_plan()
    write_tuning_and_fingering()
    write_assembly_manual()
    write_drawing_brief(family)
    write_visual_bom_brief()
    write_supplier_rfq(family)
    write_cnc_plan()
    write_wolfram(family)
    write_scad(family)
    write_bom_and_sourcing(family)
    write_cut_and_validation(family, modern_holes, historical_holes)
    write_svg_drawings(family, modern_holes)
    write_xlsx(family, modern_holes, historical_holes)
    write_index_and_manifest(family)

    print(f"Wrote gemshorn packet to {PACKET_DIR}")


if __name__ == "__main__":
    main()
