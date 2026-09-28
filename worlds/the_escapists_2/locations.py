from __future__ import annotations
from typing import TYPE_CHECKING, Dict

from BaseClasses import Location

from . import items

if TYPE_CHECKING:
    from .world import TheEscapists2World

BASE_LOCATION_ID: int = 80000

LOCATION_NAME_TO_ID: Dict[str, int] = {
    # Organised by prison, and by desks, jobs, and general checks
    # Default: 80000
    # Global: Start at default
    # Stat Milestones: Global + 200 (Start at 30 for each stat, end at 100)
    # Prison Number: + 1000 * Prison number
    # Escapes: + 100
    # Jobs: + 200

    # Global Checks (Doesn't matter what prison you get these in)

    # Crafting TODO: Implementation of this
    #"Craft: Tool Handle": BASE_LOCATION_ID + 10,
    #"Craft: Flimsy Pickaxe": BASE_LOCATION_ID + 11,
    #"Craft: Flimsy Shovel": BASE_LOCATION_ID + 12,
    #"Craft: Flimsy Cutters": BASE_LOCATION_ID + 13,
    #"Craft: Fake Wall Block": BASE_LOCATION_ID + 14,
    #"Craft: Contraband Pouch": BASE_LOCATION_ID + 15,
    #"Craft: Bed Dummy": BASE_LOCATION_ID + 16,

    #TODO: Check these to see if I put them here or not
    #"Craft: Fake Carrot": BASE_LOCATION_ID + 17,
    #"Craft: Grappling Hook": BASE_LOCATION_ID + 18,

    #Stat Milestones
    # 200 for strength, 300 for stamina, 400 for intellect
    # Max are here, everything else is below in a for loop

    "Strength Stat: Max": BASE_LOCATION_ID + 200,
    "Stamina Stat: Max": BASE_LOCATION_ID + 300,
    "Intellect Stat: Max": BASE_LOCATION_ID + 400,

    # Job Quotas (Requires completing the job quota once)
    "Job: Woodwork": BASE_LOCATION_ID + 301, #RSS, HMPOff
    "Job: Shoemaker": BASE_LOCATION_ID + 302, #CP, RSS
    "Job: Blacksmith": BASE_LOCATION_ID + 303, #HMPOff, FT, A17
    "Job: Mining": BASE_LOCATION_ID + 304, #HMPOff, USSA
    "Job: Plumbing": BASE_LOCATION_ID + 305, #KAPOW, FT, A17
    "Job: Engineering": BASE_LOCATION_ID + 306, #A17, USSA
    "Job: Kitchen": BASE_LOCATION_ID + 307, #KAPOW, USSA
    "Job: Farming": BASE_LOCATION_ID + 308, #KAPOW, USSA
    "Job: Waste Disposal": BASE_LOCATION_ID + 309, #CP, RSS, A17
    "Job: Mail Sorting": BASE_LOCATION_ID + 310, #CP, KAPOW
    "Job: Canine Carer": BASE_LOCATION_ID + 311, #HMPOff, FT
    "Job: Painting": BASE_LOCATION_ID + 312, #CP, RSS, FT

    # Escapes (Single player only for now)

    # Center Perks 2.0
    "Escape: Perimeter Breakout (Center Perks 2.0)" : BASE_LOCATION_ID + 1000 + 100 + 1,
    "Escape: Meet the Crew (Center Perks 2.0)" : BASE_LOCATION_ID + 100 + 2,

    # Rattlesnake Springs
    "Escape: Perimeter Breakout (Rattlesnake Springs)" : BASE_LOCATION_ID + 2000 + 100 + 1,
    "Escape: Zip It Up (Rattlesnake Springs)" : BASE_LOCATION_ID + 2000 + 100 + 2,

    #KAPOW Camp
    "Escape: Perimeter Breakout (K.A.P.O.W Camp)"  : BASE_LOCATION_ID + 3000 + 100 + 1,
    "Escape: Speed McQueen (K.A.P.O.W Camp)"  : BASE_LOCATION_ID + 3000 + 100 + 2,

    #HMP Offshore
    "Escape: Perimeter Breakout (H.M.P. Offshore)" : BASE_LOCATION_ID + 4000 + 100 + 1,
    "Escape: Swimming With Dolphins  (H.M.P. Offshore)" : BASE_LOCATION_ID + 4000 + 100 + 2,
    "Escape: Trash Talk  (H.M.P. Offshore)" : BASE_LOCATION_ID + 4000 + 100 + 3,

    #Fort Tundra
    "Escape: Perimeter Breakout (Fort Tundra)" : BASE_LOCATION_ID + 5000 + 100 + 1,
    "Escape: Rock-hammer Hard Place (Fort Tundra)" : BASE_LOCATION_ID + 5000 + 100 + 2,

    #Area 17
    "Escape: Perimeter Breakout (Area 17)" : BASE_LOCATION_ID + 6000 + 100 + 1,
    "Escape: I'm Only Human (Area 17)" : BASE_LOCATION_ID + 6000 + 100 + 2,

    #USS Anomaly
    "Escape: Perimeter Breakout (U.S.S. Anomaly)" : BASE_LOCATION_ID + 7000 + 100 + 1,
    "Escape: Race From Space (U.S.S. Anomaly)" : BASE_LOCATION_ID + 7000 + 100 + 2,

    #TRANSPORT PRISONS

    #Cougar Creek Railroad
    "Escape: My Little Phoney (Cougar Creek Railroad)" : BASE_LOCATION_ID + 8000 + 100 + 1,
    "Escape: Hooked On You (Cougar Creek Railroad)" : BASE_LOCATION_ID + 8000 + 100 + 2,

    #HMS Orca
    "Escape: Scuba Doo (H.M.S. Orca)" : BASE_LOCATION_ID + 9000 + 100 + 1,
    "Escape: Wave Goodbye (H.M.S. Orca)" : BASE_LOCATION_ID + 9000 + 100 + 2,

    #Air Force Con
    "Escape: Passport To Freedom (Air Force Con)" : BASE_LOCATION_ID + 10000 + 100 + 1,
    "Escape: Plane Crazy (Air Force Con)" : BASE_LOCATION_ID + 10000 + 100 + 2,

    #Desks for each prison (Where not called the same)
    #CP2.0
    "Center Perks 2.0 Contraband Desk" : BASE_LOCATION_ID + 1000 + 35,
    "Center Perks 2.0 Cutlery Tray" : BASE_LOCATION_ID + 1000 + 36,

    #RSS
    "Rattlesnake Springs Contraband Desk" : BASE_LOCATION_ID + 2000 + 36,
    "Rattlesnake Springs Cutlery Tray" : BASE_LOCATION_ID + 2000 + 37,

    #KAPOW
    "K.A.P.O.W Camp Contraband Desk" : BASE_LOCATION_ID + 3000 + 25,
    "K.A.P.O.W Camp Cutlery Tray" : BASE_LOCATION_ID + 3000 + 26,

    #HMPOff
    "H.M.P. Offshore Contraband Desk" : BASE_LOCATION_ID + 4000 + 28,
    "H.M.P. Offshore Cutlery Tray" : BASE_LOCATION_ID + 4000 + 29,

    #FT
    "Fort Tundra Contraband Desk" : BASE_LOCATION_ID + 5000 + 34,
    "Fort Tundra Cutlery Tray" : BASE_LOCATION_ID + 5000 + 35,

    #A17
    "Area 17 Contraband Desk" : BASE_LOCATION_ID + 6000 + 28,
    "Area 17 Cutlery Tray" : BASE_LOCATION_ID + 6000 + 29,

    #USSA
    "U.S.S. Anomaly Contraband Desk" : BASE_LOCATION_ID + 7000 + 27,
    "U.S.S. Anomaly Cutlery Tray" : BASE_LOCATION_ID + 7000 + 28,
}

