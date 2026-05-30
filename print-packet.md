# Gemshorn Build Methods And Slip-Cast Family Print Packet

Generated: 2026-05-06
Packet folder: `/mnt/c/Users/Tony/Documents/GitHub/gemshorn`

## File Map

| File | Purpose |
| --- | --- |
| `design.md` | Project intent, catalog metadata, assumptions, and validation plan. |
| `bom.csv` | Starter bill of materials with part categories, quantities, drawing refs, and notes. |
| `sourcing.csv` | Supplier/search tracker with specs, price/date fields, lead time, substitutes, and risks. |
| `cut-list.csv` | Rough/final stock sizes, material, grain/orientation, operations, yield, and offcuts. |
| `drawing-brief.md` | Manufacturing drawing and technical product sketch brief. |
| `assembly-manual.md` | Shop-facing sequence, tools, fixtures, safety, tuning, finishing, and maintenance notes. |
| `validation.csv` | Target/measured values, tolerance, environment, result, and tuning/build action log. |
| `supplier-rfq.md` | Supplier email/request-for-quote starter. |
| `visual-bom-brief.md` | Art direction for an image-forward visual BOM. |
| `wolfram-starter.wl` | Wolfram starter for physics, optimization, visualization, and validation. |
| `README.md` | Project artifact. |
| `authentic-horn-build-plan.md` | Project artifact. |
| `authenticity-notes.md` | Project artifact. |
| `build-methods.md` | Project artifact. |
| `family-spec.csv` | Project artifact. |
| `hole-schedule-historical.csv` | Project artifact. |
| `hole-schedule-modern.csv` | Project artifact. |
| `horn-blank-spec.csv` | Project artifact. |
| `material-options.md` | Project artifact. |
| `mold-and-slip-casting-plan.md` | Project artifact. |
| `photo-shotlist.md` | Project artifact. |
| `risks.md` | Project artifact. |
| `sources.md` | Project artifact. |
| `tuning-and-fingering.md` | Project artifact. |
| `validation-report.md` | Project artifact. |

<div class="page-break"></div>

## design.md

Project intent, catalog metadata, assumptions, and validation plan.

# Slip-Cast Gemshorn Family Build Packet

Generated: 2026-05-02
v4 refresh: 2026-05-06

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

<div class="page-break"></div>

## bom.csv

Starter bill of materials with part categories, quantities, drawing refs, and notes.

| item | part | qty | material_spec | make_buy | drawing_ref | notes |
| --- | --- | --- | --- | --- | --- | --- |
| BOM-000 | Natural horn blank | 3 blanks for first authentic prototype | Domesticated cow/ox/goat/sheep horn, closed tip, no cracks | buy | horn-blank-spec.csv | Authentic build path; avoid endangered/wild chamois sourcing |
| BOM-001 | Slip-cast ceramic body | 1 per instrument | White stoneware or porcelain casting slip, measured shrinkage | make | drawings/gemshorn-body-section.svg | Use family-spec.csv for size-specific fired and master dimensions |
| BOM-002 | Two-part plaster mold | 1 per size | Pottery plaster or equivalent | make | drawings/gemshorn-mold-schematic.svg | Add registration keys and pour mouth |
| BOM-003 | Master pattern | 1 per size | 3D printed resin/PLA, tooling board, or sealed wood | make or outsource | cad/gemshorn_family.scad | Scale for shrinkage and seal before plaster |
| BOM-004 | Fipple/block | 1 per instrument | Cedar, maple, pear, plaster, or stable hardwood | make | drawings/gemshorn-voicing-detail.svg | Removable block recommended for tuning and service |
| BOM-005 | Seal wrap/gasket | 1 set per instrument | Leather, cork, beeswax, or thin silicone gasket | buy | drawings/gemshorn-voicing-detail.svg | Keep mouth-contact material safe and replaceable |
| BOM-006 | Optional tuning ring/collar | 1 per instrument | Thin brass/stainless ring, leather band, or ceramic collar | buy or make | drawings/gemshorn-voicing-detail.svg | Rotates over vent to lower closed keynote |
| BOM-007 | Tuning and measurement kit | 1 shop set | Pin gauges, drill bits, reamers, tuner, thermometer, wax | buy | validation.csv | Required before final pitch claims |
| BOM-008 | CNC split-wood body blanks | 2 halves per prototype | Maple, cherry, pear, beech, or boxwood; straight-grained; oversized for routing | make | drawings/gemshorn-cnc-wood-body.svg | Modern CNC router build path; start with C5 or G4 |
| BOM-009 | Wood body registration dowels | 2 to 4 per prototype | 1/4 in hardwood dowels or metal datum pins | buy | cnc/wood-body-cnc-plan.md | Outside final body outline or hidden after shaping |
| BOM-010 | Wood body adhesive/seal system | 1 set per prototype | Thin even glue line plus mouth-safe interior/finish test coupon | buy | risks.md | Critical leak and mouth-safety gate |
| BOM-011 | Alternate material coupons | 1 set | Stoneware, porcelain, maple/cherry/pear, printed master material, optional acrylic teaching coupon | make or buy | material-options.md | Use coupons before committing alternate materials to instruments |

<div class="page-break"></div>

## sourcing.csv

Supplier/search tracker with specs, price/date fields, lead time, substitutes, and risks.

| item | spec | supplier_or_search_terms | price_each | date_checked | lead_time | substitution_rule | risk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Natural horn blank | Domesticated cow/ox/goat/sheep horn, closed tip, cleanable interior | cow horn blank ox horn craft horn goat horn instrument blank | TBD live check |  | TBD | Do not use endangered species; reject cracked or delaminated blanks | Each horn has different volume and curvature, so every blank is tuned empirically |
| Casting slip | White stoneware or porcelain casting slip; shrinkage data required | ceramic casting slip cone 6 porcelain stoneware gallon | TBD live check |  | TBD | Must provide shrinkage and firing cone | Shrinkage variation changes all dimensions and pitch |
| Pottery plaster | No. 1 pottery plaster or equivalent mold plaster | pottery plaster mold plaster 50 lb | TBD live check |  | TBD | Use ceramic mold plaster, not construction plaster | Poor absorption causes slow wall growth and release trouble |
| Hardwood block stock | Fine-grain stable hardwood blanks, 1/2 to 2 in depending size | cedar pear maple turning blank instrument block | TBD live check |  | TBD | Avoid resinous or mouth-unsafe finishes | Block swelling or warping changes windway |
| Leather/cork gasket | Thin natural leather, cork sheet, or mouth-safe gasket material | thin cork gasket sheet leather scrap beeswax | TBD live check |  | TBD | Must seal without shedding dust | Leaks make voicing unstable |
| Tuning ring material | Thin brass strip/tube or leather collar | thin brass strip tube hobby K&S brass | TBD live check |  | TBD | Collar must rotate smoothly and not chip clay | Rough collar damages vent edge |
| CNC wood body blank | Straight-grained maple, cherry, pear, beech, or boxwood; two oversized halves per prototype | hardwood turning blank maple cherry pear boxwood 12 inch | TBD live check |  | TBD | Substitute only with stable, mouth-safe-finish-compatible hardwood | Glue seam and humidity movement can shift tuning |
| Registration dowels | 1/4 in hardwood dowels or reusable metal datum pins | quarter inch hardwood dowel precision dowel pins | TBD live check |  | TBD | Pin diameter must match CAM and drill operation | Registration error ruins split-body alignment |
| Mouth-safe finish test materials | Shellac flakes, food-safe oil/wax, or proven instrument finish for coupons | shellac flakes food safe wood finish beeswax carnauba | TBD live check |  | TBD | Must pass mouth-contact and odor test before use | Finish can swell/round windway and labium |
| Prototype/master print material | PLA/PETG/SLA resin for sealed masters only unless mouth safety is proven | 3D print filament resin mold master sealant | TBD live check |  | TBD | Final playing body requires safety review | Layer lines leak and roughen windway |

<div class="page-break"></div>

## cut-list.csv

Rough/final stock sizes, material, grain/orientation, operations, yield, and offcuts.

