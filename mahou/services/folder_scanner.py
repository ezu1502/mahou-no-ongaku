from __future__ import annotations
import mutagen
from mutagen.mp3 import EasyMP3
import json
from pathlib import Path
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from mahou.database.song_database import SongDatabase

ALLOWED_EXTENSIONS = [".mp3", ".m4a", ".wav", ".flac", ".ogg"]

def scan_metadata(song_path: Path) -> str | None:
    match song_path.suffix.lower():
        case ".mp3":
            audio = EasyMP3(song_path)


            artist = audio.get("artist")
            album = audio.get("album")
            title = audio.get("title")

            result = {
                "artist": artist[0] if artist else None,
                "album": album[0] if album else None,
            }
        case _:
            result = None

    return json.dumps(result, ensure_ascii = False) if result is not None else None

def scan_folder(database: SongDatabase, folder: Path) -> int | None:
    if not folder.is_dir():
        print("Invalid folder path")
        return None  

    files_scanned = 0
    
    for song_path in folder.iterdir():
        if song_path.suffix.lower() in ALLOWED_EXTENSIONS:
            metadata = scan_metadata(song_path)

            database.insert_song_path(song_path, metadata, commit = False)
            files_scanned += 1


    database.commit()

    return files_scanned


    # TODO decidir oq fazer com subpastas






