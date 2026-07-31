from mahou.audio.player import MahouPlayer
from mahou.core.enums import PS, Paths
from mahou.user_interface.window import MahouInterface
from mahou_libs.time_functions import TimeCounter
from PySide6.QtWidgets import QApplication
from mahou.core.song_library import SongLibrary
import sys
import time
from mahou import file_manager as FM
from mahou.database.song_database import SongDatabase
from mahou.database.folder_scanner import FolderScanner

class App:
    @TimeCounter
    def __init__(self) -> None:
        self.state = PS.IN_MENU #DEFAULT STATE SET
        
        self.song_database = SongDatabase()
        self.song_database.initialize()

        self.folder_scanner = FolderScanner(database = self.song_database)

        self.library = SongLibrary(app = self) #library
        folder = self.library.folder

        if folder is not None:
            self.library.set_song_map(folder) #song_list
        
        self.qt_app = QApplication(sys.argv) #qt app
        self.player = MahouPlayer(app = self) #player
        self.mahou_window = MahouInterface(app = self) #mainwindow

        self.mahou_window.show()

      
        
    def run(self):
        self.qt_app.exec()
        pass

    def set_state(self, state: PS) -> None:
        self.state = state

    
    def set_library_folder(self, folder):
        self.library.set_folder(folder)
    

    def get_library_song_map(self):
        return self.library.song_map
    
    def get_song_from_id(self, id: str):
        return self.library.get_song_from_id(id)