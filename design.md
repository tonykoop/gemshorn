# Slip-Cast Gemshorn Family Build Packet

Generated: 2026-05-02
v4 refresh: 2026-05-06

Packet root: repository root

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
- `build-methods.md` - side-by-side real horn, slip-cast ceramic, CNC split wood, and research-material build methods.
- `material-options.md` - candidate materials and safety/finish gates.
- `risks.md`, `photo-shotlist.md`, `site/index.html` - v4 risk, photo, and build-log-site deliverables.
- `cnc/cnc-plan.json`, `cnc/operations.csv`, `cnc/setup-sheet.md`, `cnc/wood-body-cnc-plan.md` - CNC/router planning deliverables.
- `wolfram/gemshorn-wolfram-model.wl` - v4.2 Wolfram package.
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

## Vessel And Flue Assumptions

- Governing acoustic assumption: closed vessel / Helmholtz resonator excited by
  a duct-flute fipple, not an open-open bore, stopped pipe, NAF, reed pipe, or
  free-reed coupled pipe.
- End condition: sealed pointed tip, closed cavity, wide-end block/fipple,
  labium window, and tone holes that add incremental conductance when opened.
- Dimension provenance: current family dimensions are workbook/model planning
  values. They are `measurement_required` for production molds until the clay
  body shrinkage, fired water-fill volume, leak state, and tuner results are
  measured.
- Flue authority: windway height, labium setback, window size, and block fit
  are first-pass shop targets. Final voicing must be set by physical fipple
  response, onset, stability, and cents error, not by generated previews.
- Correction boundary: do not apply open-open flute, NAF K2, reed, or
  stopped-pipe empirical corrections to this packet unless a future measured
  gemshorn-specific correction is added with evidence.

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

## Build Methods

| Method | Status | Primary Files | Notes |
| --- | --- | --- | --- |
| Natural horn | Historically informed reference | `authentic-horn-build-plan.md`, `horn-blank-spec.csv` | Tune each horn as a one-off; no endangered/wild horn sourcing. |
| Slip-cast ceramic | Production family path | `mold-and-slip-casting-plan.md`, `family-spec.csv`, `hole-schedule-modern.csv` | Best repeatability after clay shrinkage is measured. |
| CNC-routed split wood | Modern prototype path | `cnc/wood-body-cnc-plan.md`, `cad/gemshorn_split_wood_body.scad`, `drawings/gemshorn-cnc-wood-body.svg` | Good for fast fipple, volume, and hand-layout tests. |
| Alternate materials | Research path | `material-options.md`, `risks.md`, `validation.csv` | Must pass mouth-safety, edge-retention, and leak tests. |

## Hardware Alignment

| Operation | Tool / Fixture | Applies To | Release Check |
| --- | --- | --- | --- |
| Horn blank fitting | Fine saw, scraper, drill press, tapered reamers | Natural horn | Tip remains closed; fipple block seats without leaks. |
| Mold master shaping | 3D print, CNC tooling board, or sealed master | Slip-cast ceramic | Master is scaled by measured shrinkage and releases from plaster. |
| Plaster mold making | Two-part mold box, registration keys, pour mouth | Slip-cast ceramic | Mold halves register and cast releases at leather hard. |
| Split-wood CNC routing | 1/4 in upcut, 1/4 in ball end, 1/8 in ball end, dowel-pin fixture | CNC wood body | Halves register, cavity leak test passes before shaping. |
| Hole tuning | Pin gauges, drill bits, tapered reamers, wax | All methods | Holes start undersize and tune low to high. |
| Validation | Tuner, thermometer, water-fill volume setup, calipers | All methods | `validation.csv` records measured values, cents error, and action. |

## Validation Gates

- Measure fired cavity volume by water fill before final tuning.
- Record closed note, all scale degrees, and high/tuning vent at 68 F reference or with temperature logged.
- Tune by opening holes only. Lower pitch by wax, removable clay-safe filler, or ring/vent control.
- Reject or rework bodies with warped windways, rounded labium edges, cracks at holes, or shrinkage outside the measured clay-body range.

## Open Decisions

- Actual clay body, firing cone, glaze schedule, and shrinkage test result.
- Whether the production family should be C/F consort, G/D historical consort, or both.
- Whether the tuning ring is a brass sleeve, leather wrap with rotating vent, or ceramic collar.
- Whether CNC wood bodies should use a permanent glue seam, a gasketed service seam, or both as parallel prototypes.
- Which alternate material coupons are worth testing after ceramic/wood/horn baselines.
