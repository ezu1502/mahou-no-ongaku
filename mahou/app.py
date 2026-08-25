from mahou.ui.window import MahouWindow
from mahou.database.song_database import SongDatabase
from mahou.ui.song_model import SongModel, SongProxy
from mahou.folder_scanner import scan_folder
from pathlib import Path

class App:
    def __init__(self) -> None:
        self.database = SongDatabase(app = self)
        self.window = MahouWindow(app = self)
        self.song_model = SongModel(database = self.database)
        self.song_proxy = SongProxy(model = self.song_model)
        
        
    def run(self):
        self.database.initialize()
        self.song_model.initialize()
        self.window.launch()

       

    
    def call_folder_scanner(self, folder_path: Path):
        result = scan_folder(database = self.database, folder = folder_path)

        if result is None:
            print("Folder Scanner failed")
            return

        print(f"Folder Scanner scanned {result} files")