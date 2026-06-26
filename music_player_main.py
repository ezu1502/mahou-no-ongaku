import time
import os
import getpass 
import pygame
import player_controls as controller
from file_handler import load_music_list, showmusiclist, get_song_full_path
#import Player Controller


program_is_running = True
FPS = 60

user = getpass.getuser()
sourcefolder = rf"C:\Users\{user}\Mahou no Ongaku"
#define a pasta a ser usada e descobre o nome do usuário ativo

pygame.mixer.init()


now_playing = False
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
    global now_playing

    if path is None:
        print("Número inválido:")
        return
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    justthename = os.path.basename(path)
    stylizedname = f"< {justthename} >"
    print("Now Playing: ", stylizedname)
    now_playing = True
   
       
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

def ask_leave_or_play_new_song():
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


def tick():
    time.sleep(1 / FPS)
    #anda 1 frame

def deal_with_song_status():
    global now_playing
    global is_it_paused
    is_it_busy = pygame.mixer.music.get_busy()
    #reallyplaying = pygame.mixer.music.get_busy()
#pygame.mixer.music.
    check_key = check_key_and_return()
    if check_key == "pause":
        is_it_paused = True
    if check_key == "unpause":
        is_it_paused = False
    if check_key == "stop":
        ask_leave_or_play_new_song()


#BUG AQUI!!!!

    if(now_playing and not is_it_paused):
        pygame.mixer.music.pause()

    elif(now_playing and is_it_paused):
        pygame.mixer.music.unpause()
    elif(now_playing and not is_it_busy and not is_it_paused):
        print("Cabou a música kkkkkkkk")
        now_playing = False
        ask_leave_or_play_new_song()
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

         




def update():
    deal_with_song_status()
    #atualiza tudo, chama o verificador


while program_is_running:
    update()
    tick()



   