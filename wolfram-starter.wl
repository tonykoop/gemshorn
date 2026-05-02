(* Slip-Cast Gemshorn Family Wolfram Starter *)
(* Generated 2026-05-02. Paste into Wolfram Desktop or Cloud. *)

ClearAll["Global`*"];

speedOfSoundInPerS = 13549.0;
shrinkage = 0.12;

family = {
  <|"ID" -> "GEM-SC-F3", "Key" -> "F3", "MIDI" -> 53, "LengthIn" -> 27.7187, "VolumeIn3" -> 146.5677, "WindowAreaIn2" -> 0.54058, "WallIn" -> 0.2400|>,
  <|"ID" -> "GEM-SC-C4", "Key" -> "C4", "MIDI" -> 60, "LengthIn" -> 18.5000, "VolumeIn3" -> 39.6387, "WindowAreaIn2" -> 0.24080, "WallIn" -> 0.2040|>,
  <|"ID" -> "GEM-SC-F4", "Key" -> "F4", "MIDI" -> 65, "LengthIn" -> 13.8593, "VolumeIn3" -> 15.8811, "WindowAreaIn2" -> 0.13514, "WallIn" -> 0.1691|>,
  <|"ID" -> "GEM-SC-C5", "Key" -> "C5", "MIDI" -> 72, "LengthIn" -> 9.2500, "VolumeIn3" -> 4.3665, "WindowAreaIn2" -> 0.06020, "WallIn" -> 0.1300|>,
  <|"ID" -> "GEM-SC-F5", "Key" -> "F5", "MIDI" -> 77, "LengthIn" -> 6.9297, "VolumeIn3" -> 1.6964, "WindowAreaIn2" -> 0.03379, "WallIn" -> 0.1100|>
};

midiToFreq[m_] := 440*2^((m - 69)/12);
centsError[measured_, target_] := 1200*Log[2, measured/target];
holeLeff[diameter_, wall_] := wall + 0.85*(diameter/2);
conductance[diameter_, wall_] := Pi*(diameter/2)^2/holeLeff[diameter, wall];
helmholtzHz[conductanceTotal_, volumeIn3_] :=
  speedOfSoundInPerS/(2*Pi)*Sqrt[conductanceTotal/volumeIn3];

Dataset[family]

Manipulate[
 Module[{freq = midiToFreq[midi], scale, volume, windowArea, wall, windowLeff, gBase, predicted},
  scale = midiToFreq[72]/freq;
  wall = Min[0.24, Max[0.11, 0.13*scale^0.65]];
  windowArea = (0.43*scale)*(0.14*scale);
  windowLeff = wall + 0.85*Sqrt[windowArea/Pi];
  gBase = windowArea/windowLeff;
  volume = 4.366467*scale^3;
  predicted = helmholtzHz[gBase, volume];
  Column[{
    Row[{"Target Hz: ", NumberForm[freq, {6, 2}]}],
    Row[{"Predicted closed Hz: ", NumberForm[predicted, {6, 2}]}],
    Row[{"Cents error: ", NumberForm[centsError[predicted, freq], {6, 1}]}],
    Row[{"Scale factor: ", NumberForm[scale, {5, 3}]}],
    Row[{"Volume in3: ", NumberForm[volume, {7, 3}]}],
    Row[{"Window area in2: ", NumberForm[windowArea, {6, 4}]}]
  }]
 ],
 {{midi, 72, "Closed-note MIDI"}, 53, 77, 1}
]

(* Import validation.csv after prototypes exist:
validation = Import["validation.csv", "Dataset"];
*)
