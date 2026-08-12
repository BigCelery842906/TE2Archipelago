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

    # Crafting
    "Craft: Tool Handle": BASE_LOCATION_ID + 10,
    "Craft: Flimsy Pickaxe": BASE_LOCATION_ID + 11,
    "Craft: Flimsy Shovel": BASE_LOCATION_ID + 12,
    "Craft: Flimsy Cutters": BASE_LOCATION_ID + 13,
    "Craft: Fake Wall Block": BASE_LOCATION_ID + 14,
    "Craft: Contraband Pouch": BASE_LOCATION_ID + 15,
    "Craft: Bed Dummy": BASE_LOCATION_ID + 16,

    #TODO: Check these to see if I put them here or not
    #"Craft: Fake Carrot": BASE_LOCATION_ID + 17,
    #"Craft: Grappling Hook": BASE_LOCATION_ID + 18,

    #Stat Milestones
    # 200 for strength, 300 for stamina, 400 for intellect

    # Strength Stat
    "Strength Stat: 30": BASE_LOCATION_ID + 200 + 30,
    "Strength Stat: 31": BASE_LOCATION_ID + 200 + 31,
    "Strength Stat: 32": BASE_LOCATION_ID + 200 + 32,
    "Strength Stat: 33": BASE_LOCATION_ID + 200 + 33,
    "Strength Stat: 34": BASE_LOCATION_ID + 200 + 34,
    "Strength Stat: 35": BASE_LOCATION_ID + 200 + 35,
    "Strength Stat: 36": BASE_LOCATION_ID + 200 + 36,
    "Strength Stat: 37": BASE_LOCATION_ID + 200 + 37,
    "Strength Stat: 38": BASE_LOCATION_ID + 200 + 38,
    "Strength Stat: 39": BASE_LOCATION_ID + 200 + 39,
    "Strength Stat: 40": BASE_LOCATION_ID + 200 + 40,
    "Strength Stat: 41": BASE_LOCATION_ID + 200 + 41,
    "Strength Stat: 42": BASE_LOCATION_ID + 200 + 42,
    "Strength Stat: 43": BASE_LOCATION_ID + 200 + 43,
    "Strength Stat: 44": BASE_LOCATION_ID + 200 + 44,
    "Strength Stat: 45": BASE_LOCATION_ID + 200 + 45,
    "Strength Stat: 46": BASE_LOCATION_ID + 200 + 46,
    "Strength Stat: 47": BASE_LOCATION_ID + 200 + 47,
    "Strength Stat: 48": BASE_LOCATION_ID + 200 + 48,
    "Strength Stat: 49": BASE_LOCATION_ID + 200 + 49,
    "Strength Stat: 50": BASE_LOCATION_ID + 200 + 50,
    "Strength Stat: 51": BASE_LOCATION_ID + 200 + 51,
    "Strength Stat: 52": BASE_LOCATION_ID + 200 + 52,
    "Strength Stat: 53": BASE_LOCATION_ID + 200 + 53,
    "Strength Stat: 54": BASE_LOCATION_ID + 200 + 54,
    "Strength Stat: 55": BASE_LOCATION_ID + 200 + 55,
    "Strength Stat: 56": BASE_LOCATION_ID + 200 + 56,
    "Strength Stat: 57": BASE_LOCATION_ID + 200 + 57,
    "Strength Stat: 58": BASE_LOCATION_ID + 200 + 58,
    "Strength Stat: 59": BASE_LOCATION_ID + 200 + 59,
    "Strength Stat: 60": BASE_LOCATION_ID + 200 + 60,
    "Strength Stat: 61": BASE_LOCATION_ID + 200 + 61,
    "Strength Stat: 62": BASE_LOCATION_ID + 200 + 62,
    "Strength Stat: 63": BASE_LOCATION_ID + 200 + 63,
    "Strength Stat: 64": BASE_LOCATION_ID + 200 + 64,
    "Strength Stat: 65": BASE_LOCATION_ID + 200 + 65,
    "Strength Stat: 66": BASE_LOCATION_ID + 200 + 66,
    "Strength Stat: 67": BASE_LOCATION_ID + 200 + 67,
    "Strength Stat: 68": BASE_LOCATION_ID + 200 + 68,
    "Strength Stat: 69": BASE_LOCATION_ID + 200 + 69,
    "Strength Stat: 70": BASE_LOCATION_ID + 200 + 70,
    "Strength Stat: 71": BASE_LOCATION_ID + 200 + 71,
    "Strength Stat: 72": BASE_LOCATION_ID + 200 + 72,
    "Strength Stat: 73": BASE_LOCATION_ID + 200 + 73,
    "Strength Stat: 74": BASE_LOCATION_ID + 200 + 74,
    "Strength Stat: 75": BASE_LOCATION_ID + 200 + 75,
    "Strength Stat: 76": BASE_LOCATION_ID + 200 + 76,
    "Strength Stat: 77": BASE_LOCATION_ID + 200 + 77,
    "Strength Stat: 78": BASE_LOCATION_ID + 200 + 78,
    "Strength Stat: 79": BASE_LOCATION_ID + 200 + 79,
    "Strength Stat: 80": BASE_LOCATION_ID + 200 + 80,
    "Strength Stat: 81": BASE_LOCATION_ID + 200 + 81,
    "Strength Stat: 82": BASE_LOCATION_ID + 200 + 82,
    "Strength Stat: 83": BASE_LOCATION_ID + 200 + 83,
    "Strength Stat: 84": BASE_LOCATION_ID + 200 + 84,
    "Strength Stat: 85": BASE_LOCATION_ID + 200 + 85,
    "Strength Stat: 86": BASE_LOCATION_ID + 200 + 86,
    "Strength Stat: 87": BASE_LOCATION_ID + 200 + 87,
    "Strength Stat: 88": BASE_LOCATION_ID + 200 + 88,
    "Strength Stat: 89": BASE_LOCATION_ID + 200 + 89,
    "Strength Stat: 90": BASE_LOCATION_ID + 200 + 90,
    "Strength Stat: 91": BASE_LOCATION_ID + 200 + 91,
    "Strength Stat: 92": BASE_LOCATION_ID + 200 + 92,
    "Strength Stat: 93": BASE_LOCATION_ID + 200 + 93,
    "Strength Stat: 94": BASE_LOCATION_ID + 200 + 94,
    "Strength Stat: 95": BASE_LOCATION_ID + 200 + 95,
    "Strength Stat: 96": BASE_LOCATION_ID + 200 + 96,
    "Strength Stat: 97": BASE_LOCATION_ID + 200 + 97,
    "Strength Stat: 98": BASE_LOCATION_ID + 200 + 98,
    "Strength Stat: 99": BASE_LOCATION_ID + 200 + 99,
    "Strength Stat: Max": BASE_LOCATION_ID + 200,

    #Stamina
    "Stamina Stat: 30": BASE_LOCATION_ID + 300 + 30,
    "Stamina Stat: 31": BASE_LOCATION_ID + 300 + 31,
    "Stamina Stat: 32": BASE_LOCATION_ID + 300 + 32,
    "Stamina Stat: 33": BASE_LOCATION_ID + 300 + 33,
    "Stamina Stat: 34": BASE_LOCATION_ID + 300 + 34,
    "Stamina Stat: 35": BASE_LOCATION_ID + 300 + 35,
    "Stamina Stat: 36": BASE_LOCATION_ID + 300 + 36,
    "Stamina Stat: 37": BASE_LOCATION_ID + 300 + 37,
    "Stamina Stat: 38": BASE_LOCATION_ID + 300 + 38,
    "Stamina Stat: 39": BASE_LOCATION_ID + 300 + 39,
    "Stamina Stat: 40": BASE_LOCATION_ID + 300 + 40,
    "Stamina Stat: 41": BASE_LOCATION_ID + 300 + 41,
    "Stamina Stat: 42": BASE_LOCATION_ID + 300 + 42,
    "Stamina Stat: 43": BASE_LOCATION_ID + 300 + 43,
    "Stamina Stat: 44": BASE_LOCATION_ID + 300 + 44,
    "Stamina Stat: 45": BASE_LOCATION_ID + 300 + 45,
    "Stamina Stat: 46": BASE_LOCATION_ID + 300 + 46,
    "Stamina Stat: 47": BASE_LOCATION_ID + 300 + 47,
    "Stamina Stat: 48": BASE_LOCATION_ID + 300 + 48,
    "Stamina Stat: 49": BASE_LOCATION_ID + 300 + 49,
    "Stamina Stat: 50": BASE_LOCATION_ID + 300 + 50,
    "Stamina Stat: 51": BASE_LOCATION_ID + 300 + 51,
    "Stamina Stat: 52": BASE_LOCATION_ID + 300 + 52,
    "Stamina Stat: 53": BASE_LOCATION_ID + 300 + 53,
    "Stamina Stat: 54": BASE_LOCATION_ID + 300 + 54,
    "Stamina Stat: 55": BASE_LOCATION_ID + 300 + 55,
    "Stamina Stat: 56": BASE_LOCATION_ID + 300 + 56,
    "Stamina Stat: 57": BASE_LOCATION_ID + 300 + 57,
    "Stamina Stat: 58": BASE_LOCATION_ID + 300 + 58,
    "Stamina Stat: 59": BASE_LOCATION_ID + 300 + 59,
    "Stamina Stat: 60": BASE_LOCATION_ID + 300 + 60,
    "Stamina Stat: 61": BASE_LOCATION_ID + 300 + 61,
    "Stamina Stat: 62": BASE_LOCATION_ID + 300 + 62,
    "Stamina Stat: 63": BASE_LOCATION_ID + 300 + 63,
    "Stamina Stat: 64": BASE_LOCATION_ID + 300 + 64,
    "Stamina Stat: 65": BASE_LOCATION_ID + 300 + 65,
    "Stamina Stat: 66": BASE_LOCATION_ID + 300 + 66,
    "Stamina Stat: 67": BASE_LOCATION_ID + 300 + 67,
    "Stamina Stat: 68": BASE_LOCATION_ID + 300 + 68,
    "Stamina Stat: 69": BASE_LOCATION_ID + 300 + 69,
    "Stamina Stat: 70": BASE_LOCATION_ID + 300 + 70,
    "Stamina Stat: 71": BASE_LOCATION_ID + 300 + 71,
    "Stamina Stat: 72": BASE_LOCATION_ID + 300 + 72,
    "Stamina Stat: 73": BASE_LOCATION_ID + 300 + 73,
    "Stamina Stat: 74": BASE_LOCATION_ID + 300 + 74,
    "Stamina Stat: 75": BASE_LOCATION_ID + 300 + 75,
    "Stamina Stat: 76": BASE_LOCATION_ID + 300 + 76,
    "Stamina Stat: 77": BASE_LOCATION_ID + 300 + 77,
    "Stamina Stat: 78": BASE_LOCATION_ID + 300 + 78,
    "Stamina Stat: 79": BASE_LOCATION_ID + 300 + 79,
    "Stamina Stat: 80": BASE_LOCATION_ID + 300 + 80,
    "Stamina Stat: 81": BASE_LOCATION_ID + 300 + 81,
    "Stamina Stat: 82": BASE_LOCATION_ID + 300 + 82,
    "Stamina Stat: 83": BASE_LOCATION_ID + 300 + 83,
    "Stamina Stat: 84": BASE_LOCATION_ID + 300 + 84,
    "Stamina Stat: 85": BASE_LOCATION_ID + 300 + 85,
    "Stamina Stat: 86": BASE_LOCATION_ID + 300 + 86,
    "Stamina Stat: 87": BASE_LOCATION_ID + 300 + 87,
    "Stamina Stat: 88": BASE_LOCATION_ID + 300 + 88,
    "Stamina Stat: 89": BASE_LOCATION_ID + 300 + 89,
    "Stamina Stat: 90": BASE_LOCATION_ID + 300 + 90,
    "Stamina Stat: 91": BASE_LOCATION_ID + 300 + 91,
    "Stamina Stat: 92": BASE_LOCATION_ID + 300 + 92,
    "Stamina Stat: 93": BASE_LOCATION_ID + 300 + 93,
    "Stamina Stat: 94": BASE_LOCATION_ID + 300 + 94,
    "Stamina Stat: 95": BASE_LOCATION_ID + 300 + 95,
    "Stamina Stat: 96": BASE_LOCATION_ID + 300 + 96,
    "Stamina Stat: 97": BASE_LOCATION_ID + 300 + 97,
    "Stamina Stat: 98": BASE_LOCATION_ID + 300 + 98,
    "Stamina Stat: 99": BASE_LOCATION_ID + 300 + 99,
    "Stamina Stat: Max": BASE_LOCATION_ID + 300,

    # Intellect Stat
    "Intellect Stat: 30": BASE_LOCATION_ID + 400 + 30,
    "Intellect Stat: 31": BASE_LOCATION_ID + 400 + 31,
    "Intellect Stat: 32": BASE_LOCATION_ID + 400 + 32,
    "Intellect Stat: 33": BASE_LOCATION_ID + 400 + 33,
    "Intellect Stat: 34": BASE_LOCATION_ID + 400 + 34,
    "Intellect Stat: 35": BASE_LOCATION_ID + 400 + 35,
    "Intellect Stat: 36": BASE_LOCATION_ID + 400 + 36,
    "Intellect Stat: 37": BASE_LOCATION_ID + 400 + 37,
    "Intellect Stat: 38": BASE_LOCATION_ID + 400 + 38,
    "Intellect Stat: 39": BASE_LOCATION_ID + 400 + 39,
    "Intellect Stat: 40": BASE_LOCATION_ID + 400 + 40,
    "Intellect Stat: 41": BASE_LOCATION_ID + 400 + 41,
    "Intellect Stat: 42": BASE_LOCATION_ID + 400 + 42,
    "Intellect Stat: 43": BASE_LOCATION_ID + 400 + 43,
    "Intellect Stat: 44": BASE_LOCATION_ID + 400 + 44,
    "Intellect Stat: 45": BASE_LOCATION_ID + 400 + 45,
    "Intellect Stat: 46": BASE_LOCATION_ID + 400 + 46,
    "Intellect Stat: 47": BASE_LOCATION_ID + 400 + 47,
    "Intellect Stat: 48": BASE_LOCATION_ID + 400 + 48,
    "Intellect Stat: 49": BASE_LOCATION_ID + 400 + 49,
    "Intellect Stat: 50": BASE_LOCATION_ID + 400 + 50,
    "Intellect Stat: 51": BASE_LOCATION_ID + 400 + 51,
    "Intellect Stat: 52": BASE_LOCATION_ID + 400 + 52,
    "Intellect Stat: 53": BASE_LOCATION_ID + 400 + 53,
    "Intellect Stat: 54": BASE_LOCATION_ID + 400 + 54,
    "Intellect Stat: 55": BASE_LOCATION_ID + 400 + 55,
    "Intellect Stat: 56": BASE_LOCATION_ID + 400 + 56,
    "Intellect Stat: 57": BASE_LOCATION_ID + 400 + 57,
    "Intellect Stat: 58": BASE_LOCATION_ID + 400 + 58,
    "Intellect Stat: 59": BASE_LOCATION_ID + 400 + 59,
    "Intellect Stat: 60": BASE_LOCATION_ID + 400 + 60,
    "Intellect Stat: 61": BASE_LOCATION_ID + 400 + 61,
    "Intellect Stat: 62": BASE_LOCATION_ID + 400 + 62,
    "Intellect Stat: 63": BASE_LOCATION_ID + 400 + 63,
    "Intellect Stat: 64": BASE_LOCATION_ID + 400 + 64,
    "Intellect Stat: 65": BASE_LOCATION_ID + 400 + 65,
    "Intellect Stat: 66": BASE_LOCATION_ID + 400 + 66,
    "Intellect Stat: 67": BASE_LOCATION_ID + 400 + 67,
    "Intellect Stat: 68": BASE_LOCATION_ID + 400 + 68,
    "Intellect Stat: 69": BASE_LOCATION_ID + 400 + 69,
    "Intellect Stat: 70": BASE_LOCATION_ID + 400 + 70,
    "Intellect Stat: 71": BASE_LOCATION_ID + 400 + 71,
    "Intellect Stat: 72": BASE_LOCATION_ID + 400 + 72,
    "Intellect Stat: 73": BASE_LOCATION_ID + 400 + 73,
    "Intellect Stat: 74": BASE_LOCATION_ID + 400 + 74,
    "Intellect Stat: 75": BASE_LOCATION_ID + 400 + 75,
    "Intellect Stat: 76": BASE_LOCATION_ID + 400 + 76,
    "Intellect Stat: 77": BASE_LOCATION_ID + 400 + 77,
    "Intellect Stat: 78": BASE_LOCATION_ID + 400 + 78,
    "Intellect Stat: 79": BASE_LOCATION_ID + 400 + 79,
    "Intellect Stat: 80": BASE_LOCATION_ID + 400 + 80,
    "Intellect Stat: 81": BASE_LOCATION_ID + 400 + 81,
    "Intellect Stat: 82": BASE_LOCATION_ID + 400 + 82,
    "Intellect Stat: 83": BASE_LOCATION_ID + 400 + 83,
    "Intellect Stat: 84": BASE_LOCATION_ID + 400 + 84,
    "Intellect Stat: 85": BASE_LOCATION_ID + 400 + 85,
    "Intellect Stat: 86": BASE_LOCATION_ID + 400 + 86,
    "Intellect Stat: 87": BASE_LOCATION_ID + 400 + 87,
    "Intellect Stat: 88": BASE_LOCATION_ID + 400 + 88,
    "Intellect Stat: 89": BASE_LOCATION_ID + 400 + 89,
    "Intellect Stat: 90": BASE_LOCATION_ID + 400 + 90,
    "Intellect Stat: 91": BASE_LOCATION_ID + 400 + 91,
    "Intellect Stat: 92": BASE_LOCATION_ID + 400 + 92,
    "Intellect Stat: 93": BASE_LOCATION_ID + 400 + 93,
    "Intellect Stat: 94": BASE_LOCATION_ID + 400 + 94,
    "Intellect Stat: 95": BASE_LOCATION_ID + 400 + 95,
    "Intellect Stat: 96": BASE_LOCATION_ID + 400 + 96,
    "Intellect Stat: 97": BASE_LOCATION_ID + 400 + 97,
    "Intellect Stat: 98": BASE_LOCATION_ID + 400 + 98,
    "Intellect Stat: 99": BASE_LOCATION_ID + 400 + 99,
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
    "Escape: Perimeter Breakout (H.M.P Offshore)" : BASE_LOCATION_ID + 4000 + 100 + 1,
    "Escape: Swimming With Dolphins  (H.M.P Offshore)" : BASE_LOCATION_ID + 4000 + 100 + 2,
    "Escape: Trash Talk  (H.M.P Offshore)" : BASE_LOCATION_ID + 4000 + 100 + 3,

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

}

