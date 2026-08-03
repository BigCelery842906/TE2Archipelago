from BaseClasses import Location
from typing import Dict

# Base ID offset for all Escapists 2 locations
BASE_LOCATION_ID = 80000

class Escapists2Location(Location):
    game: str = "The Escapists 2"

# Maps physical game interactions to Archipelago Location IDs.
# Organized by prison and access level.
location_dictionary: Dict[str, int] = {

    # ==========================================
    # === PRISON 1: CENTER PERKS 2.0         ===
    # ==========================================
    
    # Inmate Desks (Free Access)
    "Inmate_Player_P1_80009": BASE_LOCATION_ID + 9,
    "Inmate_Player_P1_80020": BASE_LOCATION_ID + 20,
    "Inmate_Player_P1_80027": BASE_LOCATION_ID + 27,
    "Inmate_PNubertNLocal_80007": BASE_LOCATION_ID + 7,
    "Inmate_AI_Inmate_1_80035": BASE_LOCATION_ID + 35,
    "Inmate_AI_Inmate_2_80004": BASE_LOCATION_ID + 4,
    "Inmate_AI_Inmate_3_80029": BASE_LOCATION_ID + 29,
    "Inmate_AI_Inmate_4_80012": BASE_LOCATION_ID + 12,
    "Inmate_AI_Inmate_5_80034": BASE_LOCATION_ID + 34,
    "Inmate_AI_Inmate_6_80019": BASE_LOCATION_ID + 19,
    "Inmate_AI_Inmate_7_80022": BASE_LOCATION_ID + 22,
    "Inmate_AI_Inmate_8_80025": BASE_LOCATION_ID + 25,
    "Inmate_AI_Inmate_9_80015": BASE_LOCATION_ID + 15,
    "Inmate_AI_Inmate_10_80037": BASE_LOCATION_ID + 37,
    "Inmate_AI_Inmate_11_80002": BASE_LOCATION_ID + 2,
    "Inmate_AI_Inmate_12_80028": BASE_LOCATION_ID + 28,
    "Inmate_AI_Inmate_13_80026": BASE_LOCATION_ID + 26,
    "Inmate_AI_Inmate_14_80031": BASE_LOCATION_ID + 31,
    "Inmate_AI_Inmate_15_80036": BASE_LOCATION_ID + 36,
    "Inmate_AI_Inmate_16_80003": BASE_LOCATION_ID + 3,
    "Inmate_AI_Inmate_17_80001": BASE_LOCATION_ID + 1,
    "Inmate_AI_Inmate_18_80011": BASE_LOCATION_ID + 11,
    "Inmate_AI_Inmate_19_80005": BASE_LOCATION_ID + 5,
    "Inmate_AI_Inmate_80017": BASE_LOCATION_ID + 17,

    # System Desks (Public or Job-Specific)
    "SystemDesk_F1_XN32_Y10_80008": BASE_LOCATION_ID + 8, # Cutlery Tray
    "UnownedDesk_80006": BASE_LOCATION_ID + 6,
    "UnownedDesk_80013": BASE_LOCATION_ID + 13,
    "UnownedDesk_80014": BASE_LOCATION_ID + 14,
    "UnownedDesk_80018": BASE_LOCATION_ID + 18,
    "UnownedDesk_80032": BASE_LOCATION_ID + 32,
    "UnownedDesk_80033": BASE_LOCATION_ID + 33,

    # Restricted Desks
    "GuardsDesk_80016": BASE_LOCATION_ID + 16, # Requires Red Key
    "GuardsDesk_80021": BASE_LOCATION_ID + 21, # Requires Red Key
    "ContrabandDesk_80023": BASE_LOCATION_ID + 23, # Requires Red Key + Guard Outfit
    "MaintenanceDesk_80010": BASE_LOCATION_ID + 10, # Requires Cyan Key
    "MaintenanceDesk_80024": BASE_LOCATION_ID + 24, # Requires Cyan Key
    "MedicDesk_80030": BASE_LOCATION_ID + 30, # Requires Medic Outfit

    # ==========================================
    # === PRISON 2: COUGAR CREEK RAILROAD    ===
    # ==========================================
    "Cougar Creek - Unowned Desk 1": BASE_LOCATION_ID + 1001,
    "Cougar Creek - Contraband Desk": BASE_LOCATION_ID + 1002,
    "Cougar Creek - Unowned Desk 2": BASE_LOCATION_ID + 1003,
    "Cougar Creek - Unowned Desk 3": BASE_LOCATION_ID + 1004,
    "Cougar Creek - Medic Desk": BASE_LOCATION_ID + 1005,
    "Cougar Creek - Unowned Desk 4": BASE_LOCATION_ID + 1006,
    "Cougar Creek - Unowned Desk 5": BASE_LOCATION_ID + 1007,
    "Cougar Creek - Unowned Desk 6": BASE_LOCATION_ID + 1008,

    # ==========================================
    # === GLOBAL/SHARED PROGRESSION CHECKS   ===
    # ==========================================

    # Crafting Milestones
    "Craft: Tool Handle": BASE_LOCATION_ID + 100,
    "Craft: Flimsy Pickaxe": BASE_LOCATION_ID + 101,
    "Craft: Flimsy Shovel": BASE_LOCATION_ID + 102,
    "Craft: Flimsy Cutters": BASE_LOCATION_ID + 103,
    "Craft: Fake Wall Block": BASE_LOCATION_ID + 104,
    "Craft: Contraband Pouch": BASE_LOCATION_ID + 105,
    "Craft: Bed Dummy": BASE_LOCATION_ID + 106,
    "Craft: Fake Carrot": BASE_LOCATION_ID + 1100, 
    "Craft: Grappling Hook": BASE_LOCATION_ID + 1101, 

    # Shop Checks (Mystery Boxes)
    "Shop: Mystery Box 1": BASE_LOCATION_ID + 200,
    "Shop: Mystery Box 2": BASE_LOCATION_ID + 201,
    "Shop: Mystery Box 3": BASE_LOCATION_ID + 202,
    "Shop: Mystery Box 4": BASE_LOCATION_ID + 203,
    "Shop: Mystery Box 5": BASE_LOCATION_ID + 204,

    # Job Quotas (Requires completing the job quota once)
    "Job: Woodwork": BASE_LOCATION_ID + 301,
    "Job: Shoemaker": BASE_LOCATION_ID + 302,
    "Job: Blacksmith": BASE_LOCATION_ID + 303,
    "Job: Mining": BASE_LOCATION_ID + 304,
    "Job: Plumbing": BASE_LOCATION_ID + 305,
    "Job: Electrician": BASE_LOCATION_ID + 306,
    "Job: Kitchen": BASE_LOCATION_ID + 307,
    "Job: Farming": BASE_LOCATION_ID + 308,
    "Job: Waste Disposal": BASE_LOCATION_ID + 309,
    "Job: Mail Sorting": BASE_LOCATION_ID + 310,
    "Job: Canine Carer": BASE_LOCATION_ID + 311,
    "Job: Painting": BASE_LOCATION_ID + 312,
    "Job: Pumpkin Carving": BASE_LOCATION_ID + 313,
    "Job: Vampire Laundry": BASE_LOCATION_ID + 314,
    "Job: Trick Or Treat": BASE_LOCATION_ID + 315,
    "Job: Werewolf Carer": BASE_LOCATION_ID + 316,
    "Job: Balloon Animals": BASE_LOCATION_ID + 317,
    "Job: Face Painting": BASE_LOCATION_ID + 318,
    "Job: Lion Taming": BASE_LOCATION_ID + 319,
    "Job: Hanging Posters": BASE_LOCATION_ID + 320,
    "Job: Relight Torches": BASE_LOCATION_ID + 321,
    "Job: Horseshoe Making": BASE_LOCATION_ID + 322,
    "Job: Minstrel": BASE_LOCATION_ID + 323,
    "Job: Stonemason": BASE_LOCATION_ID + 324,
    "Job: Guard The Box": BASE_LOCATION_ID + 325,
    "Job: Destroy Mail": BASE_LOCATION_ID + 326,
    "Job: Robot Servicing": BASE_LOCATION_ID + 327,
    "Job: Raindeer": BASE_LOCATION_ID + 328,

    # Max Stat Milestones (Reach 100 in a specific stat)
    "Milestone: Max Intellect": BASE_LOCATION_ID + 401,
    "Milestone: Max Strength": BASE_LOCATION_ID + 402,
    "Milestone: Max Fitness": BASE_LOCATION_ID + 403,

# ==========================================
    # === ESCAPE SPECIFIC CHECKS             ===
    # ==========================================
    
    # Center Perks 2.0
    "Escape: Perimeter Breakout (Center Perks)": BASE_LOCATION_ID + 1500, # 81500
    "Escape: Meet The Crew": BASE_LOCATION_ID + 1501, # 81501

    # Cougar Creek Railroad
    "Escape: My Little Phoney": BASE_LOCATION_ID + 1502, # 81502
    "Escape: Hooked On You": BASE_LOCATION_ID + 1503, # 81503

    # Rattlesnake Springs
    "Escape: Perimeter Breakout (Rattlesnake)": BASE_LOCATION_ID + 2500, # 82500
    "Escape: Zip It Up": BASE_LOCATION_ID + 2501, # 82501

    # K.A.P.O.W. Camp
    "Escape: Perimeter Breakout (KAPOW)": BASE_LOCATION_ID + 3500, # 83500
    "Escape: Speed McQueen": BASE_LOCATION_ID + 3501, # 83501

    # H.M.S. Orca
    "Escape: Scuba Doo": BASE_LOCATION_ID + 4500, # 84500
    "Escape: Wave Goodbye": BASE_LOCATION_ID + 4501, # 84501

    # HMP Offshore
    "Escape: Perimeter Breakout (Offshore)": BASE_LOCATION_ID + 5500, # 85500
    "Escape: Trash Talk": BASE_LOCATION_ID + 5501, # 85501
    "Escape: Swimming With Dolphins": BASE_LOCATION_ID + 5502, # 85502

    # Fort Tundra
    "Escape: Perimeter Breakout (Tundra)": BASE_LOCATION_ID + 6500, # 86500
    "Escape: Rock-hammer Hard Place": BASE_LOCATION_ID + 6501, # 86501

    # Area 17
    "Escape: Perimeter Breakout (Area 17)": BASE_LOCATION_ID + 7500, # 87500
    "Escape: I'm Only Human": BASE_LOCATION_ID + 7501, # 87501

    # Air Force Con
    "Escape: Passport To Freedom": BASE_LOCATION_ID + 8500, # 88500
    "Escape: Plane Crazy": BASE_LOCATION_ID + 8501, # 88501

# === U.S.S. ANOMALY ===
    "Escape: Perimeter Breakout (Anomaly)": BASE_LOCATION_ID + 9500, # 89500
    "Escape: Race From Space": BASE_LOCATION_ID + 9501, # 89501

} 

