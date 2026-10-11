from __future__ import annotations
import sys
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ongaku.app import App
    from ongaku.list_model import ListProxy

from PySide6.QtCore import QUrl, QObject, Slot
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtGui import QGuiApplication, QFontDatabase

class BackEnd(QObject):
    def __init__(self, window: Window):
        super().__init__()

        self.window = window

    @Slot(QUrl)
    def receive_folder(self, folder_qurl: QUrl) -> None:
        """
            Receives folderDialog's QUrl to chosen folder's path. Converts it into a Path object and
            updates the window's folder 
        """
        folder_path = Path(folder_qurl.toLocalFile())

        if folder_path.is_dir():
            self.window.call_folder_scanner(folder_path)

class Window:
    def __init__(self, app: App) -> None:
        self.app: App = app
        self.gui_app = QGuiApplication(sys.argv)
        self.engine = QQmlApplicationEngine()

        self.backend = BackEnd(window = self)

        self.qml_path = Path(__file__).parent / "qml" / "main.qml"

        self.proxy: ListProxy = self.app.list_proxy

    def load_fonts(self) -> None:
        fonts_dir: Path = Path(__file__).parent / "fonts"

        outfit_path: Path =  fonts_dir / "Outfit" / "Outfit-VariableFont_wght.ttf"
        noto_sans_path: Path = fonts_dir / "Noto_Sans" / "NotoSans-VariableFont_wdth,wght.ttf"

        outfit_id = QFontDatabase.addApplicationFont(str(outfit_path))
        noto_sans_id = QFontDatabase.addApplicationFont(str(noto_sans_path))

        if outfit_id == -1:
            raise RuntimeError("Couldn't load Outfit")

        if noto_sans_id == -1:
            raise RuntimeError("Couldn't load Noto_Sans")

    def run(self) -> int:
        self.load_fonts()

        self.engine.rootContext().setContextProperty("backend", self.backend)
        self.engine.rootContext().setContextProperty("proxy", self.proxy)

        self.engine.load(QUrl.fromLocalFile(str(self.qml_path)))

        if not self.engine.rootObjects():
            return -1
        
        return self.gui_app.exec()

    def call_folder_scanner(self, folder: Path) -> None:
        """
            Receives a folder path, calls App's folder scanner, which communicates with the database and
            returns the result.
        """
        result = self.app.call_folder_scanner(folder)

        if result is not None:
            self.app.reload_list_model()


        print(result)
        # TODO Devo fazer alguma coisa com esse resultado depois. Por enquanto fica só assim




# TODO CONTINUAR DAQUI! ListModel e ListProxy criados, falta usar eles na ListView do QML!