from ongaku.ui.window import Window
from ongaku.database.database import Database
from ongaku.folder_scanner import scan_folder
from ongaku.list_model import ListModel, ListProxy
from ongaku.player import Player
from ongaku.enums import PlayerState as PS
from pathlib import Path

class App():
    def __init__(self):
        self.database = Database(app = self)

        self.list_model: ListModel = ListModel(app = self)
        self.list_proxy: ListProxy = ListProxy(model = self.list_model)

        self.window = Window(app = self)
        self.player = Player(app = self)

        self.state: PS = PS.MENU

    def set_state(self, state: PS) -> None:
        self.state = state

        self.window.backend.app_state_changed.emit()

    def run(self):
        self.database.initialize()
        self.window.run()

    def call_folder_scanner(self, folder_path: Path) -> dict[str, list[Path]] | None:
        return scan_folder(folder_path, self.database)

    def reload_list_model(self):
        self.list_model.reload()

    # region player controls

    def toggle(self, song_path: Path | None) -> None:
        if song_path is None:
            return

        match self.state:
            case PS.MENU:
                self.player.load_and_play(song_path)
                self.set_state(PS.PLAYING)
            case PS.PAUSED:
                self.player.unpause()
                self.set_state(PS.PLAYING)
            case PS.PLAYING:
                self.player.pause()
                self.set_state(PS.PAUSED)
    # endregion


    

