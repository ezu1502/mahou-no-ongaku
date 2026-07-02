import tkinter as tk
import os
from .widget_classes_folder.button_class import MahouButton
from .screens_folder.menu_screen import MenuScreen



class MahouWindow:

    def __init__(self, player, dimensions = "600x600"):
        self.player = player

        self.root = tk.Tk()
        self.root.title("Mahou no Ongaku - True Music Player")

        calculate_centered_geometry = self.center_window(dimensions)

        self.root.geometry(calculate_centered_geometry)
        self.root.resizable(False, False)

        self.root.protocol("WM_DELETE_WINDOW", self.Xpressed)

        self.current_screen = "menu_screen"

        self.detected_folder = None

        self.in_menu()
        this_pathlist = self.callback_path_list()

        self.selected_path = self.callback_get_selected()
        

        if self.play_button_was_pressed():
            self.player.play_song(self.selected_path)



        # self.test_button = tk.Button(self.root, text = "Text Button", command = self.test_button_pressed)
        # self.test_button.pack(pady = 30) 

    
    def run(self):
        self.root.mainloop()
    def Xpressed(self):
        self.player.shut_program_down()
        self.root.destroy()
        # os._exit(0)

    def in_menu(self):
        self.menu = MenuScreen(self.root, change_folder_function = self.set_folder, play_function = self.play_selected_song)

        self.menu.pack(fill = "both", expand = True)

    def center_window(self, dimensions):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width, window_height = dimensions.split("x")
        window_width, window_height = int(window_width), int(window_height)
        

        x = (screen_width//2) - (window_width//2)
        y = (screen_height//2) - (window_height//2)
        position_and_dimensions = f"{dimensions}+{x}+{y}"
        return position_and_dimensions
    



    
    def set_folder(self, path):
        self.player.set_sourcefolder(path)

    def set_music_list(self, musiclist, folder_path):
        self.menu.set_music_list(musiclist, folder_path)

    def callback_path_list(self):
        return self.menu.callback_get_selected()

    def callback_get_selected(self):
        path = self.menu.callback_get_selected(path_only = True)
        print(path) if path is not None else ""
        return path if path is not None else None


    def play_button_was_pressed(self):
        return self.menu.play_command
         
    def play_button_status(self):
        return self.menu.mode
    
    def play_selected_song(self):
        # self.menu.mode = self.play_button_status()
        if self.menu.mode == "none yet":
            path = self.menu.callback_get_selected(path_only = True)
            if path is not None:
                self.player.play_song(path)
                self.menu.set_play_button_mode("playing")
        elif self.menu.mode == "paused":
            self.player.unpause_song()
            self.menu.set_play_button_mode("playing")
        elif self.menu.mode == "playing":
            self.player.pause_song()
            self.menu.set_play_button_mode("paused")

            #TODO organizar lógica e arrumar a bagunça
   