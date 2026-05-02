# Tuning And Fingering

## Modern Slip-Cast Consort

Hole names run from the distal/lower front hand toward the mouth:

```text
T1 on back behind H7

Mouth / fipple
H7 H6 H5 H4 H3 H2 H1
Tip closed
```

First-pass diatonic opening sequence:

| Sounding note above tonic | Fingering idea |
| --- | --- |
| 0 semitones | all holes closed |
| +2 | open H1 |
| +4 | open H1-H2 |
| +5 | open H1-H3 |
| +7 | open H1-H4 |
| +9 | open H1-H5 |
| +11 | open H1-H6 |
| +12 | open H1-H7 |
| +14 | open H1-H7 plus T1 |

Chromatic notes are by half-holing, cross-fingering, removable wax, or a rotating tuning ring. Treat the chart as a tuning scaffold, not a final published fingering chart.

## Historical Archetype

Use the `hole-schedule-historical.csv` pilot. Build it with waxable holes and tune by ear/tuner:

| Sounding note above tonic | Fingering idea |
| --- | --- |
| 0 semitones | all holes closed |
| +2 | open F1 |
| +4 | open F1-F2 |
| +5 | open F1-F3, optional |
| +7 | open F1-F4 |
| +12 | open front holes plus T1/back vent |

The strict historical version should be documented as "limited range, four-hole evidence, exact pitch unknown." The practical consort should be documented as "modern reconstruction."

## Tuning Order

1. Tune closed tonic by cavity volume, window area, and any tuning vent.
2. Tune H1, then H2, working upward.
3. Tune the octave hole after the lower scale speaks reliably.
4. Tune T1 last. It doubles as high note, thumb vent, or pitch control.
5. Leave small holes slightly flat before glaze fire, then do final opening after glaze if needed.

## Cents Formula

```text
cents = 1200 * log2(measured_frequency / target_frequency)
```

Keep final production tolerance to +/-15 cents for first playable prototypes and tighten to +/-8 cents after shrinkage and voicing data are stable.
