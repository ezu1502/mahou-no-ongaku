import tkinter as tk

class MahouWindow:

    def __init__(self, player, dimensions = "600x600"):
        self.player = player

        self.root = tk.Tk()
        self.root.title("Mahou no Ongaku - True Music Player")
        self.root.geometry(dimensions)
        self.root.resizable(False, False)

        self.title_label = tk.Label(self.root, text = "Mahou no Ongaku")
        self.title_label.pack(pady = 20)

        self.status_label = tk.Label(self.root, text = "Status: Ready")
        self.status_label.pack(pady = 10)
        
        self.testpath = r"C:\Users\dudul\Mahou no Ongaku\0 - ﻿Ado.mp3"
        self.test_button = tk.Button(self.root, text = "Text Button", command=lambda: self.player.play_song(self.testpath))
        self.test_button.pack(pady = 30) 

    def test_button_pressed(self):
        self.status_label.config(text = "Status: Button Pressed")
    def run(self):
        self.root.mainloop()














