# Machining Speed & Feed Calculator

A Python tool that recommends optimal cutting speed, feed rate, depth of cut, and estimated cycle time for CNC turning and milling operations. Covers 12 common workpiece materials and 4 tool material types.

## Features
- Supports turning (OD, facing, boring) and milling (end mill, face mill, slot) operations
- 12 workpiece materials: steels, aluminums, stainless, cast iron, plastics, titanium
- 4 cutting tool types: HSS, uncoated carbide, coated carbide (TiAlN), ceramic
- Calculates: cutting speed (SFM/m·min⁻¹), RPM, feed rate (IPM/mm·min⁻¹), MRR, cycle time estimate
- Built-in Taylor's tool life equation for recommended tool change interval
- Outputs formatted report + optional CSV log

## Quick Start
```bash
python code/speed_feed_calc.py
```

## Example Output
```
══════════════════════════════════════════════════════
  MACHINING SPEED & FEED CALCULATOR
══════════════════════════════════════════════════════
  Operation  : Turning (OD)
  Material   : 6061-T6 Aluminum
  Tool       : Coated Carbide (TiAlN)
  Diameter   : 50.00 mm
──────────────────────────────────────────────────────
  Cutting Speed  :  305 m/min  (1000 SFM)
  RPM            : 1943 rpm
  Feed/rev       :  0.25 mm/rev
  Feed Rate      :  486 mm/min
  Depth of Cut   :  2.0 mm (recommended)
  MRR            :  2430 mm³/min
  Est. Tool Life :  45 min at this speed
══════════════════════════════════════════════════════
```

## Repository Structure
```
machining-speed-feed-calculator/
├── code/
│   ├── speed_feed_calc.py       # Main calculator
│   └── cutting_data.py          # Speed/feed database
├── calculations/
│   ├── cutting_theory.md        # Taylor's equation, MRR derivations
│   └── worked_examples.py       # Step-by-step example runs
├── bom/
│   ├── BOM.md
│   └── bom.csv
├── docs/
│   ├── operation_guide.md
│   └── tool_selection_guide.md
├── issues/
│   └── ISSUES_LOG.md
├── results/
│   └── RESULTS.md
└── tests/
    └── test_calculations.py
```

## Supported Materials & Operations

**Workpiece Materials:** 1018 Steel, 4140 Steel, 304 SS, Cast Iron (Class 30), 6061-T6 Al, 7075-T6 Al, C360 Brass, Nylon 66, ABS, Polycarbonate, Grade 5 Titanium, Inconel 718

**Operations:** OD Turning, Facing, Boring, End Milling, Face Milling, Slot Milling

**Tool Materials:** HSS, Uncoated Carbide (C2), Coated Carbide (TiAlN), Ceramic

## Author
Prabdeep Singh Ghatora | [github.com/prabdeepg](https://github.com/prabdeepg)
