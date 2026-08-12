from __future__ import annotations
from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import TheEscapists2World


ITEM_NAME_TO_ID = {
    # --- PROGRESSION ITEMS
    "Blueprint: Fake Audio Equipment": 1,
    "Blueprint: Civilian Clothes": 2,

    "Blueprint: Fake Carrot": 3,
    "Blueprint: Grappling Hook": 4,

    "Blueprint: Complete Crossbow": 5,

    "Blueprint: Makeshift Rocket Thruster": 6,
    "Blueprint: Makeshift Ladder": 7,

    "Blueprint: Makeshift Breathing Apparatus": 8,

    "Blueprint: Bed Dummy": 9,
    "Blueprint: Guard Outfit": 10,

    "Blueprint: Security Pass": 11,
    "Blueprint: Plastic Red Key": 12,
    "Blueprint: Plastic Cyan Key": 13,
    "Blueprint: Key Mould Red": 14,
    "Blueprint: Key Mould Cyan": 15,
    "Blueprint: Makeshift Harness": 16,
    "Blueprint: Parachute": 17,
    "Blueprint: Lightweight Cutters": 18,

    # --- PRISON UNLOCKS
    "Center Perks 2.0 Prison Unlock": 19,
    "Rattlesnake Springs Prison Unlock": 20,
    "K.A.P.O.W Camp Prison Unlock": 21,
    "H.M.P. Offshore Prison Unlock": 22,
    "Fort Tundra Prison Unlock": 23,
    "Area 17 Prison Unlock": 24,
    "U.S.S. Anomaly Prison Unlock": 25,
    "Cougar Creek Railroad Prison Unlock": 26,
    "H.M.S. Orca Prison Unlock": 27,
    "Air Force Con Prison Unlock": 28,


    # --- USEFUL ITEMS
    "Blueprint: Multitool": 29,
    "Blueprint: Tool Handle": 30,
    "Blueprint: Flimsy Pickaxe": 31,
    "Blueprint: Lightweight Pickaxe": 32,
    "Blueprint: Sturdy Pickaxe": 33,
    "Blueprint: Flimsy Cutters": 34,
    "Blueprint: Sturdy Cutters": 35,
    "Blueprint: Flimsy Shovel": 36,
    "Blueprint: Lightweight Shovel": 37,
    "Blueprint: Sturdy Shovel": 38,
    "Blueprint: Contraband Pouch": 39,
    "Blueprint: Durable Contraband Pouch": 40,
    "Blueprint: Fake Wall Block": 41,
    "Blueprint: Fake Vent Cover": 42,
    "Blueprint: Sheet Rope": 43,
    "Blueprint: Timber Brace": 44,
    "Blueprint: Super Metal Baton": 45,
    "Blueprint: Super Knuckle Duster": 46,
    "Blueprint: Super Whip": 47,
    "Blueprint: Makeshift Stungun": 48,
    "Blueprint: Gun Maker Kit": 49,
    "Blueprint: Moulded Gun": 50,
    "Blueprint: Fake Gun": 51,

    # --- PROGRESSIVE STATS - Start at 235
    "Progressive Strength": 235,
    "Progressive Stamina": 236,
    "Progressive Intellect": 237,
    # "Unique Escapes": 238,

    # --- TRAPS - Starting from 240
    "Max Heat Trap": 240,
    "Cell Search Trap": 241,
    "Lockdown Trap": 242,
    "Butterfingers Trap": 243,
    # "Contraband Purge Trap": 244,

    # --- FILLER/JUNK - Starting from 250
    "Soap": 250,
    "Comb": 251,
    "Toothpaste": 252,
    "Toothbrush": 253,
    "ToiletPaper": 254,
    "Dirt": 255,
    "Sock": 256,
    "Magazine": 257,
    "Book": 258,
    "PlayingCards": 259,
    "Foil": 260,
    "PaperClip": 261,
    "RubberGloves": 262,
    "TalcumPowder": 263,
    "Nails": 264,
    "Mug": 265,
    "PlasticSpoon": 266,
    "PlasticFork": 267,
    "PlasticKnife": 268,
    "TeaBag": 269,
    "Sugar": 270,
    "Milk": 271,
    "Cookie": 272,
    "Chocolate": 273,
    "BalsaWood": 274,
    "ArtBrush": 275,
    "ArtPaints": 276,
    "Sheet": 277,
    "Pillow": 278,
    "PillowCase": 279,
    "InmateOutfit": 280,
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    # --- PROGRESSION ITEMS
    "Blueprint: Fake Audio Equipment": ItemClassification.progression,
    "Blueprint: Civilian Clothes": ItemClassification.progression,

    "Blueprint: Fake Carrot": ItemClassification.progression,
    "Blueprint: Grappling Hook": ItemClassification.progression,

    "Blueprint: Complete Crossbow": ItemClassification.progression,

    "Blueprint: Makeshift Rocket Thruster": ItemClassification.progression,
    "Blueprint: Makeshift Ladder": ItemClassification.progression,

    "Blueprint: Makeshift Breathing Apparatus": ItemClassification.progression,

    "Blueprint: Bed Dummy": ItemClassification.progression,
    "Blueprint: Guard Outfit": ItemClassification.progression,

    "Blueprint: Security Pass": ItemClassification.progression,
    "Blueprint: Plastic Red Key": ItemClassification.progression,
    "Blueprint: Plastic Cyan Key": ItemClassification.progression,
    "Blueprint: Key Mould Red": ItemClassification.progression,
    "Blueprint: Key Mould Cyan": ItemClassification.progression,
    "Blueprint: Makeshift Harness": ItemClassification.progression,
    "Blueprint: Parachute": ItemClassification.progression,
    "Blueprint: Lightweight Cutters": ItemClassification.progression,

    # --- PRISON UNLOCKS
    "Center Perks 2.0 Prison Unlock": ItemClassification.progression,
    "Rattlesnake Springs Prison Unlock": ItemClassification.progression,
    "K.A.P.O.W Camp Prison Unlock": ItemClassification.progression,
    "H.M.P. Offshore Prison Unlock": ItemClassification.progression,
    "Fort Tundra Prison Unlock": ItemClassification.progression,
    "Area 17 Prison Unlock": ItemClassification.progression,
    "U.S.S. Anomaly Prison Unlock": ItemClassification.progression,
    "Cougar Creek Railroad Prison Unlock": ItemClassification.progression,
    "H.M.S. Orca Prison Unlock": ItemClassification.progression,
    "Air Force Con Prison Unlock": ItemClassification.progression,

    # --- PROGRESSIVE STATS
    "Progressive Strength": ItemClassification.progression,
    "Progressive Stamina": ItemClassification.progression,
    "Progressive Intellect": ItemClassification.progression,

    # --- USEFUL ITEMS
    "Blueprint: Multitool": ItemClassification.useful,
    "Blueprint: Tool Handle": ItemClassification.useful,
    "Blueprint: Flimsy Pickaxe": ItemClassification.useful,
    "Blueprint: Lightweight Pickaxe": ItemClassification.useful,
    "Blueprint: Sturdy Pickaxe": ItemClassification.useful,
    "Blueprint: Flimsy Cutters": ItemClassification.useful,
    "Blueprint: Sturdy Cutters": ItemClassification.useful,
    "Blueprint: Flimsy Shovel": ItemClassification.useful,
    "Blueprint: Lightweight Shovel": ItemClassification.useful,
    "Blueprint: Sturdy Shovel": ItemClassification.useful,
    "Blueprint: Contraband Pouch": ItemClassification.useful,
    "Blueprint: Durable Contraband Pouch": ItemClassification.useful,
    "Blueprint: Fake Wall Block": ItemClassification.useful,
    "Blueprint: Fake Vent Cover": ItemClassification.useful,
    "Blueprint: Sheet Rope": ItemClassification.useful,
    "Blueprint: Timber Brace": ItemClassification.useful,
    "Blueprint: Super Metal Baton": ItemClassification.useful,
    "Blueprint: Super Knuckle Duster": ItemClassification.useful,
    "Blueprint: Super Whip": ItemClassification.useful,
    "Blueprint: Makeshift Stungun": ItemClassification.useful,
    "Blueprint: Gun Maker Kit": ItemClassification.useful,
    "Blueprint: Moulded Gun": ItemClassification.useful,
    "Blueprint: Fake Gun": ItemClassification.useful,

    # --- TRAPS
    "Max Heat Trap": ItemClassification.trap,
    "Cell Search Trap": ItemClassification.trap,
    "Lockdown Trap": ItemClassification.trap,
    "Butterfingers Trap": ItemClassification.trap,
    # "Contraband Purge Trap": ItemClassification.trap,

    # --- FILLER/JUNK
    "Soap": ItemClassification.filler,
    "Comb": ItemClassification.filler,
    "Toothpaste": ItemClassification.filler,
    "Toothbrush": ItemClassification.filler,
    "ToiletPaper": ItemClassification.filler,
    "Dirt": ItemClassification.filler,
    "Sock": ItemClassification.filler,
    "Magazine": ItemClassification.filler,
    "Book": ItemClassification.filler,
    "PlayingCards": ItemClassification.filler,
    "Foil": ItemClassification.filler,
    "PaperClip": ItemClassification.filler,
    "RubberGloves": ItemClassification.filler,
    "TalcumPowder": ItemClassification.filler,
    "Nails": ItemClassification.filler,
    "Mug": ItemClassification.filler,
    "PlasticSpoon": ItemClassification.filler,
    "PlasticFork": ItemClassification.filler,
    "PlasticKnife": ItemClassification.filler,
    "TeaBag": ItemClassification.filler,
    "Sugar": ItemClassification.filler,
    "Milk": ItemClassification.filler,
    "Cookie": ItemClassification.filler,
    "Chocolate": ItemClassification.filler,
    "BalsaWood": ItemClassification.filler,
    "ArtBrush": ItemClassification.filler,
    "ArtPaints": ItemClassification.filler,
    "Sheet": ItemClassification.filler,
    "Pillow": ItemClassification.filler,
    "PillowCase": ItemClassification.filler,
    "InmateOutfit": ItemClassification.filler,
}

