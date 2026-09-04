from dataclasses import dataclass
from Options import Toggle, PerGameCommonOptions, Range


class CenterPerks(Toggle):
    """Enable Center Perks 2.0 in the item pool"""
    display_name = "Center Perks 2.0"
    default = 1


class CougarCreek(Toggle):
    """Enable Cougar Creek Railroad in the item pool"""
    display_name = "Cougar Creek Railroad"
    default = 1


class RattlesnakeSprings(Toggle):
    """Enable Rattlesnake Springs in the item pool"""
    display_name = "Rattlesnake Springs"
    default = 0


class KAPOWCamp(Toggle):
    """Enable K.A.P.O.W Camp in the item pool"""
    display_name = "K.A.P.O.W Camp"
    default = 0


class HMSOrca(Toggle):
    """Enable H.M.S. Orca in the item pool"""
    display_name = "H.M.S. Orca"
    default = 0


class HMPOffshore(Toggle):
    """Enable H.M.P. Offshore in the item pool"""
    display_name = "H.M.P. Offshore"
    default = 0


class FortTundra(Toggle):
    """Enable Fort Tundra in the item pool"""
    display_name = "Fort Tundra"
    default = 0


class Area17(Toggle):
    """Enable Area 17 in the item pool"""
    display_name = "Area 17"
    default = 0


class AirForceCon(Toggle):
    """Enable Air Force Con in the item pool"""
    display_name = "Air Force Con"
    default = 0


class USSAnomaly(Toggle):
    """Enable U.S.S. Anomaly in the item pool"""
    display_name = "U.S.S. Anomaly"
    default = 0

class StrengthStep(Range):
    """How often you will send out a check for increasing your strength.
        This also changes how many Progressive Strength items you will need to receive for specific checks.
        0 Disables this option, and you will start with the Max"""
    display_name = "Strength Step"
    default = 10
    range_start = 0
    range_end = 100

class StaminaStep(Range):
    """How often you will send out a check for increasing your stamina.
        This also changes how many Progressive Stamina items you will need to receive for specific checks.
        0 Disables this option, and you will start with the Max"""
    display_name = "Stamina Step"
    default = 10
    range_start = 0
    range_end = 100

class IntellectStep(Range):
    """How often you will send out a check for increasing your intellect.
        This also changes how many Progressive Intellect items you will need to receive for specific checks.
        0 Disables this option, and you will start with the Max"""
    display_name = "Intellect Step"
    default = 10
    range_start = 0
    range_end = 100

class TrapChance(Range):
    """What percent of filler items are replaced with traps"""
    display_name = "Trap Chance"
    default = 5
    range_start = 0
    range_end = 100

class UniqueEscapesRequired(Range):
    """How many unique escapes you must make to goal.
    This will automatically reduce to the max escapes you can make with your selected prisons if you set a higher amount."""
    display_name = "Unique Escapes Required"
    default = 1
    range_start = 0
    range_end = 21

@dataclass
class TheEscapists2Options(PerGameCommonOptions):
    center_perks: CenterPerks
    cougar_creek_railroad: CougarCreek
    rattlesnake_springs: RattlesnakeSprings
    kapow_camp: KAPOWCamp
    hms_orca: HMSOrca
    hmp_offshore: HMPOffshore
    fort_tundra: FortTundra
    area_17: Area17
    air_force_con: AirForceCon
    uss_anomaly: USSAnomaly
    strength_step: StrengthStep
    stamina_step: StaminaStep
    intellect_step: IntellectStep
    trap_chance: TrapChance
    unique_escapes_required: UniqueEscapesRequired