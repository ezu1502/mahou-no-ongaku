import tkinter as tk
from ..widget_classes_folder import MahouButton, MahouLabel, MahouListBox
from tkinter import filedialog as explorer

class MenuScreen(tk.Frame):
    def __init__(self, parent, change_folder_function, play_function):
        super().__init__(
            parent,
            bg = "#111111"
        )
        
        self.mode = "none yet"
        self.play_function = play_function

        self.title_label = MahouLabel(self, "Mahou no Ongaku")

        self.play_button = MahouButton(self, "▶ Play", self.play_function)

        self.change_folder_function = change_folder_function

        self.choose_folder_button = MahouButton(
            
            self,
            "Choose Music Folder",
            self.call_explorer_and_choose_folder,
            pack_config = {"pady": 20}
            
            )
        

        self.play_command = False
        self.musiclist = MahouListBox(self)
        self.musiclist.insert("end", "TESTE")
        self.musiclist.bind("<<ListboxSelect>>", self.print_selected_path)
        

    def play_button_pressed(self):
        self.play_command = True

        
    def call_explorer_and_choose_folder(self):
        folder_path = explorer.askdirectory()
        if folder_path:
            self.change_folder_function(folder_path)
            
            self.testlabel = MahouLabel(self, f"{folder_path}")
        
    def set_music_list(self, music_list, folder_path):
        self.musiclist.clear_self()
        self.musiclist.add_list(music_list, folder_path)


    def callback_path_list(self):
        return self.musiclist.pathlist

    def callback_get_selected(self, path_only = False):
        return self.musiclist.get_selected(path_only)
    
    def print_selected_path(self, path_only = False):
        selected_path = self.callback_get_selected(path_only)
        print(selected_path)
        return selected_path if selected_path is not None else None
    
    def set_play_button_mode(self, mode):
        self.mode = mode
        if mode == "playing":
            self.play_button.config(text = "❚❚ PAUSE")
        elif mode == "paused":
            self.play_button.config(text = "▶ Play")