# --- DESKS FOR EACH PRISON

for i in range (1, 37): LOCATION_NAME_TO_ID[f"Center Perks 2.0 Desk {i}"] = BASE_LOCATION_ID + 1000 + i
for i in range(1, 39): LOCATION_NAME_TO_ID[f"Rattlesnake Springs Desk {i}"] = BASE_LOCATION_ID + 2000 + i
for i in range(1, 28): LOCATION_NAME_TO_ID[f"K.A.P.O.W Camp Desk {i}"] = BASE_LOCATION_ID + 3000 + i
for i in range(1, 35): LOCATION_NAME_TO_ID[f"H.M.P. Offshore Desk {i}"] = BASE_LOCATION_ID + 4000 + i
for i in range(1, 37): LOCATION_NAME_TO_ID[f"Fort Tundra Desk {i}"] = BASE_LOCATION_ID + 5000 + i
for i in range(1, 34): LOCATION_NAME_TO_ID[f"Area 17 Desk {i}"] = BASE_LOCATION_ID + 6000 + i
for i in range(1, 29): LOCATION_NAME_TO_ID[f"U.S.S. Anomaly Desk {i}"] = BASE_LOCATION_ID + 7000 + i

#TODO: Cougar Creek Railroad to double check
for i in range(1, 8): LOCATION_NAME_TO_ID[f"Cougar Creek Railroad Desk {i}"] = BASE_LOCATION_ID + 8000 + i
for i in range(1, 16): LOCATION_NAME_TO_ID[f"H.M.S. Orca Desk {i}"] = BASE_LOCATION_ID + 9000 + i
for i in range(1, 13): LOCATION_NAME_TO_ID[f"Air Force Con Desk {i}"] = BASE_LOCATION_ID + 10000 + i

