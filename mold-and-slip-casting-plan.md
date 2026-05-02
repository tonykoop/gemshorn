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