class TheEscapists2Item(Item):
    game = "The Escapists 2"

def get_random_filler_item_name(world: TheEscapists2World) -> str:

    #TODO: Actually set these as random
    if world.random.randint(0, 99) < world.options.trap_chance:
        return "Max Heat Trap" #Temp set trap

    return "Soap" #Also temp

def create_item_with_correct_classification(world: TheEscapists2World, name: str) -> TheEscapists2Item:
    classificaion = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return TheEscapists2Item(name, classificaion, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: TheEscapists2World) -> None:

    itempool: list[Item] = []
    validPrisonUnlocks = []
    if world.options.center_perks:
        validPrisonUnlocks.append("Center Perks 2.0 Prison Unlock")
        itempool.append(world.create_item("Center Perks 2.0 Prison Unlock"))
        itempool.append(world.create_item("Blueprint: Fake Audio Equipment"))
        itempool.append(world.create_item("Blueprint: Civilian Clothes"))
    if world.options.rattlesnake_springs:
        validPrisonUnlocks.append("Rattlesnake Springs Prison Unlock")
        itempool.append(world.create_item("Rattlesnake Springs Prison Unlock"))
        itempool.append(world.create_item("Blueprint: Complete Crossbow"))
    if world.options.kapow_camp:
        validPrisonUnlocks.append("K.A.P.O.W Camp Prison Unlock")
        itempool.append(world.create_item( "K.A.P.O.W Camp Prison Unlock"))
        itempool.append(world.create_item("Blueprint: Makeshift Rocket Thruster"))
        itempool.append(world.create_item("Blueprint: Makeshift Ladder"))
    if world.options.hmp_offshore:
        validPrisonUnlocks.append("H.M.P Offshore Prison Unlock")
        itempool.append(world.create_item("H.M.P. Offshore Prison Unlock"))
    if world.options.fort_tundra:
        validPrisonUnlocks.append("Fort Tundra Prison Unlock")
        itempool.append(world.create_item("Fort Tundra Prison Unlock"))
        itempool.append(world.create_item("Blueprint: Bed Dummy"))
        itempool.append(world.create_item("Blueprint: Guard Outfit"))
    if world.options.area_17:
        validPrisonUnlocks.append("Area 17 Prison Unlock")
        itempool.append(world.create_item("Area 17 Prison Unlock"))
        itempool.append(world.create_item("Blueprint: Security Pass"))
        itempool.append(world.create_item("Blueprint: Plastic Red Key"))
        itempool.append(world.create_item("Blueprint: Plastic Cyan Key"))
        itempool.append(world.create_item("Blueprint: Key Mould Red"))
        itempool.append(world.create_item("Blueprint: Key Mould Cyan"))
    if world.options.uss_anomaly:
        validPrisonUnlocks.append("U.S.S. Anomaly Prison Unlock")
        itempool.append(world.create_item("U.S.S. Anomaly Prison Unlock"))
    if world.options.cougar_creek:
        validPrisonUnlocks.append("Cougar Creek Railroad Prison Unlock")
        itempool.append(world.create_item("Cougar Creek Railroad Prison Unlock"))
        itempool.append(world.create_item("Blueprint: Fake Carrot"))
        itempool.append(world.create_item("Blueprint: Grappling Hook"))
    if world.options.hms_orca:
        validPrisonUnlocks.append("H.M.S. Orca Prison Unlock")
        itempool.append(world.create_item("H.M.S. Orca Prison Unlock"))
        itempool.append(world.create_item("Blueprint: Makeshift Breathing Apparatus"))
    if world.options.air_force_con:
        validPrisonUnlocks.append("Air Force Con Prison Unlock")
        itempool.append(world.create_item("Air Force Con Prison Unlock"))
        itempool.append(world.create_item("Blueprint: Makeshift Harness"))
        itempool.append(world.create_item("Blueprint: Parachute"))

        # Stats
        increment = world.options.strength_step
        for i in range(30, 100, increment):
            itempool.append(world.create_item("Progressive Strength"))

        increment = world.options.stamina_step
        for i in range(30, 100, increment):
            itempool.append(world.create_item("Progressive Stamina"))

        increment = world.options.intellect_step
        for i in range(30, 100, increment):
            itempool.append(world.create_item("Progressive Intellect"))

      #  for i in range(0, world.options.unique_escapes_required):
      #      itempool.append(world.create_item("Unique Escapes"))

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool

    starting_prison_unlock = world.create_item(validPrisonUnlocks[world.random.randint(0, len(validPrisonUnlocks) - 1)])
    world.push_precollected(starting_prison_unlock)