# Slip-Cast Gemshorn Family Build Packet

Generated: 2026-05-02

Packet root: `/mnt/c/Users/Tony/Documents/GitHub/gemshorn`

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

| ID | Key | Hz | Fired L in | Master L in | Wide OD in | Volume ml | Window W in | Window H in |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GEM-SC-F3 | F3 | 174.614 | 27.719 | 31.499 | 4.645 | 2401.814 | 1.289 | 0.420 |
| GEM-SC-C4 | C4 | 261.626 | 18.500 | 21.023 | 3.100 | 649.562 | 0.860 | 0.280 |
| GEM-SC-F4 | F4 | 349.228 | 13.859 | 15.749 | 2.322 | 260.245 | 0.644 | 0.210 |
| GEM-SC-C5 | C5 | 523.251 | 9.250 | 10.511 | 1.550 | 71.554 | 0.430 | 0.140 |
| GEM-SC-F5 | F5 | 698.456 | 6.930 | 7.875 | 1.161 | 27.799 | 0.322 | 0.105 |

## Historical Archetype

Prototype: `GEM-HIST-G4` in `G4`, fired centerline length `12.35 in`, wide OD `2.07 in`, volume `180 ml`.

The historical model should be built first with waxable/reworkable holes. If you want the strictest Virdung/Agricola reading, make three front holes plus a back/thumb hole, then treat the fourth front hole in `hole-schedule-historical.csv` as an optional clay-find/modern-convenience variant.

## Manufacturing Assumptions

- Fired clay shrinkage: `12.0%` linear. Update this from your actual clay body test bars before committing to molds.
- Clay body: white stoneware or porcelain casting slip, cone 5/6 or cone 10 depending on shop practice.
- Wall: scaled from `0.130 in` at soprano C, clamped between `0.110 in` and `0.240 in`.
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
