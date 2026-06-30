import time
import os
import getpass 
import pygame
from pygame.mixer import music as pymusic
import keyboard_receiver as controller
import file_handler as fH
import state_handler as stateH 
import player_actions as music_Control
from difflib import get_close_matches as fuzzymatch
import short_math as mycalc
import fuzzy_matcher

program_is_running = True
FPS = 60
FRAME_TIME = 1/FPS

user = getpass.getuser()
sourcefolder = rf"C:\Users\{user}\Mahou no Ongaku"
#define a pasta a ser usada e descobre o nome do usuário ativo

pygame.mixer.init()

player_state = {

    "mode" : "welcomescreen", #pode ser "playing", "paused", "menu", "stopped", "welcomescreen"
    "welcome_was_shown" : False

}

# IMPORT + VARIÁVEIS INICIAIS + PYGAME INIT

def welcome_screen():
    if not player_state["welcome_was_shown"]:
        print("WELCOME to Mahou no Ongaku, the True Music Player!")
        print("Press [ANY KEY] to continue!")

        player_state["welcome_was_shown"] = True

    anykey = controller.anykey_detector()
    if anykey:
        stateH.set_state_menu(player_state)
        player_state["welcome_was_shown"] = False


def quit_program():
    global program_is_running
    program_is_running = False
    return

def stopped():
    wannacontinue = input("What do you wanna do now?\nP = PLAY ANOTHER SONG\nL = LEAVE\n>")
    if wannacontinue.lower() == "l":
        quit_program()
    elif wannacontinue.lower() == "p":
        stateH.set_state_menu()
        return
        

def check_key_and_return(player_state):
    command = controller.command_detector()
    state = stateH.check_state(player_state)
   # print(command)
   # SPACEBAR
    if command == " ":
        if state == "playing":
            return "pause"
        elif state == "paused":
            return("unpause")
    elif command == "s":
            return("stop")


def in_song_mode(): #Vai rodar se o state for playing, e estiver tudo bonitinho, sem ninguém pausando nem nada
    ...




def deal_with_song_status():
    is_it_busy = pymusic.get_busy()
    check_key = check_key_and_return(player_state)
    state = stateH.check_state(player_state)

    if(state == "playing" and check_key == "pause"): #Spacebar
       music_Control.pause_song(player_state)
    
    elif(state == "paused" and check_key == "unpause"): #Spacebar
       music_Control.unpause_song(player_state) 
    
    elif(state in ("playing", "paused") and check_key == "stop"): #Música parando por comando do usuário
        print("Music Stopped.")
        music_Control.stop_song(player_state)

    elif(state == "playing" and not is_it_busy): #Música parou sozinha
        print("Song ended!")
        music_Control.stop_song(player_state)
    
    elif(state == "playing" and is_it_busy):
        in_song_mode()


# LIDAM COM CAMINHO DE MÚSICA 


def get_wanted_song_index(string_input):
        try:
            integer_input = (int(string_input) - 1)
            return integer_input
        except ValueError:
            return None
        

def get_closest_matches_list(string_input, chosenlist):
    string_input = string_input.lower()
    matcheslist = fuzzy_matcher.get_matches(string_input, chosenlist, number_of_matches=3)
    return matcheslist
        

def get_song_path():
    loaded_music_list = fH.turn_path_into_list(sourcefolder) #pega a pasta e lista as músicas
    fH.return_or_show_musiclist(loaded_music_list) #mostra a lista inicial
    songpath = None

    inputted = input("Type song number or name:\n>") #Motor da def: Acha o input do user

    try:
        wantedindex = int(inputted)
        wantedsong = loaded_music_list[wantedindex - 1]
        # print (wantedsong)
        songpath = os.path.join(sourcefolder, wantedsong)       #Se o input for número, já retorna um caminho pronto
        # print(songpath)
        return songpath
        
    except ValueError:

        list_that_matches_input = get_closest_matches_list(inputted, loaded_music_list)
        print("Based in your input, we found the following matches:")
        fH.return_or_show_musiclist(list_that_matches_input)            #se nao for int, acha as closematches da string
        secondinputted = input("Type song number or name:\n>")    #e faz uma nova lista, perguntando dnv qual o user quer
        
        try:
            wantedindex = int(secondinputted)
            wantedsong = list_that_matches_input[wantedindex - 1]
            print (wantedsong)
            songpath = os.path.join(sourcefolder, wantedsong)
            print(songpath)
            return songpath
        except Exception as error:
            print("Couldn't find the chosen song.", error)
            return None
        
def get_path_and_play():
    songpath = get_song_path()

    if songpath is None:
        return
    try:
        music_Control.play_song(songpath, player_state)
    except:
       return
    
#Se o caminho for válido, toca a música. Senão, manda uma mensagem de erro








def realtick(initial_time):
    final_time = initial_time + FRAME_TIME
    current_time = time.monotonic()
    remaining = final_time - current_time

    if remaining > 0:
        time.sleep(remaining)
        

def update():
    state = stateH.check_state(player_state)

    if state == "playing":
        deal_with_song_status()
    elif state == "menu":
        get_path_and_play()
    elif state == "stopped":
        stopped()
    elif state == "welcomescreen":
        welcome_screen()
#atualiza tudo, decide oq cada estado faz



while program_is_running:
    thistime = time.monotonic()
    update()
    realtick(thistime)



