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
