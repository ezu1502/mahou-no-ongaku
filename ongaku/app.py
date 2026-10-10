from ongaku.window import Window
from ongaku.database.database import Database
from ongaku.folder_scanner import scan_folder

from pathlib import Path

class App():
    def __init__(self):
        self.database = Database(app = self)
        self.window = Window(app = self)

    def run(self):
        self.database.initialize()
        self.window.run()

    def call_folder_scanner(self, folder_path: Path) -> dict[str, list[Path]] | None:
        return scan_folder(folder_path, self.database)
