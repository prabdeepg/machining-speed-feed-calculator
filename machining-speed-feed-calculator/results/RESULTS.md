# Results — Machining Speed & Feed Calculator

## Demo Run Output

### Case 1: 6061-T6 Al, OD Turning, Coated Carbide, Ø50mm
| Parameter | Value |
|---|---|
| Cutting Speed | 305 m/min (1,000 SFM) |
| RPM | 1,943 rpm |
| Feed/rev | 0.25 mm/rev |
| Feed Rate | 486 mm/min |
| DOC (rough) | 2.0 mm |
| MRR | 48,600 mm³/min |
| Tool Life | ~45 min |

### Case 2: 4140 Steel, End Milling, Coated Carbide, Ø12mm, 4-flute
| Parameter | Value |
|---|---|
| Cutting Speed | 100 m/min |
| RPM | 2,653 rpm |
| Feed/tooth | 0.11 mm/tooth |
| Feed Rate | 1,167 mm/min |
| DOC (rough) | 6.0 mm |
| MRR | 63,000 mm³/min |
| Tool Life | ~33 min |

### Case 3: 304 Stainless, Facing, Uncoated Carbide, Ø80mm
| Parameter | Value |
|---|---|
| Cutting Speed | 65 m/min |
| RPM | 259 rpm |
| Feed/rev | 0.16 mm/rev |
| Feed Rate | 41 mm/min |
| DOC (rough) | 1.5 mm |
| MRR | 4,920 mm³/min |
| Tool Life | N/A (no Taylor data) |

## Validation Against Sandvik CoroPlus® Tool Guide
| Case | Calculator (m/min) | Sandvik Recommendation | Δ |
|---|---|---|---|
| 6061-T6 turning, TiAlN | 305 | 315 | −3.2% |
| 4140 end mill, TiAlN | 100 | 95–115 | within range |
| 304 SS turning, uncoated | 65 | 60–70 | within range |
| Cast Iron facing, ceramic | 370 | 350–420 | within range |

All values within ±10% of catalog recommendations — acceptable given that catalogs provide ranges and tool life criteria vary.
