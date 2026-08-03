from BaseClasses import Tutorial, ItemClassification
from worlds.AutoWorld import World
from .items import Escapists2Item, item_dictionary
from .locations import Escapists2Location, location_dictionary
from .regions import create_regions
from .rules import set_rules
from .options import Escapists2Options

class Escapists2World(World):
    """
    The Escapists 2 is a  prison escape simulator.
    """
    game = "The Escapists 2"
    topology_present = True 
    options_dataclass = Escapists2Options
    options: Escapists2Options

    item_name_to_id = {name: data["ap_id"] for name, data in item_dictionary.items()}
    location_name_to_id = location_dictionary

    def create_regions(self):
        create_regions(self.multiworld, self.player, self.options)

    def create_item(self, name: str) -> Escapists2Item:
        item_data = item_dictionary[name]
        return Escapists2Item(name, item_data["classification"], item_data["ap_id"], self.player)

    def create_items(self):
        item_pool = []
        
        guaranteed_names = [
            "Trap: Max Heat", "Trap: Butterfingers", "Trap: Contraband Purge",
            "Blueprint: Multitool", "Blueprint: Tool Handle", "Blueprint: Flimsy Pickaxe", 
            "Blueprint: Flimsy Cutters", "Blueprint: Flimsy Shovel", "Blueprint: Contraband Pouch"
        ]

        if self.options.center_perks:
            guaranteed_names.extend(["Blueprint: Fake Audio Equipment", "Blueprint: Civilian Clothes", "Broom", "DuctTape", "RadioReceiver"])
        if self.options.cougar_creek:
            guaranteed_names.extend(["Blueprint: Fake Carrot", "Blueprint: Grappling Hook"])
        if self.options.rattlesnake_springs:
            guaranteed_names.extend(["Blueprint: Plastic Red Key", "Blueprint: Complete Crossbow"])
        if self.options.kapow_camp:
            guaranteed_names.extend(["Blueprint: Makeshift Rocket Thruster", "Screwdriver", "Blueprint: Makeshift Ladder"])
        if self.options.hms_orca:
            guaranteed_names.extend(["Blueprint: Makeshift Breathing Apparatus", "Tubing", "Bolts"])
        if self.options.hmp_offshore:
            guaranteed_names.extend(["Blueprint: Plastic Red Key", "Crowbar", "SheetOfMetal", "Blueprint: Sheet Rope"])
        if self.options.fort_tundra:
            guaranteed_names.extend(["Blueprint: Guard Outfit", "Blueprint: Bed Dummy", "Blueprint: Lightweight Cutters"])
        if self.options.area_17:
            guaranteed_names.extend(["Blueprint: Plastic Red Key", "Blueprint: Plastic Cyan Key", "Blueprint: Key Mould Red", "Blueprint: Key Mould Cyan", "Blueprint: Security Pass", "JarOfInk", "Feather"])
        if self.options.air_force_con:
            guaranteed_names.extend(["CircuitBoard", "EnergyModule", "Screwdriver", "Blueprint: Makeshift Harness", "Blueprint: Parachute"])
        if self.options.uss_anomaly:
            guaranteed_names.extend(["JetPack", "EnergyModule", "Screwdriver"])

        for name in guaranteed_names:
            if name in item_dictionary:
                item_pool.append(self.create_item(name))

        filler_items = [name for name, data in item_dictionary.items() if data["classification"] == ItemClassification.filler]
        
        total_locations = len(self.multiworld.get_unfilled_locations(self.player))
        remaining_capacity = total_locations - len(item_pool)
        
        for _ in range(remaining_capacity):
            item_pool.append(self.create_item(self.multiworld.random.choice(filler_items)))
            
        self.multiworld.itempool += item_pool
        
    def set_rules(self):
        set_rules(self.multiworld, self.player, self.options)