class TheEscapists2Location(Location):
    game = "The Escapists 2"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: TheEscapists2World) -> None:
    create_regular_locations(world)
    # Don't think I have events that need to be created?
    create_events(world)

def create_regular_locations(world: TheEscapists2World) -> None:

    global_region = world.get_region("Global")

    #Stats

    increment = world.options.strength_step
    temp_locations = ["Strength Stat: Max", "Stamina Stat: Max", "Intellect Stat: Max"]
    for i in range(30, 100, increment):
        temp_locations.append(f"Strength Stat: {i}")

    increment = world.options.stamina_step
    for i in range(30, 100, increment):
        temp_locations.append(f"Stamina Stat: {i}")

    increment = world.options.intellect_step
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

    #Crafting
    global_region_locations = get_location_names_with_ids(["Craft: Tool Handle",
                                                           "Craft: Flimsy Pickaxe",
                                                           "Craft: Flimsy Shovel",
                                                           "Craft: Flimsy Cutters",
                                                           "Craft: Fake Wall Block",
                                                           "Craft: Contraband Pouch",
                                                           "Craft: Bed Dummy"])
    global_region.add_locations(global_region_locations)

    #Prison Specific Checks
    if world.options.center_perks:
        center_perks = world.get_region("Center Perks")
        temp_locations = ["Escape: Perimeter Breakout (Center Perks 2.0)", "Escape: Meet the Crew (Center Perks 2.0)"]
        for i in range (1, 37): temp_locations.append(f"Center Perks 2.0 Desk {i}")
        center_perks_locations = get_location_names_with_ids(temp_locations)
        center_perks.add_locations(center_perks_locations, TheEscapists2Location)

    if world.options.rattlesnake_springs:
        rattlesnake_springs = world.get_region("Rattlesnake Springs")
        temp_locations = ["Escape: Perimeter Breakout (Rattlesnake Springs)","Escape: Zip It Up (Rattlesnake Springs)"]
        for i in range (1, 39): temp_locations.append(f"Rattlesnake Springs Desk {i}")
        rattlesnake_springs_locations = get_location_names_with_ids(temp_locations)
        rattlesnake_springs.add_locations(rattlesnake_springs_locations, TheEscapists2Location)

    if world.options.kapow_camp:
        kapow_camp = world.get_region("KAPOW Camp")
        temp_locations = [ "Escape: Perimeter Breakout (K.A.P.O.W Camp)", "Escape: Speed McQueen (K.A.P.O.W Camp)"]
        for i in range (1, 28): temp_locations.append(f"K.A.P.O.W Camp Desk {i}")
        kapow_camp_locations = get_location_names_with_ids(temp_locations)
        kapow_camp.add_locations(kapow_camp_locations, TheEscapists2Location)

    if world.options.hmp_offshore:
        hmp_offshore = world.get_region("HMP Offshore")
        temp_locations = ["Escape: Perimeter Breakout (H.M.P Offshore)", "Escape: Swimming With Dolphins  (H.M.P Offshore)", "Escape: Trash Talk  (H.M.P Offshore)"]
        for i in range (1, 35): temp_locations.append(f"H.M.P. Offshore Desk {i}")
        hmp_offshore_locations = get_location_names_with_ids(temp_locations)
        hmp_offshore.add_locations(hmp_offshore_locations, TheEscapists2Location)

    if world.options.fort_tundra:
        fort_tundra = world.get_region("Fort Tundra")
        temp_locations = ["Escape: Perimeter Breakout (Fort Tundra)", "Escape: Rock-hammer Hard Place (Fort Tundra)"]
        for i in range (1, 37): temp_locations.append(f"Fort Tundra Desk {i}")
        fort_tundra_locations = get_location_names_with_ids(temp_locations)
        fort_tundra.add_locations(fort_tundra_locations, TheEscapists2Location)

    if world.options.area_17:
        area_17 = world.get_region("Area 17")
        temp_locations = ["Escape: Perimeter Breakout (Area 17)", "Escape: I'm Only Human (Area 17)"]
        for i in range (1, 34): temp_locations.append(f"Area 17 Desk {i}")
        area_17_locations = get_location_names_with_ids(temp_locations)
        area_17.add_locations(area_17_locations, TheEscapists2Location)

    if world.options.uss_anomaly:
        uss_anomaly = world.get_region("USS Anomaly")
        temp_locations = ["Escape: Perimeter Breakout (U.S.S. Anomaly)", "Escape: Race From Space (U.S.S. Anomaly)"]
        for i in range (1, 29): temp_locations.append(f"U.S.S. Anomaly Desk {i}")
        uss_anomaly_locations = get_location_names_with_ids(temp_locations)
        uss_anomaly.add_locations(uss_anomaly_locations, TheEscapists2Location)

    if world.options.cougar_creek:
        cougar_creek = world.get_region("Cougar Creek")
        temp_locations = ["Escape: My Little Phoney (Cougar Creek Railroad)", "Escape: Hooked On You (Cougar Creek Railroad)"]
        for i in range (1,8): temp_locations.append(f"Cougar Creek Railroad Desk {i}")
        cougar_creek_locations = get_location_names_with_ids(temp_locations)
        cougar_creek.add_locations(cougar_creek_locations, TheEscapists2Location)

    if world.options.hms_orca:
        hms_orca = world.get_region("HMS Orca")
        temp_locations = ["Escape: Scuba Doo (H.M.S. Orca)", "Escape: Wave Goodbye (H.M.S. Orca)"]
        for i in range (1, 16): temp_locations.append(f"H.M.S. Orca Desk {i}")
        hms_orca_locations = get_location_names_with_ids(temp_locations)
        hms_orca.add_locations(hms_orca_locations, TheEscapists2Location)

    if world.options.air_force_con:
        air_force_con = world.get_region("Air Force Con")
        temp_locations = ["Escape: Passport To Freedom (Air Force Con)", "Escape: Plane Crazy (Air Force Con)"]
        for i in range (1, 13): temp_locations.append(f"Air Force Con Desk {i}")
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

    if world.options.cougar_creek:
        cougar_creek = world.get_region("Cougar Creek")
        cougar_creek.add_event("CCR MLP", "Unique Escapes", location_type=TheEscapists2Location, item_type=items.TheEscapists2Item)
        cougar_creek.add_event("CCR HOY", "Unique Escapes", location_type=TheEscapists2Location, item_type=items.TheEscapists2Item)

    if world.options.hms_orca:
        hms_orca = world.get_region("HMS Orca")
        hms_orca.add_event("HMSO SD", "Unique Escapes", location_type=TheEscapists2Location, item_type=items.TheEscapists2Item)
        hms_orca.add_event("HMSO WG", "Unique Escapes", location_type=TheEscapists2Location, item_type=items.TheEscapists2Item)

    if world.options.air_force_con:
        air_force_con = world.get_region("Air Force Con")
        air_force_con.add_event("AFC PTF", "Unique Escapes", location_type=TheEscapists2Location, item_type=items.TheEscapists2Item)
        air_force_con.add_event("AFC PC", "Unique Escapes", location_type=TheEscapists2Location, item_type=items.TheEscapists2Item)