| part_id | part | qty | rough_size | finished_size | material | operation | yield_or_offcut | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GEM-SC-F3-MASTER | Bass F scaled master | 1 | 33.50 x 7.28 x 7.28 in envelope | 31.50 in centerline, 5.28 in wide OD | sealed print/tooling board | print/CNC, seal, sand, polish, mark dimples | one master per size | Check mold release before committing plaster |
| GEM-SC-F3-MOLD | Bass F plaster mold | 1 | mold box about 35.50 x 9.28 x 9.28 in | two plaster halves plus pour opening | pottery plaster | cast mold halves around sealed master | reuse for production run after seasoning | Add registration keys and split-line witness marks |
| GEM-SC-C4-MASTER | Tenor C scaled master | 1 | 23.02 x 5.52 x 5.52 in envelope | 21.02 in centerline, 3.52 in wide OD | sealed print/tooling board | print/CNC, seal, sand, polish, mark dimples | one master per size | Check mold release before committing plaster |
| GEM-SC-C4-MOLD | Tenor C plaster mold | 1 | mold box about 25.02 x 7.52 x 7.52 in | two plaster halves plus pour opening | pottery plaster | cast mold halves around sealed master | reuse for production run after seasoning | Add registration keys and split-line witness marks |
| GEM-SC-F4-MASTER | Alto F scaled master | 1 | 17.75 x 4.64 x 4.64 in envelope | 15.75 in centerline, 2.64 in wide OD | sealed print/tooling board | print/CNC, seal, sand, polish, mark dimples | one master per size | Check mold release before committing plaster |
| GEM-SC-F4-MOLD | Alto F plaster mold | 1 | mold box about 19.75 x 6.64 x 6.64 in | two plaster halves plus pour opening | pottery plaster | cast mold halves around sealed master | reuse for production run after seasoning | Add registration keys and split-line witness marks |
| GEM-SC-C5-MASTER | Soprano C scaled master | 1 | 12.51 x 3.76 x 3.76 in envelope | 10.51 in centerline, 1.76 in wide OD | sealed print/tooling board | print/CNC, seal, sand, polish, mark dimples | one master per size | Check mold release before committing plaster |
| GEM-SC-C5-MOLD | Soprano C plaster mold | 1 | mold box about 14.51 x 5.76 x 5.76 in | two plaster halves plus pour opening | pottery plaster | cast mold halves around sealed master | reuse for production run after seasoning | Add registration keys and split-line witness marks |
| GEM-SC-F5-MASTER | Sopranino F scaled master | 1 | 9.87 x 3.32 x 3.32 in envelope | 7.87 in centerline, 1.32 in wide OD | sealed print/tooling board | print/CNC, seal, sand, polish, mark dimples | one master per size | Check mold release before committing plaster |
| GEM-SC-F5-MOLD | Sopranino F plaster mold | 1 | mold box about 11.87 x 5.32 x 5.32 in | two plaster halves plus pour opening | pottery plaster | cast mold halves around sealed master | reuse for production run after seasoning | Add registration keys and split-line witness marks |
| GEM-WOOD-C5-HALVES | Soprano C CNC split-wood body halves | 1 pair | 12.50 x 2.50 x 1.00 in each half | 10.50 in routed body envelope, 0.150 in min wall | maple/cherry/pear/boxwood | joint, plane, CNC route mirrored cavity, drill dowel registration | offcuts become fipple/block test coupons | Modern CNC router proof of concept |
| GEM-WOOD-G4-HALVES | Historical G4 CNC split-wood body halves | 1 pair | 15.50 x 3.00 x 1.10 in each half | 14.00 in routed body envelope, 0.160 in min wall | maple/cherry/pear/boxwood | joint, plane, CNC route mirrored cavity, drill dowel registration | offcuts become windway and finish coupons | Good comparison against natural-horn G4 |
| GEM-WOOD-DOWELS | Split-body registration dowels | 2 to 4 | 0.25 dia x 1.00 in each | 0.25 in dowel or removable metal pin | hardwood or steel | drill from CNC datum before cavity routing | trim flush or remove before exterior shaping | Keep outside tone-critical cavity |
| GEM-FINISH-COUPONS | Material/finish coupons | 1 set | 2.00 x 2.00 x 0.25 in samples | finished per material test | wood/ceramic/printed material | seal, finish, odor test, water test, edge-retention check | document in validation.csv | Required before alternate final-body materials |

<div class="page-break"></div>

## drawing-brief.md

Manufacturing drawing and technical product sketch brief.

# Drawing Brief

Generated: 2026-05-02

## Required Drawing Set

1. `drawings/gemshorn-family-scale.svg` - side-by-side family scale and title block.
2. `drawings/gemshorn-body-section.svg` - longitudinal body section with closed tip, wall, cavity, and fipple seat.
3. `drawings/gemshorn-voicing-detail.svg` - windway, block, labium, window, and tuning ring/vent.
4. `drawings/gemshorn-mold-schematic.svg` - two-part plaster mold, split line, keys, pour mouth, and release direction.
5. `drawings/hole-layout-template.svg` - soprano C hole positions and diameters for a drilling template.
6. `drawings/visual-bom-plate.svg` - visual BOM plate layout.
7. `drawings/gemshorn-cnc-wood-body.svg` - CNC split-wood body halves, datums, registration pins, operation notes, and tolerances.

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
- CNC split-wood body half stock, dowel-pin locations, cavity wall minimum, and glue seam datum.

## Tolerances

- Tone-hole final diameter: +/-0.005 in before tuning, final by pitch.
- Window width/height: +/-0.005 in on soprano and smaller, +/-0.010 in on alto and larger.
- Windway height: +/-0.003 in for soprano/sopranino, +/-0.005 in for larger sizes.
- Wall thickness: +/-15% unless structural cracks appear.
- Noncritical exterior profile: +/-0.060 in.

## Current Family Reference

| ID | Key | Fired length in | Wide OD in | Wall in |
| --- | --- | --- | --- | --- |
| GEM-SC-F3 | F3 | 27.719 | 4.645 | 0.240 |
| GEM-SC-C4 | C4 | 18.500 | 3.100 | 0.204 |
| GEM-SC-F4 | F4 | 13.859 | 2.322 | 0.169 |
| GEM-SC-C5 | C5 | 9.250 | 1.550 | 0.130 |
| GEM-SC-F5 | F5 | 6.930 | 1.161 | 0.110 |

## Notes

The SVGs are shop-reference drawings and review plates. Before making production molds, convert the dimensions into SolidWorks, OpenSCAD/STL, or another CAD system and verify mold release.

For the CNC wood path, verify `cad/gemshorn_split_wood_body.scad` in CAD/CAM before cutting. The SVG is a datum and operation drawing, not a toolpath source.

<div class="page-break"></div>

## assembly-manual.md

Shop-facing sequence, tools, fixtures, safety, tuning, finishing, and maintenance notes.

# Assembly Manual

Generated: 2026-05-02

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
- CNC router, dowel-pin fixture, ball end bits, clamps, and leak-test supplies for the split-wood method.

## Build Method Selection

See `build-methods.md` before starting.

- Use natural horn when authenticity is the goal.
- Use slip-cast ceramic when repeatability and consort scaling are the goal.
- Use CNC split wood when fast iteration and repairability are the goal.
- Use alternate materials only after coupon tests in `material-options.md` pass.

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

## CNC Split-Wood Body Method

1. Choose the C5 or G4 prototype from `build-methods.md`.
2. Prepare two straight-grained hardwood halves from `cut-list.csv`.
3. Face the mating surfaces and drill registration-pin holes.
4. Route mirrored cavity halves using `cnc/wood-body-cnc-plan.md`.
5. Engrave or mark fipple, tone-hole, and datum references.
6. Dry-fit the body with dowels and perform the leak test in `validation.csv`.
7. Glue the body only after the cavity volume and leak test pass.
8. Shape the exterior, then cut the fipple/window by hand.
9. Drill holes undersize and tune low to high.
10. Record final volume, pitch, cents error, and finish notes in `validation.csv`.

## Maintenance

- Keep removable blocks dry and replaceable.
- Avoid soaking fired ceramic bodies unless the clay/glaze combination is proven.
- Store with a cork or cloth spacer so the labium is protected.
- Keep a small wax kit for tuning during outdoor or temperature-variable use.

<div class="page-break"></div>

## validation.csv

Target/measured values, tolerance, environment, result, and tuning/build action log.

