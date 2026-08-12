from __future__ import annotations
from typing import TYPE_CHECKING

from rule_builder.rules import Has, HasAny

if TYPE_CHECKING:
    from .world import TheEscapists2World


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

def set_all_entrance_rules(world: TheEscapists2World) -> None:
    if world.options.center_perks:
        to_center_perks = world.get_entrance("Menu to Center Perks")
        world.set_rule(to_center_perks, Has(CP2_Unlock))

    if world.options.rattlesnake_springs:
        to_rattlesnake_springs = world.get_entrance("Menu to Rattlesnake Springs")
        world.set_rule(to_rattlesnake_springs, Has(RSS_Unlock))

    if world.options.kapow_camp:
        to_kapow_camp = world.get_entrance("Menu to Kapow Camp")
        world.set_rule(to_kapow_camp, Has(KAPOW_Unlock))

    if world.options.hmp_offshore:
        to_hmp_offshore = world.get_entrance("Menu to HMP Offshore")
        world.set_rule(to_hmp_offshore, Has(HMPOFF_Unlock))

    if world.options.fort_tundra:
        to_fort_tundra = world.get_entrance("Menu to Fort Tundra")
        world.set_rule(to_fort_tundra, Has(FT_Unlock))

    if world.options.area_17:
        to_area_17 = world.get_entrance("Menu to Area 17")
        world.set_rule(to_area_17, Has(A17_Unlock))

    if world.options.uss_anomaly:
        to_uss_anomaly = world.get_entrance("Menu to USS Anomaly")
        world.set_rule(to_uss_anomaly, Has(USSA_Unlock))

    if world.options.cougar_creek:
        to_cougar_creek = world.get_entrance("Menu to Cougar Creek")
        world.set_rule(to_cougar_creek, Has(CCR_Unlock))

    if world.options.hms_orca:
        to_hms_orca = world.get_entrance("Menu to HMS Orca")
        world.set_rule(to_hms_orca, Has(HMSO_Unlock))

    if world.options.air_force_con:
        to_air_force_con = world.get_entrance("Menu to Air Force Con")
        world.set_rule(to_air_force_con, Has(AFC_Unlock))


def set_all_location_rules(world: TheEscapists2World) -> None:

    if world.options.rattlesnake_springs or world.options.hmp_offshore:
        world.set_rule(world.get_location("Job: Woodwork"), HasAny(CP2_Unlock, HMPOFF_Unlock))
    if world.options.center_perks or world.options.rattlesnake_springs:
        world.set_rule(world.get_location("Job: Shoemaker"), HasAny(CP2_Unlock, RSS_Unlock))
    if world.options.hmp_offshore or world.options.fort_tundra or world.options.area_17:
        world.set_rule(world.get_location("Job: Blacksmith"), HasAny(FT_Unlock, A17_Unlock))
    if world.options.hmp_offshore or world.options.uss_anomaly:
        world.set_rule(world.get_location("Job: Mining"), HasAny(HMPOFF_Unlock, USSA_Unlock))
    if world.options.kapow_camp or world.options.fort_tundra or world.options.area_17:
        world.set_rule(world.get_location("Job: Plumbing"), HasAny(KAPOW_Unlock, FT_Unlock, A17_Unlock))
    if world.options.area_17 or world.options.uss_anomaly:
        world.set_rule(world.get_location("Job: Engineering"), HasAny(A17_Unlock), USSA_Unlock)
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
    world.set_completion_rule(Has("Unique Escapes", count = int(world.options.unique_escapes_required)))