(* instrument-maker-v4.2 Wolfram packet source *)
ClearAll["Global`*"];

packetDir = "/mnt/c/Users/Tony/Documents/GitHub/gemshorn";
metadata = <|
  "PacketName" -> "Slip-Cast Gemshorn Family Build Packet",
  "PacketPath" -> ".",
  "GeneratedOn" -> "2026-05-06",
  "Model" -> "Helmholtz",
  "HasFamilySpec" -> True,
  "HasValidation" -> True,
  "HasCncPlan" -> True
|>;

familySpecPath = FileNameJoin[{packetDir, "family-spec.csv"}];
validationPath = FileNameJoin[{packetDir, "validation.csv"}];
cncPlanPath = FileNameJoin[{packetDir, "cnc", "cnc-plan.json"}];

familySpec = If[FileExistsQ[familySpecPath],
  Import[familySpecPath, "Dataset"],
  Dataset[ImportString["[{\"id\": \"GEM-SC-F3\", \"name\": \"Bass F\", \"key\": \"F3\", \"midi\": \"53\", \"freq_hz\": \"174.6141\", \"scale\": \"2.9966\", \"line\": \"modern slip-cast consort\", \"fired_centerline_length_in\": \"27.7187\", \"master_centerline_length_in\": \"31.4985\", \"fired_wide_od_in\": \"4.6448\", \"master_wide_od_in\": \"5.2781\", \"fired_tip_od_in\": \"1.0788\", \"fired_wall_in\": \"0.24\", \"fired_wide_id_in\": \"4.1648\", \"fired_tip_id_in\": \"0.5988\", \"fired_internal_volume_in3\": \"146.5677\", \"fired_internal_volume_ml\": \"2401.8139\", \"window_width_in\": \"1.2885\", \"window_height_in\": \"0.4195\", \"windway_height_in\": \"0.0589\", \"labium_setback_in\": \"1.2885\", \"playing_support\": \"bench, lap, or simple sling; large horn\"}, {\"id\": \"GEM-SC-C4\", \"name\": \"Tenor C\", \"key\": \"C4\", \"midi\": \"60\", \"freq_hz\": \"261.6256\", \"scale\": \"2.0\", \"line\": \"modern slip-cast consort\", \"fired_centerline_length_in\": \"18.5\", \"master_centerline_length_in\": \"21.0227\", \"fired_wide_od_in\": \"3.1\", \"master_wide_od_in\": \"3.5227\", \"fired_tip_od_in\": \"0.72\", \"fired_wall_in\": \"0.204\", \"fired_wide_id_in\": \"2.692\", \"fired_tip_id_in\": \"0.312\", \"fired_internal_volume_in3\": \"39.6387\", \"fired_internal_volume_ml\": \"649.5624\", \"window_width_in\": \"0.86\", \"window_height_in\": \"0.28\", \"windway_height_in\": \"0.0481\", \"labium_setback_in\": \"0.86\", \"playing_support\": \"two-hand standing or seated\"}, {\"id\": \"GEM-SC-F4\", \"name\": \"Alto F\", \"key\": \"F4\", \"midi\": \"65\", \"freq_hz\": \"349.2282\", \"scale\": \"1.4983\", \"line\": \"modern slip-cast consort\", \"fired_centerline_length_in\": \"13.8593\", \"master_centerline_length_in\": \"15.7493\", \"fired_wide_od_in\": \"2.3224\", \"master_wide_od_in\": \"2.6391\", \"fired_tip_od_in\": \"0.5394\", \"fired_wall_in\": \"0.1691\", \"fired_wide_id_in\": \"1.9842\", \"fired_tip_id_in\": \"0.2012\", \"fired_internal_volume_in3\": \"15.8811\", \"fired_internal_volume_ml\": \"260.245\", \"window_width_in\": \"0.6443\", \"window_height_in\": \"0.2098\", \"windway_height_in\": \"0.0416\", \"labium_setback_in\": \"0.6443\", \"playing_support\": \"comfortable hand instrument\"}, {\"id\": \"GEM-SC-C5\", \"name\": \"Soprano C\", \"key\": \"C5\", \"midi\": \"72\", \"freq_hz\": \"523.2511\", \"scale\": \"1.0\", \"line\": \"modern slip-cast consort baseline\", \"fired_centerline_length_in\": \"9.25\", \"master_centerline_length_in\": \"10.5114\", \"fired_wide_od_in\": \"1.55\", \"master_wide_od_in\": \"1.7614\", \"fired_tip_od_in\": \"0.36\", \"fired_wall_in\": \"0.13\", \"fired_wide_id_in\": \"1.29\", \"fired_tip_id_in\": \"0.1\", \"fired_internal_volume_in3\": \"4.3665\", \"fired_internal_volume_ml\": \"71.5536\", \"window_width_in\": \"0.43\", \"window_height_in\": \"0.14\", \"windway_height_in\": \"0.034\", \"labium_setback_in\": \"0.43\", \"playing_support\": \"primary pilot size\"}, {\"id\": \"GEM-SC-F5\", \"name\": \"Sopranino F\", \"key\": \"F5\", \"midi\": \"77\", \"freq_hz\": \"698.4565\", \"scale\": \"0.7492\", \"line\": \"modern slip-cast consort\", \"fired_centerline_length_in\": \"6.9297\", \"master_centerline_length_in\": \"7.8746\", \"fired_wide_od_in\": \"1.1612\", \"master_wide_od_in\": \"1.3195\", \"fired_tip_od_in\": \"0.2697\", \"fired_wall_in\": \"0.11\", \"fired_wide_id_in\": \"0.9412\", \"fired_tip_id_in\": \"0.0497\", \"fired_internal_volume_in3\": \"1.6964\", \"fired_internal_volume_ml\": \"27.799\", \"window_width_in\": \"0.3221\", \"window_height_in\": \"0.1049\", \"windway_height_in\": \"0.0294\", \"labium_setback_in\": \"0.3221\", \"playing_support\": \"small hand instrument; hole accuracy is critical\"}, {\"id\": \"GEM-HIST-G4\", \"name\": \"Historical Clay/Horn Archetype\", \"key\": \"G4\", \"midi\": \"67\", \"freq_hz\": \"391.9954\", \"scale\": \"1.3348\", \"line\": \"historically informed 4 front plus thumb study\", \"fired_centerline_length_in\": \"12.3473\", \"master_centerline_length_in\": \"14.031\", \"fired_wide_od_in\": \"2.069\", \"master_wide_od_in\": \"2.3511\", \"fired_tip_od_in\": \"0.4805\", \"fired_wall_in\": \"0.1568\", \"fired_wide_id_in\": \"1.7553\", \"fired_tip_id_in\": \"0.1669\", \"fired_internal_volume_in3\": \"10.9964\", \"fired_internal_volume_ml\": \"180.1994\", \"window_width_in\": \"0.574\", \"window_height_in\": \"0.1869\", \"windway_height_in\": \"0.0393\", \"labium_setback_in\": \"0.574\", \"playing_support\": \"small hand instrument; exact historical pitch is not known\"}]", "JSON"]]
];