# ==========================================
# === AUTOMATIC DESK GENERATOR           ===
# ==========================================
# This automatically generates all the required desk IDs for the Python server
# so they match the dictionary without needing 3 millionlines of code

for i in range(1, 39): location_dictionary[f"Rattlesnake Desk {i}"] = BASE_LOCATION_ID + 2000 + i
for i in range(1, 28): location_dictionary[f"KAPOW Camp Desk {i}"] = BASE_LOCATION_ID + 3000 + i
for i in range(1, 16): location_dictionary[f"HMS Orca Desk {i}"] = BASE_LOCATION_ID + 4000 + i
for i in range(1, 35): location_dictionary[f"HMP Offshore Desk {i}"] = BASE_LOCATION_ID + 5000 + i
for i in range(1, 37): location_dictionary[f"Fort Tundra Desk {i}"] = BASE_LOCATION_ID + 6000 + i
for i in range(1, 34): location_dictionary[f"Area 17 Desk {i}"] = BASE_LOCATION_ID + 7000 + i
for i in range(1, 13): location_dictionary[f"Air Force Con Desk {i}"] = BASE_LOCATION_ID + 8000 + i
for i in range(1, 29): location_dictionary[f"USS Anomaly Desk {i}"] = BASE_LOCATION_ID + 9000 + i
