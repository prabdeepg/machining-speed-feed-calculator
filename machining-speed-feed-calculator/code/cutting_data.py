"""
Cutting speed and feed rate database.
Sources: Machinery's Handbook 30th Ed., Sandvik Coromant, Kennametal catalogs.
Units: speeds in m/min, feeds in mm/rev (turning) or mm/tooth (milling)
"""

# Structure: CUTTING_DATA[material][tool][operation] = (speed_m_min, feed_mm)
# feed for turning = mm/rev; for milling = mm/tooth
# depth of cut recommendations in DOC_REC[material_group][operation] = (rough_mm, finish_mm)

CUTTING_DATA = {
    "6061-T6 Al": {
        "HSS": {
            "turning":      (120, 0.20),
            "facing":       (100, 0.18),
            "boring":       (90,  0.15),
            "end_mill":     (60,  0.08),
            "face_mill":    (80,  0.10),
            "slot_mill":    (45,  0.06),
        },
        "carbide_uncoated": {
            "turning":      (250, 0.25),
            "facing":       (230, 0.22),
            "boring":       (200, 0.20),
            "end_mill":     (150, 0.12),
            "face_mill":    (200, 0.15),
            "slot_mill":    (100, 0.08),
        },
        "carbide_coated": {
            "turning":      (305, 0.25),
            "facing":       (280, 0.22),
            "boring":       (250, 0.20),
            "end_mill":     (200, 0.14),
            "face_mill":    (250, 0.18),
            "slot_mill":    (140, 0.10),
        },
        "ceramic": {
            "turning":      (500, 0.15),
            "facing":       (450, 0.13),
            "boring":       (400, 0.12),
            "end_mill":     (None, None),   # ceramic end mills not typical
            "face_mill":    (600, 0.10),
            "slot_mill":    (None, None),
        },
    },
    "7075-T6 Al": {
        "HSS":              {"turning":(110,0.18),"facing":(95,0.16),"boring":(85,0.14),"end_mill":(55,0.07),"face_mill":(75,0.09),"slot_mill":(40,0.05)},
        "carbide_uncoated": {"turning":(230,0.23),"facing":(210,0.20),"boring":(185,0.18),"end_mill":(140,0.11),"face_mill":(185,0.14),"slot_mill":(90,0.07)},
        "carbide_coated":   {"turning":(280,0.23),"facing":(260,0.20),"boring":(230,0.18),"end_mill":(185,0.13),"face_mill":(230,0.17),"slot_mill":(130,0.09)},
        "ceramic":          {"turning":(450,0.14),"facing":(420,0.12),"boring":(380,0.11),"end_mill":(None,None),"face_mill":(550,0.09),"slot_mill":(None,None)},
    },
    "1018 Steel": {
        "HSS":              {"turning":(38,0.18),"facing":(35,0.15),"boring":(30,0.12),"end_mill":(25,0.06),"face_mill":(30,0.08),"slot_mill":(20,0.04)},
        "carbide_uncoated": {"turning":(120,0.22),"facing":(110,0.20),"boring":(100,0.18),"end_mill":(80,0.10),"face_mill":(100,0.12),"slot_mill":(60,0.07)},
        "carbide_coated":   {"turning":(180,0.25),"facing":(165,0.22),"boring":(150,0.20),"end_mill":(120,0.12),"face_mill":(160,0.15),"slot_mill":(90,0.08)},
        "ceramic":          {"turning":(350,0.12),"facing":(320,0.10),"boring":(300,0.09),"end_mill":(None,None),"face_mill":(420,0.08),"slot_mill":(None,None)},
    },
    "4140 Steel": {
        "HSS":              {"turning":(25,0.15),"facing":(22,0.12),"boring":(20,0.10),"end_mill":(18,0.05),"face_mill":(22,0.07),"slot_mill":(14,0.04)},
        "carbide_uncoated": {"turning":(100,0.20),"facing":(90,0.18),"boring":(80,0.15),"end_mill":(65,0.09),"face_mill":(85,0.11),"slot_mill":(50,0.06)},
        "carbide_coated":   {"turning":(150,0.22),"facing":(140,0.20),"boring":(120,0.18),"end_mill":(100,0.11),"face_mill":(130,0.13),"slot_mill":(75,0.08)},
        "ceramic":          {"turning":(300,0.10),"facing":(280,0.09),"boring":(260,0.08),"end_mill":(None,None),"face_mill":(380,0.07),"slot_mill":(None,None)},
    },
    "304 Stainless": {
        "HSS":              {"turning":(20,0.12),"facing":(18,0.10),"boring":(16,0.08),"end_mill":(14,0.04),"face_mill":(18,0.06),"slot_mill":(11,0.03)},
        "carbide_uncoated": {"turning":(70,0.18),"facing":(65,0.16),"boring":(58,0.14),"end_mill":(45,0.08),"face_mill":(60,0.10),"slot_mill":(35,0.05)},
        "carbide_coated":   {"turning":(110,0.20),"facing":(100,0.18),"boring":(90,0.16),"end_mill":(70,0.10),"face_mill":(95,0.12),"slot_mill":(55,0.07)},
        "ceramic":          {"turning":(220,0.09),"facing":(200,0.08),"boring":(185,0.07),"end_mill":(None,None),"face_mill":(280,0.06),"slot_mill":(None,None)},
    },
    "Cast Iron Cl30": {
        "HSS":              {"turning":(30,0.20),"facing":(27,0.18),"boring":(25,0.15),"end_mill":(20,0.07),"face_mill":(25,0.09),"slot_mill":(16,0.05)},
        "carbide_uncoated": {"turning":(110,0.25),"facing":(100,0.22),"boring":(90,0.20),"end_mill":(70,0.12),"face_mill":(95,0.15),"slot_mill":(55,0.08)},
        "carbide_coated":   {"turning":(160,0.28),"facing":(145,0.25),"boring":(130,0.22),"end_mill":(100,0.14),"face_mill":(140,0.18),"slot_mill":(80,0.10)},
        "ceramic":          {"turning":(400,0.15),"facing":(370,0.13),"boring":(350,0.11),"end_mill":(None,None),"face_mill":(500,0.10),"slot_mill":(None,None)},
    },
    "C360 Brass": {
        "HSS":              {"turning":(90,0.22),"facing":(80,0.20),"boring":(70,0.18),"end_mill":(55,0.09),"face_mill":(70,0.11),"slot_mill":(40,0.06)},
        "carbide_uncoated": {"turning":(200,0.28),"facing":(185,0.25),"boring":(170,0.22),"end_mill":(130,0.14),"face_mill":(170,0.18),"slot_mill":(95,0.09)},
        "carbide_coated":   {"turning":(260,0.30),"facing":(240,0.27),"boring":(220,0.24),"end_mill":(165,0.16),"face_mill":(215,0.20),"slot_mill":(120,0.10)},
        "ceramic":          {"turning":(None,None),"facing":(None,None),"boring":(None,None),"end_mill":(None,None),"face_mill":(None,None),"slot_mill":(None,None)},
    },
    "Grade 5 Ti": {
        "HSS":              {"turning":(15,0.10),"facing":(13,0.08),"boring":(11,0.07),"end_mill":(10,0.03),"face_mill":(12,0.05),"slot_mill":(8,0.02)},
        "carbide_uncoated": {"turning":(45,0.15),"facing":(40,0.13),"boring":(36,0.11),"end_mill":(28,0.06),"face_mill":(38,0.08),"slot_mill":(22,0.04)},
        "carbide_coated":   {"turning":(60,0.18),"facing":(55,0.15),"boring":(50,0.13),"end_mill":(40,0.08),"face_mill":(52,0.10),"slot_mill":(30,0.05)},
        "ceramic":          {"turning":(None,None),"facing":(None,None),"boring":(None,None),"end_mill":(None,None),"face_mill":(None,None),"slot_mill":(None,None)},
    },
    "ABS": {
        "HSS":              {"turning":(150,0.25),"facing":(130,0.22),"boring":(110,0.18),"end_mill":(80,0.12),"face_mill":(100,0.15),"slot_mill":(60,0.08)},
        "carbide_coated":   {"turning":(300,0.30),"facing":(270,0.27),"boring":(240,0.24),"end_mill":(180,0.18),"face_mill":(230,0.22),"slot_mill":(130,0.12)},
        "carbide_uncoated": {"turning":(250,0.28),"facing":(225,0.25),"boring":(200,0.22),"end_mill":(150,0.15),"face_mill":(195,0.18),"slot_mill":(110,0.10)},
        "ceramic":          {"turning":(None,None),"facing":(None,None),"boring":(None,None),"end_mill":(None,None),"face_mill":(None,None),"slot_mill":(None,None)},
    },
}