validationData = If[FileExistsQ[validationPath],
  Import[validationPath, "Dataset"],
  Dataset[ImportString["[{\"instrument_id\": \"GEM-SC-F3\", \"check\": \"closed tonic frequency\", \"target\": \"174.61 Hz\", \"measured\": \"\", \"tolerance\": \"+/-15 cents prototype\", \"environment\": \"record temp F, humidity\", \"result\": \"\", \"action\": \"adjust cavity/window/vent before hole tuning\", \"measured_hz\": \"\", \"cents_error\": \"\", \"tuner\": \"\", \"measurement_date\": \"\"}, {\"instrument_id\": \"GEM-SC-F3\", \"check\": \"fired centerline length\", \"target\": \"27.719 in\", \"measured\": \"\", \"tolerance\": \"+/-0.060 in\", \"environment\": \"after glaze if glazed\", \"result\": \"\", \"action\": \"update shrinkage factor if systematic\", \"measured_hz\": \"\", \"cents_error\": \"\", \"tuner\": \"\", \"measurement_date\": \"\"}, {\"instrument_id\": \"GEM-SC-F3\", \"check\": \"fired internal volume\", \"target\": \"2402 ml\", \"measured\": \"\", \"tolerance\": \"+/-5%\", \"environment\": \"water-fill, dry after\", \"result\": \"\", \"action\": \"retune window/vent model\", \"measured_hz\": \"\", \"cents_error\": \"\", \"tuner\": \"\", \"measurement_date\": \"\"}, {\"instrument_id\": \"GEM-SC-C4\", \"check\": \"closed tonic frequency\", \"target\": \"261.63 Hz\", \"measured\": \"\", \"tolerance\": \"+/-15 cents prototype\", \"environment\": \"record temp F, humidity\", \"result\": \"\", \"action\": \"adjust cavity/window/vent before hole tuning\", \"measured_hz\": \"\", \"cents_error\": \"\", \"tuner\": \"\", \"measurement_date\": \"\"}, {\"instrument_id\": \"GEM-SC-C4\", \"check\": \"fired centerline length\", \"target\": \"18.500 in\", \"measured\": \"\", \"tolerance\": \"+/-0.060 in\", \"environment\": \"after glaze if glazed\", \"result\": \"\", \"action\": \"update shrinkage factor if systematic\", \"measured_hz\": \"\", \"cents_error\": \"\", \"tuner\": \"\", \"measurement_date\": \"\"}, {\"instrument_id\": \"GEM-SC-C4\", \"check\": \"fired internal volume\", \"target\": \"650 ml\", \"measured\": \"\", \"tolerance\": \"+/-5%\", \"environment\": \"water-fill, dry after\", \"result\": \"\", \"action\": \"retune window/vent model\", \"measured_hz\": \"\", \"cents_error\": \"\", \"tuner\": \"\", \"measurement_date\": \"\"}, {\"instrument_id\": \"GEM-SC-F4\", \"check\": \"closed tonic frequency\", \"target\": \"349.23 Hz\", \"measured\": \"\", \"tolerance\": \"+/-15 cents prototype\", \"environment\": \"record temp F, humidity\", \"result\": \"\", \"action\": \"adjust cavity/window/vent before hole tuning\", \"measured_hz\": \"\", \"cents_error\": \"\", \"tuner\": \"\", \"measurement_date\": \"\"}, {\"instrument_id\": \"GEM-SC-F4\", \"check\": \"fired centerline length\", \"target\": \"13.859 in\", \"measured\": \"\", \"tolerance\": \"+/-0.060 in\", \"environment\": \"after glaze if glazed\", \"result\": \"\", \"action\": \"update shrinkage factor if systematic\", \"measured_hz\": \"\", \"cents_error\": \"\", \"tuner\": \"\", \"measurement_date\": \"\"}]", "JSON"]]
];

