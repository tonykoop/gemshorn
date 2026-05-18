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

Visual authority is tracked in `visual-output-register.csv`. SVG review plates,
site previews, print-packet images, and future generated concept images are not
fabrication authority unless they are derived from the named design table, CAD,
DXF, measured template, or reviewed drawing authority.