| instrument_id | check | target | measured | tolerance | environment | result | action | measured_hz | cents_error | tuner | measurement_date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GEM-SC-F3 | closed tonic frequency | 174.61 Hz |  | +/-15 cents prototype | record temp F, humidity |  | adjust cavity/window/vent before hole tuning |  |  |  |  |
| GEM-SC-F3 | fired centerline length | 27.719 in |  | +/-0.060 in | after glaze if glazed |  | update shrinkage factor if systematic |  |  |  |  |
| GEM-SC-F3 | fired internal volume | 2402 ml |  | +/-5% | water-fill, dry after |  | retune window/vent model |  |  |  |  |
| GEM-SC-C4 | closed tonic frequency | 261.63 Hz |  | +/-15 cents prototype | record temp F, humidity |  | adjust cavity/window/vent before hole tuning |  |  |  |  |
| GEM-SC-C4 | fired centerline length | 18.500 in |  | +/-0.060 in | after glaze if glazed |  | update shrinkage factor if systematic |  |  |  |  |
| GEM-SC-C4 | fired internal volume | 650 ml |  | +/-5% | water-fill, dry after |  | retune window/vent model |  |  |  |  |
| GEM-SC-F4 | closed tonic frequency | 349.23 Hz |  | +/-15 cents prototype | record temp F, humidity |  | adjust cavity/window/vent before hole tuning |  |  |  |  |
| GEM-SC-F4 | fired centerline length | 13.859 in |  | +/-0.060 in | after glaze if glazed |  | update shrinkage factor if systematic |  |  |  |  |
| GEM-SC-F4 | fired internal volume | 260 ml |  | +/-5% | water-fill, dry after |  | retune window/vent model |  |  |  |  |
| GEM-SC-C5 | closed tonic frequency | 523.25 Hz |  | +/-15 cents prototype | record temp F, humidity |  | adjust cavity/window/vent before hole tuning |  |  |  |  |
| GEM-SC-C5 | fired centerline length | 9.250 in |  | +/-0.060 in | after glaze if glazed |  | update shrinkage factor if systematic |  |  |  |  |
| GEM-SC-C5 | fired internal volume | 72 ml |  | +/-5% | water-fill, dry after |  | retune window/vent model |  |  |  |  |
| GEM-SC-F5 | closed tonic frequency | 698.46 Hz |  | +/-15 cents prototype | record temp F, humidity |  | adjust cavity/window/vent before hole tuning |  |  |  |  |
| GEM-SC-F5 | fired centerline length | 6.930 in |  | +/-0.060 in | after glaze if glazed |  | update shrinkage factor if systematic |  |  |  |  |
| GEM-SC-F5 | fired internal volume | 28 ml |  | +/-5% | water-fill, dry after |  | retune window/vent model |  |  |  |  |
| GEM-SC-F3 | H1 final diameter | 0.3409 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-F3 | H2 final diameter | 0.3936 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-F3 | H3 final diameter | 0.2857 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-F3 | H4 final diameter | 0.4914 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-F3 | H5 final diameter | 0.5723 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-F3 | H6 final diameter | 0.6692 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-F3 | H7 final diameter | 0.4727 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-F3 | T1 final diameter | 0.8530 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-C4 | H1 final diameter | 0.2347 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-C4 | H2 final diameter | 0.2699 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-C4 | H3 final diameter | 0.1977 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-C4 | H4 final diameter | 0.3345 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-C4 | H5 final diameter | 0.3875 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-C4 | H6 final diameter | 0.4504 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-C4 | H7 final diameter | 0.3222 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-C4 | T1 final diameter | 0.5687 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-F4 | H1 final diameter | 0.1780 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-F4 | H2 final diameter | 0.2043 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-F4 | H3 final diameter | 0.1502 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-F4 | H4 final diameter | 0.2525 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-F4 | H5 final diameter | 0.2919 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-F4 | H6 final diameter | 0.3386 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-F4 | H7 final diameter | 0.2434 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-F4 | T1 final diameter | 0.4258 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-C5 | H1 final diameter | 0.1208 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-C5 | H2 final diameter | 0.1383 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-C5 | H3 final diameter | 0.1021 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-C5 | H4 final diameter | 0.1703 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-C5 | H5 final diameter | 0.1963 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-C5 | H6 final diameter | 0.2270 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-C5 | H7 final diameter | 0.1643 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-C5 | T1 final diameter | 0.2840 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-F5 | H1 final diameter | 0.0917 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-F5 | H2 final diameter | 0.1048 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-F5 | H3 final diameter | 0.0777 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-F5 | H4 final diameter | 0.1287 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-F5 | H5 final diameter | 0.1480 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-F5 | H6 final diameter | 0.1707 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-F5 | H7 final diameter | 0.1242 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-SC-F5 | T1 final diameter | 0.2127 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-HIST-G4 | F1 final diameter | 0.1594 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-HIST-G4 | F2 final diameter | 0.1828 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-HIST-G4 | F3 final diameter | 0.1345 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-HIST-G4 | F4 final diameter | 0.2257 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-HIST-G4 | T1 final diameter | 0.5445 in |  | by pitch, do not oversize | after bisque and final tune |  | open gradually or wax if sharp |  |  |  |  |
| GEM-WOOD-C5 | split-body cavity leak test | no bubbles at 2 minute low-pressure test |  | pass/fail | shop bench before exterior shaping |  | seal seam or remake glue-up |  |  |  |  |
| GEM-WOOD-C5 | measured internal volume | match C5 target within +/-5% |  | +/-5% | water-fill after sealed glue-up |  | update Helmholtz model and hole schedule |  |  |  |  |
| GEM-WOOD-G4 | split-body cavity leak test | no bubbles at 2 minute low-pressure test |  | pass/fail | shop bench before exterior shaping |  | seal seam or remake glue-up |  |  |  |  |
| GEM-MATERIAL-COUPON | finish odor and mouth-contact screen | no tacky odor or surface shedding after cure |  | pass/fail | after full cure at shop temperature |  | reject finish or move finish away from mouth-contact areas |  |  |  |  |
| GEM-MATERIAL-COUPON | labium edge retention | coupon edge stays crisp after finish/wet-dry handling |  | visual and caliper check | after finish and wipe-down |  | change material or mask voicing edges |  |  |  |  |

<div class="page-break"></div>

## supplier-rfq.md

Supplier email/request-for-quote starter.

# Supplier RFQ Draft

Subject: RFQ - slip-cast ceramic gemshorn prototypes and plaster mold materials

Hello,

I am prototyping a family of slip-cast ceramic gemshorns, a small fipple/vessel-flute instrument. I am looking for pricing, lead time, and technical guidance for the following:

1. White stoneware or porcelain casting slip suitable for thin musical-instrument bodies.
2. Pottery plaster or equivalent mold plaster for two-part molds.
3. Optional 3D print or CNC master service for sealed masters up to about 31.5 in long and 5.3 in wide.
4. Small hardwood, cork, leather, or silicone sheet suitable for removable fipple blocks and seals.
5. Brass or stainless thin-wall tubing/strip for optional rotating tuning collars.

Please quote unit price, volume price, minimum order, lead time, shipping estimate, data sheets, shrinkage range, recommended firing cone, and any substitutions you recommend.

The current prototype set includes: F3, C4, F4, C5, F5. Critical requirements are stable shrinkage, clean release from plaster molds, and a fired body that can hold crisp tone-hole and voicing edges.

Thank you,
Tony

<div class="page-break"></div>

## visual-bom-brief.md

Art direction for an image-forward visual BOM.

# Visual BOM Brief

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

<div class="page-break"></div>

## wolfram-starter.wl

Wolfram starter for physics, optimization, visualization, and validation.

```wolfram
(* Slip-Cast Gemshorn Family Wolfram Starter *)
(* Generated 2026-05-02. Paste into Wolfram Desktop or Cloud. *)

ClearAll["Global`*"];

speedOfSoundInPerS = 13549.0;
shrinkage = 0.12;

family = {
  <|"ID" -> "GEM-SC-F3", "Key" -> "F3", "MIDI" -> 53, "LengthIn" -> 27.7187, "VolumeIn3" -> 146.5677, "WindowAreaIn2" -> 0.54058, "WallIn" -> 0.2400|>,
  <|"ID" -> "GEM-SC-C4", "Key" -> "C4", "MIDI" -> 60, "LengthIn" -> 18.5000, "VolumeIn3" -> 39.6387, "WindowAreaIn2" -> 0.24080, "WallIn" -> 0.2040|>,
  <|"ID" -> "GEM-SC-F4", "Key" -> "F4", "MIDI" -> 65, "LengthIn" -> 13.8593, "VolumeIn3" -> 15.8811, "WindowAreaIn2" -> 0.13514, "WallIn" -> 0.1691|>,
  <|"ID" -> "GEM-SC-C5", "Key" -> "C5", "MIDI" -> 72, "LengthIn" -> 9.2500, "VolumeIn3" -> 4.3665, "WindowAreaIn2" -> 0.06020, "WallIn" -> 0.1300|>,
  <|"ID" -> "GEM-SC-F5", "Key" -> "F5", "MIDI" -> 77, "LengthIn" -> 6.9297, "VolumeIn3" -> 1.6964, "WindowAreaIn2" -> 0.03379, "WallIn" -> 0.1100|>
};

midiToFreq[m_] := 440*2^((m - 69)/12);
centsError[measured_, target_] := 1200*Log[2, measured/target];
holeLeff[diameter_, wall_] := wall + 0.85*(diameter/2);
conductance[diameter_, wall_] := Pi*(diameter/2)^2/holeLeff[diameter, wall];
helmholtzHz[conductanceTotal_, volumeIn3_] :=
  speedOfSoundInPerS/(2*Pi)*Sqrt[conductanceTotal/volumeIn3];

Dataset[family]

Manipulate[
 Module[{freq = midiToFreq[midi], scale, volume, windowArea, wall, windowLeff, gBase, predicted},
  scale = midiToFreq[72]/freq;
  wall = Min[0.24, Max[0.11, 0.13*scale^0.65]];
  windowArea = (0.43*scale)*(0.14*scale);
  windowLeff = wall + 0.85*Sqrt[windowArea/Pi];
  gBase = windowArea/windowLeff;
  volume = 4.366467*scale^3;
  predicted = helmholtzHz[gBase, volume];
  Column[{
    Row[{"Target Hz: ", NumberForm[freq, {6, 2}]}],
    Row[{"Predicted closed Hz: ", NumberForm[predicted, {6, 2}]}],
    Row[{"Cents error: ", NumberForm[centsError[predicted, freq], {6, 1}]}],
    Row[{"Scale factor: ", NumberForm[scale, {5, 3}]}],
    Row[{"Volume in3: ", NumberForm[volume, {7, 3}]}],
    Row[{"Window area in2: ", NumberForm[windowArea, {6, 4}]}]
  }]
 ],
 {{midi, 72, "Closed-note MIDI"}, 53, 77, 1}
]

