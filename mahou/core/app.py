from mahou.mahou_player import MahouPlayer
from mahou.core.ENUMS import PS
from mahou.user_interface.window import MahouInterface
from mahou_libs.time_functions import log_delta_time
from PySide6.QtWidgets import QApplication
from mahou.core.song_library import SongLibrary
import sys

class App:
    def __init__(self) -> None:
        self.state = PS.IN_MENU #DEFAULT STATE SET

        self.mahou_player = MahouPlayer(app = self) #player

        self.library = SongLibrary() #library
        folder = self.library.folder
        if folder is not None:
            self.library.set_song_list(folder) #song_list
        
        self.qt_app = QApplication(sys.argv) #qt app
        self.mahou_window = MahouInterface(player = self.mahou_player, app = self) #mainwindow
        self.mahou_window.show()

        
    def run(self):
        self.qt_app.exec()
        pass

    def set_state(self, state: PS) -> None:
        self.state = state

    
    
    