# --- STAT CHECKS

for i in range(30, 100): LOCATION_NAME_TO_ID[f"Strength Stat: {i}"] = BASE_LOCATION_ID + 200 + i
for i in range(30, 100): LOCATION_NAME_TO_ID[f"Stamina Stat: {i}"] = BASE_LOCATION_ID + 300 + i
for i in range(30, 100): LOCATION_NAME_TO_ID[f"Intellect Stat: {i}"] = BASE_LOCATION_ID + 400 + i

# --- DESKS FOR EACH PRISON

for i in range (1, 35): LOCATION_NAME_TO_ID[f"Center Perks 2.0 Desk {i}"] = BASE_LOCATION_ID + 1000 + i
for i in range(1, 36): LOCATION_NAME_TO_ID[f"Rattlesnake Springs Desk {i}"] = BASE_LOCATION_ID + 2000 + i
for i in range(1, 25): LOCATION_NAME_TO_ID[f"K.A.P.O.W Camp Desk {i}"] = BASE_LOCATION_ID + 3000 + i
for i in range(1, 28): LOCATION_NAME_TO_ID[f"H.M.P. Offshore Desk {i}"] = BASE_LOCATION_ID + 4000 + i
for i in range(1, 34): LOCATION_NAME_TO_ID[f"Fort Tundra Desk {i}"] = BASE_LOCATION_ID + 5000 + i
for i in range(1, 28): LOCATION_NAME_TO_ID[f"Area 17 Desk {i}"] = BASE_LOCATION_ID + 6000 + i
for i in range(1, 27): LOCATION_NAME_TO_ID[f"U.S.S. Anomaly Desk {i}"] = BASE_LOCATION_ID + 7000 + i

