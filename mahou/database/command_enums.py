from enum import Enum, StrEnum
from pathlib import Path

class GeneralCommands(StrEnum):
    CREATE_TABLE = "create_table.sql"

class SongCommands(StrEnum):
    SEARCH_ID = "search_song_id.sql"
    SEARCH_PATH = "search_song_path.sql"

    CHECK_EXISTS = "check_song_exists.sql"
    INSERT_SONG = "insert_song.sql"
    SELECT_ALL = "select_all_songs.sql"