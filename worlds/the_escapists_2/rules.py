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

def can_do_perimeter_breakout(world: TheEscapists2World) -> Has:
    items_for_40_intellect = get_items_required_for_stat_value(world, "Intellect", 40)
    items_for_50_intellect = get_items_required_for_stat_value(world, "Intellect", 50)
    items_for_60_intellect = get_items_required_for_stat_value(world, "Intellect", 60)
    items_for_70_intellect = get_items_required_for_stat_value(world, "Intellect", 70)

    CAN_DO_CHIP = (Has("Blueprint: Flimsy Pickaxe") & Has("Progressive Intellect", items_for_40_intellect)) | (Has( "Blueprint: Flimsy Shovel") & Has("Progressive Intellect", items_for_40_intellect)) | (Has( "Blueprint: Lightweight Pickaxe") & Has("Progressive Intellect", items_for_50_intellect)) | (Has( "Blueprint: Lightweight Shovel") & Has("Progressive Intellect", items_for_50_intellect)) | (Has( "Blueprint: Sturdy Pickaxe") & Has("Progressive Intellect", items_for_60_intellect)) | (Has( "Blueprint: Sturdy Shovel") & Has("Progressive Intellect", items_for_60_intellect)) | (Has( "Blueprint: Multitool") & Has("Progressive Intellect", items_for_70_intellect))
    CAN_DO_CUT = (Has("Blueprint: Flimsy Cutters") & Has("Progressive Intellect", items_for_40_intellect)) | (Has( "Blueprint: Lightweight Cutters") & Has("Progressive Intellect", items_for_50_intellect)) | (Has( "Blueprint: Sturdy Cutters") & Has("Progressive Intellect", items_for_60_intellect))
    CAN_DO_DIG = (Has("Blueprint: Flimsy Shovel") & Has("Progressive Intellect", items_for_40_intellect)) | (Has( "Blueprint: Flimsy Pickaxe") & Has("Progressive Intellect", items_for_40_intellect)) | (Has( "Blueprint: Lightweight Shovel") & Has("Progressive Intellect", items_for_50_intellect)) | (Has( "Blueprint: Lightweight Pickaxe") & Has("Progressive Intellect", items_for_50_intellect)) | (Has( "Blueprint: Sturdy Shovel") & Has("Progressive Intellect", items_for_60_intellect)) | (Has( "Blueprint: Sturdy Pickaxe") & Has("Progressive Intellect", items_for_60_intellect)) | (Has( "Blueprint: Multitool") & Has("Progressive Intellect", items_for_70_intellect))
    can_do_perimeter = CAN_DO_CHIP | CAN_DO_CUT | CAN_DO_DIG
    return can_do_perimeter

def can_do_cut(world: TheEscapists2World) -> Has:
    items_for_40_intellect = get_items_required_for_stat_value(world, "Intellect", 40)
    items_for_50_intellect = get_items_required_for_stat_value(world, "Intellect", 50)
    items_for_60_intellect = get_items_required_for_stat_value(world, "Intellect", 60)

    CAN_DO_CUT = (Has("Blueprint: Flimsy Cutters") & Has("Progressive Intellect", items_for_40_intellect)) | (Has("Blueprint: Lightweight Cutters") & Has("Progressive Intellect", items_for_50_intellect)) | (Has("Blueprint: Sturdy Cutters") & Has("Progressive Intellect", items_for_60_intellect))
    return CAN_DO_CUT

def has_guard_outfit(world: TheEscapists2World) -> Has:
    items_for_40_intellect = get_items_required_for_stat_value(world, "Intellect", 40)

    has_guard = Has("Blueprint: Guard Outfit") & Has("Progressive Intellect", items_for_40_intellect)
    return has_guard

def has_infirmary_outfit(world: TheEscapists2World) -> Has:
    items_for_50_intellect = get_items_required_for_stat_value(world, "Intellect", 50)

    has_infirmary = Has("Progressive Intellect", items_for_50_intellect)
    return has_infirmary

def has_red_key(world: TheEscapists2World) -> Has:
    items_for_60_intellect = get_items_required_for_stat_value(world, "Intellect", 60)

    has_red = Has("Progressive Intellect", items_for_60_intellect) & Has("Blueprint: Plastic Red Key") & Has("Blueprint: Key Mould Red")
    return has_red

