
#STATE HANDLER!!!!!!!



def set_state_playing(player_state):
    player_state["mode"] = "playing"
def set_state_paused(player_state):
    player_state["mode"] = "paused"
def set_state_inmenu(player_state):
    player_state["mode"] = "menu"

def check_state(player_state):
    return player_state["mode"]