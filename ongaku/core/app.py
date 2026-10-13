from ongaku.ui.window import Window
from ongaku.database.database import Database
from ongaku.core.folder_scanner import scan_folder
from ongaku.core.list_model import ListModel, ListProxy
from ongaku.core.player import Player
from ongaku.core.enums import PlayerState as PS
from pathlib import Path

class App():
    def __init__(self):
        self.database = Database(app = self)
        self.database.initialize()

        self.list_model: ListModel = ListModel(app = self)
        self.list_proxy: ListProxy = ListProxy(model = self.list_model)

        self.window = Window(app = self)
        self.player = Player(app = self)

        self.state: PS = PS.MENU

    def set_state(self, state: PS) -> None:
        self.state = state

        self.window.backend.app_state_changed.emit()

    def run(self):
        self.window.backend.connect_signals() # * Connects backend's signals, preventing it from referencing Player before it initializes
        self.window.run()
        

    def call_folder_scanner(self, folder_path: Path) -> dict[str, list[Path]] | None:
        return scan_folder(folder_path, self.database)

    def reload_list_model(self):
        self.list_model.reload()

    # region player controls

    def get_loaded_path(self) -> Path | None:
        return self.player.loaded_path

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

    def change_song(self, delta: int) -> None:
        if delta not in (-1, 1):
            return
        
        playing_path: Path | None = self.get_loaded_path()
        if playing_path is None:
            return
        
        row_count = self.list_proxy.rowCount()
        if row_count == 0: 
            return
       
        playing_row: int = self.list_proxy.find_song_row(playing_path)
        if playing_row < 0:
            return

        new_row: int = (playing_row + delta) % row_count

        new_path: Path | None = self.list_proxy.find_song_path(row = new_row)
        if new_path is None:
            return

        match self.state:
            case PS.PAUSED:
                self.player.load_path(new_path)
            case PS.PLAYING:
                self.player.load_and_play(new_path)
            
    def restart_song(self) -> None:
        self.player.set_position(0)

    # endregion


    

