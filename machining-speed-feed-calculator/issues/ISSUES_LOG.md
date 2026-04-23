# Issues Log — Machining Speed & Feed Calculator

---

## ISSUE-001 — RPM Exceeds Machine Spindle Limit for Small Diameters
**Status:** Resolved  
**Severity:** Medium  

**Description:**  
For small diameters (e.g., Ø3mm end mill in aluminum at 200 m/min), the calculated RPM = 21,221 rpm, which exceeds the 12,000 rpm limit of most standard VMCs.

**Root Cause:**  
Calculator applies catalog cutting speed without checking against machine capability.

**Fix:**  
Added `MAX_RPM` parameter (default: 12,000 rpm). If calculated RPM exceeds limit, the tool automatically back-calculates the maximum achievable cutting speed and reports both the catalog recommendation and the machine-limited value. User can override MAX_RPM with `--max-rpm`.

---

## ISSUE-002 — Taylor Equation Data Missing for Many Material/Tool Combos
**Status:** Known Limitation  
**Severity:** Low  

**Description:**  
`TAYLOR` dict only covers ~10 of the 36+ possible material/tool combinations. Combinations not in the dict silently skip tool life output.

**Fix (Partial):**  
Added a note in the output: "No Taylor data for this combo — see Machinery's Handbook Table 3 p. 1065 for manual lookup." Full Taylor database expansion is a future enhancement.

---

## ISSUE-003 — Ceramic Not Applicable for Milling Operations Warning
**Status:** Resolved  
**Severity:** Low  

**Description:**  
Initial version didn't warn users when they selected ceramic inserts for end milling — it silently returned `None` for speed.

**Fix:**  
Added explicit check: if speed is None, print "Ceramic end/slot milling not recommended — ceramic inserts are brittle and prone to chipping under interrupted cuts. Use coated carbide instead."

---

## ISSUE-004 — Feed Rate for Multi-Tooth Milling Not Using Tooth Count
**Status:** Resolved  
**Severity:** High  

**Description:**  
Early version calculated `Vf = N × fz` without multiplying by number of teeth. For a 4-flute end mill this underestimates feed rate by 4×, leading to very conservative (slow) recommended feeds.

**Root Cause:**  
`calc_feed_rate()` function was missing `n_teeth` parameter.

**Fix:**  
Added `n_teeth` parameter: `Vf = N × fz × n_teeth`. Updated all milling calculations. Added test `test_milling_feed_uses_tooth_count()` to prevent regression.
