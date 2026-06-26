import time
import os
import getpass 
import pygame
from pygame.mixer import music as pymusic
import keyboardreceiver as controller
from file_handler import load_music_list, showmusiclist, get_song_full_path
#import Player Controller


program_is_running = True
FPS = 60

user = getpass.getuser()
sourcefolder = rf"C:\Users\{user}\Mahou no Ongaku"
#define a pasta a ser usada e descobre o nome do usuário ativo

pygame.mixer.init()


should_be_playing = False
is_it_paused = False

# IMPORT + VARIÁVEIS INICIAIS + PYGAME INIT

def askget_music_number():
    while True:
        try:
            chosenmusicnumber = int(input("Choose song number:\n>")) - 1
            return chosenmusicnumber
        except ValueError:
            print("Dumbass, type a number")
            continue


def play_song(path):
    global should_be_playing

    if path is None:
        print("Número inválido:")
        return
    pymusic.load(path)
    pymusic.play()
    justthename = os.path.basename(path)
    stylizedname = f"< {justthename} >"
    print("Now Playing: ", stylizedname)
    should_be_playing = True
   
       
#Manda o Pygame tocar a música e avisa o update()

#loadedlist = loaded_music_list


def show_list_and_play(loadedlist, folder):
    while True:
        showmusiclist(loadedlist)
        numberweget = askget_music_number()
        wannaplay = get_song_full_path(numberweget, loadedlist, folder)
        if wannaplay is not None:
            play_song(wannaplay)
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




def pause_song():
    global is_it_paused
    pymusic.pause()
    is_it_paused = True

def unpause_song():
    global is_it_paused
    pymusic.unpause()
    is_it_paused = False
def stop_song():
    global is_it_paused
    global should_be_playing
    pymusic.stop()
    should_be_playing = False
    is_it_paused = False

def deal_with_song_status():
    global should_be_playing
    global is_it_paused
    is_it_busy = pymusic.get_busy()
    check_key = check_key_and_return()

    if(should_be_playing and check_key == "pause"): #Spacebar
       pause_song()
    elif(should_be_playing and check_key == "unpause"): #Spacebar
       unpause_song() 
    elif(should_be_playing and check_key == "stop"): #Música parando por comando do usuário
        print("Music Stopped.")
        stop_song()
        menu()
    elif(should_be_playing and not is_it_busy and not is_it_paused): #Música parou sozinha
        print("Song ended!")
        stop_song()
        menu()
        

#Checa o status da música e avisa se tiver acabado, também chama o cumpridor de comandos


def check_key_and_return():
    command = controller.command_detector()
   # print(command)
   # SPACEBAR
    if command == " ":
        if not is_it_paused:
            return "pause"
        elif is_it_paused:
            return("unpause")
    elif command == "s":
            return("stop")


#def control_player():
  #  givencommand = check_key_and_return()

         

def tick():
    time.sleep(1 / FPS)
    #anda 1 frame


def update():
    deal_with_song_status()
    #atualiza tudo, chama o verificador


while program_is_running:
    update()
    tick()



   