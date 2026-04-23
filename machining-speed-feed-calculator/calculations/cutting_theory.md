# Cutting Theory — Speed, Feed & Tool Life

## 1. Cutting Speed to RPM

RPM is derived from the desired surface cutting speed and the workpiece/tool diameter:

```
N (rpm) = (V × 1000) / (π × D)
```

Where:
- V = cutting speed [m/min]
- D = diameter [mm]
- N = spindle speed [rpm]

**Example:** 6061-T6 Al, coated carbide, OD turning, Ø50mm workpiece
- V = 305 m/min (from Sandvik Coromant catalog)
- N = (305 × 1000) / (π × 50) = **1,943 rpm**

---

## 2. Feed Rate

For turning (feed per revolution):
```
Vf = N × fn
```

For milling (feed per tooth):
```
Vf = N × fz × z
```

Where:
- fn = feed per revolution [mm/rev]
- fz = feed per tooth [mm/tooth]
- z = number of teeth/flutes
- Vf = feed rate [mm/min]

**Example:** N = 1,943 rpm, fn = 0.25 mm/rev
- Vf = 1,943 × 0.25 = **486 mm/min**

---

## 3. Material Removal Rate (MRR)

```
MRR = Vf × ap × ae   [mm³/min]
```

Where:
- Vf = feed rate [mm/min]
- ap = depth of cut (axial) [mm]
- ae = width of cut (radial) [mm]

For OD turning: ae = workpiece diameter
For end milling: ae = radial engagement (typically 50–75% of cutter diameter)

**Example:** Vf = 486 mm/min, ap = 2.0 mm, ae = 50mm
- MRR = 486 × 2.0 × 50 = **48,600 mm³/min**

---

## 4. Taylor's Tool Life Equation

Frederick Winslow Taylor (1907) developed the empirical relationship between cutting speed and tool life:

```
V × Tⁿ = C
```

Or equivalently:
```
T = (C / V)^(1/n)
```

Where:
- V = cutting speed [m/min]
- T = tool life [min] (to defined failure criterion, typically 0.3mm flank wear)
- n = Taylor exponent (material/tool dependent, typically 0.1–0.4)
- C = Taylor constant (speed at T = 1 min)

**Typical Taylor exponents:**
| Tool Material | n value |
|---|---|
| HSS | 0.08–0.15 |
| Uncoated Carbide | 0.20–0.28 |
| Coated Carbide | 0.23–0.32 |
| Ceramic | 0.35–0.45 |

**Example:** 4140 Steel, TiAlN carbide: n = 0.23, C = 2200
- At V = 150 m/min: T = (2200/150)^(1/0.23) = (14.67)^4.35 = **42 min**
- At V = 200 m/min: T = (2200/200)^(1/0.23) = (11.00)^4.35 = **14 min**

A 33% speed increase cuts tool life by ~67%.

---

## 5. Specific Cutting Force and Power

Cutting power can be estimated from specific cutting force (kc):

```
Pc = (Vf × ap × ae × kc) / (60 × 10⁶)   [kW]
```

Typical kc values [N/mm²]:
- Aluminum: 700–900
- Low carbon steel: 1,400–1,800  
- Alloy steel: 2,000–2,600
- Stainless steel: 2,200–2,800
- Ti alloy: 3,000–3,500
