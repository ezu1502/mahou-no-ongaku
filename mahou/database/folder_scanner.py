from pathlib import Path
from mahou.core.song import Song
from mahou.database.song_database import SongDatabase

class FolderScanner:
    def __init__(self, database:SongDatabase):
        self.database = database

    def scan_folder(self, folder: str | Path):
        folder = Path(folder)
        if folder == Path(".") or not folder.exists() or not folder.is_dir():
            return

        for path in folder.iterdir():
            if self.database.search_song_by_path(path = path) is None:
                #adicionar ao banco de dados

                # ! CONTINUAR DAQUI!!!
                ...
            
        