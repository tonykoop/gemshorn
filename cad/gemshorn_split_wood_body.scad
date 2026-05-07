// CNC split-wood gemshorn body starter
// Generated 2026-05-06
// Units: inches. This is a concept/pre-CAM model, not verified toolpath geometry.

$fn = 64;

body_length = 10.511;        // C5 master-like envelope
wide_od = 1.761;
tip_od = 0.409;
wall = 0.150;
pin_d = 0.250;
pin_offset_y = 0.950;

module centerline_body(len=body_length, wide=wide_od, tip=tip_od) {
  hull() {
    translate([0, 0, 0]) sphere(d=wide);
    translate([len*0.38, 0, len*0.10]) sphere(d=wide*0.70);
    translate([len*0.72, 0, len*0.15]) sphere(d=wide*0.42);
    translate([len, 0, len*0.16]) sphere(d=tip);
  }
}

module split_half(show_cavity=true) {
  difference() {
    intersection() {
      centerline_body();
      translate([body_length/2, -2, -1.5]) cube([body_length+2, 2, 4], center=true);
    }
    if (show_cavity) {
      scale([(body_length-2*wall)/body_length, 1, 1])
        translate([wall, 0, 0])
          centerline_body(body_length-2*wall, wide_od-2*wall, max(0.08, tip_od-2*wall));
    }
    for (x=[1.0, body_length-1.0]) {
      translate([x, -pin_offset_y, 0]) rotate([90,0,0]) cylinder(d=pin_d, h=1.2, center=true);
    }
  }
}

translate([0, -0.08, 0]) split_half(true);
mirror([0,1,0]) translate([0, -0.08, 0]) split_half(true);
