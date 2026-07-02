import tkinter as tk
import os

class MahouListBox(tk.Listbox):
    def __init__(self, parent, pack_config = None, **listbox_config):

        default_config = {
            "font": ("Segoe UI", 12),
            # "bg": parent.cget("bg") or "#000000",
            "bg": "#2E2E2E",
            "fg": "#ffffff",
            "selectbackground": "#616161",
            "selectforeground": "#ffffff",
            "width": 70,
            "height": 14,
            "highlightthickness": 0,
            "borderwidth": 0,
            "activestyle": "none"
        }

        chosen_config = default_config.copy()
        chosen_config.update(listbox_config)


        super().__init__(
            parent,
            **chosen_config
        )

        if pack_config is None:
            pack_config = {}

        self.pack(**pack_config)
        self.pathlist = []

    def add_item(self, item):
        self.insert("end", item)

    def clear_self(self):
        self.delete(0, "end")
        self.pathlist.clear()

    def get_selected(self, path_only = False):
        selection = self.curselection()
        if selection:
            index = selection[0]
            name_and_path = (self.get(index), self.pathlist[index])
            just_path = self.pathlist[index]
            return name_and_path if not path_only else just_path
        return None
    
    def add_list(self, wanted_list, folder_path):
        print("oi")
        
        for indx, name in enumerate(wanted_list, start = 1):
            final_name = f"{indx} - {name}"
            
            song_path = os.path.join(folder_path, name)

            self.add_item(final_name)
            self.pathlist.append(song_path)

    def callback_path_list(self):
        return self.pathlist

        








# insert()      adiciona item
# delete()      remove item
# get()         pega item
# curselection() vê qual foi selecionado