def has_cyan_key(world: TheEscapists2World) -> Has:
    items_for_60_intellect = get_items_required_for_stat_value(world, "Intellect", 60)

    has_cyan = Has("Progressive Intellect", items_for_60_intellect) & Has("Blueprint: Plastic Cyan Key") & Has("Blueprint: Key Mould Cyan")
    return has_cyan

#TODO: CHECK IF REQUIRED BEFORE RELEASE
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

    if option_step == 0:
        return 0

    items_required = 0
    for i in range(30, 100, option_step):
        if i >= value_to_get:
            return items_required
        items_required += 1
    return items_required


def set_all_entrance_rules(world: TheEscapists2World) -> None:
    global max_escapes_possible
    max_escapes_possible = 0
    if world.options.center_perks:
        to_center_perks = world.get_entrance("Menu to Center Perks")
        world.set_rule(to_center_perks, Has(CP2_Unlock))
        max_escapes_possible += 2

        world.set_rule(world.get_location("CP2.0 PE"), can_do_perimeter_breakout(world))
        world.set_rule(world.get_location("Escape: Perimeter Breakout (Center Perks 2.0)"), can_do_perimeter_breakout(world))

        items_for_50_intellect = get_items_required_for_stat_value(world, "Intellect", 50)
        world.set_rule(world.get_location("Escape: Meet the Crew (Center Perks 2.0)"), Has("Blueprint: Fake Audio Equipment") & Has("Progressive Intellect", items_for_50_intellect))
        world.set_rule(world.get_location("CP2.0 MTC"), Has("Blueprint: Fake Audio Equipment") & Has("Progressive Intellect", items_for_50_intellect))

        world.set_rule(world.get_location("Center Perks 2.0 Desk 29"), has_infirmary_outfit(world))
        world.set_rule(world.get_location("Center Perks 2.0 Desk 30"), has_cyan_key(world))
        world.set_rule(world.get_location("Center Perks 2.0 Desk 31"), has_cyan_key(world))
        world.set_rule(world.get_location("Center Perks 2.0 Desk 32"), has_red_key(world))
        world.set_rule(world.get_location("Center Perks 2.0 Desk 33"), has_red_key(world))
        world.set_rule(world.get_location("Center Perks 2.0 Desk 34"), has_red_key(world))
        world.set_rule(world.get_location("Center Perks 2.0 Contraband Desk"), has_guard_outfit(world) & has_red_key(world))

    if world.options.rattlesnake_springs:
        to_rattlesnake_springs = world.get_entrance("Menu to Rattlesnake Springs")
        world.set_rule(to_rattlesnake_springs, Has(RSS_Unlock))
        max_escapes_possible += 2

        world.set_rule(world.get_location("Escape: Perimeter Breakout (Rattlesnake Springs)"), can_do_perimeter_breakout(world))
        world.set_rule(world.get_location("RSS PE"), can_do_perimeter_breakout(world))

        items_for_70_intellect = get_items_required_for_stat_value(world, "Intellect", 70)
        world.set_rule(world.get_location("Escape: Zip It Up (Rattlesnake Springs)"), Has("Blueprint: Complete Crossbow") & has_red_key(world) & Has("Progressive Intellect", items_for_70_intellect))
        world.set_rule(world.get_location("RSS ZIU"), Has("Blueprint: Complete Crossbow") & has_cyan_key(world) & Has("Progressive Intellect", items_for_70_intellect))

        world.set_rule(world.get_location("Rattlesnake Springs Desk 23"), has_infirmary_outfit(world))
        world.set_rule(world.get_location("Rattlesnake Springs Desk 24"), has_cyan_key(world))
        world.set_rule(world.get_location("Rattlesnake Springs Desk 25"), has_cyan_key(world))

        world.set_rule(world.get_location("Rattlesnake Springs Desk 26"), has_red_key(world))
        world.set_rule(world.get_location("Rattlesnake Springs Desk 27"), has_red_key(world))
        world.set_rule(world.get_location("Rattlesnake Springs Desk 28"), has_red_key(world))
        world.set_rule(world.get_location("Rattlesnake Springs Desk 29"), has_red_key(world))
        world.set_rule(world.get_location("Rattlesnake Springs Desk 30"), has_red_key(world))
        world.set_rule(world.get_location("Rattlesnake Springs Desk 31"), has_red_key(world))
        world.set_rule(world.get_location("Rattlesnake Springs Desk 32"), has_red_key(world))
        world.set_rule(world.get_location("Rattlesnake Springs Desk 33"), has_red_key(world))
        world.set_rule(world.get_location("Rattlesnake Springs Desk 34"), has_red_key(world))
        world.set_rule(world.get_location("Rattlesnake Springs Desk 35"), has_red_key(world))
        world.set_rule(world.get_location("Rattlesnake Springs Contraband Desk"), has_red_key(world))

    if world.options.kapow_camp:
        to_kapow_camp = world.get_entrance("Menu to Kapow Camp")
        world.set_rule(to_kapow_camp, Has(KAPOW_Unlock))
        max_escapes_possible += 2

        world.set_rule(world.get_location("Escape: Perimeter Breakout (K.A.P.O.W Camp)"), can_do_perimeter_breakout(world))
        world.set_rule(world.get_location("KAPOW PE"), can_do_perimeter_breakout(world))

        items_for_40_intellect = get_items_required_for_stat_value(world, "Intellect", 40)
        world.set_rule(world.get_location("Escape: Speed McQueen (K.A.P.O.W Camp)"), Has("Progressive Intellect", items_for_40_intellect) & Has("Blueprint: Makeshift Rocket Thruster") & Has("Blueprint: Makeshift Ladder"))
        world.set_rule(world.get_location("KAPOW SM"), Has("Progressive Intellect", items_for_40_intellect) & Has("Blueprint: Makeshift Rocket Thruster") & Has("Blueprint: Makeshift Ladder"))

        world.set_rule(world.get_location("K.A.P.O.W Camp Desk 19"), has_infirmary_outfit(world))
        world.set_rule(world.get_location("K.A.P.O.W Camp Desk 20"), Has("Blueprint: Makeshift Ladder"))
        world.set_rule(world.get_location("K.A.P.O.W Camp Desk 21"), has_cyan_key(world))
        world.set_rule(world.get_location("K.A.P.O.W Camp Desk 22"), has_cyan_key(world))

        world.set_rule(world.get_location("K.A.P.O.W Camp Desk 23"), has_red_key(world))
        world.set_rule(world.get_location("K.A.P.O.W Camp Desk 24"), has_red_key(world))
        world.set_rule(world.get_location("K.A.P.O.W Camp Contraband Desk"), has_red_key(world) & has_guard_outfit(world))


    if world.options.hmp_offshore:
        to_hmp_offshore = world.get_entrance("Menu to HMP Offshore")
        world.set_rule(to_hmp_offshore, Has(HMPOFF_Unlock))
        max_escapes_possible += 3

        world.set_rule(world.get_location("Escape: Perimeter Breakout (H.M.P. Offshore)"), can_do_perimeter_breakout(world))
        world.set_rule(world.get_location("HMPOff PE"), can_do_perimeter_breakout(world))

        items_for_70_intellect = get_items_required_for_stat_value(world, "Intellect", 70)
        world.set_rule(world.get_location("Escape: Swimming With Dolphins  (H.M.P. Offshore)"), Has("Progressive Intellect", items_for_70_intellect) & Has("Blueprint: Fishing Rod") & has_red_key(world))
        world.set_rule(world.get_location("HMPOff SWD"), Has("Progressive Intellect", items_for_70_intellect) & Has("Blueprint: Fishing Rod") & has_red_key(world))

        items_for_60_intellect = get_items_required_for_stat_value(world, "Intellect", 60)
        world.set_rule(world.get_location("Escape: Trash Talk  (H.M.P. Offshore)"), Has("Progressive Intellect", items_for_60_intellect) & Has("Blueprint: Breathable Trash Bag") & has_red_key(world))
        world.set_rule(world.get_location("HMPOff TT"), Has("Progressive Intellect", items_for_60_intellect) & Has("Blueprint: Breathable Trash Bag") & has_red_key(world))

        world.set_rule(world.get_location("H.M.P. Offshore Desk 18"), has_infirmary_outfit(world))
        world.set_rule(world.get_location("H.M.P. Offshore Desk 19"), has_cyan_key(world))
        world.set_rule(world.get_location("H.M.P. Offshore Desk 20"), has_cyan_key(world))
        world.set_rule(world.get_location("H.M.P. Offshore Desk 21"), has_cyan_key(world))
        world.set_rule(world.get_location("H.M.P. Offshore Desk 22"), has_cyan_key(world) & has_red_key(world))
        world.set_rule(world.get_location("H.M.P. Offshore Desk 23"), has_red_key(world))
        world.set_rule(world.get_location("H.M.P. Offshore Desk 24"), has_red_key(world))
        world.set_rule(world.get_location("H.M.P. Offshore Desk 25"), has_red_key(world))
        world.set_rule(world.get_location("H.M.P. Offshore Desk 26"), has_red_key(world))
        world.set_rule(world.get_location("H.M.P. Offshore Desk 27"), has_red_key(world))
        world.set_rule(world.get_location("H.M.P. Offshore Contraband Desk"), has_red_key(world) & has_guard_outfit(world))

    if world.options.fort_tundra:
        to_fort_tundra = world.get_entrance("Menu to Fort Tundra")
        world.set_rule(to_fort_tundra, Has(FT_Unlock))
        max_escapes_possible += 2

        world.set_rule(world.get_location("Escape: Perimeter Breakout (Fort Tundra)"), can_do_perimeter_breakout(world))
        world.set_rule(world.get_location("FT PE"), can_do_perimeter_breakout(world))

        items_for_70_intellect = get_items_required_for_stat_value(world, "Intellect", 70)
        world.set_rule(world.get_location("Escape: Rock-hammer Hard Place (Fort Tundra)"), can_do_cut(world) & Has("Progressive Intellect", items_for_70_intellect))
        world.set_rule(world.get_location("FT RHHP"), can_do_cut(world) & Has("Progressive Intellect", items_for_70_intellect)) #The Rock Hammer is acquired via a quest

        world.set_rule(world.get_location("Fort Tundra Desk 27"), has_infirmary_outfit(world))
        world.set_rule(world.get_location("Fort Tundra Desk 28"), has_cyan_key(world))
        world.set_rule(world.get_location("Fort Tundra Desk 29"), has_red_key(world))
        world.set_rule(world.get_location("Fort Tundra Desk 30"), has_red_key(world))
        world.set_rule(world.get_location("Fort Tundra Desk 31"), has_red_key(world))
        world.set_rule(world.get_location("Fort Tundra Desk 32"), has_red_key(world))
        world.set_rule(world.get_location("Fort Tundra Desk 33"), has_red_key(world))
        world.set_rule(world.get_location("Fort Tundra Contraband Desk"), has_red_key(world) & has_guard_outfit(world))

    if world.options.area_17:
        to_area_17 = world.get_entrance("Menu to Area 17")
        world.set_rule(to_area_17, Has(A17_Unlock))
        max_escapes_possible += 2

        world.set_rule(world.get_location("Escape: Perimeter Breakout (Area 17)"), can_do_perimeter_breakout(world))
        world.set_rule(world.get_location("A17 PE"), can_do_perimeter_breakout(world))

        items_for_60_intellect = get_items_required_for_stat_value(world, "Intellect", 60)
        world.set_rule(world.get_location("Escape: I'm Only Human (Area 17)"), Has("Progressive Intellect", items_for_60_intellect) & Has("Blueprint: Security Pass") & has_red_key(world) & has_cyan_key(world))
        world.set_rule(world.get_location("A17 IOH"), Has("Progressive Intellect", items_for_60_intellect) & Has("Blueprint: Security Pass") & has_red_key(world) & has_cyan_key(world))

        world.set_rule(world.get_location("Area 17 Desk 14"), has_infirmary_outfit(world))
        world.set_rule(world.get_location("Area 17 Desk 15"), has_cyan_key(world))
        world.set_rule(world.get_location("Area 17 Desk 16"), has_red_key(world))
        world.set_rule(world.get_location("Area 17 Desk 17"), has_red_key(world))
        world.set_rule(world.get_location("Area 17 Desk 18"), has_red_key(world))
        world.set_rule(world.get_location("Area 17 Desk 19"), has_red_key(world))
        world.set_rule(world.get_location("Area 17 Desk 20"), has_red_key(world))
        world.set_rule(world.get_location("Area 17 Desk 21"), has_red_key(world))
        world.set_rule(world.get_location("Area 17 Desk 22"), has_red_key(world))
        world.set_rule(world.get_location("Area 17 Desk 23"), has_red_key(world))
        world.set_rule(world.get_location("Area 17 Desk 24"), has_red_key(world))
        world.set_rule(world.get_location("Area 17 Desk 25"), has_red_key(world))
        world.set_rule(world.get_location("Area 17 Desk 26"), has_red_key(world))
        world.set_rule(world.get_location("Area 17 Desk 27"), has_red_key(world))
        world.set_rule(world.get_location("Area 17 Contraband Desk"), has_red_key(world) & has_guard_outfit(world))

    if world.options.uss_anomaly:
        to_uss_anomaly = world.get_entrance("Menu to USS Anomaly")
        world.set_rule(to_uss_anomaly, Has(USSA_Unlock))
        max_escapes_possible += 2

        world.set_rule(world.get_location("Escape: Perimeter Breakout (U.S.S. Anomaly)"), can_do_perimeter_breakout(world))
        world.set_rule(world.get_location("USSA PE"), can_do_perimeter_breakout(world))

        items_for_60_intellect = get_items_required_for_stat_value(world, "Intellect", 60)
        world.set_rule(world.get_location("Escape: Race From Space (U.S.S. Anomaly)"), Has("Progressive Intellect", items_for_60_intellect) & Has("Blueprint: Contraband Pouch") & has_red_key(world))
        world.set_rule(world.get_location("USSA RFS"), Has("Progressive Intellect", items_for_60_intellect) & Has("Blueprint: Contraband Pouch") & has_red_key(world))

        world.set_rule(world.get_location("U.S.S. Anomaly Desk 24"), can_do_cut(world))
        world.set_rule(world.get_location("U.S.S. Anomaly Desk 25"), has_cyan_key(world))
        world.set_rule(world.get_location("U.S.S. Anomaly Desk 26"), has_cyan_key(world))
        world.set_rule(world.get_location("U.S.S. Anomaly Contraband Desk"), has_red_key(world) & has_guard_outfit(world))

    if world.options.cougar_creek_railroad:
        to_cougar_creek = world.get_entrance("Menu to Cougar Creek")
        world.set_rule(to_cougar_creek, Has(CCR_Unlock))
        max_escapes_possible += 2

        items_for_30_intellect = get_items_required_for_stat_value(world, "Intellect", 30)
        world.set_rule(world.get_location("Escape: My Little Phoney (Cougar Creek Railroad)"), Has("Blueprint: Pretend Carrot") & Has("Progressive Intellect", items_for_30_intellect))
        world.set_rule(world.get_location("CCR MLP"), Has("Blueprint: Pretend Carrot") & Has("Progressive Intellect", items_for_30_intellect))

        items_for_70_intellect = get_items_required_for_stat_value(world, "Intellect", 70)
        world.set_rule(world.get_location("Escape: Hooked On You (Cougar Creek Railroad)"), Has("Blueprint: Grappling Hook") & Has("Progressive Intellect", items_for_70_intellect))
        world.set_rule(world.get_location("CCR HOY"), Has("Blueprint: Grappling Hook") & Has("Progressive Intellect", items_for_70_intellect))

    if world.options.hms_orca:
        to_hms_orca = world.get_entrance("Menu to HMS Orca")
        world.set_rule(to_hms_orca, Has(HMSO_Unlock))
        max_escapes_possible += 2

        items_for_60_intellect = get_items_required_for_stat_value(world, "Intellect", 60)
        world.set_rule(world.get_location("Escape: Scuba Doo (H.M.S. Orca)"), Has("Blueprint: Makeshift Breathing Apparatus") & Has("Progressive Intellect", items_for_60_intellect))
        world.set_rule(world.get_location("HMSO SD"), Has("Blueprint: Makeshift Breathing Apparatus") & Has("Progressive Intellect", items_for_60_intellect))

        #Escape: Wave Goodbye only needs access to orca (Nothing needs to be crafted)
        #Which also means the event does not need a set rule

    if world.options.air_force_con:
        to_air_force_con = world.get_entrance("Menu to Air Force Con")
        world.set_rule(to_air_force_con, Has(AFC_Unlock))
        max_escapes_possible += 2

        items_for_30_intellect = get_items_required_for_stat_value(world, "Intellect", 30)
        world.set_rule(world.get_location("Escape: Plane Crazy (Air Force Con)"), Has("Blueprint: Makeshift Harness") & Has("Blueprint: Parachute") & Has("Progressive Intellect", items_for_30_intellect))
        world.set_rule(world.get_location("AFC PC"), Has("Blueprint: Makeshift Harness") & Has("Blueprint: Parachute") & Has("Progressive Intellect", items_for_30_intellect))

        items_for_60_intellect = get_items_required_for_stat_value(world, "Intellect", 60)
        world.set_rule(world.get_location("Escape: Passport To Freedom (Air Force Con)"), Has("Blueprint: Energy Module") & Has("Progressive Intellect", items_for_60_intellect))
        world.set_rule(world.get_location("AFC PTF"), Has("Blueprint: Energy Module") & Has("Progressive Intellect", items_for_60_intellect))


