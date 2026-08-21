from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from rule_builder.rules import Has, HasAny

if TYPE_CHECKING:
    from .world import TheEscapists2World

max_escapes_possible = 0

def set_all_rules(world: TheEscapists2World) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

CP2_Unlock = "Center Perks 2.0 Prison Unlock"
RSS_Unlock = "Rattlesnake Springs Prison Unlock"
KAPOW_Unlock = "K.A.P.O.W Camp Prison Unlock"
HMPOFF_Unlock = "H.M.P. Offshore Prison Unlock"
FT_Unlock = "Fort Tundra Prison Unlock"
A17_Unlock = "Area 17 Prison Unlock"
USSA_Unlock = "U.S.S. Anomaly Prison Unlock"
CCR_Unlock = "Cougar Creek Railroad Prison Unlock"
HMSO_Unlock = "H.M.S. Orca Prison Unlock"
AFC_Unlock = "Air Force Con Prison Unlock"

#TODO: THIS COULD BE WRONG, I MIGHT WANT TO BE CALCULATING HOW MANY ITEMS ARE REQUIRED TO HIT A VALUE
def get_current_stat_value(world: TheEscapists2World, state: CollectionState, stat_to_check) -> None:
    if stat_to_check == "Strength":
        option_step = world.options.strength_step
        progressive_item = "Progressive Strength"
    elif stat_to_check == "Stamina" :
        option_step = world.options.stamina_step
        progressive_item = "Progressive Stamina"
    elif stat_to_check == "Intellect":
        option_step = world.options.intellect_step
        progressive_item = "Progressive Intellect"
    else:
        raise KeyError("Stat Value check not valid, value provided did not match a stat type.")

    #TODO: Replace with this: https://alwaysintreble.github.io/Archipelago/baseclasses.html#BaseClasses.CollectionState.count_from_list
    num_of_progressives_received = state.count_from_list(progressive_item, world.player)

    current_stat_value = 30 + (num_of_progressives_received * option_step)

    if current_stat_value > 100:
        return 100

    else:
        return current_stat_value

def get_items_required_for_stat_value(world: TheEscapists2World, stat_to_check, value_to_get) -> int:
    if stat_to_check == "Strength":
        option_step = world.options.strength_step
    elif stat_to_check == "Stamina":
        option_step = world.options.stamina_step
    elif stat_to_check == "Intellect":
        option_step = world.options.intellect_step
    else:
        raise KeyError("Stat Value check not valid, value provided did not match a stat type. Can't return the items required for this stat value.")

    items_required = 0
    for i in range(30, 100, option_step):
        items_required += 1
        if i > value_to_get:
            return items_required
    return items_required


def set_all_entrance_rules(world: TheEscapists2World) -> None:
    global max_escapes_possible
    if world.options.center_perks:
        to_center_perks = world.get_entrance("Menu to Center Perks")
        world.set_rule(to_center_perks, Has(CP2_Unlock))
        max_escapes_possible += 2

        items_for_50_intellect = get_items_required_for_stat_value(world, "Intellect", 50)
        world.set_rule(world.get_location("Escape: Perimeter Breakout (Center Perks 2.0)"), Has("Blueprint: Civilian Clothes") & Has("Blueprint: Fake Audio Equipment") & Has("Progressive Intellect", items_for_50_intellect))

    if world.options.rattlesnake_springs:
        to_rattlesnake_springs = world.get_entrance("Menu to Rattlesnake Springs")
        world.set_rule(to_rattlesnake_springs, Has(RSS_Unlock))
        max_escapes_possible += 2

    if world.options.kapow_camp:
        to_kapow_camp = world.get_entrance("Menu to Kapow Camp")
        world.set_rule(to_kapow_camp, Has(KAPOW_Unlock))
        max_escapes_possible += 2

    if world.options.hmp_offshore:
        to_hmp_offshore = world.get_entrance("Menu to HMP Offshore")
        world.set_rule(to_hmp_offshore, Has(HMPOFF_Unlock))
        max_escapes_possible += 3

    if world.options.fort_tundra:
        to_fort_tundra = world.get_entrance("Menu to Fort Tundra")
        world.set_rule(to_fort_tundra, Has(FT_Unlock))
        max_escapes_possible += 2

    if world.options.area_17:
        to_area_17 = world.get_entrance("Menu to Area 17")
        world.set_rule(to_area_17, Has(A17_Unlock))
        max_escapes_possible += 2

    if world.options.uss_anomaly:
        to_uss_anomaly = world.get_entrance("Menu to USS Anomaly")
        world.set_rule(to_uss_anomaly, Has(USSA_Unlock))
        max_escapes_possible += 2

    if world.options.cougar_creek_railroad:
        to_cougar_creek = world.get_entrance("Menu to Cougar Creek")
        world.set_rule(to_cougar_creek, Has(CCR_Unlock))
        max_escapes_possible += 2

    if world.options.hms_orca:
        to_hms_orca = world.get_entrance("Menu to HMS Orca")
        world.set_rule(to_hms_orca, Has(HMSO_Unlock))
        max_escapes_possible += 2

    if world.options.air_force_con:
        to_air_force_con = world.get_entrance("Menu to Air Force Con")
        world.set_rule(to_air_force_con, Has(AFC_Unlock))
        max_escapes_possible += 2