# Taylor's tool life constants: VTn = C → [n, C]  (V in m/min, T in min)
TAYLOR = {
    ("6061-T6 Al",   "carbide_coated"):   [0.30, 4500],
    ("7075-T6 Al",   "carbide_coated"):   [0.30, 4200],
    ("1018 Steel",   "carbide_coated"):   [0.25, 2800],
    ("4140 Steel",   "carbide_coated"):   [0.23, 2200],
    ("304 Stainless","carbide_coated"):   [0.20, 1600],
    ("Cast Iron Cl30","carbide_coated"):  [0.27, 3100],
    ("Grade 5 Ti",   "carbide_coated"):   [0.18, 900],
    ("6061-T6 Al",   "HSS"):              [0.125, 800],
    ("1018 Steel",   "HSS"):              [0.100, 400],
    ("4140 Steel",   "HSS"):              [0.090, 280],
}

# Recommended depth of cut [roughing_mm, finishing_mm]
DOC_REC = {
    "soft":     {"turning":(3.0,0.5), "facing":(2.5,0.4), "boring":(2.0,0.4), "end_mill":(8.0,0.5), "face_mill":(3.0,0.5), "slot_mill":(1.0*8,0.3)},
    "medium":   {"turning":(2.0,0.4), "facing":(2.0,0.3), "boring":(1.5,0.3), "end_mill":(6.0,0.4), "face_mill":(2.5,0.4), "slot_mill":(0.8*8,0.3)},
    "hard":     {"turning":(1.5,0.3), "facing":(1.5,0.25),"boring":(1.0,0.25),"end_mill":(4.0,0.3), "face_mill":(2.0,0.3), "slot_mill":(0.5*8,0.25)},
    "superhard":{"turning":(0.5,0.15),"facing":(0.5,0.12),"boring":(0.4,0.10),"end_mill":(2.0,0.2), "face_mill":(1.0,0.2), "slot_mill":(0.3*8,0.15)},
}

MATERIAL_HARDNESS_GROUP = {
    "6061-T6 Al":"soft","7075-T6 Al":"soft","ABS":"soft","C360 Brass":"soft",
    "1018 Steel":"medium","Cast Iron Cl30":"medium",
    "4140 Steel":"hard","304 Stainless":"hard",
    "Grade 5 Ti":"superhard",
}
