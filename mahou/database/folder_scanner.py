from pathlib import Path
from mahou.database.song_database import SongDatabase
from mutagen import File, MutagenError
from mutagen.id3 import ID3
from enum import Enum
AUDIO_EXTENSIONS = {
    ".mp3",
    ".flac",
    ".wav",
    ".ogg",
    ".m4a",
    ".aac",
}

class Tags:
    class MP3(Enum):
        TITLE = "TIT2"
        ARTIST = "TPE1"
        ALBUM = "TALB"
        DATE = "TDRC"
        GENRE = "TCON"
        TRACK_NUMBER = "TRCK"   






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

    def scan_metadata(self, song_path: Path):
        try:
            id3_tags = ID3(song_path)
        except MutagenError:
            return {}


        loaded_tags = {}
        
        for tag_type in Tags.MP3:
            tag = id3_tags.get(tag_type.value)

            if tag is None:
                loaded_tags[tag_type.name] = "None"
                continue

            loaded_tags[tag_type.name] = tag.text[0]
    
        