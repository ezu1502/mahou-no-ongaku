
#STATE HANDLER!!!!!!!



def set_state_playing(player_state):
    player_state["mode"] = "playing"
def set_state_paused(player_state):
    player_state["mode"] = "paused"
def set_state_menu(player_state):
    player_state["mode"] = "menu"
def set_state_stopped(player_state):
    player_state["mode"] = "stopped"
def set_state_welcome_screen(player_state):
    player_state["mode"] = "welcomescreen"




def check_state(player_state):
    return player_state["mode"]