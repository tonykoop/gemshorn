// Slip-Cast Gemshorn Family OpenSCAD Starter
// Generated 2026-05-02
// Units: inches. This is a master-shape starter, not final production CAD.

$fn = 64;

family = [
  ["GEM-SC-F3", 31.4985, 5.2781, 1.2259, 0.2727],
  ["GEM-SC-C4", 21.0227, 3.5227, 0.8182, 0.2318],
  ["GEM-SC-F4", 15.7493, 2.6391, 0.6129, 0.1921],
  ["GEM-SC-C5", 10.5114, 1.7614, 0.4091, 0.1477],
  ["GEM-SC-F5", 7.8746, 1.3195, 0.3065, 0.1250]
];

module horn_outer(len, wide_od, tip_od) {
  hull() {
    translate([0, 0, 0]) sphere(d=wide_od);
    translate([len*0.38, 0, len*0.12]) sphere(d=wide_od*0.70);
    translate([len*0.72, 0, len*0.17]) sphere(d=wide_od*0.43);
    translate([len, 0, len*0.18]) sphere(d=tip_od);
  }
}

module gemshorn_master(len, wide_od, tip_od, wall) {
  difference() {
    horn_outer(len, wide_od, tip_od);
    // Wide-end block seat and pour mouth.
    translate([-0.05, 0, 0]) rotate([0, 90, 0]) cylinder(h=wide_od*0.7, d=max(0.20, wide_od - 2*wall));
    // Voicing/window starter. Cut final labium and windway by hand or in detailed CAD.
    translate([wide_od*0.15, -wide_od*0.55, wide_od*0.18]) cube([wide_od*0.22, wide_od*1.1, wide_od*0.10], center=true);
  }
}

// Preview all masters side by side.
for (i = [0:len(family)-1]) {
  translate([0, i*7, 0])
    gemshorn_master(family[i][1], family[i][2], family[i][3], family[i][4]);
}
