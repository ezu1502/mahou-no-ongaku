from mahou.audio.player import MahouPlayer
from mahou.core.enums import PS, Paths
from mahou.user_interface.window import MahouInterface
from mahou_libs.time_functions import TimeCounter
from PySide6.QtWidgets import QApplication
import sys
from mahou import file_manager as FM
from mahou.database.song_database import SongDatabase
from mahou.database.folder_scanner import FolderScanner
from pathlib import Path

class App:
    @TimeCounter
    def __init__(self) -> None:
        self.state = PS.IN_MENU #DEFAULT STATE SET
        
        self.song_database = SongDatabase()
        self.song_database.initialize()

        self.folder_scanner = FolderScanner(database = self.song_database)

        self.qt_app = QApplication(sys.argv) #qt app
        self.player = MahouPlayer(app = self) #player
        self.mahou_window = MahouInterface(app = self) #mainwindow

        self.mahou_window.show()

      
        
    def run(self):
        self.qt_app.exec()
        pass

    def set_state(self, state: PS) -> None:
        self.state = state

    def scan_folder(self, folder: Path):
        return self.folder_scanner.scan_folder(folder)
    
    def get_song_from_id(self, id: str):
        # ! REFAZER
        ...

    @property
    def song_map(self):
        return self.song_database.song_map

