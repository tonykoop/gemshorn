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

## Round 30 V5 Explorer Readiness Check

Additional validation run on 2026-05-18:

```bash
jq . capstone-manifest.json
test -f explorer.html
git diff --check
python3 /home/tony/.codex/skills/instrument-maker/scripts/validate_visual_authority.py visual-output-register.csv
python3 /home/tony/.codex/skills/instrument-maker/scripts/validate_acoustic_law.py family-spec.csv
```

Result: clean. The visual register validates with 11 checked rows and no
warnings. The acoustic-law validator checks all 6 family-spec rows and reports
no warnings. The acoustic-law entries intentionally use `empirical_only` with
`governing_model=helmholtz_vessel_flute` because this gemshorn packet is a
closed vessel / duct-flute system whose production dimensions remain
measurement-gated.
