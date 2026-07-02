# Design Intent — gemshorn rev A

- Master CAD: `cad/gemshorn_family.scad` (sha256: 3e44b4512fa53c2f4b269b9f4acf376a463cc325ed00b7db3be1859a602b5fad) with CNC split-wood variant `cad/gemshorn_split_wood_body.scad` (sha256: 8c15bf96ff18e572031fd1db3fbd55b948c6880186c8065aae35abfa2fd0eb47), driven by `gemshorn-design-table.xlsx` (sha256: d433076e905ae23f0d28698743f3ea13379f254da5a784da288bae011168262b)
- Function: Closed horn-shaped vessel (Helmholtz duct-flute). Sealed pointed tip, wide end carries the fipple/block and labium window; pitch is governed by chamber volume, window/vent conductance, and opened tone-hole area — NOT an open-open bore. Modern slip-cast consort (F/C sizes, seven front holes + thumb vent) plus a historically informed 4-front+thumb archetype in natural horn or clay.
- Environment: hand/lap/sling-played wind instrument; ceramic bodies are shrinkage- and glaze-sensitive; CNC split-wood bodies carry a long glue seam that must be leak-sealed. Final pitch is empirical (fipple/window/leak dominate the last cents).
- Target qty: 1 (prototype — GEM-SC-C5 soprano pilot first). Deadline: TBD. Budget/unit ceiling: TBD.

## Critical dimensions (carry tolerances)

| Feature | Nominal | Tolerance | Why critical | Source |
| --- | --- | --- | --- | --- |
| Soprano C5 master centerline length | 10.5114 in | fired 9.25 in target after shrinkage | sets acoustic family scaling baseline | family-spec.csv GEM-SC-C5 (measurement_required) |
| Soprano C5 fired internal volume | 71.55 ml (4.3665 in³) | water-fill check on fired body | Helmholtz cavity governs fundamental | family-spec.csv GEM-SC-C5 (measurement_required) |
| Window width × height (C5) | 0.43 × 0.14 in | voicing is empirical; do not finalize from table | window vent conductance / speaking | family-spec.csv GEM-SC-C5 (measurement_required) |
| Wall thickness (C5) | 0.13 in fired | drying/leak/crack gate | shell strength + acoustic sealing | family-spec.csv GEM-SC-C5 (measurement_required) |
| Tone-hole radius (per note) | r = (0.85·G + √((0.85·G)²+4π·G·wall))/(2π) | slots undersized before empirical tuning | incremental conductance sets scale pitches | design.md acoustic model |
| Fundamental target (C5 pilot) | 523.2511 Hz | ±cents logged in validation.csv | tuning correctness | family-spec.csv GEM-SC-C5 |

## Incidental (free for DFM)

- Horn outer curvature styling, tip cosmetic profile, surface finish/glaze color, non-mating exterior contour, sling/support hardware.

## Must-nots (DFM may never violate)

- Window/fipple/labium geometry is tuning-sensitive: never freeze voicing dimensions from the table or a lossy mesh export — refine by hand and log in validation.csv (design.md / risks.md).
- Do not scale to bass/tenor before measured fired water-fill volume + empirical hole corrections from the GEM-SC-C5 pilot are in validation.csv (risks.md Acoustic).
- Keep tone holes flat/undersized before final empirical tuning (risks.md).
- CNC split-wood: do not glue up before a continuous gasket groove + interior seal plan; leak-test the seam (risks.md Acoustic — seam leakage).
- Large low-register holes in ceramic: prove a coupon (largest bass hole + wall target) through bisque before committing the bass mold (risks.md Structural).

## Material intent

- Preferred: slip-cast ceramic (repeatable production family); natural horn for the historical archetype; CNC-routed split hardwood for fast prototype/teaching (per bom.csv / material-options.md).
- Acceptable subs: per sourcing.csv and material-options.md (spec-first; live prices unverified; mouth-safe finishes only).
- Forbidden: non-mouth-safe interior finishes on played bodies (material-options.md safety gate).

## Stage status

Stage 0 intake complete 2026-07-01. Gate A (Alpha shop compile) NOT yet run — no concessions logged, nothing presented as shippable. Fabrication authority remains measurement-gated.
