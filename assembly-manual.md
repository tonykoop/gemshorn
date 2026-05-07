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