def set_all_location_rules(world: TheEscapists2World) -> None:
#    logging.warning("Job locations currently disabled for fuzz testing. Please notify the dev (BigCelery842906) if you get this notification")
    if world.options.rattlesnake_springs or world.options.hmp_offshore:
        items_for_30_strength = get_items_required_for_stat_value(world, "Strength", 30)
        items_for_40_intellect = get_items_required_for_stat_value(world, "Intellect", 40)
        world.set_rule(world.get_location("Job: Woodwork"), HasAny(RSS_Unlock, HMPOFF_Unlock) & Has("Progressive Strength", items_for_30_strength) & Has("Progressive Intellect", items_for_40_intellect))

    if world.options.center_perks or world.options.rattlesnake_springs:
        items_for_40_strength = get_items_required_for_stat_value(world, "Strength", 40)
        items_for_80_intellect = get_items_required_for_stat_value(world, "Intellect", 80)
        world.set_rule(world.get_location("Job: Shoemaker"), HasAny(CP2_Unlock, RSS_Unlock) & Has("Progressive Strength", items_for_40_strength) & Has("Progressive Intellect", items_for_80_intellect))

    if world.options.hmp_offshore or world.options.fort_tundra or world.options.area_17:
        items_for_50_strength = get_items_required_for_stat_value(world, "Strength", 50)
        items_for_80_intellect = get_items_required_for_stat_value(world, "Intellect", 80)
        world.set_rule(world.get_location("Job: Blacksmith"), HasAny(HMPOFF_Unlock, FT_Unlock, A17_Unlock) & Has("Progressive Strength", items_for_50_strength) & Has("Progressive Intellect", items_for_80_intellect))

    if world.options.hmp_offshore or world.options.uss_anomaly:
        items_for_70_strength = get_items_required_for_stat_value(world, "Strength", 70)
        items_for_50_intellect = get_items_required_for_stat_value(world, "Intellect", 50)
        world.set_rule(world.get_location("Job: Mining"), HasAny(HMPOFF_Unlock, USSA_Unlock) & Has("Progressive Strength", items_for_70_strength) & Has("Progressive Intellect", items_for_50_intellect))

    if world.options.kapow_camp or world.options.fort_tundra or world.options.area_17:
        items_for_40_strength = get_items_required_for_stat_value(world, "Strength", 40)
        items_for_40_intellect = get_items_required_for_stat_value(world, "Intellect", 40)
        world.set_rule(world.get_location("Job: Plumbing"), HasAny(KAPOW_Unlock, FT_Unlock, A17_Unlock) & Has("Progressive Strength", items_for_40_strength) & Has("Progressive Intellect", items_for_40_intellect))

    if world.options.area_17 or world.options.uss_anomaly:
        items_for_30_strength = get_items_required_for_stat_value(world, "Strength", 30)
        items_for_80_intellect = get_items_required_for_stat_value(world, "Intellect", 80)
        world.set_rule(world.get_location("Job: Engineering"), HasAny(A17_Unlock, USSA_Unlock) & Has("Progressive Strength", items_for_30_strength) & Has("Progressive Intellect", items_for_80_intellect))

    if world.options.kapow_camp or world.options.uss_anomaly:
        items_for_30_strength = get_items_required_for_stat_value(world, "Strength", 30)
        items_for_40_intellect = get_items_required_for_stat_value(world, "Intellect", 40)
        world.set_rule(world.get_location("Job: Kitchen"), HasAny(KAPOW_Unlock, USSA_Unlock) & Has("Progressive Strength", items_for_30_strength) & Has("Progressive Intellect", items_for_40_intellect))
        items_for_30_intellect = get_items_required_for_stat_value(world, "Intellect", 30)
        world.set_rule(world.get_location("Job: Farming"), HasAny(KAPOW_Unlock, USSA_Unlock) & Has("Progressive Strength", items_for_30_strength) & Has("Progressive Intellect", items_for_30_intellect))

    if world.options.center_perks or world.options.rattlesnake_springs or world.options.area_17:
        items_for_60_strength = get_items_required_for_stat_value(world, "Strength", 60)
        items_for_30_intellect = get_items_required_for_stat_value(world, "Intellect", 30)
        world.set_rule(world.get_location("Job: Waste Disposal"), HasAny(CP2_Unlock, RSS_Unlock, A17_Unlock) & Has("Progressive Strength", items_for_60_strength) & Has("Progressive Intellect", items_for_30_intellect))

    if world.options.center_perks or world.options.kapow_camp:
        items_for_30_strength = get_items_required_for_stat_value(world, "Strength", 30)
        items_for_40_intellect = get_items_required_for_stat_value(world, "Intellect", 40)
        world.set_rule(world.get_location("Job: Mail Sorting"), HasAny(CP2_Unlock, KAPOW_Unlock) & Has("Progressive Strength", items_for_30_strength) & Has("Progressive Intellect", items_for_40_intellect))

    if world.options.hmp_offshore or world.options.fort_tundra:
        items_for_30_strength = get_items_required_for_stat_value(world, "Strength", 30)
        items_for_30_intellect = get_items_required_for_stat_value(world, "Intellect", 30)
        world.set_rule(world.get_location("Job: Canine Carer"), HasAny(HMPOFF_Unlock, FT_Unlock) & Has("Progressive Strength", items_for_30_strength) & Has("Progressive Intellect", items_for_30_intellect))

    if world.options.center_perks or world.options.rattlesnake_springs or world.options.fort_tundra:
        items_for_40_strength = get_items_required_for_stat_value(world, "Strength", 40)
        items_for_30_intellect = get_items_required_for_stat_value(world, "Intellect", 30)
        world.set_rule(world.get_location("Job: Painting"), HasAny(CP2_Unlock, RSS_Unlock, FT_Unlock) & Has("Progressive Strength", items_for_40_strength) & Has("Progressive Intellect", items_for_30_intellect))

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

        increment = world.options.intellect_step
        if increment != 0:
            temp_locations.append("Intellect Stat: Max")
            for i in range(30, 100, increment):
                temp_locations.append(f"Intellect Stat: {i}")

        for i in range(0, len(temp_locations)):
            world.set_rule(world.get_location(temp_locations[i]), HasAny(CP2_Unlock, RSS_Unlock, KAPOW_Unlock, HMPOFF_Unlock, FT_Unlock, A17_Unlock, USSA_Unlock))

def set_completion_condition(world: TheEscapists2World) -> None:
    yaml_unique_escapes_required = int(world.options.unique_escapes_required)
    if yaml_unique_escapes_required > max_escapes_possible:
        yaml_unique_escapes_required = max_escapes_possible
        logging.warning(f"The Escapists 2 - Slot {world.player_name} has too many required escapes, reducing to the max available given options provided (No action required)")
        world.options.unique_escapes_required.value = yaml_unique_escapes_required

    world.set_completion_rule(Has("Unique Escapes", count = yaml_unique_escapes_required))
