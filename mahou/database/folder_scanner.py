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

    def scan_folder(self, folder: str | Path) -> list | None:
        """ Retorna o número de músicas analisadas
        """

        folder = Path(folder)
        if folder == Path(".") or not folder.is_dir():
            return

        songs = []
        for path in folder.iterdir():
            if path.is_file() and path.suffix.lower() in AUDIO_EXTENSIONS:
                song = self.database.get_or_create_song(song_path = path, commit = False) #esse método retorna songs
                if song is not None:
                    songs.append(song)
            
                
        self.database.commit()
        self.database.reset_song_map()

        return songs
        