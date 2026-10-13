from __future__ import annotations
from typing import TYPE_CHECKING
from pathlib import Path
import mutagen

if TYPE_CHECKING:
    from ongaku.database.database import Database

EXTENSIONS: set[str] = {
    ".mp3",
    ".m4a",
    ".flac",
    ".wav",
    ".ogg",
    ".aac",
    ".opus",
    ".aiff",
    ".aif"
}

def get_song_metadata(song_path: Path) -> dict[str, str | None]:
    try:
        audio = mutagen.File(song_path, easy = True)

    except (mutagen.MutagenError, OSError):
        return {}

    if audio is None or audio.tags is None:
        return {}

    def find(tag: str):
        return audio.tags.get(tag, [None])[0]

    return {
        "artist": find("artist"),
        "album": find("album"),
        "date": find("date"),
        "tracknumber": find("tracknumber")
    }


def scan_folder(folder: Path, database: Database) -> dict[str, list[Path]] | None:
    """
        Receives a folder path and a database object. Scans through the folder and inserts each valid
        song path into the database.

        Returns a dict containing stats about the files scanned or None, in case of invalid folderpath.
    """

    discovered_files: list[Path] = []
    successful_files: list[Path] = []
    failed_files: list[Path] = []

    if not folder.is_dir():
        return

    for file_path in folder.iterdir():
        if not file_path.is_file():
            continue

        discovered_files.append(file_path)

        if file_path.suffix.lower() not in EXTENSIONS:
            failed_files.append(file_path)
            continue

        metadata: dict = get_song_metadata(file_path)

        result = database.insert_song(file_path, metadata)

        if result:
            successful_files.append(file_path)
        else:
            failed_files.append(file_path)

    return {
        "discovered_files": discovered_files,
        "successful_files": successful_files,
        "failed_files": failed_files
    }



    