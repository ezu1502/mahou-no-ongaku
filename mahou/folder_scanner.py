from __future__ import annotations
from pathlib import Path
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from mahou.database.song_database import SongDatabase

ALLOWED_EXTENSIONS = [".mp3", ".m4a", ".wav", ".flac", ".ogg"]

def scan_folder(database: SongDatabase, folder: Path) -> int | None:
    if not folder.is_dir():
        print("Invalid folder path")
        return None  

    files_scanned = 0
    
    for song_path in folder.iterdir():
        if song_path.suffix.lower() in ALLOWED_EXTENSIONS:
            database.insert_song_path(song_path, commit = False)
            files_scanned += 1


    database.commit()

    return files_scanned


    # TODO decidir oq fazer com subpastas


