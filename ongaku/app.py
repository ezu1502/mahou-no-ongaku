from ongaku.window import Window
from ongaku.database.database import Database
from ongaku.folder_scanner import scan_folder
from ongaku.list_model import ListModel, ListProxy

from pathlib import Path

class App():
    def __init__(self):
        self.database = Database(app = self)

        self.list_model: ListModel = ListModel(app = self)
        self.list_proxy: ListProxy = ListProxy(model = self.list_model)

        self.window = Window(app = self)

    def run(self):
        self.database.initialize()
        self.window.run()

    def call_folder_scanner(self, folder_path: Path) -> dict[str, list[Path]] | None:
        return scan_folder(folder_path, self.database)

    def reload_list_model(self):
        self.list_model.reload()
