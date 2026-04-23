"""
Worked calculation examples for machining parameters.
Demonstrates manual calculations that match speed_feed_calc.py output.
"""
import math

print("=" * 60)
print("WORKED EXAMPLE 1: 6061-T6 OD Turning")
print("=" * 60)

# Inputs
V_mpm   = 305       # cutting speed m/min (Sandvik Coromant catalog)
D_mm    = 50        # workpiece diameter mm
fn      = 0.25      # feed per revolution mm/rev
ap      = 2.0       # depth of cut mm (roughing)
ae      = D_mm      # for OD turning, width = diameter

# Step 1: RPM
N = (V_mpm * 1000) / (math.pi * D_mm)
print(f"\nStep 1 — RPM")
print(f"  N = (V × 1000) / (π × D)")
print(f"  N = ({V_mpm} × 1000) / (π × {D_mm})")
print(f"  N = {N:.1f} rpm")

# Step 2: Feed rate
Vf = N * fn
print(f"\nStep 2 — Feed Rate")
print(f"  Vf = N × fn = {N:.1f} × {fn} = {Vf:.1f} mm/min")

# Step 3: MRR
MRR = Vf * ap * ae
print(f"\nStep 3 — MRR")
print(f"  MRR = Vf × ap × ae = {Vf:.1f} × {ap} × {ae} = {MRR:.0f} mm³/min")

# Step 4: Taylor tool life
n_taylor, C = 0.30, 4500
T = (C / V_mpm) ** (1/n_taylor)
print(f"\nStep 4 — Taylor Tool Life (n={n_taylor}, C={C})")
print(f"  T = (C/V)^(1/n) = ({C}/{V_mpm})^(1/{n_taylor}) = {T:.1f} min")

print()
print("=" * 60)
print("WORKED EXAMPLE 2: 4140 Steel End Milling")
print("=" * 60)

V2  = 100   # m/min coated carbide
D2  = 12    # mm end mill diameter
fz  = 0.11  # mm/tooth
z   = 4     # flutes
ap2 = 6.0   # axial depth mm
ae2 = D2 * 0.75  # 75% radial engagement

N2  = (V2 * 1000) / (math.pi * D2)
Vf2 = N2 * fz * z
MRR2 = Vf2 * ap2 * ae2
n2, C2 = 0.23, 2200
T2 = (C2 / V2) ** (1/n2)

print(f"\n  Cutting Speed : {V2} m/min")
print(f"  RPM           : {N2:.0f} rpm")
print(f"  Feed/tooth    : {fz} mm")
print(f"  Feed rate     : {Vf2:.0f} mm/min")
print(f"  MRR           : {MRR2:.0f} mm³/min")
print(f"  Tool Life     : {T2:.0f} min")
