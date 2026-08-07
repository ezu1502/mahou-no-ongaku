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
from mahou.user_interface.components.song_list_model import SongListModel, SongProxyModel

class App:
    @TimeCounter
    def __init__(self) -> None:

        with TimeCounter("Basic variables created"):
            self.state = PS.IN_MENU #DEFAULT STATE SET
            
            self.song_database = SongDatabase()
            self.song_database.initialize()

            self.list_model = SongListModel(self.song_database)
            self.proxy_model = SongProxyModel(self.list_model)

            self.folder_scanner = FolderScanner(database = self.song_database)


        with TimeCounter("Qt_app + Player + Window"):
            self.qt_app = QApplication(sys.argv) #qt app

            self.player = MahouPlayer(app = self) #player
            self.player.listening_time_signal.connect(self.handle_listening_time)

            self.mahou_window = MahouInterface(app = self) #mainwindow
            with TimeCounter("window_show"):
                self.mahou_window.show()
                



    def handle_listening_time(self, song_id: int, listening_time: float):
        if listening_time >= 30:
            self.song_database.increment_song_play_count(song_id)

        self.song_database.update_song_listen_time(song_id, listening_time)
        


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

    def set_stylesheet(self, stylesheet_string):
        self.qt_app.setStyleSheet(stylesheet_string)


    def get_list_model(self) -> SongListModel:
        return self.list_model

    def get_proxy_model(self) -> SongProxyModel:
        return self.proxy_model