for i in range(1, 9): LOCATION_NAME_TO_ID[f"Cougar Creek Railroad Desk {i}"] = BASE_LOCATION_ID + 8000 + i
for i in range(1, 15): LOCATION_NAME_TO_ID[f"H.M.S. Orca Desk {i}"] = BASE_LOCATION_ID + 9000 + i
for i in range(1, 12): LOCATION_NAME_TO_ID[f"Air Force Con Desk {i}"] = BASE_LOCATION_ID + 10000 + i

class TheEscapists2Location(Location):
    game = "The Escapists 2"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: TheEscapists2World) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: TheEscapists2World) -> None:

    global_region = world.get_region("Global")

    #Stats
    options = world.options

    if options.center_perks or options.rattlesnake_springs or options.kapow_camp or options.hmp_offshore or options.fort_tundra or options.area_17 or options.uss_anomaly:
        temp_locations = []

        increment = world.options.strength_step
        if increment != 0:
            temp_locations.append("Strength Stat: Max")
            for i in range(30, 100, increment):
                temp_locations.append(f"Strength Stat: {i}")

        increment = world.options.stamina_step
        if increment != 0:
            temp_locations.append("Stamina Stat: Max")
            for i in range(30, 100, increment):
                temp_locations.append(f"Stamina Stat: {i}")

        global_region_locations = get_location_names_with_ids(temp_locations)
        global_region.add_locations(global_region_locations)

    if options.center_perks or options.rattlesnake_springs or options.kapow_camp or options.hmp_offshore or options.fort_tundra or options.area_17 or options.uss_anomaly or options.hms_orca:
        temp_locations = []

        increment = world.options.intellect_step
        if increment != 0:
            temp_locations.append("Intellect Stat: Max")
            for i in range(30, 100, increment):
                temp_locations.append(f"Intellect Stat: {i}")

        global_region_locations = get_location_names_with_ids(temp_locations)
        global_region.add_locations(global_region_locations)

    #Jobs
    temp_locations = []
    if world.options.rattlesnake_springs or world.options.hmp_offshore:
        temp_locations.append("Job: Woodwork")
    if world.options.center_perks or world.options.rattlesnake_springs:
        temp_locations.append("Job: Shoemaker")
    if  world.options.hmp_offshore or world.options.fort_tundra or world.options.area_17:
        temp_locations.append("Job: Blacksmith")
    if world.options.hmp_offshore or world.options.uss_anomaly:
        temp_locations.append("Job: Mining")
    if world.options.kapow_camp or world.options.fort_tundra or world.options.area_17:
        temp_locations.append("Job: Plumbing")
    if world.options.area_17 or world.options.uss_anomaly:
        temp_locations.append("Job: Engineering")
    if world.options.kapow_camp or world.options.uss_anomaly:
        temp_locations.append("Job: Kitchen")
        temp_locations.append("Job: Farming")
    if world.options.center_perks or world.options.rattlesnake_springs or world.options.area_17:
        temp_locations.append("Job: Waste Disposal")
    if world.options.center_perks or world.options.kapow_camp:
        temp_locations.append("Job: Mail Sorting")
    if world.options.hmp_offshore or world.options.fort_tundra:
        temp_locations.append("Job: Canine Carer")
    if world.options.center_perks or world.options.rattlesnake_springs or world.options.fort_tundra:
        temp_locations.append("Job: Painting")
    global_region_locations = get_location_names_with_ids(temp_locations)
    global_region.add_locations(global_region_locations)

    # Crafting
    # global_region_locations = get_location_names_with_ids(["Craft: Tool Handle",
    #                                                       "Craft: Flimsy Pickaxe",
    #                                                       "Craft: Flimsy Shovel",
    #                                                       "Craft: Flimsy Cutters",
    #                                                       "Craft: Fake Wall Block",
    #                                                       "Craft: Contraband Pouch",
    #                                                       "Craft: Bed Dummy"])
    # global_region.add_locations(global_region_locations)

    #Prison Specific Checks
    if world.options.center_perks:
        center_perks = world.get_region("Center Perks")
        temp_locations = ["Escape: Perimeter Breakout (Center Perks 2.0)", "Escape: Meet the Crew (Center Perks 2.0)"]
        for i in range (1, 35): temp_locations.append(f"Center Perks 2.0 Desk {i}")
        temp_locations.append("Center Perks 2.0 Contraband Desk")
        temp_locations.append("Center Perks 2.0 Cutlery Tray")
        center_perks_locations = get_location_names_with_ids(temp_locations)
        center_perks.add_locations(center_perks_locations, TheEscapists2Location)

    if world.options.rattlesnake_springs:
        rattlesnake_springs = world.get_region("Rattlesnake Springs")
        temp_locations = ["Escape: Perimeter Breakout (Rattlesnake Springs)","Escape: Zip It Up (Rattlesnake Springs)"]
        for i in range (1, 36): temp_locations.append(f"Rattlesnake Springs Desk {i}")
        temp_locations.append("Rattlesnake Springs Contraband Desk")
        temp_locations.append("Rattlesnake Springs Cutlery Tray")
        rattlesnake_springs_locations = get_location_names_with_ids(temp_locations)
        rattlesnake_springs.add_locations(rattlesnake_springs_locations, TheEscapists2Location)

    if world.options.kapow_camp:
        kapow_camp = world.get_region("KAPOW Camp")
        temp_locations = [ "Escape: Perimeter Breakout (K.A.P.O.W Camp)", "Escape: Speed McQueen (K.A.P.O.W Camp)"]
        for i in range (1, 25): temp_locations.append(f"K.A.P.O.W Camp Desk {i}")
        temp_locations.append("K.A.P.O.W Camp Contraband Desk")
        temp_locations.append("K.A.P.O.W Camp Cutlery Tray")
        kapow_camp_locations = get_location_names_with_ids(temp_locations)
        kapow_camp.add_locations(kapow_camp_locations, TheEscapists2Location)

    if world.options.hmp_offshore:
        hmp_offshore = world.get_region("HMP Offshore")
        temp_locations = ["Escape: Perimeter Breakout (H.M.P. Offshore)", "Escape: Swimming With Dolphins  (H.M.P. Offshore)", "Escape: Trash Talk  (H.M.P. Offshore)"]
        for i in range (1, 28): temp_locations.append(f"H.M.P. Offshore Desk {i}")
        temp_locations.append("H.M.P. Offshore Contraband Desk")
        temp_locations.append("H.M.P. Offshore Cutlery Tray")
        hmp_offshore_locations = get_location_names_with_ids(temp_locations)
        hmp_offshore.add_locations(hmp_offshore_locations, TheEscapists2Location)

    if world.options.fort_tundra:
        fort_tundra = world.get_region("Fort Tundra")
        temp_locations = ["Escape: Perimeter Breakout (Fort Tundra)", "Escape: Rock-hammer Hard Place (Fort Tundra)"]
        for i in range (1, 34): temp_locations.append(f"Fort Tundra Desk {i}")
        temp_locations.append("Fort Tundra Contraband Desk")
        temp_locations.append("Fort Tundra Cutlery Tray")
        fort_tundra_locations = get_location_names_with_ids(temp_locations)
        fort_tundra.add_locations(fort_tundra_locations, TheEscapists2Location)

    if world.options.area_17:
        area_17 = world.get_region("Area 17")
        temp_locations = ["Escape: Perimeter Breakout (Area 17)", "Escape: I'm Only Human (Area 17)"]
        for i in range (1, 28): temp_locations.append(f"Area 17 Desk {i}")
        temp_locations.append("Area 17 Contraband Desk")
        temp_locations.append("Area 17 Cutlery Tray")
        area_17_locations = get_location_names_with_ids(temp_locations)
        area_17.add_locations(area_17_locations, TheEscapists2Location)

    if world.options.uss_anomaly:
        uss_anomaly = world.get_region("USS Anomaly")
        temp_locations = ["Escape: Perimeter Breakout (U.S.S. Anomaly)", "Escape: Race From Space (U.S.S. Anomaly)"]
        for i in range (1, 27): temp_locations.append(f"U.S.S. Anomaly Desk {i}")
        temp_locations.append("U.S.S. Anomaly Contraband Desk")
        temp_locations.append("U.S.S. Anomaly Cutlery Tray")
        uss_anomaly_locations = get_location_names_with_ids(temp_locations)
        uss_anomaly.add_locations(uss_anomaly_locations, TheEscapists2Location)

    if world.options.cougar_creek_railroad:
        cougar_creek = world.get_region("Cougar Creek")
        temp_locations = ["Escape: My Little Phoney (Cougar Creek Railroad)", "Escape: Hooked On You (Cougar Creek Railroad)"]
        for i in range (1,9): temp_locations.append(f"Cougar Creek Railroad Desk {i}")
        cougar_creek_locations = get_location_names_with_ids(temp_locations)
        cougar_creek.add_locations(cougar_creek_locations, TheEscapists2Location)

    if world.options.hms_orca:
        hms_orca = world.get_region("HMS Orca")
        temp_locations = ["Escape: Scuba Doo (H.M.S. Orca)", "Escape: Wave Goodbye (H.M.S. Orca)"]
        for i in range (1, 15): temp_locations.append(f"H.M.S. Orca Desk {i}")
        hms_orca_locations = get_location_names_with_ids(temp_locations)
        hms_orca.add_locations(hms_orca_locations, TheEscapists2Location)

    if world.options.air_force_con:
        air_force_con = world.get_region("Air Force Con")
        temp_locations = ["Escape: Passport To Freedom (Air Force Con)", "Escape: Plane Crazy (Air Force Con)"]
        for i in range (1, 12): temp_locations.append(f"Air Force Con Desk {i}")
        air_force_con_locations = get_location_names_with_ids(temp_locations)
        air_force_con.add_locations(air_force_con_locations, TheEscapists2Location)

