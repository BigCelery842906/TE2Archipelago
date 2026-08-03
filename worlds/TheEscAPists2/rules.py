from BaseClasses import MultiWorld
from worlds.generic.Rules import set_rule

def set_rules(multiworld: MultiWorld, player: int, options):
    
    # Helper for generic perimeter breakouts (I add this and the whole things works, im really not sure why)
    def can_perimeter(state):
        return state.has("BedDummy", player) and state.has("FlimsyCutters", player)

    # === CENTER PERKS 2.0 ===
    if options.center_perks:
        try:
            set_rule(multiworld.get_location("Escape: Perimeter Breakout (Center Perks)", player), can_perimeter)
            set_rule(multiworld.get_location("Escape: Meet The Crew", player), lambda state: 
                state.has("CivilianClothes", player) and state.has("Blueprint: Fake Audio Equipment", player) and
                state.has("Broom", player) and state.has("DuctTape", player) and state.has("RadioReceiver", player))
        except KeyError: pass
    # === COUGAR CREEK RAILROAD ===
    if options.cougar_creek:
        try:
            set_rule(multiworld.get_location("Escape: My Little Phoney", player), lambda state: state.has("PretendCarrot", player))
            set_rule(multiworld.get_location("Escape: Hooked On You", player), lambda state: state.has("GrapplingHook", player))
        except KeyError: pass

    # === RATTLESNAKE SPRINGS ===
    if options.rattlesnake_springs:
        try:
            set_rule(multiworld.get_location("Escape: Perimeter Breakout (Rattlesnake)", player), can_perimeter)
            set_rule(multiworld.get_location("Escape: Zip It Up", player), lambda state: 
                state.has("CompleteCrossbow", player) and (state.has("RedKey", player) or state.has("Blueprint: Plastic Red Key", player)))
        except KeyError: pass

    # === K.A.P.O.W. CAMP ===
    if options.kapow_camp:
        try:
            set_rule(multiworld.get_location("Escape: Perimeter Breakout (KAPOW)", player), can_perimeter)
            set_rule(multiworld.get_location("Escape: Speed McQueen", player), lambda state: 
                state.has("MakeshiftRocketThruster", player) and state.has("MakeshiftLadder", player) and state.has("Screwdriver", player))
        except KeyError: pass

    # === H.M.S. ORCA ===
    if options.hms_orca:
        try:
            set_rule(multiworld.get_location("Escape: Scuba Doo", player), lambda state: state.has("MakeshiftBreathingApparatus", player))
            set_rule(multiworld.get_location("Escape: Wave Goodbye", player), lambda state: state.has("Tubing", player) and state.has("Bolts", player))
        except KeyError: pass

    # === HMP OFFSHORE ===
    if options.hmp_offshore:
        try:
            set_rule(multiworld.get_location("Escape: Perimeter Breakout (Offshore)", player), can_perimeter)
            set_rule(multiworld.get_location("Escape: Trash Talk", player), lambda state: 
                (state.has("RedKey", player) or state.has("Blueprint: Plastic Red Key", player)) and state.has("Crowbar", player) and state.has("BreathableTrashbag", player))
            set_rule(multiworld.get_location("Escape: Swimming With Dolphins", player), lambda state: 
                state.has("ReadiedFishingRod", player) and state.has("HowToSpeakDolphinBook", player) and state.has("Sugar", player) and state.has("Flour", player) and state.has("Milk", player))
        except KeyError: pass

    # === FORT TUNDRA ===
    if options.fort_tundra:
        try:
            set_rule(multiworld.get_location("Escape: Perimeter Breakout (Tundra)", player), can_perimeter)
            set_rule(multiworld.get_location("Escape: Rock-hammer Hard Place", player), lambda state: 
                state.has("RockHammer", player) and state.has("GuardOutfit", player) and state.has("BedDummy", player) and state.has("LightweightCutters", player))
        except KeyError: pass

    # === AREA 17 ===
    if options.area_17:
        try:
            set_rule(multiworld.get_location("Escape: Perimeter Breakout (Area 17)", player), can_perimeter)
            set_rule(multiworld.get_location("Escape: I'm Only Human", player), lambda state: 
                state.has("CivilianClothes", player) and state.has("SecurityPass", player) and 
                (state.has("CyanKey", player) or state.has("Blueprint: Plastic Cyan Key", player)) and
                (state.has("RedKey", player) or state.has("Blueprint: Plastic Red Key", player)))
        except KeyError: pass

    # === AIR FORCE CON ===
    if options.air_force_con:
        try:
            set_rule(multiworld.get_location("Escape: Passport To Freedom", player), lambda state: 
                state.has("CircuitBoard", player) and state.has("EnergyModule", player) and state.has("Screwdriver", player))
            set_rule(multiworld.get_location("Escape: Plane Crazy", player), lambda state: 
                state.has("BedSheetRed", player) and state.has("Rope", player, 3)) # Note: AP handles counts dynamically!
        except KeyError: pass

    # === U.S.S. ANOMALY ===
    if options.uss_anomaly:
        try:
            set_rule(multiworld.get_location("Escape: Perimeter Breakout (Anomaly)", player), can_perimeter)
            set_rule(multiworld.get_location("Escape: Race From Space", player), lambda state: 
                state.has("JetPack", player) and (
                    state.has("EnergyModule", player, 2) or 
                    state.has("Screwdriver", player) or 
                    state.has("Crowbar", player)
                )
            )
        except KeyError: pass
