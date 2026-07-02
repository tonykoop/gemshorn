# MCP / External-Tool Session Log

V5 provenance record for artifacts generated or modified by external tools.
Required before claiming any artifact came from OpenSCAD, Blender, Illustrator,
Photoshop, Fusion, SketchUp, or similar tooling.

| session_id | tool | input_authority | outputs | role | authority_result | review_status | notes |
|---|---|---|---|---|---|---|---|
| fable-v5-refresh-2026-07-01 | claude-code (Fable 5) | gemshorn-design-table.xlsx | gemshorn-design-table.xlsx, bom.csv, sourcing.csv, cut-list.csv, validation.csv, family-spec.csv | packet_refresh | fabrication | self_checked | V5 refresh pass; tabular packet data reviewed against design table. No dimension changes made. Provenance rows added to satisfy V5 fabrication-artifact logging. |
| fable-v5-refresh-2026-07-01 | claude-code (Fable 5) + OpenSCAD CLI | gemshorn-design-table.xlsx | cad/gemshorn_family.scad | cad_authoring | pending_measurement | self_checked | Existing parametric slip-cast family master-shape starter (kept, not rewritten). Authority pending measured shrinkage/volume/leak/fipple validation. openscad render check: pass (openscad -o STL, exit 0). |
| fable-v5-refresh-2026-07-01 | claude-code (Fable 5) + OpenSCAD CLI | gemshorn-design-table.xlsx | cad/gemshorn_split_wood_body.scad | cad_authoring | pending_measurement | self_checked | Existing CNC split-wood prototype master-shape starter (kept, not rewritten). openscad render check: pass (openscad -o STL, exit 0; top-level object empty — components are module-scoped, pre-existing). |
| fable-v5-refresh-2026-07-01 | claude-code (Fable 5) | gemshorn-design-table.xlsx | wolfram/gemshorn-wolfram-model.wl | analysis_source | derived_preview | unreviewed | Existing Wolfram model package; source-only (not executed). L2 evidence. |