frequencyFromMidi[midi_, a4_: 440] := a4*2^((midi - 69)/12);
centsError[measured_, target_] := 1200*Log[2, measured/target];
openPipeLengthIn[freq_, c_: 13552, radius_: 0] := c/(2*freq) - 2*0.6*radius;
stoppedPipeLengthIn[freq_, c_: 13552, radius_: 0] := c/(4*freq) - 0.6*radius;
helmholtzFrequency[area_, volume_, leff_, c_: 13552] :=
  (c/(2*Pi))*Sqrt[area/(volume*leff)];
cantileverFrequency[k_, thickness_, length_] := k*thickness/length^2;
stringFrequency[length_, tension_, linearDensity_] :=
  1/(2*length)*Sqrt[tension/linearDensity];

modelExplorer = Switch[metadata["Model"],
  "Helmholtz",
    Manipulate[
      helmholtzFrequency[portArea, chamberVolume, effectiveLength],
      {{portArea, 0.4, "port area (in^2)"}, 0.05, 4},
      {{chamberVolume, 40, "volume (in^3)"}, 5, 400},
      {{effectiveLength, 0.6, "effective length (in)"}, 0.05, 3}
    ],
  "OpenPipe",
    Manipulate[
      openPipeLengthIn[f, 13552, radius],
      {{f, 440, "target Hz"}, 80, 1200},
      {{radius, 0.375, "bore radius (in)"}, 0, 1.5}
    ],
  "StoppedPipe",
    Manipulate[
      stoppedPipeLengthIn[f, 13552, radius],
      {{f, 220, "target Hz"}, 40, 1000},
      {{radius, 0.375, "bore radius (in)"}, 0, 1.5}
    ],
  "CantileverBeam",
    Manipulate[
      cantileverFrequency[k, thickness, length],
      {{k, 24000, "K constant"}, 1000, 80000},
      {{thickness, 0.25, "thickness (in)"}, 0.05, 1},
      {{length, 4.5, "length (in)"}, 0.5, 24}
    ],
  _,
    Manipulate[
      frequencyFromMidi[midi],
      {{midi, 69, "MIDI note"}, 24, 96, 1}
    ]
];

audioPreview[f_: 440, seconds_: 1.5] :=
  AudioNormalize[
    AudioAdd[
      AudioGenerator[{"Sin", f}, seconds],
      .35 AudioGenerator[{"Sin", 2 f}, seconds],
      .18 AudioGenerator[{"Sin", 3 f}, seconds]
    ]
  ];

validationRows = Normal[validationData];
validationPlot = Quiet@Check[
  ListPlot[
    DeleteMissing[
      ToExpression /@ Lookup[validationRows, "Cents Error", Missing[]]
    ],
    PlotTheme -> "Scientific",
    Frame -> True,
    FrameLabel -> {{"Cents error", None}, {"Measurement row", metadata["PacketName"]}}
  ],
  "No numeric validation cents-error values yet."
];

packetNotebook[] := CreateDocument[
  {
    TextCell[metadata["PacketName"], "Title"],
    TextCell["instrument-maker v4.2 computational packet", "Subtitle"],
    TextCell["Metadata", "Section"],
    ExpressionCell[metadata, "Input"],
    TextCell["Family/design data", "Section"],
    ExpressionCell[familySpec, "Input"],
    TextCell["Model explorer", "Section"],
    ExpressionCell[modelExplorer, "Input"],
    TextCell["Audio preview", "Section"],
    ExpressionCell[audioPreview[440], "Input"],
    TextCell["Validation", "Section"],
    ExpressionCell[validationPlot, "Input"]
  },
  WindowTitle -> metadata["PacketName"]
];

packetNotebook[];
