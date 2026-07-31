from pathlib import Path
from mahou.database.song_database import SongDatabase

AUDIO_EXTENSIONS = {
    ".mp3",
    ".flac",
    ".wav",
    ".ogg",
    ".m4a",
    ".aac",
}

class FolderScanner:
    def __init__(self, database:SongDatabase):
        self.database = database

    def scan_folder(self, folder: str | Path):
        folder = Path(folder)
        if folder == Path(".") or not folder.is_dir():
            return

        for path in folder.iterdir():
            if path.is_file() and path.suffix.lower() in AUDIO_EXTENSIONS:
                self.database.insert_new_song(song_path = path, commit = False)

        self.database.commit()
        self.database.reset_song_map()
        