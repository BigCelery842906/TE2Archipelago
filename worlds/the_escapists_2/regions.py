from BaseClasses import Region
from .locations import Escapists2Location, location_dictionary

def create_regions(multiworld, player: int, options):
    menu_region = Region("Menu", player, multiworld)
    multiworld.regions.append(menu_region)

    map_prefixes = {
        "Center Perks": ["80", "81", "Craft:", "Shop:", "Job:", "Milestone:", "Escape: Center", "Escape: Perimeter Breakout (Center Perks)", "Escape: Meet The Crew"],
        "Cougar Creek": ["Cougar Creek", "Escape: My Little", "Escape: Hooked"],
        "Rattlesnake": ["82"], 
        "KAPOW": ["83"],
        "HMS Orca": ["84"],
        "HMP Offshore": ["85"],
        "Fort Tundra": ["86"],
        "Area 17": ["87"],
        "Air Force Con": ["88"],
        "USS Anomaly": ["89"]
    }


    active_regions = {}
    if options.center_perks: active_regions["Center Perks"] = Region("Center Perks", player, multiworld)
    if options.cougar_creek: active_regions["Cougar Creek"] = Region("Cougar Creek", player, multiworld)
    if options.rattlesnake_springs: active_regions["Rattlesnake"] = Region("Rattlesnake", player, multiworld)
    if options.kapow_camp: active_regions["KAPOW"] = Region("KAPOW", player, multiworld)
    if options.hms_orca: active_regions["HMS Orca"] = Region("HMS Orca", player, multiworld)
    if options.hmp_offshore: active_regions["HMP Offshore"] = Region("HMP Offshore", player, multiworld)
    if options.fort_tundra: active_regions["Fort Tundra"] = Region("Fort Tundra", player, multiworld)
    if options.area_17: active_regions["Area 17"] = Region("Area 17", player, multiworld)
    if options.air_force_con: active_regions["Air Force Con"] = Region("Air Force Con", player, multiworld)
    if options.uss_anomaly: active_regions["USS Anomaly"] = Region("USS Anomaly", player, multiworld)

    for region_name, region_obj in active_regions.items():
        multiworld.regions.append(region_obj)
        menu_region.connect(region_obj)

        valid_prefixes = map_prefixes[region_name]
        for loc_name, loc_id in location_dictionary.items():
            if any(str(loc_id).startswith(prefix) or loc_name.startswith(prefix) for prefix in valid_prefixes):
                loc = Escapists2Location(player, loc_name, loc_id, region_obj)
                region_obj.locations.append(loc)