def create_events(world: TheEscapists2World) -> None:
    # This is being used to determine go mode
    if world.options.center_perks:
        center_perks = world.get_region("Center Perks")
        center_perks.add_event("CP2.0 PE", "Unique Escapes", location_type=TheEscapists2Location, item_type = items.TheEscapists2Item)
        center_perks.add_event("CP2.0 MTC", "Unique Escapes", location_type=TheEscapists2Location, item_type = items.TheEscapists2Item)

    if world.options.rattlesnake_springs:
        rattlesnake_springs = world.get_region("Rattlesnake Springs")
        rattlesnake_springs.add_event("RSS PE", "Unique Escapes", location_type=TheEscapists2Location, item_type=items.TheEscapists2Item)
        rattlesnake_springs.add_event("RSS ZIU", "Unique Escapes", location_type=TheEscapists2Location, item_type=items.TheEscapists2Item)

    if world.options.kapow_camp:
        kapow_camp = world.get_region("KAPOW Camp")
        kapow_camp.add_event("KAPOW PE", "Unique Escapes", location_type=TheEscapists2Location, item_type=items.TheEscapists2Item)
        kapow_camp.add_event("KAPOW SM", "Unique Escapes", location_type=TheEscapists2Location, item_type=items.TheEscapists2Item)

    if world.options.hmp_offshore:
        hmp_offshore = world.get_region("HMP Offshore")
        hmp_offshore.add_event("HMPOff PE", "Unique Escapes", location_type=TheEscapists2Location, item_type=items.TheEscapists2Item)
        hmp_offshore.add_event("HMPOff SWD", "Unique Escapes", location_type=TheEscapists2Location, item_type=items.TheEscapists2Item)
        hmp_offshore.add_event("HMPOff TT", "Unique Escapes", location_type=TheEscapists2Location, item_type=items.TheEscapists2Item)

    if world.options.fort_tundra:
        fort_tundra = world.get_region("Fort Tundra")
        fort_tundra.add_event("FT PE", "Unique Escapes", location_type=TheEscapists2Location, item_type=items.TheEscapists2Item)
        fort_tundra.add_event("FT RHHP", "Unique Escapes", location_type=TheEscapists2Location, item_type=items.TheEscapists2Item)

    if world.options.area_17:
        area_17 = world.get_region("Area 17")
        area_17.add_event("A17 PE", "Unique Escapes", location_type=TheEscapists2Location, item_type=items.TheEscapists2Item)
        area_17.add_event("A17 IOH", "Unique Escapes", location_type=TheEscapists2Location, item_type=items.TheEscapists2Item)

    if world.options.uss_anomaly:
        uss_anomaly = world.get_region("USS Anomaly")
        uss_anomaly.add_event("USSA PE", "Unique Escapes", location_type=TheEscapists2Location, item_type=items.TheEscapists2Item)
        uss_anomaly.add_event("USSA RFS", "Unique Escapes", location_type=TheEscapists2Location, item_type=items.TheEscapists2Item)

    if world.options.cougar_creek_railroad:
        cougar_creek_railroad = world.get_region("Cougar Creek")
        cougar_creek_railroad.add_event("CCR MLP", "Unique Escapes", location_type=TheEscapists2Location, item_type=items.TheEscapists2Item)
        cougar_creek_railroad.add_event("CCR HOY", "Unique Escapes", location_type=TheEscapists2Location, item_type=items.TheEscapists2Item)

    if world.options.hms_orca:
        hms_orca = world.get_region("HMS Orca")
        hms_orca.add_event("HMSO SD", "Unique Escapes", location_type=TheEscapists2Location, item_type=items.TheEscapists2Item)
        hms_orca.add_event("HMSO WG", "Unique Escapes", location_type=TheEscapists2Location, item_type=items.TheEscapists2Item)

    if world.options.air_force_con:
        air_force_con = world.get_region("Air Force Con")
        air_force_con.add_event("AFC PTF", "Unique Escapes", location_type=TheEscapists2Location, item_type=items.TheEscapists2Item)
        air_force_con.add_event("AFC PC", "Unique Escapes", location_type=TheEscapists2Location, item_type=items.TheEscapists2Item)
