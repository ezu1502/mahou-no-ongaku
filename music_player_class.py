from pygame.mixer import music as pymusic
import os
import getpass 
import file_handler as Fhandler

class MusicPlayer:
# CONFIGURAÇÕES PADRÃO NO INIT
    def __init__(self):
        self.mode = "menu" #pode ser "playing", "paused", "menu", "stopped", "welcomescreen"
        self.welcome_was_shown = False
        self.paused_was_shown = False

        user = getpass.getuser()
        self.sourcefolder = rf"C:\Users\{user}\Mahou no Ongaku"


#NOVO STATE_HANDLER

    def set_state_playing(self):
        self.mode = "playing"

    def set_state_paused(self):
        self.mode = "paused"

    def set_state_stopped(self):
        self.mode = "stopped"

    def set_state_menu(self):
        pymusic.stop()
        self.mode = "menu"

    def set_state_killed(self):
        pymusic.stop()
        self.mode = "shut_down"
        
    def set_state_welcomescreen(self):
        self.mode = "welcomescreen"

    def check_state(self):
        return self.mode

#CONTROLES DA MÚSICA

    def play_song(self, path):
        self.paused_was_shown = False
        if self.mode != "playing":
            if path is None:
                print("Número inválido:")
                self.set_state_stopped()
                return
            
            pymusic.load(path)
            pymusic.play()

            justthename = os.path.basename(path)
            stylizedname = f"< {justthename} >"
            print("Now Playing: ", stylizedname)
            self.set_state_playing()
        

    def pause_song(self):
        if self.mode == "playing":
            pymusic.pause()
            self.set_state_paused()

    def unpause_song(self):
        self.paused_was_shown = False
        if self.mode == "paused":
            pymusic.unpause()
            print("Playing!")
            self.set_state_playing()

    def stop_song(self):
        if self.mode == "playing" or self.mode == "paused":
            pymusic.stop()
            self.set_state_stopped()

    def shut_program_down(self):
        if self.mode != "shut_down":
            pymusic.stop()
            self.set_state_killed()

    def check_welcome_was_shown(self):
        return self.welcome_was_shown
    def check_pause_was_shown(self):
        return self.pause_was_shown

#CONTROLES DA SOURCEFOLDER

    def set_sourcefolder(self, path):
        self.sourcefolder = path
        self.get_music_list(path)

    def get_music_list(self, folder): #folder no caso é o mesmo que o path
        self.song_list = Fhandler.turn_path_into_list(folder)

    







