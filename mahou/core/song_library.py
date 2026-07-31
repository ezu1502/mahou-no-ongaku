from pathlib import Path
from mahou_libs.colors import COLORS, painted_string
from mahou.core.song import Song
from send2trash import send2trash
import json
from mahou_libs.bocca import BoccaFiglia
from mahou.core.enums import Paths
from mahou import file_manager
from mahou_libs.time_functions import TimeCounter
import random
import string

log = BoccaFiglia("song_library", "#FF0000")

class SongLibrary:
    def __init__(self, app) -> None:
        self.folder: Path | None = None

        self.app = app

        self.song_map: dict[str, Song] = {}

        default_folder = self.default_folder
        if default_folder is not None and default_folder != Path("."):
            self.set_folder(default_folder)

    @property
    def default_folder(self):
        options_dict = file_manager.read_file(Paths.SETTINGS_FILE)

        folder = options_dict.get("default_folder", None)

        return Path(folder) if folder is not None else None
            
    def save_folder(self, folder):
        folder = str(folder)

        file_manager.save_setting(folder, "default_folder")

    @TimeCounter
    def set_folder(self, folder: Path) -> None:
        if folder is None:
            log.warning("Exception: path is null")
            return None
        
        self.folder = folder
        self.set_song_map(folder)
        self.save_folder(folder) 

    def set_song_map(self, folder: Path):
        self.song_map = {}

        supported_formats = {".mp3", ".wav", ".ogg", ".m4a", ".flac"}

        for file_path in folder.iterdir():
            if file_path.is_file() and file_path.suffix.lower() in supported_formats:

                song_id = self.make_song_id()
                self.song_map[song_id] = Song(path = file_path, id = song_id)
           
        log.debug("song list set")


    def make_song_id(self):
        possible_chars = string.ascii_letters + string.digits

        def roll_random_ids():
            choices = random.choices(possible_chars, k = 8)
            return  "".join(choices)

        random_id = roll_random_ids()
        
        while random_id in self.song_map:
            random_id = roll_random_ids()

        song_id = random_id

        return song_id

    def get_song_from_id(self, id: str) -> Song | None:
        return self.song_map.get(id, None)


