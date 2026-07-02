import tkinter as tk

class MahouLabel(tk.Label):
    def __init__(self, parent, text, pack_config = None, **label_config):
        default_config = {
            "font": ("Segoe UI", 12),
            "bg": parent.cget("bg") or "#000000",
            "fg": "#ffffff",
            "anchor": "center",
            "justify": "center",
            "wraplength": 400
        }

        chosen_config = default_config.copy()

        chosen_config.update(label_config)

        super().__init__(
            parent,
            text = text,
            **chosen_config
        )

        if pack_config is None:
            pack_config = {}

        self.pack(**pack_config)