def set_all_location_rules(world: TheEscapists2World) -> None:

    if world.options.rattlesnake_springs or world.options.hmp_offshore:
        world.set_rule(world.get_location("Job: Woodwork"), HasAny(RSS_Unlock, HMPOFF_Unlock))

    if world.options.center_perks or world.options.rattlesnake_springs:
        world.set_rule(world.get_location("Job: Shoemaker"), HasAny(CP2_Unlock, RSS_Unlock))

    if world.options.hmp_offshore or world.options.fort_tundra or world.options.area_17:
        world.set_rule(world.get_location("Job: Blacksmith"), HasAny(HMPOFF_Unlock, FT_Unlock, A17_Unlock))

    if world.options.hmp_offshore or world.options.uss_anomaly:
        world.set_rule(world.get_location("Job: Mining"), HasAny(HMPOFF_Unlock, USSA_Unlock))

    if world.options.kapow_camp or world.options.fort_tundra or world.options.area_17:
        world.set_rule(world.get_location("Job: Plumbing"), HasAny(KAPOW_Unlock, FT_Unlock, A17_Unlock))

    if world.options.area_17 or world.options.uss_anomaly:
        world.set_rule(world.get_location("Job: Engineering"), HasAny(A17_Unlock, USSA_Unlock))

    if world.options.kapow_camp or world.options.uss_anomaly:
        world.set_rule(world.get_location("Job: Kitchen"), HasAny(KAPOW_Unlock, USSA_Unlock))
        world.set_rule(world.get_location("Job: Farming"), HasAny(KAPOW_Unlock, USSA_Unlock))

    if world.options.center_perks or world.options.rattlesnake_springs or world.options.area_17:
        world.set_rule(world.get_location("Job: Waste Disposal"), HasAny(CP2_Unlock, RSS_Unlock, A17_Unlock))

    if world.options.center_perks or world.options.kapow_camp:
        world.set_rule(world.get_location("Job: Mail Sorting"), HasAny(CP2_Unlock, KAPOW_Unlock))

    if world.options.hmp_offshore or world.options.fort_tundra:
        world.set_rule(world.get_location("Job: Canine Carer"), HasAny(HMPOFF_Unlock, FT_Unlock))

    if world.options.center_perks or world.options.rattlesnake_springs or world.options.fort_tundra:
        world.set_rule(world.get_location("Job: Painting"), HasAny(CP2_Unlock, RSS_Unlock, FT_Unlock))

def set_completion_condition(world: TheEscapists2World) -> None:
    yaml_unique_escapes_required = int(world.options.unique_escapes_required)
    if yaml_unique_escapes_required > max_escapes_possible:
        yaml_unique_escapes_required = max_escapes_possible
        logging.warning(f"The Escapists 2 - Slot {world.player_name} has too many required escapes, reducing to the max available given options provided (No action required)")

    world.set_completion_rule(Has("Unique Escapes", count = yaml_unique_escapes_required))