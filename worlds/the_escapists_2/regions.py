from __future__ import annotations
from typing import TYPE_CHECKING

from BaseClasses import Region

if TYPE_CHECKING:
    from .world import TheEscapists2World


# Regions should be each Prison

def create_and_connect_regions(world: TheEscapists2World) -> None:
    create_all_regions(world)
    create_regions(world)

def create_all_regions(world: TheEscapists2World) -> None:
    TE2regions = []

    newRegion = Region("Prison Select Menu", world.player, world.multiworld)
    TE2regions.append(newRegion)

    newRegion = Region("Global", world.player, world.multiworld)
    TE2regions.append(newRegion)

    if world.options.center_perks:        
        newRegion = Region("Center Perks", world.player, world.multiworld) 
        TE2regions.append(newRegion)
    if world.options.rattlesnake_springs: 
        newRegion = Region("Rattlesnake Springs", world.player, world.multiworld)
        TE2regions.append(newRegion)
    if world.options.kapow_camp:          
        newRegion = Region("KAPOW Camp", world.player, world.multiworld)
        TE2regions.append(newRegion)
    if world.options.hmp_offshore:        
        newRegion = Region("HMP Offshore", world.player, world.multiworld)
        TE2regions.append(newRegion)
    if world.options.fort_tundra:         
        newRegion = Region("Fort Tundra", world.player, world.multiworld)
        TE2regions.append(newRegion)
    if world.options.area_17:             
        newRegion = Region("Area 17", world.player, world.multiworld)
        TE2regions.append(newRegion)
    if world.options.uss_anomaly:         
        newRegion = Region("USS Anomaly", world.player, world.multiworld)
        TE2regions.append(newRegion)
        
    # Transport Prisons
    if world.options.cougar_creek:        
        newRegion = Region("Cougar Creek", world.player, world.multiworld)
        TE2regions.append(newRegion)
    if world.options.hms_orca:
        newRegion = Region("HMS Orca", world.player, world.multiworld)
        TE2regions.append(newRegion)
    if world.options.air_force_con:       
        newRegion = Region("Air Force Con", world.player, world.multiworld)
        TE2regions.append(newRegion)


    world.multiworld.regions += TE2regions

def create_regions(world: TheEscapists2World) -> None:
    prison_select_menu = world.get_region("Prison Select Menu")

    global_prison = world.get_region("Global")
    prison_select_menu.connect(global_prison, "Menu to Global")

    if world.options.center_perks:
        center_perks = world.get_region("Center Perks")
        prison_select_menu.connect(center_perks, "Menu to Center Perks")

    if world.options.rattlesnake_springs:
        rattlesnake_springs = world.get_region("Rattlesnake Springs")
        prison_select_menu.connect(rattlesnake_springs, "Menu to Rattlesnake Springs")

    if world.options.kapow_camp:
        kapow_camp = world.get_region("KAPOW Camp")
        prison_select_menu.connect(kapow_camp, "Menu to Kapow Camp")

    if world.options.hmp_offshore:
        hmp_offshore = world.get_region("HMP Offshore")
        prison_select_menu.connect(hmp_offshore, "Menu to HMP Offshore")

    if world.options.fort_tundra:
        fort_tundra = world.get_region("Fort Tundra")
        prison_select_menu.connect(fort_tundra, "Menu to Fort Tundra")

    if world.options.area_17:
        area_17 = world.get_region("Area 17")
        prison_select_menu.connect(area_17, "Menu to Area 17")

    if world.options.uss_anomaly:
        uss_anomaly = world.get_region("USS Anomaly")
        prison_select_menu.connect(uss_anomaly, "Menu to USS Anomaly")

    if world.options.cougar_creek:
        cougar_creek = world.get_region("Cougar Creek")
        prison_select_menu.connect(cougar_creek, "Menu to Cougar Creek")

    if world.options.hms_orca:
        hms_orca = world.get_region("HMS Orca")
        prison_select_menu.connect(hms_orca, "Menu to HMS Orca")

    if world.options.air_force_con:
        air_force_con = world.get_region("Air Force Con")
        prison_select_menu.connect(air_force_con, "Menu to Air Force Con")












