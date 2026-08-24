from __future__ import annotations

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Property, Slot, QUrl
import sys
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mahou.app import App

class BackEnd(QObject):
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


class MahouWindow:
    def __init__(self, app: App):
        self.app = app
        
        self.qml_app = QGuiApplication(sys.argv)
        self.engine = QQmlApplicationEngine()
        self.backend = BackEnd(window = self)

        self.qml_file = Path(__file__).parent / "qml" / "MainWindow.qml"

    def launch(self):
        self.engine.rootContext().setContextProperty("backend", self.backend)
        self.engine.rootContext().setContextProperty("song_proxy", self.app.song_proxy)

        self.engine.load(self.qml_file)

        if not self.engine.rootObjects():
            sys.exit(-1)

        self.qml_app.exec()






