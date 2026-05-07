# CNC / Manufacturing Setup Sheet

Generated: 2026-05-06

Packet: `/mnt/c/Users/Tony/Documents/GitHub/gemshorn`

Family: `vessel-flute`

This is a pre-CAM operation graph, not verified G-code. It covers three build methods: natural horn, slip-cast ceramic, and CNC-routed split wood.

## Assumptions

- Verify feeds, speeds, work envelope, hold-down, and tool clearance at the machine.
- Run air-cut or simulation before cutting instrument material.
- Tune every body empirically by measured volume, leak behavior, and hole opening.
- Use `GEM-SC-C5` as the first repeatable prototype unless historical horn authenticity is the sole goal.

## Operation Graph

### OP-010 - Review design package and choose build method

- Machine: bench.
- Inputs: `design.md`, `build-methods.md`, `family-spec.csv`.
- Output: selected prototype and build method.
- Check: validation rows exist for the selected path.

### OP-020 - Prepare natural horn blank

- Machine: bench / drill press.
- Tooling: fine saw, scraper, calipers, mild detergent.
- Datum: wide-end seating plane.
- Output: cleaned horn blank with measured volume.
- Release check: tip remains closed and the voicing wall is sound.

### OP-030 - Fabricate slip-cast master

- Machine: CNC router, 3D printer, or bench finishing.
- Tooling: 1/4 in ball end or print process, sealant, sandpaper.
- Input: `cad/gemshorn_family.scad`, `family-spec.csv`.
- Output: sealed scaled master.
- Release check: shrinkage scale applied, split line marked, no mold-trapping undercuts.

### OP-040 - Make plaster mold

- Machine: bench.
- Tooling: mold box, plaster, release, registration key tools.
- Output: two-part plaster mold.
- Release check: mold halves register and cast releases without tearing.

### OP-050 - Prepare CNC wood halves

- Machine: CNC router.
- Tooling: surfacing bit, 1/4 in upcut, 1/4 in dowel drill.
- Workholding: spoilboard clamps and dowel fixture.
- Output: faced halves with dowel registration.
- Release check: dowels are outside the acoustic cavity or hidden after shaping.

### OP-060 - Route CNC wood cavity halves

- Machine: CNC router.
- Tooling: 1/4 in ball end, optional 1/8 in ball end for detail.
- Input: `cad/gemshorn_split_wood_body.scad`, `cnc/wood-body-cnc-plan.md`.
- Output: mirrored routed cavity halves.
- Release check: minimum wall remains, cavity volume is estimated, and no tearout appears in the voicing zone.

### OP-070 - Dry-fit and leak test wood body

- Machine: bench.
- Tooling: dowel pins, low-pressure bulb, soapy water.
- Output: leak-tested dry assembly.
- Release check: no bubbles for two minutes before glue-up.

### OP-080 - Cast ceramic body

- Machine: bench / kiln.
- Tooling: casting slip, plaster mold, drill bits, kiln.
- Output: bisque test body.
- Release check: shrinkage, wall, cracks, and volume recorded.

### OP-090 - Fipple block and voicing

- Machine: bench.
- Tooling: chisels, knife, files, feeler gauges.
- Output: speaking instrument.
- Release check: windway is even, labium is crisp, and closed note speaks.

### OP-100 - Tone-hole drilling and tuning

- Machine: bench / drill press.
- Tooling: undersize bits, tapered reamers, tuner, wax.
- Output: tuned scale pass.
- Release check: holes opened low to high and cents error logged.

### OP-900 - Final validation and documentation

- Machine: bench.
- Tooling: tuner, microphone, calipers, thermometer, camera.
- Output: updated `validation.csv`, photos, and build notes.
- Release check: measured Hz, cents error, temperature, and build method recorded.

## Final Release Checks

- [ ] Every method has a material-specific risk entry in `risks.md`.
- [ ] Every CNC operation has datum, workholding, tool, input, output, and check.
- [ ] All tuning-critical holes start undersize.
- [ ] Ceramic bodies have shrinkage-bar data before production molds.
- [ ] Wood bodies pass the leak test before exterior shaping.
- [ ] Natural horn blanks are documented as one-off tuned instruments.
