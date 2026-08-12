from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World

from . import items, locations, regions, rules
from . import options as theescapists2_options


class TheEscapists2World(World):
    """The Escapists 2 is a prison simulation game where you are an inmate and must
    escape various prisons, varying in difficulty, by crafting, fighting and
    stealing to complete your objective"""

    game = "The Escapists 2"

    options_dataclass = theescapists2_options.TheEscapists2Options
    options: theescapists2_options.TheEscapists2Options

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Prison Select Menu"

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.TheEscapists2Item:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        # If you need access to the player's chosen options on the client side, there is a helper for that.
        return self.options.as_dict("center_perks", "cougar_creek", "rattlesnake_springs", "kapow_camp", "hms_orca", "hmp_offshore", "fort_tundra", "area_17", "air_force_con", "uss_anomaly", "strength_step", "stamina_step", "intellect_step", "unique_escapes_required")