(* Import validation.csv after prototypes exist:
validation = Import["validation.csv", "Dataset"];
*)
```

<div class="page-break"></div>

## README.md

Project artifact.

# Gemshorn

![Gemshorn family scale drawing](drawings/gemshorn-family-scale.svg)

Generated/refreshed: 2026-05-06

This repo is the build documentation for an authentic/historically informed gemshorn and a modern slip-cast gemshorn consort. A gemshorn is a closed horn-shaped vessel flute: the pointed end is sealed, the wide end carries the fipple/block and voicing window, and pitch is governed primarily by chamber volume, window/vent conductance, and opened tone-hole area.

The repo deliberately separates the strict historical path from modern production paths. Natural horn is the authenticity reference; slip-cast ceramic is the repeatable family path; CNC-routed split wood is a modern prototype path for quick iteration and teaching.

## Quick Start

1. Read `design.md`, `build-methods.md`, and `authenticity-notes.md`.
2. Open `gemshorn-design-table.xlsx` and replace shrinkage with your clay test-bar value.
3. Build the CNC-routed wood `GEM-SC-C5` if you want the fastest fipple/tuning test.
4. Build the slip-cast ceramic `GEM-SC-C5` to validate shrinkage and mold workflow.
5. Build the natural-horn `GEM-HIST-G4` to establish the authentic reference voice.
6. Update `validation.csv` after each prototype before scaling the full family.

## Build Methods

| Method | Purpose | Main Files |
| --- | --- | --- |
| Natural horn | Most historically conservative build path | `authentic-horn-build-plan.md`, `horn-blank-spec.csv`, `hole-schedule-historical.csv` |
| Slip-cast ceramic | Repeatable production family | `mold-and-slip-casting-plan.md`, `family-spec.csv`, `hole-schedule-modern.csv` |
| CNC-routed split wood | Modern fast prototype / teaching body | `cnc/wood-body-cnc-plan.md`, `cad/gemshorn_split_wood_body.scad`, `drawings/gemshorn-cnc-wood-body.svg` |
| Alternate materials | Research and prototyping candidates | `material-options.md`, `risks.md`, `validation.csv` |

## File Map

| File | Purpose |
| --- | --- |
| design.md | Project intent, acoustic model, assumptions, and file map. |
| build-methods.md | Real horn, slip-cast ceramic, CNC wood, and research-material build paths. |
| material-options.md | Candidate body/block/finish materials and safety gates. |
| authenticity-notes.md | Historical/provenance notes and source links. |
| authentic-horn-build-plan.md | Natural-horn authentic build workflow. |
| horn-blank-spec.csv | Horn blank buying/selection requirements. |
| gemshorn-design-table.xlsx | Parametric spreadsheet with formulas. |
| family-spec.csv | Size family dimensions. |
| hole-schedule-modern.csv | Modern consort hole schedule. |
| hole-schedule-historical.csv | Historically informed pilot hole schedule. |
| mold-and-slip-casting-plan.md | Master, mold, and casting workflow. |
| assembly-manual.md | Shop sequence from casting to final tuning. |
| risks.md | Red-team risk register with tests and mitigations. |
| photo-shotlist.md | Required photos for the v4 build-log site and future deck refreshes. |
| drawings/ | SVG drawings, visual BOM plate, and CNC wood-body drawing. |
| cad/ | OpenSCAD master-shape starters for ceramic and split-wood paths. |
| cnc/ | CNC operation plan, setup sheet, operations table, and wood-body CNC notes. |
| images/ | Placeholder folder and naming rules for future real build photos. |
| data/ | Material-test matrix and future measured-data tables. |
| wolfram-starter.wl | Lightweight physics starter. |
| wolfram/gemshorn-wolfram-model.wl | v4.2 Wolfram model package. |
| site/index.html | Static build-log site. |
| print-packet.html / print-packet.pdf | Shop packet for browser or print use. |
| capstone-deck.md / capstone-deck.pptx | Capstone orientation deck. |

## First Build Recommendation

Start with a wood or ceramic `GEM-SC-C5` because it is small enough to make quickly and large enough to work by hand. After that, make `GEM-HIST-G4` in real horn to test the historically informed four-hole path. Expand to bass/tenor only after measured shrinkage, volume, leak, and tuning corrections are in `validation.csv`.

## v4 Deliverable Status

- Parametric design: `gemshorn-design-table.xlsx`
- Build methods: `build-methods.md`
- BOM/sourcing/cut/validation: `bom.csv`, `sourcing.csv`, `cut-list.csv`, `validation.csv`
- Drawings: `drawings/*.svg`
- CNC plan: `cnc/cnc-plan.json`, `cnc/operations.csv`, `cnc/setup-sheet.md`
- Wolfram package: `wolfram/gemshorn-wolfram-model.wl`
- Risks: `risks.md`
- Photo pipeline: `photo-shotlist.md`
- Build-log site: `site/index.html`
- Capstone and print packet: `capstone-deck.*`, `print-packet.*`

<div class="page-break"></div>

## authentic-horn-build-plan.md

Project artifact.

# Authentic Natural-Horn Gemshorn Build Plan

Generated: 2026-05-02

## Intent

This is the most historically conservative build path in the packet: a short curved horn body with a fipple/block at the wide end, closed pointed tip, limited hole count, and soft vessel-flute voice. Use domesticated cow, ox, goat, or sheep horn. Do not source endangered chamois or wild-animal horn.

## Target Prototype

- Prototype ID: `GEM-HIST-G4`
- Suggested starting pitch: `G4` at `392.00 Hz`
- Design centerline length: `12.35 in`
- Wide OD target: `2.07 in`
- Internal volume target: `180 ml`
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

| Hole | Face | From labium in | Final dia in | Green/pilot dia in | Target |
| --- | --- | --- | --- | --- | --- |
| F1 | front distal | 5.309 | 0.159 | 0.181 | +2 semitones |
| F2 | front | 4.198 | 0.183 | 0.208 | +4 semitones |
| F3 | front | 3.334 | 0.135 | 0.153 | +5 semitones |
| F4 | front proximal | 2.531 | 0.226 | 0.256 | +7 semitones |
| T1 | back thumb | 2.531 | 0.544 | 0.619 | +12 semitones |

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

<div class="page-break"></div>

## authenticity-notes.md

Project artifact.

# Authenticity Notes

Generated: 2026-05-02

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

- [Horace Fitzpatrick, The Gemshorn: a Reconstruction](https://www.cambridge.org/core/journals/proceedings-of-the-royal-musical-association/article/gemshorn-a-reconstruction/0AD60F0FE7748111C8455FA2F4DD1CC3): Defines the gemshorn as a fipple instrument made from animal horn and calls out the stopped inverted cone bore. Used as the boundary-condition anchor.
- [Early Music Muse, The gemshorn: a short history](https://earlymusicmuse.com/gemshorn/): Summarizes the open-end fipple construction, four-hole historical evidence, and the 1455 clay gemshorn-like find. Used for authenticity notes.
- [Cincinnati Early Music, Medieval Gemshorn](https://cincinnatiearlymusic.com/gemshorn.html): Contrasts historical four-hole evidence with modern recorder-like reconstructions and consort families. Used to separate historical and modern lines.
- [Baltimore Recorders, Information about the Gemshorn](https://www.baltimorerecorders.org/gemshorns.html): Describes front holes, thumb hole, whistle/fipple, tuning ring, and the lack of an outlet other than whistle and fingerholes. Used for construction details.
- [Institut fuer Musikforschung Wuerzburg, Lo 29-31 Gemshoerner](https://www.musikwissenschaft.uni-wuerzburg.de/musikinstrumente/bestand/inventarliste/lo29-31-gemshoerner/): Gives measured modern HFK gemshorns in g, d1, and g1 and cautions that modern gemshorns are reconstruction products. Used as dimensional sanity check.

## Provenance Warning

No file in this packet claims to reproduce an extant original gemshorn exactly. The historical record is sparse; this packet gives a traceable and tunable workshop path with explicit assumptions.

<div class="page-break"></div>

## build-methods.md

Project artifact.

# Gemshorn Build Methods

Generated: 2026-05-06

## Build Method Matrix

| Method | Authenticity | Repeatability | Tooling | Best First Size | Main Risk | Recommended Use |
| --- | --- | --- | --- | --- | --- | --- |
| Natural horn | Highest historical fit | Low, each blank differs | Hand tools, drill press, block fitting tools | `GEM-HIST-G4` | Horn volume/curve varies and forces empirical tuning | Make the historically informed reference instrument |
| Slip-cast ceramic | Historically plausible clay lineage, modern process | High after shrinkage data | Master, plaster mold, casting slip, kiln | `GEM-SC-C5` | Shrinkage and voicing edge movement | Make the repeatable consort family |
| CNC-routed wood split body | Modern adaptation | Medium to high | CNC router, flip jig, clamps, glue-up, fipple tools | `GEM-SC-C5` or `GEM-HIST-G4` | Glue seam leaks and routed cavity volume error | Make fast prototypes and serviceable teaching instruments |
| 3D printed body | Modern prototype only | High | SLA/FDM printer, sealant, post-processing | `GEM-SC-C5` | Mouth safety, porosity, rough windway | Fit/ergonomics tests before committing molds |
| Carved hardwood solid horn | Modern craft adaptation | Low to medium | Carving, gouges, drills, fipple tools | `GEM-HIST-G4` | Internal volume hard to control | One-off art instrument |
| Metal spun/formed shell | Modern experimental | Medium after tooling | Metal forming or fabrication | Alto/tenor only | Condensation, sharp edges, tuning vent noise | Research or sculpture, not first playable build |
| Gourd/calabash or seed pod | Folk-adjacent experiment | Low | Hand tools, sealing, block fitting | Small high register | Cracking and inconsistent volume | Acoustic experiment, not production |
| Resin/composite cast | Modern prototype | High | Silicone mold or printed mold, resin safety controls | `GEM-SC-C5` | Mouth-contact safety and off-gassing | Non-mouth-contact display or sealed prototype only |

## Method 1: Natural-Horn Gemshorn

Use `authentic-horn-build-plan.md` and `horn-blank-spec.csv`.

1. Select several domesticated cow, ox, goat, or sheep horn blanks.
2. Clean and stabilize the cavity while keeping the tip closed.
3. Fit a removable hardwood or plaster block at the wide end.
4. Cut the windway and labium before drilling tone holes.
5. Tune the closed note by block/window/vent behavior.
6. Drill holes undersize, tune low to high, and record final values in `validation.csv`.

This method should be labeled "historically informed reconstruction." Do not claim a museum copy unless the exact source instrument and dimensions are known.

## Method 2: Slip-Cast Ceramic Family

Use `mold-and-slip-casting-plan.md`, `family-spec.csv`, and `hole-schedule-modern.csv`.

1. Confirm clay shrinkage with test bars.
2. Make the `GEM-SC-C5` master first.
3. Cast a two-part plaster mold around a sealed master.
4. Cast one body, bisque, measure volume, and tune.
5. Update the design table before scaling to larger family members.
6. Keep the windway, labium, tone-hole interiors, and block seat unglazed.

This is the best production path once shrinkage and tuning corrections are measured.

## Method 3: CNC-Routed Split-Wood Body

Use `cad/gemshorn_split_wood_body.scad`, `drawings/gemshorn-cnc-wood-body.svg`, and `cnc/wood-body-cnc-plan.md`.

1. Mill two matching wood halves oversized.
2. Route registration-pin holes.
3. Route mirrored internal cavity halves with a ball end or round-nose bit.
4. Add tone-hole pilot marks and fipple/window layout.
5. Dry-fit with dowel pins and test the closed cavity for leaks.
6. Glue with a thin, continuous, reversible-enough seam strategy for prototypes.
7. Shape exterior, cut the voicing, and tune as a vessel flute.

This path is not historically authentic, but it is valuable because the body can be measured, repaired, and iterated without kiln or horn-blank variability.

## Method 4: Prototype And Research Materials

Use `material-options.md` before committing to any material outside horn, ceramic, or wood. The material must pass three gates:

- It must be safe around the mouth after finish.
- It must hold a crisp labium edge and stable tone-hole edges.
- It must maintain airtight seams and predictable cavity volume.

## Recommended Build Sequence

1. CNC-routed wood `GEM-SC-C5` to prove the fipple and Helmholtz schedule quickly.
2. Slip-cast ceramic `GEM-SC-C5` to validate shrinkage and mold process.
3. Natural-horn `GEM-HIST-G4` to establish the authentic reference voice.
4. Expand the ceramic family from C5 outward after measured corrections exist.

<div class="page-break"></div>

## family-spec.csv

Project artifact.

| id | name | key | midi | freq_hz | scale | line | fired_centerline_length_in | master_centerline_length_in | fired_wide_od_in | master_wide_od_in | fired_tip_od_in | fired_wall_in | fired_wide_id_in | fired_tip_id_in | fired_internal_volume_in3 | fired_internal_volume_ml | window_width_in | window_height_in | windway_height_in | labium_setback_in | playing_support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GEM-SC-F3 | Bass F | F3 | 53 | 174.6141 | 2.9966 | modern slip-cast consort | 27.7187 | 31.4985 | 4.6448 | 5.2781 | 1.0788 | 0.24 | 4.1648 | 0.5988 | 146.5677 | 2401.8139 | 1.2885 | 0.4195 | 0.0589 | 1.2885 | bench, lap, or simple sling; large horn |
| GEM-SC-C4 | Tenor C | C4 | 60 | 261.6256 | 2.0 | modern slip-cast consort | 18.5 | 21.0227 | 3.1 | 3.5227 | 0.72 | 0.204 | 2.692 | 0.312 | 39.6387 | 649.5624 | 0.86 | 0.28 | 0.0481 | 0.86 | two-hand standing or seated |
| GEM-SC-F4 | Alto F | F4 | 65 | 349.2282 | 1.4983 | modern slip-cast consort | 13.8593 | 15.7493 | 2.3224 | 2.6391 | 0.5394 | 0.1691 | 1.9842 | 0.2012 | 15.8811 | 260.245 | 0.6443 | 0.2098 | 0.0416 | 0.6443 | comfortable hand instrument |
| GEM-SC-C5 | Soprano C | C5 | 72 | 523.2511 | 1.0 | modern slip-cast consort baseline | 9.25 | 10.5114 | 1.55 | 1.7614 | 0.36 | 0.13 | 1.29 | 0.1 | 4.3665 | 71.5536 | 0.43 | 0.14 | 0.034 | 0.43 | primary pilot size |
| GEM-SC-F5 | Sopranino F | F5 | 77 | 698.4565 | 0.7492 | modern slip-cast consort | 6.9297 | 7.8746 | 1.1612 | 1.3195 | 0.2697 | 0.11 | 0.9412 | 0.0497 | 1.6964 | 27.799 | 0.3221 | 0.1049 | 0.0294 | 0.3221 | small hand instrument; hole accuracy is critical |
| GEM-HIST-G4 | Historical Clay/Horn Archetype | G4 | 67 | 391.9954 | 1.3348 | historically informed 4 front plus thumb study | 12.3473 | 14.031 | 2.069 | 2.3511 | 0.4805 | 0.1568 | 1.7553 | 0.1669 | 10.9964 | 180.1994 | 0.574 | 0.1869 | 0.0393 | 0.574 | small hand instrument; exact historical pitch is not known |

<div class="page-break"></div>

## hole-schedule-historical.csv

Project artifact.

| instrument_id | key | hole | face | target_interval_semitones | previous_interval_semitones | position_pct_from_labium | fired_position_from_labium_in | master_position_from_labium_in | fired_diameter_in | greenware_drill_start_in | incremental_conductance_in | hole_leff_in | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GEM-HIST-G4 | G4 | F1 | front distal | 2 | 0 | 0.43 | 5.3093 | 6.0333 | 0.1594 | 0.1811 | 0.0888 | 0.2246 | whole-tone hole |
| GEM-HIST-G4 | G4 | F2 | front | 4 | 2 | 0.34 | 4.1981 | 4.7705 | 0.1828 | 0.2077 | 0.1119 | 0.2345 | third hole |
| GEM-HIST-G4 | G4 | F3 | front | 5 | 4 | 0.27 | 3.3338 | 3.7884 | 0.1345 | 0.1529 | 0.0664 | 0.214 | fourth hole; omit or wax for stricter 3-front interpretation |
| GEM-HIST-G4 | G4 | F4 | front proximal | 7 | 5 | 0.205 | 2.5312 | 2.8764 | 0.2257 | 0.2564 | 0.1583 | 0.2528 | fifth hole |
| GEM-HIST-G4 | G4 | T1 | back thumb | 12 | 7 | 0.205 | 2.5312 | 2.8764 | 0.5445 | 0.6187 | 0.5997 | 0.3883 | octave-area vent; tune empirically |

<div class="page-break"></div>

## hole-schedule-modern.csv

Project artifact.

| instrument_id | key | hole | face | target_interval_semitones | previous_interval_semitones | position_pct_from_labium | fired_position_from_labium_in | master_position_from_labium_in | fired_diameter_in | greenware_drill_start_in | incremental_conductance_in | hole_leff_in | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GEM-SC-F3 | F3 | H1 | front distal | 2 | 0 | 0.479 | 13.2772 | 15.0878 | 0.3409 | 0.3873 | 0.2371 | 0.3849 | open first for scale degree 2 |
| GEM-SC-F3 | F3 | H2 | front | 4 | 2 | 0.424 | 11.7527 | 13.3554 | 0.3936 | 0.4473 | 0.2987 | 0.4073 | open second for scale degree 3 |
| GEM-SC-F3 | F3 | H3 | front | 5 | 4 | 0.369 | 10.2282 | 11.6229 | 0.2857 | 0.3246 | 0.1773 | 0.3614 | open third for scale degree 4 |
| GEM-SC-F3 | F3 | H4 | front | 7 | 5 | 0.316 | 8.7591 | 9.9535 | 0.4914 | 0.5584 | 0.4225 | 0.4488 | open fourth for scale degree 5 |
| GEM-SC-F3 | F3 | H5 | front | 9 | 7 | 0.263 | 7.29 | 8.2841 | 0.5723 | 0.6503 | 0.5323 | 0.4832 | open fifth for scale degree 6 |
| GEM-SC-F3 | F3 | H6 | front | 11 | 9 | 0.21 | 5.8209 | 6.6147 | 0.6692 | 0.7604 | 0.6706 | 0.5244 | open sixth for scale degree 7 |
| GEM-SC-F3 | F3 | H7 | front proximal | 12 | 11 | 0.157 | 4.3518 | 4.9453 | 0.4727 | 0.5372 | 0.3981 | 0.4409 | open seventh for octave |
| GEM-SC-F3 | F3 | T1 | back thumb | 14 | 12 | 0.157 | 4.3518 | 4.9453 | 0.853 | 0.9693 | 0.9484 | 0.6025 | opens to ninth or acts as high-note/tuning vent |
| GEM-SC-C4 | C4 | H1 | front distal | 2 | 0 | 0.479 | 8.8615 | 10.0699 | 0.2347 | 0.2667 | 0.1425 | 0.3038 | open first for scale degree 2 |
| GEM-SC-C4 | C4 | H2 | front | 4 | 2 | 0.424 | 7.844 | 8.9136 | 0.2699 | 0.3067 | 0.1795 | 0.3187 | open second for scale degree 3 |
| GEM-SC-C4 | C4 | H3 | front | 5 | 4 | 0.369 | 6.8265 | 7.7574 | 0.1977 | 0.2246 | 0.1066 | 0.288 | open third for scale degree 4 |
| GEM-SC-C4 | C4 | H4 | front | 7 | 5 | 0.316 | 5.846 | 6.6432 | 0.3345 | 0.3801 | 0.2538 | 0.3461 | open fourth for scale degree 5 |
| GEM-SC-C4 | C4 | H5 | front | 9 | 7 | 0.263 | 4.8655 | 5.529 | 0.3875 | 0.4403 | 0.3198 | 0.3687 | open fifth for scale degree 6 |
| GEM-SC-C4 | C4 | H6 | front | 11 | 9 | 0.21 | 3.885 | 4.4148 | 0.4504 | 0.5118 | 0.403 | 0.3954 | open sixth for scale degree 7 |
| GEM-SC-C4 | C4 | H7 | front proximal | 12 | 11 | 0.157 | 2.9045 | 3.3006 | 0.3222 | 0.3662 | 0.2392 | 0.3409 | open seventh for octave |
| GEM-SC-C4 | C4 | T1 | back thumb | 14 | 12 | 0.157 | 2.9045 | 3.3006 | 0.5687 | 0.6462 | 0.5699 | 0.4457 | opens to ninth or acts as high-note/tuning vent |
| GEM-SC-F4 | F4 | H1 | front distal | 2 | 0 | 0.479 | 6.6386 | 7.5439 | 0.178 | 0.2023 | 0.1017 | 0.2447 | open first for scale degree 2 |
| GEM-SC-F4 | F4 | H2 | front | 4 | 2 | 0.424 | 5.8764 | 6.6777 | 0.2043 | 0.2322 | 0.1281 | 0.2559 | open second for scale degree 3 |
| GEM-SC-F4 | F4 | H3 | front | 5 | 4 | 0.369 | 5.1141 | 5.8115 | 0.1502 | 0.1707 | 0.0761 | 0.2329 | open third for scale degree 4 |
| GEM-SC-F4 | F4 | H4 | front | 7 | 5 | 0.316 | 4.3796 | 4.9768 | 0.2525 | 0.287 | 0.1812 | 0.2764 | open fourth for scale degree 5 |
| GEM-SC-F4 | F4 | H5 | front | 9 | 7 | 0.263 | 3.645 | 4.1421 | 0.2919 | 0.3317 | 0.2283 | 0.2931 | open fifth for scale degree 6 |
| GEM-SC-F4 | F4 | H6 | front | 11 | 9 | 0.21 | 2.9105 | 3.3073 | 0.3386 | 0.3847 | 0.2877 | 0.313 | open sixth for scale degree 7 |
| GEM-SC-F4 | F4 | H7 | front proximal | 12 | 11 | 0.157 | 2.1759 | 2.4726 | 0.2434 | 0.2766 | 0.1708 | 0.2725 | open seventh for octave |
| GEM-SC-F4 | F4 | T1 | back thumb | 14 | 12 | 0.157 | 2.1759 | 2.4726 | 0.4258 | 0.4839 | 0.4068 | 0.3501 | opens to ninth or acts as high-note/tuning vent |
| GEM-SC-C5 | C5 | H1 | front distal | 2 | 0 | 0.479 | 4.4307 | 5.0349 | 0.1208 | 0.1372 | 0.0632 | 0.1813 | open first for scale degree 2 |
| GEM-SC-C5 | C5 | H2 | front | 4 | 2 | 0.424 | 3.922 | 4.4568 | 0.1383 | 0.1572 | 0.0796 | 0.1888 | open second for scale degree 3 |
| GEM-SC-C5 | C5 | H3 | front | 5 | 4 | 0.369 | 3.4133 | 3.8787 | 0.1021 | 0.1161 | 0.0473 | 0.1734 | open third for scale degree 4 |
| GEM-SC-C5 | C5 | H4 | front | 7 | 5 | 0.316 | 2.923 | 3.3216 | 0.1703 | 0.1935 | 0.1126 | 0.2024 | open fourth for scale degree 5 |
| GEM-SC-C5 | C5 | H5 | front | 9 | 7 | 0.263 | 2.4327 | 2.7645 | 0.1963 | 0.2231 | 0.1418 | 0.2134 | open fifth for scale degree 6 |
| GEM-SC-C5 | C5 | H6 | front | 11 | 9 | 0.21 | 1.9425 | 2.2074 | 0.227 | 0.258 | 0.1787 | 0.2265 | open sixth for scale degree 7 |
| GEM-SC-C5 | C5 | H7 | front proximal | 12 | 11 | 0.157 | 1.4523 | 1.6503 | 0.1643 | 0.1867 | 0.1061 | 0.1998 | open seventh for octave |
| GEM-SC-C5 | C5 | T1 | back thumb | 14 | 12 | 0.157 | 1.4523 | 1.6503 | 0.284 | 0.3228 | 0.2527 | 0.2507 | opens to ninth or acts as high-note/tuning vent |
| GEM-SC-F5 | F5 | H1 | front distal | 2 | 0 | 0.479 | 3.3193 | 3.7719 | 0.0917 | 0.1042 | 0.0443 | 0.149 | open first for scale degree 2 |
| GEM-SC-F5 | F5 | H2 | front | 4 | 2 | 0.424 | 2.9382 | 3.3388 | 0.1048 | 0.1191 | 0.0558 | 0.1545 | open second for scale degree 3 |
| GEM-SC-F5 | F5 | H3 | front | 5 | 4 | 0.369 | 2.557 | 2.9057 | 0.0777 | 0.0883 | 0.0331 | 0.143 | open third for scale degree 4 |
| GEM-SC-F5 | F5 | H4 | front | 7 | 5 | 0.316 | 2.1898 | 2.4884 | 0.1287 | 0.1462 | 0.079 | 0.1647 | open fourth for scale degree 5 |
| GEM-SC-F5 | F5 | H5 | front | 9 | 7 | 0.263 | 1.8225 | 2.071 | 0.148 | 0.1682 | 0.0995 | 0.1729 | open fifth for scale degree 6 |
| GEM-SC-F5 | F5 | H6 | front | 11 | 9 | 0.21 | 1.4552 | 1.6537 | 0.1707 | 0.194 | 0.1254 | 0.1825 | open sixth for scale degree 7 |
| GEM-SC-F5 | F5 | H7 | front proximal | 12 | 11 | 0.157 | 1.088 | 1.2363 | 0.1242 | 0.1411 | 0.0744 | 0.1628 | open seventh for octave |
| GEM-SC-F5 | F5 | T1 | back thumb | 14 | 12 | 0.157 | 1.088 | 1.2363 | 0.2127 | 0.2417 | 0.1773 | 0.2004 | opens to ninth or acts as high-note/tuning vent |

<div class="page-break"></div>

## horn-blank-spec.csv

Project artifact.

| use_case | preferred_material | blank_centerline_length_in | wide_end_od_in | minimum_wall_in | tip_condition | reject_if | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Historical G4 pilot | domesticated cow, ox, goat, or sheep horn | 13.35 to 16.35 | 1.76 to 2.59 | 0.070 near wide end after cleaning | closed or plug-friendly | cracked, delaminated, moldy core, thin/transparent wall at voicing, severe twist under hands | Buy several blanks; tune by measured volume and final holes |
| Small high historical pilot | goat or sheep horn | 7.5 to 10.5 | 1.2 to 1.8 | 0.055 near wide end after cleaning | closed | too small for removable block or stable windway | Good fast test for fipple and hole-count behavior |
| Lower/alto horn pilot | cow or ox horn | 13.5 to 18.0 | 1.8 to 3.0 | 0.080 near wide end after cleaning | closed or permanently pluggable | wide end too oval to seal with a block | Likely more playable than very small horns for first tuning tests |

<div class="page-break"></div>

## material-options.md

Project artifact.

# Gemshorn Material Options

Generated: 2026-05-06

## Material Selection Rules

A gemshorn body is a closed vessel flute. The material mostly affects durability, edge stability, moisture behavior, weight, and finish, while pitch is dominated by chamber volume, window/vent area, tone-hole conductance, and fipple behavior.

Use any alternate material only after a small coupon proves:

- The labium edge can stay crisp.
- The windway can stay smooth and airtight.
- The material is safe for mouth contact after finish.
- The body can be cleaned and dried without swelling, softening, or shedding dust.

## Candidate Materials

| Material | Build Path | Pros | Risks | Recommendation |
| --- | --- | --- | --- | --- |
| Cow/ox/goat/sheep horn | Natural horn | Strong authenticity, beautiful surface, naturally curved closed cone | Variable volume, odor/dust while working, ethical sourcing | Best authentic reference path |
| White stoneware casting slip | Slip-cast | Durable, repeatable, historically plausible clay form | Shrinkage, warping, glaze shifts pitch | Best production family path |
| Porcelain casting slip | Slip-cast | Fine detail, crisp holes, clean white body | More brittle, shrinkage can be high | Good after stoneware pilot |
| Maple, cherry, pear, boxwood | CNC split wood | Stable, machinable, good edge detail | Glue seam leaks, humidity movement | Best CNC router path |
| Cedar or cypress | CNC split wood/block | Easy to work, light, traditional windway/block feel | Soft labium, dents, resin/finish concerns | Good for removable blocks, not first body |
| Bamboo or cane | Hand-built tube/horn-like adaptation | Light, musical, low cost | Natural tube is not horn-shaped and tip sealing is awkward | Good experiment, not authentic gemshorn |
| Gourd/calabash | Hand-built vessel | Folk resonance, light | Cracks, inconsistent wall, hard fipple seat | Experimental only |
| SLA resin | Printed prototype | Accurate shape, fast iteration | Mouth safety and post-cure uncertainty | Use for masters or non-mouth-contact prototypes |
| PETG/PLA | FDM prototype/master | Cheap, fast, good mold master after sealing | Layer leaks, rough windway, heat sensitivity | Use as mold master, not final instrument |
| Machinable wax/tooling board | CNC master | Stable for mold masters | Not final instrument material | Excellent for plaster mold masters |
| Aluminum/brass/copper | Metal shell | Durable, striking look | Condensation, thermal feel, sharp-edge risk, fabrication complexity | Advanced research only |
| Acrylic/polycarbonate | CNC/laser/formed prototype | Transparent tuning demo | Mouth safety, solvent crazing, brittle chips | Teaching display only unless safety proven |
| Bone/antler | Hand-built | Dense and visually related to horn | Ethical sourcing, dust hazards, small sizes | Avoid for first builds |

## Preferred Material Stack

| Component | Preferred | Acceptable Substitute | Avoid |
| --- | --- | --- | --- |
| Authentic body | Domesticated horn | Burnished ceramic historical pilot | Wild/endangered horn |
| Ceramic production body | White stoneware slip | Porcelain slip | Unknown shrinkage hobby clay |
| CNC wood body | Maple, cherry, pear, boxwood | Walnut, birch, beech | Open-pore oily woods near mouth |
| Fipple/block | Pear, maple, cedar | Plaster or sealed hardwood | Soft crumbly wood, toxic finishes |
| Gasket/seal | Cork, leather, beeswax | Food-safe silicone | Permanent brittle epoxy at tuning joints |
| Finish near mouth | Burnish, shellac after safety review, food-safe oil/wax | Exterior-only glaze away from windway | Heavy glaze in windway or hole interiors |

## Material Experiments Worth Doing

1. Ceramic body with wood removable block.
2. CNC maple split body with cork gasket and reversible block.
3. Transparent acrylic section model for teaching airflow and cavity behavior.
4. 3D printed master versus CNC tooling-board master shrinkage comparison.
5. Porcelain versus stoneware tuning shift after glaze fire.

<div class="page-break"></div>

## mold-and-slip-casting-plan.md

Project artifact.

# Mold And Slip-Casting Plan

Generated: 2026-05-02

## Build Strategy

Use a sealed master for each size and make a two-part plaster mold with the split line along the outside curvature. The wide end acts as the pour opening and later receives the fipple/block system.

## Master Prep

1. Print or CNC the master from `cad/gemshorn_family.scad` dimensions.
2. Scale all fired dimensions by `1/(1 - shrinkage)`. The default packet value is `1.1364`.
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

<div class="page-break"></div>

## photo-shotlist.md

Project artifact.

# Gemshorn Photo Shot List

Generated: 2026-05-06

This shot list feeds the v4 build-log site and future capstone/print refreshes. Use real photos when prototypes exist; until then, the SVG drawings are placeholders.

## Required Hero And Overview

| Shot ID | Subject | Purpose | Status |
| --- | --- | --- | --- |
| HERO-001 | Full family lineup, bass F through sopranino F | README and build-log hero | Needed |
| HERO-002 | Historical horn blank beside ceramic body | Shows authentic vs production paths | Needed |
| HERO-003 | Soprano C pilot in hand | Scale/ergonomics | Needed |

## Natural-Horn Build

| Shot ID | Subject | Purpose | Status |
| --- | --- | --- | --- |
| HORN-001 | Raw horn blanks, rejected and accepted examples | Blank-selection documentation | Needed |
| HORN-002 | Cleaned horn cavity and closed tip | Shows boundary condition | Needed |
| HORN-003 | Fitted removable block before windway cut | Fipple construction | Needed |
| HORN-004 | Labium/window detail | Critical voicing reference | Needed |
| HORN-005 | Final hole layout and tuning wax | Tuning method | Needed |

## Slip-Cast Ceramic Build

| Shot ID | Subject | Purpose | Status |
| --- | --- | --- | --- |
| CER-001 | Sealed master with split-line marks | Mold-making reference | Needed |
| CER-002 | Two-part plaster mold open | Mold layout and registration | Needed |
| CER-003 | Leather-hard cast with pilot holes | Greenware state | Needed |
| CER-004 | Bisque body with temporary block | First playable test | Needed |
| CER-005 | Finished glazed/burnished body | Final product | Needed |

## CNC-Routed Wood Build

| Shot ID | Subject | Purpose | Status |
| --- | --- | --- | --- |
| CNC-001 | Two wood halves on spoilboard with datum pins | Workholding proof | Needed |
| CNC-002 | Routed cavity halves before glue-up | Shows internal geometry | Needed |
| CNC-003 | Dry-fit leak test | Quality gate | Needed |
| CNC-004 | Exterior shaping and fipple detail | CNC-to-handwork transition | Needed |
| CNC-005 | Finished wood prototype next to ceramic pilot | Material comparison | Needed |

## Validation And Audio

| Shot ID | Subject | Purpose | Status |
| --- | --- | --- | --- |
| VAL-001 | Tuner reading for closed note | Evidence for `validation.csv` | Needed |
| VAL-002 | Water-fill volume measurement | Helmholtz model correction | Needed |
| VAL-003 | Hole diameter with pin gauge/calipers | Tuning traceability | Needed |
| VAL-004 | Short audio/spectrogram capture | Build-log media | Needed |

## Naming Convention

Place future images under `images/`:

```text
images/hero-family-lineup.jpg
images/horn-001-raw-blanks.jpg
images/cer-002-plaster-mold-open.jpg
images/cnc-002-routed-cavity-halves.jpg
images/val-001-closed-note-tuner.jpg
```

<div class="page-break"></div>

## risks.md

Project artifact.

# Risks

Generated: 2026-05-06

## Acoustic

### Acoustic: Helmholtz model overpredicts playable pitch

**Symptom:** The closed note or upper scale speaks flat/sharp even when the calculated cavity volume and tone-hole areas match the design sheet.

**Mechanism:** Gemshorn pitch depends on coupled fipple/window behavior, leakage, tone-hole chamfer, and effective neck length. The first-pass Helmholtz model is directionally useful but not a finished calibration.

**Test:** Build `GEM-SC-C5` first, measure fired water-fill volume, record the closed note and each opened-hole note at logged temperature, and compute cents error in `validation.csv`.

**Mitigation:** Update the design table with measured volume and empirical hole corrections before scaling to the full family. Keep holes flat/undersized before final tuning.

**Severity:** Medium.

### Acoustic: CNC wood seam leakage weakens fundamental

**Symptom:** The CNC-routed wood version sounds airy, unstable, or low in volume compared with ceramic/horn.

**Mechanism:** Split-blank construction creates a long glue seam around the cavity. Even tiny leaks reduce acoustic conductance control and can change the fipple response.

**Test:** Before final shaping, plug the window and tone holes, gently pressurize the cavity by mouth or bulb, and brush soapy water along the seam.

**Mitigation:** Add a continuous shallow gasket groove, use a thin even glue line, and seal the interior before final glue-up if the finish is mouth-safe after cure.

**Severity:** Medium.

## Structural

### Structural: Ceramic cracks around large low-register holes

**Symptom:** Bass/tenor bodies crack during drying, bisque, drilling, or tuning around H6/T1 or the tuning vent.

**Mechanism:** Large holes interrupt a curved ceramic shell and create stress concentration. Wall thickness and drying gradients matter more on the larger family members.

**Test:** Make a clay coupon with the largest bass hole and wall target. Dry and bisque it before committing to the full bass mold.

**Mitigation:** Add local boss thickness around large holes, drill greenware undersize, slow dry under loose cover, and tune after bisque with gradual reaming.

**Severity:** High. Human decision required before cutting a bass mold if coupon fails.

### Structural: Natural horn delaminates or cracks during cleaning

**Symptom:** A horn blank flakes, splits, or opens at the tip while being cleaned or drilled.

**Mechanism:** Horn is layered keratin. Heat, aggressive soaking, old dry material, or internal defects can delaminate the blank.

**Test:** Inspect with light through the wall, flex gently at the wide end, and clean one sacrificial blank before layout.

**Mitigation:** Buy multiple blanks, avoid boiling unless tested, keep the tip closed or permanently plug it, and reject thin/transparent wall sections near the voicing.

**Severity:** Medium.

## Ergonomic

### Ergonomic: Bass F body exceeds comfortable hand support

**Symptom:** The bass F is hard to hold, requires wrist extension, or pulls the mouthpiece angle downward.

**Mechanism:** The scaled bass body is long and wide enough that the instrument behaves like a small supported vessel rather than a hand flute.

**Test:** Make a cardboard or foam full-scale silhouette from `family-spec.csv` and check seated/lap, sling, and stand support positions.

**Mitigation:** Treat `GEM-SC-F3` as bench/lap/sling-supported, move holes for reach without assuming position strongly determines pitch, and add a support point to the design drawing.

**Severity:** Medium.

### Ergonomic: Sopranino holes are too small for reliable playing

**Symptom:** The sopranino F plays inconsistently because fingertips cannot seal tiny holes precisely.

**Mechanism:** Scaling reduces tone-hole diameters and spacing. Small holes are tuning-sensitive and are easily rounded by finish or reaming.

**Test:** Make a flat fingerboard coupon with final hole diameters and ask the intended player to cover holes without looking.

**Mitigation:** Keep the sopranino as an optional family member, use a slightly larger body scale if needed, or omit chromatic ambitions on that size.

**Severity:** Low.

## Supply

### Supply: Ethical horn blanks are inconsistent

**Symptom:** Purchased horn blanks differ too much in curve, wall, odor, core condition, or closed-tip geometry.

**Mechanism:** Natural horn is not an industrial material. Blank descriptions rarely specify internal volume or fipple-friendly wide-end geometry.

**Test:** Order several candidate blanks and log length, wide OD, wall, tip condition, water volume, and rejection reason in `horn-blank-spec.csv` notes.

**Mitigation:** Buy extras, tune each horn as a one-off, and keep the ceramic/CNC paths as repeatable alternatives.

**Severity:** Medium.

### Supply: Clay shrinkage data is missing or batch-specific

**Symptom:** Fired parts do not match master dimensions, and the family scale drifts.

**Mechanism:** Casting slip shrinkage varies by clay body, water content, mold age, drying, firing cone, and glaze schedule.

**Test:** Fire shrinkage bars with every clay batch and compare green, bone-dry, bisque, and glaze dimensions.

**Mitigation:** Update `gemshorn-design-table.xlsx` before master fabrication and keep masters editable until the clay body is locked.

**Severity:** High. Human decision required before production mold set if shrinkage is unmeasured.

## Fit/Finish

### Fit/Finish: Glaze or finish rounds the labium edge

**Symptom:** The instrument becomes breathy, slow to speak, or loses pitch stability after finishing.

**Mechanism:** The labium and windway need crisp, controlled edges. Glaze, oil, wax buildup, or sanding dust can change the edge and windway height.

**Test:** Photograph and measure the window before and after finish. Test-blow with the same temporary block before and after finishing.

**Mitigation:** Mask windway, labium, hole interiors, and block seats. Use exterior-only finish near the voicing and retouch the labium after firing/finish only with controlled tools.

**Severity:** High. Human decision required if the finish system cannot keep the voicing clean.

### Fit/Finish: Wood body glue line is visible or uncomfortable

**Symptom:** The routed wood body has a visible seam, rough mouth feel, or finish witness line along the body.

**Mechanism:** Split-body construction exposes a longitudinal seam and can leave mismatched grain or finish absorption.

**Test:** Make one finish coupon with the planned glue, seal coat, and final finish; inspect under raking light and touch around the mouth area.

**Mitigation:** Choose straight-grained matched halves, place seam away from lips/fingers where possible, scrape flush before finish, and use a mouth-safe topcoat.

**Severity:** Low.

<div class="page-break"></div>

## sources.md

Project artifact.

# Authenticity Notes

Generated: 2026-05-02

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

- [Horace Fitzpatrick, The Gemshorn: a Reconstruction](https://www.cambridge.org/core/journals/proceedings-of-the-royal-musical-association/article/gemshorn-a-reconstruction/0AD60F0FE7748111C8455FA2F4DD1CC3): Defines the gemshorn as a fipple instrument made from animal horn and calls out the stopped inverted cone bore. Used as the boundary-condition anchor.
- [Early Music Muse, The gemshorn: a short history](https://earlymusicmuse.com/gemshorn/): Summarizes the open-end fipple construction, four-hole historical evidence, and the 1455 clay gemshorn-like find. Used for authenticity notes.
- [Cincinnati Early Music, Medieval Gemshorn](https://cincinnatiearlymusic.com/gemshorn.html): Contrasts historical four-hole evidence with modern recorder-like reconstructions and consort families. Used to separate historical and modern lines.
- [Baltimore Recorders, Information about the Gemshorn](https://www.baltimorerecorders.org/gemshorns.html): Describes front holes, thumb hole, whistle/fipple, tuning ring, and the lack of an outlet other than whistle and fingerholes. Used for construction details.
- [Institut fuer Musikforschung Wuerzburg, Lo 29-31 Gemshoerner](https://www.musikwissenschaft.uni-wuerzburg.de/musikinstrumente/bestand/inventarliste/lo29-31-gemshoerner/): Gives measured modern HFK gemshorns in g, d1, and g1 and cautions that modern gemshorns are reconstruction products. Used as dimensional sanity check.

## Provenance Warning

No file in this packet claims to reproduce an extant original gemshorn exactly. The historical record is sparse; this packet gives a traceable and tunable workshop path with explicit assumptions.

<div class="page-break"></div>

## tuning-and-fingering.md

Project artifact.

# Tuning And Fingering

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

<div class="page-break"></div>

## validation-report.md

Project artifact.

# Validation Report

Generated: 2026-05-06

Verifier command:

```bash
python3 /mnt/c/Users/Tony/.codex/skills/instrument-maker-v4/scripts/validate_packet.py . --fix --json
```

Result: clean. No pass-1 findings and no fixes required.

## Clean Checks

- Tier 1 packet files are present: design, BOM, sourcing, cut list, validation, assembly manual, RFQ, drawing brief, visual BOM brief, Wolfram starter, risks, capstone deck, print packet, manifest, and README.
- Capstone deck has 15 slides, above the v4 verifier threshold.
- README is no longer a minimal scaffold and references an existing hero drawing.
- Referenced drawing files exist.
- `print-packet.pdf` exists.
- `capstone-deck.pptx` exists.
- CSVs load successfully.
- SVG drawings parse as XML.
- `gemshorn-design-table.xlsx` passes zip integrity checks.

## Fixed In v4 Verifier Loop

None. The final verifier pass reported no findings before applying fixes.

## Escalated

None from the packet verifier.

## Remaining Human Measurements

These are not verifier failures; they are shop measurements needed after first prototypes:

- Clay shrinkage by actual slip batch and firing schedule.
- Fired ceramic water-fill volume.
- Natural-horn blank measured volume and final hole diameters.
- CNC wood split-body leak test result.
- Measured Hz and cents error for each prototype.
