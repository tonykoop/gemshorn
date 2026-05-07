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
