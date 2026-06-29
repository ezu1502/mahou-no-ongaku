import time
import os
import getpass 
import pygame
from pygame.mixer import music as pymusic
import keyboard_receiver as controller
from file_handler import load_music_list, showmusiclist, get_song_full_path
from state_handler import set_state_inmenu, set_state_playing, set_state_paused, check_state
from player_actions import pause_song, play_song, stop_song, unpause_song
from difflib import get_close_matches as fuzzymatch
from rapidfuzz import process, fuzz

#import Player Controller


program_is_running = True
FPS = 60
FRAME_TIME = 1/FPS



user = getpass.getuser()
sourcefolder = rf"C:\Users\{user}\Mahou no Ongaku"
#define a pasta a ser usada e descobre o nome do usuário ativo

pygame.mixer.init()

player_state = {

    "mode" : "menu" #pode ser ""playing", "paused", "menu"
    
}


# IMPORT + VARIÁVEIS INICIAIS + PYGAME INIT


""" def askget_music_number():
    while True:
        try:
            chosenmusicnumber = int(input("Choose song number:\n>")) - 1
            return chosenmusicnumber
        except ValueError:
            print("Dumbass, type a number")
            continue """


def apply_fuzzymatching(text, loadedlist):
    matches = process.extract(text, loadedlist, scorer=fuzz.WRatio, limit=5)
    print(matches)

def best_matches(string, givenlist, cap = 1, justindex = False):
    matches_list = []
    for indx, musicname in enumerate(givenlist):
        music_lower = musicname.lower()
        str_input_lower = string.lower()

        score1 = fuzz.partial_ratio(str_input_lower, music_lower)
        score2 = fuzz.token_set_ratio(str_input_lower, music_lower)
        score3 = fuzz.token_sort_ratio(str_input_lower, music_lower)
        score4 = fuzz.partial_token_set_ratio(str_input_lower, music_lower)
        score5 = fuzz.WRatio(str_input_lower, music_lower)
        score6 = fuzz.ratio(str_input_lower, music_lower)

        score = (score1 + score2 + (2*score3) + score4 + score5 + score6)/7
        if music_lower.startswith(str_input_lower):
            score += 14.28
        matches_list.append((musicname.replace("\ufeff", ""), int(score), indx))
    matches_list.sort(key=lambda item: item[1], reverse=True)   
    #matches_list = matches_list[:cap]

    # print(matches_list)
    if not justindex:
        return matches_list
    elif justindex:
        resultindex = matches_list[0][2]
        return resultindex
            


def askget_music_number(loadedlist):
    while True:
        string_input = input("Choose song number:\n>")
        try:
            integer_input = (int(string_input) - 1)
            return integer_input
        except ValueError:
            return best_matches(string_input, loadedlist, 1, True)

            
        else:
            print("Dumbass, type a number")
            continue


#Manda o Pygame tocar a música e avisa o update()

#loadedlist = loaded_music_list


def show_list_and_play(loadedlist, folder):
    while True:
        showmusiclist(loadedlist)
        numberweget = askget_music_number(loadedlist)
        wannaplay = get_song_full_path(numberweget, loadedlist, folder)
        if wannaplay is not None:
            play_song(wannaplay, player_state)
            return
#Faz as quatro funções mais importantes do file_handler em sequência: Mostra a lista de músicas, obtém o caminho da
#música e manda o Pygame tocar, também verifica se o número que o usuário digitou é válido


loaded_music_list = load_music_list(sourcefolder)
show_list_and_play(loaded_music_list, sourcefolder)




def menu():
    global program_is_running
    while True:
        wannacontinue = input("What do you wanna do now?\nP = PLAY ANOTHER SONG\nL = LEAVE\n>")
        if wannacontinue.lower() == "l":
            program_is_running = False
            return
        elif wannacontinue.lower() == "p":
            show_list_and_play(loaded_music_list, sourcefolder)
            return
        else:
            continue  

def in_song_mode():
    ...

def counter(seconds):
    currenttime = time.monotonic()
    targettime = time.monotonic() + seconds
    


def deal_with_song_status():
    is_it_busy = pymusic.get_busy()
    check_key = check_key_and_return(player_state)
    state = check_state(player_state)

    if(state == "playing" and check_key == "pause"): #Spacebar
       pause_song(player_state)
    
    elif(state == "paused" and check_key == "unpause"): #Spacebar
       unpause_song(player_state) 
    
    elif(state in ("playing", "paused") and check_key == "stop"): #Música parando por comando do usuário
        print("Music Stopped.")
        stop_song(player_state)
        menu()
    
    elif(state == "playing" and not is_it_busy): #Música parou sozinha
        print("Song ended!")
        stop_song(player_state)
        menu()
    
    elif(state == "playing" and is_it_busy):
        in_song_mode()


        

#Checa o status da música e avisa se tiver acabado, também chama o cumpridor de comandos


def check_key_and_return(player_state):
    command = controller.command_detector()
    state = check_state(player_state)
   # print(command)
   # SPACEBAR
    if command == " ":
        if state == "playing":
            return "pause"
        elif state == "paused":
            return("unpause")
    elif command == "s":
            return("stop")


#def control_player():
  #  givencommand = check_key_and_return()

#TODO Ainda preciso fazer um tick mais preciso que esse

def realtick(initial_time):
    final_time = initial_time + FRAME_TIME
    current_time = time.monotonic()
    remaining = final_time - current_time

    if remaining > 0:
        time.sleep(remaining)
        

def tick():
    time.sleep(1 / FPS)
    #anda 1 frame


def update():
    deal_with_song_status()
    #atualiza tudo, chama o verificador


while program_is_running:
    thistime = time.monotonic()
    update()
    realtick(thistime)




    


