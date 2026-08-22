from mahou_libs.time_functions import TimeCounter
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
import sys
from pathlib import Path

from mahou.ui.python.backend import BackEnd

class UILauncher:
    def __init__(self):
        self.app = QGuiApplication(sys.argv)
        self.engine = QQmlApplicationEngine()
        self.backend = BackEnd()

    def launch(self):
        self.engine.rootContext().setContextProperty("backend", self.backend)
        self.qml_file = Path(__file__).parent.parent / "qml" / "window.qml"

        self.engine.load(self.qml_file)

        if not self.engine.rootObjects():
            sys.exit(-1)

        self.app.exec()

