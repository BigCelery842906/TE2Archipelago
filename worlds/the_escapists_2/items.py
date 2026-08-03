from BaseClasses import Item, ItemClassification
from typing import Dict

BASE_ITEM_ID = 80000

class Escapists2Item(Item):
    game: str = "The Escapists 2"

item_dictionary: Dict[str, dict] = {

    # ==========================================
    # === CUSTOM AP TRAPS                    ===
    # ==========================================
    "Trap: Max Heat": {"ingame_id": 90101, "ap_id": 90101, "classification": ItemClassification.trap},
    "Trap: Butterfingers": {"ingame_id": 90102, "ap_id": 90102, "classification": ItemClassification.trap},
    "Trap: Contraband Purge": {"ingame_id": 90103, "ap_id": 90103, "classification": ItemClassification.trap},

    # ==========================================
    # === PROGRESSION BLUEPRINTS (ESCAPES)   ===
    # ==========================================
    # Center Perks 2.0 / General
    "Blueprint: Fake Audio Equipment": {"ingame_id": 91182, "ap_id": 91182, "classification": ItemClassification.progression},
    "Blueprint: Civilian Clothes": {"ingame_id": 91136, "ap_id": 91136, "classification": ItemClassification.progression},
    
    # Cougar Creek
    "Blueprint: Fake Carrot": {"ingame_id": 91322, "ap_id": 91322, "classification": ItemClassification.progression},
    "Blueprint: Grappling Hook": {"ingame_id": 91210, "ap_id": 91210, "classification": ItemClassification.progression},
    
    # Rattlesnake Springs
    "Blueprint: Complete Crossbow": {"ingame_id": 91140, "ap_id": 91140, "classification": ItemClassification.progression},
    
    # KAPOW Camp
    "Blueprint: Makeshift Rocket Thruster": {"ingame_id": 91268, "ap_id": 91268, "classification": ItemClassification.progression},
    "Blueprint: Makeshift Ladder": {"ingame_id": 91265, "ap_id": 91265, "classification": ItemClassification.progression},
    
    # HMS Orca
    "Blueprint: Makeshift Breathing Apparatus": {"ingame_id": 91259, "ap_id": 91259, "classification": ItemClassification.progression},
    
    # Fort Tundra
    "Blueprint: Bed Dummy": {"ingame_id": 91113, "ap_id": 91113, "classification": ItemClassification.progression},
    "Blueprint: Guard Outfit": {"ingame_id": 91426, "ap_id": 91426, "classification": ItemClassification.progression},
    
    # Area 17
    "Blueprint: Security Pass": {"ingame_id": 91343, "ap_id": 91343, "classification": ItemClassification.progression},
    "Blueprint: Plastic Red Key": {"ingame_id": 91313, "ap_id": 91313, "classification": ItemClassification.progression},
    "Blueprint: Plastic Cyan Key": {"ingame_id": 91307, "ap_id": 91307, "classification": ItemClassification.progression},
    "Blueprint: Key Mould Red": {"ingame_id": 91420, "ap_id": 91420, "classification": ItemClassification.progression},
    "Blueprint: Key Mould Cyan": {"ingame_id": 91417, "ap_id": 91417, "classification": ItemClassification.progression},
    
    # Air Force Con
    "Blueprint: Makeshift Harness": {"ingame_id": 91264, "ap_id": 91264, "classification": ItemClassification.progression},
    "Blueprint: Parachute": {"ingame_id": 91300, "ap_id": 91300, "classification": ItemClassification.progression},
    
    # Utilities Required by Multiple Escapes
    "Blueprint: Lightweight Cutters": {"ingame_id": 91249, "ap_id": 91249, "classification": ItemClassification.progression},

    # ==========================================
    # === USEFUL BLUEPRINTS (TOOLS/COMBAT)   ===
    # ==========================================
    "Blueprint: Multitool": {"ingame_id": 91286, "ap_id": 91286, "classification": ItemClassification.useful},
    "Blueprint: Tool Handle": {"ingame_id": 91387, "ap_id": 91387, "classification": ItemClassification.useful},
    "Blueprint: Flimsy Pickaxe": {"ingame_id": 91193, "ap_id": 91193, "classification": ItemClassification.useful},
    "Blueprint: Lightweight Pickaxe": {"ingame_id": 91250, "ap_id": 91250, "classification": ItemClassification.useful},
    "Blueprint: Sturdy Pickaxe": {"ingame_id": 91371, "ap_id": 91371, "classification": ItemClassification.useful},
    "Blueprint: Flimsy Cutters": {"ingame_id": 91195, "ap_id": 91195, "classification": ItemClassification.useful},
    "Blueprint: Sturdy Cutters": {"ingame_id": 91370, "ap_id": 91370, "classification": ItemClassification.useful},
    "Blueprint: Flimsy Shovel": {"ingame_id": 91196, "ap_id": 91196, "classification": ItemClassification.useful},
    "Blueprint: Lightweight Shovel": {"ingame_id": 91251, "ap_id": 91251, "classification": ItemClassification.useful},
    "Blueprint: Sturdy Shovel": {"ingame_id": 91372, "ap_id": 91372, "classification": ItemClassification.useful},
    "Blueprint: Contraband Pouch": {"ingame_id": 91143, "ap_id": 91143, "classification": ItemClassification.useful},
    "Blueprint: Durable Contraband Pouch": {"ingame_id": 91175, "ap_id": 91175, "classification": ItemClassification.useful},
    "Blueprint: Fake Wall Block": {"ingame_id": 91187, "ap_id": 91187, "classification": ItemClassification.useful},
    "Blueprint: Fake Vent Cover": {"ingame_id": 91186, "ap_id": 91186, "classification": ItemClassification.useful},
    "Blueprint: Sheet Rope": {"ingame_id": 91459, "ap_id": 91459, "classification": ItemClassification.useful},
    "Blueprint: Timber Brace": {"ingame_id": 91384, "ap_id": 91384, "classification": ItemClassification.useful},
    "Blueprint: Super Metal Baton": {"ingame_id": 91377, "ap_id": 91377, "classification": ItemClassification.useful},
    "Blueprint: Super Knuckle Duster": {"ingame_id": 91376, "ap_id": 91376, "classification": ItemClassification.useful},
    "Blueprint: Super Whip": {"ingame_id": 91379, "ap_id": 91379, "classification": ItemClassification.useful},
    "Blueprint: Makeshift Stungun": {"ingame_id": 91271, "ap_id": 91271, "classification": ItemClassification.useful},
    "Blueprint: Gun Maker Kit": {"ingame_id": 91220, "ap_id": 91220, "classification": ItemClassification.useful},
    "Blueprint: Moulded Gun": {"ingame_id": 91284, "ap_id": 91284, "classification": ItemClassification.useful},
    "Blueprint: Fake Gun": {"ingame_id": 91184, "ap_id": 91184, "classification": ItemClassification.useful},

    # ==========================================
    # === PROGRESSION BASE MATERIALS         ===
    # ==========================================
    # These physical items are required for escapes, so they are progression.
    "DuctTape": {"ingame_id": 174, "ap_id": BASE_ITEM_ID + 174, "classification": ItemClassification.progression},
    "Timber": {"ingame_id": 382, "ap_id": BASE_ITEM_ID + 382, "classification": ItemClassification.progression},
    "File": {"ingame_id": 190, "ap_id": BASE_ITEM_ID + 190, "classification": ItemClassification.progression},
    "Wire": {"ingame_id": 405, "ap_id": BASE_ITEM_ID + 405, "classification": ItemClassification.progression},
    "WadOfPutty": {"ingame_id": 399, "ap_id": BASE_ITEM_ID + 399, "classification": ItemClassification.progression},
    "MoltenPlastic": {"ingame_id": 282, "ap_id": BASE_ITEM_ID + 282, "classification": ItemClassification.progression},
    "CircuitBoard": {"ingame_id": 135, "ap_id": BASE_ITEM_ID + 135, "classification": ItemClassification.progression},
    "EnergyModule": {"ingame_id": 178, "ap_id": BASE_ITEM_ID + 178, "classification": ItemClassification.progression},
    "Tubing": {"ingame_id": 393, "ap_id": BASE_ITEM_ID + 393, "classification": ItemClassification.progression},
    "Bolts": {"ingame_id": 117, "ap_id": BASE_ITEM_ID + 117, "classification": ItemClassification.progression},
    "Crowbar": {"ingame_id": 154, "ap_id": BASE_ITEM_ID + 154, "classification": ItemClassification.progression},
    "Screwdriver": {"ingame_id": 342, "ap_id": BASE_ITEM_ID + 342, "classification": ItemClassification.progression},
    "Feather": {"ingame_id": 189, "ap_id": BASE_ITEM_ID + 189, "classification": ItemClassification.progression},
    "JarOfInk": {"ingame_id": 237, "ap_id": BASE_ITEM_ID + 237, "classification": ItemClassification.progression},
    "BlankSecurityPass": {"ingame_id": 115, "ap_id": BASE_ITEM_ID + 115, "classification": ItemClassification.progression},
    "CyanKey": {"ingame_id": 160, "ap_id": BASE_ITEM_ID + 160, "classification": ItemClassification.progression},
    "RedKey": {"ingame_id": 335, "ap_id": BASE_ITEM_ID + 335, "classification": ItemClassification.progression},
    "JetPack": {"ingame_id": 238, "ap_id": BASE_ITEM_ID + 238, "classification": ItemClassification.progression},

    # ==========================================
    # === USEFUL BASE MATERIALS & ITEMS      ===
    # ==========================================
    "SheetOfMetal": {"ingame_id": 346, "ap_id": BASE_ITEM_ID + 346, "classification": ItemClassification.useful},
    "AdrenalineShot": {"ingame_id": 100, "ap_id": BASE_ITEM_ID + 100, "classification": ItemClassification.useful},
    "EnergyDrink": {"ingame_id": 177, "ap_id": BASE_ITEM_ID + 177, "classification": ItemClassification.useful},
    "Medicine": {"ingame_id": 274, "ap_id": BASE_ITEM_ID + 274, "classification": ItemClassification.useful},
    "Medikit": {"ingame_id": 275, "ap_id": BASE_ITEM_ID + 275, "classification": ItemClassification.useful},
    "Lighter": {"ingame_id": 248, "ap_id": BASE_ITEM_ID + 248, "classification": ItemClassification.useful},
    "Battery": {"ingame_id": 110, "ap_id": BASE_ITEM_ID + 110, "classification": ItemClassification.useful},
    "Bleach": {"ingame_id": 116, "ap_id": BASE_ITEM_ID + 116, "classification": ItemClassification.useful},

    # ==========================================
    # === THE JUNK (FILLER)                  ===
    # ==========================================
    # These items exist to ensure the AP Server has enough items to fill all the desks.
    "Soap": {"ingame_id": 356, "ap_id": BASE_ITEM_ID + 356, "classification": ItemClassification.filler},
    "Comb": {"ingame_id": 137, "ap_id": BASE_ITEM_ID + 137, "classification": ItemClassification.filler},
    "Toothpaste": {"ingame_id": 390, "ap_id": BASE_ITEM_ID + 390, "classification": ItemClassification.filler},
    "Toothbrush": {"ingame_id": 388, "ap_id": BASE_ITEM_ID + 388, "classification": ItemClassification.filler},
    "ToiletPaper": {"ingame_id": 386, "ap_id": BASE_ITEM_ID + 386, "classification": ItemClassification.filler},
    "Dirt": {"ingame_id": 166, "ap_id": BASE_ITEM_ID + 166, "classification": ItemClassification.filler},
    "Sock": {"ingame_id": 359, "ap_id": BASE_ITEM_ID + 359, "classification": ItemClassification.filler},
    "Magazine": {"ingame_id": 255, "ap_id": BASE_ITEM_ID + 255, "classification": ItemClassification.filler},
    "Book": {"ingame_id": 421, "ap_id": BASE_ITEM_ID + 421, "classification": ItemClassification.filler},
    "PlayingCards": {"ingame_id": 319, "ap_id": BASE_ITEM_ID + 319, "classification": ItemClassification.filler}, # Poster
    "Foil": {"ingame_id": 198, "ap_id": BASE_ITEM_ID + 198, "classification": ItemClassification.filler},
    "PaperClip": {"ingame_id": 298, "ap_id": BASE_ITEM_ID + 298, "classification": ItemClassification.filler},
    "RubberGloves": {"ingame_id": 339, "ap_id": BASE_ITEM_ID + 339, "classification": ItemClassification.filler},
    "TalcumPowder": {"ingame_id": 380, "ap_id": BASE_ITEM_ID + 380, "classification": ItemClassification.filler},
    "Nails": {"ingame_id": 289, "ap_id": BASE_ITEM_ID + 289, "classification": ItemClassification.filler},
    "Mug": {"ingame_id": 285, "ap_id": BASE_ITEM_ID + 285, "classification": ItemClassification.filler},
    "PlasticSpoon": {"ingame_id": 314, "ap_id": BASE_ITEM_ID + 314, "classification": ItemClassification.filler},
    "PlasticFork": {"ingame_id": 308, "ap_id": BASE_ITEM_ID + 308, "classification": ItemClassification.filler},
    "PlasticKnife": {"ingame_id": 311, "ap_id": BASE_ITEM_ID + 311, "classification": ItemClassification.filler},
    "TeaBag": {"ingame_id": 381, "ap_id": BASE_ITEM_ID + 381, "classification": ItemClassification.filler},
    "Sugar": {"ingame_id": 373, "ap_id": BASE_ITEM_ID + 373, "classification": ItemClassification.filler},
    "Milk": {"ingame_id": 278, "ap_id": BASE_ITEM_ID + 278, "classification": ItemClassification.filler},
    "Cookie (RIP Muffin)": {"ingame_id": 145, "ap_id": BASE_ITEM_ID + 145, "classification": ItemClassification.filler},
    "Chocolate": {"ingame_id": 133, "ap_id": BASE_ITEM_ID + 133, "classification": ItemClassification.filler},
    "BalsaWood": {"ingame_id": 104, "ap_id": BASE_ITEM_ID + 104, "classification": ItemClassification.filler},
    "ArtBrush": {"ingame_id": 102, "ap_id": BASE_ITEM_ID + 102, "classification": ItemClassification.filler},
    "ArtPaints": {"ingame_id": 103, "ap_id": BASE_ITEM_ID + 103, "classification": ItemClassification.filler},
    "Sheet": {"ingame_id": 345, "ap_id": BASE_ITEM_ID + 345, "classification": ItemClassification.filler},
    "Pillow": {"ingame_id": 303, "ap_id": BASE_ITEM_ID + 303, "classification": ItemClassification.filler},
    "PillowCase": {"ingame_id": 304, "ap_id": BASE_ITEM_ID + 304, "classification": ItemClassification.filler},
    "InmateOutfit": {"ingame_id": 235, "ap_id": BASE_ITEM_ID + 235, "classification": ItemClassification.filler}
}

item_names = list(item_dictionary.keys())
