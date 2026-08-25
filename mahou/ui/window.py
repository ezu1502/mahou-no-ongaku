from __future__ import annotations

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Property, Slot, QUrl, Signal
import sys
from pathlib import Path
from typing import TYPE_CHECKING
from mahou.core.enums import PlayerState as PS

if TYPE_CHECKING:
    from mahou.core.app import App



class BackEnd(QObject):

    stateChanged = Signal()

    def __init__(self, window: MahouWindow):
        super().__init__()

        self.window = window
        self.app = self.window.app

    @Slot(QUrl)
    def receive_folder(self, folder: QUrl):
        """ Manda o app chamar o folder_scanner na pasta recebida pelo FolderDialog """
        folder_path = folder.toLocalFile()

        if not folder_path:
            return

        folder_path = Path(folder_path)

        self.app.call_folder_scanner(folder_path = folder_path)

    @Slot(str)
    def select_song(self, song_path: str):
        """ Vai receber o caminho da música do proxy por meio do QML, converte pro formato Path e avisa
        que a current_selection mudou
        """

        true_path = Path(song_path)

        self.window.selected_path = true_path

        print(true_path)

    @Slot()
    def play_button(self):
        self.window.play_button()

    @Property(str, notify = stateChanged)
    def state(self):
        return self.window.state




class MahouWindow:
    def __init__(self, app: App):
        self.app = app
        
        self.qml_app = QGuiApplication(sys.argv)
        self.engine = QQmlApplicationEngine()
        self.backend = BackEnd(window = self)

        self.qml_file = Path(__file__).parent / "qml" / "MainWindow.qml"

        self.state: PS = PS.MENU
        self.selected_path: None | Path = None
        self.playing_path: None | Path = None

    def launch(self):
        self.engine.rootContext().setContextProperty("backend", self.backend)
        self.engine.rootContext().setContextProperty("song_proxy", self.app.song_proxy)

        self.engine.load(self.qml_file)

        if not self.engine.rootObjects():
            sys.exit(-1)

        self.qml_app.exec()

    def play_button(self):
        if self.selected_path is None:
            return
        
        self.app.player.load_and_play(self.selected_path)
        self.playing_path = self.selected_path
        self.selected_path = None

    def set_state(self, state: PS) -> None:
        self.state = state




        








