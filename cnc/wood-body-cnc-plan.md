# CNC Router Wood Body Plan

Generated: 2026-05-06

This plan adds a modern split-wood gemshorn build path. It is a pre-CAM setup plan, not verified G-code.

## Target

- First wood prototype: `GEM-SC-C5` soprano C or `GEM-HIST-G4` historical pilot.
- Construction: two routed wood halves, registered with dowel pins, glued into a closed vessel body.
- Acoustic model: same Helmholtz schedule as the ceramic/horn packet; tune by measured volume and hole opening.

## Stock

| Size | Recommended Stock | Notes |
| --- | --- | --- |
| Soprano C | Two blanks, 12.5 x 2.5 x 1.0 in each | Start here |
| Historical G4 | Two blanks, 15.5 x 3.0 x 1.1 in each | Good authenticity comparison |
| Alto F | Two blanks, 18.0 x 3.5 x 1.25 in each | Check CNC travel and clamp clearance |

Use maple, cherry, pear, beech, or boxwood. Avoid oily/open-pore woods near the mouth unless the finish is proven safe.

## Datums

- Datum A: labium/window lower edge at wide end.
- Datum B: routed centerline curve.
- Datum C: split plane mating surface.
- Datum D: dowel-pin axis pair.

## Operation Summary

1. Joint and plane both halves.
2. CNC face skim mating surface.
3. Drill 1/4 in dowel registration holes outside the body outline.
4. Route internal half-cavity with 1/4 in ball end or 1/8 in ball end for small sizes.
5. Engrave tone-hole and window pilot marks.
6. Dry-fit with dowels and leak-test the cavity.
7. Glue body halves.
8. CNC or bandsaw exterior profile, leaving sanding allowance.
9. Hand-cut/final-fit fipple block, windway, window, and labium.
10. Drill holes undersize and tune.

## Tooling

| Tool | Use | Notes |
| --- | --- | --- |
| 1/4 in upcut spiral | Registration holes and rough pockets | Use conservative depth of cut |
| 1/4 in ball end | Internal cavity rough/finish on C5 and larger | Check scallop height |
| 1/8 in ball end | Small body detail and pilot dimples | Use for F5 and fine hole marks |
| 60 deg V-bit | Datum labels and centerline engraving | Optional |
| Flush trim/sanding tools | Exterior cleanup | Keep labium area crisp |

## Release Checks

- [ ] CAM model includes actual wood body wall thickness, not ceramic wall assumptions.
- [ ] Dowel holes are outside the final body or intentionally hidden.
- [ ] Workholding does not cover the routed cavity or final outline.
- [ ] Glue squeeze-out cannot enter the windway/window area.
- [ ] Cavity leak test passes before exterior shaping.
- [ ] Finished body receives measured volume and tuning rows in `validation.csv`.
