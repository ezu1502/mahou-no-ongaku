
import os

#FILE HANDLER


def load_music_list(folder):
    music_files_list = []

    files = os.listdir(folder)

    for eachfile in files:
        if eachfile.lower().endswith(".mp3"):
            
            music_files_list.append(eachfile)  
    music_files_list.sort(key=lambda name: name.lstrip("\ufeff").strip().lower())
    
    return music_files_list



#load_music_list() transforma a pasta escolhida em uma lista, eliminando os arquivos que não são .mp3
# e retorna essa lista. printmusiclist() printa no terminal cada nome de arquivo junto com um número no formato:
# Número, Nome.mp3



#Executando load e print na nossa pasta escolhida sourcefolder, atribuindo a lista a uma variável global loaded_...

# PREPARANDO OS ARQUIVOS
def showmusiclist(chosenlist):
    for indx, musicname in enumerate(chosenlist):
        print(indx + 1, " ", (musicname))


#Pega o input do usuário e retorna ele -1 pra usarmos na arraylist

def get_song_full_path(musicnumber, loadedmusiclist, folder):
    listlength = len(loadedmusiclist)
    if musicnumber < 0 or musicnumber >= listlength:
        print("Please choose a number between 1 and ", listlength)
        return None
    
    song_name = loadedmusiclist[musicnumber]
    #print(song_name)
    fullsongpath = os.path.join(folder, song_name)
    #print(fullsongpath)
    return fullsongpath
            
        
#Retorna o caminho da música baseado no numero que receber