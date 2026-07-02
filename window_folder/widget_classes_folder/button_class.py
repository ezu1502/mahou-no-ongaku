import tkinter as tk



class MahouButton(tk.Button):
    def __init__(self, parent, text, command, pack_config = None, **button_config):
        default_config = {
            "font": ("Segoe UI", 14),
            "width": 20,
            "height": 2,
            "bg": "#222222",
            "fg": "#ffffff",
            "activebackground": "#333333",
            "activeforeground": "#ffffff"
        }
        
        chosen_config = default_config.copy()
        chosen_config.update(button_config)
        
        
        
        super().__init__(
            parent,
            text = text,
            command = command,
            **chosen_config
        )


        if pack_config is None:
            pack_config = {}

        self.pack(**pack_config)



