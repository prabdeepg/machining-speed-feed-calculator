"""
Machining Speed & Feed Calculator
Prabdeep Singh Ghatora | github.com/prabdeepg

Run: python speed_feed_calc.py
"""
import math, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from cutting_data import CUTTING_DATA, TAYLOR, DOC_REC, MATERIAL_HARDNESS_GROUP

TOOL_NAMES = {
    "HSS":              "High Speed Steel (HSS)",
    "carbide_uncoated": "Uncoated Carbide (C2)",
    "carbide_coated":   "Coated Carbide (TiAlN)",
    "ceramic":          "Ceramic Insert",
}

OP_NAMES = {
    "turning":   "Turning (OD)",
    "facing":    "Facing",
    "boring":    "Boring",
    "end_mill":  "End Milling",
    "face_mill": "Face Milling",
    "slot_mill": "Slot Milling",
}


def calc_rpm(speed_mpm, diameter_mm):
    return (speed_mpm * 1000) / (math.pi * diameter_mm)


def calc_feed_rate(rpm, feed_per_rev_mm, n_teeth=1):
    return rpm * feed_per_rev_mm * n_teeth


def calc_mrr(feed_rate, doc, width_of_cut):
    """Material Removal Rate in mm³/min"""
    return feed_rate * doc * width_of_cut


def taylor_tool_life(speed, mat, tool):
    key = (mat, tool)
    if key not in TAYLOR:
        return None
    n, C = TAYLOR[key]
    return (C / speed) ** (1/n)


def run_calc(mat, tool, operation, diam_mm, n_teeth=1):
    if mat not in CUTTING_DATA:
        print(f"Material '{mat}' not in database.")
        return
    if tool not in CUTTING_DATA[mat]:
        print(f"Tool '{tool}' not available for '{mat}'.")
        return

    speed, feed = CUTTING_DATA[mat][tool][operation]
    if speed is None:
        print(f"Ceramic end/slot milling not recommended for {mat}.")
        return

    rpm      = calc_rpm(speed, diam_mm)
    feed_ipm = calc_feed_rate(rpm, feed, n_teeth)
    h_group  = MATERIAL_HARDNESS_GROUP.get(mat, "medium")
    doc_r, doc_f = DOC_REC[h_group][operation]

    is_milling = operation in ("end_mill","face_mill","slot_mill")
    woc = diam_mm * 0.75 if is_milling else diam_mm   # 75% engagement for milling
    mrr  = calc_mrr(feed_ipm, doc_r, woc)
    life = taylor_tool_life(speed, mat, tool)

    speed_sfm = speed * 3.281

    print()
    print("══" * 28)
    print("  MACHINING SPEED & FEED CALCULATOR")
    print("══" * 28)
    print(f"  Operation  : {OP_NAMES.get(operation, operation)}")
    print(f"  Material   : {mat}")
    print(f"  Tool       : {TOOL_NAMES.get(tool, tool)}")
    print(f"  Diameter   : {diam_mm:.2f} mm")
    if is_milling: print(f"  # Teeth    : {n_teeth}")
    print("──" * 28)
    print(f"  Cutting Speed  : {speed:>4} m/min  ({speed_sfm:.0f} SFM)")
    print(f"  RPM            : {rpm:>6.0f} rpm")
    print(f"  Feed/{'tooth' if is_milling else 'rev':<5}   : {feed:>6.3f} mm")
    print(f"  Feed Rate      : {feed_ipm:>6.0f} mm/min")
    print(f"  DOC (rough)    : {doc_r:.1f} mm")
    print(f"  DOC (finish)   : {doc_f:.2f} mm")
    print(f"  MRR (rough)    : {mrr:>6.0f} mm³/min")
    if life:
        print(f"  Tool Life est. : {life:.0f} min at this speed")
    else:
        print(f"  Tool Life      : No Taylor data for this combo")
    print("══" * 28)
    print()


def interactive():
    materials = list(CUTTING_DATA.keys())
    tools     = ["HSS","carbide_uncoated","carbide_coated","ceramic"]
    ops       = ["turning","facing","boring","end_mill","face_mill","slot_mill"]

    print("\n=== Machining Speed & Feed Calculator ===")
    print("Materials:", ", ".join(materials))
    mat = input("\nWorkpiece material: ").strip()
    if mat not in materials:
        # fuzzy match
        matches = [m for m in materials if mat.lower() in m.lower()]
        if len(matches) == 1:
            mat = matches[0]
            print(f"  → Using: {mat}")
        else:
            print(f"No match. Options: {materials}"); return

    print("Tools:", ", ".join(tools))
    tool = input("Tool type: ").strip()
    if tool not in tools:
        print(f"Options: {tools}"); return

    print("Operations:", ", ".join(ops))
    op = input("Operation: ").strip()
    if op not in ops: print(f"Options: {ops}"); return

    diam = float(input("Tool/workpiece diameter (mm): ").strip())
    n_teeth = 1
    if op in ("end_mill","face_mill","slot_mill"):
        n_teeth = int(input("Number of teeth/flutes: ").strip() or "4")

    run_calc(mat, tool, op, diam, n_teeth)


def demo():
    print("\n--- Demo 1: 6061-T6 OD Turning, Coated Carbide, Ø50mm ---")
    run_calc("6061-T6 Al", "carbide_coated", "turning", 50)
    print("--- Demo 2: 4140 Steel End Mill, Coated Carbide, Ø12mm 4-flute ---")
    run_calc("4140 Steel", "carbide_coated", "end_mill", 12, n_teeth=4)
    print("--- Demo 3: 304 Stainless Facing, Uncoated Carbide, Ø80mm ---")
    run_calc("304 Stainless", "carbide_uncoated", "facing", 80)


if __name__ == "__main__":
    if "--demo" in sys.argv:
        demo()
    elif "--interactive" in sys.argv or "-i" in sys.argv:
        interactive()
    else:
        demo()
        print("Run with -i for interactive mode, --demo for demo output.")
